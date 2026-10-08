# SERVICES.md: every page, its URL and target keyword

Keyword source: keywords/Houston-AC-Heating-Keywords.xlsx (Ubersuggest, US, pulled Oct 8 2026).
Figures are monthly volume / SEO difficulty. The full assignment of all 577 keywords (target,
supporting or deliberately unused) is in docs/keyword-plan.md. Every URL the live site had is KEPT at
the same path; nothing is moved. "Near me" figures are national and never treated as Houston demand.

## Services (Prompt 9, one page each)

| # | Service | URL | Target keyword (vol/SD) | Main supporting keywords | Status |
|---|---|---|---|---|---|
| 1 | AC Repair | /ac-repair/ | ac repair houston (2,900/48) | hvac repair houston (390/48), ac repair today (110/14), how long does ac repair take (50/11) | existing URL, rebuilt |
| 2 | Air Conditioning Repair | /air-conditioning-repair/ | air conditioning repair in houston (5,400/17) | houston air conditioner repair (4,400/39), air conditioning repair houston (2,900/49), air conditioning in houston (880/18) | NEW real page (old rule sent it to /ac-repair/) |
| 3 | Emergency AC Repair (24/7) | /emergency-ac-repair/ | 24 hour ac repair houston tx (720/28) | 24 hour ac repair houston (260/25), emergency ac repair houston (90/20), "is a broken ac an emergency" questions (130 combined) | existing URL, rebuilt |
| 4 | AC Installation and Replacement | /ac-installation/ | ac installation houston tx (590/32) | ac installation houston (390/27), hvac installation houston (170/44), hvac replacement houston (110/33), ac installation cost (5,400/39 national) | existing URL, rebuilt |
| 5 | Furnace Repair | /furnace-repair/ | furnace repair houston (210/37) | repair furnace near me (74,000 national) | NEW real page (old rule sent it to /ac-repair/) |
| 6 | Heating Repair (heat pumps, electric heat) | /heating-repair/ | heating repair houston (90/47) | heating and cooling houston tx (30/53), heating repair near me (40,500 national) | NEW |
| 7 | HVAC Tune-Up and Maintenance | /hvac-tune-up/ | ac maintenance houston (170/40) | hvac service houston (590/40), how often hvac service (260/21), how often air conditioner service (210/17), how often furnace maintenance (210/18) | existing URL, rebuilt |
| 8 | Commercial HVAC | /commercial-hvac/ | commercial hvac houston tx (140/32) | commercial ac repair houston (70/19) | NEW |

## Guides (researched question pages)

| # | Guide | URL | Target keyword (vol/SD) | Status |
|---|---|---|---|---|
| 1 | How much does AC repair cost | /ac-repair-cost.html | how much does an air conditioner repair cost (1,000/40) | existing URL, rebuilt |
| 2 | AC running but not cooling | /ac-not-cooling.html | why did ac stop working (20/23); how to fix my air conditioning (390/63) | existing URL, rebuilt |
| 3 | AC leaking water | /ac-leaking-water.html | (no direct row; existing indexed URL kept) | existing URL, rebuilt |
| 4 | Repair or replace | /repair-or-replace-ac/ | repair or replace furnace (50/18) | NEW |
| 5 | Is an HVAC tune-up worth it | /is-hvac-tune-up-worth-it/ | is hvac tune up worth it (140/19) | NEW |
| 6 | What an HVAC tune-up includes | /hvac-tune-up-checklist/ | what is a hvac tune up (110/15); what does hvac tune up include (70/18) | NEW |
| 7 | How to choose an HVAC company in Houston | /hvac-company/ | hvac companies in houston (1,600/29); houston hvac companies (1,300/38); houston ac companies (590/44) | NEW |
| 8 | Water heater repair: who to call | /water-heater-repair.html | water heater repair houston tx (590/20) | existing URL, rebuilt as an honest guide (see docs/decisions.md) |
| 9 | Free AC refrigerant guide (PDF) | /free-ac-guide/ | none (book download page) | existing URL, form removed |

## Service areas (Prompt 11, one page each, all at /ac-repair/<city>-tx.html)

| # | City | County | Target keyword (vol/SD) |
|---|---|---|---|
| 1 | The Woodlands | Montgomery, Harris | ac repair the woodlands (1,600/29) |
| 2 | Cypress | Harris | ac repair cypress (1,000/13) |
| 3 | Spring | Harris, Montgomery | ac repair spring texas (1,000/12) |
| 4 | Humble | Harris | ac repair humble texas (880/14) |
| 5 | Katy | Harris, Fort Bend, Waller | a c repair katy (720/32) |
| 6 | Sugar Land | Fort Bend | sugar land ac repair (480/27) |
| 7 | Pearland | Brazoria, Harris, Fort Bend | ac repair pearland tx (480/19) |
| 8 | Pasadena | Harris | a c repair pasadena (260/25) |
| 9 | League City | Galveston, Harris | ac repair league city tx (140/12) |
| 10 | Missouri City | Fort Bend, Harris | ac repair missouri city tx (70/22) |
| 11 | Kingwood | Harris, Montgomery | under 30/mo (kept: existing URL) |
| 12 | Baytown | Harris, Chambers | not in data (kept: existing URL) |
| 13 | Conroe | Montgomery | not in data (kept: existing URL) |
| 14 | Tomball | Harris | not in data (kept: existing URL) |
| 15 | Friendswood | Galveston, Harris | not in data (kept: existing URL) |
| 16 | Richmond | Fort Bend | not in data (kept: existing URL) |
| 17 | Fulshear | Fort Bend | not in data (kept: existing URL) |
| 18 | Fresno | Fort Bend | not in data (kept: existing URL) |

No other Houston-area place in the data reaches 30 searches a month, so no new city pages were added.

## Core pages

| Page | URL | Target keyword (vol/SD) | Status |
|---|---|---|---|
| Home | / | hvac houston (2,400/55); ac in houston (1,000/51); ac unit houston (720/36) | existing URL |
| Services overview (Prompt 8) | /services/ | hvac services in houston tx (720/52) | existing URL |
| Service areas overview (Prompt 10) | /service-areas/ | none (hub for the 18 city pages) | NEW |
| How it works | /how-it-works/ | none (support) | NEW |
| About, FAQ, Contact | /about/ /faq/ /contact/ | none (support) | existing URLs |
| Privacy, Terms, 404 | /privacy-policy.html /terms.html /404.html | none | existing URLs |

## Redirects (src/static/_redirects, copied to dist/_redirects)
Kept: the Sep 11 2026 wildcards for retired templated sub-pages and the Sep 25 retired blog posts
(targets updated to the .html guide URLs and new guides). Removed: the two Sep 11 rules that sent
/furnace-repair/ and /air-conditioning-repair/ to /ac-repair/ (both are real pages now). Added:
/contact/thanks/ to /contact/ and /free-ac-guide/thanks/ to /free-ac-guide/ (forms retired).
