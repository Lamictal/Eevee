#!/usr/bin/env python3
"""Append Stage 8M catalyst and progression patch after Stage 8L build steps."""
from pathlib import Path

file = Path(__file__).parent / "kit" / "build_stage8d.py"
original = file.read_text(encoding="utf-8")
old = "    run([sys.executable, str(ROOT.parent/'stage8l_eevee_evolution.py'), str(dest)])\n"
end = "    buildlog=ROOT/'stage8d_build.log'\n"
added = "    run([sys.executable, str(ROOT.parent/'stage8m_catalyst_evolutions.py'), str(dest)])\n"
if original.count(old + end) != 1 or added in original:
    raise SystemExit("Unexpected Stage 8L source build order; refusing unsafe patch")
file.write_text(original.replace(old + end, old + added + end, 1), encoding="utf-8")
print("Stage 8M appended after 8L, before compilation")
