# Stage 11: full-roster wild ecology across Hoenn

> **Historical Stage 11 snapshot, not the current Stage 15.1 encounter rules.** The latest ROM restores Treecko/Torchic/Mudkip, keeps wild Eevee, and adds Stage 15 bonus pools that can override ordinary wild encounters. See the [current Field Guide](EEVEE_FIELD_GUIDE.md), [Stage 15 design](STAGE15_SOLO_DEX.md), and [latest successful ROM](https://github.com/Lamictal/Eevee/actions/runs/43467069844).

**Corrected build:** [Stage 11 habitat alpha compiled successfully](https://github.com/Lamictal/Eevee/actions/runs/43276563803). **Stage 12** repairs missing evolution effects on type-booster items in the [updated build](https://github.com/Lamictal/Eevee/actions/runs/43279472956). For the complete player-facing wild encounter and evolution-item tables, see **[EEVEE_FIELD_GUIDE.md](EEVEE_FIELD_GUIDE.md)**. All 153 dual forms have 306 intended item routes, but only nine distinct duals spawn in the wild.

**Build:** [171-form habitat alpha](https://github.com/Lamictal/Eevee/actions/runs/43276563803), separate from the [previous successful 171-form source alpha](https://github.com/Lamictal/Eevee/actions/runs/43273919245).

**Stage 11 behavior at the time:** the ecology patch retained the underlying Emerald wild tables while replacing selected 5%, 4%, or 1% land slots. The Stage 11 table validator kept at least 90% of those **table slot weights** for ordinary species. **This is not a guarantee for the current Stage 15.1 game:** Stage 15 adds a separate 12% normal / optional 3% rare bonus encounter override on 61 maps. Eevee remains wild on Routes 101/102/104/117, but **Birch now offers Treecko/Torchic/Mudkip**, not Eevee. The Stage 9 Aerieon (Route 119, 5% core slot) and Aerartheon (Victory Road 1F, 1% core slot) entries still exist.

The ecology patch requires the complete Stage 10 roster. It is never applied to the separate Stage 9 two-form ROM.

## Main wild habitats

| Area | New single types | Wild chance |
|---|---|---|
| Route 117 | Normal (Neuteon), alongside Eevee | 4%, plus Eevee's 5% |
| Granite Cave 1F/B1F | Fighting; Rock | 1% each, across floors |
| Petalburg Woods | Bug | 1%, rare early sighting |
| Route 114 | Fighting | 5% |
| Route 113 | Poison | 5% |
| Fiery Path | Fire, Ground | 5% and 4% |
| New Mauville | Electric, Steel | 5% and 4% |
| Route 119 | Flying (existing), Bug | 5% and 4% |
| Route 120 | Grass, Psychic | 5% and 4% |
| Route 121 | Fairy | 5% |
| Route 123 | Grass, Fairy | 5% and 4% |
| Mt. Pyre 2F and exterior | Ghost, Dark, Psychic | 4–5% in selected locations |
| Shoal Cave low-tide inner room | Ice, Water | 5% and 4% |
| Meteor Falls 1F 2R | Dragon, Rock | 5% and 4% |
| Safari Zone North | Fairy, Bug | 5% and 4% |
| Mirage Tower 1F | Ground, Rock | 5% and 4% |
| Route 118 | Water | 5% |
| Route 110 | Electric | 1%, uncommon early sighting |
| Jagged Pass | Fire, Rock | 5% and 4% |
| Seafloor Cavern Room 1 | Water, Dark | 5% and 4% |
| Sky Pillar 1F | Dragon, Flying | 5% and 4% |

All 18 single types are represented in at least one wild location. Levels are defined by location, generally matching area progression with exceptions for very rare early evolved encounters.

## Rare dual-type wild encounters

Each dual sighting occupies **a 1% slot** in these advanced areas:

| Location | Dual types |
|---|---|
| Sky Pillar 1F | Flying/Dragon |
| Sky Pillar 3F | Psychic/Dragon, Flying/Ghost |
| Victory Road 1F | Existing Flying/Bug plus Steel/Dragon |
| Victory Road B1F | Fire/Dragon and Water/Dragon |
| Victory Road B2F | Dragon/Fairy and Dragon/Dark |
| Meteor Falls B1F 2R | Water/Dragon |

These are *selected* rare core-table sightings. **All 153 duals have intended routes through the type-item evolution system** added in Stage 10 and repaired in Stage 12; live gameplay has not yet verified all those routes. The Stage 15 official-National-Dex bonus pools do not add custom dual Eevee forms. That avoids making each map an improbable lottery.

## Evolution-item progression

The existing Stage 9/10 distribution is deliberately **preserved**:
- Oldale: Sky Catalyst
- Rustboro: Fire/Water/Thunder Stones plus Neutral, Swarm, and Stone Catalysts
- Slateport: Silk Scarf/Mystic Water/Miracle Seed plus Valor and Venom Catalysts
- Mauville: Leaf/Ice Stones and early Electric/Psychic boosters; Alloy and Earth Catalysts
- Lavaridge: Fire/Rock/Ground boosters
- Fortree: Flying/Bug/Ghost/Dark/Fighting/Poison/Steel boosters; Spirit and Dragon Catalysts
- Lilycove Department Store: all available type boosters and custom first-stage catalysts

The Stage 10 importer provides the 18-type second-stage item routes and six-badge/level-38 progression gates. Existing native Eevee paths are preserved.

## Implementation and testing

- **Source:** `stage11_full_ecology.py`, after `stage10/import_full_roster_alpha.py` in the full-alpha workflow.
- **Historical Stage 11 automatic checks:** each target map has a single 12-slot Emerald land table; all 18 singles have a habitat; dedicated rare duals occupy 1% slots; species symbols are defined; at least 90% of Stage 11 **core table weight** remains ordinary. Current Stage 15.1 adds separate bonus encounters, so total observed rates differ.
- **Save:** no additional species IDs or save changes in this stage compared with Stage 10. The full 171-form alpha itself has an expanded save layout. **Use a fresh save; migration not available.**
- **Status distinction:** a successful GitHub compile is not the same as gameplay verification. No manual tests required at this milestone unless a gameplay bug appears later.

