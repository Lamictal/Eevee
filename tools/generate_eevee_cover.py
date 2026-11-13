#!/usr/bin/env python3
"""Generate optional emulator cover PNGs from the project's existing title artwork.

GBA files have no standard cover-image field. These are companion images,
not embedded artwork or a replacement for an emulator's cover-library API.
"""
from pathlib import Path
import argparse
import sys
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from stage14_title_ui import source_image

NAVY = (22, 19, 60)
PURPLE = (37, 27, 76)
GOLD = (252, 209, 108)
LIGHT = (247, 235, 221)

def getfont(size):
    for candidate in (
        '/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf',
        '/usr/share/fonts/truetype/liberation2/LiberationMono-Bold.ttf',
    ):
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            pass
    return ImageFont.load_default()

def center(draw, text, y, size, color):
    f = getfont(size)
    box = draw.textbbox((0, 0), text, font=f)
    x = (512 - (box[2] - box[0])) // 2
    draw.text((x + 2, y + 2), text, font=f, fill=(8, 7, 24))
    draw.text((x, y), text, font=f, fill=color)

def background(height):
    canvas = Image.new('RGB', (512, height), NAVY)
    d = ImageDraw.Draw(canvas)
    for y in range(height):
        t = y / max(1, height - 1)
        d.line((0, y, 511, y), fill=(round(16 + 25*t), round(19 + 8*t), round(63 + 8*t)))
    return canvas

def border(d, rect):
    d.rectangle(rect, outline=(112, 99, 185), width=4)
    d.rectangle((rect[0]+9,rect[1]+9,rect[2]-9,rect[3]-9), outline=GOLD, width=2)

def render(out):
    source = source_image(ROOT)
    if source.size != (240, 160):
        raise ValueError('Unexpected supplied title art dimensions')
    # Remove the old PRESS START and footer only; keep the original Pokémon/Eevee
    # wordmark, Eeveelution silhouettes, and Eevee standing on the coast.
    art = source.crop((0, 0, 240, 135))
    art = art.resize((500, 281), Image.Resampling.NEAREST)

    square = background(512)
    square.paste(art, (6, 83))
    d = ImageDraw.Draw(square)
    d.rectangle((5,5,506,76), fill=NAVY)
    border(d, (5,5,506,76))
    center(d, 'GBA  ·  FAN EDITION', 25, 25, GOLD)
    d.rectangle((5,369,506,506), fill=NAVY)
    border(d, (5,369,506,506))
    center(d, '171 FORMS  ·  HOENN', 397, 21, LIGHT)
    center(d, 'MONOAMINE  2026', 447, 25, GOLD)

    portrait = background(768)
    portrait.paste(art, (6, 211))
    d = ImageDraw.Draw(portrait)
    border(d, (5,5,506,761))
    d.rectangle((19,23,492,83),fill=NAVY)
    d.rectangle((19,23,492,83),outline=GOLD,width=2)
    center(d, 'GAME BOY ADVANCE', 35, 25, GOLD)
    center(d, 'UNOFFICIAL EMERALD EXPANSION', 107, 14, LIGHT)
    center(d, '171 EEVEE EVOLUTIONS', 165, 19, GOLD)
    d.rectangle((5,210,506,492),outline=GOLD,width=3)
    center(d, 'EXPLORE. EVOLVE. COLLECT.', 530, 18, LIGHT)
    d.rectangle((34,590,478,676),fill=NAVY,outline=GOLD,width=3)
    center(d, 'MONOAMINE', 600, 32, GOLD)
    center(d, '2026 · ALPHA EDITION', 645, 16, LIGHT)
    center(d, 'UNOFFICIAL FAN PROJECT', 704, 14, (209,188,218))

    out.mkdir(parents=True, exist_ok=True)
    square.save(out/'pokemon_eevee_thumbnail.png',optimize=True)
    square.resize((256,256),Image.Resampling.NEAREST).save(out/'pokemon_eevee_thumbnail_256.png',optimize=True)
    portrait.save(out/'pokemon_eevee_gba_cover.png',optimize=True)
    (out/'COVER_README.txt').write_text(
        'Pokémon Eevee fan-project emulator cover images, Monoamine 2026.\n'
        'Set these separately in your emulator cover manager if supported.\n'
        'A standard GBA ROM has no embedded cover field; loading the ROM may\n'
        'require manual artwork association. Unofficial fan project.\n',
        encoding='utf8'
    )
    print('Created three optional emulator cover PNGs.')

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=ROOT/'cover')
    render(parser.parse_args().out)
