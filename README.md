# Pokémon Eevee: 171 Forms

**An unofficial Pokémon Emerald Expansion fan project · Monoamine, 2026**

Explore Hoenn with the original Pokémon **plus 171 Eeveelution forms across all 18 types**: 18 single-type forms and 153 unique dual-type combinations (including the eight official Eeveelutions). Keep the classic story, discover new habitats, and evolve Eevee into unexpected type combinations.

**Current version:** Stage 15.1, Monoamine 2026 alpha · **Platform:** Game Boy Advance · **Build:** Compiled successfully · **Gameplay testing:** Still in progress

## Download the current alpha

<!-- EEVEE_LATEST_BUILD_START -->
<!-- data-build-run=43473796334 -->
### [VIEW THE LATEST DEVELOPMENT BUILD](https://github.com/Lamictal/Eevee/actions/runs/43473796334)

**Stage 15.1 - Monoamine 2026 Title and Cover Alpha** · [Build details](https://github.com/Lamictal/Eevee/actions/runs/43473796334)

**Not a public patch release:** the build page contains a temporary GitHub Actions artifact for testing. Sign-in may be required. See [the download guide](DOWNLOAD.md).
<!-- EEVEE_LATEST_BUILD_END -->

**[Step-by-step download and emulator setup](DOWNLOAD.md)** · **[Known issues and test status](KNOWN_ISSUES.md)**

The GitHub repository is public, but this is **not a tagged GitHub Release or a verified public ROM patch**. GitHub Actions artifacts expire, and may require sign-in. A permission-cleared patch package is a separate release goal.

## What's in the latest build?

- **Original Hoenn starters:** Professor Birch offers **Treecko, Torchic and Mudkip**. Eevee does **not** replace a starter anymore.
- **Wild Eevee early on:** Catch Eevee on Routes **101 (5% core-slot rate), 102 (10%), 104 (5%) and 117 (5%)**. On Routes 104 and 117, Stage 15's bonus species pool reduces the approximate overall Eevee chance to **4.4%**; the percentages in the table are base slot weights, not always final odds.
- **171 Eeveelution forms:** 18 singles and 153 distinct dual types. All eight original Eeveelutions retain their native evolution options.
- **Solo National Pokédex design:** Source checks assign a potential wild encounter to **all 1,025 official National Dex species**, including trade-evolution and event-only Pokémon, through 1,024 bonus species across **61 Hoenn land habitats** plus existing wild Eevee. This is **not proof** that every habitat is reachable, every encounter works in-game, or the Pokédex is fully completable yet.
- **Explore to collect:** All 18 single-type Eeveelutions appear in suitable wild habitats. Nine distinct dual-type forms have rare wild encounters; other dual forms are designed to come through evolution.
- **Evolution items:** Custom first-stage catalysts and second-type booster items are sold throughout Hoenn. The code defines **306 single-to-dual evolution routes** for all 153 unique duals.
- **Level-up moves for every form:** [Searchable-by-heading move-level tables for Eevee and all 171 Eeveelutions](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_LEVEL_UP_MOVES.md). All tables are extracted from the compiled ROM source; custom movesets are still being balanced.
- **Quality-of-life features:** IV/EV details, basic move-effectiveness indicators, quick fleeing and provisional following Pokémon and party icons.
- **Custom visuals:** Animated Eevee sunset title screen, **2026 MONOAMINE** credit, and custom New Journey/Continue/Settings menu artwork. Optional square and portrait GBA-style **emulator cover PNGs** are packaged with the latest build.

### The starter choices

| Treecko | Torchic | Mudkip |
|:---:|:---:|:---:|
| Grass | Fire | Water |

**Want Eevee?** Walk into the grass on **Route 102**; it has a 10% encounter slot in the core table. Eevee is also available on several early routes, without taking Treecko's starter slot.

### How to evolve into a dual type

1. Obtain a **single-type Eeveelution**, using a normal Eevee method or one of the custom catalysts.
2. Reach **level 38 or higher** and earn **at least six Hoenn Gym Badges**.
3. In the Bag, **Use** the item representing the *additional type* on your eligible single-type Eeveelution.

For example, Aerieon (Flying) + Silver Powder (Bug) is designed to evolve into **Aerartheon (Flying/Bug)**. Going the other way, Artheon (Bug) + Sharp Beak (Flying), targets the same species. The source validates all 306 routes, but some outcomes still need emulator testing.

**[Full Eevee Field Guide: all forms, items, shops and locations](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_FIELD_GUIDE.md)**

## Playing and saving

**This is a real playable-build candidate, not a verified finished game.** Stage 15.1 compiled successfully, but the new-game intro, custom evolution items, follower art, long-term save/reload and complete story progression still need thorough testing.

**Start a fresh save.** Do not overwrite or reuse Evergreen, ordinary Emerald or early Eevee prototype saves. Keep backups as you test.

A `.gba` ROM **does not embed a universal emulator thumbnail**. The optional image files in the build ZIP and separate cover-art ZIP are for emulator cover managers that support custom artwork.

## Project status and feedback

- **[Known issues and limitations](KNOWN_ISSUES.md)**: what is verified versus still untested
- **[Stage 15 solo-National-Dex design](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/STAGE15_SOLO_DEX.md)**: encounter system and starter locations
- **[v0.1.0-alpha release-candidate notes](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/RELEASE_NOTES_v0.1.0-alpha.md)**: release scope, saves and QA
- **[Beta 1 roadmap](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/BETA1_RELEASE_PLAN.md)**: work remaining
- **[Report a bug or suggest a feature](https://github.com/Lamictal/Eevee/issues/new/choose)**
- **[Development source and build scripts](https://github.com/Lamictal/Eevee/tree/stage8e-cloud-prototype)** · **[Contribution guide](CONTRIBUTING.md)**

## Credits and distribution

**Monoamine (2026)** is the fan-project credit shown on the game title screen. This project builds on the open-source [pokeemerald-expansion](https://github.com/rh-hideout/pokeemerald-expansion) engine. The project also uses Eeveelution artwork sourced from *Oops! All Eevees!* for development; original authorship, attribution and public redistribution rights must be verified before distributing those assets.

This is a **noncommercial, unofficial fan project**, not sponsored, approved or endorsed by Nintendo, Game Freak, Creatures or The Pokémon Company. Pokémon and related names/art remain the property of their respective owners. Do not redistribute complete copyrighted base ROMs. Any later public release should use a permission-cleared patch and appropriate notices.

---

*171 forms. One extremely ambitious Eevee.*
