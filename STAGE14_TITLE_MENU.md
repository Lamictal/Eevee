# Stage 14: Eevee title screen and matching native menu

**Scope:** Stage 13's tested source-based Emerald Expansion project, with all 171 forms. Stage 14 does not change any save data, species, items, encounters or evolution logic.

## Artwork and readability

- Uses the user's supplied Eevee sunset/title illustration, reconstructed as a compact 32-color 240 × 160 indexed source and stored under `data/stage14_title_source.b85`.
- Generates a true **GBA mode-4, 240 × 160, 8bpp bitmap** with a 256-entry palette. No browser renderer is used in the ROM.
- Redraws the small captions (**171 FORMS**, **EMERALD EXPANSION**, **PRESS START**, **2025 LAMICTAL PROJECTS**) at their native resolution using explicitly plotted 5×7 glyphs instead of antialiasing an enlarged desktop font. The large logo and illustration remain derived from the supplied source and naturally lose some detail at 240 × 160.
- Reserves three title-screen palette indices for low-cost title animation: starlight, water glints and a gently blinking/pulsing Start label.
- Preserves the title music and sends A/Start into Emerald's **real** main menu. Existing B/Select diagnostic shortcuts are still routed to the original callbacks.

## Main menu

- Stage 13 already wired the **real** New Journey/Continue/Settings handlers and original save-file display. Stage 14 replaces only its BG1 visual artwork with a 16-color GBA interpretation of the same supplied sunset scene.
- BG1 is allocated tile memory from character base 0 through screen base 15 (0x7800); BG0 remains untouched in character base 2 (0x8000). The 4bpp title-derived scene is deduplicated into fewer than 960 unique tiles and uses palette bank 1.
- No fabricated Extras feature is added. Mystery Gift remains governed by the engine's native availability and menu states. Do not assume the HTML mockup's button layout exactly matches native game windows.

## Files and build

- `stage14_title_ui.py`: unpack supplied image, create native bitmap/palette and matching 4bpp menu background, patch the real `src/title_screen.c` callback, and move Stage 13 BG1 tilemap to screen base 15 to avoid VRAM overlap.
- `stage14_patch_builder.py`: chains this after Stage 13 in the full-171 cloud build.
- `.github/workflows/eevee-full171-build.yml`: builds the new alpha when files change and publishes a temporary GitHub Actions artifact, not a public ROM release.

## Acceptance tests (actual emulator)

1. Fresh boot in mGBA: full Eevee sunset, crisp small caption text, subtle stars/sea/prompt color cycling, no missing graphics.
2. Press A/Start: title transitions to native New Journey/Continue/Settings menu; art should appear behind the selection windows.
3. New Journey begins the genuine Birch sequence; save in-game, reboot and check Continue is available, with correct save summary.
4. Settings changes persist and returning to the main menu works. B returns to the title.
5. Any native Mystery Gift and diagnostic menu variants still work if enabled.
6. Confirm all 171 forms, custom sprites, starter choice, evolution items, routes and save/reload remain unaffected.

**Important:** GitHub compilation is not visual or controller QA. This remains an alpha until an in-emulator test succeeds. The user-provided fan artwork may need permissions/attribution before public redistribution; keep the repo private and do not distribute a full commercial ROM as a public release.
