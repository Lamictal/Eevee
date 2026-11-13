#!/usr/bin/env python3
"""Enable effectiveness hints and convenient Gen 3 in-battle move rearrangement.

Run with an expansion checkout after the species installer and before make.
The engine already supports reordering moves on the Pokemon summary screen;
setting B_MOVE_REARRANGEMENT_IN_BATTLE=GEN_3 also enables Select on the
battle move-selection screen (not link battles). No save layout is changed.
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
        'B_MOVE_REARRANGEMENT_IN_BATTLE': ('GEN_3', {
            'GEN_1', 'GEN_2', 'GEN_3', 'GEN_4', 'GEN_5',
            'GEN_6', 'GEN_7', 'GEN_8', 'GEN_9', 'GEN_LATEST'}),
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
    enable_colored_effectiveness(checkout)
    print('Battle UI: B_SHOW_TYPES=SHOW_TYPES_ALWAYS')
    print('Battle UI: B_SHOW_EFFECTIVENESS=SHOW_EFFECTIVENESS_ALWAYS')
    print('Battle UI: B_MOVE_REARRANGEMENT_IN_BATTLE=GEN_3 (Select swaps move slots).')
    print('Colored effectiveness labels appear alongside remaining PP; L opens move details.')


def enable_colored_effectiveness(checkout: Path):
    """Replace pictographs with color-coded multipliers in the existing PP label.

    Keep native damage/type checks and the regular remaining-PP number untouched.
    Text is limited to three visible characters so it fits the 4-tile label.
    """
    source = checkout / 'src/battle_controller_player.c'
    text = source.read_text(encoding='utf-8')
    old = '''    static const u8 effectiveIcon[] =  _("{CIRCLE_HOLLOW}");
    static const u8 extremeleyEffectiveIcon[] =  _("{STAR}");
    static const u8 superEffectiveIcon[] =  _("{CIRCLE_DOT}");
    static const u8 notVeryEffectiveIcon[] =  _("{TRIANGLE}");
    static const u8 mostlyIneffectiveIcon[] =  _("{TRIANGLE_UPSIDE_DOWN}");
    static const u8 immuneIcon[] =  _("{BIG_MULT_X}");'''
    new = '''    // STAGE8F_COLOR_EFFECTIVENESS: colored, readable multipliers, not symbols.
    static const u8 effectiveIcon[] =  _("{COLOR DYNAMIC_COLOR6}1x");
    static const u8 extremeleyEffectiveIcon[] =  _("{COLOR LIGHT_GREEN}4x");
    static const u8 superEffectiveIcon[] =  _("{COLOR GREEN}2x");
    static const u8 notVeryEffectiveIcon[] =  _("{COLOR LIGHT_RED}1/2");
    static const u8 mostlyIneffectiveIcon[] =  _("{COLOR LIGHT_RED}1/4");
    static const u8 immuneIcon[] =  _("{COLOR LIGHT_BLUE}0x");'''
    if text.count(old) != 1:
        raise ValueError('Unexpected battle effectiveness icon source; aborting patch')
    source.write_text(text.replace(old, new, 1), encoding='utf-8')

    # Battle text uses palette 5. Its slots 5/6/7/9 are originally black
    # and available for colored PP indicators. Do not alter regular PP colors
    # (12/13), window background (14), or text shadow (15).
    palette = checkout / 'graphics/battle_interface/text.pal'
    lines = palette.read_text(encoding='utf-8').splitlines()
    if len(lines) != 19 or lines[:3] != ['JASC-PAL', '0100', '16']:
        raise ValueError('Unexpected 16-color battle text palette')
    colors = {
        5: '217 48 55',   # LIGHT_RED: resisted 1/2x or 1/4x
        6: '21 142 70',   # GREEN: super effective 2x
        7: '14 172 82',   # LIGHT_GREEN: very effective 4x
        9: '54 105 153',  # LIGHT_BLUE: immunity 0x
    }
    for index, rgb in colors.items():
        if lines[index + 3] != '0 0 0':
            raise ValueError(f'Palette slot {index} already in use; aborting patch')
    for index, rgb in colors.items():
        lines[index + 3] = rgb
    palette.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print('Battle UI: effectiveness now uses colored multipliers: 4x/2x green, 1x neutral, 1/2 or 1/4 red, 0x blue.')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkout', type=Path)
    args = parser.parse_args()
    enable(args.checkout.resolve())
