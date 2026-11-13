# Stage 8N: fixed 171-form registry and save-compatibility contract (historical)

> **Historical Stage 8N registry-only milestone.** The text below is accurate as a description of that planning stage, **not current ROM content**. Stage 10 later installed the full 171-form source roster; current Stage 15.1 is [here](RELEASE_NOTES_v0.1.0-alpha.md). No safe migration from Stage 8N/Evergreen saves is established; start a fresh save.

**Stage 8N status at that time:** registry and CI validation only; Stage 8N itself added no ROM species or save changes. **Current build:** [Stage 15.1, all 171 forms compiled](https://github.com/Lamictal/Eevee/actions/runs/43467069844).

## Canonical target

- 18 single-type Eeveelutions: **eight official species already supported by the engine**, plus ten new single-type forms.
- 153 unordered dual-type combinations, all custom.
- **171 total forms = 8 native + 163 custom**, not 171 new species beyond the native ones.
- Aerieon (Flying) keeps custom National Dex #1026.
- Aerartheon (Flying/Bug) keeps custom National Dex #1027.
- Reserve custom Dex #1028..#1188 for the other **161** custom forms.
- Official forms preserve their actual National Dex numbers and existing normal evolutions.
- Never assign a placeholder custom *species symbol or name* that might overwrite a real Evergreen form. Stage 8N records null names/symbols for future forms until the old roster is recovered or redesigned.

The canonical machine-readable form list lives at [data/eevee_form_registry.json](data/eevee_form_registry.json). Validation: `python3 tools/validate_eevee_registry.py`.

## Evolution design (future target; not yet all in game)

1. Eevee -> one of the eighteen single types using the type's original evolution method or its dedicated catalyst. Prototype Aerieon uses Sky Catalyst at level 15+.
2. A single -> a dual form by combining its existing type with a second chosen type; the chosen extra type determines the catalyst.
3. Dual evolution unlocks at level 38+ and six badges. The eventual design may support either single-type parent for each unordered pair, since Flying/Bug and Bug/Flying should not duplicate a species.
4. **Stage 8M exception:** existing Aerieon -> Aerartheon currently uses Sky Catalyst at level 38 and six badges. That is a valid initial test path, not the final universal typed-catalyst routing.
5. Original eight Eeveelutions must remain obtainable. No item that ambiguously resolves to multiple targets without an explicit choice.

## Why the save may break on full roster introduction

The current National Dex ends at 1027 and `POKEMON_SLOTS_NUMBER = NATIONAL_DEX_COUNT + 1`.
The engine allocates:

```c
#define NUM_DEX_FLAG_BYTES ROUND_BITS_TO_BYTES(POKEMON_SLOTS_NUMBER)
// SaveBlock1:
// u8 dexSeen[NUM_DEX_FLAG_BYTES];
// u8 dexCaught[NUM_DEX_FLAG_BYTES];
```

| Layout | Dex count | Bytes per seen/caught array |
| --- | ---: | ---: |
| Current 8M source | 1027 | 129 |
| 171-form final registry | 1188 | 149 |
| Change | +161 | **+20 per array** |

That's **40 extra saved bytes across the two arrays**, potentially shifting fields that follow them inside SaveBlock1. It is *not* automatically compatible merely because both ROMs compile. It also affects save-block size limits and any dex-indexed RAM/UI structures.

**No change to SaveBlock1 is made in Stage 8N.** Before Stage 9 expands the actual National Dex:

- Freeze the upstream engine Git commit and both existing custom species enum values.
- Choose a versioned migration path (or an explicitly audited fixed-capacity design) so old save fields aren't silently misread.
- Ensure previous seen/caught bits are copied unchanged into the expanded arrays.
- Verify species IDs inside party and PC storage remain stable. Dex numbers are not the same as internal species enum IDs.
- Reject incompatible save formats explicitly instead of pretending they loaded correctly.
- Validate fresh-game saves, upgraded copies, in-game save/reload, both PC and party Pokémon, bag inventory, Dex flags, map progress, and save checksum/sector handling.
- Do not assume unrelated **Evergreen 2.0 Stage 8A.1 saves** are compatible with this Emerald Expansion engine.

## Testing policy

- `tools/validate_eevee_registry.py` must pass on each registry change: 18/153 uniqueness, eight native species, 163 custom Dex IDs, original two fixed IDs, level/badge requirements, and accurate save-footprint math.
- Build failures are developer problems, not user gameplay tasks.
- When save migration is implemented, run automated synthetic-fixture tests plus scripted emulator tests when possible.
- In-game manual smoke tests should happen **at milestone releases**, not after every individual item or custom species. No Stage 8N manual test is needed.

## Next milestones

1. **Stage 9A:** recover the original Evergreen design names/artwork/evolution items for the previous 30-form prototype; keep unverified entries reserved in this manifest.
2. **Stage 9B:** generate and integrate the other missing single-type custom species and final single-type catalyst selection.
3. **Stage 10A:** produce the 153 unique dual-type species and both single-to-dual routes from the registry, with deterministic ID allocation, stat balancing, and placeholder art clearly labeled where needed.
4. **Stage 10B:** validate complete playability, integrate artwork, move pools, encounters, balance and migration. Freeze save schema before inviting a long playthrough.

A green registry CI check means only **planning data is consistent**. It does not mean the 161 reserved species are present or playable.
