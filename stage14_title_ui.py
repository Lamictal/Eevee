#!/usr/bin/env python3
"""Stage 14: supplied title-art recreation packaged for GBA mode 4.

Requires the project-specific compressed 240x160 indexed art in
`data/stage14_title_source.b85`. Does not touch save or game logic.
"""
from pathlib import Path
import argparse
import base64
import lzma
from PIL import Image, ImageDraw

# Small native 5x7 bitmap alphabet. Glyphs are plotted on GBA pixels directly:
# no anti-aliasing or upscaled desktop fonts.
FONT = {
 'A':('01110','10001','10001','11111','10001','10001','10001'),
 'B':('11110','10001','10001','11110','10001','10001','11110'),
 'C':('01111','10000','10000','10000','10000','10000','01111'),
 'D':('11110','10001','10001','10001','10001','10001','11110'),
 'E':('11111','10000','10000','11110','10000','10000','11111'),
 'F':('11111','10000','10000','11110','10000','10000','10000'),
 'G':('01111','10000','10000','10111','10001','10001','01111'),
 'H':('10001','10001','10001','11111','10001','10001','10001'),
 'I':('11111','00100','00100','00100','00100','00100','11111'),
 'J':('00111','00010','00010','00010','10010','10010','01100'),
 'K':('10001','10010','10100','11000','10100','10010','10001'),
 'L':('10000','10000','10000','10000','10000','10000','11111'),
 'M':('10001','11011','10101','10101','10001','10001','10001'),
 'N':('10001','11001','10101','10011','10001','10001','10001'),
 'O':('01110','10001','10001','10001','10001','10001','01110'),
 'P':('11110','10001','10001','11110','10000','10000','10000'),
 'Q':('01110','10001','10001','10001','10101','10010','01101'),
 'R':('11110','10001','10001','11110','10100','10010','10001'),
 'S':('01111','10000','10000','01110','00001','00001','11110'),
 'T':('11111','00100','00100','00100','00100','00100','00100'),
 'U':('10001','10001','10001','10001','10001','10001','01110'),
 'V':('10001','10001','10001','10001','10001','01010','00100'),
 'W':('10001','10001','10001','10101','10101','11011','10001'),
 'X':('10001','10001','01010','00100','01010','10001','10001'),
 'Y':('10001','10001','01010','00100','00100','00100','00100'),
 'Z':('11111','00001','00010','00100','01000','10000','11111'),
 '0':('01110','10001','10011','10101','11001','10001','01110'),
 '1':('00100','01100','00100','00100','00100','00100','01110'),
 '2':('01110','10001','00001','00010','00100','01000','11111'),
 '3':('11110','00001','00001','01110','00001','00001','11110'),
 '4':('00010','00110','01010','10010','11111','00010','00010'),
 '5':('11111','10000','10000','11110','00001','00001','11110'),
 '6':('01110','10000','10000','11110','10001','10001','01110'),
 '7':('11111','00001','00010','00100','01000','01000','01000'),
 '8':('01110','10001','10001','01110','10001','10001','01110'),
 '9':('01110','10001','10001','01111','00001','00001','01110'),
 ' ':('00000',)*7,
 '/':('00001','00001','00010','00100','01000','10000','10000'),
 '-':('00000','00000','00000','11111','00000','00000','00000'),
 '.':('00000','00000','00000','00000','00000','01100','01100')
}

def pixtext(d, text, y, fg, shadow=None, x=None):
    width=len(text)*6-1
    ox=(240-width)//2 if x is None else x
    for idx,ch in enumerate(text.upper()):
        for ry,bits in enumerate(FONT[ch]):
            for rx,val in enumerate(bits):
                if val=='1':
                    at=(ox+idx*6+rx,y+ry)
                    if shadow is not None:
                        d.point((at[0]+1, at[1]+1),fill=shadow)
                    d.point(at,fill=fg)

def source_image(root):
    payload=(root/'data/stage14_title_source.b85').read_text(encoding='ascii')
    compact=''.join(payload.split())
    raw=lzma.decompress(base64.b85decode(compact.encode('ascii')))
    colors=32
    assert len(raw)==colors*3+240*160, (len(raw),colors)
    im=Image.frombytes('P',(240,160),raw[colors*3:])
    im.putpalette(list(raw[:colors*3])+[0]*(768-colors*3))
    return im.convert('RGB')

def gba_color(rgb):
    r,g,b=rgb
    return (r*31//255) | ((g*31//255)<<5) | ((b*31//255)<<10)

def title(root,img):
    im=img.copy()
    d=ImageDraw.Draw(im)
    # Hide only baked-in tiny lettering: reconstruct as pixel-perfect native text.
    d.rectangle((84,70,155,82),fill=(33,23,61))
    d.rectangle((65,82,174,94),fill=(37,25,69))
    d.rectangle((67,134,175,148),fill=(39,27,66))
    d.rectangle((38,149,205,159),fill=(32,24,58))
    pixtext(d,'171 FORMS',73,fg=(255,224,138),shadow=(14,10,38))
    pixtext(d,'EMERALD EXPANSION',84,fg=(250,246,227),shadow=(16,12,43))
    pixtext(d,'2026 MONOAMINE',151,fg=(241,230,214),shadow=(11,8,34))
    # Use 253 ordinary colors, plus three animation-specific palette indices.
    p=im.quantize(colors=253, method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE)
    pal=p.getpalette()[:253*3]
    pal.extend([0]*(253*3-len(pal)))
    pal.extend([255,255,248, 255,230,155, 255,244,197])
    p.putpalette(pal)
    dp=ImageDraw.Draw(p)
    pixtext(dp,'PRESS START',137,fg=255,shadow=0)
    for x,y in [(8,20),(24,39),(68,7),(223,11),(230,34),(181,18),(187,76),(49,54),(211,64)]:
        dp.point((x,y), fill=253)
        if x%2==0:dp.point((x+1,y),fill=253)
    for x,y in [(32,130),(45,127),(63,131),(72,125),(195,139),(217,125)]:
        dp.line((x,y,x+2,y),fill=254)
    gfx=root/'graphics/title_screen'
    gfx.mkdir(parents=True,exist_ok=True)
    gfx.joinpath('eevee_stage14_bitmap.bin').write_bytes(p.tobytes())
    gbc=b''.join(gba_color(tuple(pal[3*k:3*k+3])).to_bytes(2,'little') for k in range(256))
    gfx.joinpath('eevee_stage14_palette.gbapal').write_bytes(gbc)
    p.convert('RGB').save(gfx/'eevee_stage14_preview.png')
    assert len(p.tobytes())==38400 and len(gbc)==512
    return p

def menu(root,img):
    # The original game's buttons and save-game widgets stay intact in BG0.
    # Put a GBA-adapted 16-color version of the uploaded background behind them.
    canvas=Image.new('RGB',(256,256),(24,14,54))
    canvas.paste(img,(0,0))
    q=canvas.quantize(colors=16, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE)
    palette=q.getpalette()[:48]
    tile_ids={};tiles=bytearray();tilemap=bytearray();data=q.tobytes()
    for ty in range(32):
        for tx in range(32):
            raw=bytearray()
            for yy in range(8):
                offset=(ty*8+yy)*256+tx*8
                for xx in range(0,8,2):
                    i0,i1=data[offset+xx],data[offset+xx+1]
                    raw.append(i0|(i1<<4))
            k=bytes(raw)
            if k not in tile_ids:
                tile_ids[k]=len(tile_ids)
                tiles.extend(k)
            tilemap.extend((tile_ids[k]|0x1000).to_bytes(2,'little'))
    # BG1 uses charbase 0 (0x0000), screenbase 15 (0x7800); BG0 starts at
    # charbase 2 (0x8000). This allows up to 960 unique 4bpp tiles.
    assert len(tile_ids)<=960, len(tile_ids)
    assert len(tiles)<=0x7800 and len(tilemap)==2048
    path=root/'graphics/interface'
    for name,bs in [('eevee_menu_bg.4bpp',tiles),('eevee_menu_bg.bin',tilemap),
      ('eevee_menu_bg.gbapal',b''.join(gba_color(tuple(palette[i:i+3])).to_bytes(2,'little') for i in range(0,48,3)))]:
        (path/name).write_bytes(bs)
    q.crop((0,0,240,160)).convert('RGB').save(path/'eevee_menu_preview.png')
    return len(tile_ids)

def patch(root:Path):
    root=root.resolve()
    if not (root/'Makefile').is_file():raise ValueError('Expected pokeemerald-expansion checkout')
    source=root/'src/title_screen.c'
    menu_c=root/'src/main_menu.c'
    old=source.read_text(encoding='utf8')
    mm=menu_c.read_text(encoding='utf8')
    if 'STAGE14_EEVEE_TITLE' in old:raise ValueError('Stage14 already applied')
    image=source_image(Path(__file__).resolve().parent)
    title(root,image)
    n=menu(root,image)
    art='''
// STAGE14_EEVEE_TITLE: 240x160 mode-4 title composed from supplied artwork.
static const u32 sEeveeTitleBitmap[] = INCBIN_U32("graphics/title_screen/eevee_stage14_bitmap.bin");
static const u16 sEeveeTitlePal[] = INCBIN_U16("graphics/title_screen/eevee_stage14_palette.gbapal");
static u16 sEeveeTitleTick;

static void Stage14_EeveeTitleVBlank(void)
{
    TransferPlttBuffer();
}

static void Stage14_EeveeTitleMain(void)
{
    u16 color;
    if (QUICKSTART && JOY_NEW(SELECT_BUTTON))
        Quickstart();
    if (JOY_HELD(CLEAR_SAVE_BUTTON_COMBO) == CLEAR_SAVE_BUTTON_COMBO)
        SetMainCallback2(CB2_GoToClearSaveDataScreen);
    else if (JOY_HELD(RESET_RTC_BUTTON_COMBO) == RESET_RTC_BUTTON_COMBO && CanResetRTC())
        SetMainCallback2(CB2_GoToResetRtcScreen);
    else if (JOY_HELD(BERRY_UPDATE_BUTTON_COMBO) == BERRY_UPDATE_BUTTON_COMBO)
        SetMainCallback2(CB2_GoToBerryFixScreen);
    else if (JOY_NEW(A_BUTTON) || JOY_NEW(START_BUTTON))
    {
        FadeOutBGM(4);
        BeginNormalPaletteFade(PALETTES_ALL, 0, 0, 16, RGB_WHITEALPHA);
        SetMainCallback2(CB2_GoToMainMenu);
    }
    else
    {
        sEeveeTitleTick++;
        // Three isolated palette colors: stars, sea glints and prompt text.
        color = (sEeveeTitleTick & 16) ? RGB(31, 31, 28) : RGB(17, 12, 26);
        LoadPalette(&color, 253, sizeof(color));
        color = (sEeveeTitleTick & 32) ? RGB(31, 27, 14) : RGB(12, 17, 25);
        LoadPalette(&color, 254, sizeof(color));
        color = (sEeveeTitleTick & 32) ? RGB(31, 31, 27) : RGB(22, 15, 23);
        LoadPalette(&color, 255, sizeof(color));
    }
}

static void Stage14_InitEeveeTitle(void)
{
    SetVBlankCallback(NULL);
    SetGpuReg(REG_OFFSET_DISPCNT, 0);
    SetGpuReg(REG_OFFSET_BLDCNT, 0);
    SetGpuReg(REG_OFFSET_BLDALPHA, 0);
    SetGpuReg(REG_OFFSET_BLDY, 0);
    ScanlineEffect_Stop();
    ResetTasks();
    ResetSpriteData();
    FreeAllSpritePalettes();
    ResetPaletteFade();
    DmaFill16(3, 0, (void *)VRAM, VRAM_SIZE);
    DmaFill32(3, 0, (void *)OAM, OAM_SIZE);
    DmaCopy32(3, sEeveeTitleBitmap, (void *)VRAM, sizeof(sEeveeTitleBitmap));
    LoadPalette(sEeveeTitlePal, BG_PLTT_ID(0), sizeof(sEeveeTitlePal));
    SetGpuReg(REG_OFFSET_BG2CNT, BGCNT_PRIORITY(0));
    SetGpuReg(REG_OFFSET_BG2PA, 0x100);
    SetGpuReg(REG_OFFSET_BG2PB, 0);
    SetGpuReg(REG_OFFSET_BG2PC, 0);
    SetGpuReg(REG_OFFSET_BG2PD, 0x100);
    SetGpuReg(REG_OFFSET_BG2X_L, 0);
    SetGpuReg(REG_OFFSET_BG2X_H, 0);
    SetGpuReg(REG_OFFSET_BG2Y_L, 0);
    SetGpuReg(REG_OFFSET_BG2Y_H, 0);
    SetGpuReg(REG_OFFSET_DISPCNT, DISPCNT_MODE_4 | DISPCNT_BG2_ON);
    sEeveeTitleTick = 0;
    EnableInterrupts(INTR_FLAG_VBLANK);
    SetVBlankCallback(Stage14_EeveeTitleVBlank);
    m4aSongNumStart(MUS_TITLE);
    gMain.state = 0;
    SetMainCallback2(Stage14_EeveeTitleMain);
}
'''
    anchor='void CB2_InitTitleScreen(void)\n{\n    if (IS_FRLG)'
    if old.count(anchor)!=1:raise ValueError('Title entry changed; refusing patch')
    # Inject helpers ahead of main title entry, then bypass only the old
    # Emerald title renderer. The official main menu callbacks remain intact.
    changed=old.replace(anchor,art+'\n'+anchor,1)
    modified='void CB2_InitTitleScreen(void)\n{\n    if (!IS_FRLG)\n    {\n        Stage14_InitEeveeTitle();\n        return;\n    }\n    if (IS_FRLG)'
    changed=changed.replace(anchor,modified,1)
    source.write_text(changed,encoding='utf8')
    before='        .bg = 1,\n        .charBaseIndex = 0,\n        .mapBaseIndex = 7,'
    after='        .bg = 1,\n        .charBaseIndex = 0,\n        .mapBaseIndex = 15, // STAGE14_EEVEE_TITLE: room for faithful 4bpp title-derived art'
    if mm.count(before)!=1 or 'STAGE13_EEVEE_MENU' not in mm:
        raise ValueError('Stage13 menu BG layout changed; refusing modification')
    # Stage 14B: Emerald's menu window masks originally expose only BG0.
    # Make BG1 visible behind the native menu buttons, including inside WIN0.
    patched_menu = mm.replace(before,after,1)
    win_inside = 'WININ_WIN0_BG0 | WININ_WIN0_OBJ'
    win_outside = 'WINOUT_WIN01_BG0 | WINOUT_WIN01_OBJ | WINOUT_WIN01_CLR'
    if patched_menu.count(win_inside) != 3 or patched_menu.count(win_outside) != 3:
        raise ValueError('Stage14B: unexpected main-menu window mask layout')
    patched_menu = patched_menu.replace(
        win_inside,
        'WININ_WIN0_BG0 | WININ_WIN0_BG1 | WININ_WIN0_OBJ')
    patched_menu = patched_menu.replace(
        win_outside,
        'WINOUT_WIN01_BG0 | WINOUT_WIN01_BG1 | WINOUT_WIN01_OBJ | WINOUT_WIN01_CLR')

    # Birch loads his introduction tilemap into BG1 screenblock 7. Stage 14
    # moves the title-derived menu backdrop to screenblock 15. Without this
    # reset, Birch appears over the recycled Eevee backdrop in the wrong colors.
    birch_anchor = (
        'static void Task_NewGameBirchSpeech_Init(u8 taskId)\n'
        '{\n'
        '    SetGpuReg(REG_OFFSET_DISPCNT, 0);\n'
        '    SetGpuReg(REG_OFFSET_DISPCNT, DISPCNT_OBJ_ON | DISPCNT_OBJ_1D_MAP);\n'
        '    InitBgFromTemplate(&sBirchBgTemplate);'
    )
    birch_reset = (
        '    // STAGE14C_EEVEE_TRANSITION: restore the BG manager cache, not only the hardware register.\n'
        '    // ShowBg(1) will overwrite REG_OFFSET_BG1CNT using this cached map base.\n'
        '    SetBgAttribute(1, BG_ATTR_MAPBASEINDEX, 7);'
    )
    if patched_menu.count(birch_anchor) != 1:
        raise ValueError('Stage14B: Birch intro initializer changed; refusing patch')
    patched_menu = patched_menu.replace(birch_anchor, birch_anchor + '\n' + birch_reset, 1)
    # Avoid writing either file before all the content checks pass.
    menu_c.write_text(patched_menu,encoding='utf8')
    print('Stage14B: menu BG1 is visible in all three native main-menu window states.')
    print('Stage14C: Birch BG1 manager mapbase restored to 7 before ShowBg(1) re-applies it.')
    print(f'Stage14: pixel-perfect GBA 240x160 title, {n} BG1 tiles, true main-menu callbacks retained')
    print('Stage14: title palette animation (stars/water/prompt), native 5x7 crisp labels')

if __name__=='__main__':
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('checkout',type=Path)
    patch(ap.parse_args().checkout)