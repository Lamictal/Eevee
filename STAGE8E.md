# Eevee expansion prototype: source migration and current status

This document began with Stage 8E, the first source-based Pokémon Emerald Expansion build. For current version-by-version changes, **see [CHANGELOG.md](CHANGELOG.md)**.

## Current status (November 10, 2026)

- **Latest compiled build: [Stage 8J](https://github.com/Lamictal/Eevee/actions/runs/42923311309)**. Includes repaired party icons, provisional overworld follower sprites, IV/EV summary view, effectiveness hints, double-B wild escape, and proper Pokédex registration for two experimental forms.
- **Stage 8I sprite-only build:** [successful](https://github.com/Lamictal/Eevee/actions/runs/42922943309).
- **Experimental species added:** Aerieon (Flying) and Aerartheon (Flying/Bug), with test-only level-6 evolution and Route 102 canary encounters (25% / 11% in the current build).
- **Not yet finished:** Full 171 Eeveelutions, Eevee starter selection, Evergreen-specific content, refined 4-direction overworld sprites, final balancing, and full save migration verification.
- **Gameplay QA:** Builds compiled successfully, but new Stage 8I/8J functionality still requires actual emulator testing. Use [TEST_PLAN.md](TEST_PLAN.md).

## Architecture

1. Build source kit shipped in `stage8d-kit.tar.xz.b64`. GitHub Actions unpacks it into `kit/`, clones upstream `rh-hideout/pokeemerald-expansion`, installs two new species and applies versioned patches.
2. Stage 8E fixes custom static animations.
3. Stage 8F enables native opponent types and move effectiveness hints.
4. Stage 8G increases Route 102 test encounters and enables double-B escape.
5. Stage 8H enables following Pokémon and IV/EV summary pages.
6. Stage 8I replaces provisional Eevee and Substitute graphics with custom art-derived icons and follower sprites.
7. Stage 8J registers Aerieon #1026 and Aerartheon #1027 with real Pokédex descriptions and measurements.

This is **not** the Evergreen 2.0 ROM or game. The original Evergreen Stage 8A.1 patch and save remain separate and untouched.

## Safety

Do not commit commercial ROMs or user saves. Keep an untouched backup of every `.sav` before testing a newly built ROM. Two new Dex entries fit in the current allocated saved seen/caught flag bytes, but **runtime migration and compatibility have not been verified**. Future 171-form expansion requires a deliberate save layout strategy.

## Build location

[GitHub Actions workflow](.github/workflows/eevee-build.yml) builds from source and publishes a GBA artifact if successful. There is no need to run a local compiler.
