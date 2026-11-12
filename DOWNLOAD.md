# Download and play Eevee (Alpha)

**Current version:** Stage 12, an experimental 171-form Pokémon Emerald Expansion build.

**[DOWNLOAD CURRENT ALPHA ZIP](https://github.com/Lamictal/Eevee/actions/runs/43279472956/artifacts/13972053637)**

This is the exact artifact from the [successful Stage 12 GitHub build](https://github.com/Lamictal/Eevee/actions/runs/43279472956). It is called **Eevee-All171-ItemEvolutions-Alpha-GBA**.

> **Important:** This is a **temporary development build**, not a permanent public release or an officially supported download. The repository is currently private; only people with access to it can use the link. GitHub build artifacts typically expire (this workflow retains them for **14 days**). Public redistribution of the full ROM or the original *Oops! All Eevees!* artwork has not been cleared.

## Getting the game (no GitHub experience required)

1. **Open the download link above.** Sign in to GitHub if prompted. You need access to this repository while it is private. If it says **404** or **Not Found**, you do not currently have access; this is not an issue with your emulator.
2. **Download the ZIP file** if prompted. If the link opens the build page instead, find **Artifacts** at the bottom and select **Eevee-All171-ItemEvolutions-Alpha-GBA**.
3. **Extract/unzip the download.** You should get a **.gba** game file (typically \`pokeemerald.gba\`). Do **not** try to open the ZIP as a save file.
4. **Open the extracted .gba in your GBA emulator** (for example, mGBA on a computer). Use your emulator's normal **Open ROM / Import** command.
5. Select **New Game**. **Do not load an older Eevee alpha or Evergreen save.** This build expands the Pokédex save layout. Keep your existing save files separately backed up.

### Where is the latest build if this link expires?

**[See the latest full-roster build runs](https://github.com/Lamictal/Eevee/actions/workflows/eevee-full171-build.yml?query=branch%3Astage8e-cloud-prototype)**. Open a run marked **Success**, scroll to **Artifacts**, and choose the alpha ZIP. Only download builds from the trusted project repository.

### On a phone

Use a GBA emulator that can import a \`.gba\` game file. You may need to extract the ZIP first in your phone's file manager. The emulator's buttons, import process and save-file location depend on the app.

## What is in this version?

- 18 single-type Eeveelutions and 153 unordered dual-type combinations (**171 total**).
- Normal Pokémon and Hoenn's original adventure remain.
- Eevee as a starter option and in selected early routes.
- All 18 single types appearing in wild encounters; nine distinct rare wild dual forms in advanced locations.
- Evolution catalysts and 18 second-type booster items across Hoenn. At level **38+**, with **six badges**, use a booster for the desired second type on a single-type Eeveelution.
- The item evolution code has passed static checks for 306 routes; **not every evolution has been verified in a running emulator**.

**[Where to find every Eevee form and evolution item](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_FIELD_GUIDE.md)**

## Common questions

**Why does the link say 404?** The repository is private until its owner makes it public, so a random friend cannot download it yet. Also check that the artifact has not expired.

**Can my friend edit the project when it becomes public?** No. Public GitHub repositories are viewable and forkable by anyone, but only authorized collaborators can directly push edits.

**Can I carry over my old save?** No supported migration is available. Use a new save, and keep a backup of the older one.

**Does "Build successful" mean "bug-free"?** No. It means the GBA ROM compiled. A short in-emulator test is still necessary before a player-friendly beta release.

**Can this page have a permanent one-click download?** Yes, once the project has a **public release artifact** and distribution rights are confirmed. The intended safer route is a **ROM patch file** with installation instructions, not a full commercial Pokémon ROM.

## Bugs and feedback

**[Report a bug](https://github.com/Lamictal/Eevee/issues/new/choose)**. Include the build version, emulator, steps to reproduce, and what happened. If the repository is private, the reporter needs access.

## Release and attribution notes

This is an unofficial fan project built with [pokeemerald-expansion](https://github.com/rh-hideout/pokeemerald-expansion). Some sprites were imported from *Oops! All Eevees!* provided for personal testing; public redistribution permissions are not established. No affiliation or endorsement by Nintendo, Game Freak or The Pokémon Company is claimed. Do not publish a full copyrighted game ROM as a "free download."
