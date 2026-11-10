#!/usr/bin/env python3
"""Stage 8E build hotfix for the prototype's two static animation entries.

Uses the engine's existing sAnims_SingleFramePlaceHolder table rather than embedding ANIM_FRAMES
in our custom species entries. Assert exactly two replacements to avoid touching
unexpected future source revisions.
"""
from pathlib import Path

file = Path(__file__).parent / "kit" / "install_stage8c.py"
text = file.read_text(encoding="utf-8")
old = ".frontAnimFrames = ANIM_FRAMES(ANIMCMD_FRAME(0, 1)),"
new = ".frontAnimFrames = sAnims_SingleFramePlaceHolder,"
count = text.count(old)
if count != 2:
    raise SystemExit(f"Unexpected sprite animation definitions: found {count}, expected 2; refusing modification")
file.write_text(text.replace(old, new), encoding="utf-8")
print("Patched Aerieon and Aerartheon to use sAnims_SingleFramePlaceHolder, the expansion engine's static sprite-animation table.")
