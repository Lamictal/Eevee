# Stage 15: Original Hoenn starters and solo National Pokédex

This milestone is part of the **Stage 15.1 Monoamine Eevee Emerald Expansion alpha**. It is not Evergreen save-compatible. The animated title screen is present, and the Stage 14C Birch-background correction **compiled successfully**; actual emulator confirmation is still required.

## Starters and Eevee

- Professor Birch's original three options are **Treecko, Torchic, and Mudkip**. Stage 8K's temporary Eevee replacement is reversed at the end of the source build.
- **Eevee remains catchable on Route 102** at the existing natural encounter rate. Other early Eevee encounters from Stage 9 remain untouched. Eevee does not require a separate starter slot.
- All three original starters and their later evolutions are included in the solo-Dex encounter coverage.

## Solo-completable National Pokédex

- The source generator assigns a land bonus habitat to **1,023 of the 1,025 canonical National Pokédex species**, from Bulbasaur through Pecharunt. **Eevee** already appears in normal wild tables and **Carvanha** stays in its original fishing encounters. This is an automated coverage claim, **not** a verified completion of the National Dex in-game.
- Eevee is already available on Route 102. Carvanha remains available using the native Good Rod and Super Rod tables rather than appearing in grass. The remaining **1,023 species** receive deterministic, biome-oriented land bonus encounter habitats.
- The intended design avoids online trading and limited-time events, including for trade-evolution and event-only Pokémon. **Every official species has a scripted potential encounter**, but actual map accessibility, encounter behavior, Pokédex registration and catchability still need emulator checks before guaranteeing full completion.
- This is **National Dex species coverage**, not a guarantee of every alternate battle form, variant, costume, regional form, or gender-specific appearance.
- The **171 Eevee forms**, including eight canonical species, remain governed by the existing Stage 10–12 item-evolution mechanics. All 153 dual forms are intended to remain reachable via item paths, pending in-game QA.

## Encounter balance and locations

Existing Hoenn land encounter tables are **not replaced**. Fishing, surfing, rocks, story/static encounters, trainer teams, item shops, and Pokédex save layout are not changed.

In **61 selected land habitats**, Stage 15's balanced bonus pools can replace a normal-table encounter. The new *ordinary pool* chance depends on location progression: **4% in opening areas**, **8% in midgame areas**, and **10% in late areas**. Legendary/mythical pool rolls are **1%**, and are confined to selected late-game habitats; if the rare roll misses, the ordinary roll can still occur. For example, in a late map with both pools, the native table retains approximately **89.1%** of encounters. Routes **101 and 102** are exempt from the bonus override, preserving the intended first wild Eevee encounter. Percentages are for the whole local pool, not for individual species.

**Evolution-stage gates:** The generator reads the official species evolution graph and stat totals, rather than assigning everything by type alone. Opening areas receive only unevolved, appropriately modest-power bonus species. Midgame areas can include first evolutions; second-stage/final-chain evolutions and especially powerful species are deferred to later maps. These are source-level gating rules, not yet a completed in-game progression test. In addition, bonus species have minimum wild levels: **18 for one-stage evolutions**, **34 for two-stage evolutions**, and **45 for legendary/mythical species**. If the original wild slot rolls a lower level, the bonus encounter is raised to its minimum. This prevents a level-4 Azumarill/Decidueye, although late-area difficulty still needs playtesting.

**Custom Eeveelution correction:** Stage 11 no longer inserts early high-stat forms such as Artheon into Petalburg Woods or Champeon/Brickeon into Granite Cave. These still have other midgame/later wild habitats and explicit evolution routes. The original Hoenn tables and existing wild Eevee placements remain intact.

### Starter sightings by generation

| Generation | Grass starter | Fire starter | Water starter |
|---|---|---|---|
| Kanto | Bulbasaur: Petalburg Woods | Charmander: Fiery Path | Squirtle: Route 118 |
| Johto | Chikorita: Route 119 | Cyndaquil: Jagged Pass | Totodile: Route 118 |
| Hoenn | Treecko: Petalburg Woods | Torchic: Fiery Path | Mudkip: Route 118 |
| Sinnoh | Turtwig: Route 119 | Chimchar: Jagged Pass | Piplup: Shoal Cave |
| Unova | Snivy: Route 119 | Tepig: Fiery Path | Oshawott: Route 118 |
| Kalos | Chespin: Route 119 | Fennekin: Jagged Pass | Froakie: Route 118 |
| Alola | Rowlet: Route 119 | Litten: Jagged Pass | Popplio: Route 118 |
| Galar | Grookey: Petalburg Woods | Scorbunny: Fiery Path | Sobble: Route 118 |
| Paldea | Sprigatito: Petalburg Woods | Fuecoco: Fiery Path | Quaxly: Route 118 |

These sightings use the bonus pools; they do **not** replace regular grass spawns. Some biomes and routes become available later in the story. The full list of all locations is generated as `stage15_solo_dex_report.json` during compilation and uploaded with the diagnostic-log artifact.

## What the automated checks do and do not prove

The source patch fails if the canonical National roster has fewer or more than 1,025 distinct entries, if a referenced species has no enum constant, if the Birch starter patch anchor changed, or if any of the 1,023 additional bonus species lacks a habitat or Carvanha lacks a native aquatic encounter. It does **not** change saved data or the meaning of a Pokédex entry.

GitHub compilation checks whether the modified ROM builds. **A successful build does not establish emulator playability or certify a completed Pokédex.**

Before calling this a beta, manually verify:
1. New game has Treecko, Torchic, Mudkip, not Eevee, in Birch's bag.
2. Route 102 still produces Eevee along with native wild Pokémon.
3. A non-Hoenn starter appears in a listed habitat.
4. Route 104 no longer produces fully evolved Azumarill, Petalburg Woods no longer produces early Artheon, and later areas produce Quilladin / Decidueye at appropriate levels.
5. A trade-evolution species (for example Gengar or Alakazam) appears in its assigned biome and can be caught, without trading.
6. The Stage 14C Birch introduction now shows its own background correctly instead of the green-tinted Eevee logo. The code fix compiled but is not visually confirmed yet.
7. Save and reload after catching a newly introduced species; confirm Pokédex registration and existing custom-Eevee forms.

Use a **fresh save** or a separately backed-up experimental save. Do not reuse your only Evergreen save.

## Compilation status

**Previous Stage 15.1 build** [#43506764573](https://github.com/Lamictal/Eevee/actions/runs/43506764573) compiled successfully before the aquatic-only Carvanha correction. The revised generator is designed to assign **1,023 bonus species across Hoenn land habitats**, plus preexisting wild Eevee and native fishing Carvanha, for **1,025/1,025 official species** with an encounter path. The revised build still requires compilation and in-game checking; successful compilation alone does not prove every habitat is reachable.

## Source and build

- Patch: [`stage15_solo_dex.py`](stage15_solo_dex.py)
- Build chain: [`stage15_patch_builder.py`](stage15_patch_builder.py)
- Workflow: [`eevee-full171-build.yml`](.github/workflows/eevee-full171-build.yml)
- No full ROM or saved games are committed to GitHub.
