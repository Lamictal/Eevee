#!/usr/bin/env python3
"""Enable Unbound-like type indicators using native pokeemerald-expansion settings.

Run with the path to an expansion checkout after the species installer and
before make. Only the two battle UI config defines are edited.
"""
import argparse
from pathlib import Path
import re


def enable(checkout: Path):
    config = checkout / 'include' / 'config' / 'battle.h'
    text = config.read_text(encoding='utf-8')
    rules = {
        'B_SHOW_TYPES': ('SHOW_TYPES_ALWAYS', {
            'SHOW_TYPES_NEVER', 'SHOW_TYPES_SEEN', 'SHOW_TYPES_CAUGHT', 'SHOW_TYPES_ALWAYS'}),
        'B_SHOW_EFFECTIVENESS': ('SHOW_EFFECTIVENESS_ALWAYS', {
            'SHOW_EFFECTIVENESS_NEVER', 'SHOW_EFFECTIVENESS_SEEN',
            'SHOW_EFFECTIVENESS_CAUGHT', 'SHOW_EFFECTIVENESS_ALWAYS'}),
    }
    edited = text
    for name, (replacement, accepted) in rules.items():
        regex = re.compile(rf'^(#define\s+{re.escape(name)}\s+)(\S+)([^\n]*)$', re.M)
        matches = list(regex.finditer(edited))
        if len(matches) != 1:
            raise SystemExit(f'Refusing to edit: expected one {name} define, got {len(matches)}')
        current = matches[0].group(2)
        if current not in accepted:
            raise SystemExit(f'Refusing to edit: unexpected {name} value {current!r}')
        edited = regex.sub(lambda m: m.group(1) + replacement + m.group(3), edited, count=1)
    if edited != text:
        config.write_text(edited, encoding='utf-8')
    print('Battle UI: B_SHOW_TYPES=SHOW_TYPES_ALWAYS')
    print('Battle UI: B_SHOW_EFFECTIVENESS=SHOW_EFFECTIVENESS_ALWAYS')
    print('Native effectiveness labels replace PP during move selection; L opens move details.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkout', type=Path)
    args = parser.parse_args()
    enable(args.checkout.resolve())
