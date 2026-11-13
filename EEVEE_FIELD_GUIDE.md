# Eevee Field Guide: 171-Form Hoenn Alpha

> **Latest build status:** [latest Stage 15.1 Monoamine 2026 build compiled successfully](https://github.com/Lamictal/Eevee/actions/runs/43467069844), including the Stage 12 dual-item fix, restored original Hoenn starters, and solo National Dex habitats. Compilation is not emulator playtesting. **Use a fresh save**; older prototype / Evergreen saves are not confirmed compatible.

**Short answer:**
- **No:** not all 153 dual forms spawn in the wild. There are **nine distinct rare dual forms** in selected advanced locations, generally **1% per encounter slot**, with Water/Dragon in two areas.
- **Yes, in the Stage 12 source design:** every one of the **18 single-type forms** has **17 item evolution routes**, one for each *different* second type. That's **306 routes to 153 unique unordered dual forms**. The selected second-type booster item determines which pair you get. The Stage 12 fix enables the actual evolution effect on held type boosters; earlier Stage 11 builds lacked that effect and should **not** be relied on for dual-item evolution.
- **Level/badge gate:** a single-type Eeveelution must be **level 38+** and you must have **at least 6 Hoenn badges** before using the relevant booster as an evolution item.
- **Every dual form is intended to be obtainable without a wild encounter** via these evolutions. Individual in-game evolution outcomes are still pending emulator QA.
- Original Emerald land encounter tables, fishing/surfing tables, story, and native Eevee evolutions remain in the source. **Important:** Stage 15 also adds a separate encounter override on 61 land maps. Therefore the older Stage 11 guarantee that 90% of actual encounters are ordinary Pokémon no longer applies on those maps. See the rates note below.

## Stage 15: Complete the National Pokédex without online trades

The current source assigns a potential wild encounter to **each of the 1,025 official National Pokédex species**, including trade-evolution and event-only species. This is a source-level coverage check, **not** proof that every habitat is accessible, every catch succeeds, or the complete Pokédex is attainable in a real playthrough. Birch now offers the **original Treecko, Torchic and Mudkip** starter trio. Eevee stays wild on Route 102 and other early routes. Rare legendary/mythical species are concentrated in later locations.

See the [complete solo-Dex design, starter location chart, rarity notes, and testing checklist](STAGE15_SOLO_DEX.md). The build also generates a per-map species report, packaged with its diagnostic logs. Compilation alone is not emulator confirmation.

## 1. Where to find Eevee

| Location | Eevee level | Core land-table slot |
|---|---:|---:|
| Route 101 | 3–4 | **5%** |
| Route 102 | 4–5 | **10%** |
| Route 104 | 5–7 | **5%** |
| Route 117 | 12–16 | **5%** |

**Eevee is not a starter.** Birch offers **Treecko, Torchic, and Mudkip**. Eevee is caught in the wild. The Stage 15 bonus-encounter override does **not** run on Routes 101 and 102, so their listed 5% and 10% are the direct normal land-table odds. On Routes 104 and 117, Stage 15 can replace an otherwise normal encounter with a bonus species (12% chance), lowering Eevee's effective ordinary-encounter odds to approximately **4.4%** on each of those routes. Normal abilities and other encounter modifiers can affect observed results.

You can collect dual forms through evolution without having to find a rare wild dual.

## 2. All 18 single-type Eeveelutions in the wild

Percentages below are the **core land-encounter table slot weights**, before the Stage 15 bonus encounter override. On a map with a normal bonus pool, 12% of ordinary encounters can be replaced; on maps that also host a legendary/mythical bonus pool, the 3%-rare roll occurs first and the 12%-ordinary roll is then attempted on the remaining 97%, leaving approximately **85.36%** for the underlying encounter table. Some rare encounters may be easier to obtain via evolution.

| Type | Eeveelution | Wild locations and chances |
|---|---|---|
| Normal | **Neuteon** | Route 117 (4%) |
| Fighting | **Champeon** | Granite Cave 1F (1%), Route 114 (5%) |
| Flying | **Aerieon** | Route 119 (5%), Sky Pillar 1F (4%) |
| Poison | **Vireon** | Route 113 (5%) |
| Ground | **Duneon** | Fiery Path (4%), Mirage Tower 1F (5%) |
| Rock | **Brickeon** | Granite Cave B1F (1%), Mirage Tower 1F (4%), Jagged Pass (4%), Meteor Falls 1F 2R (4%) |
| Bug | **Artheon** | Petalburg Woods (1%), Route 119 (4%), Safari Zone North (4%) |
| Ghost | **Fanteon** | Mt. Pyre 2F (5%), Mt. Pyre exterior (5%) |
| Steel | **Ferumeon** | New Mauville interior (4%) |
| Fire | **Flareon** | Fiery Path (5%), Jagged Pass (5%) |
| Water | **Vaporeon** | Route 118 (5%), Shoal Cave low-tide inner room (4%), Seafloor Cavern Room 1 (5%) |
| Grass | **Leafeon** | Route 120 (5%), Route 123 (5%) |
| Electric | **Jolteon** | Route 110 (1%), New Mauville interior (5%) |
| Psychic | **Espeon** | Route 120 (4%), Mt. Pyre exterior (4%) |
| Ice | **Glaceon** | Shoal Cave low-tide inner room (5%) |
| Dragon | **Drakeon** | Meteor Falls 1F 2R (5%), Sky Pillar 1F (5%) |
| Dark | **Umbreon** | Mt. Pyre 2F (4%), Seafloor Cavern Room 1 (4%) |
| Fairy | **Sylveon** | Route 121 (5%), Route 123 (4%), Safari Zone North (5%) |

**Note:** Stage 11 changed selected rare slots in existing Hoenn tables. Stage 15 adds a separate chance to replace a normal encounter on designated maps; the original tables remain, but observed percentages are lower when that bonus pool triggers.

## 3. Which dual forms appear in the wild?

**The following nine distinct custom dual-type forms** have dedicated wild slots in Stage 11. All are **1% slots in the core encounter table**, before any Stage 15 encounter override.

| Location | Rare wild dual Eeveelution | Levels |
|---|---|---|
| Victory Road 1F | **Aerartheon** (Flying/Bug) | 40–42 |
| Victory Road 1F | **Draferreon** (Steel/Dragon) | 40–42 |
| Victory Road B1F | **Draflareon** (Fire/Dragon) | 41–43 |
| Victory Road B1F | **Dravapreon** (Water/Dragon) | 41–43 |
| Victory Road B2F | **Syldrakeon** (Dragon/Fairy) | 43–45 |
| Victory Road B2F | **Umbdrakeon** (Dragon/Dark) | 43–45 |
| Sky Pillar 1F | **Aerdrakeon** (Flying/Dragon) | 39–40 |
| Sky Pillar 3F | **Draespeon** (Psychic/Dragon) | 39–41 |
| Sky Pillar 3F | **Aerfanteon** (Flying/Ghost) | 39–41 |
| Meteor Falls B1F 2R | **Dravapreon** (Water/Dragon) | 38–40 |

The other **144 custom dual-type Eeveelutions** have no dedicated wild habitat in the current scripts and are intended to be obtained through evolution. **Stage 15's solo National Dex bonus pools cover official species only, not these 144 custom duals.** Evolution outcomes still need in-game testing.

## 4. Eevee → single-type form: item / condition and location

For the **ten custom single-type forms**, use the appropriate **Catalyst** on Eevee at **level 15+**. Original eight Eeveelution mechanics remain native to Emerald Expansion.

| Result | Eevee's first evolution | Where to get the item |
|---|---|---|
| Neuteon (Normal) | **Neutral Catalyst**, Lv. 15+ | Rustboro expanded Mart; Lilycove 4F |
| Champeon (Fighting) | **Valor Catalyst**, Lv. 15+ | Slateport Mart; Lilycove 4F |
| Aerieon (Flying) | **Sky Catalyst**, Lv. 15+ | **Oldale expanded Mart**, 3,000 (not part of the Lilycove nine-catalyst stock) |
| Vireon (Poison) | **Venom Catalyst**, Lv. 15+ | Slateport Mart; Lilycove 4F |
| Duneon (Ground) | **Earth Catalyst**, Lv. 15+ | Mauville Mart; Lilycove 4F |
| Brickeon (Rock) | **Stone Catalyst**, Lv. 15+ | Rustboro expanded Mart; Lilycove 4F |
| Artheon (Bug) | **Swarm Catalyst**, Lv. 15+ | Rustboro expanded Mart; Lilycove 4F |
| Fanteon (Ghost) | **Spirit Catalyst**, Lv. 15+ | Fortree Mart; Lilycove 4F |
| Ferumeon (Steel) | **Alloy Catalyst**, Lv. 15+ | Mauville Mart; Lilycove 4F |
| Drakeon (Dragon) | **Dragon Catalyst**, Lv. 15+ | Fortree Mart; Lilycove 4F |
| Flareon (Fire) | Fire Stone | Rustboro expanded Mart |
| Vaporeon (Water) | Water Stone | Rustboro expanded Mart |
| Jolteon (Electric) | Thunder Stone | Rustboro expanded Mart |
| Leafeon (Grass) | Leaf Stone or original location requirement | Mauville Mart (stone) |
| Glaceon (Ice) | Ice Stone or original location requirement | Mauville Mart (stone) |
| Espeon (Psychic) | High friendship and level up during the day | No catalyst |
| Umbreon (Dark) | High friendship and level up at night | No catalyst |
| Sylveon (Fairy) | High friendship, Fairy move, level up | No catalyst |

The **nine custom catalysts other than Sky** cost **3,200 each** in the source alpha. Sky costs **3,000**. Original stone prices use the engine's item pricing.

## 5. Single-type form → any dual type: choose the second type

Once your single-type Eeveelution is **Lv. 38+** and you've earned **six Hoenn gym badges**:

1. Open the **Bag**.
2. Choose the **type-boosting item for the second type you want to add**.
3. Choose **Use**, then select your single-type Eeveelution. **Do not merely Give/hold** the item.
4. The Pokémon should evolve into the corresponding two-type species. For example, **Aerieon (Flying) + Silver Powder (Bug) → Aerartheon (Flying/Bug)**; or **Artheon (Bug) + Sharp Beak (Flying) → Aerartheon**.
5. The pair is **unordered**: Fire/Water and Water/Fire are the same species. Any original or custom single-type form can add any one of the **17 other types**.

**Important technical note:** All 306 evolution entries were present in Stage 10/11, but some type boosters were missing the actual item-effect flag. The **Stage 12** source patch adds that flag, checks all 306 entries and preserves normal held-item boosts. Use the latest Stage 15.1 alpha, which includes the Stage 12 repair, for gameplay testing.

| Type you want to ADD | Use this type item on a single-type Eeveelution | Earlier shop | Also at Lilycove 4F |
|---|---|---|---|
| Normal | Silk Scarf | Slateport Mart | Yes |
| Fighting | Black Belt | Fortree Mart | Yes |
| Flying | Sharp Beak | Fortree Mart | Yes |
| Poison | Poison Barb | Fortree Mart | Yes |
| Ground | Soft Sand | Lavaridge Mart | Yes |
| Rock | Hard Stone | Lavaridge Mart | Yes |
| Bug | Silver Powder | Fortree Mart | Yes |
| Ghost | Spell Tag | Fortree Mart | Yes |
| Steel | Metal Coat | Fortree Mart | Yes |
| Fire | Charcoal | Lavaridge Mart | Yes |
| Water | Mystic Water | Slateport Mart | Yes |
| Grass | Miracle Seed | Slateport Mart | Yes |
| Electric | Magnet | Mauville Mart | Yes |
| Psychic | Twisted Spoon | Mauville Mart | Yes |
| Ice | Never-Melt Ice | Lilycove 4F | Yes |
| Dragon | Dragon Fang | Lilycove 4F | Yes |
| Dark | Black Glasses | Fortree Mart | Yes |
| Fairy | Fairy Feather | Lilycove 4F | Yes |

All 18 type-boosting items retain their traditional **held-item type-power bonus**. Using one from the Bag for evolution is a separate action.

## 6. Shops by town (quick index)

| Shop | Added Eevee evolution items |
|---|---|
| **Oldale Mart**, after Poké Balls unlock | Sky Catalyst |
| **Rustboro Mart**, expanded stock | Fire Stone, Water Stone, Thunder Stone; Neutral, Swarm, Stone Catalysts |
| **Slateport Mart** | Silk Scarf, Mystic Water, Miracle Seed; Valor and Venom Catalysts |
| **Mauville Mart** | Leaf Stone, Ice Stone, Magnet, Twisted Spoon; Alloy and Earth Catalysts |
| **Lavaridge Mart** | Charcoal, Hard Stone, Soft Sand |
| **Fortree Mart** | Sharp Beak, Silver Powder, Spell Tag, Black Glasses, Poison Barb, Black Belt, Metal Coat; Spirit and Dragon Catalysts |
| **Lilycove Department Store 4F, right clerk** | All 18 type boosters listed above and nine custom single-type Catalysts (not Sky). |

Existing shop stock is retained and these are **added** items, not replacements. Some shop lists only appear after normal story progression or shop expansion.

## 7. Every Eeveelution's moves by level

**[Complete level-up move reference: Eevee + all 171 Eeveelutions](EEVEE_LEVEL_UP_MOVES.md)**

The linked guide lists exactly what each form's current compiled learnset provides, grouped by level, including **level 0 (on evolution)** and **level 1 (starting/relearner)** entries where present. The normal Eeveelutions use the engine's active Gen 9 learnsets, whereas the custom forms have separately defined experimental schedules. **TMs, tutors, eggs and other move-acquisition methods are not included.**

**Balance still needs work:** All **163 custom forms have just five or six level entries**, and **26** have a move repeated at multiple levels. These are current source facts, not necessarily final design choices. Individual in-emulator move-learning behavior has not been fully tested.

## 8. Alpha / saves / testing

- [Historical Stage 11 habitat build](https://github.com/Lamictal/Eevee/actions/runs/43276563803): its earlier type-boosters lacked the necessary item evolution effect; do not use Stage 11 as the current test build.
- **Stage 12 evolution repair:** included in the [latest Stage 15.1 full-roster build workflow](.github/workflows/eevee-full171-build.yml); use its latest successful artifact to test deliberate dual evolutions.
- **Emulator QA outstanding:** a successful GitHub build confirms compilation and static route checks. It does **not** prove every evolution or shop interaction succeeds in mGBA.
- **Use a fresh save for the 171-form alpha.** The full roster expands saved Pokédex flags; there's no validated migration from the early two-form alpha or separate Evergreen ROM.

**Source of truth:** the actual habitat script [stage11_full_ecology.py](stage11_full_ecology.py), the verified [source installer in the Stage 10 build bundle](.github/workflows/eevee-full171-build.yml), [type-item fix](stage12_verify_dual_items.py), and [Stage 9 item distribution](stage9_world_balance.py).
