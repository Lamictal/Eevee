#!/usr/bin/env python3
"""Stage 9 world balance: original Hoenn wild Pokémon retained.

Keep Eevee attainable early, make Aerieon a rare later encounter, and move
Aerartheon out of the beginner route into Victory Road. Add evolution
stones to accessible Poké Marts without removing their vanilla stock.

This source patch only references Eevee, Aerieon and Aerartheon, which are
already integrated. The other 161 custom Eevee forms remain roster-registered
but are not used by the ROM until their species entries and artwork are built.
"""
from pathlib import Path
import argparse
import json

# The engine's twelve standard land slots have these encounter weights.
WEIGHTS = (20, 20, 10, 10, 10, 10, 5, 5, 4, 4, 1, 1)
ROUTES = {
    # map -> (slot, new species, minimum level, maximum level, probability)
    "MAP_ROUTE101": (7, "SPECIES_EEVEE", 3, 4, 5),
    "MAP_ROUTE102": (2, "SPECIES_EEVEE", 4, 5, 10),
    "MAP_ROUTE104": (7, "SPECIES_EEVEE", 5, 7, 5),
    "MAP_ROUTE117": (7, "SPECIES_EEVEE", 12, 16, 5),
    "MAP_ROUTE119": (7, "SPECIES_AERIEON", 24, 27, 5),
    "MAP_VICTORY_ROAD_1F": (10, "SPECIES_AERARTHEON", 40, 42, 1),
}
MART_STOCK = {
    "RustboroCity_Mart": {
        "RustboroCity_Mart_Pokemart_Expanded":
            ["ITEM_FIRE_STONE", "ITEM_WATER_STONE", "ITEM_THUNDER_STONE"]
    },
    "MauvilleCity_Mart": {
        "MauvilleCity_Mart_Pokemart":
            ["ITEM_LEAF_STONE", "ITEM_ICE_STONE", "ITEM_MAGNET", "ITEM_TWISTED_SPOON"]
    },
    "SlateportCity_Mart": {
        "SlateportCity_Mart_Pokemart":
            ["ITEM_SILK_SCARF", "ITEM_MYSTIC_WATER", "ITEM_MIRACLE_SEED"]
    },
    "LavaridgeTown_Mart": {
        "LavaridgeTown_Mart_Pokemart":
            ["ITEM_CHARCOAL", "ITEM_HARD_STONE", "ITEM_SOFT_SAND"]
    },
    "FortreeCity_Mart": {
        "FortreeCity_Mart_Pokemart":
            ["ITEM_SHARP_BEAK", "ITEM_SILVER_POWDER", "ITEM_SPELL_TAG",
             "ITEM_BLACK_GLASSES", "ITEM_POISON_BARB", "ITEM_BLACK_BELT",
             "ITEM_METAL_COAT"]
    },
    "LilycoveCity_DepartmentStore_4F": {
        "LilycoveCity_DepartmentStore_4F_Pokemart_DefenseTMs":
            ["ITEM_SILK_SCARF", "ITEM_BLACK_BELT", "ITEM_SHARP_BEAK",
             "ITEM_POISON_BARB", "ITEM_SOFT_SAND", "ITEM_HARD_STONE",
             "ITEM_SILVER_POWDER", "ITEM_SPELL_TAG", "ITEM_METAL_COAT",
             "ITEM_CHARCOAL", "ITEM_MYSTIC_WATER", "ITEM_MIRACLE_SEED",
             "ITEM_MAGNET", "ITEM_TWISTED_SPOON", "ITEM_NEVER_MELT_ICE",
             "ITEM_DRAGON_FANG", "ITEM_BLACK_GLASSES", "ITEM_FAIRY_FEATHER"]
    },
}

def world_balance(root: Path) -> None:
    root = root.resolve()
    if not (root / "Makefile").exists():
        raise ValueError("Not a pokeemerald-expansion source checkout")
    wild_path = root / "src/data/wild_encounters.json"
    source = wild_path.read_text(encoding="utf-8")
    if "STAGE9_WORLD_BALANCE" in source:
        raise ValueError("World balance was already applied")
    wild = json.loads(source)
    locations = [e for g in wild["wild_encounter_groups"]
                 for e in g.get("encounters", []) if e.get("land_mons")]
    route_index = {name: [] for name in ROUTES}
    for item in locations:
        if item.get("map") in route_index:
            route_index[item["map"]].append(item)
    if any(len(found) != 1 for found in route_index.values()):
        raise ValueError("Expected exactly one 12-slot land encounter per target route")
    if sum(WEIGHTS) != 100:
        raise AssertionError("Encounter weights do not total 100")
    if route_index["MAP_ROUTE102"][0]["land_mons"]["mons"][2]["species"] != "SPECIES_AERIEON":
        raise ValueError("Expected Stage 8K Aerieon in Route 102 10% canary slot")
    if route_index["MAP_ROUTE102"][0]["land_mons"]["mons"][10]["species"] != "SPECIES_AERARTHEON":
        raise ValueError("Expected Stage 8K Aerartheon in Route 102 1% canary slot")

    before = {}
    for map_id, (slot, species, low, high, chance) in ROUTES.items():
        mon = route_index[map_id][0]["land_mons"]["mons"]
        if len(mon) != 12 or WEIGHTS[slot] != chance:
            raise ValueError(f"Unexpected land slot proportions in {map_id}")
        before[map_id] = sum(weight for i, weight in enumerate(WEIGHTS)
                             if mon[i]["species"].startswith("SPECIES_AER"))
        mon[slot] = {"min_level": low, "max_level": high, "species": species}

    # Remove the last beginner-route Aerartheon catch shortcut; now evolves
    # through level / badge gating or rare high-level Victory Road encounters.
    route102 = route_index["MAP_ROUTE102"][0]["land_mons"]["mons"]
    route102[10] = {"min_level": 4, "max_level": 4, "species": "SPECIES_ZIGZAGOON"}

    # Guarantee normal Pokémon remain at least 90% of each configured route
    # (excluding Eevee, which counts as a special Eevee-focused appearance).
    for map_id in ROUTES:
        mon = route_index[map_id][0]["land_mons"]["mons"]
        special = sum(weight for i, weight in enumerate(WEIGHTS)
                      if mon[i]["species"] in
                      ("SPECIES_EEVEE", "SPECIES_AERIEON", "SPECIES_AERARTHEON"))
        if special > 10:
            raise ValueError(f"More than 10% Eevee-line encounters in {map_id}: {special}")
        if map_id == "MAP_ROUTE102" and any(
            m["species"] == "SPECIES_AERARTHEON" for m in mon
        ):
            raise ValueError("Aerartheon still accessible on Route 102")
    updated = json.dumps(wild, indent=2, ensure_ascii=False) + "\n"
    changes = {wild_path: updated}

    # Shop updates preserve all original stock. New items only appended in
    # the named stock list, not globally replacing a Mart or story script.
    for building, shops in MART_STOCK.items():
        path = root / "data/maps" / building / "scripts.inc"
        original = path.read_text(encoding="utf-8")
        changed = original
        for label, item_ids in shops.items():
            head = label + ":\n"
            if changed.count(head) != 1:
                raise ValueError(f"Missing unique shop list: {label}")
            start = changed.index(head) + len(head)
            end = changed.find("\tpokemartlistend", start)
            if end < 0 or end-start > 3000:
                raise ValueError(f"Unrecognized shop termination: {label}")
            block = changed[start:end]
            if any(f"\t.2byte {item}\n" in block for item in item_ids):
                raise ValueError(f"Already changed shop: {label}")
            addition = "".join(f"\t.2byte {item} @ STAGE9_WORLD_BALANCE\n"
                               for item in item_ids)
            changed = changed[:end] + addition + changed[end:]
        changes[path] = changed

    # Commit only after every validation passes, and keep original bytes in a
    # sidecar backup on the runner (not shipped as part of the game).
    for path, updated in changes.items():
        backup = path.with_name(path.name+".stage9.bak")
        if backup.exists():
            raise ValueError(f"Already applied: {path}")
    for path, updated in changes.items():
        backup = path.with_name(path.name+".stage9.bak")
        backup.write_bytes(path.read_bytes())
        path.write_text(updated, encoding="utf-8")
    print("Stage 9: regular Hoenn Pokémon retain >= 90% of the targeted routes.")
    print("Stage 9: Eevee 5-10% early; Aerieon 5% Route 119; Aerartheon 1% Victory Road.")
    print("Stage 9: key stones offered earlier; 18 type booster items sold at Lilycove.")
    print("Stage 9: no encounters for reserved unimplemented forms; no save changes.")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("checkout", type=Path)
    world_balance(p.parse_args().checkout)
