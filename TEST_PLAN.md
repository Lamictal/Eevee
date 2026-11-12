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

## Stage 8I and Stage 8J regression checklist (new)

**Builds:** [8I graphics fix](https://github.com/Lamictal/Eevee/actions/runs/42922943309) and [8J Dex fix](https://github.com/Lamictal/Eevee/actions/runs/42923311309). Compilation and gameplay are separate gates.

1. In party screen, verify Aerieon and Aerartheon display their custom 32×32 icons, not Eevee.
2. Put each custom species first in party and walk outside; follower must display species-specific art rather than Substitute. Check facing down/up/side, running, doorway transitions and swapping party leads.
3. Visit summary screen and battle; both custom species must retain their correct established battle art.
4. Catch both on Route 102; Stage 8J must register them with `No. 1026 / 1027`, show correct category, height, weight, and description, not `No. 000`.
5. Save in-game, close mGBA, relaunch, load .sav, and confirm the party, follower, Pokédex caught status, moves, and trainer progression.
6. Repeat from a COPY of the prior 8G/8H save; never overwrite the only working backup. Verify no corruption and existing Pokémon remain intact.
7. Remember the model uses *temporary 25%/11% test rates* and temporary level-6 evolution. This is not final balance.
8. If the ROM fails to boot, freezes, or shows malformed art, retain the prior ROM and save, take a screenshot and note exact steps.

**Known limitations:** Stage 8I follower sprite art is derived from the species front graphic, so some directional frames are not final hand-drawn art. Custom species are not inserted into the Hoenn **regional** Pokédex list yet; Stage 8J gives National numbers in registration. Official Evergreen content and saves are separate.

## Stage 8K starter and encounter-balance tests

- [ ] On a **new game**, reach Professor Birch's bag and inspect all three balls. First (former Treecko) should say **Eevee**, use its real sprite and show Normal typing when acquired; Torchic/Mudkip should remain selectable.
- [ ] Take Eevee through Birch's rescue, first rival battle, lab conversations, Pokédex unlock, save and reload. Check that story scripts don't assume the removed Treecko in a way that causes an error.
- [ ] Use a separate copy of an existing Stage 8J `.sav`: party, lead Pokémon/follower, dex entries, moves and IV/EV view must remain unchanged. Existing saves do **not** gain Eevee automatically.
- [ ] On Route 102, Aerieon appears in the 10% grass slot and Aerartheon in the 1% slot. Probabilities are theoretical, so a few encounters do not establish actual exact rate.
- [ ] Check other original wild Pokémon still appear, and that effectiveness symbols remain monochrome until future optional color-label UX work.
- [ ] Keep an untouched copy of the working Stage 8J ROM and save; don't overwrite with temporary new-game tests.

## Stage 8M selective evolution smoke tests

- [ ] Verify Stage 8M Actions run succeeds and publishes a ROM.
- [ ] Oldale Mart expanded stock offers Sky Catalyst for 3,000.
- [ ] Eevee under level 15 should not evolve with Sky Catalyst. At 15+, using it should evolve into Aerieon.
- [ ] Eevee leveling up on Route 102 should not evolve automatically.
- [ ] Aerieon should not auto-evolve at level 6.
- [ ] Aerieon level 38+, fewer than six badges: Sky Catalyst should not evolve it.
- [ ] Aerieon level 38+, six badges: Sky Catalyst should evolve into Aerartheon.
- [ ] Confirm one catalyst is consumed per successful evolution; standard Eevee evolution paths remain unchanged.
- [ ] Back up saves and check save/reload and a copy of a Stage 8L save. Never mix Evergreen saves with this engine.
