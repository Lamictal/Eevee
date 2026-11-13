#!/usr/bin/env python3
"""Stage 16: unique PC/party box icons for imported 171 Eeveelution forms.

Stage 10's original importer used .iconSprite = gMonIcon_Eevee for its
custom species, so otherwise correctly named Artheon and other forms
all display the same placeholder. Derive each icon from that species'
already imported original front sprite, reusing the Stage 8I palette
converter. The original front/back sprites and save IDs are untouched.
"""
import argparse
import json
import re
from pathlib import Path

from PIL import Image
from stage8i_sprites import make_icons


def patch(checkout: Path):
    root=checkout.resolve()
    if not (root/'Makefile').exists():
        raise ValueError('Need Emerald Expansion checkout')
    repo=Path(__file__).resolve().parent
    manifest=json.loads((repo/'stage10'/'manifest.json').read_text(encoding='utf-8'))
    forms=manifest['forms']
    if len(forms)!=171:
        raise ValueError('Expected complete 171-form roster')

    species_file=root/'src/data/pokemon/species_info.h'
    gfx_file=root/'src/data/graphics/pokemon.h'
    header_file=root/'include/graphics.h'
    species=species_file.read_text(encoding='utf-8')
    graphics=gfx_file.read_text(encoding='utf-8')
    header=header_file.read_text(encoding='utf-8')
    gfx_anchor='const u32 gMonFrontPic_Egg[]'
    header_anchor='extern const u16 gMonIconPalettes[][16];'
    if graphics.count(gfx_anchor)!=1 or header.count(header_anchor)!=1:
        raise ValueError('Icon graphics/declaration insertion anchors changed')
    if 'STAGE16_FORM_ICONS' in species or 'STAGE16_FORM_ICONS' in graphics:
        raise ValueError('Stage 16 custom icon patch already applied')

    todo=[]
    for form in forms:
        name=form['name']
        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9]*', name):
            raise ValueError(f'Unsafe form name {name!r}')
        symbol='SPECIES_'+name.upper()
        marker='['+symbol+'] ='
        if marker not in species:
            # Canonical Eeveelutions use the engine's real existing icons.
            if form.get('national_dex',0)<=1025:
                continue
            raise ValueError(f'Custom Eeveelution {name} not imported')
        start=species.index(marker)
        end=species.find('\n    },',start)
        if end<0:
            raise ValueError(f'Cannot delimit species definition for {name}')
        block=species[start:end]
        placeholder='.iconSprite = gMonIcon_Eevee,'
        if placeholder not in block:
            # Aerieon/Aerartheon already received dedicated Stage 8I icons.
            if re.search(r'\.iconSprite\s*=\s*gMonIcon_'+re.escape(name)+r'\s*,', block):
                continue
            raise ValueError(f'{name}: neither dedicated icon nor expected placeholder')
        if block.count(placeholder)!=1 or block.count('.iconPalIndex = 0,')!=1:
            raise ValueError(f'{name}: ambiguous placeholder icon setup')
        folder=root/'graphics/pokemon'/name.lower()
        front=folder/'front.png'
        if not front.is_file() or (folder/'icon.png').exists():
            raise ValueError(f'{name}: missing front art or conflicting existing icon')
        with Image.open(front) as img:
            if img.mode!='P' or img.size!=(64,64) or img.getpixel((0,0))!=0:
                raise ValueError(f'{name}: unexpected original-art sprite format')
        todo.append((name, folder, start, end))

    # There should be 161 newly imported custom forms, plus the two Stage 8I
    # prototypes, and eight preexisting official Eeveelution species.
    if len(todo)<150 or len(todo)>163:
        raise ValueError(f'Unexpected number of Eevee icon placeholders: {len(todo)}')

    registrations=[]
    declarations=[]
    updated=species
    for name,folder,_,_ in todo:
        with Image.open(folder/'front.png') as img:
            palette_id=make_icons(root,name.lower(),img.copy())
        marker='[SPECIES_'+name.upper()+'] ='
        start=updated.index(marker)
        end=updated.find('\n    },',start)
        block=updated[start:end]
        block=block.replace('.iconSprite = gMonIcon_Eevee,',
                            '.iconSprite = gMonIcon_'+name+', // STAGE16_FORM_ICONS',1)
        block=block.replace('.iconPalIndex = 0,',
                            '.iconPalIndex = '+str(palette_id)+',',1)
        updated=updated[:start]+block+updated[end:]
        registrations.append(
            f'const u8 gMonIcon_{name}[] = INCGFX_U8("graphics/pokemon/{name.lower()}/icon.png", ".4bpp");\n')
        declarations.append(f'extern const u8 gMonIcon_{name}[];\n')

    species_file.write_text(updated,encoding='utf-8')
    gfx_file.write_text(graphics.replace(gfx_anchor,
        '// STAGE16_FORM_ICONS: each imported Eeveelution has a matching PC/party icon\n'
        +''.join(registrations)+'\n'+gfx_anchor,1),encoding='utf-8')
    header_file.write_text(header.replace(header_anchor,
        '// STAGE16_FORM_ICONS: unique imported icons\n'
        +''.join(declarations)+header_anchor,1),encoding='utf-8')
    (repo/'stage16_icon_report.json').write_text(json.dumps({
        'generated_icons':len(todo),'species':[name for name,_,_,_ in todo],
        'preserved': ['Aerieon','Aerartheon']},indent=2)+'\n',encoding='utf-8')
    print(f'Stage 16: regenerated {len(todo)} custom PC/party icons from matching front art.')
    print('Stage 16: Artheon and other imported forms no longer use Eevee placeholder icons.')
    print('Stage 16: no front/back sprite, form ID, stat, evolution or save layout changes.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('checkout',type=Path)
    patch(parser.parse_args().checkout)
