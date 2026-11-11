#!/usr/bin/env python3
"""Stage 8L: connect ordinary starter Eevee to Aerieon with a test-only path.

Level Eevee to at least 6 while on Route 102 to get Aerieon. This is a
temporary QA condition, NOT the planned six-badge / level-38 catalyst system.
All canonical Eevee evolution entries and Aerieon -> Aerartheon are preserved.
"""
from pathlib import Path
import argparse
import re

TAG = "STAGE8L_EEVEE_AERIEON"
EEVEE_MARKER = "    [SPECIES_EEVEE] ="
# Anchored in Eevee's EVOLUTION macro, after the final optional Gen 4 choices.
ENDING = "                            #endif\n                            ),"
CUSTOM = (
    "                            #endif\n"
    "                                ,{EVO_LEVEL, 6, SPECIES_AERIEON, CONDITIONS({IF_IN_MAP, MAP_ROUTE102})} // "
    + TAG + ": QA-only Route 102 level-up\n"
    "                            ),"
)
PRESERVE = ("SPECIES_JOLTEON", "SPECIES_VAPOREON", "SPECIES_FLAREON",
            "SPECIES_SYLVEON", "SPECIES_ESPEON", "SPECIES_UMBREON",
            "SPECIES_LEAFEON", "SPECIES_GLACEON")

def patch(root: Path) -> None:
    root = root.resolve()
    if not (root / "Makefile").is_file():
        raise ValueError("Not a pokeemerald-expansion source checkout")
    path = root / "src/data/pokemon/species_info/gen_1_families.h"
    custom_path = root / "src/data/pokemon/species_info.h"
    if "[SPECIES_AERIEON]" not in custom_path.read_text(encoding="utf-8"):
        raise ValueError("Stage 8E Aerieon species not installed")
    original = path.read_text(encoding="utf-8")
    if original.count(EEVEE_MARKER) != 1 or TAG in original:
        raise ValueError("Unexpected or already modified Eevee species layout")
    start = original.index(EEVEE_MARKER)
    match = re.search(r"\n    \[SPECIES_[A-Z0-9_]+\]\s*=", original[start + len(EEVEE_MARKER):])
    if match is None:
        raise ValueError("Unable to isolate Eevee species")
    end = start + len(EEVEE_MARKER) + match.start()
    eevee = original[start:end]
    if eevee.count(".evolutions = EVOLUTION(") != 1 or eevee.count(ENDING) != 1:
        raise ValueError("Eevee evolution table changed; refusing risky overwrite")
    if not all(target in eevee for target in PRESERVE):
        raise ValueError("Existing Eevee evolution branches differ from tested baseline")
    updated = eevee.replace(ENDING, CUSTOM, 1)
    if any(updated.count(target) != eevee.count(target) for target in PRESERVE):
        raise ValueError("Standard Eevee evolution changed")
    if updated.count(TAG) != 1 or updated.count("SPECIES_AERIEON") != 1:
        raise ValueError("New Eevee -> Aerieon entry missing or duplicated")
    result = original[:start] + updated + original[end:]
    path.write_text(result, encoding="utf-8")
    print("Stage 8L: Eevee evolves to Aerieon when leveled to 6+ on Route 102 (test only).")
    print("All eight standard Eeveelution destinations and existing species IDs retained.")
    print("Stage 8E Aerieon -> Aerartheon evolution and Stage 8K encounters unchanged.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("checkout", type=Path)
    patch(parser.parse_args().checkout)
