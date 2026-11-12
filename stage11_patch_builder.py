#!/usr/bin/env python3
"""Attach Stage 11 habitats after the Stage 10 full-roster importer."""
from pathlib import Path
p = Path(__file__).parent / "kit" / "build_stage8d.py"
s = p.read_text(encoding="utf8")
old = "    run([sys.executable, str(ROOT.parent/'stage10/import_full_roster_alpha.py'), str(dest)])\n"
end = "    buildlog=ROOT/'stage8d_build.log'\n"
new = "    run([sys.executable, str(ROOT.parent/'stage11_full_ecology.py'), str(dest)])\n"
if s.count(old+end)!=1 or new in s:
    raise SystemExit("Unknown Stage 10 build order: no changes made")
p.write_text(s.replace(old+end, old+new+end, 1), encoding="utf8")
print("Stage 11 full Hoenn encounter ecology hooked after all 171 forms")
