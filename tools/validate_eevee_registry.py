#!/usr/bin/env python3
"""Stage 8N deterministic form-registry and save-layout planning checks.

This check verifies *planning data*, not in-game functionality or save migration.
Run: python3 tools/validate_eevee_registry.py
"""
from __future__ import annotations
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "data/eevee_form_registry.json"
OFFICIAL = {
    "WATER": ("Vaporeon", 134),
    "ELECTRIC": ("Jolteon", 135),
    "FIRE": ("Flareon", 136),
    "PSYCHIC": ("Espeon", 196),
    "DARK": ("Umbreon", 197),
    "GRASS": ("Leafeon", 470),
    "ICE": ("Glaceon", 471),
    "FAIRY": ("Sylveon", 700),
}
TYPES = (
    "NORMAL", "FIGHTING", "FLYING", "POISON", "GROUND", "ROCK",
    "BUG", "GHOST", "STEEL", "FIRE", "WATER", "GRASS",
    "ELECTRIC", "PSYCHIC", "ICE", "DRAGON", "DARK", "FAIRY",
)

def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)

def main() -> None:
    doc = json.loads(REGISTRY.read_text(encoding="utf8"))
    forms = doc["forms"]
    require(doc["schema_version"] == 1, "Unknown registry schema")
    require(tuple(doc["type_order"]) == TYPES, "Type order must not drift")
    require(len(forms) == 171, "18 single + 153 dual entries expected")
    require(len({f["key"] for f in forms}) == 171, "Duplicate form keys")
    singles = [f for f in forms if f["category"] == "single"]
    duals = [f for f in forms if f["category"] == "dual"]
    require(len(singles) == 18 and len(duals) == 153, "Incomplete form types")
    require({f["types"][0] for f in singles} == set(TYPES), "Missing a single type")
    expected_pairs = set(itertools.combinations(TYPES, 2))
    observed_pairs = {tuple(f["types"]) for f in duals}
    require(len(observed_pairs) == 153, "Duplicate dual type")
    require(observed_pairs == expected_pairs, "Missing/unexpected unordered dual types")

    by_key = {f["key"]: f for f in forms}
    custom = [f for f in forms if f["origin"] == "custom"]
    native = [f for f in forms if f["origin"] == "official"]
    require(len(native) == 8 and len(custom) == 163, "Wrong official/custom partition")
    for t, (name, dex_no) in OFFICIAL.items():
        f = by_key[f"SINGLE_{t}"]
        require(f["origin"] == "official", f"{name} accidentally made custom")
        require(f["species_symbol"] == f"SPECIES_{name.upper()}", f"Wrong symbol for {name}")
        require(f["national_dex"] == dex_no and f["name"] == name,
                f"Changed canonical official National Dex number for {name}")
        require(f["integration_status"] == "inherited_engine", f"Native {name} status changed")
    for f in custom:
        require(f["national_dex"] is not None, f"Missing reserved custom dex number: {f['key']}")
        if f["integration_status"] == "reserved":
            require(f["name"] is None and f["species_symbol"] is None,
                    f"Do not assign unverified names/symbols to {f['key']}")
    require(by_key["SINGLE_FLYING"]["national_dex"] == 1026, "Aerieon legacy dex moved")
    require(by_key["SINGLE_FLYING"]["species_symbol"] == "SPECIES_AERIEON", "Aerieon ID changed")
    require(by_key["DUAL_FLYING_BUG"]["national_dex"] == 1027, "Aerartheon legacy dex moved")
    require(by_key["DUAL_FLYING_BUG"]["species_symbol"] == "SPECIES_AERARTHEON", "Aerartheon ID changed")
    custom_ids = [f["national_dex"] for f in custom]
    require(sorted(custom_ids) == list(range(1026, 1189)), "Custom IDs must cover 1026..1188 exactly")
    new_ids = [f["national_dex"] for f in forms if f["integration_status"] == "reserved"]
    require(new_ids == list(range(1028,1189)), "Do not renumber unimplemented IDs")
    for f in duals:
        a, b = f["types"]
        route = f["planned_evolution"]
        require(route["from_either_single"] == [f"SINGLE_{a}", f"SINGLE_{b}"],
                f"Dual-form source route missing: {f['key']}")
        require(route["min_level"] == 38 and route["min_badges"] == 6,
                f"Progression plan changed for {f['key']}")

    scope = doc["scope"]
    require((scope["single_type_forms"],scope["dual_type_forms"],scope["official_existing_forms"],
             scope["total_custom_forms"]) == (18,153,8,163), "Scope counts drifted")
    plan = doc["save_layout_plan"]
    current, future = plan["current_national_dex_count"], plan["full_national_dex_count"]
    current_bytes = (current + 1 + 7) // 8
    future_bytes = (future + 1 + 7) // 8
    require((current,future,current_bytes,future_bytes)==(1027,1188,129,149),
            "Save layout constants inconsistent")
    require(plan["growth_bytes_each"] == future_bytes-current_bytes == 20,
            "Miscomputed save array growth")
    require(plan["requires_migration"] is True,
            "171-form layout must NOT be claimed backward-compatible")
    print("PASS: 18 single-type + 153 unordered dual-type Eeveelutions in stable registry.")
    print("PASS: eight original official Eeveelutions retain official IDs.")
    print("PASS: 163 custom Dex numbers reserved #1026..#1188; Aerieon/Aerartheon unchanged.")
    print("SAVE AUDIT: Dex seen/caught arrays grow 129 -> 149 bytes each (+40 combined).")
    print("NOTE: No saved-game layout or actual playable roster is changed in Stage 8N.")

if __name__ == "__main__":
    main()
