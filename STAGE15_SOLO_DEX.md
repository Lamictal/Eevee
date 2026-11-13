# Stage 15: Original Hoenn starters and solo National Pokédex

This milestone extends the **171-form Eevee Emerald Expansion alpha**. It is not an Evergreen save-compatible release. Stage 14's animated Eevee title and Birch graphics transition correction remain in place.

## Starters and Eevee

- Professor Birch's original three options are **Treecko, Torchic, and Mudkip**. Stage 8K's temporary Eevee replacement is reversed at the end of the source build.
- **Eevee remains catchable on Route 102** at the existing natural encounter rate. Other early Eevee encounters from Stage 9 remain untouched. Eevee does not require a separate starter slot.
- All three original starters and their later evolutions are included in the solo-Dex encounter coverage.

## Solo-completable National Pokédex

- The project generates habitats for **all 1,025 canonical National Pokédex species**, from Bulbasaur through Pecharunt.
- Eevee is already available in the normal Route 102 encounter table. The other **1,024 species** are each assigned a deterministic, biome-oriented bonus encounter habitat.
- **No online trade or limited-time event is needed to get a National Pokédex species**. Even species traditionally evolved via trading, or distributed through events, have a possible direct wild encounter.
- This is **National Dex species coverage**, not a guarantee of every alternate battle form, variant, costume, regional form, or gender-specific appearance.
- The **171 Eevee forms**, including eight canonical species, remain governed by the existing Stage 10–12 item-evolution mechanics. All 153 dual forms are intended to remain reachable via item paths, pending in-game QA.

## Encounter balance and locations

Existing Hoenn land encounter tables are **not replaced**. Fishing, surfing, rocks, story/static encounters, trainer teams, item shops, and Pokédex save layout are not changed.

In selected land habitats, ordinary species are drawn from a local extra-species pool on approximately **12% of wild encounters**. Rare legendary/mythical entries have their own approximately **3% pool** where applicable, largely in late-game locations such as Sky Pillar, Victory Road, Meteor Falls, Shoal Cave, and Mt. Pyre. The odds of *one specific species* are the pool's chance divided by its population; do not mistake 12% for the chance of one specific Pokémon.

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

The source patch fails if the canonical National roster has fewer or more than 1,025 distinct entries, if a referenced species has no enum constant, if the Birch starter patch anchor changed, or if any of the 1,024 additional species lacks a habitat. It does **not** change saved data or the meaning of a Pokédex entry.

GitHub compilation checks whether the modified ROM builds. **A successful build does not establish emulator playability or certify a completed Pokédex.**

Before calling this a beta, manually verify:
1. New game has Treecko, Torchic, Mudkip, not Eevee, in Birch's bag.
2. Route 102 still produces Eevee along with native wild Pokémon.
3. A non-Hoenn starter appears in a listed habitat.
4. A trade-evolution species (for example Gengar or Alakazam) appears as a wild encounter and can be caught.
5. The Stage 14B Birch screen is no longer green or backed by the Eevee title image.
6. Save and reload after catching a newly introduced species; confirm Pokédex registration and existing custom-Eevee forms.

Use a **fresh save** or a separately backed-up experimental save. Do not reuse your only Evergreen save.

## Source and build

- Patch: [`stage15_solo_dex.py`](stage15_solo_dex.py)
- Build chain: [`stage15_patch_builder.py`](stage15_patch_builder.py)
- Workflow: [`eevee-full171-build.yml`](.github/workflows/eevee-full171-build.yml)
- No full ROM or saved games are committed to GitHub.
