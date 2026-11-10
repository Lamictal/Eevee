#!/usr/bin/env python3
"""Stage 8H: follower Pokémon and numeric IV/EV summary pages.

PokeNav is already in Emerald. This script does not alter its story unlock.
DexNav hunting is a separate feature requiring dedicated flags/save assessment.
Requires the upstream follower graphics/event system already enabled.
"""
from pathlib import Path
import argparse
import re

def apply(checkout: Path):
    root = checkout.resolve()
    if not (root / "Makefile").is_file():
        raise SystemExit("Missing expansion source Makefile")

    targets = {
        "include/config/overworld.h": {
            "OW_POKEMON_OBJECT_EVENTS": ("TRUE", "TRUE"),
            "OW_SUBSTITUTE_PLACEHOLDER": ("TRUE", "TRUE"),
            "OW_FOLLOWERS_ENABLED": ("FALSE", "TRUE"),
        },
        "include/config/summary_screen.h": {
            "P_SUMMARY_SCREEN_IV_EV_INFO": ("FALSE", "TRUE"),
            "P_SUMMARY_SCREEN_IV_EV_VALUES": ("FALSE", "TRUE"),
            "P_SUMMARY_SCREEN_IV_EV_TILESET": ("FALSE", "TRUE"),
        },
    }
    proposed={}
    for relative, requirements in targets.items():
        path=root / relative
        source=path.read_text(encoding="utf-8")
        replacement=source
        for key,(expected,desired) in requirements.items():
            regex=re.compile(rf"^(#define[ \t]+{re.escape(key)}[ \t]+)([A-Za-z0-9_]+)([^\n]*)$", re.M)
            hits=list(regex.finditer(replacement))
            if len(hits)!=1 or hits[0].group(2)!=expected:
                found=[h.group(2) for h in hits]
                raise SystemExit(f"Unsafe config state for {key}: expected {[expected]}, found {found}")
            replacement=regex.sub(lambda m: m.group(1)+desired+m.group(3),replacement,count=1)
        proposed[path]=replacement
    # Validate all settings before modifying either file.
    for path,data in proposed.items():
        if not data:
            raise SystemExit(f"Unexpected empty output for {path}")
    for path,data in proposed.items():
        path.write_text(data,encoding="utf-8")
    print("Stage 8H: Following Pokémon enabled. The lead healthy party Pokémon can follow.")
    print("Stage 8H: Overworld sprite fallback remains enabled for custom species lacking walk art.")
    print("Stage 8H: IV/EV summary enabled, including actual IV numbers and alternate label graphics.")
    print("Stage 8H: Standard Emerald PokéNav left unchanged; DexNav not enabled.")
    print("Stage 8H: No deliberate saved-data structure changes; back up saves before first load.")

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("checkout",type=Path)
    apply(p.parse_args().checkout)
