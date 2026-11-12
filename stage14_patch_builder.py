#!/usr/bin/env python3
"""Attach Stage 14 native title and matching menu art after Stage 13."""
from pathlib import Path

p = Path(__file__).resolve().parent / "kit" / "build_stage8d.py"
s = p.read_text(encoding="utf8")
anchor = "    run([sys.executable, str(ROOT.parent/'stage13_custom_menu.py'), str(dest)])\n"
end = "    buildlog=ROOT/'stage8d_build.log'\n"
addition = "    run([sys.executable, str(ROOT.parent/'stage14_title_ui.py'), str(dest)])\n"
if s.count(anchor + end) != 1 or addition in s:
    raise SystemExit("Stage 13 builder sequence differs; refusing unsafe patch")
p.write_text(s.replace(anchor + end, anchor + addition + end, 1), encoding="utf8")
print("Stage 14 source-based Eevee title art and menu backdrops enabled")
