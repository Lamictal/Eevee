#!/usr/bin/env python3
"""Run Stage 8J National Dex registration after sprites, before compilation."""
from pathlib import Path
file=Path(__file__).parent/'kit'/'build_stage8d.py'
s=file.read_text(encoding='utf-8')
prior="    run([sys.executable, str(ROOT.parent/'stage8i_sprites.py'), str(dest)])\n"
next="    run([sys.executable, str(ROOT.parent/'stage8j_pokedex.py'), str(dest)])\n"
anchor="    buildlog=ROOT/'stage8d_build.log'\n"
if s.count(prior+anchor)!=1 or next in s:
    raise SystemExit('Unexpected prior build hook, refusing Stage 8J injection')
file.write_text(s.replace(prior+anchor,prior+next+anchor,1),encoding='utf-8')
print('Stage 8J save-array-preserving Pokédex installer hooked into build')
