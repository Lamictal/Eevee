#!/usr/bin/env python3
"""Stage 13: Eevee-themed main menu art without changing main-menu state logic.

Create an original GBA-compatible 4bpp background from simple vector shapes.
Menu actions (Continue/New Game/Options), save-file checks, Mystery Gift,
button controls and Birch's intro code remain untouched.
"""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Palette zero is a real background color; tiles explicitly use palette bank 1.
COLORS = [
    (10, 19, 42),   # 0 midnight
    (18, 29, 60),   # 1 navy
    (32, 43, 80),   # 2 steel blue
    (47, 54, 91),   # 3 violet
    (64, 73, 108),  # 4 muted lilac
    (84, 91, 124),  # 5 silver violet
    (139, 119, 157),# 6 plum
    (203, 152, 125),# 7 cocoa rose
    (237, 197, 132),# 8 gold
    (253, 226, 167),# 9 soft cream
    (245, 240, 217),# 10 pearl
    (118, 212, 194),# 11 teal
    (80, 158, 173), # 12 deep teal
    (87, 60, 79),   # 13 shadow brown
    (148, 91, 91),  # 14 brown
    (232, 143, 152),# 15 rose
]

def index(rgb):
    return min(range(16), key=lambda i: sum((rgb[k]-COLORS[i][k])**2 for k in range(3)))

def font(size):
    for name in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                 "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"):
        try:
            return ImageFont.truetype(name,size=size)
        except OSError:
            pass
    return ImageFont.load_default()

def create_art(path):
    image=Image.new("RGB",(256,256), COLORS[0])
    d=ImageDraw.Draw(image)
    # Pixel-friendly twilight/aurora gradient, entirely GBA 4bpp.
    for y in range(160):
        c=COLORS[(1 if y<32 else 2 if y<90 else 3 if y<135 else 1)]
        d.line((0,y,255,y),fill=c)
    # A ribbon of starlight behind the selectable menus.
    d.polygon([(0,103),(24,92),(64,102),(95,87),(136,94),(177,84),
               (224,104),(255,99),(255,160),(0,160)], fill=COLORS[2])
    d.polygon([(0,136),(46,124),(91,138),(147,120),(192,132),(255,119),
               (255,160),(0,160)],fill=COLORS[3])
    # Stars and type-color sparkles.
    for x,y,r,c in [(14,24,2,9),(215,26,3,11),(181,41,2,8),(222,78,2,9),
                    (25,88,2,15),(200,104,3,8),(232,143,2,11),
                    (110,26,2,11),(48,52,2,8),(157,12,2,15)]:
        d.line((x-r,y,x+r,y),fill=COLORS[c],width=1)
        d.line((x,y-r,x,y+r),fill=COLORS[c],width=1)
    # Original stylized fox silhouette, not extracted third-party artwork.
    # Tail, body, pointed ears, face, ruff, paws.
    d.polygon([(176,128),(199,97),(224,89),(235,104),(227,129),
               (214,146),(189,150)],fill=COLORS[13])
    d.polygon([(174,124),(196,102),(215,94),(222,102),
               (213,115),(197,126)],fill=COLORS[8])
    d.ellipse((109,77,191,147),fill=COLORS[14],outline=COLORS[13],width=2)
    d.polygon([(118,88),(122,29),(148,64),(157,73)],fill=COLORS[13])
    d.polygon([(163,71),(187,25),(184,99),(177,103)],fill=COLORS[13])
    d.polygon([(127,78),(127,43),(145,75)],fill=COLORS[15])
    d.polygon([(167,80),(183,43),(179,87)],fill=COLORS[15])
    d.ellipse((117,68,186,120),fill=COLORS[8],outline=COLORS[13],width=2)
    d.polygon([(111,110),(123,103),(134,116),(143,110),(154,124),
               (164,111),(176,115),(183,105),(188,126),(173,139),
               (156,133),(140,143),(124,132)],fill=COLORS[9])
    d.ellipse((134,87,141,93),fill=COLORS[0])
    d.ellipse((165,87,172,93),fill=COLORS[0])
    d.polygon([(150,98),(159,98),(155,103)],fill=COLORS[13])
    d.line((155,103,155,107),fill=COLORS[13],width=1)
    d.line((145,107,151,110,155,107,160,110,166,107),fill=COLORS[13],width=1)
    d.ellipse((122,132,142,151),fill=COLORS[13])
    d.ellipse((162,132,184,152),fill=COLORS[13])
    # A custom title/signature displayed below main-menu selection windows.
    d.rectangle((8,127,123,159),fill=COLORS[0],outline=COLORS[11],width=1)
    d.text((13,128),"EEVEE",font=font(19),fill=COLORS[9],stroke_width=0)
    d.text((13,148),"171 FORMS",font=font(10),fill=COLORS[11])
    d.line((6,124,98,124),fill=COLORS[8],width=2)
    # GBA 4bpp tile order: 32x32 tiles, each tile 8x8, packed two pixels/byte.
    # Tile graphics must fit BEFORE BG1 screenblock 7 (0x3800):
    # 448 distinct tiles maximum, not 1024 sequential tiles.
    raw=bytearray()
    tilemap=bytearray()
    tile_ids={}
    for ty in range(32):
        for tx in range(32):
            tile=bytearray()
            for py in range(8):
                for px in range(0,8,2):
                    i0=index(image.getpixel((tx*8+px,ty*8+py)))
                    i1=index(image.getpixel((tx*8+px+1,ty*8+py)))
                    tile.append(i0 | i1<<4)
            tile=bytes(tile)
            if tile not in tile_ids:
                tile_ids[tile]=len(tile_ids)
                raw.extend(tile)
            tilemap.extend((tile_ids[tile]|0x1000).to_bytes(2,"little"))
    if len(raw)>0x3800 or len(raw)%32 or len(tilemap)!=2048:
        raise ValueError(f"Background overlaps tilemap: {len(tile_ids)} unique tiles")
    path.joinpath("eevee_menu_bg.4bpp").write_bytes(raw)
    path.joinpath("eevee_menu_bg.bin").write_bytes(tilemap)
    palette=bytearray()
    for r,g,b in COLORS:
        n=((r*31//255)&31)|(((g*31//255)&31)<<5)|(((b*31//255)&31)<<10)
        palette.extend(n.to_bytes(2,"little"))
    path.joinpath("eevee_menu_bg.gbapal").write_bytes(palette)
    # Preview is intentionally local build collateral, not a runtime resource.
    image.crop((0,0,240,160)).save(path.joinpath("eevee_menu_preview.png"))
    return len(raw),len(tilemap),len(palette)

def patch(root: Path):
    root=root.resolve()
    if not (root/"Makefile").exists():
        raise ValueError("Expected pokeemerald-expansion checkout")
    source=root/"src/main_menu.c"
    original=source.read_text(encoding="utf8")
    if "STAGE13_EEVEE_MENU" in original:
        raise ValueError("Stage 13 already installed")
    gfx=root/"graphics/interface"
    gfx.mkdir(parents=True,exist_ok=True)
    sizes=create_art(gfx)
    if not (32<=sizes[0]<=0x3800 and sizes[1:]==(2048,32)):
        raise AssertionError("Invalid GBA background data sizes")

    anchor='static const u16 sMainMenuTextPal[] = INCGFX_U16("graphics/interface/main_menu_text.pal", ".gbapal");'
    declaration=(
      '\n\n// STAGE13_EEVEE_MENU: independently authored 4bpp GBA artwork.\n'
      'static const u8 sEeveeMenuBackgroundTiles[] = INCBIN_U8("graphics/interface/eevee_menu_bg.4bpp");\n'
      'static const u16 sEeveeMenuBackgroundMap[] = INCBIN_U16("graphics/interface/eevee_menu_bg.bin");\n'
      'static const u16 sEeveeMenuBackgroundPalette[] = INCBIN_U16("graphics/interface/eevee_menu_bg.gbapal");'
    )
    if original.count(anchor)!=1:
        raise ValueError("Original main-menu graphics declarations have changed")
    modified=original.replace(anchor,anchor+declaration,1)
    bgs="    InitBgsFromTemplates(0, sMainMenuBgTemplates, ARRAY_COUNT(sMainMenuBgTemplates));"
    addition=(
      "\n    // Eevee backdrop occupies BG1 charblock 0 and palette bank 1.\n"
      "    // Existing menu text and selection graphics remain on BG0.\n"
      "    LoadBgTiles(1, sEeveeMenuBackgroundTiles, sizeof(sEeveeMenuBackgroundTiles), 0);\n"
      "    LoadBgTilemap(1, sEeveeMenuBackgroundMap, sizeof(sEeveeMenuBackgroundMap), 0);\n"
      "    LoadPalette(sEeveeMenuBackgroundPalette, BG_PLTT_ID(1), PLTT_SIZE_4BPP);"
    )
    if modified.count(bgs)!=1: raise ValueError("Main BG templates changed")
    modified=modified.replace(bgs,bgs+addition,1)
    showing="    ShowBg(0);\n    HideBg(1);\n    CreateTask(Task_MainMenuCheckSaveFile, 0);"
    if modified.count(showing)!=1:
        raise ValueError("Main-menu BG visibility anchor changed")
    modified=modified.replace(showing,
        "    ShowBg(0);\n    ShowBg(1); // STAGE13_EEVEE_MENU\n"
        "    CreateTask(Task_MainMenuCheckSaveFile, 0);",1)
    for a,b in [
      ('static const u8 gText_MainMenuNewGame[] = _("NEW GAME");',
       'static const u8 gText_MainMenuNewGame[] = _("NEW JOURNEY");'),
      ('static const u8 gText_MainMenuOption[] = _("OPTION");',
       'static const u8 gText_MainMenuOption[] = _("SETTINGS");')
    ]:
        if modified.count(a)!=1:raise ValueError("Menu label anchor changed")
        modified=modified.replace(a,b,1)
    # Preserve all menu selection, error, save and callback paths.
    for mandatory in ["Task_HandleMainMenuAPressed", "Task_HandleMainMenuBPressed",
                      "CB2_ContinueSavedGame", "CB2_InitOptionMenu", "CB2_InitTitleScreen",
                      "Task_NewGameBirchSpeech_Init", "MainMenu_FormatSavegameText"]:
        if mandatory not in modified:
            raise AssertionError("Removed menu functionality: "+mandatory)
    source.write_text(modified,encoding="utf8")
    print("Stage 13: original custom Eevee background installed in GBA main menu.")
    print("Stage 13: NEW JOURNEY / CONTINUE / SETTINGS retain original button callbacks.")
    print("Stage 13: deduplicated 4bpp tiles fit BG1 charblock before screenblock 7; no save changes.")

if __name__=="__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("checkout",type=Path)
    patch(ap.parse_args().checkout)
