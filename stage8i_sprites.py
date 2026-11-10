#!/usr/bin/env python3
"""Stage 8I: species-specific party icons and follower graphics.

Generate provisional six-frame 32px overworld sheets from ORIGINAL species art
already in the private source kit. Requires python3-pil. This does not alter
species IDs or save layout. Replacement art is intentionally provisional.
"""
from pathlib import Path
from PIL import Image
import argparse
import re
import shutil

CUSTOM = ("Aerieon", "Aerartheon")
FRAMES = 6

def palette(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[:3] == ["JASC-PAL", "0100", "16"], path
    return [tuple(map(int, line.split())) for line in lines[3:19]]

def image_p(size, colors):
    img = Image.new("P", size, 0)
    img.putpalette([v for rgb in colors for v in rgb] + [0] * ((256 - len(colors)) * 3))
    return img

def scaled_sprite(source, maxw, maxh, flip=False):
    transparent = source.getpixel((0, 0))
    bbox = source.point(lambda x: 255 if x != transparent else 0).getbbox()
    if bbox is None:
        raise ValueError("Empty custom sprite")
    cropped = source.crop(bbox)
    if flip:
        cropped = cropped.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
    scale = min(maxw / cropped.width, maxh / cropped.height)
    sz = (max(1, round(cropped.width * scale)), max(1, round(cropped.height * scale)))
    return cropped.resize(sz, Image.Resampling.NEAREST), transparent

def distance(a, b):
    return 2 * (a[0] - b[0]) ** 2 + 3 * (a[1] - b[1]) ** 2 + 3 * (a[2] - b[2]) ** 2

def make_icons(checkout, species, front):
    source_pal = front.getpalette()
    cropped, bg = scaled_sprite(front, 29, 27)
    rgb_pixels = [tuple(source_pal[v*3:v*3+3]) for v in cropped.getdata() if v != bg]
    candidates = {i: palette(checkout / "graphics/pokemon/icon_palettes" / f"pal{i}.pal") for i in range(6)}
    best = min(candidates, key=lambda k: sum(min(distance(rgb, c) for c in candidates[k][1:]) for rgb in rgb_pixels))
    colors = candidates[best]
    icon = image_p((32, 64), colors)
    remap = {
        i: min(range(1,16), key=lambda j: distance(tuple(source_pal[3*i:3*i+3]), colors[j]))
        for i in range(16) if i != bg
    }
    for frame in range(2):
        x = (32 - cropped.width)//2 + frame
        y = frame*32 + (32-cropped.height)//2 - frame
        for yy in range(cropped.height):
            for xx in range(cropped.width):
                v = cropped.getpixel((xx, yy))
                if v != bg:
                    icon.putpixel((x+xx,y+yy),remap[v])
    icon.save(checkout/"graphics/pokemon"/species/"icon.png",optimize=True)
    return best

def make_overworld(checkout, species, front):
    directory = checkout / "graphics/pokemon" / species
    normal = palette(directory / "normal.pal")
    atlas = image_p((192, 32), normal)
    for frame in range(FRAMES):
        # Down/down-step, up/up-step, and side/side-step.
        # Derived from original artwork. True three-angle art is a later polish item.
        maxw,maxh = (23,23) if frame >= 4 else (28,26)
        piece, bg = scaled_sprite(front, maxw, maxh, flip=frame in (3,5))
        x = frame*32 + (32-piece.width)//2 - (1 if frame in (1,3) else 0)
        y = 31-piece.height - (1 if frame in (1,3,5) else 0)
        for yy in range(piece.height):
            for xx in range(piece.width):
                v = piece.getpixel((xx,yy))
                if v != bg:
                    atlas.putpixel((x+xx,y+yy),v)
    atlas.save(directory/"overworld.png",optimize=True)
    shutil.copyfile(directory/"normal.pal",directory/"overworld_normal.pal")
    shutil.copyfile(directory/"shiny.pal",directory/"overworld_shiny.pal")

def replace_one(file, needle, inserted):
    current = file.read_text(encoding="utf-8")
    if current.count(needle) != 1 or "STAGE8I_GRAPHICS" in current:
        raise ValueError(f"Unexpected file/duplicate sprite patch: {file}")
    file.write_text(current.replace(needle,inserted+needle,1),encoding="utf-8")

def install(root):
    root = root.resolve()
    if not (root/"Makefile").is_file():
        raise ValueError("Expected expansion source Makefile")
    species_file = root/"src/data/pokemon/species_info.h"
    source = species_file.read_text(encoding="utf-8")
    if "STAGE8C_CUSTOM_EEVEE_PROTO" not in source or "STAGE8I_GRAPHICS" in source:
        raise ValueError("Expected fresh Stage 8C species install")
    start = source.index("    // STAGE8C_CUSTOM_EEVEE_PROTO",source.index("const struct SpeciesInfo"))
    end = source.index("    /* You may add any custom species below this point",start)
    region = source[start:end]
    if region.count(".iconSprite = gMonIcon_Eevee") != 2:
        raise ValueError("Expected two temporary Eevee icons")

    # Validate all target data and format before touching anything.
    data = {}
    for name in CUSTOM:
        key = name.lower()
        directory = root/"graphics/pokemon"/key
        front = Image.open(directory/"front.png")
        if front.size != (64,64) or front.mode != "P" or front.getpixel((0,0)) != 0:
            raise ValueError(f"Unexpected input art {name}")
        data[name] = front.copy()
        for suffix in ("icon.png","overworld.png","overworld_normal.pal","overworld_shiny.pal"):
            if (directory/suffix).exists():
                raise ValueError(f"Refusing to overwrite existing {name}/{suffix}")

    # Native sprite reference definitions, without altering official species gfx.
    defs = "\n// STAGE8I_GRAPHICS: original-art-derived custom icons and follower sheets\n"
    for name in CUSTOM:
        key=name.lower()
        defs+=(
            f'const u8 gMonIcon_{name}[] = INCGFX_U8("graphics/pokemon/{key}/icon.png", ".4bpp");\n'
            f'#if OW_POKEMON_OBJECT_EVENTS\n'
            
            f'#if OW_PKMN_OBJECTS_SHARE_PALETTES == FALSE\n'
            f'const u16 gOverworldPalette_{name}[] = INCGFX_U16("graphics/pokemon/{key}/overworld_normal.pal", ".gbapal");\n'
            f'const u16 gShinyOverworldPalette_{name}[] = INCGFX_U16("graphics/pokemon/{key}/overworld_shiny.pal", ".gbapal");\n'
            f'#endif\n#endif\n'
        )
    tables = "\n// STAGE8I_GRAPHICS: 32x32 by six frames each, consistent with stock followers\n"
    for name in CUSTOM:
        tables += f"static const struct SpriteFrameImage sPicTable_{name}[] = {{\n    overworld_ascending_frames(gObjectEventPic_{name}, 4, 4),\n}};\n"
    gfx = root/"src/data/graphics/pokemon.h"
    owgfx = root/"src/data/object_events/object_event_graphics.h"
    tablefile=root/"src/data/object_events/object_event_pic_tables_followers.h"
    owdefs = "\n// STAGE8I_GRAPHICS: bespoke follower overworld sprites\n"
    for name in CUSTOM:
        key=name.lower()
        owdefs += f'const u32 gObjectEventPic_{name}[] = INCGFX_U32("graphics/pokemon/{key}/overworld.png", ".4bpp.smol", "-mwidth 4 -mheight 4");\n'
    if gfx.read_text(encoding="utf-8").count("const u32 gMonFrontPic_Egg[]") != 1:
        raise ValueError("Missing graphics insertion anchor")
    if owgfx.read_text(encoding="utf-8").count("const u32 gObjectEventPic_RubySapphireBrendanNormal[]") != 1:
        raise ValueError("Missing overworld graphics anchor")
    if tablefile.read_text(encoding="utf-8").count("static const struct SpriteFrameImage sPicTable_Substitute[]") != 1:
        raise ValueError("Missing follower insertion anchor")
    for name in CUSTOM:
        if region.count(f"[SPECIES_{name.upper()}]") != 1:
            raise ValueError(f"Missing species entry: {name}")

    # Construct the modified species region before writing.
    new_region=region.replace("    // STAGE8C_CUSTOM_EEVEE_PROTO",
                              "    // STAGE8C_CUSTOM_EEVEE_PROTO\n    // STAGE8I_GRAPHICS: custom party icons and overworld followers",1)
    new_region = ("    // STAGE8I_GRAPHICS: custom icon symbol declarations\n" +
                  "    extern const u8 gMonIcon_Aerieon[];\n" +
                  "    extern const u8 gMonIcon_Aerartheon[];\n" +
                  new_region)
    for name in CUSTOM:
        pattern = re.compile(r"(\[SPECIES_"+name.upper()+r"\] = \{)(.*?)(?=\n    \},)",re.S)
        hits=list(pattern.finditer(new_region))
        if len(hits)!=1:
            raise ValueError(f"Can't isolate {name} species")
        block=hits[0].group(0)
        if block.count(".iconSprite = gMonIcon_Eevee")!=1:
            raise ValueError("Unexpected old icon reference")
        best=make_icons(root,name.lower(),data[name])
        make_overworld(root,name.lower(),data[name])
        edited=block.replace(".iconSprite = gMonIcon_Eevee",f".iconSprite = gMonIcon_{name}")
        edited=edited.replace(".iconPalIndex = 0",f".iconPalIndex = {best}",1)
        learn=f"        .levelUpLearnset = s{name}LevelUpLearnset,"
        if edited.count(learn)!=1:
            raise ValueError(f"Unexpected {name} learnset")
        ov=(
            f"        OVERWORLD(\n"
            f"            sPicTable_{name}, SIZE_32x32, SHADOW_SIZE_M, TRACKS_FOOT,\n"
            f"            sAnimTable_Following,\n"
            f"            gOverworldPalette_{name}, gShinyOverworldPalette_{name}\n"
            f"        )\n"
        )
        edited=edited.replace(learn,ov+learn,1)
        new_region=new_region.replace(block,edited,1)
        print(f"{name}: dedicated 32x64 party icon (palette {best}), six 32x32 follower frames")
    replace_one(gfx,"const u32 gMonFrontPic_Egg[]",defs)
    replace_one(owgfx,"const u32 gObjectEventPic_RubySapphireBrendanNormal[]",owdefs)
    replace_one(tablefile,"static const struct SpriteFrameImage sPicTable_Substitute[]",tables)
    species_file.write_text(source[:start]+new_region+source[end:],encoding="utf-8")
    print("Stage 8I graphics installed; no species IDs, dex numbers, or save fields changed.")

if __name__ == "__main__":
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("checkout",type=Path)
    install(cli.parse_args().checkout)
