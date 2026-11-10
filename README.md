# Eevee expansion project

Custom Pokémon Emerald Expansion proof of concept for a long-term **18 single-type + 153 dual-type Eeveelution** game.

**Current development stage: 8I**, cloud build running; last confirmed successful compile: Stage 8H. Emulator validation remains incomplete. Only **Aerieon and Aerartheon** are integrated as additional species in this source-based prototype. The working Evergreen 2.0 Stage 8A.1 ROM and save are a **separate project** and remain untouched.

## Development reference
- [CHANGELOG.md](CHANGELOG.md): stage-by-stage changes, inherited engine QoL, planned balance, and test status.
- [TEST_PLAN.md](TEST_PLAN.md): gameplay and save test checklist.
- [Stage 8G compiled ROM download](https://github.com/Lamictal/Eevee/actions/runs/42892764393): GitHub Actions artifacts, accessible when signed in.
- [Stage 8F compiled ROM download](https://github.com/Lamictal/Eevee/actions/runs/42887055365): earlier effectiveness-indicator build.
- [Development workflow](.github/workflows/eevee-build.yml): reconstructs the upstream source on GitHub Actions and applies our patches.
- [Stage 8E engineering notes](STAGE8E.md): initial architecture, now superseded by the changelog for current status.

## Stage 8I sprite corrections
- Replaces Eevee party-menu placeholder icons for both custom species with sprites derived from their battle artwork.
- Replaces green Substitute follower with provisional six-frame species follower graphics.
- [Stage 8I build](https://github.com/Lamictal/Eevee/actions/runs/42921554174) and [sprite bug issue #2](https://github.com/Lamictal/Eevee/issues/2).
- Next: [Stage 8J save-aware Pokédex registration plan](STAGE8J_POKEDEX_PLAN.md) for issue #1.

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
