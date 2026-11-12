#!/usr/bin/env python3
"""Stage 8M: explicit Sky Catalyst Eevee evolution, with real progression gates.

Eevee -> Aerieon: use Sky Catalyst at level >= 15.
Aerieon -> Aerartheon: use Sky Catalyst at level >= 38 with six Hoenn badges.
No automatic custom level-up evolutions. All eight canonical Eevee evolutions
retain their original behavior. Sky Catalyst is sold in the expanded Oldale Mart.
Existing species and item IDs are preserved; one new item ID is appended (874).
"""
from pathlib import Path
import argparse
import re

STAGE = "STAGE8M"
PRESERVE = (
    "SPECIES_JOLTEON", "SPECIES_VAPOREON", "SPECIES_FLAREON",
    "SPECIES_SYLVEON", "SPECIES_ESPEON", "SPECIES_UMBREON",
    "SPECIES_LEAFEON", "SPECIES_GLACEON",
)

def replace_exact(original, old, new, description):
    count = original.count(old)
    if count != 1:
        raise ValueError(f"{description}: expected one anchor, found {count}")
    return original.replace(old, new, 1)

def patch(checkout: Path):
    root = checkout.resolve()
    if not (root / "Makefile").is_file():
        raise ValueError("Not a pokeemerald-expansion checkout")

    files = {
        "evo_enum": root / "include/constants/pokemon.h",
        "evo_code": root / "src/pokemon.c",
        "items_enum": root / "include/constants/items.h",
        "items_data": root / "src/data/items.h",
        "eevee": root / "src/data/pokemon/species_info/gen_1_families.h",
        "custom": root / "src/data/pokemon/species_info.h",
        "shop": root / "data/maps/OldaleTown_Mart/scripts.inc",
    }
    old = {key: path.read_text(encoding="utf-8") for key, path in files.items()}
    if any(STAGE in content for content in old.values()):
        raise ValueError("Stage 8M already applied; refusing double patch")
    new = dict(old)

    # Explicit numeric ID, appended after current upstream 873, avoids shifting
    # existing item IDs and fails closed if the engine enum is reorganized.
    new["items_enum"] = replace_exact(
        old["items_enum"],
        "    ITEM_GLIMMORANITE = 873,\n\n    ITEMS_COUNT,",
        "    ITEM_GLIMMORANITE = 873,\n"
        "    ITEM_SKY_CATALYST = 874, // STAGE8M: custom evolution item\n\n"
        "    ITEMS_COUNT,",
        "item ID anchor",
    )
    if old["items_data"].count("[ITEM_SKY_CATALYST]") != 0:
        raise ValueError("Sky Catalyst item already exists")
    item = """
    [ITEM_SKY_CATALYST] = // STAGE8M: initial dedicated evolution catalyst
    {
        .name = ITEM_NAME("Sky Catalyst"),
        .price = 3000,
        .description = COMPOUND_STRING(
            "A special stone that\\n"
            "awakens skyward\\n"
            "Eevee evolutions."),
        .pocket = POCKET_ITEMS,
        .sortType = ITEM_TYPE_EVOLUTION_STONE,
        .type = ITEM_USE_PARTY_MENU,
        .fieldUseFunc = ItemUseOutOfBattle_EvolutionStone,
        .effect = gItemEffect_EvoItem,
        .flingPower = 80,
        .iconPic = gItemIcon_DawnStone, // provisional artwork, no new sprite assets
        .iconPalette = gItemIconPalette_DawnStone,
    },
"""
    new["items_data"] = replace_exact(
        old["items_data"], "\n};\n\n#undef ITEM_NAME",
        item + "\n};\n\n#undef ITEM_NAME", "item data array end",
    )

    # Add two new evolution predicates *before* CONDITIONS_END, so existing
    # values keep their ordinal IDs in the engine.
    new["evo_enum"] = replace_exact(
        old["evo_enum"],
        "    CONDITIONS_END\n};",
        "    IF_MIN_LEVEL,                       // STAGE8M: min level for item evolution\n"
        "    IF_MIN_BADGES,                      // STAGE8M: count obtained Hoenn badges\n"
        "    CONDITIONS_END\n};",
        "additional evolution conditions",
    )
    start = old["evo_code"].find("bool32 DoesMonMeetAdditionalConditions(")
    stop = old["evo_code"].find("enum Species GetEvolutionTargetSpecies(", start)
    if start < 0 or stop <= start:
        raise ValueError("Evolution predicate function boundaries changed")
    section = old["evo_code"][start:stop]
    addition = """        // STAGE8M: custom catalyst gates without interfering with normal evolutions
        case IF_MIN_LEVEL:
            if (GetMonData(mon, MON_DATA_LEVEL) >= params[i].arg1)
                currentCondition = TRUE;
            break;
        case IF_MIN_BADGES:
        {
            u32 badgesObtained = 0;
            for (j = 0; j < NUM_BADGES; j++)
                if (FlagGet(FLAG_BADGE01_GET + j))
                    badgesObtained++;
            if (badgesObtained >= params[i].arg1)
                currentCondition = TRUE;
            break;
        }
"""
    updated_section = replace_exact(
        section, "        case CONDITIONS_END:\n", addition + "        case CONDITIONS_END:\n",
        "additional evolution switch",
    )
    if "FlagGet(" not in old["evo_code"] and '#include "event_data.h"' not in old["evo_code"]:
        raise ValueError("Missing flag access import")
    new["evo_code"] = old["evo_code"][:start] + updated_section + old["evo_code"][stop:]

    # Replace only Stage 8L's test-only Eevee entry.
    start = old["eevee"].find("    [SPECIES_EEVEE] =")
    end = old["eevee"].find("    [SPECIES_EEVEE_STARTER] =", start)
    if start < 0 or end < 0:
        raise ValueError("Unable to isolate normal Eevee family")
    eevee = old["eevee"][start:end]
    old_entry = re.compile(
        r'(?m)^([ \t]*),\{EVO_LEVEL,\s*6,\s*SPECIES_AERIEON,\s*'
        r'CONDITIONS\(\{IF_IN_MAP,\s*MAP_ROUTE102\}\)\}'
        r'\s*// STAGE8L_EEVEE_AERIEON: QA-only Route 102 level-up[ \t]*$'
    )
    if len(old_entry.findall(eevee)) != 1:
        raise ValueError("Stage 8L Eevee test evolution is missing or changed")
    eevee_new = old_entry.sub(
        r'\1,{EVO_ITEM, ITEM_SKY_CATALYST, SPECIES_AERIEON, '
        r'CONDITIONS({IF_MIN_LEVEL, 15})} // STAGE8M: Sky Catalyst choice',
        eevee, count=1,
    )
    for target in PRESERVE:
        if eevee.count(target) != eevee_new.count(target):
            raise ValueError(f"Original Eevee evolution changed: {target}")
    if eevee_new.count("ITEM_SKY_CATALYST") != 1:
        raise ValueError("Expected exactly one Eevee catalyst branch")
    new["eevee"] = old["eevee"][:start] + eevee_new + old["eevee"][end:]

    # Replace the Aerieon -> Aerartheon TEST-ONLY level 6 shortcut.
    custom = old["custom"]
    target = "    [SPECIES_AERIEON] ="
    start = custom.find(target)
    if start < 0 or custom.find(target, start + 1) >= 0:
        raise ValueError("Aerieon custom species definition missing or duplicated")
    stop = custom.find("\n    },", start)
    if stop < 0:
        raise ValueError("Aerieon species definition has no closing marker")
    species_section = custom[start:stop]
    test_evo = re.compile(
        r'\.evolutions\s*=\s*EVOLUTION\(\{\s*EVO_LEVEL\s*,\s*6\s*,'
        r'\s*SPECIES_AERARTHEON\s*\}\s*\)'
    )
    if len(test_evo.findall(species_section)) != 1:
        raise ValueError("Expected temporary Aerieon level-6 evolution not found")
    species_new = test_evo.sub(
        ".evolutions = EVOLUTION({EVO_ITEM, ITEM_SKY_CATALYST, SPECIES_AERARTHEON, "
        "CONDITIONS({IF_MIN_LEVEL, 38}, {IF_MIN_BADGES, 6})})", species_section
    )
    new["custom"] = custom[:start] + species_new + custom[stop:]

    # Make the new item obtainable through normal gameplay without rewriting
    # Birch's starter event or introducing new save flags.
    shop_anchor = "\t.2byte ITEM_POKE_BALL\n\t.2byte ITEM_POTION\n"
    new["shop"] = replace_exact(
        old["shop"], shop_anchor,
        shop_anchor + "\t.2byte ITEM_SKY_CATALYST @ STAGE8M: expanded shop only\n",
        "Oldale Mart expanded inventory",
    )

    # Validate all in-memory changes before touching any checkout file.
    if not all(new[key] != old[key] for key in files):
        raise ValueError("One or more changes had no effect")
    if "EVO_LEVEL, 6, SPECIES_AERARTHEON" in new["custom"]:
        raise ValueError("Old Aerartheon auto-evolution survived")
    if "STAGE8L_EEVEE_AERIEON" in new["eevee"]:
        raise ValueError("Old Eevee Route 102 auto-evolution survived")

    for key, path in files.items():
        path.write_text(new[key], encoding="utf-8")

    print("Stage 8M: Sky Catalyst (ID 874) available at expanded Oldale Town Mart.")
    print("Eevee -> Aerieon: Sky Catalyst, level >= 15; other 8 evolutions preserved.")
    print("Aerieon -> Aerartheon: Sky Catalyst, level >= 38, at least 6 badges.")
    print("Removed both automatic level-6 test evolutions; wild encounter rates unchanged.")
    print("Only staged source was changed. Gameplay and saved-game compatibility need testing.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path)
    patch(parser.parse_args().checkout)
