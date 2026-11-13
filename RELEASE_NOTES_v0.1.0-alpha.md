# Pokémon Eevee: 171 Forms — v0.1.0-alpha release candidate

**Monoamine, 2026 · Unofficial fan project**

This is the first compiled candidate for a full-playthrough **alpha test**, not a stable release and not an officially licensed Pokémon title. The project's GitHub Actions output is a temporary build artifact, **not a GitHub Release**.

## Features

- Custom Eevee sunset title art, native GBA resolution, subtle palette animation, and **2026 MONOAMINE** credit.
- Optional emulator square thumbnail (512×512 and 256×256) and portrait cover art (512×768), packaged separately from game data.
- Original Emerald starter trio (Treecko / Torchic / Mudkip), with Eevee naturally catchable on Route 102 and other early routes.
- Eevee-family project scope: 18 single-type plus 153 dual-type combinations, including the eight standard Eeveelutions.
- National Pokédex solo-catchability design for all 1,025 official species: ordinary bonus pools and rarer late-game legendary/mythical pools across 61 Hoenn habitats, without removing original encounter tables.
- Catalysts, single-to-dual type-boost item evolution system, IV/EV summary pages, following Pokémon, and basic move-effectiveness indicators.

## Known limitations before Beta 1

- **Stage 15.1, including the Stage 14C Birch background correction, compiled successfully** in [Actions run #43467069844](https://github.com/Lamictal/Eevee/actions/runs/43467069844), alongside the 2026 Monoamine title credit and companion cover art. A real emulator screenshot had shown that Stage 14B's earlier background fix was incomplete; **the new Stage 14C fix still needs an emulator retest**, regardless of compilation status.
- New-game graphics transitions, save/reload behavior, custom evolution outcomes, and long-term story progression remain to be tested in mGBA.
- Stage 15's bonus encounter pools guarantee scripted species coverage, not reasonable completion time or optimized in-game UX. Some species can be very rare individually.
- Several custom follower frames, icons, movesets, stats, abilities and Pokédex strings still need polishing.
- No guaranteed save compatibility with prior Eevee alpha builds, Evergreen, or regular Emerald saves. Start a fresh save and back it up.
- Better colored effectiveness indicators, encounter search/DexNav, and comprehensive habitat navigation are not yet implemented.

## Artwork and ROM file notes

A GBA game cartridge or `.gba` file does not support a universal embedded cover image. Set one of the PNGs in your emulator's cover manager, if it provides that feature. These image files don't affect game saves or ROM content.

**Distribution:** Do not attach a full commercial Pokémon ROM to a public release. Verify artwork and code permissions, obtain third-party sprite attribution/redistribution clearance, and publish a lawful patch with clear instructions before the first public release. This is not endorsed by Nintendo, Game Freak, Creatures, or The Pokémon Company.

## Playtest acceptance checklist

1. Boot the Monoamine 2026 title, open menu, and return from Settings.
2. Start New Journey; verify Birch's graphics are correct and the three standard starters are present.
3. Catch a Route 102 Eevee, then test a custom form's party/summary/battle/follower art.
4. Catch a bonus out-of-region species; verify its National Pokédex registration.
5. Save normally, quit mGBA, reopen, and inspect party, PC, inventory and Pokédex.
6. Test a normal Eevee evolution, a catalyst evolution, and an appropriate six-badge dual item evolution.
7. Report unexpected graphics, crashes, balance problems or inaccessible encounters with the build ID and screenshots.

The recommended first-test build is always the newest **successful** Stage 15.1 development artifact; its GitHub Actions artifacts are temporary and should not be confused with a tagged GitHub Release.
