#!/usr/bin/env python3
"""Post-build roster and ROM sanity gate. Static checks, not emulator playtests."""
import argparse
import itertools
import json
import re
from pathlib import Path
from generate_eevee_learnsets import pointers

def audit(root, manifest, report):
    errors = []
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            errors.append(name)
    doc = json.loads(manifest.read_text())
    forms = doc["forms"]
    types = doc["types"]
    expected = {frozenset([t]) for t in types} | {frozenset(p) for p in itertools.combinations(types, 2)}
    check("171 distinct type combinations", len(types)==18 and len(forms)==171 and {frozenset(f["types"]) for f in forms}==expected)
    check("unique species names", len({f["name"].upper() for f in forms})==171)
    check("unique national dex IDs", len({f["national_dex"] for f in forms})==171)
    ptr = pointers(root)
    for f in forms:
        name = f["name"].upper()
        entries = ptr.get(name, [])
        check("unique species and learnset pointer: "+name, len(entries)==1 and len(entries[0][1])==1)
    rom = root / "pokeemerald.gba"
    data = rom.read_bytes() if rom.is_file() else b""
    check("GBA image size and fixed header byte", 192 <= len(data) <= 32*1024*1024 and len(data)%4==0 and data[0xB2]==0x96)
    check("GBA header complement", len(data)>=192 and ((-sum(data[0xA0:0xBD])-0x19)&255)==data[0xBD])
    report.write_text(json.dumps({"scope":"static post-build checks; no emulator execution","passed":sum(checks.values()),"failed":errors,"checks":checks},indent=2)+"\n")
    print(f"Static QA: {sum(checks.values())}/{len(checks)} checks passed")
    if errors:
        raise SystemExit("\n".join(errors))

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--checkout",type=Path,required=True)
    p.add_argument("--manifest",type=Path,required=True)
    p.add_argument("--report",type=Path,required=True)
    a=p.parse_args()
    audit(a.checkout,a.manifest,a.report)
