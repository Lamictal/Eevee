#!/usr/bin/env python3
"""Chain Stage 12 dual item effect repairs after the Stage 11 wild habitats."""
from pathlib import Path
p=Path(__file__).parent/"kit"/"build_stage8d.py"
txt=p.read_text(encoding="utf8")
needle="    run([sys.executable, str(ROOT.parent/'stage11_full_ecology.py'), str(dest)])\n"
end="    buildlog=ROOT/'stage8d_build.log'\n"
extra="    run([sys.executable, str(ROOT.parent/'stage12_verify_dual_items.py'), str(dest)])\n"
if txt.count(needle+end)!=1 or extra in txt:
    raise SystemExit("Stage 11 builder hook missing or already patched")
p.write_text(txt.replace(needle+end,needle+extra+end,1),encoding="utf8")
print("Stage 12 dual evolution item repairs appended after Stage 11 habitat patch")
