#!/usr/bin/env python3
"""Wire Stage 8H configuration into the Stage 8D-based cloud build."""
from pathlib import Path

file=Path(__file__).parent/'kit'/'build_stage8d.py'
text=file.read_text(encoding='utf-8')
anchor="    buildlog=ROOT/'stage8d_build.log'\n"
prior="    run([sys.executable, str(ROOT.parent/'stage8g_encounters_quickrun.py'), str(dest)])\n"
insert="    run([sys.executable, str(ROOT.parent/'stage8h_followers_ivev.py'), str(dest)])\n"
if text.count(anchor)!=1 or text.count(prior)!=1 or insert in text:
    raise SystemExit("Unexpected builder layout: refusing to change")
needle=prior+anchor
if text.count(needle)!=1:
    raise SystemExit("Could not find expected Stage 8G build hook")
file.write_text(text.replace(needle,prior+insert+anchor,1),encoding='utf-8')
print("Stage 8H following Pokémon and IV/EV config hook installed")
