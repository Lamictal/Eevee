#!/usr/bin/env python3
"""Apply Stage 8K balance and starter changes after all Stage 8J patches."""
from pathlib import Path
f=Path(__file__).parent/'kit'/'build_stage8d.py'
s=f.read_text(encoding='utf-8')
old="    run([sys.executable, str(ROOT.parent/'stage8j_pokedex.py'), str(dest)])\n"
added="    run([sys.executable, str(ROOT.parent/'stage8k_starter_balance.py'), str(dest)])\n"
end="    buildlog=ROOT/'stage8d_build.log'\n"
if s.count(old+end)!=1 or added in s:
    raise SystemExit('Unknown Stage 8J build arrangement')
f.write_text(s.replace(old+end,old+added+end,1),encoding='utf-8')
print('Stage 8K patched into cloud source builder')
