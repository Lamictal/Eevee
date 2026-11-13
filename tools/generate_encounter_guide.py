#!/usr/bin/env python3
"""Build a browsable, probability-weighted encounter guide from the compiled ROM source.

Rates are probabilities conditioned on generating a wild Pokemon by the named
method, not per-step spawn odds or capture probabilities. This incorporates
the Stage 15 land-only bonus replacement pools and Stage 11/custom land slots.
"""
import argparse
import json
import re
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

METHODS = (
    ("land_mons", "Grass / cave"),
    ("water_mons", "Surf"),
    ("rock_smash_mons", "Rock Smash"),
    ("old_rod", "Old Rod"),
    ("good_rod", "Good Rod"),
    ("super_rod", "Super Rod"),
)
SPECIAL = {
    "HO_OH": "Ho-Oh",
    "MR_MIME": "Mr. Mime",
    "MR_RIME": "Mr. Rime",
    "MIME_JR": "Mime Jr.",
    "PORYGON_Z": "Porygon-Z",
    "TYPE_NULL": "Type: Null",
    "FARFETCHD": "Farfetch'd",
    "SIRFETCHD": "Sirfetch'd",
    "FLABEBE": "Flabébé",
}
def pretty(species):
    name = species.removeprefix("SPECIES_")
    return SPECIAL.get(name, name.replace("_", " ").title())

def area_name(mapid):
    s = mapid.removeprefix("MAP_")
    s = re.sub(r"^ROUTE(\d+)", r"Route \1", s)
    s = s.replace("_", " ").title()
    s = re.sub(r"\bMt\b", "Mt.", s)
    s = s.replace("Ssan ne", "S.S. Anne")
    return s

def fmt_chance(value):
    pct = float(value * 100)
    if pct >= 1:
        return f"{pct:.2f}%".rstrip("0").rstrip(".") + ("" if False else "") if False else f"{pct:.2f}%"
    if pct >= .01:
        return f"{pct:.3f}%"
    return f"{pct:.5f}%"

def rates_by_type(fields):
    base = {x["type"]: x for x in fields}
    for kind in ("land_mons", "water_mons", "rock_smash_mons", "fishing_mons"):
        if kind not in base:
            raise ValueError(f"Encounter table lacks {kind} weights")
    result = {k: tuple(v["encounter_rates"]) for k,v in base.items()}
    fishing = base["fishing_mons"]
    for name, indices in fishing["groups"].items():
        weights = [result["fishing_mons"][i] for i in indices]
        if sum(weights) != 100:
            raise ValueError(f"{name}: encounter slot weights total {sum(weights)}")
        result[name] = tuple(indices)
    for k in ("land_mons", "water_mons", "rock_smash_mons"):
        if sum(result[k]) != 100:
            raise ValueError(f"{k}: encounter slot weights do not total 100")
    return result

def entries_for_method(entry, key, weights, groups, bonus, minimum, rare_pct):
    source_key = "fishing_mons" if key.endswith("_rod") else key
    if source_key not in entry:
        return None
    table = entry[source_key]
    slots = table["mons"]
    if len(slots) != len(weights[source_key]):
        raise ValueError(f"{entry['map']} {source_key}: unexpected slot count")
    if key in groups:
        indices = groups[key]
    else:
        indices = tuple(range(len(slots)))
    numbers = [weights[source_key][index] for index in indices]
    if sum(numbers) != 100:
        raise ValueError(f"{entry['map']} {key}: slot weights sum {sum(numbers)}")
    land = key == "land_mons"
    common = bonus.get("common", []) if land else []
    rare = bonus.get("rare", []) if land else []
    base_bonus = Fraction(bonus.get("bonus_chance_percent", 0), 100) if common else Fraction(0)
    base_rare = Fraction(rare_pct, 100) if rare else Fraction(0)
    native_factor = (1-base_rare)*(1-base_bonus)
    records = defaultdict(lambda: {"chance": Fraction(0), "min": 999, "max": 0, "sources": set()})
    for i,weight in zip(indices,numbers):
        slot = slots[i]
        name = slot["species"].removeprefix("SPECIES_")
        rec = records[name]
        rec["chance"] += Fraction(weight,100)*native_factor
        rec["min"] = min(rec["min"], slot["min_level"])
        rec["max"] = max(rec["max"], slot["max_level"])
        rec["sources"].add("Native / custom slot")
    if land:
        base_min = min(slot["min_level"] for slot in slots)
        base_max = max(slot["max_level"] for slot in slots)
        for pool, probability, origin in (
            (rare,base_rare,"Rare bonus pool"),
            (common,(1-base_rare)*base_bonus,"National Dex bonus"),
        ):
            if not pool:
                continue
            share = probability / len(pool)
            for name in pool:
                rec = records[name]
                floor = minimum[name]
                rec["chance"] += share
                rec["min"] = min(rec["min"], max(base_min, floor))
                rec["max"] = max(rec["max"], max(base_max, floor))
                rec["sources"].add(origin)
    total = sum((x["chance"] for x in records.values()), Fraction(0))
    if total != 1:
        raise ValueError(f"{entry['map']} {key}: combined species chance is {total}, not 1")
    return sorted(records.items(), key=lambda item: (-item[1]["chance"],pretty(item[0])))

def generate(checkout, bonus_report, output):
    encounters = json.loads((checkout/"src/data/wild_encounters.json").read_text(encoding="utf-8"))
    group = next(x for x in encounters["wild_encounter_groups"] if x.get("for_maps")
                 and x.get("label") == "gWildMonHeaders")
    weights = rates_by_type(group["fields"])
    fishing_groups = {k: weights[k] for k in ("old_rod","good_rod","super_rod")}
    report = json.loads(bonus_report.read_text(encoding="utf-8"))
    if report["national_dex_species"] != 1025 or report["bonus_species"] != 1024:
        raise ValueError("Encounter balance report does not cover all 1025 species")
    habitats = report["habitats"]
    minimum = report["minimum_levels"]
    rare_pct = report["rare_encounter_chance_percent"]
    extra = [n for b in habitats.values() for n in b.get("common", []) + b.get("rare", [])]
    if len(extra) != 1024 or len(set(extra)) != 1024:
        raise ValueError("Duplicate or missing National Dex pool species")
    if set(extra) != set(minimum):
        raise ValueError("Missing minimum wild levels for bonus species")
    maps = defaultdict(list)
    for entry in group["encounters"]:
        if "map" in entry and any(k in entry for k in
                ("land_mons", "water_mons", "rock_smash_mons", "fishing_mons")):
            maps[entry["map"]].append(entry)
    if len(maps) < 180:
        raise ValueError(f"Too few wild encounter maps: {len(maps)}")

    def sort_key(mapid):
        route = re.fullmatch(r"MAP_ROUTE(\d+)", mapid)
        if route and 101 <= int(route.group(1)) <= 134:
            return (0, int(route.group(1)), mapid)
        hoenn = ("PETALBURG","RUSTURF","GRANITE","METEOR","FIERY","JAGGED","MT_PYRE",
                 "NEW_MAUVILLE","VICTORY_ROAD","SKY_PILLAR","SHOAL","SAFARI_ZONE",
                 "ARTISAN","DESERT","SEAFLOOR","MIRAGE","EVER_GRANDE","MOSSDEEP")
        return (1 if any(k in mapid for k in hoenn) else 2,0,mapid)
    map_ids = sorted(maps, key=sort_key)
    out = [
        "# Pokémon Eevee: complete wild encounter rates by area",
        "",
        "> **Automatically generated from the source of the successful Stage 15.1+ Monoamine ROM build.** "
        "These are expected encounter probabilities, **not** results from catching Pokémon in an emulator.",
        "",
        "**What the percentages mean:** If you generate a wild encounter using the stated method, "
        "the percentage is the modeled probability of encountering that species. "
        "It is *not* the probability per walking step, the catch rate, or a guarantee.",
        "",
        "**Included:** All map wild tables in the built source, grass/caves, Surf, Rock Smash, "
        "Old/Good/Super Rod, Stage 11 custom Eeveelution encounter slots, and the Stage 15 "
        "National Dex bonus pools with their actual replacement probabilities and minimum levels.",
        "",
        "**Important limitations:** The source includes alternate and Kanto/FRLG map tables, "
        "some of which may not be reachable in this Emerald-based hack. Duplicate areas are "
        "listed as separate source variants, **not** merged. Static encounters, NPC trades, "
        "gift Pokémon and scripted events are not covered. Abilities, lures, fishing-chain "
        "effects, Feebas-specific tiles, repel, alternate time-of-day tables, and special "
        "events can change practical outcomes. The displayed rates are *baseline* "
        "type-selection rates without these modifiers.",
        "",
        f"**Coverage:** {len(map_ids)} distinct maps, "
        f"{sum(len(items) for items in maps.values())} source area tables, "
        f"{len(extra)} supplementary National Dex species.",
        "",
        "## Jump to an area",
        "",
        "<details><summary>Open area index</summary>",
        "",
    ]
    for i,mapid in enumerate(map_ids):
        out.append(f"- [{area_name(mapid)}](#area-{i})")
    out += ["", "</details>", "", "## All areas", ""]
    checks = {}
    for i,mapid in enumerate(map_ids):
        area = area_name(mapid)
        out += [f'<a id="area-{i}"></a>',f"## {area}","",
                f"Source map: {mapid}.",""]
        variants = maps[mapid]
        for variant_idx,entry in enumerate(variants):
            if len(variants)>1:
                out += [f"### Source variant {variant_idx+1}: {entry.get('base_label','unnamed')}","",
                        "This is a separate source table. Availability can depend on game mode or special flags.",""]
            bonus = habitats.get(mapid,{})
            for key,label in METHODS:
                rows = entries_for_method(entry,key,weights,fishing_groups,bonus,minimum,rare_pct)
                if rows is None:
                    continue
                table_key = "fishing_mons" if key.endswith("_rod") else key
                step_rate = entry[table_key].get("encounter_rate")
                extra_label = f" (base encounter-frequency setting: {step_rate})" if step_rate is not None else ""
                out += [f"### {label}{extra_label}","",
                        "| Pokémon | Chance | Levels | Source |",
                        "|---|---:|---:|---|"]
                for name,rec in rows:
                    if rec["min"] == 999 or rec["min"]>rec["max"]:
                        raise ValueError(f"Invalid levels for {area}: {name}")
                    levels = str(rec["min"]) if rec["min"]==rec["max"] else f'{rec["min"]}–{rec["max"]}'
                    out.append(f'| {pretty(name)} | {fmt_chance(rec["chance"])} | '
                               f'{levels} | {", ".join(sorted(rec["sources"]))} |')
                out.append("")
                if mapid=="MAP_ROUTE104" and key=="land_mons":
                    checks["Route 104 grass"] = {name: fmt_chance(rec["chance"]) for name,rec in rows}
                if mapid=="MAP_ROUTE102" and key=="land_mons":
                    checks["Route 102 grass"] = {name: fmt_chance(rec["chance"]) for name,rec in rows}
        out.append("---")
        out.append("")
    for name in ("AZUMARILL","DECIDUEYE","QUILLADIN"):
        if name in checks.get("Route 104 grass", {}):
            raise ValueError(f"Unexpected early {name} on Route 104")
    if "EEVEE" not in checks.get("Route 102 grass",{}):
        raise ValueError("Route 102 Eevee was lost from native wild encounters")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(out)+"\n", encoding="utf-8")
    print(json.dumps({"areas":len(map_ids),"variants":sum(map(len,maps.values())),
                      "bytes":output.stat().st_size,
                      "route104_grass":checks.get("Route 104 grass",{}),
                      "route102_grass":checks.get("Route 102 grass",{})}))

if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout",type=Path,required=True)
    parser.add_argument("--bonus-report",type=Path,required=True)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    generate(args.checkout.resolve(), args.bonus_report, args.output)
