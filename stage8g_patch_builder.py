#!/usr/bin/env python3
"""Inject Stage 8G changes after Stage 8F hook and before make."""
from pathlib import Path

file=Path(__file__).parent/'kit'/'build_stage8d.py'
text=file.read_text(encoding='utf-8')
anchor="    buildlog=ROOT/'stage8d_build.log'\n"
ui_call="    run([sys.executable, str(ROOT.parent/'stage8f_enable_battle_ui.py'), str(dest)])\n"
insert="    run([sys.executable, str(ROOT.parent/'stage8g_encounters_quickrun.py'), str(dest)])\n"
if text.count(anchor)!=1 or text.count(ui_call)!=1 or insert in text:
    raise SystemExit('Unknown builder layout or duplicate patch; refusing changes')
file.write_text(text.replace(ui_call+anchor,ui_call+insert+anchor,1),encoding='utf-8')
print('Stage 8G compiler hook installed after battle UI configuration')
