# Eevee expansion (Stage 8E)

Experimental **source-based** expansion of Pokémon Emerald, separate from the known-working Evergreen Stage 8A.1 patch and save. The goal is 18 single-type Eeveelutions plus 153 dual-type combinations while keeping standard Pokémon intact.

## Current state

- Connected GitHub repository: `Lamictal/Eevee`.
- Initial cloud-build workflow on branch `stage8e-cloud-prototype`.
- The Stage 8D source kit is **not yet committed**; the workflow cannot build until the source kit is added.
- First target: Aerieon (Flying) and Aerartheon (Flying/Bug) with a temporary level-6 evolution and Route 102 test encounters.
- The full 171-species roster is a plan, **not 171 implemented species**.
- No new playable ROM has been compiled or emulator-tested from this source prototype.

## Safety

Never commit commercial game ROMs or existing save files. Distribute source modifications and BPS patches only. Keep all Evergreen Stage 8A.1 files unchanged. A source build needs a new save and does not preserve Evergreen gameplay/content automatically.

## Build

The GitHub Actions workflow is at `.github/workflows/eevee-build.yml`. It attempts a source compilation from `stage8d-kit.tar.xz.b64` after decoding it; until that package is committed, builds fail at the unpack stage.
