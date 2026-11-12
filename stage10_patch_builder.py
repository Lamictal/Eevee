#!/usr/bin/env python3
"""Hook Stage 10 all-171 source importer after balanced Stage 9 checkout patches.

Run only in the independent all-171 workflow; keep Stage 9 compile separate.
"""
from pathlib import Path
p=Path(__file__).parent/"kit"/"build_stage8d.py"
s=p.read_text(encoding="utf-8")
old="    run([sys.executable, str(ROOT.parent/'stage9_world_balance.py'), str(dest)])\n"
end="    buildlog=ROOT/'stage8d_build.log'\n"
extra="    run([sys.executable, str(ROOT.parent/'stage10/import_full_roster_alpha.py'), str(dest)])\n"
if s.count(old+end)!=1 or extra in s:
    raise SystemExit("Unexpected Stage 9 build chain; no changes written")
if not (Path(__file__).parent/"stage10"/"import_full_roster_alpha.py").exists():
    raise SystemExit("Extract Stage 10 roster/art bundle before hooking builder")
p.write_text(s.replace(old+end,old+extra+end,1),encoding="utf-8")
print("Stage 10 full 171 roster source import hooked into GitHub Actions compile")
