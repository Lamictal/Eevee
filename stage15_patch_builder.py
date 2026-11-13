#!/usr/bin/env python3
"""Stage 15: append solo National Dex habitats and restored Birch trio after UI."""
from pathlib import Path
p=Path(__file__).resolve().parent/'kit'/'build_stage8d.py'
s=p.read_text(encoding='utf8')
anchor="    run([sys.executable, str(ROOT.parent/'stage14_title_ui.py'), str(dest)])\n"
end="    buildlog=ROOT/'stage8d_build.log'\n"
added="    run([sys.executable, str(ROOT.parent/'stage15_solo_dex.py'), str(dest)])\n"
if s.count(anchor+end)!=1 or added in s:
    raise SystemExit('Stage 14 build chain changed; refusing to modify')
p.write_text(s.replace(anchor+end,anchor+added+end,1),encoding='utf8')
print('Stage 15: restoring native Birch starters and solo National habitats after the title fix')
