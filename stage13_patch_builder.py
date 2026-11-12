#!/usr/bin/env python3
"""Attach the safe custom Eevee main-menu skin after Stage 12."""
from pathlib import Path
p=Path(__file__).resolve().parent/"kit"/"build_stage8d.py"
s=p.read_text(encoding="utf8")
anchor="    run([sys.executable, str(ROOT.parent/'stage12_verify_dual_items.py'), str(dest)])\n"
end="    buildlog=ROOT/'stage8d_build.log'\n"
extra="    run([sys.executable, str(ROOT.parent/'stage13_custom_menu.py'), str(dest)])\n"
if s.count(anchor+end)!=1 or extra in s:
    raise SystemExit("Unexpected Stage 12 builder hook; no changes written")
p.write_text(s.replace(anchor+end,anchor+extra+end,1),encoding="utf8")
print("Stage 13: custom menu background installed after all 171 species and evolution items")
