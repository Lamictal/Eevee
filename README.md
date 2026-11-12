# Eevee: 171 Forms

### A bigger Eevee adventure in Pokémon Emerald

**171 Eeveelution forms. All 18 Pokémon types. The original Hoenn adventure.**

Explore Hoenn with the usual wild Pokémon **plus a huge family of Eevee evolutions**, ranging from single-type favorites to unusual dual-type combinations. Catch them in habitats across the region or choose a second type by using a special item.

**Status:** Experimental alpha · **Platform:** Game Boy Advance · **Latest successful build:** Stage 12 · **Gameplay QA:** In progress

---

## Download and play

### [⬇️ DOWNLOAD THE LATEST ALPHA ZIP](https://github.com/Lamictal/Eevee/actions/runs/43279472956/artifacts/13972053637)

**[New to GitHub? Read the easy download and setup guide.](DOWNLOAD.md)**

The ZIP is named **Eevee-All171-ItemEvolutions-Alpha-GBA**. Extract it, then open the included **.gba** file in a compatible Game Boy Advance emulator. **Start a new game** and keep your old saves backed up.

> **Alpha access warning:** This is a **temporary GitHub Actions download**, retained for 14 days, not a public one-click release. The repository is **currently private**: people without access cannot download it, even with this link. Once distribution permissions and release testing are resolved, the long-term plan is an easier-to-share **ROM patch release**, rather than public distribution of the complete commercial game ROM.
>
> If that specific build expires, use the **[latest successful 171-form workflow run](https://github.com/Lamictal/Eevee/actions/workflows/eevee-full171-build.yml?query=branch%3Astage8e-cloud-prototype)** and select the alpha ZIP under **Artifacts**.

## What's in the game?

- **171 Eeveelution forms:** 18 single-type and 153 unique dual-type combinations, including the eight official Eeveelutions.
- **Keep the regular Pokémon:** the original Hoenn story and normal Pokémon remain, rather than being replaced by Eevees.
- **Eevee from the beginning:** pick Eevee from Professor Birch's bag (replacing the Treecko choice in this alpha), or find one on Routes 101, 102, 104 and 117.
- **Wild single types:** all 18 single-type forms appear in locations suited to their type, including forests, caves, mountains and spooky areas.
- **Rare wild duals:** nine different dual-type forms have especially rare late-game encounters. The others are designed to be obtained through evolution.
- **Choose the second type:** use the appropriate type-boosting item to evolve one of 18 single-type forms into a dual type. There are **306 item routes** targeting all 153 unique dual forms.
- **Helpful features:** move-effectiveness hints, numeric IV/EV information, and provisional following Pokémon and party icons.

### How dual-type evolution works

1. Get any **single-type Eeveelution**.
2. Level it to **38+** and earn **at least six Hoenn badges**.
3. In your Bag, **Use** the booster item representing the second type you want to add.

For example, **Aerieon (Flying) + Silver Powder (Bug) → Aerartheon (Flying/Bug)**. The reverse route, **Artheon (Bug) + Sharp Beak (Flying)**, targets the same dual-type Pokémon.

The item effect and all 306 routes were checked automatically in Stage 12, but **not every possible in-game evolution has been emulator-tested yet**.

**[Full evolution item and location guide](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_FIELD_GUIDE.md)**

## Where can I find Eevee?

| Location | How to get Eevee |
|---|---|
| Professor Birch's starter bag | Choose Eevee instead of Treecko |
| Route 101 | 5% wild encounter |
| Route 102 | 10% wild encounter |
| Route 104 | 5% wild encounter |
| Route 117 | 5% wild encounter |

For the other Eeveelutions, see the **[full wild encounter guide](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_FIELD_GUIDE.md)**. Regular Pokémon remain at least 90% of land encounters in the modified habitat tables.

## Evolution items and shops

| Location | Examples of new items |
|---|---|
| **Oldale** | Sky Catalyst |
| **Rustboro** | Fire, Water and Thunder Stones; Neutral, Swarm and Stone Catalysts |
| **Slateport** | Valor and Venom Catalysts; Silk Scarf, Mystic Water, Miracle Seed |
| **Mauville** | Alloy and Earth Catalysts; Leaf and Ice Stones, Magnet, Twisted Spoon |
| **Lavaridge** | Charcoal, Hard Stone, Soft Sand |
| **Fortree** | Spirit and Dragon Catalysts; Flying/Bug/Ghost/Dark/Fighting/Poison/Steel boosters |
| **Lilycove Department Store, 4F** | **All 18 second-type boosters** and nine first-stage custom Catalysts (Sky remains in Oldale) |

See **[the full item-by-type chart](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/EEVEE_FIELD_GUIDE.md#5-single-type-form--any-dual-type-choose-the-second-type)** for the exact item needed to evolve each form.

## Is it finished?

**It's a working build, not a verified complete game.** Stage 12 compiled successfully and passed its automated evolution-route checks. However, starter progression, all evolution-item behavior, save/reload, party icons, follower art and full story progression still need emulator testing.

We're working toward a **friend-playable Beta 1**, followed by polish and a stable v1.0.

- **[Known limitations](KNOWN_ISSUES.md)**: what is and isn't tested
- **[Beta 1 roadmap](https://github.com/Lamictal/Eevee/blob/stage8e-cloud-prototype/BETA1_RELEASE_PLAN.md)**: what's next
- **[Report a bug](https://github.com/Lamictal/Eevee/issues/new/choose)**: use the simple bug report template
- **[Development source](https://github.com/Lamictal/Eevee/tree/stage8e-cloud-prototype)**: build scripts, changes and project history
- **[Contributing and access](CONTRIBUTING.md)**: how to send suggestions without getting edit rights

## Credits and legal notes

This is an **unofficial, noncommercial Pokémon fan project**, built using the open-source [pokeemerald-expansion](https://github.com/rh-hideout/pokeemerald-expansion) engine and art sourced from *Oops! All Eevees!* for development. Pokémon and associated trademarks and characters belong to their respective owners. This project is not affiliated with or endorsed by Nintendo, Game Freak or The Pokémon Company.

**Rights to publicly redistribute the third-party Eeveelution sprites have not been verified.** Public code access does not grant anyone a license to reuse that artwork, and a public release should use an appropriate patch rather than hosting a full commercial game ROM.

---
*Built for Eevee fans who thought eight evolutions was a suspiciously low number.*
