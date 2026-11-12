# Eevee expansion project

Custom Pokémon Emerald Expansion proof of concept for a long-term **18 single-type + 153 dual-type Eeveelution** game.

**Current development stage: 11**, [wild-habitat alpha build](https://github.com/Lamictal/Eevee/actions/runs/43276563803). The [Stage 10 full 171-form alpha](https://github.com/Lamictal/Eevee/actions/runs/43273919245) compiled successfully; full-roster gameplay has not yet been validated in mGBA. This Emerald Expansion ROM is separate from the user's earlier Evergreen 2.0 Stage 8A.1 ROM/save. The full 171-form alpha changes the saved Pokédex layout: **use a fresh save**.

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
