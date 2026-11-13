# Stage 15: Original Hoenn starters and solo National Pokédex

This milestone is part of the **Stage 15.1 Monoamine Eevee Emerald Expansion alpha**. It is not Evergreen save-compatible. The animated title screen is present, and the Stage 14C Birch-background correction **compiled successfully**; actual emulator confirmation is still required.

## Starters and Eevee

- Professor Birch's original three options are **Treecko, Torchic, and Mudkip**. Stage 8K's temporary Eevee replacement is reversed at the end of the source build.
- **Eevee remains catchable on Route 102** at the existing natural encounter rate. Other early Eevee encounters from Stage 9 remain untouched. Eevee does not require a separate starter slot.
- All three original starters and their later evolutions are included in the solo-Dex encounter coverage.

## Solo-completable National Pokédex

- The source generator assigns a bonus wild habitat to **1,024 of the 1,025 canonical National Pokédex species**, from Bulbasaur through Pecharunt. **Eevee** already appears in normal wild tables. This is an automated coverage claim, **not** a verified completion of the National Dex in-game.
- Eevee is already available in the normal Route 102 encounter table. The other **1,024 species** are each assigned a deterministic, biome-oriented bonus encounter habitat.
- The intended design avoids online trading and limited-time events, including for trade-evolution and event-only Pokémon. **Every official species has a scripted potential encounter**, but actual map accessibility, encounter behavior, Pokédex registration and catchability still need emulator checks before guaranteeing full completion.
- This is **National Dex species coverage**, not a guarantee of every alternate battle form, variant, costume, regional form, or gender-specific appearance.
- The **171 Eevee forms**, including eight canonical species, remain governed by the existing Stage 10–12 item-evolution mechanics. All 153 dual forms are intended to remain reachable via item paths, pending in-game QA.

## Encounter balance and locations

Existing Hoenn land encounter tables are **not replaced**. Fishing, surfing, rocks, story/static encounters, trainer teams, item shops, and Pokédex save layout are not changed.

In **61 selected land habitats**, the game can replace a normal table encounter with an extra species: an ordinary pool triggers on **12%** of rolls where reached. In maps with a rare legendary/mythical pool, the **3% rare roll happens first**; if it fails, the 12% ordinary roll runs, leaving approximately **85.36%** of encounters to the original table (versus 88% on maps with only an ordinary bonus pool). On Routes **101 and 102**, the Stage 15 override is disabled. These percentages are **pool probabilities, not odds for a specific Pokémon**; those depend on the local pool size. The original land tables remain in the code, but some actual encounter rates are reduced by the override.

**Important implementation detail:** The bonus replacement happens *after* the engine chooses a level from the original wild encounter slot. A bonus species therefore inherits that slot's chosen level; the current source does **not** define a separate per-species bonus level range. This needs balance testing, especially for legendary/mythical encounters.

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
4. A trade-evolution species (for example Gengar or Alakazam) appears in its assigned biome and can be caught, without trading.
5. The Stage 14C Birch introduction now shows its own background correctly instead of the green-tinted Eevee logo. The code fix compiled but is not visually confirmed yet.
6. Save and reload after catching a newly introduced species; confirm Pokédex registration and existing custom-Eevee forms.

Use a **fresh save** or a separately backed-up experimental save. Do not reuse your only Evergreen save.

## Compilation status

**Latest Stage 15.1 compiled successfully** in [GitHub Actions run #43467069844](https://github.com/Lamictal/Eevee/actions/runs/43467069844). The source checks generated 1,024 bonus species across **61 Hoenn land habitats**, plus the preexisting early wild Eevee, for **1,025/1,025 canonical National Dex species** with an assigned encounter path. The updated ROM artifact was uploaded. These checks do **not** establish every encounter's in-game accessibility or a fully completable Pokédex; manual mGBA tests of Birch, catching, evolution, saving and loading remain necessary.

## Source and build

- Patch: [`stage15_solo_dex.py`](stage15_solo_dex.py)
- Build chain: [`stage15_patch_builder.py`](stage15_patch_builder.py)
- Workflow: [`eevee-full171-build.yml`](.github/workflows/eevee-full171-build.yml)
- No full ROM or saved games are committed to GitHub.
