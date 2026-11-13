# Stage 8J plan: Proper custom Eeveelution Pokédex registration (historical)

> **Archived engineering plan, not current feature status.** The original “no implemented patch” note below describes a pre-Stage-8J planning moment. Stage 8J subsequently compiled and assigned National Dex #1026 to Aerieon and #1027 to Aerartheon. The latest Stage 15.1 full-roster alpha has 163 custom Eevee forms in source, although gameplay/registration still needs emulator verification. See [current release notes](RELEASE_NOTES_v0.1.0-alpha.md).

**Historical status when originally written:** engineering plan only. **Current status:** the Stage 8J registration patch compiled successfully; individual in-game Dex display and save handling remain subject to emulator QA.

Tracked bug: [issue #1](https://github.com/Lamictal/Eevee/issues/1). Stage 8H screenshot showed `No. 000`, `Unknown Pokémon`, `HT 0'00"`, `WT 0.0 lbs.` while the species front art rendered.

## Confirmed root cause
The source prototype defines both Aerieon and Aerartheon with `.natDexNum = NATIONAL_DEX_NONE`. As a result, the registration UI calls `NationalPokedexNumToSpeciesForm(0)`, which resolves to `SPECIES_NONE`. The correct species' `.height`, `.weight` and `.categoryName` fields are never read from that screen. Unlike battle graphics, these screens **depend on a valid Pokédex number**.

The current species records do contain provisional physical data:
- Aerieon: `.categoryName = _("Sky")`, `.height=9` decimeters (0.9 m), `.weight=250` hectograms (25 kg).
- Aerartheon: `.categoryName = _("Sky Bug")`, `.height=10` decimeters (1.0 m), `.weight=290` hectograms (29 kg).
These are not yet final approved lore.

## Correct implementation path
1. Extend `enum NationalDexOrder` with `NATIONAL_DEX_AERIEON` and `NATIONAL_DEX_AERARTHEON` **after** official Gen IX numbers. Keep existing official numbers stable, and design a fixed contiguous reservation for the full 171 intended new forms.
2. Set `.natDexNum` in both species, provide concise custom descriptions instead of `gFallbackPokedexText`, and ensure category/dimensions render correctly.
3. Extend the national Pokédex count and verify all relevant arrays, bitsets and UI code. Regional Hoenn Pokédex behavior should be explicitly designed rather than silently adding forms.
4. **Audit save layout before deploying.** Upstream `POKEMON_SLOTS_NUMBER = NATIONAL_DEX_COUNT + 1`. Increasing dex count may enlarge save-resident seen/caught storage or change offsets. **Do not assume Stage 8H/8I saves survive this change.**
5. If save layout changes, implement a migration or maintain compatibility through a dedicated versioned layout. Avoid mixing new save data with Evergreen's unrelated older save.
6. Automate compile checks, then verify actual capture registration / category / height / weight / text / dex order in mGBA. Test both a brand-new save and a backed-up Stage 8I save. Only report save compatibility after testing it.

## Immediate priorities
- Finish Stage 8I sprite fix and check compilation.
- Keep Stage 8I playable while dex migration is designed.
- Then perform Stage 8J as a separately versioned build. Avoid silently changing the existing user's save.

## Important distinction
An entry can have valid raw species stats and battle art **without** having a registered National Pokédex number. Fixing the display is not just a matter of editing a measurement value.
