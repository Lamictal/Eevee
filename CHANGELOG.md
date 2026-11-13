# Eevee expansion development changelog

This file tracks the **source-based Emerald Expansion** prototype in [Lamictal/Eevee](https://github.com/Lamictal/Eevee). It is separate from the user's working **Evergreen 2.0 + Eevee Stage 8A.1** ROM and save.

**Conventions**
- **Custom work** = code or data we added or modified.
- **Engine default** = upstream `rh-hideout/pokeemerald-expansion` functionality; do not credit as a custom feature.
- **Compiled** = GitHub Actions successfully produced a ROM. **Gameplay verified** requires an actual emulator test and is not implied by a green build.
- Each new stage should have: scope, changed files, user-facing differences, build run URL and result, save compatibility notes, and outstanding testing.

## Stage 15.1 / Stage 14C: Monoamine title, GBA cover art, Birch-background fix and documentation audit (November 13, 2026)
- **Latest compiled ROM:** [Stage 15.1 + Stage 14C](https://github.com/Lamictal/Eevee/actions/runs/43467069844), GitHub Actions **Success**. This proves compilation, not a passing in-emulator Birch intro or full gameplay test.
- Replaced the title credit with **2026 MONOAMINE** and bundled optional emulator artwork in square and GBA box styles. Cover PNGs are **companion files**, not embedded ROM cover metadata.
- **Stage 14C** updates the cached BG1 screen base for Birch's introductory scene; an earlier hardware-register-only correction compiled yet still displayed the old Eevee menu graphics behind Birch. **Visual confirmation remains open.**
- Updated homepage, download guide, known issues, Field Guide, historical stage docs, bug-report template and current smoke test for accuracy. In particular, removed the obsolete claim that Birch offers Eevee as a starter.
- No official tagged GitHub Release has been published. Current alpha download is a temporary Actions artifact, and third-party artwork/public patch permissions require review.

## Stage 15: restore original starters and assign solo National Dex habitats (November 13, 2026)
- **Source/ROM build:** [Stage 15](https://github.com/Lamictal/Eevee/actions/runs/43377956728), GitHub Actions **Success**.
- Birch again offers **Treecko, Torchic and Mudkip**. Eevee is wild on Routes 101/102/104/117. The current **Route 102 Eevee core slot is 10%**; old experimental Aerieon/Aerartheon slots were removed from that route.
- Assigned a potential encounter to every **official National Dex species** via 1,024 new bonus species across **61 Hoenn land habitats**, plus Eevee in its existing table. Actual accessibility, catchability and Dex completion are **not fully emulator-tested**.
- Current bonus encounter logic uses an **optional 3% rare pool** first, then a **12% ordinary pool** on the remaining rolls. Therefore old Stage 11 guarantees of 90% actual ordinary encounters and some listed core-table spawn odds do **not** apply unchanged.
- Bonus species inherit the original selected encounter's **level**, which still needs balance testing. All 171 Eevee forms and prior evolution routes were retained in source.

## Stage 14: custom title screen and graphical transition (November 12–13, 2026)
- Implemented a native 240×160 GBA Eevee title image, crisp pixel captions, palette effects, and matching main-menu background.
- [Initial Stage 14 title/menu build](https://github.com/Lamictal/Eevee/actions/runs/43318859008) compiled. An mGBA screenshot then revealed an incorrect green-tinted Eevee logo behind Birch, prompting Stage 14B and 14C fixes.

## Stage 13: custom main menu (November 12, 2026)
- Added a custom Eevee menu background and New Journey / Settings labels, retaining Emerald's existing handlers and save logic.
- [Historical Stage 13 build](https://github.com/Lamictal/Eevee/actions/runs/43305777808) compiled. Current Stage 15.1 supersedes this menu-only build.

## Stage 12: dual evolution item effect repair and player guide
**Build:** [All-171 source with corrected type-boosting item effects](https://github.com/Lamictal/Eevee/actions/runs/43279472956); build and gameplay verification tracked separately.

- Confirmed Stage 10/11 source added 18 × 17 item evolution routes (306 directed paths) targeting all 153 unique unordered dual species, subject to level 38 and six Hoenn badges.
- Found and fixed an actual engine issue: the 18 ordinary type-boosting held items had party-use callbacks but lacked `.effect = gItemEffect_EvoItem`; the engine's item-effect handler would reject them before checking evolution targets.
- Added source check to validate all 18 booster effects, all 306 source/target evolutions, exact mapping to 153 unique dual forms, and item availability in Lilycove Department Store 4F.
- Preserved their traditional held-type power boosts and all existing wild encounters, other items and species IDs; this patch introduces no new save-layout changes beyond the previous full-roster alpha.
- Published [EEVEE_FIELD_GUIDE.md](EEVEE_FIELD_GUIDE.md) with wild Eevee areas, all 18 singles, nine rare wild duals, first-stage catalyst locations, second-stage boosters and shop locations.
- Full 171-form ROM is **not yet gameplay verified**; use fresh saves for the full-roster alpha.

## Stage 11: 18 single-type habitats plus rare endgame duals
**Build:** [171-form habitat alpha](https://github.com/Lamictal/Eevee/actions/runs/43276563803), following [successful Stage 10 171-form build](https://github.com/Lamictal/Eevee/actions/runs/43273919245).
**Status:** Source habitat patch is integrated; compiler / emulator verification are tracked separately.

- Adds wild habitats across 28 specific Hoenn Emerald land maps, including the early/midgame single-type ecosystem and rarer dual-type sightings in advanced areas.
- Preserves vanilla Pokémon dominance (at least 90%) in every modified map, and keeps previously balanced Eevee sightings and Aerieon/Aerartheon.
- All 18 single types appear in the wild; eight unique dual forms have occasional 1% sightings across endgame sites. The remaining dual combinations are evolution-first, using the Stage 10 item's progression framework.
- Adds source assertions for every map count, species symbol, prior encounter, probability cap, and coverage.
- No species ID or new save-layout changes beyond Stage 10. Use a fresh save when playing the complete 171-form version. Gameplay remains unverified.

## Stage 10: complete 171-form source alpha
**Status:** [Full 171-form ROM compiled successfully](https://github.com/Lamictal/Eevee/actions/runs/43273919245); in-game QA pending.
- Ported artwork and stats from the original Oops! All Eevees artwork supplied by the user into a separate Emerald Expansion build.
- Includes original eight and 163 custom Eeveelution forms in source. The user can also encounter native Hoenn Pokémon.
- Adds item-targeted dual evolutions with six badges and level 38, retains existing canonical Eevee evolution routes.
- Save structure differs from previous two-species alpha; start a fresh save until migration exists.

## Stage 8N: reserve entire Eeveelution roster and save-layout plan
**Status:** [Registry CI passed](https://github.com/Lamictal/Eevee/actions/runs/43267372542). No new species are compiled or save structures changed by this planning stage.
**Previous build:** [Stage 8M ROM compilation succeeded](https://github.com/Lamictal/Eevee/actions/runs/43265195678). In-game verification deferred to a later milestone.

- Machine-readable registry of 18 single type + 153 unique unordered dual type forms.
- Eight official Eeveelutions already exist in upstream; 163 custom forms to implement, two already integrated, 161 reserved.
- Preserve Aerieon custom National Dex #1026 and Aerartheon #1027. Reserve #1028–#1188 deterministically.
- Automated validator confirms combinations, official names/Dex positions, stable custom ID allocation, and evolution planning constraints.
- Save schema impact: current 129-byte seen/caught arrays would become 149 bytes each (+40 bytes together), and must not be enlarged blindly.
- Previous Evergreen 8A.1 save/ROM remain unrelated and unmodified.
- Stage 8N produces no additional playable forms. Next development milestone should recover the former 30-form art/rules before generating the missing forms.

## Stage 8M: deliberate Sky Catalyst path
**Status:** [Stage 8M cloud build](https://github.com/Lamictal/Eevee/actions/runs/43170210160) initiated, awaiting separate emulator verification.
**Confirmed by user:** Stage 8L Eevee -> Aerieon evolution worked in mGBA. The remaining evolution paths were not tested.

- New ITEM_SKY_CATALYST = 874, appended after the current upstream items to avoid changing prior item IDs, sold in Oldale Mart's expanded inventory.
- Eevee -> Aerieon through deliberate use of Sky Catalyst at level 15+.
- Aerieon -> Aerartheon through deliberate use of Sky Catalyst at level 38+ and with six badges.
- New IF_MIN_LEVEL and IF_MIN_BADGES conditions are appended to the evolution condition enumeration.
- Both previous level-6 automatic test evolutions removed. Original Eeveelutions remain intact.
- Stage 8K encounter rates unchanged; Stage 8I/J graphics, Dex, follower, battle hints and IV/EV views retained.
- Dawn Stone icon is placeholder artwork. This is not yet a dedicated multiple-evolution choice screen.
- Source modules: stage8m_catalyst_evolutions.py and stage8m_patch_builder.py.
- Open tests: build compilation, item availability and use, badge gate, item consumption, saves and canonical Eevee paths.
- Never overwrite the user's original Evergreen save.

## Stage 8K: Eevee starter and encounter balance
**Status:** [GitHub cloud compilation](https://github.com/Lamictal/Eevee/actions/runs/43092752535) launched; gameplay verification pending.
**User request:** after Stage 8J successful gameplay tests, add Eevee as a starter and rebalance overly frequent new Eeveelutions.

- **Eevee can be chosen** from Birch's starter bag on Route 101. Since upstream chooser has three slots, Eevee temporarily **replaces Treecko** in the first (grass-position) Poké Ball; it remains a Normal-type Eevee. Torchic and Mudkip remain available. A future four-option starter UI could restore all three original starters.
- **Route 102 encounters:** Aerieon **10%**, Aerartheon **1%**, normal wild Pokémon **89%**. Keeps other wild locations and all species IDs unchanged. Stage 8G originally set experimental 25% and 11%.
- Stage 8J graphics fixes, actual custom National Dex entries, followers, numeric IV/EV summary, native effectiveness symbols, and double-B wild escape remain.
- **Colored and accessible move effectiveness indicators** logged separately as [issue #3](https://github.com/Lamictal/Eevee/issues/3); this is a *wishlist item*, not included.
- **Save behavior:** Your previously chosen starter will not change when loading an older save. To choose Eevee in Birch's bag, start a new game. Back up the existing `.sav` before opening any new build.
- **QA:** Fresh new game starter bag and Birch rescue; verify Eevee sprite/name and party, Torchic and Mudkip options, old save remains unaltered, Route 102 approximate wild frequency in manual testing, and other Stage 8J features.

## Stage 8J: Aerieon/Aerartheon Pokédex registration
**Status:** [Corrected Stage 8J build](https://github.com/Lamictal/Eevee/actions/runs/42923311309) **compiled successfully**; emulator validation pending. The original build [failed on a duplicate source anchor](https://github.com/Lamictal/Eevee/actions/runs/42923026893), corrected in commit `cbf5e3c`.
**Bug:** [Issue #1](https://github.com/Lamictal/Eevee/issues/1)

- Adds Aerieon as National Dex **#1026** and Aerartheon as **#1027**, after all official Gen IX species. Existing official National numbers stay unchanged.
- Replaces `NATIONAL_DEX_NONE` species entries with proper national numbers, plus short custom Pokédex descriptions.
- Uses their existing provisional category / sizes: Aerieon, Sky, 0.9 m / 25 kg; Aerartheon, Sky Bug, 1.0 m / 29 kg.
- Corrects the registration display so custom species show a **four-digit National number** even before the National Pokédex is formally unlocked. The Hoenn regional list is unchanged for now.
- **Save layout detail:** `NUM_DEX_FLAG_BYTES = ceil((NATIONAL_DEX_COUNT+1)/8)`, and the two added species leave this at **129 bytes**, so the existing seen/caught bitset byte lengths are unchanged for this specific 2-species patch. This is not proof of complete cross-build save compatibility; back up all saves.
- The eventual **171-form Dex expansion** will need deliberate save migration since it exceeds the currently allocated bitfield capacity.
- Inherits Stage 8I custom icon and follower graphics. No original Evergreen source or saves modified.
- **Test:** capture, Dex registration, category, height, weight, descriptions, number display, saved species, existing save, and national list after unlocking.

## Stage 8I: Species-specific party icons and followers
**Status:** [Corrected Stage 8I build](https://github.com/Lamictal/Eevee/actions/runs/42922943309) **compiled successfully**; mGBA validation outstanding. The original compile attempt [failed](https://github.com/Lamictal/Eevee/actions/runs/42921554174) on missing custom overworld graphics declarations, corrected in commit `aa4cc99`.
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
