# Known limitations — Stage 15.1 alpha

**Last verified build:** [Stage 15.1, Monoamine 2026](https://github.com/Lamictal/Eevee/actions/runs/43465510674), GitHub Actions **Success**. The ROM compiled; this does **not** mean the entire game has passed emulator testing.

## Confirmed by the build and source checks

- Birch's starter bag uses **Treecko, Torchic and Mudkip**, not Eevee. Eevee is catchable on **Route 102** and other early routes.
- The source includes **18 single-type Eeveelutions plus 153 unique dual-type combinations** and validates **306 directed item-evolution routes**.
- Each of the **1,025 official National Dex species** is assigned a direct wild catchability route. The additional 1,024 species are in bonus encounter pools covering 61 Hoenn land habitats. This is static coverage, not a completed in-game Pokédex.
- Original wild encounter tables are retained, with bonus species selected by a separate encounter chance. Rare species can be difficult to find individually.
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
- The repository is public, but the current `Eevee-All171-` download is a **temporary GitHub Actions artifact**. **No GitHub Release has been published**.
- Redistribution rights for the *Oops! All Eevees!* artwork are not yet verified; a permission-cleared patch and appropriate credits are needed before public distribution.

**[Download the alpha](DOWNLOAD.md)** · **[Full Eevee Field Guide](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_FIELD_GUIDE.md)** · **[Stage 15 habitats](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/STAGE15_SOLO_DEX.md)** · **[Report a bug](https://github.com/Lamictal/Eevee/issues/new/choose)**
