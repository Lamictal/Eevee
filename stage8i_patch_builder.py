#!/usr/bin/env python3
"""Add Stage 8I party icons and overworld sprites after preceding custom patches."""
from pathlib import Path
file=Path(__file__).parent/'kit'/'build_stage8d.py'
data=file.read_text(encoding='utf-8')
before="    run([sys.executable, str(ROOT.parent/'stage8h_followers_ivev.py'), str(dest)])\n"
after="    run([sys.executable, str(ROOT.parent/'stage8i_sprites.py'), str(dest)])\n"
anchor="    buildlog=ROOT/'stage8d_build.log'\n"
if data.count(before+anchor)!=1 or after in data:
    raise SystemExit('Unexpected build installer layout')
file.write_text(data.replace(before+anchor,before+after+anchor,1),encoding='utf-8')
print('Stage 8I icon and overworld sprite install hooked into cloud build')
