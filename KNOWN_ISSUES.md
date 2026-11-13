# Known limitations — Stage 15.1 alpha

**Last verified build:** [Stage 15.1, Monoamine 2026](https://github.com/Lamictal/Eevee/actions/runs/43465510674), GitHub Actions **Success**. The ROM compiled; this does **not** mean the entire game has passed emulator testing.

## Confirmed by the build and source checks

- Birch's starter bag uses **Treecko, Torchic and Mudkip**, not Eevee. Eevee is catchable on **Route 102** and other early routes.
- The source includes **18 single-type Eeveelutions plus 153 unique dual-type combinations** and validates **306 directed item-evolution routes**.
- Each of the **1,025 official National Dex species** has an assigned potential wild encounter location in the source. The additional 1,024 species are in bonus pools covering 61 Hoenn habitats. Map accessibility and full in-game Pokédex completion are **not verified**.
- Original wild encounter tables remain in source, but Stage 15's additional encounter override can replace **12%** of land encounters, with a **3%-first rare pool** on applicable maps. This reduces effective base-table species odds. Bonus Pokémon inherit the level selected by the original encounter slot, which still needs balance testing.
- The **2026 MONOAMINE** title credit and optional square/portrait emulator cover PNGs are included in Stage 15.1.
- Cover art is a companion image, **not an embedded GBA thumbnail**.

## Still needs emulator verification

- Title-screen animation, menus, the corrected **Professor Birch introduction**, and transitions to Settings/Continue/New Journey.
- The three starter choices, early Eevee encounters, all new encounter pools and Pokédex registration in real gameplay.
- In-game catalyst/booster use, item consumption, and the level-38/six-badge evolution requirement.
- Save/reload stability with custom Eeveelutions and other species in both **party and PC**, across the full story.
- Every custom sprite, icon, follower animation, species data, moveset and ability.
- Wild-encounter balance and collecting time for the very large National Dex.
- Mobile emulator differences and complete gym/story progression.

## Current alpha limitations

- Start a **fresh save**. No save migration is guaranteed from Evergreen, ordinary Emerald or earlier Eevee test builds. Always back up saves.
- Only nine distinct dual Eeveelutions have dedicated rare wild sightings; the rest are designed to be obtained through evolution.
- Some art and follower/party icons remain provisional. The colored move-effectiveness labels and a searchable DexNav-style habitat system are planned rather than implemented.
- **Custom move learnsets still need polishing.** The [generated level-up guide](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_LEVEL_UP_MOVES.md) confirms all 163 custom forms have just five or six level entries, and 26 forms repeat at least one move at different levels. The source tables are documented, but in-game behavior and balance have not been audited.
- The repository is public, but the current `Eevee-All171-` download is a **temporary GitHub Actions artifact**. **No GitHub Release has been published**.
- Redistribution rights for the *Oops! All Eevees!* artwork are not yet verified; a permission-cleared patch and appropriate credits are needed before public distribution.

**[Download the alpha](DOWNLOAD.md)** · **[Full Eevee Field Guide](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_FIELD_GUIDE.md)** · **[Stage 15 habitats](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/STAGE15_SOLO_DEX.md)** · **[Report a bug](https://github.com/Lamictal/Eevee/issues/new/choose)**
