# Stage 9: keep original Hoenn Pokémon and distribute Eevee evolutions sensibly (historical)

> **Historical Stage 9 implementation notes.** The slot percentages below describe the **core Emerald land tables at Stage 9**. Current Stage 15.1 keeps wild Eevee and the original Hoenn starters, but adds bonus encounters across 61 Hoenn land habitats. These lower some effective core-table encounter percentages; see the [current Field Guide](EEVEE_FIELD_GUIDE.md) and [Stage 15 notes](STAGE15_SOLO_DEX.md).

## Why the balance differs from Oops! All Eevees!
The user's target game is still a traditional Pokémon Emerald playthrough,
including the original native Pokémon and storyline. We **add** the Eevee line
rather than replacing every regular wild Pokémon, trainer, or Pokédex entry.

Stage 9 code is in `stage9_world_balance.py`, invoked after the successful
Stage 8M evolution and sprite stages.

## Implemented encounter changes (two custom species only)

| Location | Added | Slots (approx) | Minimum stage |
| --- | --- | ---: | --- |
| Route 101 | Eevee, level 3-4 | 5% | Start |
| Route 102 | Eevee, level 4-5 | 10% | Start |
| Route 104 | Eevee, level 5-7 | 5% | Early |
| Route 117 | Eevee, level 12-16 | 5% | Mid |
| Route 119 | Aerieon, level 24-27 | 5% | Mid |
| Victory Road 1F | Aerartheon, level 40-42 | 1% | Late |

All other wild encounters in these maps remain at least 90% of the probability
slots, and the old early-game Aerartheon encounter is removed.
The remaining 161 reserved custom species do not appear yet. They are not
falsely advertised as implemented in the current Stage 9 ROM.

## Evolution and item locations

- **Oldale Mart:** Sky Catalyst stays in the expanded stock (Stage 8M).
- **Rustboro expanded shop:** Fire, Water, and Thunder Stones.
- **Slateport Mart:** Silk Scarf, Mystic Water and Miracle Seed.
- **Mauville Mart:** Leaf and Ice Stones, Magnet and Twisted Spoon.
- **Lavaridge Mart:** Charcoal, Hard Stone and Soft Sand.
- **Fortree Mart:** Sharp Beak, Silver Powder, Spell Tag, Black Glasses,
  Poison Barb, Black Belt and Metal Coat.
- **Lilycove Department Store 4F right clerk:** complete 18-type booster
  collection so players can deliberately evolve into any supported dual type
  once the next-stage level and badge requirements are met.

Shops retain their existing stock. These item placements are a practical
progression baseline; some stones are made purchasable earlier so the player
does not have to wait for the final city to use Eevee.

## Full 171-form ecology plan (not yet installed)

- 18 single-type forms, with relevant wild appearances in places like
  Fiery Path (Fire), Granite Cave (Rock), Petalburg Woods (Bug/Grass),
  New Mauville (Electric/Steel), Mt. Pyre (Ghost/Dark), Shoal Cave (Ice)
  and Meteor Falls (Dragon).
- Maximum ~10-15% total *new* Eevee-family wild encounter probability
  per affected map, at realistic levels. Never blanket-replace vanilla spawns.
- The 153 distinct dual-type combinations are primarily obtained by
  **choosing the second type with an item**, not through 153 competing
  rare grass encounters. Rare 1% high-level sightings may be used as
  endgame encounters where appropriate.
- Six badges and level >=38 for second evolutions. The final dual item routing
  should use type-boosting items such as Sharp Beak, Mystic Water, Charcoal,
  Silver Powder, Spell Tag, etc.
- First-stage singles keep official evolution paths where practical, with
  custom catalysts for the missing ten types.
- Preserve Pokédex IDs and migrate save data deliberately before installing
  the other 161 custom species.

## Original artwork recovered

The user-supplied **Oops! All Eevees! v1.3.2** ROM and prior
`Eevee_Stage8B_Blueprint.zip` were used outside GitHub to extract
**171 named front/back sprites and color palettes** into a downloadable
personal-use artwork kit. They have not been committed to the GitHub
repository or incorporated into the Stage 9 game binary.

The original artwork often reuses shape data with species-specific palettes;
the distinct rendered sprites and original names should be preserved.
Public redistribution requires checking the original creators' permissions.
The exact source ROM hash and mapped species indices are in the kit manifest.

## QA policy

- GitHub compile, scripted encounter-rate assertions and item-symbol checks
  are developer tasks.
- The user does not need to manually play every release.
- Verify save-layout compatibility separately. No custom save structure
  is changed by the Stage 9 world-balancing patch.
- A successful build is a compiled ROM, not automatically a gameplay-verified one.
