# Stage 11: full-roster wild ecology across Hoenn

**Corrected build:** [Stage 11 habitat alpha compiled successfully](https://github.com/Lamictal/Eevee/actions/runs/43276563803). **Stage 12** repairs missing evolution effects on type-booster items in the [updated build](https://github.com/Lamictal/Eevee/actions/runs/43279472956). For the complete player-facing wild encounter and evolution-item tables, see **[EEVEE_FIELD_GUIDE.md](EEVEE_FIELD_GUIDE.md)**. All 153 dual forms have 306 intended item routes, but only nine distinct duals spawn in the wild.

**Build:** [171-form habitat alpha](https://github.com/Lamictal/Eevee/actions/runs/43276563803), separate from the [previous successful 171-form source alpha](https://github.com/Lamictal/Eevee/actions/runs/43273919245).

The game retains all original Emerald wild species and existing encounters except selected 5%, 4%, or 1% land slots. **At least 90% of the land encounter probability in every modified map remains regular Pokémon.** Eevee continues to be wild on Routes 101/102/104/117 and is the starter option. Stage 9's Aerieon (Route 119, 5%) and Aerartheon (Victory Road 1F, 1%) encounters are retained.

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

These are *selected* rare sightings. **All 153 duals remain obtainable via the deliberate type-item evolution system** added in Stage 10; they are not all assigned separate wild slots. That avoids making each map an improbable lottery.

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
- **Automatic checks:** every target map has exactly one 12-slot Emerald land table; all 18 single types have a habitat; rare duals occupy 1% slots only; species symbols are defined; at least 90% of slots remain native; the Stage 9 encounters are not removed.
- **Save:** no additional species IDs or save changes in this stage compared with Stage 10. The full 171-form alpha itself has an expanded save layout. **Use a fresh save; migration not available.**
- **Status distinction:** a successful GitHub compile is not the same as gameplay verification. No manual tests required at this milestone unless a gameplay bug appears later.

