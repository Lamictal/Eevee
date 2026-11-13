# Beta 1 and first public release roadmap

_Last reviewed source status: 2026-11-13 (Stage 15.1 / Stage 14C compiled; Birch correction pending emulator verification)._

## Current deliverable

[Stage 15.1 full 171-form Monoamine alpha](https://github.com/Lamictal/Eevee/actions/runs/43467069844): **compiled successfully**, with original Hoenn starters, 1,025-species solo National Dex habitats, animated title, and cover art. The repository is **public**, but the build artifact is not a published GitHub Release or a vetted public redistribution package. Birch's visual transition remains pending fresh emulator verification.

Existing implemented systems:
- 18 singles + 153 unordered dual types, 171 total; includes eight original Eeveelutions.
- The normal Emerald Pokémon and storyline, with species-specific wild encounter distributions for all 18 singles plus nine rare wild dual forms.
- Treecko, Torchic, Mudkip restored as normal Hoenn starters; **wild Eevee** on Routes 101/102/104/117.
- 306 directed item evolution routes from the 18 singles to all 153 unordered pairs; six-badge/level-38 dual evolution gating.
- First-stage catalysts and type-boosting items available in Hoenn marts; Lilycove stocks all 18 type boosters.
- IV/EV summary, move effectiveness hints, double-B fleeing, provisional followers/icons.
- Full original Oops! All Eevees front/back battle artwork ported from a user-supplied source.

## Why it's alpha rather than a stable release

- **A green build is not gameplay validation.** Need a short fresh-save in-emulator smoke test and a save/reload test to verify expanded Pokédex flags and PC boxes.
- **Some graphics remain provisional.** Party icons and multi-direction follower sheets were previously improved for Aerieon and Aerartheon, not yet hand-polished for all 163 custom species.
- **Evolution routes require gameplay validation.** Static source checks verify 306 definitions and item effect bits; confirm real item consumption, unchanged native Eevee evolutions, gate behavior and party-menu flow.
- **Balance requires playtesting.** Abilities, level-up movesets, level curves, wild encounter rates, progression gating and shop pricing need review.
- **Save migration isn't implemented.** Earlier prototypes, Evergreen files, and this full-roster alpha should not be assumed compatible. Back up saves and begin with a new one.

## Minimum gate for a friend-playable v0.1 beta

1. Fresh game boots in mGBA; **Birch's intro background renders correctly**, his starter bag offers Treecko / Torchic / Mudkip, and wild Eevee appears early.
2. Eevee evolves with one custom first-stage catalyst at the right level, and doesn't evolve before the threshold.
3. Both dual-evolution paths into one unordered pair work, with six badges and level 38; wrong badge/level checks block correctly.
4. One traditional Eevee evolution still works (e.g., a Fire Stone for Flareon).
5. Save, quit and reload with at least one custom species in the party and another in the PC; confirm no corruption or lost progress.
6. Check a custom species in the Pokédex, party menu, battle and follower.
7. Test shops and item use, catching Pokémon, one trainer battle, and a few basic story events.

This is a **small milestone QA pass**, not 171 manual evolutions. Automated source checks remain in CI.

## Optional enhancements after Beta 1

- Better following Pokémon animations and party icons for all 163 custom forms.
- Readable colored move-effectiveness UI (tracked by [issue #3](https://github.com/Lamictal/Eevee/issues/3)).
- Better evolution selection UI, item descriptions, and clearer badge/level error messages.
- Optional future starter selection customization, only if we actually need an extra Eevee starter slot (currently not planned; wild Eevee makes it unnecessary).
- Regional/National Pokédex usability improvements and comprehensive habitat index.
- Stronger balancing for moves, stats, abilities, and late-game dual-type opponents.
- Save migration or frozen versioned save schema for upgrades.
- Longer playthrough regression checks and stabilization.

## Public sharing and ownership checklist

The GitHub repository is **public**. Anyone can browse and fork its public source, but only authorized collaborators have write permissions. Don't grant edit access merely so someone can test the game.

Before changing visibility or making a public Release:
- Inspect source and history for sensitive files or secrets.
- Check rights or obtain permission to redistribute the third-party *Oops! All Eevees!* illustrations/sprites.
- Avoid distributing a full commercial Pokémon ROM. If distribution rights permit, prepare a clearly sourced patch, attribution and installation instructions instead.
- Keep player saves out of the repository.
- Don't describe the game as endorsed by Pokémon, Nintendo, Game Freak or the *Oops! All Eevees!* creators.
- Publish release notes with build identifier, version, known limitations, controls, save warning and bug report instructions.

**Stage 15.1 is an experimental alpha and has not completed the Beta 1 acceptance tests.**
