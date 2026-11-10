# Eevee expansion development changelog

This file tracks the **source-based Emerald Expansion** prototype in [Lamictal/Eevee](https://github.com/Lamictal/Eevee). It is separate from the user's working **Evergreen 2.0 + Eevee Stage 8A.1** ROM and save.

**Conventions**
- **Custom work** = code or data we added or modified.
- **Engine default** = upstream `rh-hideout/pokeemerald-expansion` functionality; do not credit as a custom feature.
- **Compiled** = GitHub Actions successfully produced a ROM. **Gameplay verified** requires an actual emulator test and is not implied by a green build.
- Each new stage should have: scope, changed files, user-facing differences, build run URL and result, save compatibility notes, and outstanding testing.

## Stage 8I: Species-specific party icons and followers
**Status:** [Cloud compile](https://github.com/Lamictal/Eevee/actions/runs/42921554174) started; mGBA validation outstanding.
**Bug:** [Issue #2](https://github.com/Lamictal/Eevee/issues/2)

- Replaces temporary Eevee party icons for Aerieon/Aerartheon with original-art-derived 32×64 species icons.
- Replaces Substitute follower placeholder with six-frame 32×32 overworld sheets and matching species palettes.
- Generated walking frames are **provisional front-derived motion/angle approximations**, not polished hand-drawn overworld views.
- Does not change native species IDs, existing battle/summary sprites, Pokédex numbering, or saved-game layout.
- Uses Pillow during automated GitHub build for deterministic generated assets.
- **Test:** check party menu icon, follower on multiple maps and after party reorder, and save/reload. Compilation alone is not gameplay verification.

## Stage 8H: Following Pokémon and IV/EV summary
**Status:** GitHub build launched; gameplay and save compatibility unverified.
**Build:** https://github.com/Lamictal/Eevee/actions/runs/42902820539

**Custom configuration**
- Enabled `OW_FOLLOWERS_ENABLED=TRUE` while retaining `OW_POKEMON_OBJECT_EVENTS=TRUE` and `OW_SUBSTITUTE_PLACEHOLDER=TRUE`. The first healthy Pokémon in your party can follow in the overworld (subject to map restrictions). Custom Aerieon and Aerartheon may display placeholder overworld sprites pending dedicated walking graphics.
- Enabled `P_SUMMARY_SCREEN_IV_EV_INFO=TRUE`, `P_SUMMARY_SCREEN_IV_EV_VALUES=TRUE`, and `P_SUMMARY_SCREEN_IV_EV_TILESET=TRUE`. Intended to add Stats/IV/EV views and numeric IV values.
- Kept ordinary Emerald **PokéNav** and its original story unlock intact. Did **not** turn on **DexNav**, the unrelated wild-Pokémon search UI; it requires nonzero reserved flags/variables and a separate save audit.
- Inherits Stage 8G's elevated **testing** encounters of 25% Aerieon and 11% Aerartheon. Final balance adjustment remains pending.

**Code:** `stage8h_followers_ivev.py`, `stage8h_patch_builder.py`, cloud workflow.

**Save warning:** The intent is configuration-only changes, but follower systems and IV/EV alternate tileset can affect runtime, graphics, and old saves. Back up the entire .sav and do not overwrite Evergreen saves. Successful compilation is not sufficient to establish compatibility.

## Stage 8G: Easier test encounters and double-B wild escape
**Status:** Compiled; emulator behavior unverified.
**Build:** https://github.com/Lamictal/Eevee/actions/runs/42892764393 (success)

**Custom work**
- Increased **Route 102 grass** Aerieon test encounter rate **5% → 25%**, Aerartheon **1% → 11%**, normal Pokémon remaining **64%** of *encounters*.
- Applied the existing quick-select-Run option and patched wild battle input: press B once to focus Run; press B again to attempt escape. This does **not** guarantee escape or enable overworld sprinting. Does not alter trainer battle input.
- Preserved prior Stage 8F battle UI options and Stage 8E species definitions.

**Code:** `stage8g_encounters_quickrun.py`, `stage8g_patch_builder.py`, workflow.
**Save note:** Same species IDs as Stages 8E and 8F, so in-game saves are expected to transfer; **not runtime-verified**. Make a backup. Evergreen 2.0 saves remain incompatible.
**Balance note:** **25%/11% are temporary canary rates**, not a final-game balance decision. For a normal early-route playthrough, proposed target is ~**10% Aerieon / 1% Aerartheon** (subject to playtesting and later evolution-gate work). The current test ROM is not being retroactively changed.

## Stage 8F: Type hints in battle
**Status:** Compiled; emulator behavior unverified.
**Build:** https://github.com/Lamictal/Eevee/actions/runs/42887055365 (success)

**Custom work**
- Set the upstream engine options `B_SHOW_TYPES=SHOW_TYPES_ALWAYS` and `B_SHOW_EFFECTIVENESS=SHOW_EFFECTIVENESS_ALWAYS`.
- Opponent type indicators and move matchup effectiveness are intended to appear even for previously unseen species.
- The upstream battle UI replaces PP with effectiveness text during move selection. L-button move descriptions are an engine default and have not been rewritten.

**Code:** `stage8f_enable_battle_ui.py`, `stage8f_patch_builder.py`, workflow.
**Save note:** Config-only battle UI changes; not a new species format. Back up saves before swapping ROMs.

## Stage 8E: First compilable source expansion
**Status:** Compiled successfully on third build attempt; emulator testing user-side pending.
**Successful build:** https://github.com/Lamictal/Eevee/actions/runs/42807966659

**Custom work**
- Installed the experimental Stage 8C/8D source kit into a fresh upstream expansion checkout, including the new species **Aerieon (Flying)** and **Aerartheon (Flying/Bug)** with stats, move data, sprites and an experimental Aerieon → Aerartheon evolution at level 6.
- Added two rare wild Route 102 encounters (5% / 1%) while retaining regular Pokémon.
- Resolved source integration errors by using the upstream static sprite-animation table `sAnims_SingleFramePlaceHolder` for both species.
- Added an automated GitHub Actions compile workflow; compiled `.gba` outputs are published as Actions artifacts, **not committed to the repository**.
- **Not** Evergreen's title screen, features, or starter event. Normal Hoenn starter selection remains.

**Code:** `stage8d-kit.tar.xz.b64` (packed source kit), `stage8e_hotfix.py`, `.github/workflows/eevee-build.yml`.

## Before Stage 8E
- Stage 8A.1 on the Evergreen binary contained 30 Eeveelutions and the repaired still sprites; that **separate** build was tested by the user. Its original binary-modification scripts are not in this GitHub repository.
- Stage 8C/D produced the initial new-engine source kit and roster planning file.
- The **171 forms** are a roster plan (18 singles + 153 distinct dual types), **not** 171 functional forms in the source prototype. The current source build has **two** custom species.

## Upstream quality-of-life features, NOT custom additions
The build clones `rh-hideout/pokeemerald-expansion` master and inherits its enabled defaults, including:
- **EXP for catching** Pokémon: `B_EXP_CATCH=GEN_LATEST`.
- Participating Pokémon get full rather than split EXP: `B_SPLIT_EXP=GEN_LATEST`; level-scaled EXP: `B_SCALED_EXP=GEN_LATEST`.
- Modern critical hit and status mechanics, Fairy typing, physical/special move categories, updated move and ability data.
- Faster battle-intro text, HP bar drain and EXP bars; move-description button **L**; last-used ball button **R**.
- Nature colors in summary screen and nickname change from summary screen.
- A Repel/Lure reuse menu after items expire, and indoor running once running is otherwise available.
- **Do not assume every optional upstream feature is enabled.** For example `DEXNAV_ENABLED=FALSE`, `OW_FOLLOWERS_ENABLED=FALSE`, `P_SUMMARY_SCREEN_IV_EV_INFO=FALSE`, level caps off by default. The engine supports those, but the prototype has not turned them on.

## Open design and testing items
- Validate actual Route 102 encounters, front/back sprite quality, icons, battle move hints, double-B escape, evolution, save/reload, and same-save loading between versions in mGBA.
- Make Eevee a starter and implement 18 single-type and 153 dual-type evolution logic.
- Balance early encounters and remove the temporary level-6 shortcut for production; intended later gating is level 38, six badges, catalyst.
- Integrate/recreate Evergreen features separately; its original save is **not** interchangeable with this source-based Emerald Expansion.
- Pin the upstream engine to a fixed commit for reproducible builds; the current build fetches `master` and may change as the upstream project evolves.
