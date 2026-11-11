#!/usr/bin/env python3
"""Append Stage 8L evolution patch to the validated Stage 8K cloud builder."""
from pathlib import Path

path = Path(__file__).parent / "kit" / "build_stage8d.py"
original = path.read_text(encoding="utf-8")
old = "    run([sys.executable, str(ROOT.parent/'stage8k_starter_balance.py'), str(dest)])\n"
end = "    buildlog=ROOT/'stage8d_build.log'\n"
new = "    run([sys.executable, str(ROOT.parent/'stage8l_eevee_evolution.py'), str(dest)])\n"
if original.count(old + end) != 1 or new in original:
    raise SystemExit("Unknown Stage 8K build sequence; refusing duplicate or misplaced patch")
path.write_text(original.replace(old + end, old + new + end, 1), encoding="utf-8")
print("Stage 8L included after Stage 8K and before compilation.")
