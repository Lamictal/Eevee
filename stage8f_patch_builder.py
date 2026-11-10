#!/usr/bin/env python3
"""Call the Stage 8F UI configurator before compiling the expansion source.

Run in repository root after unpacking kit/. Asserts exactly one insertion anchor.
"""
from pathlib import Path

file = Path(__file__).parent / 'kit' / 'build_stage8d.py'
text = file.read_text(encoding='utf-8')
anchor = "    buildlog=ROOT/'stage8d_build.log'\n"
insert = "    run([sys.executable, str(ROOT.parent/'stage8f_enable_battle_ui.py'), str(dest)])\n"
if insert in text:
    raise SystemExit('Stage 8F builder already patched; refusing a second injection')
if text.count(anchor) != 1:
    raise SystemExit(f'Unexpected builder layout: found {text.count(anchor)} anchors, expected 1')
file.write_text(text.replace(anchor, insert + anchor), encoding='utf-8')
print('Stage 8F builder hook inserted (after species installation, before make).')
