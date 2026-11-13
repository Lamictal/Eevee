# Eevee expansion project

> **Looking for the game instead of build scripts?** Start at the **[player-friendly homepage](https://github.com/Lamictal/Eevee)**, **[download instructions](https://github.com/Lamictal/Eevee/blob/main/DOWNLOAD.md)**, or **[known limitations](https://github.com/Lamictal/Eevee/blob/main/KNOWN_ISSUES.md)**.
>
<!-- EEVEE_LATEST_BUILD_START -->
<!-- data-build-run=43377956728 -->
> **Latest development build:** [Stage 15 - Hoenn Starters and Solo National Dex Alpha](https://github.com/Lamictal/Eevee/actions/runs/43377956728). Find its alpha ZIP under **Artifacts**; temporary artifact, not a cleared public patch release.
<!-- EEVEE_LATEST_BUILD_END -->

Custom Pokémon Emerald Expansion proof of concept for a long-term **18 single-type + 153 dual-type Eeveelution** game.

## Stage 15: original Birch starters + solo National Dex (alpha)
- **Birch now offers Treecko / Torchic / Mudkip** again. Eevee remains catchable on Route 102 and other early routes; the old Stage 8K Eevee-starter configuration below is historical.
- **All 1,025 canonical National Pokédex species** have a designed wild encounter route somewhere in Hoenn, including trade evolutions, mythicals and other event-only Pokémon. Bonus encounters are biome-based; all original tables remain.
- The 171-form Eevee expansion and Stage 14 title-screen transition fix are kept. **Full gameplay/save behavior still needs emulator QA**.
- Read the [Stage 15 guide](STAGE15_SOLO_DEX.md) or the [updated Eevee Field Guide](EEVEE_FIELD_GUIDE.md).

**Current milestone: Stage 12 compiled successfully**, including the [full 171-form dual-evolution and habitat alpha](https://github.com/Lamictal/Eevee/actions/runs/43279472956). Its automated 306-route checks passed, but **full-roster gameplay has not yet been validated in mGBA**. See the [Beta 1 release roadmap](BETA1_RELEASE_PLAN.md) for a short smoke-test gate, future polish and a public-distribution checklist. The 171-form ROM changes the saved Pokédex layout: **start a fresh save**, and do not mix with Evergreen saves.

## Stage 13: custom Eevee selection menu
- [Custom menu design and QA plan](STAGE13_CUSTOM_MENU.md): original starry Eevee background, **NEW JOURNEY** and **SETTINGS** button labels, original menu handlers and save-file logic retained.
- [Stage 13 build](https://github.com/Lamictal/Eevee/actions/runs/43305777808): build status and artifact availability are verified separately.
- Successful full-roster builds are now configured to refresh the latest download links on the **main README**, **DOWNLOAD.md**, and this development README automatically after their artifact uploads. Old runs cannot overwrite newer links.

## Beta 1 readiness and release notes
- [Beta 1 release plan](BETA1_RELEASE_PLAN.md): short first-playthrough checks, graphics and balancing roadmap, and read-only public sharing notes.
- [Successful Stage 12 all-171 build](https://github.com/Lamictal/Eevee/actions/runs/43279472956): use this newer experimental alpha, not Stage 11, for deliberate dual evolution.

## Player guide: where to find Eevee, all 18 types, items and dual evolutions

**[Read the complete Eevee Field Guide](EEVEE_FIELD_GUIDE.md)** (wild encounters, evolution items, towns and requirements).

- **Eevee:** starter option and wild on **Routes 101 (5%), 102 (10%), 104 (5%), and 117 (5%)**.
- **All 18 single-type Eeveelutions:** distributed across Hoenn habitats including Granite Cave, Fiery Path, Route 119, Mt. Pyre, Shoal Cave, Meteor Falls and Sky Pillar; regular Pokémon retain at least 90% of affected land encounters.
- **Are all 153 dual types wild? No.** Nine distinct duals have very rare late-game wild locations (generally **1%**). Others are evolution-only.
- **Can every single become any dual with an item?** The Stage 12 source defines **17 choices per single × 18 singles = 306 item paths**, covering all **153 unordered dual pairs**. At **Lv. 38+ with six badges**, **Use** the booster item representing the *second* type (e.g., Aerieon + Silver Powder = Aerartheon). Stage 12 repairs the missing item effect from Stage 11.
- **Items:** original and custom first-stage catalysts appear in **Oldale, Rustboro, Slateport, Mauville, Fortree and Lilycove**; type boosters in Slateport, Mauville, Lavaridge, Fortree, and **all 18 boosters at Lilycove Department Store 4F**. See the [complete shop chart](EEVEE_FIELD_GUIDE.md#6-shops-by-town-quick-index).
- **Playability:** a successful compilation plus source-route validation does **not** guarantee emulator-tested gameplay. Use a fresh save for the all-171 ROM.

## Stage 11: all-type habitat balance
- [Encounter maps and item progression](STAGE11_HABITATS.md): all 18 single-type Eeveelutions have wild locations, with selected rare dual types in endgame areas.
- At least **90% of land encounters** on each affected map remain ordinary Pokémon; no existing fishing or surfing encounter tables changed.
- Stage 9/10 evolution catalysts remain distributed through shops; Lilycove remains the full type-item hub.
- [New 171-form habitat alpha](https://github.com/Lamictal/Eevee/actions/runs/43276563803); full ROM build verification separate from scripted source checks. No manual testing is required for this development step.

## Stage 8M: deliberate Sky Catalyst evolution (prototype)
- **Sky Catalyst**, new evolution item ID 874, available for 3,000 at Oldale Town Mart after Poké Balls unlock. Temporarily uses the Dawn Stone icon.
- **Eevee -> Aerieon:** use Sky Catalyst on Eevee at level 15+.
- **Aerieon -> Aerartheon:** use another Sky Catalyst at level 38+ and with at least six badges.
- Neither of these custom evolutions now triggers from leveling up automatically.
- All eight canonical Eeveelutions are retained; Route 102 wild rates remain 10% Aerieon / 1% Aerartheon.
- This is an initial controlled item path, not a 171-form selection menu.
- [Stage 8M build](https://github.com/Lamictal/Eevee/actions/runs/43170210160), separate from gameplay QA.
- Back up .sav files; same-save compatibility is not yet verified.

## Stage 8N: 171-form registry and save-compatibility guardrails
- [Full fixed-form roster](data/eevee_form_registry.json): **18 singles + 153 unordered duals** = 171 forms, including **eight official Eeveelutions**, so **163 custom forms** total.
- Custom National Dex IDs reserved **#1026..#1188**; Aerieon #1026 and Aerartheon #1027 are unchanged.
- [Save and migration contract](STAGE8N_SAVE_AND_ROSTER.md): full roster would increase each Dex seen/caught array **129 → 149 bytes**, requiring explicit migration or an audited alternate layout. Stage 8N **does not modify the ROM's saves**.
- [Automated registry checks](https://github.com/Lamictal/Eevee/actions/runs/43267372542) passed. The 161 additional forms remain *reserved*, not yet implemented.
- [Stage 8M cloud ROM build](https://github.com/Lamictal/Eevee/actions/runs/43265195678) compiled successfully; it still needs eventual milestone gameplay verification. No Stage 8N manual tests required.

## Development reference
- [CHANGELOG.md](CHANGELOG.md): stage-by-stage changes, inherited engine QoL, planned balance, and test status.
- [TEST_PLAN.md](TEST_PLAN.md): gameplay and save test checklist.
- [Stage 8G compiled ROM download](https://github.com/Lamictal/Eevee/actions/runs/42892764393): GitHub Actions artifacts, accessible when signed in.
- [Stage 8F compiled ROM download](https://github.com/Lamictal/Eevee/actions/runs/42887055365): earlier effectiveness-indicator build.
- [Development workflow](.github/workflows/eevee-build.yml): reconstructs the upstream source on GitHub Actions and applies our patches.
- [Stage 8E engineering notes](STAGE8E.md): initial architecture, now superseded by the changelog for current status.

## Stage 8K Eevee starter and balanced encounters
- Eevee temporarily replaces Treecko as the first of Birch's three starter options; Torchic and Mudkip remain available.
- Route 102 encounters: **10% Aerieon, 1% Aerartheon, 89% regular Pokémon**.
- A new game is required to choose Eevee at the starter bag; old saves won't retroactively receive Eevee.
- [Stage 8K build](https://github.com/Lamictal/Eevee/actions/runs/43092752535); compilation and mGBA validation are separate checks.
- [Future colored effectiveness UI issue](https://github.com/Lamictal/Eevee/issues/3); *not yet included*.

## Stage 8J Pokédex registration
- **Aerieon #1026** and **Aerartheon #1027** are now registered as separate National Pokédex species, with descriptions and existing height/weight fields.
- [Successful Stage 8J combined ROM](https://github.com/Lamictal/Eevee/actions/runs/42923311309), and [Stage 8I sprite-only ROM](https://github.com/Lamictal/Eevee/actions/runs/42922943309).
- Two new Dex entries fit in the existing saved seen/caught bitset byte allocation; save compatibility **still requires mGBA testing**.
- Catching a species again may be necessary to register one obtained in an older build with Dex number 000.

## Stage 8I sprite corrections
- Replaces Eevee party-menu placeholder icons for both custom species with sprites derived from their battle artwork.
- Replaces green Substitute follower with provisional six-frame species follower graphics.
- [Stage 8I successful build](https://github.com/Lamictal/Eevee/actions/runs/42922943309) and [sprite bug issue #2](https://github.com/Lamictal/Eevee/issues/2).
- Engineering notes: [Stage 8J Pokédex registration design](STAGE8J_POKEDEX_PLAN.md) for issue #1.

## Stage 8H test additions
- Following lead party Pokémon, with a substitute overworld sprite where custom walking graphics are missing.
- Optional IV/EV pages in summary screen, displaying numeric IVs.
- Standard Emerald PokéNav unchanged. DexNav (wild hunt tool) is not enabled yet.
- [Stage 8H cloud build](https://github.com/Lamictal/Eevee/actions/runs/42902820539) (check status, no gameplay verification yet).

## Stage 8G highlights
- Route 102 canary encounters: **Aerieon 25%** and **Aerartheon 11%** of wild encounters. **Temporary elevated testing rates**, not intended final balance. Proposed final ~10% / 1%, pending a later build and playtesting.
- Opponent type and move effectiveness hints during battle.
- Double-B attempt to flee wild battles. Not an overworld running speed feature.
- Normal Hoenn starters still used; Eevee-starter logic not implemented in this engine.

**Safety:** Do not commit GBA game ROM files or existing saves. Start a new save for this separate Emerald Expansion engine. For changes between 8E/8F/8G, back up the in-game .sav before reusing it; runtime save compatibility remains unverified.
