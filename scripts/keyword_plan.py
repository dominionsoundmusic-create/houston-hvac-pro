#!/usr/bin/env python3
"""Assign every keyword in keywords/Houston-AC-Heating-Keywords.xlsx to a page (target or supporting)
or to the deliberately-unused list with a reason. Writes docs/keyword-plan.md.

Usage: python3 scripts/keyword_plan.py
"""
import re
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent

PAGES = {
    "home": "/", "services": "/services/", "areas": "/service-areas/", "ac-repair": "/ac-repair/",
    "acr": "/air-conditioning-repair/", "emergency": "/emergency-ac-repair/", "install": "/ac-installation/",
    "furnace": "/furnace-repair/", "heating": "/heating-repair/", "tuneup": "/hvac-tune-up/",
    "commercial": "/commercial-hvac/", "cost": "/ac-repair-cost.html", "notcooling": "/ac-not-cooling.html",
    "leaking": "/ac-leaking-water.html", "ror": "/repair-or-replace-ac/", "worth": "/is-hvac-tune-up-worth-it/",
    "checklist": "/hvac-tune-up-checklist/", "company": "/hvac-company/", "waterheater": "/water-heater-repair.html",
}
CITIES = {"katy": "katy-tx", "sugar land": "sugar-land-tx", "cypress": "cypress-tx", "pearland": "pearland-tx",
          "woodlands": "the-woodlands-tx", "humble": "humble-tx", "pasadena": "pasadena-tx",
          "league city": "league-city-tx", "missouri city": "missouri-city-tx", "kingwood": "kingwood-tx",
          "77095": "cypress-tx", "77429": "cypress-tx", "77346": "humble-tx"}

# Primary target keyword of each page (the rest of its assigned keywords are supporting).
TARGETS = {
    "hvac houston": "home", "hvac services in houston tx": "services", "ac repair houston": "ac-repair",
    "air conditioning repair in houston": "acr", "24 hour ac repair houston tx": "emergency",
    "ac installation houston tx": "install", "furnace repair houston": "furnace", "heating repair houston": "heating",
    "ac maintenance houston": "tuneup", "commercial hvac houston tx": "commercial",
    "how much does an air conditioner repair cost": "cost", "why did ac stop working": "notcooling",
    "repair or replace furnace": "ror", "is hvac tune up worth it": "worth", "what is a hvac tune up": "checklist",
    "hvac companies in houston": "company", "water heater repair houston tx": "waterheater",
    "ac repair the woodlands": "city:the-woodlands-tx", "ac repair cypress": "city:cypress-tx",
    "ac repair spring texas": "city:spring-tx", "ac repair humble texas": "city:humble-tx",
    "a c repair katy": "city:katy-tx", "sugar land ac repair": "city:sugar-land-tx",
    "ac repair pearland tx": "city:pearland-tx", "a c repair pasadena": "city:pasadena-tx",
    "ac repair league city tx": "city:league-city-tx", "ac repair missouri city tx": "city:missouri-city-tx",
}

U_CAR = "vehicle air conditioning (car, truck, RV, bus), not home HVAC"
U_JOBS = "HVAC careers, pay, training or trade events, not a homeowner service"
U_BRAND = "names a specific company or brand (CLAUDE.md rule 3: never name an HVAC company)"
U_PLACE = "a place outside greater Houston (rule 4)"
U_OFF = "off-topic: not about heating or cooling a home"
U_SUPPLY = "trade parts, supply or wholesale, not a homeowner service"
U_DUCT = "duct or vent cleaning and mold work are not offered (INTAKE.md section 2)"
U_BANNED = "built on a banned claim (free estimate, same-day, cheapest) that the site may not make"
U_NOTOFFERED = "a service the line does not take (INTAKE.md section 2)"
U_AMBIG = "ambiguous or not clearly a Houston-area home HVAC search"

RULES = [
    # order matters: first match wins
    (r"\b(car|auto|automotive|semi truck|rv|bus|differential|midas|vehicle)\b|in my car|my ac car", ("unused", U_CAR)),
    (r"\bjobs?\b|salary|\bpay\b|make in|\bmake\b|apprentice|union|school|training|classes|course|programs?\b|certification|careers?|helper|job fair|convention|conference|technician salary|hvac tech houston|hvac technician houston|hvac trade houston|business for sale|companies for sale|hvac business houston", ("unused", U_JOBS)),
    (r"turbo|atlas|h town|comfort star|air max|latinos|west houston auto|ncr electronics|glacialair|a1 plus|preeminent|champion|john moore|carrier|helios|daikin|goodman|lennox|\bgree\b|hvac alliance|ferguson|reece|winsupply|\bww hvac|weeks hvac|brandt|kilgore|global hvac|graco|mirage|ems hvac|1st hvac|houston's heating|air conditioning heating of houston|sugar land a c|ac and heating pros|ac & heating repair co|emergency ac of houston|ac nation|ac pro houston|247 ac|houston ac repair pros|houston hvac finder|hvac direct|hvac rntl|recycling usa|ruben|paco|racing", ("unused", U_BRAND)),
    (r"in dallas|leander|jefferson city|bangalore|karachi|san antonio|mckinney|killeen|corpus christi|spring branch|dripping springs|sulphur springs|big spring|carrizo|hughes springs|bay city|ohio|newark|wilmington|gadsden|dyer|houston mo\b|houston pa\b|obx|ketchum|hailey|indio|houston mn|grifton|wapak|westpark", ("unused", U_PLACE)),
    (r"duct cleaning|vent cleaning|hvac cleaning|mold", ("unused", U_DUCT)),
    (r"free estimate|same day|cheapest|cheap ac", ("unused", U_BANNED)),
    (r"pool heater|portable air conditioner|window unit|pcb|phone repair", ("unused", U_NOTOFFERED)),
    (r"supply|parts|wholesale|warehouse|supplier|manufacturer|rentals|recycle|\bstore\b|ac filters houston", ("unused", U_SUPPLY)),
    (r"plastics|ac dc|hotel|marriott|lumber|kitchen|lounge|barbershop|houston fc|gutters|outlets|safe|good place|what time|directions|known for|weather|temperature|killing fields|health centre|what happened|big companies|where is the|ac advance|ac performance|ac houston 8|vandal|tech killed|houston hvac ron|houston hvac photos|ac downtown|houston downtown|ac houston downtown|how to repair spring|ac of houston|ac plumbing houston|houston ac law|houston ac ordinance|hvac sales houston|can hvac$|commercial hvac of houston", ("unused", U_OFF)),
    # city pages
    (r"katy", ("city", "katy-tx")), (r"sugar land", ("city", "sugar-land-tx")), (r"cypress|77095|77429", ("city", "cypress-tx")),
    (r"pearland", ("city", "pearland-tx")), (r"woodlands", ("city", "the-woodlands-tx")), (r"humble|77346", ("city", "humble-tx")),
    (r"pasadena", ("city", "pasadena-tx")), (r"league city", ("city", "league-city-tx")), (r"missouri city", ("city", "missouri-city-tx")),
    (r"kingwood", ("city", "kingwood-tx")), (r"\bspring\b", ("city", "spring-tx")),
    (r"\b77573\b", ("city", "league-city-tx")), (r"\b77(092|080)\b", ("page", "acr")),
    # topics
    (r"water heater|can hvac do plumbing", ("page", "waterheater")),
    (r"tune up|tune-up|tune ups|tuned up", None),  # handled below
    (r"emergency|24 hour|24 7|considered an emergency|an emergency", ("page", "emergency")),
    (r"furnace", None),
    (r"heating|can hvac heat|heaters|geothermal", ("page", "heating")),
    (r"commercial", ("page", "commercial")),
    (r"zoned|installation|install|replacement|replaced|replace|hvac city of houston|houston hvac permit|ac sales", ("page", "install")),
    (r"cost|how much|prices|charge per hour|expensive|affordable|hvac repair pay", ("page", "cost")),
    (r"leak", ("page", "leaking")),
    (r"stop working|stopped working|fix my air|how to fix", ("page", "notcooling")),
    (r"how often|maintenance|service houston|inspection|checked", ("page", "tuneup")),
    (r"companies|company|contractors|best |reviews|reddit|license|ac service houston reviews|largest|who repairs|who fixes|who fix|where to repair|who can fix|hvac houston pay", ("page", "company")),
    (r"air conditioning repair|air conditioner repair|air conditioning service|air conditioning in houston|what air conditioning services|ac unit repair|hvac air conditioner", ("page", "acr")),
    (r"hvac service|hvac services|services in houston", ("page", "services")),
    (r"repair|fixer|repairing|ac repair|aircon", ("page", "ac-repair")),
    (r"ac fix houston|ac guy houston|ac man houston|hvac north houston|hvac specialist houston|hvac houston|houston hvac|ac in houston|ac unit houston|do hvac houston|houston ac|ac houston|heating and cooling houston|houston air conditioning|ac sugar|sugar land ac", ("page", "home")),
]


def classify(kw):
    k = kw.lower()
    if k in TARGETS:
        t = TARGETS[k]
        return ("city", t[5:]) if t.startswith("city:") else ("page", t)
    for pat, res in RULES:
        if re.search(pat, k):
            if res is None:
                if "furnace" in k:
                    if re.search(r"how often furnace (maintenance|inspection|check)", k):
                        return ("page", "tuneup")
                    if re.search(r"replace|replaced", k):
                        return ("page", "ror")
                    if "cost" in k:
                        return ("page", "cost")
                    return ("page", "furnace")
                if re.search(r"include|what is|what does", k):
                    return ("page", "checklist")
                if re.search(r"worth|necessary|need tune|do hvac need", k):
                    return ("page", "worth")
                return ("page", "tuneup")
            return res
    return ("unused", U_AMBIG)


def main():
    wb = openpyxl.load_workbook(ROOT / "keywords" / "Houston-AC-Heating-Keywords.xlsx", read_only=True)
    rows = list(wb["ALL"].iter_rows(values_only=True))[1:]
    seen = {}
    for seed, kw, typ, vol, sd, cpc, pd in rows:
        if kw not in seen or (vol or 0) > (seen[kw][3] or 0):
            seen[kw] = (seed, kw, typ, vol or 0, sd, cpc)
    assigned = defaultdict(list)
    unused = defaultdict(list)
    for seed, kw, typ, vol, sd, cpc in sorted(seen.values(), key=lambda r: -r[3]):
        kind, val = classify(kw)
        near = " (near me: national volume, supporting only)" if "near me" in kw or "in my area" in kw else ""
        if kind == "unused":
            unused[val].append((kw, vol, sd, typ))
        else:
            url = PAGES[val] if kind == "page" else f"/ac-repair/{val}.html"
            role = "TARGET" if kw.lower() in TARGETS else "supporting"
            assigned[url].append((kw, vol, sd, typ, role, near))
    total = sum(len(v) for v in assigned.values()) + sum(len(v) for v in unused.values())
    out = ["# Keyword plan (Houston Air & Heating, Oct 8 2026)", "",
           "Source: keywords/Houston-AC-Heating-Keywords.xlsx (Ubersuggest, United States, pulled Oct 8 2026),",
           f"ALL tab, {total} unique keywords. Generated by `python3 scripts/keyword_plan.py`; every keyword is either",
           "assigned to one page (as its TARGET or a supporting keyword) or listed as deliberately unused with a reason.",
           "", "Rules applied:",
           "- \"Near me\" and \"in my area\" terms carry national volume. They are supporting keywords only and are never",
           "  read as proof of Houston demand.",
           "- City pages exist for every Houston-area city with a 30+/mo keyword (Katy, Sugar Land, Cypress, Pearland,",
           "  The Woodlands, Spring, Humble, Pasadena, League City, Missouri City) plus the 8 other existing city URLs.",
           "  No other Houston-area place in the data reaches 30/mo (Kingwood, Heights, Midtown and west Houston rows are 0;",
           "  \"spring branch tx\" and \"furnace repair westpark\" are ambiguous place names and are left unused).",
           "- Heat pumps: no heat pump keyword appears in the data, so heat pumps are covered on /heating-repair/ rather than",
           "  on a page of their own.",
           "- Volume / SD = monthly searches / Ubersuggest SEO difficulty.", ""]
    out.append(f"Assigned: {sum(len(v) for v in assigned.values())}. Unused: {sum(len(v) for v in unused.values())}.")
    out.append("")
    out.append("## Assigned keywords by page")
    order = list(PAGES.values()) + sorted(u for u in assigned if u.startswith("/ac-repair/") and u.endswith(".html"))
    for url in order:
        if url not in assigned:
            continue
        items = sorted(assigned[url], key=lambda r: (r[4] != "TARGET", -r[1]))
        out += ["", f"### {url}", "", "| Keyword | Volume | SD | Type | Role |", "|---|---:|---:|---|---|"]
        for kw, vol, sd, typ, role, near in items:
            out.append(f"| {kw} | {vol:,} | {sd} | {typ} | {role}{near} |")
    out += ["", "## Deliberately unused", ""]
    for reason, items in sorted(unused.items(), key=lambda kv: -len(kv[1])):
        out += [f"### {reason} ({len(items)})", "", "| Keyword | Volume | SD | Type |", "|---|---:|---:|---|"]
        for kw, vol, sd, typ in sorted(items, key=lambda r: -r[1]):
            out.append(f"| {kw} | {vol:,} | {sd} | {typ} |")
        out.append("")
    (ROOT / "docs" / "keyword-plan.md").write_text("\n".join(out) + "\n")
    print(f"{total} keywords: {sum(len(v) for v in assigned.values())} assigned, {sum(len(v) for v in unused.values())} unused")
    missing_targets = [k for k in TARGETS if k not in {r[1] for r in seen.values()}]
    if missing_targets:
        print("TARGETS not in data:", missing_targets)


if __name__ == "__main__":
    main()
