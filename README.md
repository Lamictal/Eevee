# Eevee: 171-form Emerald Expansion

A Pokémon Emerald Expansion project adding **18 single-type + 153 unique dual-type Eeveelutions** while keeping ordinary Hoenn Pokémon and the regular story.

### Player guide

**[Wild Eevee and Eeveelution locations, all catalysts and item shops, plus dual evolution rules](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_FIELD_GUIDE.md)**

**Are all 153 dual forms available in the wild?** No. **Nine distinct dual forms** have rare (mostly 1%) late-game wild encounters. Most are obtained through type-item evolutions.

**Can every single type evolve into any dual type?** The current source defines **17 evolution choices from each of the 18 single-type forms**, making every unordered dual combination available through two possible single-type parents. At **level 38+ and six badges**, use the type-boosting item for the **second type** on your single-type Eeveelution, e.g. **Aerieon + Silver Powder → Aerartheon**.

**Important version note:** [Stage 11 compiled](https://github.com/Lamictal/Eevee/actions/runs/43276563803) but its type-boosters were missing the evolution item-effect flag. The [Stage 12 correction build](https://github.com/Lamictal/Eevee/actions/runs/43279472956) fixes that source issue and checks all **306** directed item routes. The game has not yet undergone full emulator QA; use the **latest successful Stage 12 artifact** for actual item-evolution gameplay.

### Eevee sightings

| Place | Encounter chance |
|---|---:|
| Professor Birch's starter bag | Choose Eevee (replaces Treecko option) |
| Route 101 | 5% |
| Route 102 | 10% |
| Route 104 | 5% |
| Route 117 | 5% |

The other **18 single-type forms** have their own Hoenn habitats; see the full guide for exact routes and rates.

### Evolution items and towns

| Town | Added Eevee-related item access |
|---|---|
| Oldale | Sky Catalyst |
| Rustboro | Fire/Water/Thunder Stones; Neutral, Swarm, Stone Catalysts |
| Slateport | Valor, Venom Catalysts; Silk Scarf, Mystic Water, Miracle Seed |
| Mauville | Alloy, Earth Catalysts; Leaf/Ice Stones, Magnet, Twisted Spoon |
| Lavaridge | Charcoal, Hard Stone, Soft Sand |
| Fortree | Spirit, Dragon Catalysts; Flying/Bug/Ghost/Dark/Fighting/Poison/Steel type boosters |
| Lilycove Dept. Store 4F | **All 18 second-type boosters**, plus nine first-stage custom Catalysts (Sky is in Oldale) |

### Current development

- [**Active source development branch**](https://github.com/Lamictal/Eevee/tree/stage8e-cloud-prototype)
- [**Complete player-facing encounter and evolution item guide**](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_FIELD_GUIDE.md)
- [**Stage 11 habitat and progression design notes**](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/STAGE11_HABITATS.md)
- [**Full-roster Stage 12 build status**](https://github.com/Lamictal/Eevee/actions/runs/43279472956)

**Save compatibility:** the 171-form alpha expands the Pokédex save structure. Start a **new save** and keep prior saves backed up; older Stage 8/9 and separate Evergreen saves have not been migrated. A green compile is not a claim of full in-game verification.

This `main` README is a landing page. The actual ROM build scripts, issue tracking, and the detailed guide live on the `stage8e-cloud-prototype` branch.
