#!/usr/bin/env python3
"""Stage 8J: register Aerieon/Aerartheon as genuine custom National Dex species.

This patch also ensures National-only Pokémon (such as Dolliv) do not show\nNo. 000 on Pokédex screens before the National Dex is unlocked.\n\nThis source prototype has exactly two additions beyond the official Gen IX dex.
The increase remains within the same 129-byte seen/caught save arrays because
ROUND_BITS_TO_BYTES(1026) == ROUND_BITS_TO_BYTES(1028) == 129. The future 171
species expansion WILL need a deliberate save-format migration.
"""
from pathlib import Path
import argparse
import re

def swap_exact(data, old, new, path):
    if data.count(old) != 1:
        raise ValueError(f"{path}: expected exactly one anchor; got {data.count(old)} for {old[:80]!r}")
    return data.replace(old, new, 1)

def install(checkout: Path):
    root = checkout.resolve()
    dex = root / "include/constants/pokedex.h"
    info = root / "src/data/pokemon/species_info.h"
    classic = root / "src/pokedex.c"
    hgss = root / "src/pokedex_plus_hgss.c"
    global_h = root / "include/global.h"
    species_config = root / "include/config/species_enabled.h"
    pokemon_c = root / "src/pokemon.c"
    summary_c = root / "src/pokemon_summary_screen.c"

    if not (root / "Makefile").is_file():
        raise ValueError("Not a source checkout")
    if "#define P_GEN_9_POKEMON                  TRUE" not in species_config.read_text(encoding="utf-8"):
        raise ValueError("Stage 8J assumes all Gen IX Pokémon are enabled")
    if "#define NUM_DEX_FLAG_BYTES ROUND_BITS_TO_BYTES(POKEMON_SLOTS_NUMBER)" not in global_h.read_text(encoding="utf-8"):
        raise ValueError("Unexpected save dex flag calculation")
    # Official Pokédex ends at Pecharunt, #1025. The two appended entries
    # are #1026 and #1027. Saves still allocate ceil(1028/8) = 129 bytes.
    if ((1025 + 1 + 7) // 8) != ((1027 + 1 + 7) // 8):
        raise ValueError("Dex flag storage would change, aborting")

    files = {p: p.read_text(encoding="utf-8") for p in (dex,info,classic,hgss)}
    if any("STAGE8J_DEX" in text for text in files.values()):
        raise ValueError("Already applied Stage 8J")

    x = files[dex]
    x = swap_exact(x,
        "    NATIONAL_DEX_PECHARUNT,\n};",
        "    NATIONAL_DEX_PECHARUNT,\n"
        "    // STAGE8J_DEX: custom Eevee species appended after official Pokédex\n"
        "    NATIONAL_DEX_AERIEON,\n"
        "    NATIONAL_DEX_AERARTHEON,\n};",dex)
    x = swap_exact(x,
        "    #define NATIONAL_DEX_COUNT  NATIONAL_DEX_PECHARUNT",
        "    #define NATIONAL_DEX_COUNT  NATIONAL_DEX_AERARTHEON",dex)
    files[dex] = x

    x=files[info]
    for name,desc in (
        ("Aerieon", 'COMPOUND_STRING("Its broad wings catch warm currents.\\nIt can glide for hours without once\\nflapping, surveying the forest below.")'),
        ("Aerartheon", 'COMPOUND_STRING("It senses subtle shifts in the wind\\nwith its delicate wings. It darts\\nthrough forests with uncanny ease.")')):
        anchor=f"    [SPECIES_{name.upper()}] = {{"
        pos=x.find(anchor)
        if pos<0 or x.count(anchor)!=1:raise ValueError(f"Missing {name}")
        end=x.find("\n    },",pos)
        if end<0:raise ValueError(f"Missing {name} end")
        block=x[pos:end]
        if block.count(".natDexNum = NATIONAL_DEX_NONE")!=1 or block.count(".description = gFallbackPokedexText")!=1:
            raise ValueError(f"Unexpected {name} Pokédex placeholders")
        block=block.replace(".natDexNum = NATIONAL_DEX_NONE",f".natDexNum = NATIONAL_DEX_{name.upper()}",1)
        block=block.replace(".description = gFallbackPokedexText",f".description = {desc}",1)
        # Explicit marker so duplicate/rebase patches fail safely.
        block=block.replace(anchor,anchor+"\n        // STAGE8J_DEX: registered custom species")
        x=x[:pos]+block+x[end:]
    files[info]=x

    # Before the National Dex is unlocked the registration screen would otherwise
    # display Hoenn regional number 000. For these two custom, unlisted regional
    # species, display their genuine National numbers on registration.
    for f in (classic,hgss):
        x=files[f]
        if f == classic:
            old='u8 digitCount = (NATIONAL_DEX_COUNT > 999 && IsNationalPokedexEnabled()) ? 4 : 3;'
            new='u8 digitCount = (NATIONAL_DEX_COUNT > 999 && (IsNationalPokedexEnabled() || num >= NATIONAL_DEX_AERIEON || NationalToRegionalOrder(num) == 0)) ? 4 : 3; // STAGE8J_DEX'
        else:
            old='u8 digitCount = (NATIONAL_DEX_COUNT > 999 && value != 0) ? 4 : 3;'
            new='u8 digitCount = (NATIONAL_DEX_COUNT > 999 && (value != 0 || num >= NATIONAL_DEX_AERIEON || NationalToRegionalOrder(num) == 0)) ? 4 : 3; // STAGE8J_DEX'
        x=swap_exact(x,old,new,f)
        old='    if (value == 0)\n        value = NationalToRegionalOrder(num);\n    else\n        value = num;'
        new='    if (value == 0 && num < NATIONAL_DEX_AERIEON && NationalToRegionalOrder(num) != 0)\n        value = NationalToRegionalOrder(num);\n    else\n        value = num;'
        # The same regional number selection can occur elsewhere in HGSS code.
        # Patch ONLY the PrintMonInfo function instead of applying a global edit.
        method="static void PrintMonInfo(u32 num, u32 value, u32 owned, u32 newEntry)\n{"
        start=x.find(method)
        if start<0 or x.find(method,start+1)>=0:
            raise ValueError(f"Expected exactly one PrintMonInfo implementation in {f}")
        at=x.find(old,start)
        if at<0 or at>start+1100:
            raise ValueError(f"Regional dex display branch not found inside PrintMonInfo in {f}")
        x=x[:at]+new+x[at+len(old):]
        if f == hgss:
            # The optional HGSS stats page repeats this regional-number fallback.
            stats_method="static void PrintStatsScreen_NameGender(u8 taskId, u32 num, u32 value)\n{"
            stats_start=x.find(stats_method)
            if stats_start<0 or x.find(stats_method,stats_start+1)>=0:
                raise ValueError(f"Expected exactly one HGSS stats screen in {f}")
            stats_at=x.find(old,stats_start)
            if stats_at<0 or stats_at>stats_start+1600:
                raise ValueError(f"Regional dex branch missing from HGSS stats screen in {f}")
            x=x[:stats_at]+new+x[stats_at+len(old):]
        files[f]=x

    # The PC/party summary uses SpeciesToPokedexNum, not PrintMonInfo.
    # With the regional Pokédex still active, a non-Hoenn species has
    # regional number 0. Returning that number incorrectly prints No. 000.
    # Fall back only if a genuine National Dex number exists.
    original_numbers = pokemon_c.read_text(encoding="utf-8")
    old_numbers = """u16 SpeciesToPokedexNum(enum Species species)
{
    if (IsNationalPokedexEnabled())
    {
        return SpeciesToNationalPokedexNum(species);
    }
    else
    {
        species = SpeciesToRegionalPokedexNum(species);
        if (species <= REGIONAL_DEX_COUNT)
            return species;
        return 0xFFFF;
    }
}"""
    new_numbers = """u16 SpeciesToPokedexNum(enum Species species)
{
    u16 nationalNum = SpeciesToNationalPokedexNum(species);
    u16 regionalNum;

    if (IsNationalPokedexEnabled())
        return nationalNum;

    regionalNum = SpeciesToRegionalPokedexNum(species);
    if (regionalNum != 0 && regionalNum <= REGIONAL_DEX_COUNT)
        return regionalNum;

    // STAGE8J_DEX: Nonregional Pokemon still have real National numbers.
    if (regionalNum == 0 && nationalNum != NATIONAL_DEX_NONE)
        return nationalNum;

    return 0xFFFF;
}"""
    files[pokemon_c] = swap_exact(original_numbers,old_numbers,new_numbers,pokemon_c)

    # Four digits are needed for custom forms and later National species,
    # even while the National Pokédex is not unlocked.
    summary_original = summary_c.read_text(encoding="utf-8")
    files[summary_c] = swap_exact(
        summary_original,
        "u8 digitCount = (NATIONAL_DEX_COUNT > 999 && IsNationalPokedexEnabled()) ? 4 : 3;",
        "u8 digitCount = (NATIONAL_DEX_COUNT > 999 && (IsNationalPokedexEnabled() || dexNum > 999)) ? 4 : 3; // STAGE8J_DEX",
        summary_c)

    for path,contents in files.items():
        path.write_text(contents,encoding="utf-8")
    print("Stage 8J registered Aerieon #1026 and Aerartheon #1027 in the National Dex.")
    print("Category, height, weight, and descriptions use their custom species entries.")
    print("Hoenn Dex order unchanged; nonregional Pokemon display their real National Dex numbers in registration and PC summaries.")
    print("Save dex seen/caught array length remains 129 bytes. Runtime compatibility still untested.")

if __name__=="__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout",type=Path)
    install(parser.parse_args().checkout)
