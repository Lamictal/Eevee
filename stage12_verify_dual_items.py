#!/usr/bin/env python3
"""Stage 12: make all 18 type-booster items usable for dual evolutions.

The Stage 10 importer changes .type and .fieldUseFunc for 18 held
type-boosters, but the engine's PokemonUseItemEffects returns immediately if
an item has no .effect. Give each booster gItemEffect_EvoItem as evolution
stones do, while keeping its existing holdEffect so held type boosts work.

Audit all 18 x 17 source -> target routes, all 153 unique dual targets, and
Lilycove item availability. Does not change species IDs or saved data.
"""
from pathlib import Path
import argparse
import json
import re

def get_block(text, pattern, label):
    positions = list(re.finditer(pattern, text, flags=re.M))
    if len(positions) != 1:
        raise ValueError(f"Expected one {label}, got {len(positions)}")
    start = positions[0].start()
    stop = text.find("\n    },", positions[0].end())
    if stop < 0:
        raise ValueError(f"Unterminated {label}")
    return start, stop, text[start:stop]

def patch(checkout):
    root = checkout.resolve()
    if not (root / "Makefile").is_file():
        raise ValueError("Not a pokeemerald-expansion checkout")
    source = Path(__file__).resolve().parent / "stage10"
    boosters = json.loads((source / "type_boost_items.json").read_text(encoding="utf8"))
    manifest = json.loads((source / "manifest.json").read_text(encoding="utf8"))
    forms = manifest["forms"]
    order = manifest["types"]
    by_key = {f["key"]: f for f in forms}
    singles = [f for f in forms if f["key"].startswith("SINGLE_")]
    duals = [f for f in forms if f["key"].startswith("DUAL_")]
    if len(singles) != 18 or len(duals) != 153 or len(boosters) != 18:
        raise ValueError("Expected 18 singles, 153 duals and 18 unique boosters")
    if set(boosters) != set(order) or len(set(boosters.values())) != 18:
        raise ValueError("Invalid second-type booster map")

    path = root / "src/data/items.h"
    original = path.read_text(encoding="utf8")
    modified = original
    affected = []
    for type_name, item in boosters.items():
        a,b,block = get_block(modified, r"^    \[" + re.escape(item) + r"\] =", item)
        if ".type = ITEM_USE_PARTY_MENU," not in block:
            raise ValueError(f"{item} not enabled as party evolution item")
        field = ".fieldUseFunc = ItemUseOutOfBattle_EvolutionStone,"
        if field not in block:
            raise ValueError(f"{item} not routed to evolution item handler")
        if ".effect =" in block:
            if ".effect = gItemEffect_EvoItem," not in block:
                raise ValueError(f"{item} has conflicting effect")
        else:
            block = block.replace(field, field + "\n        .effect = gItemEffect_EvoItem, // STAGE12_EEVEE_DUAL_ITEM", 1)
        modified = modified[:a]+block+modified[b:]
        affected.append(item)
    if modified == original:
        raise ValueError("All boosters already have evo effect; refusing duplicate patch")

    # Verify that any single-type parent has exactly the seventeen target
    # items that lead to distinct unordered dual combinations.
    native = list((root / "src/data/pokemon/species_info").glob("gen_*_families.h"))
    custom = root / "src/data/pokemon/species_info.h"
    trees = [(p,p.read_text(encoding="utf8")) for p in native + [custom]]
    total_routes = 0
    seen_duals = set()
    for f in singles:
        species = "SPECIES_" + f["name"].upper()
        matches = []
        for p,t in trees:
            if re.search(r"^    \[" + re.escape(species) + r"\] =",t,flags=re.M):
                matches.append((p,t))
        if len(matches) != 1:
            raise ValueError(f"Missing unique single form species record {species}")
        _,text = matches[0]
        _,_,block = get_block(text,r"^    \[" + re.escape(species) + r"\] =", species)
        routing = dict(re.findall(r"\{\s*EVO_ITEM\s*,\s*(ITEM_[A-Z0-9_]+)\s*,\s*(SPECIES_[A-Z0-9_]+)\s*,\s*CONDITIONS\(\{IF_MIN_LEVEL,\s*38\},\s*\{IF_MIN_BADGES,\s*6\}\)\s*\}",block))
        origin = f["types"][0]
        expected = {}
        for second in order:
            if origin == second:
                continue
            pair = "DUAL_" + "_".join(t for t in order if t in (origin,second))
            target = by_key[pair]["name"]
            expected[boosters[second]] = "SPECIES_" + target.upper()
            seen_duals.add(pair)
        if routing != expected or len(routing)!=17:
            raise ValueError(f"{species}: expected all 17 distinct typed item routes; got {len(routing)}")
        total_routes += len(routing)
    if total_routes != 306 or len(seen_duals)!=153:
        raise ValueError(f"Missing 18x17 evolution routes: {total_routes} / {len(seen_duals)}")

    lily = root / "data/maps/LilycoveCity_DepartmentStore_4F/scripts.inc"
    lily_data = lily.read_text(encoding="utf8")
    for item in boosters.values():
        if f".2byte {item} " not in lily_data:
            raise ValueError(f"Missing Lilycove booster item: {item}")
    path.write_text(modified,encoding="utf8")
    print("Stage 12: restored EvoItem effect to 18 type boosters without removing their hold effects.")
    print("Stage 12: verified 306 item evolution routes from 18 singles to 153 unique dual targets.")
    print("Stage 12: verified all 18 type boosters in Lilycove Department Store 4F.")
    print("Stage 12: no species IDs, wild encounters, or save format changes.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path)
    patch(parser.parse_args().checkout)
