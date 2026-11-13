# Download and play Pokémon Eevee (alpha)

**Current version:** Stage 15.1, Monoamine 2026 · GBA · Experimental alpha. This is not yet a permanent GitHub Release.

<!-- EEVEE_LATEST_BUILD_START -->
<!-- data-build-run=43489264665 -->
**[VIEW THE LATEST TEMPORARY DEVELOPMENT BUILD](https://github.com/Lamictal/Eevee/actions/runs/43489264665)**

**Stage 15.1 - Monoamine 2026 Title and Cover Alpha** · [Successful build details](https://github.com/Lamictal/Eevee/actions/runs/43489264665)

On the build page open **Artifacts** for the ZIP if GitHub permits access. Artifacts expire after 14 days; this is not a permanent public patch release.
<!-- EEVEE_LATEST_BUILD_END -->

## Download the test build

1. Open the **latest successful build** above. Sign in to GitHub if required.
2. Scroll to **Artifacts** and select **Eevee-All171-Monoamine-2026-Alpha-GBA** (or the latest artifact starting with `Eevee-All171-`).
3. Download and **extract the ZIP**. It contains the game file `pokeemerald.gba` and optional cover images.
4. Import the **.gba** file into a compatible GBA emulator, such as mGBA. Choose **New Journey**.
5. **Start a fresh save**, keeping any existing Emerald, Evergreen or earlier Eevee alpha saves backed up separately.

For cover artwork only, choose the separately listed **Eevee-Monoamine-2026-Cover-Art** ZIP. Cover PNGs are separate emulator-library art; they are **not embedded inside the ROM**. Your emulator may let you associate an image with the imported game.

**[See full-roster build history](https://github.com/Lamictal/Eevee/actions/workflows/eevee-full171-build.yml?query=branch%3Astage8e-cloud-prototype)** if the link above expires. Only choose a run marked **Success** and note that artifacts usually expire after 14 days.

### On mobile

Extract the ZIP using your device's file manager, then import the `.gba` in your GBA emulator. Import controls and external cover support vary by emulator. Use in-game saving; avoid replacing an existing save with the same ROM filename without backing it up.

## What is actually in Stage 15.1?

- The **original Birch trio**: Treecko, Torchic and Mudkip.
- **Eevee in the wild**, including Route 102 (10% of the normal land-encounter slots), Route 101 (5%), and Route 104/117 (5% core-table slots, approximately 4.4% overall after their Stage 15 bonus pool when applicable).
- **171 Eeveelution forms**, including 18 singles and 153 unique dual-type combinations.
- Expanded solo National Dex encounter **design** assigns habitats to all **1,025 official species**, including trade and event-only Pokémon, using bonus pools across 61 habitats. **Complete in-game catchability is not verified**.
- Catalyst and typed-item evolutions, IV/EV summaries, effectiveness hints, and provisional Pokémon followers.
- New animated Eevee title, **2026 MONOAMINE** credit, and companion emulator cover art.

**[Full Eevee evolution and location guide](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_FIELD_GUIDE.md)** · **[All Eevee + 171 forms: moves by level](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_LEVEL_UP_MOVES.md)** · **[Stage 15 habitats](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/STAGE15_SOLO_DEX.md)**

## Before committing to a long playthrough

**Build Success means the ROM compiled, not that it's bug-free.** Start a new game and verify Birch's opening scene, the three starters, Route 102 Eevee, catching/party/PC behavior, and an ordinary save-reload cycle. Real custom evolution and long-story gameplay validation are still outstanding.

An old save from a different ROM version may be incompatible: there is **no supported migration path** for earlier Eevee prototype or Evergreen saves.

**[Known limitations](KNOWN_ISSUES.md)** · **[Report a bug](https://github.com/Lamictal/Eevee/issues/new/choose)**

## Is there an official release?

**No GitHub Release has been published yet.** The repository is public and the current test build is a temporary **GitHub Actions artifact**, not an approved public patch. Before a permanent release, the project must complete gameplay QA, clear third-party artwork permissions and prepare a distributable patch rather than repackaging a complete commercial Pokémon ROM.

This is an unofficial fan project; it isn't endorsed by Pokémon's rights holders.
