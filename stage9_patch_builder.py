#!/usr/bin/env python3
"""Append balanced Hoenn encounters and shop stocks after Stage 8M."""
from pathlib import Path
p=Path(__file__).parent/"kit"/"build_stage8d.py"
s=p.read_text(encoding="utf-8")
old="    run([sys.executable, str(ROOT.parent/'stage8m_catalyst_evolutions.py'), str(dest)])\n"
end="    buildlog=ROOT/'stage8d_build.log'\n"
add="    run([sys.executable, str(ROOT.parent/'stage9_world_balance.py'), str(dest)])\n"
if s.count(old+end)!=1 or add in s:
    raise SystemExit("Unexpected Stage 8M builder layout")
p.write_text(s.replace(old+end,old+add+end,1),encoding="utf-8")
print("Stage 9 balanced wild encounters and item stocks integrated")
