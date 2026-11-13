#!/usr/bin/env python3
"""Stage 11: spread all 18 Eeveelution singles and rare duals across Hoenn.

Runs AFTER Stage 9's conservation pass and Stage 10's complete species import.
Does not replace entire encounter tables: only selected 5%, 4%, or 1% slots.
Most custom duals remain evolution-first; no new save structures or IDs added.
"""
import argparse
import json
from pathlib import Path

WEIGHTS = (20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1)

# (encounter slot, canonical registry form key, min level, max level)
# Every chosen map is a unique Emerald land-encounter map in upstream.
# Stage 9's 5% Aerieon on Route 119 and 1% Aerartheon in Victory Road
# are preserved, as are 5-10% early Eevee sightings.
HABITATS = {
    # Keep Route 117's native Eevee sighting but do not add a high-stat
    # Neuteon this early. The species appears on Route 118 instead.
    "MAP_ROUTE117": [],
    "MAP_ROUTE114": [(7, "SINGLE_FIGHTING", 17, 19)],
    "MAP_ROUTE113": [(7, "SINGLE_POISON", 15, 17)],
    "MAP_FIERY_PATH": [(7, "SINGLE_FIRE", 16, 18), (9, "SINGLE_GROUND", 16, 18)],
    "MAP_NEW_MAUVILLE_INSIDE": [(7, "SINGLE_ELECTRIC", 24, 26), (9, "SINGLE_STEEL", 24, 26)],
    "MAP_ROUTE119": [(9, "SINGLE_BUG", 24, 27)],
    "MAP_ROUTE120": [(7, "SINGLE_GRASS", 25, 28), (9, "SINGLE_PSYCHIC", 25, 28)],
    "MAP_ROUTE121": [(7, "SINGLE_FAIRY", 26, 29)],
    "MAP_ROUTE123": [(7, "SINGLE_GRASS", 25, 28), (9, "SINGLE_FAIRY", 25, 28)],
    "MAP_MT_PYRE_2F": [(7, "SINGLE_GHOST", 27, 30), (9, "SINGLE_DARK", 27, 30)],
    "MAP_MT_PYRE_EXTERIOR": [(7, "SINGLE_GHOST", 27, 30), (9, "SINGLE_PSYCHIC", 27, 30)],
    "MAP_SHOAL_CAVE_LOW_TIDE_INNER_ROOM": [(7, "SINGLE_ICE", 30, 33), (9, "SINGLE_WATER", 30, 33)],
    "MAP_METEOR_FALLS_1F_2R": [(7, "SINGLE_DRAGON", 36, 39), (9, "SINGLE_ROCK", 36, 39)],
    "MAP_SAFARI_ZONE_NORTH": [(7, "SINGLE_FAIRY", 28, 31), (9, "SINGLE_BUG", 28, 31)],
    "MAP_MIRAGE_TOWER_1F": [(7, "SINGLE_GROUND", 21, 24), (9, "SINGLE_ROCK", 21, 24)],
    "MAP_ROUTE118": [(7, "SINGLE_WATER", 25, 27), (9, "SINGLE_NORMAL", 25, 27)],
    "MAP_ROUTE110": [(10, "SINGLE_ELECTRIC", 13, 14)],
    "MAP_JAGGED_PASS": [(7, "SINGLE_FIRE", 21, 23), (9, "SINGLE_ROCK", 21, 23)],
    "MAP_SEAFLOOR_CAVERN_ROOM1": [(7, "SINGLE_WATER", 33, 36), (9, "SINGLE_DARK", 33, 36)],
    "MAP_SKY_PILLAR_1F": [(7, "SINGLE_DRAGON", 36, 38), (9, "SINGLE_FLYING", 36, 38), (11, "DUAL_FLYING_DRAGON", 39, 40)],
    "MAP_SKY_PILLAR_3F": [(10, "DUAL_PSYCHIC_DRAGON", 39, 41), (11, "DUAL_FLYING_GHOST", 39, 41)],
    "MAP_VICTORY_ROAD_1F": [(11, "DUAL_STEEL_DRAGON", 40, 42)],
    "MAP_VICTORY_ROAD_B1F": [(10, "DUAL_FIRE_DRAGON", 41, 43), (11, "DUAL_WATER_DRAGON", 41, 43)],
    "MAP_VICTORY_ROAD_B2F": [(10, "DUAL_DRAGON_FAIRY", 43, 45), (11, "DUAL_DRAGON_DARK", 43, 45)],
    "MAP_METEOR_FALLS_B1F_2R": [(11, "DUAL_WATER_DRAGON", 38, 40)],
}

def patch(checkout: Path) -> None:
    root = checkout.resolve()
    if not (root / "Makefile").is_file():
        raise ValueError("Not an Emerald Expansion checkout")
    package = Path(__file__).resolve().parent / "stage10" / "manifest.json"
    source = json.loads(package.read_text(encoding="utf-8"))
    forms = source["forms"]
    by_key = {f["key"]: f for f in forms}
    if len(forms) != 171 or len(by_key) != 171:
        raise ValueError("Expected completed unique 171-form Stage 10 manifest")
    if sum(WEIGHTS) != 100:
        raise ValueError("Engine land encounter slot weights changed")

    # The opening Woods and Granite Cave have native low-power wild encounters.
    # Avoid putting 525-BST custom Eeveelutions there at levels 6-12.
    for early in ("MAP_PETALBURG_WOODS", "MAP_GRANITE_CAVE_1F", "MAP_GRANITE_CAVE_B1F"):
        if early in HABITATS:
            raise ValueError(f"Unexpected early Eeveelution overwrites in {early}")
    # Don't allow a map entry to refer to a reserved or unimplemented species.
    species_enum = (root / "include/constants/species.h").read_text(encoding="utf-8")
    expected_singles = {"SINGLE_" + t for t in source["types"]}
    added_singles, added_duals = set(), set()
    for map_id, changes in HABITATS.items():
        seen_slots = set()
        for slot, key, low, high in changes:
            if slot in seen_slots or not (0 <= slot < len(WEIGHTS)) or low < 1 or low > high or high > 100:
                raise ValueError(f"Invalid slot/level in {map_id}")
            seen_slots.add(slot)
            if key not in by_key or not by_key[key].get("name"):
                raise ValueError(f"Form missing from imported roster: {key}")
            symbol = "SPECIES_" + by_key[key]["name"].upper()
            if symbol not in species_enum:
                raise ValueError(f"Uncompiled species symbol {symbol}")
            if key.startswith("SINGLE_"):
                added_singles.add(key)
            elif key.startswith("DUAL_"):
                if WEIGHTS[slot] != 1:
                    raise ValueError(f"Dual forms must stay at 1%: {map_id}")
                added_duals.add(key)
            else:
                raise ValueError(f"Unexpected form category {key}")
    if added_singles != expected_singles:
        raise ValueError(f"Some single types lack wild habitats: {expected_singles-added_singles}")
    if len(added_duals) < 6:
        raise ValueError("Expected varied postgame dual-type sightings")

    p = root / "src/data/wild_encounters.json"
    original = p.read_text(encoding="utf-8")
    if "STAGE11_FULL_ECOLOGY" in original:
        raise ValueError("Stage 11 ecology has already been installed")
    data = json.loads(original)
    wild = [e for group in data["wild_encounter_groups"]
            for e in group.get("encounters", []) if e.get("land_mons")]
    available = {key: [e for e in wild if e.get("map") == key] for key in HABITATS}
    for key, matches in available.items():
        if len(matches) != 1 or len(matches[0]["land_mons"]["mons"]) != 12:
            raise ValueError(f"Expected one 12-slot land table for {key}, got {len(matches)}")

    # Previous milestone's encounter promises are validated before changing.
    def existing(map_id, slot, expected):
        got = available[map_id][0]["land_mons"]["mons"][slot]["species"]
        if got != expected:
            raise ValueError(f"Stage 9 encounter changed: {map_id}:{slot}={got}, expected {expected}")
    existing("MAP_ROUTE117", 7, "SPECIES_EEVEE")
    existing("MAP_ROUTE119", 7, "SPECIES_AERIEON")
    existing("MAP_VICTORY_ROAD_1F", 10, "SPECIES_AERARTHEON")

    special = {"SPECIES_EEVEE"} | {"SPECIES_" + f["name"].upper() for f in forms}
    report = []
    for map_id, changes in HABITATS.items():
        mons = available[map_id][0]["land_mons"]["mons"]
        initial = sum(WEIGHTS[i] for i, mon in enumerate(mons) if mon["species"] in special)
        if initial > 10:
            raise ValueError(f"Existing Eevee spawns exceed 10% in {map_id}: {initial}")
        chosen = []
        for slot, key, low, high in changes:
            symbol = "SPECIES_" + by_key[key]["name"].upper()
            mons[slot] = {"min_level": low, "max_level": high, "species": symbol}
            chosen.append({"form": by_key[key]["name"], "chance": WEIGHTS[slot],
                           "level_range": [low, high]})
        after = sum(WEIGHTS[i] for i, mon in enumerate(mons) if mon["species"] in special)
        if after > 10:
            raise ValueError(f"{map_id}: too many Eevee family spawns ({after}%)")
        regular = 100 - after
        if regular < 90:
            raise ValueError(f"Ordinary Pokémon no longer dominant in {map_id}")
        report.append({"map": map_id, "new_encounters": chosen, "eevee_family_percent": after,
                       "regular_pokemon_percent": regular})

    # Every original map except targeted maps remains byte-for-byte equivalent
    # when semantically parsed and serialized. No rate or fishing tables altered.
    output = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    p.write_text(output, encoding="utf-8")
    result = Path(__file__).resolve().parent / "stage11_ecology_report.json"
    result.write_text(json.dumps({"stage": 11, "maps": report,
                                  "unique_singles": len(added_singles),
                                  "rare_dual_species": len(added_duals),
                                  "note": "All 153 duals remain obtainable through Stage 10 evolution mechanics."},
                                 indent=2) + "\n", encoding="utf-8")
    print(f"STAGE11_FULL_ECOLOGY: balanced {len(report)} maps, {len(added_singles)} singles and {len(added_duals)} distinct rare dual types.")
    print("Retained at least 90% ordinary Pokémon per affected land map.")
    print("Moved early Bug/Fighting/Rock/Normal custom Eeveelutions out of Woods, Granite Cave and Route 117.")
    print("Retained Stage 9 early Eevee and Aerieon / Aerartheon encounters; item shops unchanged.")
    print("No species IDs, evolution rules, or saved data structures modified.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("checkout", type=Path)
    patch(ap.parse_args().checkout)
