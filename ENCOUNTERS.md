# Pokémon Eevee: complete wild encounter rates by area

<!-- generated-by-run=43522636352 -->

Source build: https://github.com/Lamictal/Eevee/actions/runs/43522636352

> **Automatically generated from the source of the successful Stage 15.1+ Monoamine ROM build.** These are expected encounter probabilities, **not** results from catching Pokémon in an emulator.

**What the percentages mean:** If you generate a wild encounter using the stated method, the percentage is the modeled probability of encountering that species. It is *not* the probability per walking step, the catch rate, or a guarantee.

**Included:** All map wild tables in the built source, grass/caves, Surf, Rock Smash, Old/Good/Super Rod, Stage 11 custom Eeveelution encounter slots, and the Stage 15 National Dex bonus pools with their actual replacement probabilities and minimum levels.

**Important limitations:** The source includes alternate and Kanto/FRLG map tables, some of which may not be reachable in this Emerald-based hack. Duplicate areas are listed as separate source variants, **not** merged. Static encounters, NPC trades, gift Pokémon and scripted events are not covered. Abilities, lures, fishing-chain effects, Feebas-specific tiles, repel, alternate time-of-day tables, and special events can change practical outcomes. The displayed rates are *baseline* type-selection rates without these modifiers.

**Coverage:** 240 distinct maps, 388 source area tables, 1023 supplementary land National Dex species; 1 aquatic-only species use native water/fishing tables.

## Jump to an area

<details><summary>Open area index</summary>

- [Route 101](#area-0)
- [Route 102](#area-1)
- [Route 103](#area-2)
- [Route 104](#area-3)
- [Route 105](#area-4)
- [Route 106](#area-5)
- [Route 107](#area-6)
- [Route 108](#area-7)
- [Route 109](#area-8)
- [Route 110](#area-9)
- [Route 111](#area-10)
- [Route 112](#area-11)
- [Route 113](#area-12)
- [Route 114](#area-13)
- [Route 115](#area-14)
- [Route 116](#area-15)
- [Route 117](#area-16)
- [Route 118](#area-17)
- [Route 119](#area-18)
- [Route 120](#area-19)
- [Route 121](#area-20)
- [Route 122](#area-21)
- [Route 123](#area-22)
- [Route 124](#area-23)
- [Route 125](#area-24)
- [Route 126](#area-25)
- [Route 127](#area-26)
- [Route 128](#area-27)
- [Route 129](#area-28)
- [Route 130](#area-29)
- [Route 131](#area-30)
- [Route 132](#area-31)
- [Route 133](#area-32)
- [Route 134](#area-33)
- [Artisan Cave 1F](#area-34)
- [Artisan Cave B1F](#area-35)
- [Desert Underpass](#area-36)
- [Ever Grande City](#area-37)
- [Fiery Path](#area-38)
- [Granite Cave 1F](#area-39)
- [Granite Cave B1F](#area-40)
- [Granite Cave B2F](#area-41)
- [Granite Cave Stevens Room](#area-42)
- [Jagged Pass](#area-43)
- [Meteor Falls 1F 1R](#area-44)
- [Meteor Falls 1F 2R](#area-45)
- [Meteor Falls B1F 1R](#area-46)
- [Meteor Falls B1F 2R](#area-47)
- [Meteor Falls Stevens Cave](#area-48)
- [Mirage Tower 1F](#area-49)
- [Mirage Tower 2F](#area-50)
- [Mirage Tower 3F](#area-51)
- [Mirage Tower 4F](#area-52)
- [Mossdeep City](#area-53)
- [Mt. Pyre 1F](#area-54)
- [Mt. Pyre 2F](#area-55)
- [Mt. Pyre 3F](#area-56)
- [Mt. Pyre 4F](#area-57)
- [Mt. Pyre 5F](#area-58)
- [Mt. Pyre 6F](#area-59)
- [Mt. Pyre Exterior](#area-60)
- [Mt. Pyre Summit](#area-61)
- [New Mauville Entrance](#area-62)
- [New Mauville Inside](#area-63)
- [Petalburg City](#area-64)
- [Petalburg Woods](#area-65)
- [Rusturf Tunnel](#area-66)
- [Safari Zone Center](#area-67)
- [Safari Zone East](#area-68)
- [Safari Zone North](#area-69)
- [Safari Zone Northeast](#area-70)
- [Safari Zone Northwest](#area-71)
- [Safari Zone North Frlg](#area-72)
- [Safari Zone South](#area-73)
- [Safari Zone Southeast](#area-74)
- [Safari Zone Southwest](#area-75)
- [Safari Zone West](#area-76)
- [Seafloor Cavern Entrance](#area-77)
- [Seafloor Cavern Room1](#area-78)
- [Seafloor Cavern Room2](#area-79)
- [Seafloor Cavern Room3](#area-80)
- [Seafloor Cavern Room4](#area-81)
- [Seafloor Cavern Room5](#area-82)
- [Seafloor Cavern Room6](#area-83)
- [Seafloor Cavern Room7](#area-84)
- [Seafloor Cavern Room8](#area-85)
- [Shoal Cave Low Tide Entrance Room](#area-86)
- [Shoal Cave Low Tide Ice Room](#area-87)
- [Shoal Cave Low Tide Inner Room](#area-88)
- [Shoal Cave Low Tide Lower Room](#area-89)
- [Shoal Cave Low Tide Stairs Room](#area-90)
- [Sky Pillar 1F](#area-91)
- [Sky Pillar 3F](#area-92)
- [Sky Pillar 5F](#area-93)
- [Victory Road 1F](#area-94)
- [Victory Road 1F Frlg](#area-95)
- [Victory Road 2F](#area-96)
- [Victory Road 3F](#area-97)
- [Victory Road B1F](#area-98)
- [Victory Road B2F](#area-99)
- [Abandoned Ship Hidden Floor Corridors](#area-100)
- [Abandoned Ship Rooms B1F](#area-101)
- [Altering Cave](#area-102)
- [Cave Of Origin 1F](#area-103)
- [Cave Of Origin Entrance](#area-104)
- [Cave Of Origin Unused Ruby Sapphire Map1](#area-105)
- [Cave Of Origin Unused Ruby Sapphire Map2](#area-106)
- [Cave Of Origin Unused Ruby Sapphire Map3](#area-107)
- [Celadon City](#area-108)
- [Cerulean Cave 1F](#area-109)
- [Cerulean Cave 2F](#area-110)
- [Cerulean Cave B1F](#area-111)
- [Cerulean City](#area-112)
- [Cinnabar Island](#area-113)
- [Dewford Town](#area-114)
- [Digletts Cave B1F](#area-115)
- [Five Island](#area-116)
- [Five Island Lost Cave Room1](#area-117)
- [Five Island Lost Cave Room10](#area-118)
- [Five Island Lost Cave Room11](#area-119)
- [Five Island Lost Cave Room12](#area-120)
- [Five Island Lost Cave Room13](#area-121)
- [Five Island Lost Cave Room14](#area-122)
- [Five Island Lost Cave Room2](#area-123)
- [Five Island Lost Cave Room3](#area-124)
- [Five Island Lost Cave Room4](#area-125)
- [Five Island Lost Cave Room5](#area-126)
- [Five Island Lost Cave Room6](#area-127)
- [Five Island Lost Cave Room7](#area-128)
- [Five Island Lost Cave Room8](#area-129)
- [Five Island Lost Cave Room9](#area-130)
- [Five Island Meadow](#area-131)
- [Five Island Memorial Pillar](#area-132)
- [Five Island Resort Gorgeous](#area-133)
- [Five Island Water Labyrinth](#area-134)
- [Four Island](#area-135)
- [Four Island Icefall Cave 1F](#area-136)
- [Four Island Icefall Cave B1F](#area-137)
- [Four Island Icefall Cave Back](#area-138)
- [Four Island Icefall Cave Entrance](#area-139)
- [Fuchsia City](#area-140)
- [Lilycove City](#area-141)
- [Magma Hideout 1F](#area-142)
- [Magma Hideout 2F 1R](#area-143)
- [Magma Hideout 2F 2R](#area-144)
- [Magma Hideout 2F 3R](#area-145)
- [Magma Hideout 3F 1R](#area-146)
- [Magma Hideout 3F 2R](#area-147)
- [Magma Hideout 3F 3R](#area-148)
- [Magma Hideout 4F](#area-149)
- [Mt. Ember Exterior](#area-150)
- [Mt. Ember Ruby Path 1F](#area-151)
- [Mt. Ember Ruby Path B1F](#area-152)
- [Mt. Ember Ruby Path B1F Stairs](#area-153)
- [Mt. Ember Ruby Path B2F](#area-154)
- [Mt. Ember Ruby Path B2F Stairs](#area-155)
- [Mt. Ember Ruby Path B3F](#area-156)
- [Mt. Ember Summit Path 1F](#area-157)
- [Mt. Ember Summit Path 2F](#area-158)
- [Mt. Ember Summit Path 3F](#area-159)
- [Mt. Moon 1F](#area-160)
- [Mt. Moon B1F](#area-161)
- [Mt. Moon B2F](#area-162)
- [One Island](#area-163)
- [One Island Kindle Road](#area-164)
- [One Island Treasure Beach](#area-165)
- [Pacifidlog Town](#area-166)
- [Pallet Town](#area-167)
- [Pokemon Mansion 1F](#area-168)
- [Pokemon Mansion 2F](#area-169)
- [Pokemon Mansion 3F](#area-170)
- [Pokemon Mansion B1F](#area-171)
- [Pokemon Tower 3F](#area-172)
- [Pokemon Tower 4F](#area-173)
- [Pokemon Tower 5F](#area-174)
- [Pokemon Tower 6F](#area-175)
- [Pokemon Tower 7F](#area-176)
- [Power Plant](#area-177)
- [Rock Tunnel 1F](#area-178)
- [Rock Tunnel B1F](#area-179)
- [Route 1](#area-180)
- [Route 10](#area-181)
- [Route 11](#area-182)
- [Route 12](#area-183)
- [Route 13](#area-184)
- [Route 14](#area-185)
- [Route 15](#area-186)
- [Route 16](#area-187)
- [Route 17](#area-188)
- [Route 18](#area-189)
- [Route 19](#area-190)
- [Route 2](#area-191)
- [Route 20](#area-192)
- [Route 21 North](#area-193)
- [Route 21 South](#area-194)
- [Route 22](#area-195)
- [Route 23](#area-196)
- [Route 24](#area-197)
- [Route 25](#area-198)
- [Route 3](#area-199)
- [Route 4](#area-200)
- [Route 5](#area-201)
- [Route 6](#area-202)
- [Route 7](#area-203)
- [Route 8](#area-204)
- [Route 9](#area-205)
- [Seafoam Islands 1F](#area-206)
- [Seafoam Islands B1F](#area-207)
- [Seafoam Islands B2F](#area-208)
- [Seafoam Islands B3F](#area-209)
- [Seafoam Islands B4F](#area-210)
- [Seven Island Sevault Canyon](#area-211)
- [Seven Island Sevault Canyon Entrance](#area-212)
- [Seven Island Tanoby Ruins](#area-213)
- [Seven Island Tanoby Ruins Dilford Chamber](#area-214)
- [Seven Island Tanoby Ruins Liptoo Chamber](#area-215)
- [Seven Island Tanoby Ruins Monean Chamber](#area-216)
- [Seven Island Tanoby Ruins Rixy Chamber](#area-217)
- [Seven Island Tanoby Ruins Scufib Chamber](#area-218)
- [Seven Island Tanoby Ruins Viapois Chamber](#area-219)
- [Seven Island Tanoby Ruins Weepth Chamber](#area-220)
- [Seven Island Trainer Tower](#area-221)
- [Six Island Altering Cave](#area-222)
- [Six Island Green Path](#area-223)
- [Six Island Outcast Island](#area-224)
- [Six Island Pattern Bush](#area-225)
- [Six Island Ruin Valley](#area-226)
- [Six Island Water Path](#area-227)
- [Slateport City](#area-228)
- [Sootopolis City](#area-229)
- [Ssanne Exterior](#area-230)
- [Three Island Berry Forest](#area-231)
- [Three Island Bond Bridge](#area-232)
- [Three Island Port](#area-233)
- [Two Island Cape Brink](#area-234)
- [Underwater Route124](#area-235)
- [Underwater Route126](#area-236)
- [Vermilion City](#area-237)
- [Viridian City](#area-238)
- [Viridian Forest](#area-239)

</details>

## All areas

<a id="area-0"></a>
## Route 101

Source map: MAP_ROUTE101.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wurmple | 45.00% | 2–3 | Native / custom slot |
| Poochyena | 40.00% | 2–3 | Native / custom slot |
| Zigzagoon | 10.00% | 2–3 | Native / custom slot |
| Eevee | 5.00% | 3–4 | Native / custom slot |

---

<a id="area-1"></a>
## Route 102

Source map: MAP_ROUTE102.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wurmple | 30.00% | 3–4 | Native / custom slot |
| Lotad | 20.00% | 3–4 | Native / custom slot |
| Poochyena | 20.00% | 3 | Native / custom slot |
| Zigzagoon | 15.00% | 3–4 | Native / custom slot |
| Eevee | 10.00% | 4–5 | Native / custom slot |
| Ralts | 4.00% | 4 | Native / custom slot |
| Seedot | 1.00% | 3 | Native / custom slot |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Marill | 99.00% | 5–35 | Native / custom slot |
| Goldeen | 1.00% | 20–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Corphish | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Corphish | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-2"></a>
## Route 103

Source map: MAP_ROUTE103.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poochyena | 57.60% | 2–4 | Native / custom slot |
| Wingull | 19.20% | 2–4 | Native / custom slot |
| Zigzagoon | 19.20% | 3–4 | Native / custom slot |
| Chinchou | 0.286% | 2–4 | National Dex bonus |
| Clauncher | 0.286% | 2–4 | National Dex bonus |
| Dewpider | 0.286% | 2–4 | National Dex bonus |
| Finizen | 0.286% | 2–4 | National Dex bonus |
| Happiny | 0.286% | 2–4 | National Dex bonus |
| Lotad | 0.286% | 2–4 | National Dex bonus |
| Mantyke | 0.286% | 2–4 | National Dex bonus |
| Meowth | 0.286% | 2–4 | National Dex bonus |
| Shroodle | 0.286% | 2–4 | National Dex bonus |
| Spinda | 0.286% | 2–4 | National Dex bonus |
| Swablu | 0.286% | 2–4 | National Dex bonus |
| Tirtouga | 0.286% | 2–4 | National Dex bonus |
| Wooloo | 0.286% | 2–4 | National Dex bonus |
| Wooper | 0.286% | 2–4 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-3"></a>
## Route 104

Source map: MAP_ROUTE104.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poochyena | 38.40% | 4–5 | Native / custom slot |
| Marill | 19.20% | 4–5 | Native / custom slot |
| Wurmple | 19.20% | 4 | Native / custom slot |
| Wingull | 9.60% | 3–5 | Native / custom slot |
| Eevee | 4.80% | 5–7 | Native / custom slot |
| Taillow | 4.80% | 4 | Native / custom slot |
| Combee | 0.267% | 3–7 | National Dex bonus |
| Cottonee | 0.267% | 3–7 | National Dex bonus |
| Croagunk | 0.267% | 3–7 | National Dex bonus |
| Ducklett | 0.267% | 3–7 | National Dex bonus |
| Feebas | 0.267% | 3–7 | National Dex bonus |
| Gossifleur | 0.267% | 3–7 | National Dex bonus |
| Krabby | 0.267% | 3–7 | National Dex bonus |
| Morelull | 0.267% | 3–7 | National Dex bonus |
| Nymble | 0.267% | 3–7 | National Dex bonus |
| Poliwag | 0.267% | 3–7 | National Dex bonus |
| Remoraid | 0.267% | 3–7 | National Dex bonus |
| Seedot | 0.267% | 3–7 | National Dex bonus |
| Spinarak | 0.267% | 3–7 | National Dex bonus |
| Swirlix | 0.267% | 3–7 | National Dex bonus |
| Tinkatink | 0.267% | 3–7 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wingull | 95.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-4"></a>
## Route 105

Source map: MAP_ROUTE105.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-5"></a>
## Route 106

Source map: MAP_ROUTE106.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-6"></a>
## Route 107

Source map: MAP_ROUTE107.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-7"></a>
## Route 108

Source map: MAP_ROUTE108.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-8"></a>
## Route 109

Source map: MAP_ROUTE109.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-9"></a>
## Route 110

Source map: MAP_ROUTE110.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Electrike | 29.07% | 12–14 | National Dex bonus, Native / custom slot |
| Poochyena | 19.20% | 12 | Native / custom slot |
| Gulpin | 14.40% | 12–13 | Native / custom slot |
| Minun | 14.40% | 13 | Native / custom slot |
| Oddish | 9.60% | 13 | Native / custom slot |
| Wingull | 7.68% | 12 | Native / custom slot |
| Jolteon | 0.960% | 13–14 | Native / custom slot |
| Plusle | 0.960% | 13 | Native / custom slot |
| Bidoof | 0.267% | 12–14 | National Dex bonus |
| Blitzle | 0.267% | 12–14 | National Dex bonus |
| Elekid | 0.267% | 12–14 | National Dex bonus |
| Hoothoot | 0.267% | 12–14 | National Dex bonus |
| Mareanie | 0.267% | 12–14 | National Dex bonus |
| Pawmi | 0.267% | 12–14 | National Dex bonus |
| Pichu | 0.267% | 12–14 | National Dex bonus |
| Salandit | 0.267% | 12–14 | National Dex bonus |
| Skrelp | 0.267% | 12–14 | National Dex bonus |
| Stunky | 0.267% | 12–14 | National Dex bonus |
| Tynamo | 0.267% | 12–14 | National Dex bonus |
| Voltorb | 0.267% | 12–14 | National Dex bonus |
| Wattrel | 0.267% | 12–14 | National Dex bonus |
| Yamper | 0.267% | 12–14 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-10"></a>
## Route 111

Source map: MAP_ROUTE111.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sandshrew | 32.20% | 19–21 | Native / custom slot |
| Trapinch | 32.20% | 19–21 | Native / custom slot |
| Baltoy | 22.08% | 19–21 | Native / custom slot |
| Cacnea | 5.52% | 20–22 | Native / custom slot |
| Archen | 0.533% | 19–22 | National Dex bonus |
| Bastiodon | 0.533% | 19–22 | National Dex bonus |
| Braixen | 0.533% | 19–22 | National Dex bonus |
| Ceruledge | 0.533% | 19–22 | National Dex bonus |
| Dubwool | 0.533% | 19–22 | National Dex bonus |
| Eiscue | 0.533% | 19–22 | National Dex bonus |
| Gligar | 0.533% | 19–22 | National Dex bonus |
| Klefki | 0.533% | 19–22 | National Dex bonus |
| Litleo | 0.533% | 19–22 | National Dex bonus |
| Nidoran M | 0.533% | 19–22 | National Dex bonus |
| Noctowl | 0.533% | 19–22 | National Dex bonus |
| Probopass | 0.533% | 19–22 | National Dex bonus |
| Rapidash | 0.533% | 19–22 | National Dex bonus |
| Torkoal | 0.533% | 19–22 | National Dex bonus |
| Vigoroth | 0.533% | 19–22 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Marill | 99.00% | 5–35 | Native / custom slot |
| Goldeen | 1.00% | 20–30 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 100.00% | 5–20 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Barboach | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Barboach | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-11"></a>
## Route 112

Source map: MAP_ROUTE112.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Numel | 69.00% | 14–16 | Native / custom slot |
| Marill | 23.00% | 14–16 | Native / custom slot |
| Charcadet | 0.533% | 14–16 | National Dex bonus |
| Cramorant | 0.533% | 14–16 | National Dex bonus |
| Crocalor | 0.533% | 18 | National Dex bonus |
| Delcatty | 0.533% | 18 | National Dex bonus |
| Dunsparce | 0.533% | 14–16 | National Dex bonus |
| Flabébé | 0.533% | 14–16 | National Dex bonus |
| Growlithe | 0.533% | 14–16 | National Dex bonus |
| Heatmor | 0.533% | 14–16 | National Dex bonus |
| Monferno | 0.533% | 18 | National Dex bonus |
| Nidorino | 0.533% | 18 | National Dex bonus |
| Oranguru | 0.533% | 14–16 | National Dex bonus |
| Patrat | 0.533% | 14–16 | National Dex bonus |
| Quilava | 0.533% | 18 | National Dex bonus |
| Shellos | 0.533% | 14–16 | National Dex bonus |
| Simisear | 0.533% | 18 | National Dex bonus |

---

<a id="area-12"></a>
## Route 113

Source map: MAP_ROUTE113.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Spinda | 64.40% | 14–16 | Native / custom slot |
| Slugma | 18.90% | 14–17 | National Dex bonus, Native / custom slot |
| Skarmory | 4.60% | 16 | Native / custom slot |
| Vireon | 4.60% | 15–17 | Native / custom slot |
| Ambipom | 0.500% | 18 | National Dex bonus |
| Camerupt | 0.500% | 18 | National Dex bonus |
| Clodsire | 0.500% | 14–17 | National Dex bonus |
| Darumaka | 0.500% | 14–17 | National Dex bonus |
| Diggersby | 0.500% | 18 | National Dex bonus |
| Drampa | 0.500% | 14–17 | National Dex bonus |
| Furret | 0.500% | 18 | National Dex bonus |
| Linoone | 0.500% | 18 | National Dex bonus |
| Pignite | 0.500% | 18 | National Dex bonus |
| Ponyta | 0.500% | 14–17 | National Dex bonus |
| Salazzle | 0.500% | 18 | National Dex bonus |
| Scatterbug | 0.500% | 14–17 | National Dex bonus |
| Sinistcha | 0.500% | 14–17 | National Dex bonus |
| Sinistea | 0.500% | 14–17 | National Dex bonus |
| Spearow | 0.500% | 14–17 | National Dex bonus |

---

<a id="area-13"></a>
## Route 114

Source map: MAP_ROUTE114.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Swablu | 36.80% | 15–17 | Native / custom slot |
| Lotad | 27.60% | 15–16 | Native / custom slot |
| Lombre | 13.80% | 16 | Native / custom slot |
| Seviper | 8.28% | 15–17 | Native / custom slot |
| Champeon | 4.60% | 17–19 | Native / custom slot |
| Nuzleaf | 0.920% | 15 | Native / custom slot |
| Copperajah | 0.533% | 18–19 | National Dex bonus |
| Dottler | 0.533% | 18–19 | National Dex bonus |
| Exeggutor | 0.533% | 18–19 | National Dex bonus |
| Herdier | 0.533% | 18–19 | National Dex bonus |
| Kakuna | 0.533% | 18–19 | National Dex bonus |
| Karrablast | 0.533% | 15–19 | National Dex bonus |
| Metang | 0.533% | 18–19 | National Dex bonus |
| Miltank | 0.533% | 15–19 | National Dex bonus |
| Persian | 0.533% | 18–19 | National Dex bonus |
| Purugly | 0.533% | 18–19 | National Dex bonus |
| Smoliv | 0.533% | 15–19 | National Dex bonus |
| Snubbull | 0.533% | 15–19 | National Dex bonus |
| Spewpa | 0.533% | 15–19 | National Dex bonus |
| Trapinch | 0.533% | 15–19 | National Dex bonus |
| Wishiwashi | 0.533% | 15–19 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Marill | 99.00% | 5–35 | Native / custom slot |
| Goldeen | 1.00% | 20–30 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 100.00% | 5–20 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Barboach | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Barboach | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-14"></a>
## Route 115

Source map: MAP_ROUTE115.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Taillow | 36.80% | 23–25 | Native / custom slot |
| Swablu | 27.60% | 23–25 | Native / custom slot |
| Swellow | 9.73% | 23–26 | National Dex bonus, Native / custom slot |
| Jigglypuff | 9.20% | 24–25 | Native / custom slot |
| Wingull | 9.20% | 24–26 | Native / custom slot |
| Audino | 0.533% | 23–26 | National Dex bonus |
| Basculegion | 0.533% | 23–26 | National Dex bonus |
| Chansey | 0.533% | 23–26 | National Dex bonus |
| Farfetch'd | 0.533% | 23–26 | National Dex bonus |
| Farigiraf | 0.533% | 23–26 | National Dex bonus |
| Fearow | 0.533% | 23–26 | National Dex bonus |
| Gastrodon | 0.533% | 23–26 | National Dex bonus |
| Gourgeist | 0.533% | 23–26 | National Dex bonus |
| Kecleon | 0.533% | 23–26 | National Dex bonus |
| Mimikyu | 0.533% | 23–26 | National Dex bonus |
| Sawsbuck | 0.533% | 23–26 | National Dex bonus |
| Toxapex | 0.533% | 23–26 | National Dex bonus |
| Ursaring | 0.533% | 23–26 | National Dex bonus |
| Watchog | 0.533% | 23–26 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-15"></a>
## Route 116

Source map: MAP_ROUTE116.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poochyena | 26.88% | 6–8 | Native / custom slot |
| Taillow | 19.51% | 6–8 | National Dex bonus, Native / custom slot |
| Nincada | 19.20% | 6–7 | Native / custom slot |
| Whismur | 19.20% | 6 | Native / custom slot |
| Abra | 9.60% | 7 | Native / custom slot |
| Skitty | 1.92% | 7–8 | Native / custom slot |
| Buneary | 0.308% | 6–8 | National Dex bonus |
| Ditto | 0.308% | 6–8 | National Dex bonus |
| Glameow | 0.308% | 6–8 | National Dex bonus |
| Gulpin | 0.308% | 6–8 | National Dex bonus |
| Minccino | 0.308% | 6–8 | National Dex bonus |
| Rufflet | 0.308% | 6–8 | National Dex bonus |
| Stufful | 0.308% | 6–8 | National Dex bonus |
| Tandemaus | 0.308% | 6–8 | National Dex bonus |
| Togepi | 0.308% | 6–8 | National Dex bonus |
| Trubbish | 0.308% | 6–8 | National Dex bonus |
| Yungoos | 0.308% | 6–8 | National Dex bonus |
| Zigzagoon | 0.308% | 6–8 | National Dex bonus |

---

<a id="area-16"></a>
## Route 117

Source map: MAP_ROUTE117.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 36.80% | 13–14 | Native / custom slot |
| Poochyena | 27.60% | 13–14 | Native / custom slot |
| Illumise | 11.96% | 13–14 | Native / custom slot |
| Marill | 9.20% | 13 | Native / custom slot |
| Eevee | 4.60% | 12–16 | Native / custom slot |
| Seedot | 0.920% | 13 | Native / custom slot |
| Volbeat | 0.920% | 13 | Native / custom slot |
| Bibarel | 0.533% | 18 | National Dex bonus |
| Blipbug | 0.533% | 12–16 | National Dex bonus |
| Flapple | 0.533% | 18 | National Dex bonus |
| Foongus | 0.533% | 12–16 | National Dex bonus |
| Gloom | 0.533% | 18 | National Dex bonus |
| Grubbin | 0.533% | 12–16 | National Dex bonus |
| Ivysaur | 0.533% | 18 | National Dex bonus |
| Koffing | 0.533% | 12–16 | National Dex bonus |
| Meowstic | 0.533% | 12–16 | National Dex bonus |
| Silcoon | 0.533% | 18 | National Dex bonus |
| Surskit | 0.533% | 12–16 | National Dex bonus |
| Tadbulb | 0.533% | 12–16 | National Dex bonus |
| Togetic | 0.533% | 18 | National Dex bonus |
| Whimsicott | 0.533% | 18 | National Dex bonus |
| Yanmega | 0.533% | 18 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Marill | 99.00% | 5–35 | Native / custom slot |
| Goldeen | 1.00% | 20–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Corphish | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Corphish | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-17"></a>
## Route 118

Source map: MAP_ROUTE118.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Electrike | 27.60% | 24–26 | Native / custom slot |
| Zigzagoon | 27.60% | 24–26 | Native / custom slot |
| Manectric | 9.73% | 24–27 | National Dex bonus, Native / custom slot |
| Linoone | 9.20% | 26 | Native / custom slot |
| Wingull | 9.20% | 25–27 | Native / custom slot |
| Vaporeon | 4.60% | 25–27 | Native / custom slot |
| Neuteon | 3.68% | 25–27 | Native / custom slot |
| Kecleon | 0.920% | 25 | Native / custom slot |
| Basculin | 0.533% | 24–27 | National Dex bonus |
| Bellibolt | 0.533% | 24–27 | National Dex bonus |
| Braviary | 0.533% | 24–27 | National Dex bonus |
| Froakie | 0.533% | 24–27 | National Dex bonus |
| Mothim | 0.533% | 24–27 | National Dex bonus |
| Mudkip | 0.533% | 24–27 | National Dex bonus |
| Muk | 0.533% | 24–27 | National Dex bonus |
| Oshawott | 0.533% | 24–27 | National Dex bonus |
| Popplio | 0.533% | 24–27 | National Dex bonus |
| Quaxly | 0.533% | 24–27 | National Dex bonus |
| Sobble | 0.533% | 24–27 | National Dex bonus |
| Squirtle | 0.533% | 24–27 | National Dex bonus |
| Staryu | 0.533% | 24–27 | National Dex bonus |
| Totodile | 0.533% | 24–27 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Carvanha | 20.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Carvanha | 60.00% | 20–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-18"></a>
## Route 119

Source map: MAP_ROUTE119.

### Grass / cave (base encounter-frequency setting: 15)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Linoone | 27.60% | 25–27 | Native / custom slot |
| Zigzagoon | 27.60% | 25–27 | Native / custom slot |
| Oddish | 23.00% | 25–27 | Native / custom slot |
| Aerieon | 4.60% | 24–27 | Native / custom slot |
| Tropius | 4.60% | 25–27 | Native / custom slot |
| Artheon | 3.68% | 24–27 | Native / custom slot |
| Kecleon | 0.920% | 25 | Native / custom slot |
| Cacturne | 0.533% | 24–27 | National Dex bonus |
| Capsakid | 0.533% | 24–27 | National Dex bonus |
| Caterpie | 0.533% | 24–27 | National Dex bonus |
| Chespin | 0.533% | 24–27 | National Dex bonus |
| Chikorita | 0.533% | 24–27 | National Dex bonus |
| Eldegoss | 0.533% | 24–27 | National Dex bonus |
| Parasect | 0.533% | 24–27 | National Dex bonus |
| Pinsir | 0.533% | 24–27 | National Dex bonus |
| Rowlet | 0.533% | 24–27 | National Dex bonus |
| Shuckle | 0.533% | 24–27 | National Dex bonus |
| Snivy | 0.533% | 24–27 | National Dex bonus |
| Swanna | 0.533% | 24–27 | National Dex bonus |
| Sylveon | 0.533% | 24–27 | National Dex bonus |
| Turtwig | 0.533% | 24–27 | National Dex bonus |
| Venipede | 0.533% | 24–27 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Carvanha | 20.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Carvanha | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-19"></a>
## Route 120

Source map: MAP_ROUTE120.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Mightyena | 27.60% | 25–27 | Native / custom slot |
| Oddish | 23.00% | 25–27 | Native / custom slot |
| Poochyena | 18.40% | 25 | Native / custom slot |
| Marill | 9.20% | 25 | Native / custom slot |
| Leafeon | 5.13% | 25–28 | National Dex bonus, Native / custom slot |
| Absol | 3.68% | 25 | Native / custom slot |
| Espeon | 3.68% | 25–28 | Native / custom slot |
| Kecleon | 0.920% | 25 | Native / custom slot |
| Seedot | 0.920% | 25 | Native / custom slot |
| Aromatisse | 0.533% | 25–28 | National Dex bonus |
| Bellsprout | 0.533% | 25–28 | National Dex bonus |
| Clefairy | 0.533% | 25–28 | National Dex bonus |
| Dwebble | 0.533% | 25–28 | National Dex bonus |
| Fomantis | 0.533% | 25–28 | National Dex bonus |
| Lokix | 0.533% | 25–28 | National Dex bonus |
| Milcery | 0.533% | 25–28 | National Dex bonus |
| Pineco | 0.533% | 25–28 | National Dex bonus |
| Scizor | 0.533% | 25–28 | National Dex bonus |
| Shedinja | 0.533% | 25–28 | National Dex bonus |
| Shiinotic | 0.533% | 25–28 | National Dex bonus |
| Simisage | 0.533% | 25–28 | National Dex bonus |
| Staravia | 0.533% | 25–28 | National Dex bonus |
| Tauros | 0.533% | 25–28 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Marill | 99.00% | 5–35 | Native / custom slot |
| Goldeen | 1.00% | 20–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Barboach | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Barboach | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-20"></a>
## Route 121

Source map: MAP_ROUTE121.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuppet | 27.60% | 26–28 | Native / custom slot |
| Mightyena | 18.40% | 26–28 | Native / custom slot |
| Poochyena | 18.40% | 26 | Native / custom slot |
| Oddish | 13.80% | 26–28 | Native / custom slot |
| Wingull | 8.28% | 26–28 | Native / custom slot |
| Sylveon | 4.60% | 26–29 | Native / custom slot |
| Kecleon | 0.920% | 25 | Native / custom slot |
| Dolliv | 0.533% | 25–29 | National Dex bonus |
| Durant | 0.533% | 25–29 | National Dex bonus |
| Ferrothorn | 0.533% | 25–29 | National Dex bonus |
| Granbull | 0.533% | 25–29 | National Dex bonus |
| Lycanroc | 0.533% | 25–29 | National Dex bonus |
| Nuzleaf | 0.533% | 25–29 | National Dex bonus |
| Pidgey | 0.533% | 25–29 | National Dex bonus |
| Swalot | 0.533% | 25–29 | National Dex bonus |
| Thwackey | 0.533% | 25–29 | National Dex bonus |
| Toxicroak | 0.533% | 25–29 | National Dex bonus |
| Toxtricity | 0.533% | 25–29 | National Dex bonus |
| Tranquill | 0.533% | 25–29 | National Dex bonus |
| Tropius | 0.533% | 25–29 | National Dex bonus |
| Venomoth | 0.533% | 25–29 | National Dex bonus |
| Weezing | 0.533% | 25–29 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-21"></a>
## Route 122

Source map: MAP_ROUTE122.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-22"></a>
## Route 123

Source map: MAP_ROUTE123.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuppet | 27.00% | 26–28 | Native / custom slot |
| Mightyena | 18.00% | 26–28 | Native / custom slot |
| Poochyena | 18.00% | 26 | Native / custom slot |
| Oddish | 13.50% | 26–28 | Native / custom slot |
| Leafeon | 4.50% | 25–28 | Native / custom slot |
| Wingull | 4.50% | 26–28 | Native / custom slot |
| Sylveon | 3.60% | 25–28 | Native / custom slot |
| Kecleon | 0.900% | 25 | Native / custom slot |
| Accelgor | 0.625% | 25–28 | National Dex bonus |
| Alcremie | 0.625% | 25–28 | National Dex bonus |
| Ariados | 0.625% | 25–28 | National Dex bonus |
| Brambleghast | 0.625% | 25–28 | National Dex bonus |
| Crustle | 0.625% | 25–28 | National Dex bonus |
| Grovyle | 0.625% | 25–28 | National Dex bonus |
| Jigglypuff | 0.625% | 25–28 | National Dex bonus |
| Nincada | 0.625% | 25–28 | National Dex bonus |
| Prinplup | 0.625% | 25–28 | National Dex bonus |
| Ribombee | 0.625% | 25–28 | National Dex bonus |
| Rillaboom | 0.625% | 34 | National Dex bonus |
| Scream Tail | 0.625% | 25–28 | National Dex bonus |
| Servine | 0.625% | 25–28 | National Dex bonus |
| Tangela | 0.625% | 25–28 | National Dex bonus |
| Venusaur | 0.625% | 34 | National Dex bonus |
| Vespiquen | 0.625% | 25–28 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-23"></a>
## Route 124

Source map: MAP_ROUTE124.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-24"></a>
## Route 125

Source map: MAP_ROUTE125.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-25"></a>
## Route 126

Source map: MAP_ROUTE126.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-26"></a>
## Route 127

Source map: MAP_ROUTE127.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-27"></a>
## Route 128

Source map: MAP_ROUTE128.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Luvdisc | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 45.00% | 30–45 | Native / custom slot |
| Luvdisc | 40.00% | 30–35 | Native / custom slot |
| Corsola | 15.00% | 30–35 | Native / custom slot |

---

<a id="area-28"></a>
## Route 129

Source map: MAP_ROUTE129.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 4.00% | 25–30 | Native / custom slot |
| Wailord | 1.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-29"></a>
## Route 130

Source map: MAP_ROUTE130.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wynaut | 90.00% | 5–50 | Native / custom slot |
| Bewear | 0.667% | 18–50 | National Dex bonus |
| Bouffalant | 0.667% | 5–50 | National Dex bonus |
| Chatot | 0.667% | 5–50 | National Dex bonus |
| Komala | 0.667% | 5–50 | National Dex bonus |
| Pelipper | 0.667% | 18–50 | National Dex bonus |
| Pumpkaboo | 0.667% | 5–50 | National Dex bonus |
| Qwilfish | 0.667% | 5–50 | National Dex bonus |
| Rattata | 0.667% | 5–50 | National Dex bonus |
| Relicanth | 0.667% | 5–50 | National Dex bonus |
| Samurott | 0.667% | 34–50 | National Dex bonus |
| Seaking | 0.667% | 18–50 | National Dex bonus |
| Seel | 0.667% | 5–50 | National Dex bonus |
| Tatsugiri | 0.667% | 5–50 | National Dex bonus |
| Wyrdeer | 0.667% | 18–50 | National Dex bonus |
| Zangoose | 0.667% | 5–50 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-30"></a>
## Route 131

Source map: MAP_ROUTE131.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-31"></a>
## Route 132

Source map: MAP_ROUTE132.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 45.00% | 30–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |
| Horsea | 15.00% | 25–30 | Native / custom slot |

---

<a id="area-32"></a>
## Route 133

Source map: MAP_ROUTE133.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 45.00% | 30–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |
| Horsea | 15.00% | 25–30 | Native / custom slot |

---

<a id="area-33"></a>
## Route 134

Source map: MAP_ROUTE134.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 45.00% | 30–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |
| Horsea | 15.00% | 25–30 | Native / custom slot |

---

<a id="area-34"></a>
## Artisan Cave 1F

Source map: MAP_ARTISAN_CAVE_1F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Smeargle | 100.00% | 40–50 | Native / custom slot |

---

<a id="area-35"></a>
## Artisan Cave B1F

Source map: MAP_ARTISAN_CAVE_B1F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Smeargle | 100.00% | 40–50 | Native / custom slot |

---

<a id="area-36"></a>
## Desert Underpass

Source map: MAP_DESERT_UNDERPASS.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Ditto | 44.55% | 38–45 | Native / custom slot |
| Whismur | 30.29% | 35–38 | Native / custom slot |
| Loudred | 14.26% | 38–44 | Native / custom slot |
| Aerodactyl | 0.619% | 35–45 | National Dex bonus |
| Aggron | 0.619% | 35–45 | National Dex bonus |
| Aurorus | 0.619% | 35–45 | National Dex bonus |
| Carkol | 0.619% | 35–45 | National Dex bonus |
| Duraludon | 0.619% | 35–45 | National Dex bonus |
| Garganacl | 0.619% | 35–45 | National Dex bonus |
| Gholdengo | 0.619% | 35–45 | National Dex bonus |
| Gigalith | 0.619% | 35–45 | National Dex bonus |
| Gliscor | 0.619% | 35–45 | National Dex bonus |
| Hariyama | 0.619% | 35–45 | National Dex bonus |
| Hitmonlee | 0.619% | 35–45 | National Dex bonus |
| Metagross | 0.619% | 35–45 | National Dex bonus |
| Mienshao | 0.619% | 35–45 | National Dex bonus |
| Rolycoly | 0.619% | 35–45 | National Dex bonus |
| Sandslash | 0.619% | 35–45 | National Dex bonus |
| Steelix | 0.619% | 35–45 | National Dex bonus |
| Celebi | 0.111% | 45 | Rare bonus pool |
| Chi Yu | 0.111% | 45 | Rare bonus pool |
| Dialga | 0.111% | 45 | Rare bonus pool |
| Latias | 0.111% | 45 | Rare bonus pool |
| Miraidon | 0.111% | 45 | Rare bonus pool |
| Necrozma | 0.111% | 45 | Rare bonus pool |
| Tapu Fini | 0.111% | 45 | Rare bonus pool |
| Terrakion | 0.111% | 45 | Rare bonus pool |
| Zacian | 0.111% | 45 | Rare bonus pool |

---

<a id="area-37"></a>
## Ever Grande City

Source map: MAP_EVER_GRANDE_CITY.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Luvdisc | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 45.00% | 30–45 | Native / custom slot |
| Luvdisc | 40.00% | 30–35 | Native / custom slot |
| Corsola | 15.00% | 30–35 | Native / custom slot |

---

<a id="area-38"></a>
## Fiery Path

Source map: MAP_FIERY_PATH.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Numel | 28.13% | 14–18 | National Dex bonus, Native / custom slot |
| Koffing | 23.00% | 15–16 | Native / custom slot |
| Torkoal | 12.88% | 14–15 | Native / custom slot |
| Machop | 9.20% | 15 | Native / custom slot |
| Slugma | 9.20% | 15 | Native / custom slot |
| Flareon | 4.60% | 16–18 | Native / custom slot |
| Duneon | 3.68% | 16–18 | Native / custom slot |
| Grimer | 1.84% | 14 | Native / custom slot |
| Charmander | 0.533% | 14–18 | National Dex bonus |
| Crabominable | 0.533% | 18 | National Dex bonus |
| Fletchinder | 0.533% | 18 | National Dex bonus |
| Fuecoco | 0.533% | 14–18 | National Dex bonus |
| Krokorok | 0.533% | 18 | National Dex bonus |
| Marowak | 0.533% | 18 | National Dex bonus |
| Rampardos | 0.533% | 18 | National Dex bonus |
| Revavroom | 0.533% | 18 | National Dex bonus |
| Scorbunny | 0.533% | 14–18 | National Dex bonus |
| Skarmory | 0.533% | 14–18 | National Dex bonus |
| Stunfisk | 0.533% | 14–18 | National Dex bonus |
| Sudowoodo | 0.533% | 18 | National Dex bonus |
| Tepig | 0.533% | 14–18 | National Dex bonus |
| Torchic | 0.533% | 14–18 | National Dex bonus |

---

<a id="area-39"></a>
## Granite Cave 1F

Source map: MAP_GRANITE_CAVE_1F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Makuhita | 48.00% | 6–10 | Native / custom slot |
| Zubat | 28.80% | 7–8 | Native / custom slot |
| Geodude | 9.89% | 6–10 | National Dex bonus, Native / custom slot |
| Abra | 9.60% | 8 | Native / custom slot |
| Azurill | 0.286% | 6–10 | National Dex bonus |
| Baltoy | 0.286% | 6–10 | National Dex bonus |
| Binacle | 0.286% | 6–10 | National Dex bonus |
| Bronzor | 0.286% | 6–10 | National Dex bonus |
| Drilbur | 0.286% | 6–10 | National Dex bonus |
| Golett | 0.286% | 6–10 | National Dex bonus |
| Igglybuff | 0.286% | 6–10 | National Dex bonus |
| Larvitar | 0.286% | 6–10 | National Dex bonus |
| Lechonk | 0.286% | 6–10 | National Dex bonus |
| Mudbray | 0.286% | 6–10 | National Dex bonus |
| Noibat | 0.286% | 6–10 | National Dex bonus |
| Teddiursa | 0.286% | 6–10 | National Dex bonus |
| Toedscool | 0.286% | 6–10 | National Dex bonus |

---

<a id="area-40"></a>
## Granite Cave B1F

Source map: MAP_GRANITE_CAVE_B1F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Aron | 38.40% | 9–11 | Native / custom slot |
| Zubat | 28.80% | 9–10 | Native / custom slot |
| Abra | 9.60% | 9 | Native / custom slot |
| Makuhita | 9.60% | 10–11 | Native / custom slot |
| Sableye | 9.60% | 9–11 | Native / custom slot |
| Aipom | 0.286% | 9–11 | National Dex bonus |
| Amaura | 0.286% | 9–11 | National Dex bonus |
| Cleffa | 0.286% | 9–11 | National Dex bonus |
| Doduo | 0.286% | 9–11 | National Dex bonus |
| Glimmet | 0.286% | 9–11 | National Dex bonus |
| Honedge | 0.286% | 9–11 | National Dex bonus |
| Lileep | 0.286% | 9–11 | National Dex bonus |
| Lillipup | 0.286% | 9–11 | National Dex bonus |
| Munchlax | 0.286% | 9–11 | National Dex bonus |
| Nacli | 0.286% | 9–11 | National Dex bonus |
| Rookidee | 0.286% | 9–11 | National Dex bonus |
| Sandile | 0.286% | 9–11 | National Dex bonus |
| Skitty | 0.286% | 9–11 | National Dex bonus |
| Tyrogue | 0.286% | 9–11 | National Dex bonus |

---

<a id="area-41"></a>
## Granite Cave B2F

Source map: MAP_GRANITE_CAVE_B2F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Aron | 38.40% | 10–12 | Native / custom slot |
| Zubat | 28.80% | 10–11 | Native / custom slot |
| Sableye | 19.20% | 10–12 | Native / custom slot |
| Abra | 9.60% | 10 | Native / custom slot |
| Anorith | 0.286% | 10–12 | National Dex bonus |
| Bonsly | 0.286% | 10–12 | National Dex bonus |
| Crabrawler | 0.286% | 10–12 | National Dex bonus |
| Cufant | 0.286% | 10–12 | National Dex bonus |
| Klink | 0.286% | 10–12 | National Dex bonus |
| Meditite | 0.286% | 10–12 | National Dex bonus |
| Nidoran F | 0.286% | 10–12 | National Dex bonus |
| Pancham | 0.286% | 10–12 | National Dex bonus |
| Phanpy | 0.286% | 10–12 | National Dex bonus |
| Pidove | 0.286% | 10–12 | National Dex bonus |
| Pikipek | 0.286% | 10–12 | National Dex bonus |
| Sentret | 0.286% | 10–12 | National Dex bonus |
| Varoom | 0.286% | 10–12 | National Dex bonus |
| Whismur | 0.286% | 10–12 | National Dex bonus |

### Rock Smash (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 70.00% | 5–20 | Native / custom slot |
| Nosepass | 30.00% | 10–20 | Native / custom slot |

---

<a id="area-42"></a>
## Granite Cave Stevens Room

Source map: MAP_GRANITE_CAVE_STEVENS_ROOM.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Makuhita | 48.00% | 6–10 | Native / custom slot |
| Zubat | 28.80% | 7–8 | Native / custom slot |
| Aron | 9.91% | 6–10 | National Dex bonus, Native / custom slot |
| Abra | 9.60% | 8 | Native / custom slot |
| Beldum | 0.308% | 6–10 | National Dex bonus |
| Bunnelby | 0.308% | 6–10 | National Dex bonus |
| Machop | 0.308% | 6–10 | National Dex bonus |
| Mienfoo | 0.308% | 6–10 | National Dex bonus |
| Rhyhorn | 0.308% | 6–10 | National Dex bonus |
| Roggenrola | 0.308% | 6–10 | National Dex bonus |
| Shieldon | 0.308% | 6–10 | National Dex bonus |
| Silicobra | 0.308% | 6–10 | National Dex bonus |
| Skwovet | 0.308% | 6–10 | National Dex bonus |
| Slakoth | 0.308% | 6–10 | National Dex bonus |
| Smeargle | 0.308% | 6–10 | National Dex bonus |
| Tyrunt | 0.308% | 6–10 | National Dex bonus |

---

<a id="area-43"></a>
## Jagged Pass

Source map: MAP_JAGGED_PASS.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Numel | 50.60% | 20–22 | Native / custom slot |
| Machop | 18.40% | 20–21 | Native / custom slot |
| Spoink | 14.72% | 20–22 | Native / custom slot |
| Flareon | 4.60% | 21–23 | Native / custom slot |
| Brickeon | 3.68% | 21–23 | Native / custom slot |
| Carbink | 0.533% | 20–23 | National Dex bonus |
| Chimchar | 0.533% | 20–23 | National Dex bonus |
| Combusken | 0.533% | 20–23 | National Dex bonus |
| Cyndaquil | 0.533% | 20–23 | National Dex bonus |
| Fennekin | 0.533% | 20–23 | National Dex bonus |
| Glimmora | 0.533% | 20–23 | National Dex bonus |
| Hippowdon | 0.533% | 20–23 | National Dex bonus |
| Litten | 0.533% | 20–23 | National Dex bonus |
| Machoke | 0.533% | 20–23 | National Dex bonus |
| Medicham | 0.533% | 20–23 | National Dex bonus |
| Omastar | 0.533% | 20–23 | National Dex bonus |
| Raboot | 0.533% | 20–23 | National Dex bonus |
| Stonjourner | 0.533% | 20–23 | National Dex bonus |
| Throh | 0.533% | 20–23 | National Dex bonus |
| Vulpix | 0.533% | 20–23 | National Dex bonus |

---

<a id="area-44"></a>
## Meteor Falls 1F 1R

Source map: MAP_METEOR_FALLS_1F_1R.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 73.60% | 14–20 | Native / custom slot |
| Solrock | 18.40% | 14–18 | Native / custom slot |
| Axew | 0.533% | 14–20 | National Dex bonus |
| Cetoddle | 0.533% | 14–20 | National Dex bonus |
| Crawdaunt | 0.533% | 18–20 | National Dex bonus |
| Doublade | 0.533% | 18–20 | National Dex bonus |
| Dragonair | 0.533% | 18–20 | National Dex bonus |
| Finneon | 0.533% | 14–20 | National Dex bonus |
| Golduck | 0.533% | 18–20 | National Dex bonus |
| Grapploct | 0.533% | 18–20 | National Dex bonus |
| Jangmo O | 0.533% | 14–20 | National Dex bonus |
| Lairon | 0.533% | 18–20 | National Dex bonus |
| Omanyte | 0.533% | 14–20 | National Dex bonus |
| Sealeo | 0.533% | 18–20 | National Dex bonus |
| Slowbro | 0.533% | 18–20 | National Dex bonus |
| Sneasler | 0.533% | 14–20 | National Dex bonus |
| Timburr | 0.533% | 14–20 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 90.00% | 5–35 | Native / custom slot |
| Solrock | 10.00% | 5–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Barboach | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Barboach | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-45"></a>
## Meteor Falls 1F 2R

Source map: MAP_METEOR_FALLS_1F_2R.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 54.90% | 33–40 | Native / custom slot |
| Solrock | 27.00% | 33–37 | Native / custom slot |
| Drakeon | 4.50% | 36–39 | Native / custom slot |
| Brickeon | 3.60% | 36–39 | Native / custom slot |
| Altaria | 0.625% | 33–40 | National Dex bonus |
| Clobbopus | 0.625% | 33–40 | National Dex bonus |
| Conkeldurr | 0.625% | 34–40 | National Dex bonus |
| Cubchoo | 0.625% | 33–40 | National Dex bonus |
| Frogadier | 0.625% | 33–40 | National Dex bonus |
| Graveler | 0.625% | 33–40 | National Dex bonus |
| Hakamo O | 0.625% | 33–40 | National Dex bonus |
| Iron Thorns | 0.625% | 33–40 | National Dex bonus |
| Lapras | 0.625% | 33–40 | National Dex bonus |
| Lucario | 0.625% | 33–40 | National Dex bonus |
| Naclstack | 0.625% | 33–40 | National Dex bonus |
| Octillery | 0.625% | 33–40 | National Dex bonus |
| Snorunt | 0.625% | 33–40 | National Dex bonus |
| Tyranitar | 0.625% | 34–40 | National Dex bonus |
| Ursaluna | 0.625% | 34–40 | National Dex bonus |
| Wartortle | 0.625% | 33–40 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 90.00% | 30–35 | Native / custom slot |
| Solrock | 10.00% | 5–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Barboach | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Barboach | 80.00% | 25–35 | Native / custom slot |
| Whiscash | 20.00% | 30–45 | Native / custom slot |

---

<a id="area-46"></a>
## Meteor Falls B1F 1R

Source map: MAP_METEOR_FALLS_B1F_1R.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 58.50% | 33–40 | Native / custom slot |
| Solrock | 31.50% | 33–39 | Native / custom slot |
| Azumarill | 0.625% | 34–40 | National Dex bonus |
| Bronzong | 0.625% | 33–40 | National Dex bonus |
| Coalossal | 0.625% | 34–40 | National Dex bonus |
| Cyclizar | 0.625% | 33–40 | National Dex bonus |
| Drakloak | 0.625% | 33–40 | National Dex bonus |
| Frigibax | 0.625% | 33–40 | National Dex bonus |
| Goodra | 0.625% | 34–40 | National Dex bonus |
| Gurdurr | 0.625% | 33–40 | National Dex bonus |
| Gyarados | 0.625% | 33–40 | National Dex bonus |
| Haxorus | 0.625% | 34–40 | National Dex bonus |
| Hitmonchan | 0.625% | 33–40 | National Dex bonus |
| Huntail | 0.625% | 33–40 | National Dex bonus |
| Marshtomp | 0.625% | 33–40 | National Dex bonus |
| Sandshrew | 0.625% | 33–40 | National Dex bonus |
| Tyrantrum | 0.625% | 33–40 | National Dex bonus |
| Wailord | 0.625% | 33–40 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 90.00% | 30–35 | Native / custom slot |
| Solrock | 10.00% | 5–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Barboach | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Barboach | 80.00% | 25–35 | Native / custom slot |
| Whiscash | 20.00% | 30–45 | Native / custom slot |

---

<a id="area-47"></a>
## Meteor Falls B1F 2R

Source map: MAP_METEOR_FALLS_B1F_2R.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 43.66% | 33–40 | Native / custom slot |
| Bagon | 22.27% | 25–35 | Native / custom slot |
| Solrock | 22.27% | 35–39 | Native / custom slot |
| Dravapreon | 0.891% | 38–40 | Native / custom slot |
| Araquanid | 0.619% | 25–40 | National Dex bonus |
| Cranidos | 0.619% | 25–40 | National Dex bonus |
| Dewott | 0.619% | 25–40 | National Dex bonus |
| Diglett | 0.619% | 25–40 | National Dex bonus |
| Dondozo | 0.619% | 25–40 | National Dex bonus |
| Drednaw | 0.619% | 25–40 | National Dex bonus |
| Flygon | 0.619% | 34–40 | National Dex bonus |
| Frosmoth | 0.619% | 25–40 | National Dex bonus |
| Garchomp | 0.619% | 34–40 | National Dex bonus |
| Hawlucha | 0.619% | 25–40 | National Dex bonus |
| Iron Treads | 0.619% | 25–40 | National Dex bonus |
| Jellicent | 0.619% | 25–40 | National Dex bonus |
| Marill | 0.619% | 25–40 | National Dex bonus |
| Mawile | 0.619% | 25–40 | National Dex bonus |
| Shellder | 0.619% | 25–40 | National Dex bonus |
| Starmie | 0.619% | 25–40 | National Dex bonus |
| Diancie | 0.111% | 45 | Rare bonus pool |
| Groudon | 0.111% | 45 | Rare bonus pool |
| Iron Leaves | 0.111% | 45 | Rare bonus pool |
| Regidrago | 0.111% | 45 | Rare bonus pool |
| Regigigas | 0.111% | 45 | Rare bonus pool |
| Regirock | 0.111% | 45 | Rare bonus pool |
| Solgaleo | 0.111% | 45 | Rare bonus pool |
| Thundurus | 0.111% | 45 | Rare bonus pool |
| Urshifu | 0.111% | 45 | Rare bonus pool |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 90.00% | 30–35 | Native / custom slot |
| Solrock | 10.00% | 5–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Barboach | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Barboach | 80.00% | 25–35 | Native / custom slot |
| Whiscash | 20.00% | 30–45 | Native / custom slot |

---

<a id="area-48"></a>
## Meteor Falls Stevens Cave

Source map: MAP_METEOR_FALLS_STEVENS_CAVE.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 57.91% | 33–40 | Native / custom slot |
| Solrock | 31.80% | 33–40 | National Dex bonus, Native / custom slot |
| Arctibax | 0.619% | 33–40 | National Dex bonus |
| Dreepy | 0.619% | 33–40 | National Dex bonus |
| Glalie | 0.619% | 33–40 | National Dex bonus |
| Goomy | 0.619% | 33–40 | National Dex bonus |
| Klang | 0.619% | 33–40 | National Dex bonus |
| Klawf | 0.619% | 33–40 | National Dex bonus |
| Krookodile | 0.619% | 34–40 | National Dex bonus |
| Machamp | 0.619% | 34–40 | National Dex bonus |
| Magikarp | 0.619% | 33–40 | National Dex bonus |
| Primeape | 0.619% | 33–40 | National Dex bonus |
| Rhyperior | 0.619% | 34–40 | National Dex bonus |
| Rockruff | 0.619% | 33–40 | National Dex bonus |
| Sandaconda | 0.619% | 33–40 | National Dex bonus |
| Slowking | 0.619% | 33–40 | National Dex bonus |
| Wingull | 0.619% | 33–40 | National Dex bonus |
| Kyogre | 0.111% | 45 | Rare bonus pool |
| Magearna | 0.111% | 45 | Rare bonus pool |
| Melmetal | 0.111% | 45 | Rare bonus pool |
| Mewtwo | 0.111% | 45 | Rare bonus pool |
| Regieleki | 0.111% | 45 | Rare bonus pool |
| Victini | 0.111% | 45 | Rare bonus pool |
| Volcanion | 0.111% | 45 | Rare bonus pool |
| Walking Wake | 0.111% | 45 | Rare bonus pool |
| Zekrom | 0.111% | 45 | Rare bonus pool |

---

<a id="area-49"></a>
## Mirage Tower 1F

Source map: MAP_MIRAGE_TOWER_1F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sandshrew | 50.00% | 20–24 | Native / custom slot |
| Trapinch | 41.00% | 20–24 | Native / custom slot |
| Duneon | 5.00% | 21–24 | Native / custom slot |
| Brickeon | 4.00% | 21–24 | Native / custom slot |

---

<a id="area-50"></a>
## Mirage Tower 2F

Source map: MAP_MIRAGE_TOWER_2F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sandshrew | 50.00% | 20–24 | Native / custom slot |
| Trapinch | 50.00% | 20–24 | Native / custom slot |

---

<a id="area-51"></a>
## Mirage Tower 3F

Source map: MAP_MIRAGE_TOWER_3F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sandshrew | 50.00% | 20–24 | Native / custom slot |
| Trapinch | 50.00% | 20–24 | Native / custom slot |

---

<a id="area-52"></a>
## Mirage Tower 4F

Source map: MAP_MIRAGE_TOWER_4F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sandshrew | 50.00% | 20–24 | Native / custom slot |
| Trapinch | 50.00% | 20–24 | Native / custom slot |

---

<a id="area-53"></a>
## Mossdeep City

Source map: MAP_MOSSDEEP_CITY.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-54"></a>
## Mt. Pyre 1F

Source map: MAP_MT_PYRE_1F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuppet | 90.00% | 22–29 | Native / custom slot |
| Alakazam | 0.769% | 34 | National Dex bonus |
| Banette | 0.769% | 22–29 | National Dex bonus |
| Bisharp | 0.769% | 22–29 | National Dex bonus |
| Cofagrigus | 0.769% | 22–29 | National Dex bonus |
| Dhelmise | 0.769% | 22–29 | National Dex bonus |
| Gothitelle | 0.769% | 34 | National Dex bonus |
| Houndstone | 0.769% | 22–29 | National Dex bonus |
| Morgrem | 0.769% | 22–29 | National Dex bonus |
| Murkrow | 0.769% | 22–29 | National Dex bonus |
| Phantump | 0.769% | 22–29 | National Dex bonus |
| Ralts | 0.769% | 22–29 | National Dex bonus |
| Spiritomb | 0.769% | 22–29 | National Dex bonus |
| Wynaut | 0.769% | 22–29 | National Dex bonus |

---

<a id="area-55"></a>
## Mt. Pyre 2F

Source map: MAP_MT_PYRE_2F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuppet | 81.90% | 23–29 | Native / custom slot |
| Fanteon | 4.50% | 27–30 | Native / custom slot |
| Umbreon | 3.60% | 27–30 | Native / custom slot |
| Drowzee | 0.769% | 23–30 | National Dex bonus |
| Espathra | 0.769% | 23–30 | National Dex bonus |
| Grumpig | 0.769% | 23–30 | National Dex bonus |
| Houndoom | 0.769% | 23–30 | National Dex bonus |
| Hydreigon | 0.769% | 34 | National Dex bonus |
| Liepard | 0.769% | 23–30 | National Dex bonus |
| Mabosstiff | 0.769% | 23–30 | National Dex bonus |
| Mime Jr. | 0.769% | 23–30 | National Dex bonus |
| Natu | 0.769% | 23–30 | National Dex bonus |
| Nickit | 0.769% | 23–30 | National Dex bonus |
| Sigilyph | 0.769% | 23–30 | National Dex bonus |
| Vullaby | 0.769% | 23–30 | National Dex bonus |
| Zoroark | 0.769% | 23–30 | National Dex bonus |

---

<a id="area-56"></a>
## Mt. Pyre 3F

Source map: MAP_MT_PYRE_3F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuppet | 90.00% | 22–29 | Native / custom slot |
| Abra | 0.769% | 22–29 | National Dex bonus |
| Absol | 0.769% | 22–29 | National Dex bonus |
| Chandelure | 0.769% | 34 | National Dex bonus |
| Chimecho | 0.769% | 22–29 | National Dex bonus |
| Espurr | 0.769% | 22–29 | National Dex bonus |
| Gothita | 0.769% | 22–29 | National Dex bonus |
| Houndour | 0.769% | 22–29 | National Dex bonus |
| Iron Jugulis | 0.769% | 22–29 | National Dex bonus |
| Overqwil | 0.769% | 22–29 | National Dex bonus |
| Thievul | 0.769% | 22–29 | National Dex bonus |
| Weavile | 0.769% | 22–29 | National Dex bonus |
| Xatu | 0.769% | 22–29 | National Dex bonus |
| Zorua | 0.769% | 22–29 | National Dex bonus |

---

<a id="area-57"></a>
## Mt. Pyre 4F

Source map: MAP_MT_PYRE_4F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuppet | 81.77% | 22–29 | National Dex bonus, Native / custom slot |
| Duskull | 9.00% | 25–29 | Native / custom slot |
| Drifloon | 0.769% | 22–29 | National Dex bonus |
| Gastly | 0.769% | 22–29 | National Dex bonus |
| Greavard | 0.769% | 22–29 | National Dex bonus |
| Hattrem | 0.769% | 22–29 | National Dex bonus |
| Maschiff | 0.769% | 22–29 | National Dex bonus |
| Mightyena | 0.769% | 22–29 | National Dex bonus |
| Musharna | 0.769% | 22–29 | National Dex bonus |
| Pawniard | 0.769% | 22–29 | National Dex bonus |
| Solosis | 0.769% | 22–29 | National Dex bonus |
| Umbreon | 0.769% | 22–29 | National Dex bonus |
| Yamask | 0.769% | 22–29 | National Dex bonus |
| Zweilous | 0.769% | 22–29 | National Dex bonus |

---

<a id="area-58"></a>
## Mt. Pyre 5F

Source map: MAP_MT_PYRE_5F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuppet | 81.00% | 22–29 | Native / custom slot |
| Duskull | 9.00% | 25–29 | Native / custom slot |
| Beheeyem | 0.769% | 22–29 | National Dex bonus |
| Duosion | 0.769% | 22–29 | National Dex bonus |
| Dusclops | 0.769% | 22–29 | National Dex bonus |
| Gengar | 0.769% | 34 | National Dex bonus |
| Honchkrow | 0.769% | 22–29 | National Dex bonus |
| Inkay | 0.769% | 22–29 | National Dex bonus |
| Kingambit | 0.769% | 34 | National Dex bonus |
| Obstagoon | 0.769% | 22–29 | National Dex bonus |
| Purrloin | 0.769% | 22–29 | National Dex bonus |
| Sandygast | 0.769% | 22–29 | National Dex bonus |
| Scraggy | 0.769% | 22–29 | National Dex bonus |
| Sneasel | 0.769% | 22–29 | National Dex bonus |
| Wobbuffet | 0.769% | 22–29 | National Dex bonus |

---

<a id="area-59"></a>
## Mt. Pyre 6F

Source map: MAP_MT_PYRE_6F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuppet | 80.19% | 22–29 | Native / custom slot |
| Duskull | 8.91% | 25–29 | Native / custom slot |
| Drifblim | 0.825% | 22–29 | National Dex bonus |
| Dusknoir | 0.825% | 34 | National Dex bonus |
| Elgyem | 0.825% | 22–29 | National Dex bonus |
| Grimmsnarl | 0.825% | 34 | National Dex bonus |
| Hatenna | 0.825% | 22–29 | National Dex bonus |
| Haunter | 0.825% | 22–29 | National Dex bonus |
| Kirlia | 0.825% | 22–29 | National Dex bonus |
| Mandibuzz | 0.825% | 22–29 | National Dex bonus |
| Misdreavus | 0.825% | 22–29 | National Dex bonus |
| Spoink | 0.825% | 22–29 | National Dex bonus |
| Swoobat | 0.825% | 22–29 | National Dex bonus |
| Trevenant | 0.825% | 22–29 | National Dex bonus |
| Calyrex | 0.111% | 45 | Rare bonus pool |
| Darkrai | 0.111% | 45 | Rare bonus pool |
| Fezandipiti | 0.111% | 45 | Rare bonus pool |
| Regice | 0.111% | 45 | Rare bonus pool |
| Reshiram | 0.111% | 45 | Rare bonus pool |
| Stakataka | 0.111% | 45 | Rare bonus pool |
| Tapu Koko | 0.111% | 45 | Rare bonus pool |
| Xurkitree | 0.111% | 45 | Rare bonus pool |
| Zapdos | 0.111% | 45 | Rare bonus pool |

---

<a id="area-60"></a>
## Mt. Pyre Exterior

Source map: MAP_MT_PYRE_EXTERIOR.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuppet | 54.00% | 27–29 | Native / custom slot |
| Vulpix | 22.50% | 27–29 | Native / custom slot |
| Wingull | 5.40% | 26–28 | Native / custom slot |
| Fanteon | 4.50% | 27–30 | Native / custom slot |
| Espeon | 3.60% | 27–30 | Native / custom slot |
| Chingling | 0.769% | 26–30 | National Dex bonus |
| Cursola | 0.769% | 26–30 | National Dex bonus |
| Deino | 0.769% | 26–30 | National Dex bonus |
| Flittle | 0.769% | 26–30 | National Dex bonus |
| Gallade | 0.769% | 34 | National Dex bonus |
| Kadabra | 0.769% | 26–30 | National Dex bonus |
| Litwick | 0.769% | 26–30 | National Dex bonus |
| Mr. Mime | 0.769% | 26–30 | National Dex bonus |
| Palossand | 0.769% | 26–30 | National Dex bonus |
| Poochyena | 0.769% | 26–30 | National Dex bonus |
| Reuniclus | 0.769% | 34 | National Dex bonus |
| Sableye | 0.769% | 26–30 | National Dex bonus |
| Scrafty | 0.769% | 26–30 | National Dex bonus |

---

<a id="area-61"></a>
## Mt. Pyre Summit

Source map: MAP_MT_PYRE_SUMMIT.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuppet | 75.73% | 24–30 | Native / custom slot |
| Duskull | 12.34% | 24–30 | National Dex bonus, Native / custom slot |
| Chimecho | 1.78% | 28 | Native / custom slot |
| Espeon | 0.762% | 24–30 | National Dex bonus |
| Flutter Mane | 0.762% | 24–30 | National Dex bonus |
| Gardevoir | 0.762% | 34 | National Dex bonus |
| Gothorita | 0.762% | 24–30 | National Dex bonus |
| Hatterene | 0.762% | 34 | National Dex bonus |
| Hypno | 0.762% | 24–30 | National Dex bonus |
| Impidimp | 0.762% | 24–30 | National Dex bonus |
| Lampent | 0.762% | 24–30 | National Dex bonus |
| Malamar | 0.762% | 24–30 | National Dex bonus |
| Mismagius | 0.762% | 24–30 | National Dex bonus |
| Munna | 0.762% | 24–30 | National Dex bonus |
| Woobat | 0.762% | 24–30 | National Dex bonus |
| Celesteela | 0.111% | 45 | Rare bonus pool |
| Entei | 0.111% | 45 | Rare bonus pool |
| Eternatus | 0.111% | 45 | Rare bonus pool |
| Glastrier | 0.111% | 45 | Rare bonus pool |
| Gouging Fire | 0.111% | 45 | Rare bonus pool |
| Kyurem | 0.111% | 45 | Rare bonus pool |
| Latios | 0.111% | 45 | Rare bonus pool |
| Palkia | 0.111% | 45 | Rare bonus pool |
| Tapu Lele | 0.111% | 45 | Rare bonus pool |

---

<a id="area-62"></a>
## New Mauville Entrance

Source map: MAP_NEW_MAUVILLE_ENTRANCE.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magnemite | 46.00% | 22–26 | Native / custom slot |
| Voltorb | 46.00% | 22–26 | Native / custom slot |
| Claydol | 0.533% | 22–26 | National Dex bonus |
| Dedenne | 0.533% | 22–26 | National Dex bonus |
| Dracozolt | 0.533% | 22–26 | National Dex bonus |
| Dugtrio | 0.533% | 22–26 | National Dex bonus |
| Eelektrik | 0.533% | 22–26 | National Dex bonus |
| Excadrill | 0.533% | 22–26 | National Dex bonus |
| Flaaffy | 0.533% | 22–26 | National Dex bonus |
| Helioptile | 0.533% | 22–26 | National Dex bonus |
| Hippopotas | 0.533% | 22–26 | National Dex bonus |
| Kilowattrel | 0.533% | 22–26 | National Dex bonus |
| Magneton | 0.533% | 22–26 | National Dex bonus |
| Nosepass | 0.533% | 22–26 | National Dex bonus |
| Perrserker | 0.533% | 22–26 | National Dex bonus |
| Rhydon | 0.533% | 22–26 | National Dex bonus |
| Shinx | 0.533% | 22–26 | National Dex bonus |

---

<a id="area-63"></a>
## New Mauville Inside

Source map: MAP_NEW_MAUVILLE_INSIDE.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Voltorb | 45.08% | 22–26 | Native / custom slot |
| Magnemite | 36.80% | 23–25 | Native / custom slot |
| Jolteon | 4.60% | 24–26 | Native / custom slot |
| Ferumeon | 3.68% | 24–26 | Native / custom slot |
| Electrode | 1.45% | 22–26 | National Dex bonus, Native / custom slot |
| Magneton | 0.920% | 26 | Native / custom slot |
| Armaldo | 0.533% | 22–26 | National Dex bonus |
| Boltund | 0.533% | 22–26 | National Dex bonus |
| Donphan | 0.533% | 22–26 | National Dex bonus |
| Falinks | 0.533% | 22–26 | National Dex bonus |
| Golurk | 0.533% | 22–26 | National Dex bonus |
| Kabuto | 0.533% | 22–26 | National Dex bonus |
| Makuhita | 0.533% | 22–26 | National Dex bonus |
| Mankey | 0.533% | 22–26 | National Dex bonus |
| Orthworm | 0.533% | 22–26 | National Dex bonus |
| Pachirisu | 0.533% | 22–26 | National Dex bonus |
| Pangoro | 0.533% | 22–26 | National Dex bonus |
| Sawk | 0.533% | 22–26 | National Dex bonus |
| Togedemaru | 0.533% | 22–26 | National Dex bonus |
| Zebstrika | 0.533% | 22–26 | National Dex bonus |

---

<a id="area-64"></a>
## Petalburg City

Source map: MAP_PETALBURG_CITY.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Marill | 100.00% | 5–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Corphish | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Corphish | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-65"></a>
## Petalburg Woods

Source map: MAP_PETALBURG_WOODS.

### Grass / cave (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poochyena | 28.80% | 5–6 | Native / custom slot |
| Wurmple | 24.00% | 5–6 | Native / custom slot |
| Shroomish | 14.40% | 5–6 | Native / custom slot |
| Cascoon | 9.60% | 5 | Native / custom slot |
| Silcoon | 9.60% | 5 | Native / custom slot |
| Slakoth | 4.80% | 5–6 | Native / custom slot |
| Taillow | 4.80% | 5–6 | Native / custom slot |
| Bramblin | 0.267% | 5–6 | National Dex bonus |
| Bulbasaur | 0.267% | 5–6 | National Dex bonus |
| Cherubi | 0.267% | 5–6 | National Dex bonus |
| Cutiefly | 0.267% | 5–6 | National Dex bonus |
| Ferroseed | 0.267% | 5–6 | National Dex bonus |
| Grookey | 0.267% | 5–6 | National Dex bonus |
| Hoppip | 0.267% | 5–6 | National Dex bonus |
| Ledyba | 0.267% | 5–6 | National Dex bonus |
| Pansage | 0.267% | 5–6 | National Dex bonus |
| Petilil | 0.267% | 5–6 | National Dex bonus |
| Sprigatito | 0.267% | 5–6 | National Dex bonus |
| Spritzee | 0.267% | 5–6 | National Dex bonus |
| Starly | 0.267% | 5–6 | National Dex bonus |
| Sunkern | 0.267% | 5–6 | National Dex bonus |
| Treecko | 0.267% | 5–6 | National Dex bonus |

---

<a id="area-66"></a>
## Rusturf Tunnel

Source map: MAP_RUSTURF_TUNNEL.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Whismur | 100.00% | 5–8 | Native / custom slot |

---

<a id="area-67"></a>
## Safari Zone Center

Source map: MAP_SAFARI_ZONE_CENTER.

### Source variant 1: sSafariZoneCenter_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Exeggcute | 18.00% | 24–25 | Native / custom slot |
| Nidoran M | 18.00% | 22 | Native / custom slot |
| Rhyhorn | 18.00% | 25 | Native / custom slot |
| Venonat | 13.50% | 22 | Native / custom slot |
| Nidorino | 9.00% | 31 | Native / custom slot |
| Nidorina | 4.50% | 31 | Native / custom slot |
| Parasect | 4.50% | 30 | Native / custom slot |
| Scyther | 3.60% | 23 | Native / custom slot |
| Chansey | 0.900% | 23 | Native / custom slot |
| Amoonguss | 0.625% | 22–31 | National Dex bonus |
| Applin | 0.625% | 22–31 | National Dex bonus |
| Beautifly | 0.625% | 34 | National Dex bonus |
| Bounsweet | 0.625% | 22–31 | National Dex bonus |
| Budew | 0.625% | 22–31 | National Dex bonus |
| Cacnea | 0.625% | 22–31 | National Dex bonus |
| Ekans | 0.625% | 22–31 | National Dex bonus |
| Forretress | 0.625% | 22–31 | National Dex bonus |
| Larvesta | 0.625% | 22–31 | National Dex bonus |
| Lurantis | 0.625% | 22–31 | National Dex bonus |
| Meganium | 0.625% | 34 | National Dex bonus |
| Paras | 0.625% | 22–31 | National Dex bonus |
| Serperior | 0.625% | 34 | National Dex bonus |
| Slither Wing | 0.625% | 22–31 | National Dex bonus |
| Snover | 0.625% | 22–31 | National Dex bonus |
| Squawkabilly | 0.625% | 22–31 | National Dex bonus |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Dratini | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 4.00% | 15–35 | Native / custom slot |
| Dragonair | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sSafariZoneCenter_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Exeggcute | 18.00% | 24–25 | Native / custom slot |
| Nidoran F | 18.00% | 22 | Native / custom slot |
| Rhyhorn | 18.00% | 25 | Native / custom slot |
| Venonat | 13.50% | 22 | Native / custom slot |
| Nidorina | 9.00% | 31 | Native / custom slot |
| Nidorino | 4.50% | 31 | Native / custom slot |
| Parasect | 4.50% | 30 | Native / custom slot |
| Pinsir | 3.60% | 23 | Native / custom slot |
| Chansey | 0.900% | 23 | Native / custom slot |
| Amoonguss | 0.625% | 22–31 | National Dex bonus |
| Applin | 0.625% | 22–31 | National Dex bonus |
| Beautifly | 0.625% | 34 | National Dex bonus |
| Bounsweet | 0.625% | 22–31 | National Dex bonus |
| Budew | 0.625% | 22–31 | National Dex bonus |
| Cacnea | 0.625% | 22–31 | National Dex bonus |
| Ekans | 0.625% | 22–31 | National Dex bonus |
| Forretress | 0.625% | 22–31 | National Dex bonus |
| Larvesta | 0.625% | 22–31 | National Dex bonus |
| Lurantis | 0.625% | 22–31 | National Dex bonus |
| Meganium | 0.625% | 34 | National Dex bonus |
| Paras | 0.625% | 22–31 | National Dex bonus |
| Serperior | 0.625% | 34 | National Dex bonus |
| Slither Wing | 0.625% | 22–31 | National Dex bonus |
| Snover | 0.625% | 22–31 | National Dex bonus |
| Squawkabilly | 0.625% | 22–31 | National Dex bonus |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Dratini | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 4.00% | 15–35 | Native / custom slot |
| Dragonair | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-68"></a>
## Safari Zone East

Source map: MAP_SAFARI_ZONE_EAST.

### Source variant 1: sSafariZoneEast_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Doduo | 18.00% | 26 | Native / custom slot |
| Exeggcute | 18.00% | 23–25 | Native / custom slot |
| Nidoran M | 18.00% | 24 | Native / custom slot |
| Paras | 13.50% | 22 | Native / custom slot |
| Nidorino | 9.00% | 33 | Native / custom slot |
| Nidoran F | 4.50% | 24 | Native / custom slot |
| Parasect | 4.50% | 25 | Native / custom slot |
| Kangaskhan | 4.22% | 22–33 | National Dex bonus, Native / custom slot |
| Scyther | 0.900% | 28 | Native / custom slot |
| Comfey | 0.625% | 22–33 | National Dex bonus |
| Golbat | 0.625% | 22–33 | National Dex bonus |
| Grotle | 0.625% | 22–33 | National Dex bonus |
| Iron Valiant | 0.625% | 22–33 | National Dex bonus |
| Leavanny | 0.625% | 34 | National Dex bonus |
| Ninjask | 0.625% | 22–33 | National Dex bonus |
| Pidgeot | 0.625% | 34 | National Dex bonus |
| Scovillain | 0.625% | 22–33 | National Dex bonus |
| Shelmet | 0.625% | 22–33 | National Dex bonus |
| Shiftry | 0.625% | 34 | National Dex bonus |
| Skiddo | 0.625% | 22–33 | National Dex bonus |
| Skorupi | 0.625% | 22–33 | National Dex bonus |
| Tarountula | 0.625% | 22–33 | National Dex bonus |
| Toucannon | 0.625% | 34 | National Dex bonus |
| Yanma | 0.625% | 22–33 | National Dex bonus |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Dratini | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 4.00% | 15–35 | Native / custom slot |
| Dragonair | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sSafariZoneEast_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Doduo | 18.00% | 26 | Native / custom slot |
| Exeggcute | 18.00% | 23–25 | Native / custom slot |
| Nidoran F | 18.00% | 24 | Native / custom slot |
| Paras | 13.50% | 22 | Native / custom slot |
| Nidorina | 9.00% | 33 | Native / custom slot |
| Nidoran M | 4.50% | 24 | Native / custom slot |
| Parasect | 4.50% | 25 | Native / custom slot |
| Kangaskhan | 4.22% | 22–33 | National Dex bonus, Native / custom slot |
| Pinsir | 0.900% | 28 | Native / custom slot |
| Comfey | 0.625% | 22–33 | National Dex bonus |
| Golbat | 0.625% | 22–33 | National Dex bonus |
| Grotle | 0.625% | 22–33 | National Dex bonus |
| Iron Valiant | 0.625% | 22–33 | National Dex bonus |
| Leavanny | 0.625% | 34 | National Dex bonus |
| Ninjask | 0.625% | 22–33 | National Dex bonus |
| Pidgeot | 0.625% | 34 | National Dex bonus |
| Scovillain | 0.625% | 22–33 | National Dex bonus |
| Shelmet | 0.625% | 22–33 | National Dex bonus |
| Shiftry | 0.625% | 34 | National Dex bonus |
| Skiddo | 0.625% | 22–33 | National Dex bonus |
| Skorupi | 0.625% | 22–33 | National Dex bonus |
| Tarountula | 0.625% | 22–33 | National Dex bonus |
| Toucannon | 0.625% | 34 | National Dex bonus |
| Yanma | 0.625% | 22–33 | National Dex bonus |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Dratini | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 4.00% | 15–35 | Native / custom slot |
| Dragonair | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-69"></a>
## Safari Zone North

Source map: MAP_SAFARI_ZONE_NORTH.

### Grass / cave (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 27.00% | 27–29 | Native / custom slot |
| Phanpy | 27.00% | 27–29 | Native / custom slot |
| Gloom | 13.50% | 29–31 | Native / custom slot |
| Natu | 9.00% | 27 | Native / custom slot |
| Sylveon | 4.50% | 28–31 | Native / custom slot |
| Xatu | 4.50% | 29–31 | Native / custom slot |
| Artheon | 3.60% | 28–31 | Native / custom slot |
| Heracross | 0.900% | 29 | Native / custom slot |
| Blissey | 0.625% | 34 | National Dex bonus |
| Butterfree | 0.625% | 34 | National Dex bonus |
| Charjabug | 0.625% | 27–31 | National Dex bonus |
| Exeggcute | 0.625% | 27–31 | National Dex bonus |
| Fidough | 0.625% | 27–31 | National Dex bonus |
| Kleavor | 0.625% | 27–31 | National Dex bonus |
| Kricketune | 0.625% | 27–31 | National Dex bonus |
| Ledian | 0.625% | 27–31 | National Dex bonus |
| Maractus | 0.625% | 27–31 | National Dex bonus |
| Quilladin | 0.625% | 27–31 | National Dex bonus |
| Seviper | 0.625% | 27–31 | National Dex bonus |
| Sewaddle | 0.625% | 27–31 | National Dex bonus |
| Steenee | 0.625% | 27–31 | National Dex bonus |
| Tangrowth | 0.625% | 27–31 | National Dex bonus |
| Tinkatuff | 0.625% | 27–31 | National Dex bonus |
| Vileplume | 0.625% | 34 | National Dex bonus |

### Rock Smash (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 100.00% | 5–30 | Native / custom slot |

---

<a id="area-70"></a>
## Safari Zone Northeast

Source map: MAP_SAFARI_ZONE_NORTHEAST.

### Grass / cave (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Aipom | 27.00% | 33–35 | Native / custom slot |
| Teddiursa | 27.00% | 34–36 | Native / custom slot |
| Ledyba | 9.00% | 33 | Native / custom slot |
| Sunkern | 9.00% | 34 | Native / custom slot |
| Hoothoot | 4.50% | 35 | Native / custom slot |
| Houndour | 4.50% | 36–39 | Native / custom slot |
| Miltank | 4.50% | 37–40 | Native / custom slot |
| Pineco | 4.50% | 34 | Native / custom slot |
| Appletun | 0.625% | 33–40 | National Dex bonus |
| Bayleef | 0.625% | 33–40 | National Dex bonus |
| Cascoon | 0.625% | 33–40 | National Dex bonus |
| Deerling | 0.625% | 33–40 | National Dex bonus |
| Furfrou | 0.625% | 33–40 | National Dex bonus |
| Masquerain | 0.625% | 33–40 | National Dex bonus |
| Metapod | 0.625% | 33–40 | National Dex bonus |
| Oricorio | 0.625% | 33–40 | National Dex bonus |
| Rabsca | 0.625% | 33–40 | National Dex bonus |
| Roserade | 0.625% | 34–40 | National Dex bonus |
| Rotom | 0.625% | 33–40 | National Dex bonus |
| Sunflora | 0.625% | 33–40 | National Dex bonus |
| Tinkaton | 0.625% | 34–40 | National Dex bonus |
| Whirlipede | 0.625% | 33–40 | National Dex bonus |
| Wimpod | 0.625% | 33–40 | National Dex bonus |
| Zubat | 0.625% | 33–40 | National Dex bonus |

### Rock Smash (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuckle | 100.00% | 20–40 | Native / custom slot |

---

<a id="area-71"></a>
## Safari Zone Northwest

Source map: MAP_SAFARI_ZONE_NORTHWEST.

### Grass / cave (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 27.00% | 27–29 | Native / custom slot |
| Rhyhorn | 27.00% | 27–29 | Native / custom slot |
| Doduo | 13.50% | 27–29 | Native / custom slot |
| Gloom | 13.50% | 29–31 | Native / custom slot |
| Dodrio | 4.50% | 29–31 | Native / custom slot |
| Pinsir | 4.50% | 27–29 | Native / custom slot |
| Abomasnow | 0.625% | 27–31 | National Dex bonus |
| Dipplin | 0.625% | 27–31 | National Dex bonus |
| Dustox | 0.625% | 34 | National Dex bonus |
| Floette | 0.625% | 27–31 | National Dex bonus |
| Floragato | 0.625% | 27–31 | National Dex bonus |
| Lilligant | 0.625% | 27–31 | National Dex bonus |
| Pidgeotto | 0.625% | 27–31 | National Dex bonus |
| Porygon | 0.625% | 27–31 | National Dex bonus |
| Shroomish | 0.625% | 27–31 | National Dex bonus |
| Skiploom | 0.625% | 27–31 | National Dex bonus |
| Spidops | 0.625% | 27–31 | National Dex bonus |
| Swadloon | 0.625% | 27–31 | National Dex bonus |
| Type: Null | 0.625% | 27–31 | National Dex bonus |
| Venonat | 0.625% | 27–31 | National Dex bonus |
| Vikavolt | 0.625% | 34 | National Dex bonus |
| Wormadam | 0.625% | 27–31 | National Dex bonus |

### Surf (base encounter-frequency setting: 9)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 95.00% | 20–35 | Native / custom slot |
| Golduck | 5.00% | 25–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 35)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 35)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Goldeen | 40.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 35)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 80.00% | 25–35 | Native / custom slot |
| Seaking | 20.00% | 25–40 | Native / custom slot |

---

<a id="area-72"></a>
## Safari Zone North Frlg

Source map: MAP_SAFARI_ZONE_NORTH_FRLG.

### Source variant 1: sSafariZoneNorth_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Exeggcute | 20.00% | 25–27 | Native / custom slot |
| Nidoran M | 20.00% | 30 | Native / custom slot |
| Rhyhorn | 20.00% | 26 | Native / custom slot |
| Paras | 15.00% | 23 | Native / custom slot |
| Nidorino | 10.00% | 30 | Native / custom slot |
| Nidorina | 5.00% | 30 | Native / custom slot |
| Venomoth | 5.00% | 32 | Native / custom slot |
| Chansey | 4.00% | 26 | Native / custom slot |
| Tauros | 1.00% | 28 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Dratini | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 4.00% | 15–35 | Native / custom slot |
| Dragonair | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sSafariZoneNorth_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Exeggcute | 20.00% | 25–27 | Native / custom slot |
| Nidoran F | 20.00% | 30 | Native / custom slot |
| Rhyhorn | 20.00% | 26 | Native / custom slot |
| Paras | 15.00% | 23 | Native / custom slot |
| Nidorina | 10.00% | 30 | Native / custom slot |
| Nidorino | 5.00% | 30 | Native / custom slot |
| Venomoth | 5.00% | 32 | Native / custom slot |
| Chansey | 4.00% | 26 | Native / custom slot |
| Tauros | 1.00% | 28 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Dratini | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 4.00% | 15–35 | Native / custom slot |
| Dragonair | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-73"></a>
## Safari Zone South

Source map: MAP_SAFARI_ZONE_SOUTH.

### Grass / cave (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 36.00% | 25–27 | Native / custom slot |
| Girafarig | 18.00% | 25–27 | Native / custom slot |
| Doduo | 9.00% | 25 | Native / custom slot |
| Natu | 9.00% | 25 | Native / custom slot |
| Wobbuffet | 9.00% | 27–29 | Native / custom slot |
| Gloom | 4.50% | 25 | Native / custom slot |
| Pikachu | 4.50% | 25–27 | Native / custom slot |
| Alomomola | 0.625% | 25–29 | National Dex bonus |
| Beedrill | 0.625% | 34 | National Dex bonus |
| Breloom | 0.625% | 25–29 | National Dex bonus |
| Carnivine | 0.625% | 25–29 | National Dex bonus |
| Chesnaught | 0.625% | 34 | National Dex bonus |
| Clefable | 0.625% | 34 | National Dex bonus |
| Decidueye | 0.625% | 34 | National Dex bonus |
| Dudunsparce | 0.625% | 25–29 | National Dex bonus |
| Gorebyss | 0.625% | 25–29 | National Dex bonus |
| Meowscarada | 0.625% | 34 | National Dex bonus |
| Rellor | 0.625% | 25–29 | National Dex bonus |
| Sceptile | 0.625% | 34 | National Dex bonus |
| Scyther | 0.625% | 25–29 | National Dex bonus |
| Simipour | 0.625% | 25–29 | National Dex bonus |
| Tsareena | 0.625% | 34 | National Dex bonus |
| Unown | 0.625% | 25–29 | National Dex bonus |

---

<a id="area-74"></a>
## Safari Zone Southeast

Source map: MAP_SAFARI_ZONE_SOUTHEAST.

### Grass / cave (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Mareep | 27.00% | 34–36 | Native / custom slot |
| Sunkern | 27.00% | 33–35 | Native / custom slot |
| Aipom | 9.00% | 34 | Native / custom slot |
| Spinarak | 9.00% | 33 | Native / custom slot |
| Gligar | 4.50% | 37–40 | Native / custom slot |
| Hoothoot | 4.50% | 35 | Native / custom slot |
| Snubbull | 4.50% | 34 | Native / custom slot |
| Stantler | 4.50% | 36–39 | Native / custom slot |
| Blastoise | 0.625% | 34–40 | National Dex bonus |
| Corvisquire | 0.625% | 33–40 | National Dex bonus |
| Crobat | 0.625% | 34–40 | National Dex bonus |
| Dachsbun | 0.625% | 33–40 | National Dex bonus |
| Drapion | 0.625% | 33–40 | National Dex bonus |
| Empoleon | 0.625% | 34–40 | National Dex bonus |
| Galvantula | 0.625% | 33–40 | National Dex bonus |
| Gimmighoul | 0.625% | 33–40 | National Dex bonus |
| Gogoat | 0.625% | 33–40 | National Dex bonus |
| Goldeen | 0.625% | 33–40 | National Dex bonus |
| Illumise | 0.625% | 33–40 | National Dex bonus |
| Mantine | 0.625% | 33–40 | National Dex bonus |
| Nidoking | 0.625% | 34–40 | National Dex bonus |
| Orbeetle | 0.625% | 34–40 | National Dex bonus |
| Slurpuff | 0.625% | 33–40 | National Dex bonus |
| Stoutland | 0.625% | 34–40 | National Dex bonus |

### Surf (base encounter-frequency setting: 9)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wooper | 60.00% | 25–30 | Native / custom slot |
| Marill | 39.00% | 25–35 | Native / custom slot |
| Quagsire | 1.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 35)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 25–30 | Native / custom slot |
| Goldeen | 30.00% | 25–30 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 35)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 25–30 | Native / custom slot |
| Goldeen | 20.00% | 25–30 | Native / custom slot |
| Remoraid | 20.00% | 30–35 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 35)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Remoraid | 59.00% | 25–35 | Native / custom slot |
| Goldeen | 40.00% | 25–30 | Native / custom slot |
| Octillery | 1.00% | 35–40 | Native / custom slot |

---

<a id="area-75"></a>
## Safari Zone Southwest

Source map: MAP_SAFARI_ZONE_SOUTHWEST.

### Grass / cave (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 36.00% | 25–27 | Native / custom slot |
| Girafarig | 18.00% | 25–27 | Native / custom slot |
| Doduo | 9.00% | 27 | Native / custom slot |
| Natu | 9.00% | 25 | Native / custom slot |
| Wobbuffet | 9.00% | 27–29 | Native / custom slot |
| Gloom | 4.50% | 25 | Native / custom slot |
| Pikachu | 4.50% | 25–27 | Native / custom slot |
| Bellossom | 0.625% | 34 | National Dex bonus |
| Brute Bonnet | 0.625% | 25–29 | National Dex bonus |
| Corviknight | 0.625% | 34 | National Dex bonus |
| Grafaiai | 0.625% | 25–29 | National Dex bonus |
| Heracross | 0.625% | 25–29 | National Dex bonus |
| Joltik | 0.625% | 25–29 | National Dex bonus |
| Nidoqueen | 0.625% | 34 | National Dex bonus |
| Noivern | 0.625% | 25–29 | National Dex bonus |
| Polteageist | 0.625% | 25–29 | National Dex bonus |
| Roselia | 0.625% | 25–29 | National Dex bonus |
| Seadra | 0.625% | 25–29 | National Dex bonus |
| Togekiss | 0.625% | 34 | National Dex bonus |
| Torterra | 0.625% | 34 | National Dex bonus |
| Unfezant | 0.625% | 34 | National Dex bonus |
| Volcarona | 0.625% | 25–29 | National Dex bonus |
| Weepinbell | 0.625% | 25–29 | National Dex bonus |

### Surf (base encounter-frequency setting: 9)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 35)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 35)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Goldeen | 40.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 35)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 80.00% | 25–35 | Native / custom slot |
| Seaking | 20.00% | 25–40 | Native / custom slot |

---

<a id="area-76"></a>
## Safari Zone West

Source map: MAP_SAFARI_ZONE_WEST.

### Source variant 1: sSafariZoneWest_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Doduo | 18.00% | 26 | Native / custom slot |
| Exeggcute | 18.00% | 25–27 | Native / custom slot |
| Nidoran M | 18.00% | 22 | Native / custom slot |
| Venonat | 13.50% | 23 | Native / custom slot |
| Nidorino | 9.00% | 30 | Native / custom slot |
| Nidoran F | 4.50% | 30 | Native / custom slot |
| Venomoth | 4.50% | 32 | Native / custom slot |
| Tauros | 3.60% | 25 | Native / custom slot |
| Kangaskhan | 0.900% | 28 | Native / custom slot |
| Arboliva | 0.625% | 34 | National Dex bonus |
| Dartrix | 0.625% | 22–32 | National Dex bonus |
| Escavalier | 0.625% | 22–32 | National Dex bonus |
| Golisopod | 0.625% | 22–32 | National Dex bonus |
| Hydrapple | 0.625% | 34 | National Dex bonus |
| Jumpluff | 0.625% | 34 | National Dex bonus |
| Kricketot | 0.625% | 22–32 | National Dex bonus |
| Morpeko | 0.625% | 22–32 | National Dex bonus |
| Oddish | 0.625% | 22–32 | National Dex bonus |
| Porygon-Z | 0.625% | 34 | National Dex bonus |
| Scolipede | 0.625% | 34 | National Dex bonus |
| Victreebel | 0.625% | 34 | National Dex bonus |
| Vivillon | 0.625% | 22–32 | National Dex bonus |
| Volbeat | 0.625% | 22–32 | National Dex bonus |
| Weedle | 0.625% | 22–32 | National Dex bonus |
| Wurmple | 0.625% | 22–32 | National Dex bonus |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Dratini | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 4.00% | 15–35 | Native / custom slot |
| Dragonair | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sSafariZoneWest_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Doduo | 18.00% | 26 | Native / custom slot |
| Exeggcute | 18.00% | 25–27 | Native / custom slot |
| Nidoran F | 18.00% | 22 | Native / custom slot |
| Venonat | 13.50% | 23 | Native / custom slot |
| Nidorina | 9.00% | 30 | Native / custom slot |
| Nidoran M | 4.50% | 30 | Native / custom slot |
| Venomoth | 4.50% | 32 | Native / custom slot |
| Tauros | 3.60% | 25 | Native / custom slot |
| Kangaskhan | 0.900% | 28 | Native / custom slot |
| Arboliva | 0.625% | 34 | National Dex bonus |
| Dartrix | 0.625% | 22–32 | National Dex bonus |
| Escavalier | 0.625% | 22–32 | National Dex bonus |
| Golisopod | 0.625% | 22–32 | National Dex bonus |
| Hydrapple | 0.625% | 34 | National Dex bonus |
| Jumpluff | 0.625% | 34 | National Dex bonus |
| Kricketot | 0.625% | 22–32 | National Dex bonus |
| Morpeko | 0.625% | 22–32 | National Dex bonus |
| Oddish | 0.625% | 22–32 | National Dex bonus |
| Porygon-Z | 0.625% | 34 | National Dex bonus |
| Scolipede | 0.625% | 34 | National Dex bonus |
| Victreebel | 0.625% | 34 | National Dex bonus |
| Vivillon | 0.625% | 22–32 | National Dex bonus |
| Volbeat | 0.625% | 22–32 | National Dex bonus |
| Weedle | 0.625% | 22–32 | National Dex bonus |
| Wurmple | 0.625% | 22–32 | National Dex bonus |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Dratini | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 4.00% | 15–35 | Native / custom slot |
| Dragonair | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-77"></a>
## Seafloor Cavern Entrance

Source map: MAP_SEAFLOOR_CAVERN_ENTRANCE.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Zubat | 35.00% | 5–35 | Native / custom slot |
| Golbat | 5.00% | 30–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-78"></a>
## Seafloor Cavern Room1

Source map: MAP_SEAFLOOR_CAVERN_ROOM1.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 85.00% | 28–34 | Native / custom slot |
| Golbat | 6.00% | 33–36 | Native / custom slot |
| Vaporeon | 5.00% | 33–36 | Native / custom slot |
| Umbreon | 4.00% | 33–36 | Native / custom slot |

---

<a id="area-79"></a>
## Seafloor Cavern Room2

Source map: MAP_SEAFLOOR_CAVERN_ROOM2.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 90.00% | 28–35 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

---

<a id="area-80"></a>
## Seafloor Cavern Room3

Source map: MAP_SEAFLOOR_CAVERN_ROOM3.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 90.00% | 28–35 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

---

<a id="area-81"></a>
## Seafloor Cavern Room4

Source map: MAP_SEAFLOOR_CAVERN_ROOM4.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 90.00% | 28–35 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

---

<a id="area-82"></a>
## Seafloor Cavern Room5

Source map: MAP_SEAFLOOR_CAVERN_ROOM5.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 90.00% | 28–35 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

---

<a id="area-83"></a>
## Seafloor Cavern Room6

Source map: MAP_SEAFLOOR_CAVERN_ROOM6.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 90.00% | 28–35 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Zubat | 35.00% | 5–35 | Native / custom slot |
| Golbat | 5.00% | 30–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-84"></a>
## Seafloor Cavern Room7

Source map: MAP_SEAFLOOR_CAVERN_ROOM7.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 90.00% | 28–35 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Zubat | 35.00% | 5–35 | Native / custom slot |
| Golbat | 5.00% | 30–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-85"></a>
## Seafloor Cavern Room8

Source map: MAP_SEAFLOOR_CAVERN_ROOM8.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 90.00% | 28–35 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

---

<a id="area-86"></a>
## Shoal Cave Low Tide Entrance Room

Source map: MAP_SHOAL_CAVE_LOW_TIDE_ENTRANCE_ROOM.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Spheal | 45.00% | 26–32 | Native / custom slot |
| Zubat | 40.50% | 26–32 | Native / custom slot |
| Golbat | 4.50% | 32 | Native / custom slot |
| Barboach | 0.667% | 26–32 | National Dex bonus |
| Brionne | 0.667% | 26–32 | National Dex bonus |
| Carracosta | 0.667% | 26–32 | National Dex bonus |
| Croconaw | 0.667% | 26–32 | National Dex bonus |
| Drizzile | 0.667% | 26–32 | National Dex bonus |
| Iron Bundle | 0.667% | 26–32 | National Dex bonus |
| Kingler | 0.667% | 26–32 | National Dex bonus |
| Milotic | 0.667% | 26–32 | National Dex bonus |
| Piloswine | 0.667% | 26–32 | National Dex bonus |
| Piplup | 0.667% | 26–32 | National Dex bonus |
| Poliwhirl | 0.667% | 26–32 | National Dex bonus |
| Quaquaval | 0.667% | 34 | National Dex bonus |
| Seismitoad | 0.667% | 34 | National Dex bonus |
| Smoochum | 0.667% | 26–32 | National Dex bonus |
| Snom | 0.667% | 26–32 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Zubat | 30.00% | 5–35 | Native / custom slot |
| Spheal | 10.00% | 25–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-87"></a>
## Shoal Cave Low Tide Ice Room

Source map: MAP_SHOAL_CAVE_LOW_TIDE_ICE_ROOM.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Spheal | 40.09% | 26–32 | Native / custom slot |
| Zubat | 35.64% | 26–30 | Native / custom slot |
| Snorunt | 8.91% | 26–30 | Native / custom slot |
| Golbat | 4.46% | 30–32 | Native / custom slot |
| Avalugg | 0.707% | 26–32 | National Dex bonus |
| Chewtle | 0.707% | 26–32 | National Dex bonus |
| Clamperl | 0.707% | 26–32 | National Dex bonus |
| Dewgong | 0.707% | 26–32 | National Dex bonus |
| Frillish | 0.707% | 26–32 | National Dex bonus |
| Glaceon | 0.707% | 26–32 | National Dex bonus |
| Kingdra | 0.707% | 34 | National Dex bonus |
| Lanturn | 0.707% | 26–32 | National Dex bonus |
| Pyukumuku | 0.707% | 26–32 | National Dex bonus |
| Swinub | 0.707% | 26–32 | National Dex bonus |
| Tentacool | 0.707% | 26–32 | National Dex bonus |
| Tympole | 0.707% | 26–32 | National Dex bonus |
| Wailmer | 0.707% | 26–32 | National Dex bonus |
| Wiglett | 0.707% | 26–32 | National Dex bonus |
| Cosmoem | 0.111% | 45 | Rare bonus pool |
| Deoxys | 0.111% | 45 | Rare bonus pool |
| Giratina | 0.111% | 45 | Rare bonus pool |
| Moltres | 0.111% | 45 | Rare bonus pool |
| Naganadel | 0.111% | 45 | Rare bonus pool |
| Nihilego | 0.111% | 45 | Rare bonus pool |
| Raging Bolt | 0.111% | 45 | Rare bonus pool |
| Ting Lu | 0.111% | 45 | Rare bonus pool |
| Tornadus | 0.111% | 45 | Rare bonus pool |

---

<a id="area-88"></a>
## Shoal Cave Low Tide Inner Room

Source map: MAP_SHOAL_CAVE_LOW_TIDE_INNER_ROOM.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 40.50% | 26–32 | Native / custom slot |
| Spheal | 36.90% | 26–32 | Native / custom slot |
| Glaceon | 4.50% | 30–33 | Native / custom slot |
| Golbat | 4.50% | 32 | Native / custom slot |
| Vaporeon | 3.60% | 30–33 | Native / custom slot |
| Arrokuda | 0.667% | 26–33 | National Dex bonus |
| Beartic | 0.667% | 26–33 | National Dex bonus |
| Clawitzer | 0.667% | 26–33 | National Dex bonus |
| Horsea | 0.667% | 26–33 | National Dex bonus |
| Jynx | 0.667% | 26–33 | National Dex bonus |
| Lombre | 0.667% | 26–33 | National Dex bonus |
| Luvdisc | 0.667% | 26–33 | National Dex bonus |
| Mamoswine | 0.667% | 34 | National Dex bonus |
| Panpour | 0.667% | 26–33 | National Dex bonus |
| Primarina | 0.667% | 34 | National Dex bonus |
| Psyduck | 0.667% | 26–33 | National Dex bonus |
| Quagsire | 0.667% | 26–33 | National Dex bonus |
| Quaxwell | 0.667% | 26–33 | National Dex bonus |
| Veluza | 0.667% | 26–33 | National Dex bonus |
| Whiscash | 0.667% | 26–33 | National Dex bonus |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Zubat | 30.00% | 5–35 | Native / custom slot |
| Spheal | 10.00% | 25–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-89"></a>
## Shoal Cave Low Tide Lower Room

Source map: MAP_SHOAL_CAVE_LOW_TIDE_LOWER_ROOM.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Spheal | 45.00% | 26–32 | Native / custom slot |
| Zubat | 40.50% | 26–32 | Native / custom slot |
| Golbat | 4.50% | 32 | Native / custom slot |
| Arctovish | 0.667% | 26–32 | National Dex bonus |
| Bruxish | 0.667% | 26–32 | National Dex bonus |
| Buizel | 0.667% | 26–32 | National Dex bonus |
| Cetitan | 0.667% | 26–32 | National Dex bonus |
| Corphish | 0.667% | 26–32 | National Dex bonus |
| Feraligatr | 0.667% | 34 | National Dex bonus |
| Floatzel | 0.667% | 26–32 | National Dex bonus |
| Greninja | 0.667% | 34 | National Dex bonus |
| Ludicolo | 0.667% | 34 | National Dex bonus |
| Mr. Rime | 0.667% | 26–32 | National Dex bonus |
| Palpitoad | 0.667% | 26–32 | National Dex bonus |
| Politoed | 0.667% | 34 | National Dex bonus |
| Poliwrath | 0.667% | 34 | National Dex bonus |
| Slowpoke | 0.667% | 26–32 | National Dex bonus |
| Vanillish | 0.667% | 26–32 | National Dex bonus |

---

<a id="area-90"></a>
## Shoal Cave Low Tide Stairs Room

Source map: MAP_SHOAL_CAVE_LOW_TIDE_STAIRS_ROOM.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Spheal | 45.67% | 26–32 | National Dex bonus, Native / custom slot |
| Zubat | 40.50% | 26–32 | Native / custom slot |
| Golbat | 4.50% | 32 | Native / custom slot |
| Barraskewda | 0.667% | 26–32 | National Dex bonus |
| Bergmite | 0.667% | 26–32 | National Dex bonus |
| Cloyster | 0.667% | 26–32 | National Dex bonus |
| Corsola | 0.667% | 26–32 | National Dex bonus |
| Dracovish | 0.667% | 26–32 | National Dex bonus |
| Froslass | 0.667% | 26–32 | National Dex bonus |
| Inteleon | 0.667% | 34 | National Dex bonus |
| Lumineon | 0.667% | 26–32 | National Dex bonus |
| Sharpedo | 0.667% | 26–32 | National Dex bonus |
| Swampert | 0.667% | 34 | National Dex bonus |
| Tentacruel | 0.667% | 26–32 | National Dex bonus |
| Vanilluxe | 0.667% | 34 | National Dex bonus |
| Vaporeon | 0.667% | 26–32 | National Dex bonus |
| Wugtrio | 0.667% | 26–32 | National Dex bonus |

---

<a id="area-91"></a>
## Sky Pillar 1F

Source map: MAP_SKY_PILLAR_1F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 26.73% | 34–35 | Native / custom slot |
| Sableye | 26.73% | 33–34 | Native / custom slot |
| Banette | 13.37% | 37–38 | Native / custom slot |
| Claydol | 13.37% | 36–37 | Native / custom slot |
| Drakeon | 4.46% | 36–38 | Native / custom slot |
| Aerieon | 3.56% | 36–38 | Native / custom slot |
| Aerdrakeon | 0.891% | 39–40 | Native / custom slot |
| Arbok | 0.619% | 33–40 | National Dex bonus |
| Bagon | 0.619% | 33–40 | National Dex bonus |
| Cherrim | 0.619% | 33–40 | National Dex bonus |
| Darmanitan | 0.619% | 33–40 | National Dex bonus |
| Dodrio | 0.619% | 33–40 | National Dex bonus |
| Dragalge | 0.619% | 33–40 | National Dex bonus |
| Exploud | 0.619% | 34–40 | National Dex bonus |
| Flamigo | 0.619% | 33–40 | National Dex bonus |
| Fraxure | 0.619% | 33–40 | National Dex bonus |
| Gumshoos | 0.619% | 33–40 | National Dex bonus |
| Lickilicky | 0.619% | 33–40 | National Dex bonus |
| Maushold | 0.619% | 33–40 | National Dex bonus |
| Porygon2 | 0.619% | 33–40 | National Dex bonus |
| Roaring Moon | 0.619% | 33–40 | National Dex bonus |
| Silvally | 0.619% | 33–40 | National Dex bonus |
| Snorlax | 0.619% | 33–40 | National Dex bonus |
| Azelf | 0.100% | 45 | Rare bonus pool |
| Blacephalon | 0.100% | 45 | Rare bonus pool |
| Iron Crown | 0.100% | 45 | Rare bonus pool |
| Lunala | 0.100% | 45 | Rare bonus pool |
| Mew | 0.100% | 45 | Rare bonus pool |
| Pecharunt | 0.100% | 45 | Rare bonus pool |
| Phione | 0.100% | 45 | Rare bonus pool |
| Virizion | 0.100% | 45 | Rare bonus pool |
| Yveltal | 0.100% | 45 | Rare bonus pool |
| Zarude | 0.100% | 45 | Rare bonus pool |

---

<a id="area-92"></a>
## Sky Pillar 3F

Source map: MAP_SKY_PILLAR_3F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 26.73% | 34–35 | Native / custom slot |
| Sableye | 26.73% | 33–34 | Native / custom slot |
| Claydol | 20.49% | 36–38 | Native / custom slot |
| Banette | 13.37% | 37–38 | Native / custom slot |
| Aerfanteon | 0.891% | 39–41 | Native / custom slot |
| Draespeon | 0.891% | 39–41 | Native / custom slot |
| Aegislash | 0.619% | 33–41 | National Dex bonus |
| Baxcalibur | 0.619% | 34–41 | National Dex bonus |
| Bombirdier | 0.619% | 33–41 | National Dex bonus |
| Cinccino | 0.619% | 33–41 | National Dex bonus |
| Druddigon | 0.619% | 33–41 | National Dex bonus |
| Grimer | 0.619% | 33–41 | National Dex bonus |
| Indeedee | 0.619% | 33–41 | National Dex bonus |
| Lickitung | 0.619% | 33–41 | National Dex bonus |
| Loudred | 0.619% | 33–41 | National Dex bonus |
| Minior | 0.619% | 33–41 | National Dex bonus |
| Raticate | 0.619% | 33–41 | National Dex bonus |
| Shelgon | 0.619% | 33–41 | National Dex bonus |
| Skuntank | 0.619% | 33–41 | National Dex bonus |
| Stantler | 0.619% | 33–41 | National Dex bonus |
| Staraptor | 0.619% | 34–41 | National Dex bonus |
| Trumbeak | 0.619% | 33–41 | National Dex bonus |
| Articuno | 0.111% | 45 | Rare bonus pool |
| Genesect | 0.111% | 45 | Rare bonus pool |
| Guzzlord | 0.111% | 45 | Rare bonus pool |
| Heatran | 0.111% | 45 | Rare bonus pool |
| Iron Boulder | 0.111% | 45 | Rare bonus pool |
| Meltan | 0.111% | 45 | Rare bonus pool |
| Mesprit | 0.111% | 45 | Rare bonus pool |
| Tapu Bulu | 0.111% | 45 | Rare bonus pool |
| Wo Chien | 0.111% | 45 | Rare bonus pool |

---

<a id="area-93"></a>
## Sky Pillar 5F

Source map: MAP_SKY_PILLAR_5F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 26.73% | 34–35 | Native / custom slot |
| Sableye | 26.73% | 33–34 | Native / custom slot |
| Claydol | 16.93% | 36–37 | Native / custom slot |
| Banette | 13.37% | 37–38 | Native / custom slot |
| Altaria | 5.35% | 38–39 | Native / custom slot |
| Burmy | 0.619% | 33–39 | National Dex bonus |
| Castform | 0.619% | 33–39 | National Dex bonus |
| Dratini | 0.619% | 33–39 | National Dex bonus |
| Fletchling | 0.619% | 33–39 | National Dex bonus |
| Florges | 0.619% | 33–39 | National Dex bonus |
| Garbodor | 0.619% | 33–39 | National Dex bonus |
| Girafarig | 0.619% | 33–39 | National Dex bonus |
| Greedent | 0.619% | 33–39 | National Dex bonus |
| Lopunny | 0.619% | 33–39 | National Dex bonus |
| Nidorina | 0.619% | 33–39 | National Dex bonus |
| Oinkologne | 0.619% | 33–39 | National Dex bonus |
| Palafin | 0.619% | 33–39 | National Dex bonus |
| Poltchageist | 0.619% | 33–39 | National Dex bonus |
| Slaking | 0.619% | 34–39 | National Dex bonus |
| Sliggoo | 0.619% | 33–39 | National Dex bonus |
| Wigglytuff | 0.619% | 34–39 | National Dex bonus |
| Cosmog | 0.111% | 45 | Rare bonus pool |
| Cresselia | 0.111% | 45 | Rare bonus pool |
| Keldeo | 0.111% | 45 | Rare bonus pool |
| Koraidon | 0.111% | 45 | Rare bonus pool |
| Lugia | 0.111% | 45 | Rare bonus pool |
| Ogerpon | 0.111% | 45 | Rare bonus pool |
| Pheromosa | 0.111% | 45 | Rare bonus pool |
| Poipole | 0.111% | 45 | Rare bonus pool |
| Registeel | 0.111% | 45 | Rare bonus pool |

---

<a id="area-94"></a>
## Victory Road 1F

Source map: MAP_VICTORY_ROAD_1F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 22.27% | 38–40 | Native / custom slot |
| Hariyama | 22.27% | 38–40 | Native / custom slot |
| Lairon | 8.91% | 40 | Native / custom slot |
| Loudred | 8.91% | 40 | Native / custom slot |
| Makuhita | 8.91% | 36 | Native / custom slot |
| Zubat | 8.91% | 36 | Native / custom slot |
| Aron | 3.56% | 36 | Native / custom slot |
| Whismur | 3.56% | 36 | Native / custom slot |
| Aerartheon | 0.891% | 40–42 | Native / custom slot |
| Draferreon | 0.891% | 40–42 | Native / custom slot |
| Ampharos | 0.619% | 36–42 | National Dex bonus |
| Archeops | 0.619% | 36–42 | National Dex bonus |
| Cinderace | 0.619% | 36–42 | National Dex bonus |
| Dragapult | 0.619% | 36–42 | National Dex bonus |
| Eelektross | 0.619% | 36–42 | National Dex bonus |
| Gible | 0.619% | 36–42 | National Dex bonus |
| Hitmontop | 0.619% | 36–42 | National Dex bonus |
| Kabutops | 0.619% | 36–42 | National Dex bonus |
| Luxray | 0.619% | 36–42 | National Dex bonus |
| Magnemite | 0.619% | 36–42 | National Dex bonus |
| Minun | 0.619% | 36–42 | National Dex bonus |
| Pawmo | 0.619% | 36–42 | National Dex bonus |
| Raichu | 0.619% | 36–42 | National Dex bonus |
| Sandy Shocks | 0.619% | 36–42 | National Dex bonus |
| Talonflame | 0.619% | 36–42 | National Dex bonus |
| Torracat | 0.619% | 36–42 | National Dex bonus |
| Buzzwole | 0.111% | 45 | Rare bonus pool |
| Enamorus | 0.111% | 45 | Rare bonus pool |
| Meloetta | 0.111% | 45 | Rare bonus pool |
| Munkidori | 0.111% | 45 | Rare bonus pool |
| Shaymin | 0.111% | 45 | Rare bonus pool |
| Suicune | 0.111% | 45 | Rare bonus pool |
| Uxie | 0.111% | 45 | Rare bonus pool |
| Zeraora | 0.111% | 45 | Rare bonus pool |
| Zygarde | 0.111% | 45 | Rare bonus pool |

---

<a id="area-95"></a>
## Victory Road 1F Frlg

Source map: MAP_VICTORY_ROAD_1F_FRLG.

### Source variant 1: sVictoryRoad1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Onix | 30.00% | 40–46 | Native / custom slot |
| Geodude | 20.00% | 32 | Native / custom slot |
| Machop | 20.00% | 32 | Native / custom slot |
| Zubat | 10.00% | 32 | Native / custom slot |
| Arbok | 5.00% | 44 | Native / custom slot |
| Golbat | 5.00% | 44 | Native / custom slot |
| Machoke | 5.00% | 44–46 | Native / custom slot |
| Marowak | 5.00% | 44–46 | Native / custom slot |

### Source variant 2: sVictoryRoad1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Onix | 30.00% | 40–46 | Native / custom slot |
| Geodude | 20.00% | 32 | Native / custom slot |
| Machop | 20.00% | 32 | Native / custom slot |
| Zubat | 10.00% | 32 | Native / custom slot |
| Golbat | 5.00% | 44 | Native / custom slot |
| Machoke | 5.00% | 44–46 | Native / custom slot |
| Marowak | 5.00% | 44–46 | Native / custom slot |
| Sandslash | 5.00% | 44 | Native / custom slot |

---

<a id="area-96"></a>
## Victory Road 2F

Source map: MAP_VICTORY_ROAD_2F.

### Source variant 1: sVictoryRoad2F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 18.00% | 34 | Native / custom slot |
| Machop | 18.00% | 34 | Native / custom slot |
| Onix | 18.00% | 45–48 | Native / custom slot |
| Primeape | 9.00% | 42 | Native / custom slot |
| Zubat | 9.00% | 34 | Native / custom slot |
| Arbok | 4.50% | 46 | Native / custom slot |
| Golbat | 4.50% | 46 | Native / custom slot |
| Machoke | 4.50% | 46–48 | Native / custom slot |
| Marowak | 4.50% | 46–48 | Native / custom slot |
| Annihilape | 0.588% | 34–48 | National Dex bonus |
| Archaludon | 0.588% | 34–48 | National Dex bonus |
| Arctozolt | 0.588% | 34–48 | National Dex bonus |
| Delibird | 0.588% | 34–48 | National Dex bonus |
| Delphox | 0.588% | 34–48 | National Dex bonus |
| Emolga | 0.588% | 34–48 | National Dex bonus |
| Flareon | 0.588% | 34–48 | National Dex bonus |
| Gabite | 0.588% | 34–48 | National Dex bonus |
| Golem | 0.588% | 34–48 | National Dex bonus |
| Incineroar | 0.588% | 34–48 | National Dex bonus |
| Kommo O | 0.588% | 34–48 | National Dex bonus |
| Lunatone | 0.588% | 34–48 | National Dex bonus |
| Ninetales | 0.588% | 34–48 | National Dex bonus |
| Pansear | 0.588% | 34–48 | National Dex bonus |
| Salamence | 0.588% | 34–48 | National Dex bonus |
| Skeledirge | 0.588% | 34–48 | National Dex bonus |
| Typhlosion | 0.588% | 34–48 | National Dex bonus |

### Source variant 2: sVictoryRoad2F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 18.00% | 34 | Native / custom slot |
| Machop | 18.00% | 34 | Native / custom slot |
| Onix | 18.00% | 45–48 | Native / custom slot |
| Primeape | 9.00% | 42 | Native / custom slot |
| Zubat | 9.00% | 34 | Native / custom slot |
| Golbat | 4.50% | 46 | Native / custom slot |
| Machoke | 4.50% | 46–48 | Native / custom slot |
| Marowak | 4.50% | 46–48 | Native / custom slot |
| Sandslash | 4.50% | 46 | Native / custom slot |
| Annihilape | 0.588% | 34–48 | National Dex bonus |
| Archaludon | 0.588% | 34–48 | National Dex bonus |
| Arctozolt | 0.588% | 34–48 | National Dex bonus |
| Delibird | 0.588% | 34–48 | National Dex bonus |
| Delphox | 0.588% | 34–48 | National Dex bonus |
| Emolga | 0.588% | 34–48 | National Dex bonus |
| Flareon | 0.588% | 34–48 | National Dex bonus |
| Gabite | 0.588% | 34–48 | National Dex bonus |
| Golem | 0.588% | 34–48 | National Dex bonus |
| Incineroar | 0.588% | 34–48 | National Dex bonus |
| Kommo O | 0.588% | 34–48 | National Dex bonus |
| Lunatone | 0.588% | 34–48 | National Dex bonus |
| Ninetales | 0.588% | 34–48 | National Dex bonus |
| Pansear | 0.588% | 34–48 | National Dex bonus |
| Salamence | 0.588% | 34–48 | National Dex bonus |
| Skeledirge | 0.588% | 34–48 | National Dex bonus |
| Typhlosion | 0.588% | 34–48 | National Dex bonus |

---

<a id="area-97"></a>
## Victory Road 3F

Source map: MAP_VICTORY_ROAD_3F.

### Source variant 1: sVictoryRoad3F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Onix | 27.00% | 40–46 | Native / custom slot |
| Geodude | 18.00% | 32 | Native / custom slot |
| Machop | 18.00% | 32 | Native / custom slot |
| Zubat | 9.00% | 32 | Native / custom slot |
| Arbok | 4.50% | 44 | Native / custom slot |
| Golbat | 4.50% | 44 | Native / custom slot |
| Machoke | 4.50% | 44–46 | Native / custom slot |
| Marowak | 4.50% | 44–46 | Native / custom slot |
| Arcanine | 0.625% | 32–46 | National Dex bonus |
| Boldore | 0.625% | 32–46 | National Dex bonus |
| Cryogonal | 0.625% | 32–46 | National Dex bonus |
| Dragonite | 0.625% | 34–46 | National Dex bonus |
| Electabuzz | 0.625% | 32–46 | National Dex bonus |
| Heliolisk | 0.625% | 32–46 | National Dex bonus |
| Iron Moth | 0.625% | 32–46 | National Dex bonus |
| Magnezone | 0.625% | 34–46 | National Dex bonus |
| Passimian | 0.625% | 32–46 | National Dex bonus |
| Pikachu | 0.625% | 32–46 | National Dex bonus |
| Pupitar | 0.625% | 32–46 | National Dex bonus |
| Runerigus | 0.625% | 32–46 | National Dex bonus |
| Toedscruel | 0.625% | 32–46 | National Dex bonus |
| Toxel | 0.625% | 32–46 | National Dex bonus |
| Vibrava | 0.625% | 32–46 | National Dex bonus |
| Walrein | 0.625% | 34–46 | National Dex bonus |

### Source variant 2: sVictoryRoad3F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Onix | 27.00% | 40–46 | Native / custom slot |
| Geodude | 18.00% | 32 | Native / custom slot |
| Machop | 18.00% | 32 | Native / custom slot |
| Zubat | 9.00% | 32 | Native / custom slot |
| Golbat | 4.50% | 44 | Native / custom slot |
| Machoke | 4.50% | 44–46 | Native / custom slot |
| Marowak | 4.50% | 44–46 | Native / custom slot |
| Sandslash | 4.50% | 44 | Native / custom slot |
| Arcanine | 0.625% | 32–46 | National Dex bonus |
| Boldore | 0.625% | 32–46 | National Dex bonus |
| Cryogonal | 0.625% | 32–46 | National Dex bonus |
| Dragonite | 0.625% | 34–46 | National Dex bonus |
| Electabuzz | 0.625% | 32–46 | National Dex bonus |
| Heliolisk | 0.625% | 32–46 | National Dex bonus |
| Iron Moth | 0.625% | 32–46 | National Dex bonus |
| Magnezone | 0.625% | 34–46 | National Dex bonus |
| Passimian | 0.625% | 32–46 | National Dex bonus |
| Pikachu | 0.625% | 32–46 | National Dex bonus |
| Pupitar | 0.625% | 32–46 | National Dex bonus |
| Runerigus | 0.625% | 32–46 | National Dex bonus |
| Toedscruel | 0.625% | 32–46 | National Dex bonus |
| Toxel | 0.625% | 32–46 | National Dex bonus |
| Vibrava | 0.625% | 32–46 | National Dex bonus |
| Walrein | 0.625% | 34–46 | National Dex bonus |

---

<a id="area-98"></a>
## Victory Road B1F

Source map: MAP_VICTORY_ROAD_B1F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 31.18% | 38–42 | Native / custom slot |
| Hariyama | 31.18% | 38–42 | Native / custom slot |
| Lairon | 21.38% | 40–42 | Native / custom slot |
| Mawile | 3.56% | 38 | Native / custom slot |
| Draflareon | 0.891% | 41–43 | Native / custom slot |
| Dravapreon | 0.891% | 41–43 | Native / custom slot |
| Charmeleon | 0.619% | 38–43 | National Dex bonus |
| Cradily | 0.619% | 38–43 | National Dex bonus |
| Cubone | 0.619% | 38–43 | National Dex bonus |
| Electivire | 0.619% | 38–43 | National Dex bonus |
| Emboar | 0.619% | 38–43 | National Dex bonus |
| Great Tusk | 0.619% | 38–43 | National Dex bonus |
| Jolteon | 0.619% | 38–43 | National Dex bonus |
| Klinklang | 0.619% | 38–43 | National Dex bonus |
| Luxio | 0.619% | 38–43 | National Dex bonus |
| Magby | 0.619% | 38–43 | National Dex bonus |
| Mareep | 0.619% | 38–43 | National Dex bonus |
| Mudsdale | 0.619% | 38–43 | National Dex bonus |
| Pawmot | 0.619% | 38–43 | National Dex bonus |
| Pyroar | 0.619% | 38–43 | National Dex bonus |
| Sirfetch'd | 0.619% | 38–43 | National Dex bonus |
| Sizzlipede | 0.619% | 38–43 | National Dex bonus |
| Ho-Oh | 0.111% | 45 | Rare bonus pool |
| Jirachi | 0.111% | 45 | Rare bonus pool |
| Landorus | 0.111% | 45 | Rare bonus pool |
| Manaphy | 0.111% | 45 | Rare bonus pool |
| Marshadow | 0.111% | 45 | Rare bonus pool |
| Okidogi | 0.111% | 45 | Rare bonus pool |
| Spectrier | 0.111% | 45 | Rare bonus pool |
| Xerneas | 0.111% | 45 | Rare bonus pool |
| Zamazenta | 0.111% | 45 | Rare bonus pool |

### Rock Smash (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Graveler | 70.00% | 30–40 | Native / custom slot |
| Geodude | 30.00% | 30–40 | Native / custom slot |

---

<a id="area-99"></a>
## Victory Road B2F

Source map: MAP_VICTORY_ROAD_B2F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 31.18% | 40–44 | Native / custom slot |
| Sableye | 31.18% | 40–44 | Native / custom slot |
| Lairon | 21.38% | 40–42 | Native / custom slot |
| Mawile | 3.56% | 42 | Native / custom slot |
| Syldrakeon | 0.891% | 43–45 | Native / custom slot |
| Umbdrakeon | 0.891% | 43–45 | Native / custom slot |
| Armarouge | 0.619% | 40–45 | National Dex bonus |
| Barbaracle | 0.619% | 40–45 | National Dex bonus |
| Blaziken | 0.619% | 40–45 | National Dex bonus |
| Centiskorch | 0.619% | 40–45 | National Dex bonus |
| Charizard | 0.619% | 40–45 | National Dex bonus |
| Infernape | 0.619% | 40–45 | National Dex bonus |
| Iron Hands | 0.619% | 40–45 | National Dex bonus |
| Magcargo | 0.619% | 40–45 | National Dex bonus |
| Magmar | 0.619% | 40–45 | National Dex bonus |
| Magmortar | 0.619% | 40–45 | National Dex bonus |
| Onix | 0.619% | 40–45 | National Dex bonus |
| Pincurchin | 0.619% | 40–45 | National Dex bonus |
| Plusle | 0.619% | 40–45 | National Dex bonus |
| Riolu | 0.619% | 40–45 | National Dex bonus |
| Turtonator | 0.619% | 40–45 | National Dex bonus |
| Vanillite | 0.619% | 40–45 | National Dex bonus |
| Arceus | 0.111% | 45 | Rare bonus pool |
| Chien Pao | 0.111% | 45 | Rare bonus pool |
| Cobalion | 0.111% | 45 | Rare bonus pool |
| Hoopa | 0.111% | 45 | Rare bonus pool |
| Kartana | 0.111% | 45 | Rare bonus pool |
| Kubfu | 0.111% | 45 | Rare bonus pool |
| Raikou | 0.111% | 45 | Rare bonus pool |
| Rayquaza | 0.111% | 45 | Rare bonus pool |
| Terapagos | 0.111% | 45 | Rare bonus pool |

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 100.00% | 25–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Goldeen | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Barboach | 20.00% | 10–30 | Native / custom slot |
| Goldeen | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 30)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Barboach | 80.00% | 25–35 | Native / custom slot |
| Whiscash | 20.00% | 30–45 | Native / custom slot |

---

<a id="area-100"></a>
## Abandoned Ship Hidden Floor Corridors

Source map: MAP_ABANDONED_SHIP_HIDDEN_FLOOR_CORRIDORS.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 99.00% | 5–35 | Native / custom slot |
| Tentacruel | 1.00% | 30–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 40.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 80.00% | 25–35 | Native / custom slot |
| Tentacruel | 20.00% | 20–35 | Native / custom slot |

---

<a id="area-101"></a>
## Abandoned Ship Rooms B1F

Source map: MAP_ABANDONED_SHIP_ROOMS_B1F.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 99.00% | 5–35 | Native / custom slot |
| Tentacruel | 1.00% | 30–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 40.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 80.00% | 25–35 | Native / custom slot |
| Tentacruel | 20.00% | 20–35 | Native / custom slot |

---

<a id="area-102"></a>
## Altering Cave

Source map: MAP_ALTERING_CAVE.

### Source variant 1: gAlteringCave1

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 100.00% | 6–16 | Native / custom slot |

### Source variant 2: gAlteringCave2

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Mareep | 100.00% | 3–13 | Native / custom slot |

### Source variant 3: gAlteringCave3

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pineco | 100.00% | 19–29 | Native / custom slot |

### Source variant 4: gAlteringCave4

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Houndour | 100.00% | 12–22 | Native / custom slot |

### Source variant 5: gAlteringCave5

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Teddiursa | 100.00% | 6–16 | Native / custom slot |

### Source variant 6: gAlteringCave6

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Aipom | 100.00% | 18–28 | Native / custom slot |

### Source variant 7: gAlteringCave7

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuckle | 100.00% | 18–28 | Native / custom slot |

### Source variant 8: gAlteringCave8

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Stantler | 100.00% | 18–28 | Native / custom slot |

### Source variant 9: gAlteringCave9

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Smeargle | 100.00% | 18–28 | Native / custom slot |

---

<a id="area-103"></a>
## Cave Of Origin 1F

Source map: MAP_CAVE_OF_ORIGIN_1F.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 60.00% | 30–34 | Native / custom slot |
| Sableye | 30.00% | 30–34 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

---

<a id="area-104"></a>
## Cave Of Origin Entrance

Source map: MAP_CAVE_OF_ORIGIN_ENTRANCE.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 90.00% | 28–35 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

---

<a id="area-105"></a>
## Cave Of Origin Unused Ruby Sapphire Map1

Source map: MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP1.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 60.00% | 30–34 | Native / custom slot |
| Sableye | 30.00% | 30–34 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

---

<a id="area-106"></a>
## Cave Of Origin Unused Ruby Sapphire Map2

Source map: MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP2.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 60.00% | 30–34 | Native / custom slot |
| Sableye | 30.00% | 30–34 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

---

<a id="area-107"></a>
## Cave Of Origin Unused Ruby Sapphire Map3

Source map: MAP_CAVE_OF_ORIGIN_UNUSED_RUBY_SAPPHIRE_MAP3.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 60.00% | 30–34 | Native / custom slot |
| Sableye | 30.00% | 30–34 | Native / custom slot |
| Golbat | 10.00% | 33–36 | Native / custom slot |

---

<a id="area-108"></a>
## Celadon City

Source map: MAP_CELADON_CITY.

### Source variant 1: sCeladonCity_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 99.00% | 5–40 | Native / custom slot |
| Koffing | 1.00% | 30–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 99.00% | 15–35 | Native / custom slot |
| Grimer | 1.00% | 30–40 | Native / custom slot |

### Source variant 2: sCeladonCity_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 99.00% | 5–40 | Native / custom slot |
| Koffing | 1.00% | 30–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 99.00% | 15–35 | Native / custom slot |
| Grimer | 1.00% | 30–40 | Native / custom slot |

---

<a id="area-109"></a>
## Cerulean Cave 1F

Source map: MAP_CERULEAN_CAVE_1F.

### Source variant 1: sCeruleanCave1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Parasect | 25.00% | 49–58 | Native / custom slot |
| Magneton | 20.00% | 49 | Native / custom slot |
| Golbat | 14.00% | 46–55 | Native / custom slot |
| Ditto | 11.00% | 52–61 | Native / custom slot |
| Primeape | 11.00% | 52–61 | Native / custom slot |
| Machoke | 10.00% | 46 | Native / custom slot |
| Electrode | 5.00% | 58 | Native / custom slot |
| Wobbuffet | 4.00% | 55 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 65.00% | 30–50 | Native / custom slot |
| Golduck | 35.00% | 40–55 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 30–50 | Native / custom slot |
| Graveler | 35.00% | 40–55 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sCeruleanCave1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Parasect | 25.00% | 49–58 | Native / custom slot |
| Magneton | 20.00% | 49 | Native / custom slot |
| Golbat | 14.00% | 46–55 | Native / custom slot |
| Ditto | 11.00% | 52–61 | Native / custom slot |
| Primeape | 11.00% | 52–61 | Native / custom slot |
| Machoke | 10.00% | 46 | Native / custom slot |
| Electrode | 5.00% | 58 | Native / custom slot |
| Wobbuffet | 4.00% | 55 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 65.00% | 30–50 | Native / custom slot |
| Slowbro | 35.00% | 40–55 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 30–50 | Native / custom slot |
| Graveler | 35.00% | 40–55 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-110"></a>
## Cerulean Cave 2F

Source map: MAP_CERULEAN_CAVE_2F.

### Source variant 1: sCeruleanCave2F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 25.00% | 49–58 | Native / custom slot |
| Machoke | 20.00% | 49 | Native / custom slot |
| Parasect | 14.00% | 52–61 | Native / custom slot |
| Ditto | 11.00% | 55–64 | Native / custom slot |
| Kadabra | 11.00% | 55–64 | Native / custom slot |
| Magneton | 10.00% | 52 | Native / custom slot |
| Wobbuffet | 5.00% | 58 | Native / custom slot |
| Electrode | 4.00% | 61 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 35–55 | Native / custom slot |
| Graveler | 35.00% | 45–60 | Native / custom slot |

### Source variant 2: sCeruleanCave2F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Golbat | 25.00% | 49–58 | Native / custom slot |
| Machoke | 20.00% | 49 | Native / custom slot |
| Parasect | 14.00% | 52–61 | Native / custom slot |
| Ditto | 11.00% | 55–64 | Native / custom slot |
| Kadabra | 11.00% | 55–64 | Native / custom slot |
| Magneton | 10.00% | 52 | Native / custom slot |
| Wobbuffet | 5.00% | 58 | Native / custom slot |
| Electrode | 4.00% | 61 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 35–55 | Native / custom slot |
| Graveler | 35.00% | 45–60 | Native / custom slot |

---

<a id="area-111"></a>
## Cerulean Cave B1F

Source map: MAP_CERULEAN_CAVE_B1F.

### Source variant 1: sCeruleanCaveB1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Ditto | 25.00% | 58–67 | Native / custom slot |
| Kadabra | 25.00% | 58–67 | Native / custom slot |
| Parasect | 14.00% | 55–64 | Native / custom slot |
| Golbat | 11.00% | 52–61 | Native / custom slot |
| Machoke | 10.00% | 52 | Native / custom slot |
| Magneton | 10.00% | 55 | Native / custom slot |
| Electrode | 4.00% | 64 | Native / custom slot |
| Wobbuffet | 1.00% | 61 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 65.00% | 40–60 | Native / custom slot |
| Golduck | 35.00% | 50–65 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 40–60 | Native / custom slot |
| Graveler | 35.00% | 50–65 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 16.00% | 15–35 | Native / custom slot |
| Psyduck | 4.00% | 15–25 | Native / custom slot |

### Source variant 2: sCeruleanCaveB1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Ditto | 25.00% | 58–67 | Native / custom slot |
| Kadabra | 25.00% | 58–67 | Native / custom slot |
| Parasect | 14.00% | 55–64 | Native / custom slot |
| Golbat | 11.00% | 52–61 | Native / custom slot |
| Machoke | 10.00% | 52 | Native / custom slot |
| Magneton | 10.00% | 55 | Native / custom slot |
| Electrode | 4.00% | 64 | Native / custom slot |
| Wobbuffet | 1.00% | 61 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 65.00% | 40–60 | Native / custom slot |
| Slowbro | 35.00% | 50–65 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 40–60 | Native / custom slot |
| Graveler | 35.00% | 50–65 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 16.00% | 15–35 | Native / custom slot |
| Slowpoke | 4.00% | 15–25 | Native / custom slot |

---

<a id="area-112"></a>
## Cerulean City

Source map: MAP_CERULEAN_CITY.

### Source variant 1: sCeruleanCity_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sCeruleanCity_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-113"></a>
## Cinnabar Island

Source map: MAP_CINNABAR_ISLAND.

### Source variant 1: sCinnabarIsland_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Shellder | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sCinnabarIsland_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Staryu | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowbro | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-114"></a>
## Dewford Town

Source map: MAP_DEWFORD_TOWN.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-115"></a>
## Digletts Cave B1F

Source map: MAP_DIGLETTS_CAVE_B1F.

### Source variant 1: sDiglettsCaveB1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Diglett | 95.00% | 15–22 | Native / custom slot |
| Dugtrio | 5.00% | 29–31 | Native / custom slot |

### Source variant 2: sDiglettsCaveB1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Diglett | 95.00% | 15–22 | Native / custom slot |
| Dugtrio | 5.00% | 29–31 | Native / custom slot |

---

<a id="area-116"></a>
## Five Island

Source map: MAP_FIVE_ISLAND.

### Source variant 1: sFiveIsland_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 65.00% | 5–40 | Native / custom slot |
| Hoppip | 30.00% | 5–15 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Shellder | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sFiveIsland_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 65.00% | 5–40 | Native / custom slot |
| Hoppip | 30.00% | 5–15 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Staryu | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-117"></a>
## Five Island Lost Cave Room1

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM1.

### Source variant 1: sFiveIslandLostCaveRoom1_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Murkrow | 5.00% | 22 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom1_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Misdreavus | 5.00% | 22 | Native / custom slot |

---

<a id="area-118"></a>
## Five Island Lost Cave Room10

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM10.

### Source variant 1: sFiveIslandLostCaveRoom10_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Murkrow | 5.00% | 22 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom10_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Misdreavus | 5.00% | 22 | Native / custom slot |

---

<a id="area-119"></a>
## Five Island Lost Cave Room11

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM11.

### Source variant 1: sFiveIslandLostCaveRoom11_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 20.00% | 40 | Native / custom slot |
| Murkrow | 20.00% | 15–22 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Golbat | 10.00% | 41 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom11_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 20.00% | 40 | Native / custom slot |
| Misdreavus | 20.00% | 15–22 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Golbat | 10.00% | 41 | Native / custom slot |

---

<a id="area-120"></a>
## Five Island Lost Cave Room12

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM12.

### Source variant 1: sFiveIslandLostCaveRoom12_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 20.00% | 40 | Native / custom slot |
| Murkrow | 20.00% | 15–22 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Golbat | 10.00% | 41 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom12_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 20.00% | 40 | Native / custom slot |
| Misdreavus | 20.00% | 15–22 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Golbat | 10.00% | 41 | Native / custom slot |

---

<a id="area-121"></a>
## Five Island Lost Cave Room13

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM13.

### Source variant 1: sFiveIslandLostCaveRoom13_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 20.00% | 40 | Native / custom slot |
| Murkrow | 20.00% | 15–22 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Golbat | 10.00% | 41 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom13_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 20.00% | 40 | Native / custom slot |
| Misdreavus | 20.00% | 15–22 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Golbat | 10.00% | 41 | Native / custom slot |

---

<a id="area-122"></a>
## Five Island Lost Cave Room14

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM14.

### Source variant 1: sFiveIslandLostCaveRoom14_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 20.00% | 40 | Native / custom slot |
| Murkrow | 20.00% | 15–22 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Golbat | 10.00% | 41 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom14_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 20.00% | 40 | Native / custom slot |
| Misdreavus | 20.00% | 15–22 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Golbat | 10.00% | 41 | Native / custom slot |

---

<a id="area-123"></a>
## Five Island Lost Cave Room2

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM2.

### Source variant 1: sFiveIslandLostCaveRoom2_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Murkrow | 5.00% | 22 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom2_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Misdreavus | 5.00% | 22 | Native / custom slot |

---

<a id="area-124"></a>
## Five Island Lost Cave Room3

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM3.

### Source variant 1: sFiveIslandLostCaveRoom3_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 3)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Murkrow | 5.00% | 22 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom3_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 3)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Misdreavus | 5.00% | 22 | Native / custom slot |

---

<a id="area-125"></a>
## Five Island Lost Cave Room4

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM4.

### Source variant 1: sFiveIslandLostCaveRoom4_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Murkrow | 5.00% | 22 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom4_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Misdreavus | 5.00% | 22 | Native / custom slot |

---

<a id="area-126"></a>
## Five Island Lost Cave Room5

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM5.

### Source variant 1: sFiveIslandLostCaveRoom5_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Murkrow | 5.00% | 22 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom5_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Misdreavus | 5.00% | 22 | Native / custom slot |

---

<a id="area-127"></a>
## Five Island Lost Cave Room6

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM6.

### Source variant 1: sFiveIslandLostCaveRoom6_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 6)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Murkrow | 5.00% | 22 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom6_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 6)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Misdreavus | 5.00% | 22 | Native / custom slot |

---

<a id="area-128"></a>
## Five Island Lost Cave Room7

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM7.

### Source variant 1: sFiveIslandLostCaveRoom7_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Murkrow | 5.00% | 22 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom7_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Misdreavus | 5.00% | 22 | Native / custom slot |

---

<a id="area-129"></a>
## Five Island Lost Cave Room8

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM8.

### Source variant 1: sFiveIslandLostCaveRoom8_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 8)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Murkrow | 5.00% | 22 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom8_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 8)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Misdreavus | 5.00% | 22 | Native / custom slot |

---

<a id="area-130"></a>
## Five Island Lost Cave Room9

Source map: MAP_FIVE_ISLAND_LOST_CAVE_ROOM9.

### Source variant 1: sFiveIslandLostCaveRoom9_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 9)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Murkrow | 5.00% | 22 | Native / custom slot |

### Source variant 2: sFiveIslandLostCaveRoom9_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 9)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Haunter | 30.00% | 44–52 | Native / custom slot |
| Gastly | 25.00% | 38–40 | Native / custom slot |
| Golbat | 20.00% | 41–43 | Native / custom slot |
| Zubat | 20.00% | 37 | Native / custom slot |
| Misdreavus | 5.00% | 22 | Native / custom slot |

---

<a id="area-131"></a>
## Five Island Meadow

Source map: MAP_FIVE_ISLAND_MEADOW.

### Source variant 1: sFiveIslandMeadow_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sentret | 30.00% | 10–15 | Native / custom slot |
| Pidgey | 20.00% | 44 | Native / custom slot |
| Hoppip | 15.00% | 10–15 | Native / custom slot |
| Pidgeotto | 15.00% | 48–50 | Native / custom slot |
| Meowth | 10.00% | 41 | Native / custom slot |
| Persian | 5.00% | 47–50 | Native / custom slot |
| Psyduck | 5.00% | 41 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 65.00% | 5–40 | Native / custom slot |
| Hoppip | 30.00% | 5–15 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Qwilfish | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sFiveIslandMeadow_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sentret | 30.00% | 10–15 | Native / custom slot |
| Pidgey | 20.00% | 44 | Native / custom slot |
| Hoppip | 15.00% | 10–15 | Native / custom slot |
| Pidgeotto | 15.00% | 48–50 | Native / custom slot |
| Meowth | 10.00% | 41 | Native / custom slot |
| Persian | 5.00% | 47–50 | Native / custom slot |
| Slowpoke | 5.00% | 41 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 65.00% | 5–40 | Native / custom slot |
| Hoppip | 30.00% | 5–15 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Remoraid | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-132"></a>
## Five Island Memorial Pillar

Source map: MAP_FIVE_ISLAND_MEMORIAL_PILLAR.

### Source variant 1: sFiveIslandMemorialPillar_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Hoppip | 100.00% | 6–16 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 65.00% | 5–40 | Native / custom slot |
| Hoppip | 30.00% | 5–15 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Qwilfish | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sFiveIslandMemorialPillar_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Hoppip | 100.00% | 6–16 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 65.00% | 5–40 | Native / custom slot |
| Hoppip | 30.00% | 5–15 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Remoraid | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-133"></a>
## Five Island Resort Gorgeous

Source map: MAP_FIVE_ISLAND_RESORT_GORGEOUS.

### Source variant 1: sFiveIslandResortGorgeous_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 65.00% | 5–40 | Native / custom slot |
| Hoppip | 30.00% | 5–15 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Qwilfish | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sFiveIslandResortGorgeous_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 65.00% | 5–40 | Native / custom slot |
| Hoppip | 30.00% | 5–15 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Remoraid | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-134"></a>
## Five Island Water Labyrinth

Source map: MAP_FIVE_ISLAND_WATER_LABYRINTH.

### Source variant 1: sFiveIslandWaterLabyrinth_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 65.00% | 5–40 | Native / custom slot |
| Hoppip | 30.00% | 5–15 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Qwilfish | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sFiveIslandWaterLabyrinth_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 65.00% | 5–40 | Native / custom slot |
| Hoppip | 30.00% | 5–15 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Remoraid | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-135"></a>
## Four Island

Source map: MAP_FOUR_ISLAND.

### Source variant 1: sFourIsland_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wooper | 70.00% | 5–25 | Native / custom slot |
| Psyduck | 30.00% | 5–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sFourIsland_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Marill | 70.00% | 5–25 | Native / custom slot |
| Slowpoke | 30.00% | 5–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-136"></a>
## Four Island Icefall Cave 1F

Source map: MAP_FOUR_ISLAND_ICEFALL_CAVE_1F.

### Source variant 1: sFourIslandIcefallCave1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Swinub | 50.00% | 23–31 | Native / custom slot |
| Golbat | 25.00% | 45–48 | Native / custom slot |
| Seel | 10.00% | 45 | Native / custom slot |
| Zubat | 10.00% | 40 | Native / custom slot |
| Delibird | 5.00% | 30 | Native / custom slot |

### Source variant 2: sFourIslandIcefallCave1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Swinub | 50.00% | 23–31 | Native / custom slot |
| Golbat | 25.00% | 45–48 | Native / custom slot |
| Seel | 10.00% | 45 | Native / custom slot |
| Zubat | 10.00% | 40 | Native / custom slot |
| Sneasel | 5.00% | 30 | Native / custom slot |

---

<a id="area-137"></a>
## Four Island Icefall Cave B1F

Source map: MAP_FOUR_ISLAND_ICEFALL_CAVE_B1F.

### Source variant 1: sFourIslandIcefallCaveB1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Swinub | 50.00% | 23–31 | Native / custom slot |
| Golbat | 25.00% | 45–48 | Native / custom slot |
| Seel | 10.00% | 45 | Native / custom slot |
| Zubat | 10.00% | 40 | Native / custom slot |
| Delibird | 5.00% | 30 | Native / custom slot |

### Source variant 2: sFourIslandIcefallCaveB1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Swinub | 50.00% | 23–31 | Native / custom slot |
| Golbat | 25.00% | 45–48 | Native / custom slot |
| Seel | 10.00% | 45 | Native / custom slot |
| Zubat | 10.00% | 40 | Native / custom slot |
| Sneasel | 5.00% | 30 | Native / custom slot |

---

<a id="area-138"></a>
## Four Island Icefall Cave Back

Source map: MAP_FOUR_ISLAND_ICEFALL_CAVE_BACK.

### Source variant 1: sFourIslandIcefallCaveBack_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 40.00% | 43–47 | Native / custom slot |
| Golbat | 25.00% | 45–48 | Native / custom slot |
| Dewgong | 20.00% | 49–53 | Native / custom slot |
| Zubat | 10.00% | 40 | Native / custom slot |
| Psyduck | 5.00% | 41 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–45 | Native / custom slot |
| Tentacruel | 4.00% | 35–45 | Native / custom slot |
| Lapras | 1.00% | 30–45 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Shellder | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sFourIslandIcefallCaveBack_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 40.00% | 43–47 | Native / custom slot |
| Golbat | 25.00% | 45–48 | Native / custom slot |
| Dewgong | 20.00% | 49–53 | Native / custom slot |
| Zubat | 10.00% | 40 | Native / custom slot |
| Slowpoke | 5.00% | 41 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–45 | Native / custom slot |
| Tentacruel | 4.00% | 35–45 | Native / custom slot |
| Lapras | 1.00% | 30–45 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Staryu | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-139"></a>
## Four Island Icefall Cave Entrance

Source map: MAP_FOUR_ISLAND_ICEFALL_CAVE_ENTRANCE.

### Source variant 1: sFourIslandIcefallCaveEntrance_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 40.00% | 43–47 | Native / custom slot |
| Golbat | 25.00% | 45–48 | Native / custom slot |
| Dewgong | 20.00% | 49–53 | Native / custom slot |
| Zubat | 10.00% | 40 | Native / custom slot |
| Psyduck | 5.00% | 41 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 60.00% | 5–35 | Native / custom slot |
| Psyduck | 30.00% | 5–35 | Native / custom slot |
| Dewgong | 5.00% | 35–40 | Native / custom slot |
| Wooper | 5.00% | 5–15 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sFourIslandIcefallCaveEntrance_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 40.00% | 43–47 | Native / custom slot |
| Golbat | 25.00% | 45–48 | Native / custom slot |
| Dewgong | 20.00% | 49–53 | Native / custom slot |
| Zubat | 10.00% | 40 | Native / custom slot |
| Slowpoke | 5.00% | 41 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 60.00% | 5–35 | Native / custom slot |
| Slowpoke | 30.00% | 5–35 | Native / custom slot |
| Dewgong | 5.00% | 35–40 | Native / custom slot |
| Marill | 5.00% | 5–15 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-140"></a>
## Fuchsia City

Source map: MAP_FUCHSIA_CITY.

### Source variant 1: sFuchsiaCity_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sFuchsiaCity_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-141"></a>
## Lilycove City

Source map: MAP_LILYCOVE_CITY.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 85.00% | 25–45 | Native / custom slot |
| Staryu | 15.00% | 25–30 | Native / custom slot |

---

<a id="area-142"></a>
## Magma Hideout 1F

Source map: MAP_MAGMA_HIDEOUT_1F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 55.00% | 27–30 | Native / custom slot |
| Torkoal | 30.00% | 28–30 | Native / custom slot |
| Graveler | 15.00% | 30–33 | Native / custom slot |

---

<a id="area-143"></a>
## Magma Hideout 2F 1R

Source map: MAP_MAGMA_HIDEOUT_2F_1R.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 55.00% | 27–30 | Native / custom slot |
| Torkoal | 30.00% | 28–30 | Native / custom slot |
| Graveler | 15.00% | 30–33 | Native / custom slot |

---

<a id="area-144"></a>
## Magma Hideout 2F 2R

Source map: MAP_MAGMA_HIDEOUT_2F_2R.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 55.00% | 27–30 | Native / custom slot |
| Torkoal | 30.00% | 28–30 | Native / custom slot |
| Graveler | 15.00% | 30–33 | Native / custom slot |

---

<a id="area-145"></a>
## Magma Hideout 2F 3R

Source map: MAP_MAGMA_HIDEOUT_2F_3R.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 55.00% | 27–30 | Native / custom slot |
| Torkoal | 30.00% | 28–30 | Native / custom slot |
| Graveler | 15.00% | 30–33 | Native / custom slot |

---

<a id="area-146"></a>
## Magma Hideout 3F 1R

Source map: MAP_MAGMA_HIDEOUT_3F_1R.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 55.00% | 27–30 | Native / custom slot |
| Torkoal | 30.00% | 28–30 | Native / custom slot |
| Graveler | 15.00% | 30–33 | Native / custom slot |

---

<a id="area-147"></a>
## Magma Hideout 3F 2R

Source map: MAP_MAGMA_HIDEOUT_3F_2R.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 55.00% | 27–30 | Native / custom slot |
| Torkoal | 30.00% | 28–30 | Native / custom slot |
| Graveler | 15.00% | 30–33 | Native / custom slot |

---

<a id="area-148"></a>
## Magma Hideout 3F 3R

Source map: MAP_MAGMA_HIDEOUT_3F_3R.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 55.00% | 27–30 | Native / custom slot |
| Torkoal | 30.00% | 28–30 | Native / custom slot |
| Graveler | 15.00% | 30–33 | Native / custom slot |

---

<a id="area-149"></a>
## Magma Hideout 4F

Source map: MAP_MAGMA_HIDEOUT_4F.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 55.00% | 27–30 | Native / custom slot |
| Torkoal | 30.00% | 28–30 | Native / custom slot |
| Graveler | 15.00% | 30–33 | Native / custom slot |

---

<a id="area-150"></a>
## Mt. Ember Exterior

Source map: MAP_MT_EMBER_EXTERIOR.

### Source variant 1: sMtEmberExterior_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Ponyta | 35.00% | 30–36 | Native / custom slot |
| Fearow | 25.00% | 38–40 | Native / custom slot |
| Spearow | 15.00% | 30–32 | Native / custom slot |
| Geodude | 10.00% | 33 | Native / custom slot |
| Machop | 10.00% | 35 | Native / custom slot |
| Rapidash | 5.00% | 39–42 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 95.00% | 5–30 | Native / custom slot |
| Graveler | 5.00% | 25–40 | Native / custom slot |

### Source variant 2: sMtEmberExterior_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Ponyta | 35.00% | 30–36 | Native / custom slot |
| Fearow | 25.00% | 38–40 | Native / custom slot |
| Geodude | 10.00% | 33 | Native / custom slot |
| Machop | 10.00% | 35 | Native / custom slot |
| Spearow | 10.00% | 32 | Native / custom slot |
| Magmar | 5.00% | 38–40 | Native / custom slot |
| Rapidash | 5.00% | 39–42 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 95.00% | 5–30 | Native / custom slot |
| Graveler | 5.00% | 25–40 | Native / custom slot |

---

<a id="area-151"></a>
## Mt. Ember Ruby Path 1F

Source map: MAP_MT_EMBER_RUBY_PATH_1F.

### Source variant 1: sMtEmberRubyPath1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 50.00% | 32–40 | Native / custom slot |
| Machop | 40.00% | 34–38 | Native / custom slot |
| Machoke | 10.00% | 40–42 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

### Source variant 2: sMtEmberRubyPath1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 50.00% | 32–40 | Native / custom slot |
| Machop | 40.00% | 34–38 | Native / custom slot |
| Machoke | 10.00% | 40–42 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

---

<a id="area-152"></a>
## Mt. Ember Ruby Path B1F

Source map: MAP_MT_EMBER_RUBY_PATH_B1F.

### Source variant 1: sMtEmberRubyPathB1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 70.00% | 34–42 | Native / custom slot |
| Slugma | 30.00% | 24–30 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

### Source variant 2: sMtEmberRubyPathB1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 70.00% | 34–42 | Native / custom slot |
| Slugma | 30.00% | 24–30 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

---

<a id="area-153"></a>
## Mt. Ember Ruby Path B1F Stairs

Source map: MAP_MT_EMBER_RUBY_PATH_B1F_STAIRS.

### Source variant 1: sMtEmberRubyPathB1FStairs_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slugma | 60.00% | 22–32 | Native / custom slot |
| Geodude | 40.00% | 40–44 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

### Source variant 2: sMtEmberRubyPathB1FStairs_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slugma | 60.00% | 22–32 | Native / custom slot |
| Geodude | 40.00% | 40–44 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

---

<a id="area-154"></a>
## Mt. Ember Ruby Path B2F

Source map: MAP_MT_EMBER_RUBY_PATH_B2F.

### Source variant 1: sMtEmberRubyPathB2F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slugma | 60.00% | 22–32 | Native / custom slot |
| Geodude | 40.00% | 40–44 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

### Source variant 2: sMtEmberRubyPathB2F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slugma | 60.00% | 22–32 | Native / custom slot |
| Geodude | 40.00% | 40–44 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

---

<a id="area-155"></a>
## Mt. Ember Ruby Path B2F Stairs

Source map: MAP_MT_EMBER_RUBY_PATH_B2F_STAIRS.

### Source variant 1: sMtEmberRubyPathB2FStairs_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 70.00% | 34–42 | Native / custom slot |
| Slugma | 30.00% | 24–30 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

### Source variant 2: sMtEmberRubyPathB2FStairs_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 70.00% | 34–42 | Native / custom slot |
| Slugma | 30.00% | 24–30 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

---

<a id="area-156"></a>
## Mt. Ember Ruby Path B3F

Source map: MAP_MT_EMBER_RUBY_PATH_B3F.

### Source variant 1: sMtEmberRubyPathB3F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slugma | 100.00% | 18–36 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slugma | 90.00% | 15–35 | Native / custom slot |
| Magcargo | 10.00% | 25–45 | Native / custom slot |

### Source variant 2: sMtEmberRubyPathB3F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slugma | 100.00% | 18–36 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slugma | 90.00% | 15–35 | Native / custom slot |
| Magcargo | 10.00% | 25–45 | Native / custom slot |

---

<a id="area-157"></a>
## Mt. Ember Summit Path 1F

Source map: MAP_MT_EMBER_SUMMIT_PATH_1F.

### Source variant 1: sMtEmberSummitPath1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 50.00% | 29–37 | Native / custom slot |
| Machop | 50.00% | 31–39 | Native / custom slot |

### Source variant 2: sMtEmberSummitPath1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 50.00% | 29–37 | Native / custom slot |
| Machop | 50.00% | 31–39 | Native / custom slot |

---

<a id="area-158"></a>
## Mt. Ember Summit Path 2F

Source map: MAP_MT_EMBER_SUMMIT_PATH_2F.

### Source variant 1: sMtEmberSummitPath2F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 40.00% | 30–34 | Native / custom slot |
| Machop | 40.00% | 32–36 | Native / custom slot |
| Machoke | 20.00% | 38–40 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 95.00% | 5–30 | Native / custom slot |
| Graveler | 5.00% | 25–40 | Native / custom slot |

### Source variant 2: sMtEmberSummitPath2F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 40.00% | 30–34 | Native / custom slot |
| Machop | 40.00% | 32–36 | Native / custom slot |
| Machoke | 20.00% | 38–40 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 95.00% | 5–30 | Native / custom slot |
| Graveler | 5.00% | 25–40 | Native / custom slot |

---

<a id="area-159"></a>
## Mt. Ember Summit Path 3F

Source map: MAP_MT_EMBER_SUMMIT_PATH_3F.

### Source variant 1: sMtEmberSummitPath3F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 50.00% | 29–37 | Native / custom slot |
| Machop | 50.00% | 31–39 | Native / custom slot |

### Source variant 2: sMtEmberSummitPath3F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 50.00% | 29–37 | Native / custom slot |
| Machop | 50.00% | 31–39 | Native / custom slot |

---

<a id="area-160"></a>
## Mt. Moon 1F

Source map: MAP_MT_MOON_1F.

### Source variant 1: sMtMoon1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 69.00% | 7–10 | Native / custom slot |
| Geodude | 25.00% | 7–9 | Native / custom slot |
| Paras | 5.00% | 8 | Native / custom slot |
| Clefairy | 1.00% | 8 | Native / custom slot |

### Source variant 2: sMtMoon1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 69.00% | 7–10 | Native / custom slot |
| Geodude | 25.00% | 7–9 | Native / custom slot |
| Paras | 5.00% | 8 | Native / custom slot |
| Clefairy | 1.00% | 8 | Native / custom slot |

---

<a id="area-161"></a>
## Mt. Moon B1F

Source map: MAP_MT_MOON_B1F.

### Source variant 1: sMtMoonB1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Paras | 100.00% | 5–10 | Native / custom slot |

### Source variant 2: sMtMoonB1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Paras | 100.00% | 5–10 | Native / custom slot |

---

<a id="area-162"></a>
## Mt. Moon B2F

Source map: MAP_MT_MOON_B2F.

### Source variant 1: sMtMoonB2F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 49.00% | 8–11 | Native / custom slot |
| Geodude | 30.00% | 9–10 | Native / custom slot |
| Paras | 15.00% | 10–12 | Native / custom slot |
| Clefairy | 6.00% | 10–12 | Native / custom slot |

### Source variant 2: sMtMoonB2F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 49.00% | 8–11 | Native / custom slot |
| Geodude | 30.00% | 9–10 | Native / custom slot |
| Paras | 15.00% | 10–12 | Native / custom slot |
| Clefairy | 6.00% | 10–12 | Native / custom slot |

---

<a id="area-163"></a>
## One Island

Source map: MAP_ONE_ISLAND.

### Source variant 1: sOneIsland_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Shellder | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sOneIsland_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Staryu | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-164"></a>
## One Island Kindle Road

Source map: MAP_ONE_ISLAND_KINDLE_ROAD.

### Source variant 1: sOneIslandKindleRoad_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Ponyta | 30.00% | 31–34 | Native / custom slot |
| Spearow | 25.00% | 30–32 | Native / custom slot |
| Fearow | 10.00% | 36 | Native / custom slot |
| Geodude | 10.00% | 31 | Native / custom slot |
| Meowth | 10.00% | 31 | Native / custom slot |
| Persian | 5.00% | 37–40 | Native / custom slot |
| Psyduck | 5.00% | 34 | Native / custom slot |
| Rapidash | 5.00% | 37–40 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 95.00% | 5–30 | Native / custom slot |
| Graveler | 5.00% | 25–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sOneIslandKindleRoad_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Ponyta | 30.00% | 31–34 | Native / custom slot |
| Spearow | 25.00% | 30–32 | Native / custom slot |
| Fearow | 10.00% | 36 | Native / custom slot |
| Geodude | 10.00% | 31 | Native / custom slot |
| Meowth | 10.00% | 31 | Native / custom slot |
| Persian | 5.00% | 37–40 | Native / custom slot |
| Rapidash | 5.00% | 37–40 | Native / custom slot |
| Slowpoke | 5.00% | 34 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 95.00% | 5–30 | Native / custom slot |
| Graveler | 5.00% | 25–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-165"></a>
## One Island Treasure Beach

Source map: MAP_ONE_ISLAND_TREASURE_BEACH.

### Source variant 1: sOneIslandTreasureBeach_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Spearow | 30.00% | 31–32 | Native / custom slot |
| Tangela | 30.00% | 33–35 | Native / custom slot |
| Fearow | 20.00% | 36–40 | Native / custom slot |
| Meowth | 10.00% | 31 | Native / custom slot |
| Persian | 5.00% | 37–40 | Native / custom slot |
| Psyduck | 5.00% | 31 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sOneIslandTreasureBeach_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Spearow | 30.00% | 31–32 | Native / custom slot |
| Tangela | 30.00% | 33–35 | Native / custom slot |
| Fearow | 20.00% | 36–40 | Native / custom slot |
| Meowth | 10.00% | 31 | Native / custom slot |
| Persian | 5.00% | 37–40 | Native / custom slot |
| Slowpoke | 5.00% | 31 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-166"></a>
## Pacifidlog Town

Source map: MAP_PACIFIDLOG_TOWN.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 60.00% | 25–45 | Native / custom slot |
| Sharpedo | 40.00% | 30–35 | Native / custom slot |

---

<a id="area-167"></a>
## Pallet Town

Source map: MAP_PALLET_TOWN.

### Source variant 1: sPalletTown_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Shellder | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sPalletTown_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Staryu | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-168"></a>
## Pokemon Mansion 1F

Source map: MAP_POKEMON_MANSION_1F.

### Source variant 1: sPokemonMansion1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Koffing | 30.00% | 28–30 | Native / custom slot |
| Raticate | 30.00% | 32–36 | Native / custom slot |
| Growlithe | 15.00% | 30–32 | Native / custom slot |
| Rattata | 15.00% | 26–28 | Native / custom slot |
| Grimer | 5.00% | 28 | Native / custom slot |
| Weezing | 5.00% | 32 | Native / custom slot |

### Source variant 2: sPokemonMansion1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Grimer | 30.00% | 28–30 | Native / custom slot |
| Raticate | 30.00% | 32–36 | Native / custom slot |
| Rattata | 15.00% | 26–28 | Native / custom slot |
| Vulpix | 15.00% | 30–32 | Native / custom slot |
| Koffing | 5.00% | 28 | Native / custom slot |
| Muk | 5.00% | 32 | Native / custom slot |

---

<a id="area-169"></a>
## Pokemon Mansion 2F

Source map: MAP_POKEMON_MANSION_2F.

### Source variant 1: sPokemonMansion2F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Koffing | 30.00% | 28–30 | Native / custom slot |
| Raticate | 30.00% | 32–36 | Native / custom slot |
| Growlithe | 15.00% | 30–32 | Native / custom slot |
| Rattata | 15.00% | 26–28 | Native / custom slot |
| Grimer | 5.00% | 28 | Native / custom slot |
| Weezing | 5.00% | 32 | Native / custom slot |

### Source variant 2: sPokemonMansion2F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Grimer | 30.00% | 28–30 | Native / custom slot |
| Raticate | 30.00% | 32–36 | Native / custom slot |
| Rattata | 15.00% | 26–28 | Native / custom slot |
| Vulpix | 15.00% | 30–32 | Native / custom slot |
| Koffing | 5.00% | 28 | Native / custom slot |
| Muk | 5.00% | 32 | Native / custom slot |

---

<a id="area-170"></a>
## Pokemon Mansion 3F

Source map: MAP_POKEMON_MANSION_3F.

### Source variant 1: sPokemonMansion3F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Koffing | 30.00% | 28–30 | Native / custom slot |
| Raticate | 30.00% | 32–36 | Native / custom slot |
| Growlithe | 15.00% | 30–32 | Native / custom slot |
| Rattata | 15.00% | 26–28 | Native / custom slot |
| Grimer | 5.00% | 28 | Native / custom slot |
| Weezing | 5.00% | 32 | Native / custom slot |

### Source variant 2: sPokemonMansion3F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Grimer | 30.00% | 28–30 | Native / custom slot |
| Raticate | 30.00% | 32–36 | Native / custom slot |
| Rattata | 15.00% | 26–28 | Native / custom slot |
| Vulpix | 15.00% | 30–32 | Native / custom slot |
| Koffing | 5.00% | 28 | Native / custom slot |
| Muk | 5.00% | 32 | Native / custom slot |

---

<a id="area-171"></a>
## Pokemon Mansion B1F

Source map: MAP_POKEMON_MANSION_B1F.

### Source variant 1: sPokemonMansionB1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Koffing | 30.00% | 28–30 | Native / custom slot |
| Raticate | 30.00% | 34–38 | Native / custom slot |
| Growlithe | 15.00% | 30–32 | Native / custom slot |
| Ditto | 10.00% | 30 | Native / custom slot |
| Grimer | 5.00% | 28 | Native / custom slot |
| Rattata | 5.00% | 26 | Native / custom slot |
| Weezing | 5.00% | 34 | Native / custom slot |

### Source variant 2: sPokemonMansionB1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Grimer | 30.00% | 28–30 | Native / custom slot |
| Raticate | 30.00% | 34–38 | Native / custom slot |
| Vulpix | 15.00% | 30–32 | Native / custom slot |
| Ditto | 10.00% | 30 | Native / custom slot |
| Koffing | 5.00% | 28 | Native / custom slot |
| Muk | 5.00% | 34 | Native / custom slot |
| Rattata | 5.00% | 26 | Native / custom slot |

---

<a id="area-172"></a>
## Pokemon Tower 3F

Source map: MAP_POKEMON_TOWER_3F.

### Source variant 1: sPokemonTower3F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gastly | 90.00% | 13–19 | Native / custom slot |
| Cubone | 9.00% | 15–17 | Native / custom slot |
| Haunter | 1.00% | 20 | Native / custom slot |

### Source variant 2: sPokemonTower3F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gastly | 90.00% | 13–19 | Native / custom slot |
| Cubone | 9.00% | 15–17 | Native / custom slot |
| Haunter | 1.00% | 20 | Native / custom slot |

---

<a id="area-173"></a>
## Pokemon Tower 4F

Source map: MAP_POKEMON_TOWER_4F.

### Source variant 1: sPokemonTower4F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gastly | 86.00% | 13–19 | Native / custom slot |
| Cubone | 9.00% | 15–17 | Native / custom slot |
| Haunter | 5.00% | 20 | Native / custom slot |

### Source variant 2: sPokemonTower4F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gastly | 86.00% | 13–19 | Native / custom slot |
| Cubone | 9.00% | 15–17 | Native / custom slot |
| Haunter | 5.00% | 20 | Native / custom slot |

---

<a id="area-174"></a>
## Pokemon Tower 5F

Source map: MAP_POKEMON_TOWER_5F.

### Source variant 1: sPokemonTower5F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 6)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gastly | 86.00% | 13–19 | Native / custom slot |
| Cubone | 9.00% | 15–17 | Native / custom slot |
| Haunter | 5.00% | 20 | Native / custom slot |

### Source variant 2: sPokemonTower5F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 6)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gastly | 86.00% | 13–19 | Native / custom slot |
| Cubone | 9.00% | 15–17 | Native / custom slot |
| Haunter | 5.00% | 20 | Native / custom slot |

---

<a id="area-175"></a>
## Pokemon Tower 6F

Source map: MAP_POKEMON_TOWER_6F.

### Source variant 1: sPokemonTower6F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 8)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gastly | 85.00% | 14–19 | Native / custom slot |
| Cubone | 9.00% | 17–19 | Native / custom slot |
| Haunter | 6.00% | 21–23 | Native / custom slot |

### Source variant 2: sPokemonTower6F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 8)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gastly | 85.00% | 14–19 | Native / custom slot |
| Cubone | 9.00% | 17–19 | Native / custom slot |
| Haunter | 6.00% | 21–23 | Native / custom slot |

---

<a id="area-176"></a>
## Pokemon Tower 7F

Source map: MAP_POKEMON_TOWER_7F.

### Source variant 1: sPokemonTower7F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gastly | 75.00% | 15–19 | Native / custom slot |
| Haunter | 15.00% | 23–25 | Native / custom slot |
| Cubone | 10.00% | 17–19 | Native / custom slot |

### Source variant 2: sPokemonTower7F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gastly | 75.00% | 15–19 | Native / custom slot |
| Haunter | 15.00% | 23–25 | Native / custom slot |
| Cubone | 10.00% | 17–19 | Native / custom slot |

---

<a id="area-177"></a>
## Power Plant

Source map: MAP_POWER_PLANT.

### Source variant 1: sPowerPlant_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magnemite | 30.00% | 22–25 | Native / custom slot |
| Voltorb | 30.00% | 22–25 | Native / custom slot |
| Pikachu | 25.00% | 22–26 | Native / custom slot |
| Magneton | 10.00% | 31–34 | Native / custom slot |
| Electabuzz | 5.00% | 32–35 | Native / custom slot |

### Source variant 2: sPowerPlant_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magnemite | 30.00% | 22–25 | Native / custom slot |
| Voltorb | 30.00% | 22–25 | Native / custom slot |
| Pikachu | 25.00% | 22–26 | Native / custom slot |
| Magneton | 15.00% | 31–34 | Native / custom slot |

---

<a id="area-178"></a>
## Rock Tunnel 1F

Source map: MAP_ROCK_TUNNEL_1F.

### Source variant 1: sRockTunnel1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 35.00% | 15–17 | Native / custom slot |
| Zubat | 30.00% | 15–16 | Native / custom slot |
| Machop | 15.00% | 16–17 | Native / custom slot |
| Mankey | 15.00% | 16–17 | Native / custom slot |
| Onix | 5.00% | 13–15 | Native / custom slot |

### Source variant 2: sRockTunnel1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 35.00% | 15–17 | Native / custom slot |
| Zubat | 30.00% | 15–16 | Native / custom slot |
| Machop | 15.00% | 16–17 | Native / custom slot |
| Mankey | 15.00% | 16–17 | Native / custom slot |
| Onix | 5.00% | 13–15 | Native / custom slot |

---

<a id="area-179"></a>
## Rock Tunnel B1F

Source map: MAP_ROCK_TUNNEL_B1F.

### Source variant 1: sRockTunnelB1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 35.00% | 15–17 | Native / custom slot |
| Zubat | 30.00% | 15–16 | Native / custom slot |
| Mankey | 15.00% | 16–17 | Native / custom slot |
| Machop | 10.00% | 17 | Native / custom slot |
| Onix | 10.00% | 13–17 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 95.00% | 5–30 | Native / custom slot |
| Graveler | 5.00% | 25–40 | Native / custom slot |

### Source variant 2: sRockTunnelB1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 35.00% | 15–17 | Native / custom slot |
| Zubat | 30.00% | 15–16 | Native / custom slot |
| Mankey | 15.00% | 16–17 | Native / custom slot |
| Machop | 10.00% | 17 | Native / custom slot |
| Onix | 10.00% | 13–17 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 50)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 95.00% | 5–30 | Native / custom slot |
| Graveler | 5.00% | 25–40 | Native / custom slot |

---

<a id="area-180"></a>
## Route 1

Source map: MAP_ROUTE1.

### Source variant 1: sRoute1_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgey | 50.00% | 2–5 | Native / custom slot |
| Rattata | 50.00% | 2–4 | Native / custom slot |

### Source variant 2: sRoute1_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgey | 50.00% | 2–5 | Native / custom slot |
| Rattata | 50.00% | 2–4 | Native / custom slot |

---

<a id="area-181"></a>
## Route 10

Source map: MAP_ROUTE10.

### Source variant 1: sRoute10_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Voltorb | 40.00% | 14–17 | Native / custom slot |
| Spearow | 35.00% | 13–17 | Native / custom slot |
| Ekans | 25.00% | 11–17 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sRoute10_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Voltorb | 40.00% | 14–17 | Native / custom slot |
| Spearow | 35.00% | 13–17 | Native / custom slot |
| Sandshrew | 25.00% | 11–17 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-182"></a>
## Route 11

Source map: MAP_ROUTE11.

### Source variant 1: sRoute11_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Ekans | 40.00% | 12–15 | Native / custom slot |
| Spearow | 35.00% | 13–17 | Native / custom slot |
| Drowzee | 25.00% | 11–15 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sRoute11_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sandshrew | 40.00% | 12–15 | Native / custom slot |
| Spearow | 35.00% | 13–17 | Native / custom slot |
| Drowzee | 25.00% | 11–15 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-183"></a>
## Route 12

Source map: MAP_ROUTE12.

### Source variant 1: sRoute12_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 35.00% | 22–26 | Native / custom slot |
| Pidgey | 30.00% | 23–27 | Native / custom slot |
| Venonat | 30.00% | 24–26 | Native / custom slot |
| Gloom | 5.00% | 28–30 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 60)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 60)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 60)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sRoute12_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Bellsprout | 35.00% | 22–26 | Native / custom slot |
| Pidgey | 30.00% | 23–27 | Native / custom slot |
| Venonat | 30.00% | 24–26 | Native / custom slot |
| Weepinbell | 5.00% | 28–30 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 60)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 60)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 60)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-184"></a>
## Route 13

Source map: MAP_ROUTE13.

### Source variant 1: sRoute13_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 35.00% | 22–26 | Native / custom slot |
| Venonat | 30.00% | 24–26 | Native / custom slot |
| Pidgey | 20.00% | 25–27 | Native / custom slot |
| Ditto | 5.00% | 25 | Native / custom slot |
| Gloom | 5.00% | 28–30 | Native / custom slot |
| Pidgeotto | 5.00% | 29 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sRoute13_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Bellsprout | 35.00% | 22–26 | Native / custom slot |
| Venonat | 30.00% | 24–26 | Native / custom slot |
| Pidgey | 20.00% | 25–27 | Native / custom slot |
| Ditto | 5.00% | 25 | Native / custom slot |
| Pidgeotto | 5.00% | 29 | Native / custom slot |
| Weepinbell | 5.00% | 28–30 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-185"></a>
## Route 14

Source map: MAP_ROUTE14.

### Source variant 1: sRoute14_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 35.00% | 22–26 | Native / custom slot |
| Venonat | 30.00% | 24–26 | Native / custom slot |
| Ditto | 15.00% | 23 | Native / custom slot |
| Pidgey | 10.00% | 27 | Native / custom slot |
| Gloom | 5.00% | 30 | Native / custom slot |
| Pidgeotto | 5.00% | 29 | Native / custom slot |

### Source variant 2: sRoute14_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Bellsprout | 35.00% | 22–26 | Native / custom slot |
| Venonat | 30.00% | 24–26 | Native / custom slot |
| Ditto | 15.00% | 23 | Native / custom slot |
| Pidgey | 10.00% | 27 | Native / custom slot |
| Pidgeotto | 5.00% | 29 | Native / custom slot |
| Weepinbell | 5.00% | 30 | Native / custom slot |

---

<a id="area-186"></a>
## Route 15

Source map: MAP_ROUTE15.

### Source variant 1: sRoute15_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 35.00% | 22–26 | Native / custom slot |
| Venonat | 30.00% | 24–26 | Native / custom slot |
| Pidgey | 20.00% | 25–27 | Native / custom slot |
| Ditto | 5.00% | 25 | Native / custom slot |
| Gloom | 5.00% | 28–30 | Native / custom slot |
| Pidgeotto | 5.00% | 29 | Native / custom slot |

### Source variant 2: sRoute15_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Bellsprout | 35.00% | 22–26 | Native / custom slot |
| Venonat | 30.00% | 24–26 | Native / custom slot |
| Pidgey | 20.00% | 25–27 | Native / custom slot |
| Ditto | 5.00% | 25 | Native / custom slot |
| Pidgeotto | 5.00% | 29 | Native / custom slot |
| Weepinbell | 5.00% | 28–30 | Native / custom slot |

---

<a id="area-187"></a>
## Route 16

Source map: MAP_ROUTE16.

### Source variant 1: sRoute16_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Doduo | 35.00% | 18–22 | Native / custom slot |
| Rattata | 30.00% | 18–22 | Native / custom slot |
| Spearow | 30.00% | 20–22 | Native / custom slot |
| Raticate | 5.00% | 23–25 | Native / custom slot |

### Source variant 2: sRoute16_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Doduo | 35.00% | 18–22 | Native / custom slot |
| Rattata | 30.00% | 18–22 | Native / custom slot |
| Spearow | 30.00% | 20–22 | Native / custom slot |
| Raticate | 5.00% | 23–25 | Native / custom slot |

---

<a id="area-188"></a>
## Route 17

Source map: MAP_ROUTE17.

### Source variant 1: sRoute17_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Doduo | 35.00% | 24–28 | Native / custom slot |
| Spearow | 30.00% | 20–22 | Native / custom slot |
| Raticate | 25.00% | 25–29 | Native / custom slot |
| Fearow | 5.00% | 25–27 | Native / custom slot |
| Rattata | 5.00% | 22 | Native / custom slot |

### Source variant 2: sRoute17_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Doduo | 35.00% | 24–28 | Native / custom slot |
| Spearow | 30.00% | 20–22 | Native / custom slot |
| Raticate | 25.00% | 25–29 | Native / custom slot |
| Fearow | 5.00% | 25–27 | Native / custom slot |
| Rattata | 5.00% | 22 | Native / custom slot |

---

<a id="area-189"></a>
## Route 18

Source map: MAP_ROUTE18.

### Source variant 1: sRoute18_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Doduo | 35.00% | 24–28 | Native / custom slot |
| Spearow | 30.00% | 20–22 | Native / custom slot |
| Fearow | 15.00% | 25–29 | Native / custom slot |
| Raticate | 15.00% | 25–29 | Native / custom slot |
| Rattata | 5.00% | 22 | Native / custom slot |

### Source variant 2: sRoute18_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Doduo | 35.00% | 24–28 | Native / custom slot |
| Spearow | 30.00% | 20–22 | Native / custom slot |
| Fearow | 15.00% | 25–29 | Native / custom slot |
| Raticate | 15.00% | 25–29 | Native / custom slot |
| Rattata | 5.00% | 22 | Native / custom slot |

---

<a id="area-190"></a>
## Route 19

Source map: MAP_ROUTE19.

### Source variant 1: sRoute19_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sRoute19_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-191"></a>
## Route 2

Source map: MAP_ROUTE2.

### Source variant 1: sRoute2_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgey | 45.00% | 2–5 | Native / custom slot |
| Rattata | 45.00% | 2–5 | Native / custom slot |
| Caterpie | 5.00% | 4–5 | Native / custom slot |
| Weedle | 5.00% | 4–5 | Native / custom slot |

### Source variant 2: sRoute2_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgey | 45.00% | 2–5 | Native / custom slot |
| Rattata | 45.00% | 2–5 | Native / custom slot |
| Caterpie | 5.00% | 4–5 | Native / custom slot |
| Weedle | 5.00% | 4–5 | Native / custom slot |

---

<a id="area-192"></a>
## Route 20

Source map: MAP_ROUTE20.

### Source variant 1: sRoute20_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sRoute20_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-193"></a>
## Route 21 North

Source map: MAP_ROUTE21_NORTH.

### Source variant 1: sRoute21North_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 14)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tangela | 100.00% | 17–28 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sRoute21North_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 14)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tangela | 100.00% | 17–28 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-194"></a>
## Route 21 South

Source map: MAP_ROUTE21_SOUTH.

### Source variant 1: sRoute21South_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 14)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tangela | 100.00% | 17–28 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sRoute21South_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 14)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tangela | 100.00% | 17–28 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-195"></a>
## Route 22

Source map: MAP_ROUTE22.

### Source variant 1: sRoute22_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Mankey | 45.00% | 2–5 | Native / custom slot |
| Rattata | 45.00% | 2–5 | Native / custom slot |
| Spearow | 10.00% | 3–5 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sRoute22_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Mankey | 45.00% | 2–5 | Native / custom slot |
| Rattata | 45.00% | 2–5 | Native / custom slot |
| Spearow | 10.00% | 3–5 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-196"></a>
## Route 23

Source map: MAP_ROUTE23.

### Source variant 1: sRoute23_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Mankey | 30.00% | 32–34 | Native / custom slot |
| Fearow | 25.00% | 40–44 | Native / custom slot |
| Ekans | 20.00% | 32–34 | Native / custom slot |
| Spearow | 15.00% | 32–34 | Native / custom slot |
| Arbok | 5.00% | 44 | Native / custom slot |
| Primeape | 5.00% | 42 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sRoute23_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Mankey | 30.00% | 32–34 | Native / custom slot |
| Fearow | 25.00% | 40–44 | Native / custom slot |
| Sandshrew | 20.00% | 32–34 | Native / custom slot |
| Spearow | 15.00% | 32–34 | Native / custom slot |
| Primeape | 5.00% | 42 | Native / custom slot |
| Sandslash | 5.00% | 44 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-197"></a>
## Route 24

Source map: MAP_ROUTE24.

### Source variant 1: sRoute24_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 25.00% | 12–14 | Native / custom slot |
| Caterpie | 20.00% | 7 | Native / custom slot |
| Weedle | 20.00% | 7 | Native / custom slot |
| Abra | 15.00% | 8–12 | Native / custom slot |
| Pidgey | 15.00% | 11–13 | Native / custom slot |
| Kakuna | 4.00% | 8 | Native / custom slot |
| Metapod | 1.00% | 8 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sRoute24_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Bellsprout | 25.00% | 12–14 | Native / custom slot |
| Caterpie | 20.00% | 7 | Native / custom slot |
| Weedle | 20.00% | 7 | Native / custom slot |
| Abra | 15.00% | 8–12 | Native / custom slot |
| Pidgey | 15.00% | 11–13 | Native / custom slot |
| Metapod | 4.00% | 8 | Native / custom slot |
| Kakuna | 1.00% | 8 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-198"></a>
## Route 25

Source map: MAP_ROUTE25.

### Source variant 1: sRoute25_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 25.00% | 12–14 | Native / custom slot |
| Caterpie | 20.00% | 8 | Native / custom slot |
| Weedle | 20.00% | 8 | Native / custom slot |
| Abra | 15.00% | 9–13 | Native / custom slot |
| Pidgey | 15.00% | 11–13 | Native / custom slot |
| Kakuna | 4.00% | 9 | Native / custom slot |
| Metapod | 1.00% | 9 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sRoute25_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Bellsprout | 25.00% | 12–14 | Native / custom slot |
| Caterpie | 20.00% | 8 | Native / custom slot |
| Weedle | 20.00% | 8 | Native / custom slot |
| Abra | 15.00% | 9–13 | Native / custom slot |
| Pidgey | 15.00% | 11–13 | Native / custom slot |
| Metapod | 4.00% | 9 | Native / custom slot |
| Kakuna | 1.00% | 9 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-199"></a>
## Route 3

Source map: MAP_ROUTE3.

### Source variant 1: sRoute3_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Spearow | 35.00% | 6–8 | Native / custom slot |
| Pidgey | 30.00% | 6–7 | Native / custom slot |
| Nidoran M | 14.00% | 6–7 | Native / custom slot |
| Jigglypuff | 10.00% | 3–7 | Native / custom slot |
| Mankey | 10.00% | 7 | Native / custom slot |
| Nidoran F | 1.00% | 6 | Native / custom slot |

### Source variant 2: sRoute3_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Spearow | 35.00% | 6–8 | Native / custom slot |
| Pidgey | 30.00% | 6–7 | Native / custom slot |
| Nidoran F | 14.00% | 6–7 | Native / custom slot |
| Jigglypuff | 10.00% | 3–7 | Native / custom slot |
| Mankey | 10.00% | 7 | Native / custom slot |
| Nidoran M | 1.00% | 6 | Native / custom slot |

---

<a id="area-200"></a>
## Route 4

Source map: MAP_ROUTE4.

### Source variant 1: sRoute4_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Rattata | 35.00% | 8–12 | Native / custom slot |
| Spearow | 35.00% | 8–12 | Native / custom slot |
| Ekans | 25.00% | 6–12 | Native / custom slot |
| Mankey | 5.00% | 10–12 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sRoute4_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Rattata | 35.00% | 8–12 | Native / custom slot |
| Spearow | 35.00% | 8–12 | Native / custom slot |
| Sandshrew | 25.00% | 6–12 | Native / custom slot |
| Mankey | 5.00% | 10–12 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 84.00% | 15–35 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-201"></a>
## Route 5

Source map: MAP_ROUTE5.

### Source variant 1: sRoute5_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgey | 40.00% | 13–16 | Native / custom slot |
| Meowth | 35.00% | 10–16 | Native / custom slot |
| Oddish | 25.00% | 13–16 | Native / custom slot |

### Source variant 2: sRoute5_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgey | 40.00% | 13–16 | Native / custom slot |
| Meowth | 35.00% | 10–16 | Native / custom slot |
| Bellsprout | 25.00% | 13–16 | Native / custom slot |

---

<a id="area-202"></a>
## Route 6

Source map: MAP_ROUTE6.

### Source variant 1: sRoute6_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgey | 40.00% | 13–16 | Native / custom slot |
| Meowth | 35.00% | 10–16 | Native / custom slot |
| Oddish | 25.00% | 13–16 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sRoute6_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgey | 40.00% | 13–16 | Native / custom slot |
| Meowth | 35.00% | 10–16 | Native / custom slot |
| Bellsprout | 25.00% | 13–16 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-203"></a>
## Route 7

Source map: MAP_ROUTE7.

### Source variant 1: sRoute7_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Meowth | 40.00% | 17–20 | Native / custom slot |
| Pidgey | 30.00% | 19–22 | Native / custom slot |
| Oddish | 20.00% | 19–22 | Native / custom slot |
| Growlithe | 10.00% | 18–20 | Native / custom slot |

### Source variant 2: sRoute7_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Meowth | 40.00% | 17–20 | Native / custom slot |
| Pidgey | 30.00% | 19–22 | Native / custom slot |
| Bellsprout | 20.00% | 19–22 | Native / custom slot |
| Vulpix | 10.00% | 18–20 | Native / custom slot |

---

<a id="area-204"></a>
## Route 8

Source map: MAP_ROUTE8.

### Source variant 1: sRoute8_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Meowth | 30.00% | 18–20 | Native / custom slot |
| Pidgey | 30.00% | 18–20 | Native / custom slot |
| Ekans | 20.00% | 17–19 | Native / custom slot |
| Growlithe | 20.00% | 15–18 | Native / custom slot |

### Source variant 2: sRoute8_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Meowth | 30.00% | 18–20 | Native / custom slot |
| Pidgey | 30.00% | 18–20 | Native / custom slot |
| Sandshrew | 20.00% | 17–19 | Native / custom slot |
| Vulpix | 20.00% | 15–18 | Native / custom slot |

---

<a id="area-205"></a>
## Route 9

Source map: MAP_ROUTE9.

### Source variant 1: sRoute9_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Rattata | 40.00% | 14–17 | Native / custom slot |
| Spearow | 35.00% | 13–17 | Native / custom slot |
| Ekans | 25.00% | 11–17 | Native / custom slot |

### Source variant 2: sRoute9_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Rattata | 40.00% | 14–17 | Native / custom slot |
| Spearow | 35.00% | 13–17 | Native / custom slot |
| Sandshrew | 25.00% | 11–17 | Native / custom slot |

---

<a id="area-206"></a>
## Seafoam Islands 1F

Source map: MAP_SEAFOAM_ISLANDS_1F.

### Source variant 1: sSeafoamIslands1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 55.00% | 26–33 | Native / custom slot |
| Zubat | 34.00% | 22–26 | Native / custom slot |
| Golbat | 11.00% | 26–30 | Native / custom slot |

### Source variant 2: sSeafoamIslands1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 55.00% | 26–33 | Native / custom slot |
| Zubat | 34.00% | 22–26 | Native / custom slot |
| Golbat | 11.00% | 26–30 | Native / custom slot |

---

<a id="area-207"></a>
## Seafoam Islands B1F

Source map: MAP_SEAFOAM_ISLANDS_B1F.

### Source variant 1: sSeafoamIslandsB1F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 40.00% | 29–31 | Native / custom slot |
| Zubat | 34.00% | 22–26 | Native / custom slot |
| Golbat | 11.00% | 26–30 | Native / custom slot |
| Seel | 10.00% | 28 | Native / custom slot |
| Golduck | 5.00% | 33–35 | Native / custom slot |

### Source variant 2: sSeafoamIslandsB1F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 40.00% | 29–31 | Native / custom slot |
| Zubat | 34.00% | 22–26 | Native / custom slot |
| Golbat | 11.00% | 26–30 | Native / custom slot |
| Seel | 10.00% | 28 | Native / custom slot |
| Slowbro | 5.00% | 33–35 | Native / custom slot |

---

<a id="area-208"></a>
## Seafoam Islands B2F

Source map: MAP_SEAFOAM_ISLANDS_B2F.

### Source variant 1: sSeafoamIslandsB2F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 40.00% | 30–32 | Native / custom slot |
| Seel | 20.00% | 30–32 | Native / custom slot |
| Zubat | 20.00% | 22–24 | Native / custom slot |
| Golbat | 10.00% | 26–30 | Native / custom slot |
| Golduck | 10.00% | 32–34 | Native / custom slot |

### Source variant 2: sSeafoamIslandsB2F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 40.00% | 30–32 | Native / custom slot |
| Seel | 20.00% | 30–32 | Native / custom slot |
| Zubat | 20.00% | 22–24 | Native / custom slot |
| Golbat | 10.00% | 26–30 | Native / custom slot |
| Slowbro | 10.00% | 32–34 | Native / custom slot |

---

<a id="area-209"></a>
## Seafoam Islands B3F

Source map: MAP_SEAFOAM_ISLANDS_B3F.

### Source variant 1: sSeafoamIslandsB3F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 40.00% | 30–32 | Native / custom slot |
| Psyduck | 20.00% | 30–32 | Native / custom slot |
| Golduck | 15.00% | 32–34 | Native / custom slot |
| Golbat | 10.00% | 26–30 | Native / custom slot |
| Zubat | 10.00% | 24 | Native / custom slot |
| Dewgong | 5.00% | 32–34 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 60.00% | 25–35 | Native / custom slot |
| Horsea | 30.00% | 25–30 | Native / custom slot |
| Dewgong | 5.00% | 35–40 | Native / custom slot |
| Psyduck | 4.00% | 30–40 | Native / custom slot |
| Golduck | 1.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 15–30 | Native / custom slot |
| Gyarados | 16.00% | 15–35 | Native / custom slot |
| Psyduck | 4.00% | 15–25 | Native / custom slot |

### Source variant 2: sSeafoamIslandsB3F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 40.00% | 30–32 | Native / custom slot |
| Slowpoke | 20.00% | 30–32 | Native / custom slot |
| Slowbro | 15.00% | 32–34 | Native / custom slot |
| Golbat | 10.00% | 26–30 | Native / custom slot |
| Zubat | 10.00% | 24 | Native / custom slot |
| Dewgong | 5.00% | 32–34 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 60.00% | 25–35 | Native / custom slot |
| Krabby | 30.00% | 25–30 | Native / custom slot |
| Dewgong | 5.00% | 35–40 | Native / custom slot |
| Slowpoke | 4.00% | 30–40 | Native / custom slot |
| Slowbro | 1.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 15–30 | Native / custom slot |
| Gyarados | 16.00% | 15–35 | Native / custom slot |
| Slowpoke | 4.00% | 15–25 | Native / custom slot |

---

<a id="area-210"></a>
## Seafoam Islands B4F

Source map: MAP_SEAFOAM_ISLANDS_B4F.

### Source variant 1: sSeafoamIslandsB4F_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 50.00% | 30–34 | Native / custom slot |
| Golbat | 15.00% | 26–30 | Native / custom slot |
| Golduck | 15.00% | 32–34 | Native / custom slot |
| Dewgong | 10.00% | 34–36 | Native / custom slot |
| Psyduck | 10.00% | 32 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 60.00% | 25–35 | Native / custom slot |
| Horsea | 30.00% | 25–30 | Native / custom slot |
| Dewgong | 5.00% | 35–40 | Native / custom slot |
| Psyduck | 4.00% | 30–40 | Native / custom slot |
| Golduck | 1.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 15–30 | Native / custom slot |
| Gyarados | 16.00% | 15–35 | Native / custom slot |
| Psyduck | 4.00% | 15–25 | Native / custom slot |

### Source variant 2: sSeafoamIslandsB4F_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 50.00% | 30–34 | Native / custom slot |
| Golbat | 15.00% | 26–30 | Native / custom slot |
| Slowbro | 15.00% | 32–34 | Native / custom slot |
| Dewgong | 10.00% | 34–36 | Native / custom slot |
| Slowpoke | 10.00% | 32 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Seel | 60.00% | 25–35 | Native / custom slot |
| Krabby | 30.00% | 25–30 | Native / custom slot |
| Dewgong | 5.00% | 35–40 | Native / custom slot |
| Slowpoke | 4.00% | 30–40 | Native / custom slot |
| Slowbro | 1.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 15–30 | Native / custom slot |
| Gyarados | 16.00% | 15–35 | Native / custom slot |
| Slowpoke | 4.00% | 15–25 | Native / custom slot |

---

<a id="area-211"></a>
## Seven Island Sevault Canyon

Source map: MAP_SEVEN_ISLAND_SEVAULT_CANYON.

### Source variant 1: sSevenIslandSevaultCanyon_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 20.00% | 46 | Native / custom slot |
| Phanpy | 20.00% | 15 | Native / custom slot |
| Cubone | 10.00% | 46 | Native / custom slot |
| Fearow | 10.00% | 50 | Native / custom slot |
| Marowak | 10.00% | 52 | Native / custom slot |
| Meowth | 10.00% | 43 | Native / custom slot |
| Larvitar | 5.00% | 15–20 | Native / custom slot |
| Onix | 5.00% | 54 | Native / custom slot |
| Persian | 5.00% | 49–52 | Native / custom slot |
| Skarmory | 5.00% | 30 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

### Source variant 2: sSevenIslandSevaultCanyon_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 20.00% | 46 | Native / custom slot |
| Phanpy | 20.00% | 15 | Native / custom slot |
| Fearow | 15.00% | 50 | Native / custom slot |
| Cubone | 10.00% | 46 | Native / custom slot |
| Marowak | 10.00% | 52 | Native / custom slot |
| Meowth | 10.00% | 43 | Native / custom slot |
| Larvitar | 5.00% | 15–20 | Native / custom slot |
| Onix | 5.00% | 54 | Native / custom slot |
| Persian | 5.00% | 49–52 | Native / custom slot |

### Rock Smash (base encounter-frequency setting: 25)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Geodude | 65.00% | 25–40 | Native / custom slot |
| Graveler | 35.00% | 30–50 | Native / custom slot |

---

<a id="area-212"></a>
## Seven Island Sevault Canyon Entrance

Source map: MAP_SEVEN_ISLAND_SEVAULT_CANYON_ENTRANCE.

### Source variant 1: sSevenIslandSevaultCanyonEntrance_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sentret | 30.00% | 10–15 | Native / custom slot |
| Spearow | 20.00% | 44 | Native / custom slot |
| Fearow | 15.00% | 48–50 | Native / custom slot |
| Phanpy | 15.00% | 10–15 | Native / custom slot |
| Meowth | 10.00% | 41 | Native / custom slot |
| Persian | 5.00% | 47–50 | Native / custom slot |
| Psyduck | 5.00% | 41 | Native / custom slot |

### Source variant 2: sSevenIslandSevaultCanyonEntrance_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sentret | 30.00% | 10–15 | Native / custom slot |
| Spearow | 20.00% | 44 | Native / custom slot |
| Fearow | 15.00% | 48–50 | Native / custom slot |
| Phanpy | 15.00% | 10–15 | Native / custom slot |
| Meowth | 10.00% | 41 | Native / custom slot |
| Persian | 5.00% | 47–50 | Native / custom slot |
| Slowpoke | 5.00% | 41 | Native / custom slot |

---

<a id="area-213"></a>
## Seven Island Tanoby Ruins

Source map: MAP_SEVEN_ISLAND_TANOBY_RUINS.

### Source variant 1: sSevenIslandTanobyRuins_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Qwilfish | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sSevenIslandTanobyRuins_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 90.00% | 5–35 | Native / custom slot |
| Mantine | 5.00% | 35–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Remoraid | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-214"></a>
## Seven Island Tanoby Ruins Dilford Chamber

Source map: MAP_SEVEN_ISLAND_TANOBY_RUINS_DILFORD_CHAMBER.

### Source variant 1: sSevenIslandTanobyRuinsDilfordChamber_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

### Source variant 2: sSevenIslandTanobyRuinsDilfordChamber_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

---

<a id="area-215"></a>
## Seven Island Tanoby Ruins Liptoo Chamber

Source map: MAP_SEVEN_ISLAND_TANOBY_RUINS_LIPTOO_CHAMBER.

### Source variant 1: sSevenIslandTanobyRuinsLiptooChamber_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

### Source variant 2: sSevenIslandTanobyRuinsLiptooChamber_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

---

<a id="area-216"></a>
## Seven Island Tanoby Ruins Monean Chamber

Source map: MAP_SEVEN_ISLAND_TANOBY_RUINS_MONEAN_CHAMBER.

### Source variant 1: sSevenIslandTanobyRuinsMoneanChamber_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

### Source variant 2: sSevenIslandTanobyRuinsMoneanChamber_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

---

<a id="area-217"></a>
## Seven Island Tanoby Ruins Rixy Chamber

Source map: MAP_SEVEN_ISLAND_TANOBY_RUINS_RIXY_CHAMBER.

### Source variant 1: sSevenIslandTanobyRuinsRixyChamber_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

### Source variant 2: sSevenIslandTanobyRuinsRixyChamber_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

---

<a id="area-218"></a>
## Seven Island Tanoby Ruins Scufib Chamber

Source map: MAP_SEVEN_ISLAND_TANOBY_RUINS_SCUFIB_CHAMBER.

### Source variant 1: sSevenIslandTanobyRuinsScufibChamber_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

### Source variant 2: sSevenIslandTanobyRuinsScufibChamber_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

---

<a id="area-219"></a>
## Seven Island Tanoby Ruins Viapois Chamber

Source map: MAP_SEVEN_ISLAND_TANOBY_RUINS_VIAPOIS_CHAMBER.

### Source variant 1: sSevenIslandTanobyRuinsViapoisChamber_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

### Source variant 2: sSevenIslandTanobyRuinsViapoisChamber_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

---

<a id="area-220"></a>
## Seven Island Tanoby Ruins Weepth Chamber

Source map: MAP_SEVEN_ISLAND_TANOBY_RUINS_WEEPTH_CHAMBER.

### Source variant 1: sSevenIslandTanobyRuinsWeepthChamber_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

### Source variant 2: sSevenIslandTanobyRuinsWeepthChamber_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Unown | 100.00% | 25 | Native / custom slot |

---

<a id="area-221"></a>
## Seven Island Trainer Tower

Source map: MAP_SEVEN_ISLAND_TRAINER_TOWER.

### Source variant 1: sSevenIslandTrainerTower_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Qwilfish | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sSevenIslandTrainerTower_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 90.00% | 5–35 | Native / custom slot |
| Mantine | 5.00% | 35–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Remoraid | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-222"></a>
## Six Island Altering Cave

Source map: MAP_SIX_ISLAND_ALTERING_CAVE.

### Source variant 1: sSixIslandAlteringCave_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 100.00% | 6–16 | Native / custom slot |

### Source variant 2: sSixIslandAlteringCave_2_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Mareep | 100.00% | 3–13 | Native / custom slot |

### Source variant 3: sSixIslandAlteringCave_3_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pineco | 100.00% | 19–29 | Native / custom slot |

### Source variant 4: sSixIslandAlteringCave_4_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Houndour | 100.00% | 12–22 | Native / custom slot |

### Source variant 5: sSixIslandAlteringCave_5_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Teddiursa | 100.00% | 18–28 | Native / custom slot |

### Source variant 6: sSixIslandAlteringCave_6_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Aipom | 100.00% | 18–28 | Native / custom slot |

### Source variant 7: sSixIslandAlteringCave_7_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuckle | 100.00% | 18–28 | Native / custom slot |

### Source variant 8: sSixIslandAlteringCave_8_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Stantler | 100.00% | 18–28 | Native / custom slot |

### Source variant 9: sSixIslandAlteringCave_9_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 5)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Smeargle | 100.00% | 18–28 | Native / custom slot |

### Source variant 10: sSixIslandAlteringCave_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Zubat | 100.00% | 6–16 | Native / custom slot |

### Source variant 11: sSixIslandAlteringCave_2_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Mareep | 100.00% | 3–13 | Native / custom slot |

### Source variant 12: sSixIslandAlteringCave_3_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pineco | 100.00% | 19–29 | Native / custom slot |

### Source variant 13: sSixIslandAlteringCave_4_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Houndour | 100.00% | 12–22 | Native / custom slot |

### Source variant 14: sSixIslandAlteringCave_5_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Teddiursa | 100.00% | 18–28 | Native / custom slot |

### Source variant 15: sSixIslandAlteringCave_6_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Aipom | 100.00% | 18–28 | Native / custom slot |

### Source variant 16: sSixIslandAlteringCave_7_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Shuckle | 100.00% | 18–28 | Native / custom slot |

### Source variant 17: sSixIslandAlteringCave_8_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Stantler | 100.00% | 18–28 | Native / custom slot |

### Source variant 18: sSixIslandAlteringCave_9_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 7)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Smeargle | 100.00% | 18–28 | Native / custom slot |

---

<a id="area-223"></a>
## Six Island Green Path

Source map: MAP_SIX_ISLAND_GREEN_PATH.

### Source variant 1: sSixIslandGreenPath_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Qwilfish | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sSixIslandGreenPath_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Remoraid | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-224"></a>
## Six Island Outcast Island

Source map: MAP_SIX_ISLAND_OUTCAST_ISLAND.

### Source variant 1: sSixIslandOutcastIsland_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Qwilfish | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sSixIslandOutcastIsland_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Remoraid | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-225"></a>
## Six Island Pattern Bush

Source map: MAP_SIX_ISLAND_PATTERN_BUSH.

### Source variant 1: sSixIslandPatternBush_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Spinarak | 30.00% | 9–14 | Native / custom slot |
| Heracross | 20.00% | 15–30 | Native / custom slot |
| Kakuna | 20.00% | 9 | Native / custom slot |
| Caterpie | 10.00% | 6 | Native / custom slot |
| Weedle | 10.00% | 6 | Native / custom slot |
| Ledyba | 5.00% | 9–14 | Native / custom slot |
| Metapod | 5.00% | 9 | Native / custom slot |

### Source variant 2: sSixIslandPatternBush_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Ledyba | 30.00% | 9–14 | Native / custom slot |
| Heracross | 20.00% | 15–30 | Native / custom slot |
| Kakuna | 20.00% | 9 | Native / custom slot |
| Caterpie | 10.00% | 6 | Native / custom slot |
| Weedle | 10.00% | 6 | Native / custom slot |
| Metapod | 5.00% | 9 | Native / custom slot |
| Spinarak | 5.00% | 9–14 | Native / custom slot |

---

<a id="area-226"></a>
## Six Island Ruin Valley

Source map: MAP_SIX_ISLAND_RUIN_VALLEY.

### Source variant 1: sSixIslandRuinValley_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Natu | 25.00% | 15–20 | Native / custom slot |
| Spearow | 20.00% | 44 | Native / custom slot |
| Fearow | 10.00% | 49 | Native / custom slot |
| Meowth | 10.00% | 43 | Native / custom slot |
| Wooper | 10.00% | 15 | Native / custom slot |
| Yanma | 10.00% | 18 | Native / custom slot |
| Persian | 5.00% | 49–52 | Native / custom slot |
| Psyduck | 5.00% | 41 | Native / custom slot |
| Wobbuffet | 5.00% | 25 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wooper | 100.00% | 5–25 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sSixIslandRuinValley_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Natu | 25.00% | 15–20 | Native / custom slot |
| Spearow | 20.00% | 44 | Native / custom slot |
| Fearow | 10.00% | 49 | Native / custom slot |
| Marill | 10.00% | 15 | Native / custom slot |
| Meowth | 10.00% | 43 | Native / custom slot |
| Yanma | 10.00% | 18 | Native / custom slot |
| Persian | 5.00% | 49–52 | Native / custom slot |
| Slowpoke | 5.00% | 41 | Native / custom slot |
| Wobbuffet | 5.00% | 25 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Marill | 100.00% | 5–25 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-227"></a>
## Six Island Water Path

Source map: MAP_SIX_ISLAND_WATER_PATH.

### Source variant 1: sSixIslandWaterPath_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sentret | 30.00% | 10–15 | Native / custom slot |
| Spearow | 20.00% | 44 | Native / custom slot |
| Fearow | 15.00% | 48–50 | Native / custom slot |
| Meowth | 10.00% | 41 | Native / custom slot |
| Oddish | 10.00% | 44 | Native / custom slot |
| Gloom | 5.00% | 48 | Native / custom slot |
| Persian | 5.00% | 47–50 | Native / custom slot |
| Psyduck | 5.00% | 41 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 40.00% | 15–25 | Native / custom slot |
| Qwilfish | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sSixIslandWaterPath_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Sentret | 30.00% | 10–15 | Native / custom slot |
| Spearow | 20.00% | 44 | Native / custom slot |
| Fearow | 15.00% | 48–50 | Native / custom slot |
| Bellsprout | 10.00% | 44 | Native / custom slot |
| Meowth | 10.00% | 41 | Native / custom slot |
| Persian | 5.00% | 47–50 | Native / custom slot |
| Slowpoke | 5.00% | 41 | Native / custom slot |
| Weepinbell | 5.00% | 48 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Remoraid | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-228"></a>
## Slateport City

Source map: MAP_SLATEPORT_CITY.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 60.00% | 5–35 | Native / custom slot |
| Wingull | 35.00% | 10–30 | Native / custom slot |
| Pelipper | 5.00% | 25–30 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 60.00% | 10–30 | Native / custom slot |
| Tentacool | 20.00% | 10–30 | Native / custom slot |
| Wailmer | 20.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Wailmer | 100.00% | 20–45 | Native / custom slot |

---

<a id="area-229"></a>
## Sootopolis City

Source map: MAP_SOOTOPOLIS_CITY.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5–35 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 70.00% | 5–10 | Native / custom slot |
| Tentacool | 30.00% | 5–10 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 10–30 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 80.00% | 30–35 | Native / custom slot |
| Gyarados | 20.00% | 5–45 | Native / custom slot |

---

<a id="area-230"></a>
## Ssanne Exterior

Source map: MAP_SSANNE_EXTERIOR.

### Source variant 1: sSSAnneExterior_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 44.00% | 15–35 | Native / custom slot |
| Shellder | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sSSAnneExterior_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 44.00% | 15–35 | Native / custom slot |
| Staryu | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-231"></a>
## Three Island Berry Forest

Source map: MAP_THREE_ISLAND_BERRY_FOREST.

### Source variant 1: sThreeIslandBerryForest_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Gloom | 20.00% | 35 | Native / custom slot |
| Pidgeotto | 20.00% | 37 | Native / custom slot |
| Drowzee | 10.00% | 34 | Native / custom slot |
| Oddish | 10.00% | 30 | Native / custom slot |
| Pidgey | 10.00% | 32 | Native / custom slot |
| Venonat | 10.00% | 34 | Native / custom slot |
| Exeggcute | 5.00% | 35 | Native / custom slot |
| Hypno | 5.00% | 37–40 | Native / custom slot |
| Psyduck | 5.00% | 31 | Native / custom slot |
| Venomoth | 5.00% | 37–40 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 95.00% | 5–40 | Native / custom slot |
| Golduck | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sThreeIslandBerryForest_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgeotto | 20.00% | 37 | Native / custom slot |
| Weepinbell | 20.00% | 35 | Native / custom slot |
| Bellsprout | 10.00% | 30 | Native / custom slot |
| Drowzee | 10.00% | 34 | Native / custom slot |
| Pidgey | 10.00% | 32 | Native / custom slot |
| Venonat | 10.00% | 34 | Native / custom slot |
| Exeggcute | 5.00% | 35 | Native / custom slot |
| Hypno | 5.00% | 37–40 | Native / custom slot |
| Slowpoke | 5.00% | 31 | Native / custom slot |
| Venomoth | 5.00% | 37–40 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 95.00% | 5–40 | Native / custom slot |
| Slowbro | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 60.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |
| Poliwag | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Goldeen | 40.00% | 15–25 | Native / custom slot |
| Seaking | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-232"></a>
## Three Island Bond Bridge

Source map: MAP_THREE_ISLAND_BOND_BRIDGE.

### Source variant 1: sThreeIslandBondBridge_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgey | 30.00% | 29–32 | Native / custom slot |
| Oddish | 20.00% | 31 | Native / custom slot |
| Pidgeotto | 15.00% | 34–40 | Native / custom slot |
| Gloom | 10.00% | 36 | Native / custom slot |
| Meowth | 10.00% | 31 | Native / custom slot |
| Persian | 5.00% | 37–40 | Native / custom slot |
| Psyduck | 5.00% | 31 | Native / custom slot |
| Venonat | 5.00% | 34 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Seadra | 4.00% | 25–35 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sThreeIslandBondBridge_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Pidgey | 30.00% | 29–32 | Native / custom slot |
| Bellsprout | 20.00% | 31 | Native / custom slot |
| Pidgeotto | 15.00% | 34–40 | Native / custom slot |
| Meowth | 10.00% | 31 | Native / custom slot |
| Weepinbell | 10.00% | 36 | Native / custom slot |
| Persian | 5.00% | 37–40 | Native / custom slot |
| Slowpoke | 5.00% | 31 | Native / custom slot |
| Venonat | 5.00% | 34 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 95.00% | 5–40 | Native / custom slot |
| Tentacruel | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 80.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Kingler | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-233"></a>
## Three Island Port

Source map: MAP_THREE_ISLAND_PORT.

### Source variant 1: sThreeIslandPort_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Dunsparce | 100.00% | 5–35 | Native / custom slot |

### Source variant 2: sThreeIslandPort_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Dunsparce | 100.00% | 5–35 | Native / custom slot |

---

<a id="area-234"></a>
## Two Island Cape Brink

Source map: MAP_TWO_ISLAND_CAPE_BRINK.

### Source variant 1: sTwoIslandCapeBrink_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Oddish | 30.00% | 30–32 | Native / custom slot |
| Spearow | 20.00% | 31 | Native / custom slot |
| Gloom | 15.00% | 36–38 | Native / custom slot |
| Fearow | 10.00% | 36 | Native / custom slot |
| Meowth | 10.00% | 31 | Native / custom slot |
| Golduck | 5.00% | 37–40 | Native / custom slot |
| Persian | 5.00% | 37–40 | Native / custom slot |
| Psyduck | 5.00% | 31 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 95.00% | 5–40 | Native / custom slot |
| Golduck | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sTwoIslandCapeBrink_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 21)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Bellsprout | 30.00% | 30–32 | Native / custom slot |
| Spearow | 20.00% | 31 | Native / custom slot |
| Weepinbell | 15.00% | 36–38 | Native / custom slot |
| Fearow | 10.00% | 36 | Native / custom slot |
| Meowth | 10.00% | 31 | Native / custom slot |
| Persian | 5.00% | 37–40 | Native / custom slot |
| Slowbro | 5.00% | 37–40 | Native / custom slot |
| Slowpoke | 5.00% | 31 | Native / custom slot |

### Surf (base encounter-frequency setting: 2)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 95.00% | 5–40 | Native / custom slot |
| Slowbro | 5.00% | 35–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 20)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-235"></a>
## Underwater Route124

Source map: MAP_UNDERWATER_ROUTE124.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Clamperl | 65.00% | 20–35 | Native / custom slot |
| Chinchou | 30.00% | 20–30 | Native / custom slot |
| Relicanth | 5.00% | 30–35 | Native / custom slot |

---

<a id="area-236"></a>
## Underwater Route126

Source map: MAP_UNDERWATER_ROUTE126.

### Surf (base encounter-frequency setting: 4)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Clamperl | 65.00% | 20–35 | Native / custom slot |
| Chinchou | 30.00% | 20–30 | Native / custom slot |
| Relicanth | 5.00% | 30–35 | Native / custom slot |

---

<a id="area-237"></a>
## Vermilion City

Source map: MAP_VERMILION_CITY.

### Source variant 1: sVermilionCity_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 60.00% | 5–15 | Native / custom slot |
| Krabby | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Horsea | 44.00% | 15–35 | Native / custom slot |
| Shellder | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 1.00% | 25–35 | Native / custom slot |

### Source variant 2: sVermilionCity_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Tentacool | 100.00% | 5–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 60.00% | 5–15 | Native / custom slot |
| Horsea | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Krabby | 40.00% | 15–25 | Native / custom slot |
| Staryu | 40.00% | 15–25 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Horsea | 4.00% | 25–35 | Native / custom slot |
| Slowpoke | 1.00% | 25–35 | Native / custom slot |

---

<a id="area-238"></a>
## Viridian City

Source map: MAP_VIRIDIAN_CITY.

### Source variant 1: sViridianCity_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Psyduck | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Psyduck | 5.00% | 15–35 | Native / custom slot |

### Source variant 2: sViridianCity_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Surf (base encounter-frequency setting: 1)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Slowpoke | 100.00% | 20–40 | Native / custom slot |

### Old Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Magikarp | 100.00% | 5 | Native / custom slot |

### Good Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 60.00% | 5–15 | Native / custom slot |
| Goldeen | 20.00% | 5–15 | Native / custom slot |
| Magikarp | 20.00% | 5–15 | Native / custom slot |

### Super Rod (base encounter-frequency setting: 10)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Poliwag | 40.00% | 15–25 | Native / custom slot |
| Poliwhirl | 40.00% | 20–30 | Native / custom slot |
| Gyarados | 15.00% | 15–25 | Native / custom slot |
| Slowpoke | 5.00% | 15–35 | Native / custom slot |

---

<a id="area-239"></a>
## Viridian Forest

Source map: MAP_VIRIDIAN_FOREST.

### Source variant 1: sViridianForest_FireRed

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 14)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Caterpie | 40.00% | 3–5 | Native / custom slot |
| Weedle | 40.00% | 3–5 | Native / custom slot |
| Kakuna | 10.00% | 4–6 | Native / custom slot |
| Metapod | 5.00% | 5 | Native / custom slot |
| Pikachu | 5.00% | 3–5 | Native / custom slot |

### Source variant 2: sViridianForest_LeafGreen

This is a separate source table. Availability can depend on game mode or special flags.

### Grass / cave (base encounter-frequency setting: 14)

| Pokémon | Chance | Levels | Source |
|---|---:|---:|---|
| Caterpie | 40.00% | 3–5 | Native / custom slot |
| Weedle | 40.00% | 3–5 | Native / custom slot |
| Metapod | 10.00% | 4–6 | Native / custom slot |
| Kakuna | 5.00% | 5 | Native / custom slot |
| Pikachu | 5.00% | 3–5 | Native / custom slot |

---

