# Stage 8E emulator validation plan

**Scope:** Source-based Pokémon Emerald Expansion test ROM, not Evergreen 2.0. Do **not** open an existing Evergreen save in this build. Keep existing Emerald/Evergreen and Stage 8A.1 save backups.

## Build prerequisites
- GitHub Actions build job green; output file has a valid GBA header.
- No source .gba ROMs or .sav files uploaded to the repository.
- Download the successful Eevee-Stage8E-UNTESTED-GBA artifact from the Actions run.

## Manual emulator acceptance checks
1. Launch in mGBA. Start a **new** save.
2. Enter Route 102 and encounter **Aerieon**. Its name, type (Flying), front/back image, party-menu appearance, and moves should look correct. Note that the party icon is deliberately the stock Eevee placeholder.
3. Encounter **Aerartheon** (Flying/Bug). Confirm dual typing, artwork, and moves. This is currently a rare test encounter.
4. Raise Aerieon past **level 6**; verify that it evolves into Aerartheon.
5. Save normally in-game, close the emulator, restart, and reload. Check that the custom species in the party survives. Test a battle after reload.
6. Confirm ordinary Pokémon still spawn on Route 102 and can battle normally.
7. If anything appears as ??, missing art, or crashes, record the screen, exact step, and any emulator error.

## Limitations
- Temporary level-6 evolution and wild encounter slots are strictly for testing. Intended eventual gating: six badges and level 38 with an item catalyst.
- Not yet 171 implemented species. The manifest covers 171 planned forms; only two proof-of-concept species are installed.
- This prototype does not preserve Evergreen features or save compatibility.
- A successful build by itself does not establish emulator correctness.
