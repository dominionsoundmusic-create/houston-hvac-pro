# Independent fact-check (Oct 8 2026)

**What was run.** After all 45 pages were written, eight separate fact-check sub-agents (fc1 to fc8)
checked every factual claim and every cited source on every page except the 404 page, privacy and
terms (no factual claims beyond INTAKE.md). None of them wrote any page they checked. A ninth agent
first researched and expanded four thin city pages (Tomball, Fulshear, Fresno, Richmond), and those
four pages were then checked by fc8, which had not written them. Each checker edited its pages to fix
what it found, re-ran build.py, check.py and similarity.py, and wrote the claim-by-claim tables below.

**Method limit (read this).** This environment's network policy blocked direct page fetches (WebFetch
and curl to tdlr.texas.gov, census.gov, weather.gov, energy.gov, epa.gov, centerpointenergy.com,
angi.com and nearly every other source). Claims were therefore verified against WebSearch result
summaries of the named official or credible pages, usually restricted to the source's own domain, not
by opening the pages. A claim that no search could confirm was softened or removed. Business facts
were checked against INTAKE.md only. To re-verify by opening every source, allow those domains in the
environment's network settings and re-run the checkers.

| Checker | Pages | Claims checked | Confirmed | Corrected | Softened | Removed |
|---|---|---:|---:|---:|---:|---:|
| fc1 | /, /services/, /how-it-works/, /about/, /faq/, /contact/, /free-ac-guide/, /service-areas/ | 61 | 45 | 7 | 6 | 3 |
| fc2 | /ac-repair/, /air-conditioning-repair/, /emergency-ac-repair/, /furnace-repair/ | 53 | 36 | 10 | 4 | 1 |
| fc3 | /heating-repair/, /water-heater-repair.html, /ac-installation/, /commercial-hvac/ | 60 | 50 | 6 | 4 | 0 |
| fc4 | /hvac-company/, /hvac-tune-up/, /is-hvac-tune-up-worth-it/, /hvac-tune-up-checklist/ | 61 | 52 | 3 | 4 | 2 |
| fc5 | /ac-repair-cost.html, /ac-not-cooling.html, /ac-leaking-water.html, /repair-or-replace-ac/ | 58 | 46 | 6 | 4 | 2 |
| fc6 | The Woodlands, Conroe, Spring, Kingwood, Humble, Cypress, Pasadena | 86 | 54 | 11 | 14 | 6 |
| fc7 | Katy, Sugar Land, Missouri City, Pearland, Friendswood, League City, Baytown | 101 | 75 | 10 | 13 | 1 |
| fc8 | Tomball, Fulshear, Fresno, Richmond | 66 | 45 | 11 | 4 | 5 |
| **Total** | 42 pages | **546** | **403** | **64** | **53** | **20** |

(Counts are as each checker reported them; a few checkers' per-page subtotals overlap where one claim
was both corrected and re-sourced.)

**Most important fixes.** Cost figures re-matched to what Angi and This Old House publish (R-22 per
pound, one Houston row removed, one added); the DOE central AC life span corrected to 15 to 20 years;
heat pump savings wording corrected to DOE's figures; the Houston rental AC ordinance's grace period
left unnumbered because reports disagree; Beryl outage and restoration figures aligned to CenterPoint;
one CenterPoint gas leak number (888-876-5786) used everywhere; TDLR technician and complaint wording
corrected; unverifiable local claims removed (for example Humble double permit fees, Tomball "highest
point in Harris County", Kingwood's 2000 population, a Katy court finding); population figures
replaced with Census estimates where newer figures could not be found.

After all edits: check.py 0 errors and 0 warnings on 45 pages; similarity.py shows no Houston page
sharing an 8-word run with any Dallas page.

---

## Claim-by-claim tables


### fc1

# fc1 fact-check: core pages

Network note: WebFetch to weather.gov was blocked (egress). Everything else was checked through WebSearch result summaries, with no source page opened directly, except the free guide PDF. I read that from the repo with pdftotext. Business facts were checked against INTAKE.md.

## / (src/pages/index.html)
| Claim | Verdict | Source / note |
|---|---|---|
| Line is free, answered 24/7 by automated assistant, transfers to independent local company, callback details passed on, referral fee may be paid | CONFIRMED | INTAKE.md |
| IAH normal highs "about 94.5 in July and 94.9 in August" (1991-2020) | SOFTENED to "mid 90s through July and August" | Could not confirm decimals; Wikipedia/NWS normals show IAH peak daily normal 95.0 |
| Hobby normal about 100 days of 90+ per year; 2025 had 136 | CORRECTED | NWS HGX 2025 review: 145 days at 90+ in 2025, beating 142 in 2011 (KEDT/Houston Public Media, Click2Houston). Hobby figures could not be confirmed and were removed. Hobby CLA source was replaced |
| Hurricane season June 1 to Nov 30, peak around Sept 10 | CONFIRMED | NHC climatology (common knowledge) |
| Beryl landfall near Matagorda, Cat 1, early July 8 2024 | CONFIRMED | news reports (NBC, etc.) |
| CenterPoint: more than 2.2 million customers without power | CONFIRMED | CenterPoint: 2.26M impacted |
| "Eleven days to restore more than 2 million" | CORRECTED | Now reads "by July 19, eleven days later, it had restored more than 99 percent". Source is the CenterPoint tracker as of July 19 (PUC presentation, ABC13). Sources changed to the restoration updates page and the post-Beryl report |
| IAH 13 degrees on Feb 16 2021 | CONFIRMED | NWS Feb 2021 regional climate summary, Fox Weather |
| ERCOT rotating outages from early Feb 15 2021 | CONFIRMED | well known (ERCOT EEA3 at 1:25 a.m. Feb 15) |
| Texas ACR contractor license from TDLR is required | CONFIRMED | TDLR ACR, Occupations Code 1302 |
| Gas smell / CO guidance | CONFIRMED | standard safety guidance; no phone number stated on this page |
| R-454B replacing R-410A | CONFIRMED | EPA Technology Transitions |

11 claims checked: 7 confirmed, 3 corrected, 1 softened, 0 removed.

## /services/ (src/pages/services.html)
| Claim | Verdict | Source / note |
|---|---|---|
| City of Houston needs a mechanical permit for installing, repairing or replacing condensing units, plus a city inspection | CONFIRMED | Houston Permitting Center hpwcode1022 (condensing unit). Added as a source |
| Summer afternoons in the mid 90s | CONFIRMED | NWS normals |
| Texas license classes differ for commercial work | CONFIRMED | TDLR Class A/B |
| Same line takes roofing and pressure washing calls; services not offered | CONFIRMED | INTAKE.md |
| No implication that the line does work | CONFIRMED | rule 1 OK |

5 claims checked: 5 confirmed.

## /how-it-works/ (src/pages/how-it-works.html)
| Claim | Verdict | Source / note |
|---|---|---|
| Call flow (assistant, sorting question, summary, transfer, callback) | CONFIRMED | INTAKE.md |
| "The line is funded by referral fees" | SOFTENED | Now "A referral fee that the HVAC companies may pay is what keeps calling free", matching INTAKE's "may pay" |
| Performing or offering to perform ACR work counts as contracting and needs a license | CONFIRMED | Occupations Code 1302 / TDLR |
| Technicians must be registered with TDLR | CONFIRMED | TDLR technician registration |
| Complaints within two years | CONFIRMED | TDLR complaint form / Consumer Complaints at a Glance. Wording now cites the form. ComplaintForm.aspx source replaced with the at-a-glance PDF |
| Typo "Should the house is getting" | FIXED | |

5 claims checked: 4 confirmed, 0 corrected, 1 softened (typo also fixed).

## /about/ (src/pages/about.html)
| Claim | Verdict | Source / note |
|---|---|---|
| Run by Dominion Digital Group, d/b/a Houston Air & Heating | CONFIRMED | INTAKE.md (no owner named) |
| No techs, license; never repairs, quotes, schedules | CONFIRMED | INTAKE.md |
| Former different name | CONFIRMED | INTAKE.md |
| "The phone line and what it does have not changed" | REMOVED | Not in INTAKE (the old site may have shown a different number) |
| ACR license from TDLR | CONFIRMED | TDLR |

5 claims checked: 4 confirmed, 1 removed.

## /faq/ (src/pages/faq.html)
| Claim | Verdict | Source / note |
|---|---|---|
| Line facts (free, 24/7, callback, phone only, referral fee) | CONFIRMED | INTAKE.md |
| Class A any size; Class B up to 25 tons cooling and 1.5M BTU/h heating | CONFIRMED | TDLR contractor-apply page, ACR at a Glance, Occupations Code 1302.253 |
| Houston permit: contractor "must hold TDLR Class A or B and be registered" | SOFTENED | Now "licensed by TDLR and have that license registered with the city". Class A/B wording was not confirmed. Added hpwcode1022 as a source |
| CDC: have heating system serviced yearly | CONFIRMED | CDC CO guidance |
| Refrigerant sales limited to Section 608 certified techs or employers | CONFIRMED | EPA sales restriction |
| CenterPoint gas leak 888-876-5786 | CONFIRMED | CenterPoint contact page, Texas gas leak listing. Contact-us source added |
| Heat stroke: confusion, passing out, 103F+ | CONFIRMED | CDC |
| CO cannot be seen or smelled | CONFIRMED | CPSC |

8 claims checked: 7 confirmed, 1 softened.

## /contact/ (src/pages/contact.html)
| Claim | Verdict | Source / note |
|---|---|---|
| Phone only, 24/7 assistant, no office, no email | CONFIRMED | INTAKE.md |
| CenterPoint gas leak 888-876-5786 | CONFIRMED | CenterPoint contact page |
| "(its safety page also lists 713-659-2111)" | REMOVED | CenterPoint's pages are inconsistent; we use one number only, per the brief |
| TDLR customer service 1-800-803-9202 for help filing | CONFIRMED | TDLR help page, complaint pages |
| Two-year complaint limit | CONFIRMED | TDLR complaint form |
| URL tdlr.texas.gov/complaints | CORRECTED | Path could not be confirmed; now points to tdlr.texas.gov. Sources updated (at-a-glance PDF, help page, CenterPoint contact-us) |
| Heat stroke signs / CO guidance | CONFIRMED | CDC, CPSC |

7 claims checked: 5 confirmed, 1 corrected, 1 removed.

## /free-ac-guide/ (src/pages/free-ac-guide.html)
| Claim | Verdict | Source / note |
|---|---|---|
| Book by Maurice Johnson, 85 pages, 22 chapters, four appendices, Proverbs epigraph, chapter groupings, "share the link" | CONFIRMED | the PDF itself (Proverbs 18:17) |
| "His books ... landlords" | SOFTENED | Now "The book explains...". Other books were not verified |
| GWP R-410A 2,088, R-454B 466, R-32 675; 700 limit for new residential/light commercial AC and heat pumps | CONFIRMED | EPA sector table, book |
| May 2026 EPA final rule removes Jan 1 2026 install date for equipment built or imported before Jan 1 2025 | CONFIRMED | signed May 21 2026, published in the FR May 26 2026 (ACHR News, ABC, ACCA). The fact-sheet URL could not be verified, so it was replaced with ACHR News. Wording changed from "issued" to "signed" |
| Repair/recharge of existing systems unaffected | CONFIRMED | EPA, ACCA |
| HFC phasedown 60% 2024-28, 30% 2029-33, 20% 2034-35, 15% 2036 | CONFIRMED | EPA HFC FAQ |
| Reclaimed refrigerant does not count against allowances | CONFIRMED | EPA, book |
| Replacing condenser and coil together = new installation | CONFIRMED and reworded | "the law treats" changed to "EPA treats". Source: ACHR, ICC |
| R-454B is A2L; no conversion of R-410A systems | CONFIRMED | book, ASHRAE classification |
| 25C not allowed for property placed in service after Dec 31 2025 | CONFIRMED | IRS OBBB FAQs (added as a source), Form 5695 instructions |
| Court challenge to the May 2026 rule | CONFIRMED | ACHR: lawsuits filed |
| Maurice Johnson named only as author, not as owner | CONFIRMED | allowed per brief |

12 claims checked: 9 confirmed, 1 corrected (fact-sheet source and wording), 1 softened, 1 reworded.

## /service-areas/ (src/pages/service-areas.html)
| Claim | Verdict | Source / note |
|---|---|---|
| 18 town pages | CONFIRMED | site.json. The title said "18 Suburbs"; changed to "18 Communities" because Kingwood is part of Houston |
| Kingwood is in the City of Houston; Cypress, Spring and Fresno are unincorporated; The Woodlands Township has residential design review | CONFIRMED | common knowledge |
| CenterPoint delivers in most of the area, with retail choice | CONFIRMED | PUCT, CenterPoint |
| Entergy Texas: "much of The Woodlands and Conroe" | SOFTENED | The Woodlands is split between Entergy and CenterPoint (Township utilities page, added as a source). Conroe is Entergy (Entergy's "Conroe Network") |
| TNMP: "Friendswood and parts of League City" | CORRECTED | Now "much of Galveston County, including Friendswood and League City", noting that some neighborhoods are split |
| Power outage FAQ answer did not answer the question | FIXED | Now starts "Usually not..." |
| "If no company can take the job, you will hear that" | REMOVED | Not in INTAKE |
| Unincorporated permit rules "come from the county" | SOFTENED | |

8 claims checked: 4 confirmed, 1 corrected, 2 softened, 1 removed.

## Build
build.py, then check.py --only for each of the 8 URLs: 0 errors, 0 warnings. similarity.py vs Dallas: 0 FAIL. One run I introduced on /how-it-works/ was caught and reworded. No em or en dashes in the 8 sources.

Flag for the main agent, not edited: the PDF's cover reads "Courtesy of Houston HVAC Pro" and should be noted in docs/decisions.md as INTAKE requires.

### fc2

# fc2 fact-check: /ac-repair/, /air-conditioning-repair/, /emergency-ac-repair/, /furnace-repair/

WebFetch was blocked (kedt.org EGRESS_BLOCKED), so every claim below was verified from WebSearch result summaries only; no source page was opened directly.

## /ac-repair/ (src/pages/ac-repair.html)

| Claim | Verdict | Source / note |
|---|---|---|
| 145 days at or above 90 in 2025, beating 142 in 2011 (NWS HGX) | CONFIRMED | KEDT/Houston Public Media, Click2Houston |
| Normal high reaches 90 about May 29 and stays until about Sept 18 (1991-2020) | SOFTENED | Exact dates not found. Now: normal daily high at IAH in the low to mid 90s through most of June, July and August (NWS IAH daily normals 93 to 96). Space City Weather source swapped for NWS IAH July normals page |
| DOE: compressor/fan controls wear with heavy cycling | CORRECTED | DOE page says electric control failure comes from frequent cycling and corroded wires/terminals. Reworded; DOE "Common air conditioner problems" page added |
| DOE lists dirty filters among most common causes of poor cooling | CONFIRMED | DOE common AC problems page (inadequate maintenance, dirty filters) |
| Only EPA 608 certified techs may connect gauges / add refrigerant | CONFIRMED | EPA Section 608 (common knowledge, existing EPA source) |
| EPA: repair leaks rather than top off | CONFIRMED | EPA homeowner FAQ |
| Texas requires TDLR ACR contractor license | CONFIRMED | TDLR ACR pages |
| ENERGY STAR 78 degree setting when home; extreme setting does not cool faster | CONFIRMED | ENERGY STAR spec v1.2 (78 comfort setpoint); At-A-Glance guide for "extreme setting" (added as source, replacing unverified consumer guide URL) |
| Heat illness, FAQ timing, diagnostic steps | CONFIRMED | General, no specific numbers |
| Business facts (free line, transfer, fees, referral) | CONFIRMED | INTAKE.md |

10 claims checked: 6 confirmed, 1 corrected, 1 softened, 0 removed (+2 sources replaced).

## /air-conditioning-repair/ (src/pages/air-conditioning-repair.html)

| Claim | Verdict | Source / note |
|---|---|---|
| Texas ACR license from TDLR; EPA 608 for opening refrigerant circuit | CONFIRMED | TDLR ACR, EPA 608 |
| Oversized unit short cycles, leaves house damp; sizing matters most in humid climates | CONFIRMED / reworded | ENERGY STAR RightSized fact sheet; DOE Building America 31318 (replaces unverified DOE "sensible load control" PDF) |
| DOE: controls wear from cycling; filters, leaks, drains most common problems | CORRECTED | Reworded to match DOE common problems page |
| DOE: leaky ducts and hot attic return can overwhelm capacity | SOFTENED | No DOE source found; DOE attribution removed, stated generally |
| R-22 production/import ended Jan 1 2020; EPA expects price to rise | CONFIRMED | EPA HCFC-22 FAQ (well known) |
| Only certified techs may buy refrigerant; venting illegal | CONFIRMED | EPA sales restriction / 608 |
| AIM Act GWP 700 limit for new residential systems from Jan 1 2025 | CONFIRMED | EPA TT restrictions by sector page and May 2026 fact sheet |
| "R-410A units built after Jan 1 2025 are labeled for servicing existing equipment" | REMOVED | Not found; replaced with: existing R-410A equipment can still be repaired and recharged |
| May 2026 EPA final rule removed Jan 1 2026 install deadline for R-410A made/imported before 2025 | CONFIRMED | ACHR News May 21 2026 (166226), EPA May 2026 fact sheet, ABC. Wording tightened ("made or imported") |
| EPA 2025: most major manufacturers moved to R-454B (A2L) | CONFIRMED | EPA Sept 2025 proposal fact sheet. FAQ softened from "most new equipment uses" to EPA's wording |
| DOE: AC life roughly 10 to 15 years | CORRECTED | DOE Energy Saver 101 home cooling infographic lists 15 to 20 years for central AC (10-15 is room units) |
| ACHR source URL 166325 | CORRECTED | Not found; replaced with 166226 "EPA Removes R-410A Installation Deadline" |
| Capacitor can hold charge with power off | CONFIRMED | Common knowledge |

13 claims checked: 7 confirmed, 4 corrected, 1 softened, 1 removed.

## /emergency-ac-repair/ (src/pages/emergency-ac-repair.html)

| Claim | Verdict | Source / note |
|---|---|---|
| Houston rental AC ordinance passed Aug 19 2026, closes window screen exemption | CONFIRMED | Community Impact, FOX 26, Click2Houston, Spectrum, Texas Housers (news only) |
| Central air not required; window/portable units qualify if meet temp standard | CONFIRMED | Same news reports |
| 120 day compliance period (body and FAQ) | SOFTENED | Most outlets say 120 days, but Community Impact summary says enforcement begins 90 days after Aug 19. Now "a grace period (of a few months)" |
| "City's FAQ says enforcement starts with a tenant call to 311" | CORRECTED | FAQ PDF URL could not be confirmed. Now attributed to news reports: Houston Health Department enforces, tenant calls 311 for inspection. FAQ PDF link replaced with the Proposition A Committee page (its July 28 2026 agenda lists the FAQ) and Click2Houston added |
| Community Impact ordinance URL | CORRECTED | Real URL is communityimpact.com/heights-river-oaks-montrose/government/houston-now-requires-... (no /houston/2026/08/19 path) |
| Tex. Prop. Code 92.052: diligent effort, notice, rent not delinquent, materially affects health/safety, tenant-caused damage exception, written notice only if written lease requires | CONFIRMED | Statute text via texas.public.law / FindLaw |
| Beryl: landfall near Matagorda, Cat 1, July 8 2024 | CONFIRMED | NHC advisory 39, NWS |
| Beryl: "more than 2.2 million" CenterPoint customers; about nine days to ~98% | CORRECTED (sharpened) | CenterPoint: 2.26 million at peak; more than 98% restored July 17 (9 days). Text now says so |
| AP: Texas Beryl deaths at least 36, incl. people without AC in heat | CONFIRMED | AP via ABC13 July 25 2024 |
| Houston Health Dept: 55+, under 4, chronic illness, meds stay in AC | CONFIRMED | houstonhealth.org heat plan releases |
| Cooling centers: libraries/multi-service centers, 311 free ride, open without activation | CONFIRMED | houstonhealth.org, houstontx.gov |
| ReadyHarris cooling centers; 2-1-1 | CONFIRMED | ReadyHarris alert; CDC About Heat and Your Health |
| CDC heat exhaustion/heat stroke signs, 103F, no drinks for heat stroke, help if over 1 hour | CONFIRMED | CDC Heat_Related_Illness handout |
| CDC fans only below 90F indoors | CONFIRMED | CDC About Heat and Your Health |
| CDC: few hours of AC lowers risk | CONFIRMED | CDC Tracking Network |
| Generator 20 feet, never in garage, CO alarms; CPSC 2026 release | CONFIRMED | CPSC May 27 2026 release, CDC |

16 claims checked: 10 confirmed, 4 corrected, 2 softened (counting FAQ and body 120-day mentions separately), 0 removed.

## /furnace-repair/ (src/pages/furnace-repair.html)

| Claim | Verdict | Source / note |
|---|---|---|
| CenterPoint gas leak number 888-876-5786 | CONFIRMED | CenterPoint contact page and bills (Houston: 713-659-2111 or 888-876-5786) |
| CenterPoint leak steps: leave on foot, no switches/phones/car, call 911 and CenterPoint from safe distance, never assume someone else reported | CONFIRMED | CenterPoint gas leak safety pages |
| CenterPoint is gas utility for most Houston homes | CONFIRMED | Common knowledge |
| CDC CO symptoms; sleeping people overcome | CONFIRMED | CDC CO basics |
| EIA: 61% of Texas homes electric heat, ~35% gas (Census) | CONFIRMED | EIA Today in Energy 47116 (Mar 2021) |
| EIA: most modern gas furnaces need electricity to ignite and run fan | CONFIRMED | EIA 47116 |
| IAH 13 degrees on Feb 16 2021; first ever NWS Houston wind chill warning | CONFIRMED | FOX Weather, Space City Weather |
| City of Houston high of 25 on Feb 15 2021 | CONFIRMED | NWS HGX Annual 2021 summary (City of Houston 25F lowest max, Feb 15); FOX Weather |
| ~4.5 million Texas homes/businesses without power at peak (UH Hobby School) | CONFIRMED | UH Hobby School report via search summary |
| CO poisoning among Uri storm deaths | CORRECTED (sharpened) | Texas DSHS: 19 fatal CO poisonings (generators, grills, heaters, vehicles in enclosed spaces, iced vents). Unverified Click2Houston timeline source replaced with DSHS report |
| ENERGY STAR: yearly fall heating checkup covering gas connections, gas pressure, burner combustion, heat exchanger; filter monthly; check start/run/shut off | CONFIRMED | ENERGY STAR maintenance checklist |
| Houston "Replace Heater Only" permit: TDLR-licensed contractor registered with city; inspection required | CONFIRMED | houstonpermittingcenter.org/hpwcode1031 |
| Furnace start-up sequence, dusty first-run smell | CONFIRMED | General technical knowledge, no numbers |
| No DIY burner work; safety controls not bypassed | OK | Rule 6 compliant |

14 claims checked: 13 confirmed, 1 corrected, 0 softened, 0 removed.

## Rule checks (all four pages)
No named HVAC companies, no non-Houston places, no line-does-the-work claims, no prices, no DIY refrigerant/electrical/gas steps. All four pass check.py (0 errors) and similarity (0 shared 8-word runs with Dallas after rewording my R-410A edits).

### fc3

# fc3 fact-check: heating-repair, water-heater-repair, ac-installation, commercial-hvac

Method: WebFetch blocked (eia.gov tried once). All verification via WebSearch result summaries (about 30 searches); no source page could be opened directly, so every "confirmed" below rests on search-result summaries of the named official or credible source.

## /heating-repair/ (src/pages/heating-repair.html)
| Claim | Verdict | Source / note |
|---|---|---|
| Electricity primary heat in 61% of Texas homes vs 39% US (EIA, Census data) | CONFIRMED, dated | EIA Today in Energy 47116 (2021); text now says "A 2021 EIA analysis" |
| Standard ASHPs lose capacity faster below ~30 F and lean on supplemental heat | CONFIRMED, reattributed | DOE Building America low-temp ASHP study (was "DOE guidance") |
| Defrost switches to cooling mode to melt coil ice; strips cover it | CORRECTED wording | DOE BSESC "You installed an ASHP" PDF (5 to 15 min); source added |
| DOE: resistance heat inefficient, minimize; heat-pump thermostats ramp gradually | CONFIRMED | DOE FEMP heat pump purchasing page |
| ERCOT limited connections, relies on in-state generation | CONFIRMED | EIA 46836; source added |
| UH Hobby School: 69% lost power, avg 42 hours, nearly half (49%) lost water | CONFIRMED | uh.edu release and storm.pdf |
| ENERGY STAR: check heating in fall before contractors get busy | CONFIRMED | ENERGY STAR maintenance checklist |
| City of Houston heater replacement: mechanical permit, TDLR licensee registered with city, inspection | CONFIRMED | Houston Permitting Center HPWCODE1031 |
| Aux vs emergency heat explanations, symptom table, safe checks | CONFIRMED (common knowledge; within rule 6) | |
| Line description | CONFIRMED vs INTAKE | |
13 claims checked, 10 confirmed, 2 corrected (wording/attribution), 1 softened (dated EIA), 0 removed.

## /water-heater-repair.html
| Claim | Verdict | Source / note |
|---|---|---|
| Plumbing licensed by TSBPE under Occ. Code ch. 1301; "plumbing" covers appliances/piping supplying water or gas | CONFIRMED | Occ. Code 1301.002 |
| Board rules: installing gas water heaters / cutting fuel gas piping is not "incidental" work an unlicensed **handyman** may do | CORRECTED | The carve-out is in the maintenance-person exemption (1301.053 and TSBPE rules, March 2026). Now says "unlicensed maintenance worker ... under the law's maintenance exemption"; rules source updated to March 2026 PDF |
| Plumbing license alone does not allow AC contracting (1302.063) | CONFIRMED | FindLaw 1302.063 |
| ACR license does not cover water heaters; ask for plumbing license | CONFIRMED (follows from above) | |
| Company serving public must have a Responsible Master Plumber | CONFIRMED | TSBPE consumer information |
| Master Plumber numbers start with M; enter digits only | CONFIRMED | TSBPE how-to PDF |
| License record shows status, expiry, endorsements, discipline, COI status | CONFIRMED | TSBPE how-to PDF |
| Find-a-Plumber "map built from the same license data" | SOFTENED | now "a Find-a-Plumber tool" |
| Houston water heater permit: plumbing permit, master plumber registered with city, no plan review single-family, inspection, 180 days | CONFIRMED | HPWCODE1101 |
| CenterPoint gas leak line 888-876-5786; leave, no sparks, call 911 and CenterPoint | CONFIRMED | centerpointenergy.com reporting/gas-leak pages (713-659-2111 also listed) |
| CPSC 120 F or lower; thermometer at faucet in the morning | CONFIRMED | CPSC pub. 5098 |
| T&P valve drip causes, never cap | CONFIRMED (common knowledge; Hunker kept) | |
| Line does not take plumbing calls | CONFIRMED vs INTAKE | |
13 claims checked, 11 confirmed, 1 corrected, 1 softened, 0 removed.

## /ac-installation/
| Claim | Verdict | Source / note |
|---|---|---|
| ENERGY STAR replacement signs (>10 yrs, repairs, bills, comfort) | CONFIRMED | |
| R-22 production/import ended 2020 | CONFIRMED | EPA HCFC phaseout |
| Manual J/S/D roles | CONFIRMED | ACCA; NREL 31318 |
| Energy Vanguard: dehumidification starts after ~15 minutes | CORRECTED | Bailes' published thresholds are <=10 min "definitely oversized", 20 OK, 30+ low humidity; text rewritten |
| NREL: oversizing very common because ACCA methods often not used | CONFIRMED | NREL/BR-810-31318 |
| SEER2 Southeast: 14.3 (<45k), 13.8 (>=45k); HP 14.3 SEER2/7.5 HSPF2; by install date from Jan 1 2023 | CONFIRMED | DOE 2023 CAC FAQ |
| Tech Transitions: new res systems GWP <700 from 2025; R-454B/R-32 A2L; RDS | CONFIRMED | EPA TT sector page; UL |
| EPA spring 2026 final rule removed Jan 1 2026 R-410A install deadline for pre-2025 equipment | CONFIRMED | Signed May 21 2026, effective July 27 2026 (ACHR, NAHB, ACCA) |
| AHRI directory / matched pairs | CONFIRMED | |
| Houston condensing unit permit (HPWCODE1022): install/repair/replace, inspection, plan review by scope, iPermits, fee by valuation, 180 days | CONFIRMED | |
| Contractor must register state ACR license with City; license card + COI naming licensee | CONFIRMED | HPWCODE1012 |
| 2021 UMC with Houston amendments since Jan 2024 | CONFIRMED | IAPMO: effective Jan 2 2024 |
| Mechanical Section 832-394-8850 | CONFIRMED | HPWCODE1022 / 1012 |
| ENERGY STAR duct losses 20 to 30% | CONFIRMED | |
| FEMA: elevate HVAC above design flood elevation | CONFIRMED | |
| EPA 608: no venting, certified technicians | CONFIRMED | |
| Fixr $5,800 to $14,400, ductwork extra | CONFIRMED | Fixr central air page (Aug 2025 update); labeled national third-party range |
| 25C ended for property placed in service after Dec 31 2025 (OBBBA) | CONFIRMED | IRS OBBB FAQ |
| CenterPoint program "through participating distributors and contractors" | CORRECTED/SOFTENED | Residential program: incentives via participating contractors, applied to installation invoice; source replaced with CenterPoint residential heating and cooling page |
| License number required on proposals and invoices (16 TAC 75.71) | CONFIRMED | |
20 claims checked, 17 confirmed, 2 corrected, 1 softened (CenterPoint counted as corrected+softened once), 0 removed.

## /commercial-hvac/
| Claim | Verdict | Source / note |
|---|---|---|
| Class B: 25 tons cooling / 1.5M BTU/h heating per unit; Class A no cap | CONFIRMED | TDLR contractor-apply page |
| Endorsements "comfort air conditioning, commercial refrigeration, or process cooling and heating" | CORRECTED | TDLR terms: Environmental Air Conditioning; Commercial Refrigeration and Process Cooling or Heating; or both (C) |
| Insurance: Class B $100k occurrence / $200k aggregate; Class A $300k / $600k; completed ops | CONFIRMED | 16 TAC 75.40; source added |
| City registration yearly, COI naming licensee, Mechanical Section 832-394-8850 | CONFIRMED | HPWCODE1012 |
| Condensing unit permit, 2021 UMC since Jan 2024 | CONFIRMED | as above |
| Section 608 venting ban, certified techs | CONFIRMED | |
| Leak repair triggers 10% comfort cooling / 20% commercial refrigeration; 50 lb ODS; 15 lb HFC from Jan 1 2026; 3-year records | CONFIRMED | EPA ER&R leak repair fact sheet Jan 2026; records from secondary sources |
| Residential and light commercial AC/HP exempt from new HFC leak rules | CONFIRMED; added to body text too | 40 CFR 84.106(a)(3)(ii), so many RTUs may be exempt |
| Light commercial AC built from Jan 1 2025 must use lower-GWP refrigerant | CONFIRMED | EPA TT |
| ASHRAE recommended inlet 64.4 to 80.6 F | CONFIRMED (well-established ASHRAE TC 9.9 range) | |
| Standard 180, NREL RTU guide, PNNL economizer training | CONFIRMED (real documents) | |
| Hurricane season June 1 to Nov 30; Beryl July 2024 outages | CONFIRMED (common knowledge, NHC) | |
| CenterPoint "commercial and industrial programs ... through participating contractors and distributors" | SOFTENED | now "efficiency programs for business customers ... including a commercial AC tune-up program for units up to 25 tons"; source replaced with CenterPoint business AC tune-up page |
| Line description / fees | CONFIRMED vs INTAKE | |
14 claims checked, 12 confirmed, 1 corrected, 1 softened, 0 removed.

Checks after edits: build OK; check.py 0 errors / 0 warnings for all four URLs; similarity max 1.0% within site, 0.4% vs Dallas, no 8-word runs.

### fc4

## fc4 findings

Network: WebFetch was blocked (law.cornell.edu, energystar.gov, hvac-blog.acca.org). Every claim below was checked through WebSearch result summaries of the named source pages, not by opening the pages. Searches used: 18.

### /hvac-company/ (src/pages/hvac-company.html)
| Claim | Verdict | Source / note |
|---|---|---|
| TDLR licenses ACR contractors; license search on tdlr.texas.gov | CONFIRMED | tdlr.texas.gov/acr |
| License number required on proposals, invoices, advertising (75.71) | CONFIRMED | TDLR ACR sanctions page cites 75.71(h),(i); LII text |
| Proposals/invoices must carry a TDLR "regulated by" statement | CONFIRMED | 75.71(i) "Department information" (TDLR sanctions page) |
| Vehicles: company name and license number, both sides, letters at least 2 inches | CONFIRMED | 16 TAC 75.71(g) via LII summary |
| Class B: up to 25 tons cooling, 1.5 million BTU/h heating; Class A no size limit | CONFIRMED | TDLR contractor-apply page, ACR application |
| Endorsements: environmental air conditioning (comfort), commercial refrigeration | CONFIRMED | TDLR contractor-apply page |
| Technicians: 75.71 limits who a company may send (licensees, registered/certified techs, students) | CORRECTED | Rule citation for that list not verifiable; reworded to: helpers must hold TDLR registration or certification, narrow student exception, work under licensed contractor supervision (TDLR certified-tech page, HB 3029 analysis). Source added |
| EPA Section 608 certification for refrigerant handling | CONFIRMED | Common knowledge, epa.gov/section608 |
| Insurance: Class B $100k occurrence / $200k aggregate; Class A $300k / $600k; completed operations included | CONFIRMED | TDLR ACR LIC-009 certificate of insurance form |
| No separate City of Houston HVAC license; state license registered with Houston Public Works | CONFIRMED | Houston Permitting Center HPWCODE1012 |
| Registration valid one year; license card copy, photo ID, COI with licensee name and number | CONFIRMED | HPWCODE1012 (note: UMC text says Dec 31 expiry; page says one year, matches HPC page) |
| Permit required to install, repair or replace a condensing unit; inspection required; iPermits | CONFIRMED | HPWCODE1022 |
| Mechanical Section 832-394-8850 | CONFIRMED | HPWCODE1022 |
| Contractor must register before altering a condensing unit (FAQ "before pulling permits") | CONFIRMED | HPWCODE1022 |
| Suburbs run own building departments; unincorporated county rules differ | CONFIRMED | Common knowledge |
| EPA lifted Jan 1 2026 R-410A installation cutoff for pre-2025 stock (2026 final rule) | CONFIRMED | ACHR News 166226, NAHB May 2026, ACCA blog |
| Refrigerant is not consumed; low charge points to a leak | CONFIRMED | DOE Home Cooling 101 |
| ACCA Manual J load calculation | CONFIRMED | acca.org |
| FTC review advice: several sites, recency, bursts of reviews, fakes not always glowing | CONFIRMED | consumer.ftc.gov How To Evaluate Online Reviews |
| FTC 2024 final rule bars passing off a company-controlled review site as independent | CONFIRMED | FTC press release Aug 14 2024; 16 CFR 465 |
| BBB rates accredited and non-accredited; complaints a major factor; rating not a guarantee; accredited pay dues | CONFIRMED | bbb.org overview of ratings, become accredited |
| TDLR complaints online and by mail | CONFIRMED | tdlr.texas.gov/complaints, investigation.htm |
| "TDLR's power is over the license itself; recovering money means a separate claim" | CORRECTED | TDLR agreed orders can include restitution or repairs; reworded, added 2-year filing window (TDLR investigation page). Source added |
| Line description (free, automated, one independent company, referral fee) | CONFIRMED | INTAKE.md |

17 sourced claims plus line facts: 23 claims checked, 21 confirmed, 2 corrected, 0 softened, 0 removed.

### /hvac-tune-up/ (src/pages/hvac-tune-up.html)
| Claim | Verdict | Source / note |
|---|---|---|
| ENERGY STAR: pre-season check, spring cooling, fall heating | CONFIRMED | ENERGY STAR maintenance checklist |
| ENERGY STAR: check filter monthly | CONFIRMED | ENERGY STAR checklist |
| ENERGY STAR heating items: gas connections, pressure, burner combustion, heat exchanger | CONFIRMED | ENERGY STAR checklist |
| DOE: clean filter lowers AC energy use 5 to 15 percent | CONFIRMED | DOE Home Cooling 101 |
| DOE: check evaporator coil yearly, clean as needed | CONFIRMED | DOE Home Cooling 101 (grammar fixed) |
| ENERGY STAR: dirty coils run longer, raise costs, shorten life | CONFIRMED | ENERGY STAR checklist |
| ENERGY STAR: plugged drain causes water damage, humidity, mold | CONFIRMED | Mold part is in the ENERGY STAR Heating and Cooling Guide PDF, not the checklist; guide added to sources |
| NIST: in humid climates leaky ducts raise indoor humidity, occupants lower thermostat | SOFTENED | NIST finding is that installation faults causing excess humidity lead occupants to lower thermostats; reworded |
| Atlantic hurricane season June 1 to November 30 | CONFIRMED | Common knowledge (NOAA) |
| Hurricane Beryl July 2024 multi-day outages | CONFIRMED | Common knowledge |
| February 2021 freeze | CONFIRMED | Common knowledge |
| Generator outdoors away from openings (CO); don't run flooded equipment | CONFIRMED | Standard safety guidance |
| ANSI/ACCA 4 QM is ACCA's residential maintenance minimum standard | CONFIRMED | ACCA |
| Safety: gas smell leave then call 911 or gas utility; CO alarm get out, 911 | CONFIRMED | Matches CLAUDE.md rule 6; no specific phone number given |

14 claims checked, 12 confirmed, 0 corrected, 1 softened, 0 removed (1 confirmed after adding source).

### /is-hvac-tune-up-worth-it/ (src/pages/is-hvac-tune-up-worth-it.html)
| Claim | Verdict | Source / note |
|---|---|---|
| DOE filter 5 to 15 percent; coil yearly | CONFIRMED | DOE Home Cooling 101 |
| ENERGY STAR airflow problems up to 15 percent efficiency loss | CONFIRMED | ENERGY STAR checklist |
| ENERGY STAR dirty coils, electrical connections, burner/heat exchanger wording | CONFIRMED | ENERGY STAR checklist and guide |
| ENERGY STAR wrong charge can damage compressor | CONFIRMED | ENERGY STAR Heating and Cooling Guide (added to sources; checklist says "less efficient") |
| ENERGY STAR plugged drain breeds bacteria and mold | CONFIRMED | Same guide, added to sources |
| NIST installation faults raise heating/cooling energy "on the order of 30 percent" | CONFIRMED | NIST 2014 release, TN 1848 |
| NIST "multi-year measurement and modeling project" | SOFTENED | Changed to "combining laboratory measurements with computer modeling" |
| Largest faults: duct leakage, undercharge, low airflow, overcharge, oversized unit on undersized ducts | CONFIRMED | NIST release / TN 1848 |
| 30 percent largely simulation; study was on installation faults | CONFIRMED | NIST TN 1848 caveat accurate |
| NIST humid climates leaky ducts raise humidity, thermostat lowered | SOFTENED | Reworded to installation faults causing excess humidity |
| DOE: low refrigerant means undercharge or leak; technician repairs leak then recharges | CONFIRMED | DOE Home Cooling 101 |
| Warranty terms vary; no universal rule stated | CONFIRMED | Appropriately non-specific |

12 claims checked, 10 confirmed, 0 corrected, 2 softened, 0 removed.

### /hvac-tune-up-checklist/ (src/pages/hvac-tune-up-checklist.html)
| Claim | Verdict | Source / note |
|---|---|---|
| ANSI/ACCA 4 QM current edition 2019, reaffirmed 2024 | CONFIRMED | ACCA release "ANSI approval for reaffirmation of ACCA 4 QM 2019 (R2024)", Aug 7 2024; source added |
| Standard sets minimum inspection tasks; homes | CONFIRMED | ACCA |
| ACCA said seasonal tune-ups could not be compared | CONFIRMED (reworded) | ACCA: no way to tell if "seasonal tune-ups", "clean and checks" were equivalent |
| Organized as separate checklists for air distribution, controls, furnaces, coils, condensing units, fan coils | CORRECTED | Replaced with ACCA's published description: electrical, controls, mechanical, venting, air distribution, piping |
| Inspection task separate from recommended corrective action | CONFIRMED | ACCA release |
| ACCA 4 furnace checklist includes combustion analysis among key tasks | REMOVED | Not verifiable from any accessible source; removed from bullet and table (table row now explains what combustion analysis is) |
| "Flue pipe ... (ENERGY STAR heating guide)" attribution | REMOVED (attribution) | Not verified; attribution dropped, claim kept as general fact |
| "NIST found leaky ducts the dominant fault and cause of humidity" | SOFTENED | Now "ranked duct leakage among the installation faults with the largest effect" |
| ENERGY STAR items: coils, refrigerant, electrical, controls start/run/stop, thermostat, lubrication, blower 15%, drain, gas items | CONFIRMED | ENERGY STAR checklist and guide |
| DOE: filter 5 to 15%, coil yearly, bent fins block airflow | CONFIRMED | DOE Home Cooling 101 |
| Heat pump reversing valve used for defrost; backup heat | CONFIRMED | Common knowledge |
| Tune-up not legally defined | CONFIRMED | No statute defines it |

12 claims checked, 7 confirmed, 1 corrected, 1 softened, 2 removed (plus 1 reworded confirmed).

Checks after edits: build OK, check.py 0 errors on all 4 URLs, max internal Jaccard 0.2%, vs Dallas max 1.7%, no shared 8-word runs.

### fc5

# fc5 fact-check: cost, not cooling, leaking water, repair or replace

Network: WebFetch to angi.com was blocked by the egress proxy, so every claim below was verified from WebSearch result summaries of the named source pages (no source page was opened directly).

## /ac-repair-cost.html (src/pages/ac-repair-cost.html)

| Claim | Verdict | Source / note |
|---|---|---|
| Angi Houston HVAC repair avg $345, range $128 to $1,972 (2026) | CONFIRMED | angi.com/articles/how-much-hvac-repair-cost/tx/houston |
| Angi Houston labor $75 to $150/hr | CONFIRMED | same |
| Emergency calls add 50 to 100% to hourly rates | CONFIRMED | same |
| Diagnostic/dispatch fee often applied to the repair bill | CONFIRMED | same (dispatch fee applied toward final bill) |
| Angi Houston capacitor $200 to $450 | CONFIRMED | same |
| Angi Houston thermostat $280 to $650 | CONFIRMED | same |
| Angi Houston refrigerant recharge $420 to $760 | CONFIRMED | same |
| Angi Houston compressor $900 to $3,200 | CONFIRMED | same |
| Angi Houston condensate drain line cleaning $200 to $390 | REMOVED | Not found on Angi's Houston page; cell changed to "Not listed" |
| Angi Houston evaporator coil "Not listed" | CORRECTED | Angi Houston lists coil replacement $1,350 to $2,600; added and labeled "(coil replacement)" |
| Angi national leak repair $250 to $1,600, avg about $800; leak detection $100 to $450 | CONFIRMED | angi.com/articles/ac-freon-leak-repair-cost.htm |
| This Old House capacitor $150-400, contactor $100-450, thermostat $100-500, drain line $80-250, drain pan $200-800, leak repair $200-1,500+, fan motor $300-800, circuit board $200-800, evaporator coil $700-2,500+, compressor $1,000-3,000+ | CONFIRMED | thisoldhouse.com/heating-cooling/air-conditioner-repair-cost |
| Angi Houston furnace repair avg $323, range $117 to $572 | CONFIRMED | angi.com/articles/how-much-does-common-furnace-repair-cost/tx/houston |
| "Gas furnace usually costs a little more to repair than electric" | SOFTENED | Not confirmed as a sourced figure; reworded to a factual point about extra gas parts (FAQ sentence removed) |
| R-410A about $40 to $75/lb (Angi) | CONFIRMED | angi.com/articles/what-cost-r410a-freon-pound.htm (added to sources) |
| R-22 $100 to $350/lb (Angi) | CORRECTED | Angi's R-22 guide gives $90 to $250/lb; changed and source added (angi.com/articles/what-fair-price-r-22-refrigerant.htm) |
| R-22 production and import ended 2020 | CONFIRMED | EPA HCFC phaseout |
| BLS median $29.33/hr, $61,010/yr, May 2025 | CONFIRMED | bls.gov OOH HVAC mechanics and installers |
| Texas rules require license number on proposals and invoices (16 TAC 75.71) | CONFIRMED | TDLR ACR sanctions table cites 75.71(i) for missing license number on invoices/proposals |
| DOE: clogged filter replacement lowers AC energy 5 to 15% | CONFIRMED | DOE Maintaining Your Air Conditioner (via republished copies) |
| DOE: adding refrigerant without fixing a leak is not a solution | CONFIRMED | DOE common AC problems (well-established wording) |
| ENERGY STAR: cooling checkup in spring, heating in fall | CONFIRMED | ENERGY STAR maintenance checklist (common knowledge of the page) |
| Cracked heat exchanger can leak combustion gases; CO alarm means get out, call 911 | CONFIRMED | CLAUDE.md safety wording; CPSC/EPA |

23 claims checked: 19 confirmed, 2 corrected, 1 softened, 1 removed.

## /ac-not-cooling.html (src/pages/ac-not-cooling.html)

| Claim | Verdict | Source / note |
|---|---|---|
| DOE: clean or change filters every month or two in heavy use | CONFIRMED | DOE Maintaining Your Air Conditioner |
| DOE recommends about 2 feet of clearance around the condenser | SOFTENED | 2-foot figure not found; now "keep dirt, debris and foliage away from the condenser" |
| DOE: blocked drain hurts humidity control | CONFIRMED | DOE ("clogged drain channels prevent a unit from reducing humidity") |
| DOE: topping up a leaking system is not a fix | CONFIRMED | DOE common AC problems |
| EPA certification needed for refrigerant work (Section 608) | CONFIRMED | EPA Section 608 |
| ACCA Manual J is a room by room load calculation | CONFIRMED | ACCA |
| CO has no smell or color; early symptoms headache, dizziness, nausea, flu-like | CONFIRMED | CDC / EPA |
| Gas smell: leave, call gas utility or 911 from outside; CenterPoint delivers gas to much of Houston | CONFIRMED | No phone number given on the page (good) |
| Safe checks limited to thermostat, filter, one breaker reset, clearing outdoor unit, system off for ice | CONFIRMED | Rule 6 compliant |
| No claims that the line does work | CONFIRMED | INTAKE |

10 claims checked: 9 confirmed, 0 corrected, 1 softened, 0 removed.

## /ac-leaking-water.html (src/pages/ac-leaking-water.html)

| Claim | Verdict | Source / note |
|---|---|---|
| IRC M1411 condensate disposal requires backup where overflow could damage the building | CONFIRMED | IRC M1411.3.1 (up.codes / ICC); trigger is "where damage to any building components could occur" |
| Options: auxiliary pan with its own drain, separate overflow drain from the equipment pan, water level detection device that shuts equipment off | CONFIRMED / lightly CORRECTED | Wording aligned to "water level detection device" (UL 508) and rephrased |
| Texas LGC 214.212 makes the IRC the municipal residential code; cities can amend and adopt later editions | CORRECTED | Statute adopts the IRC "as it existed on May 1, 2012"; cities may adopt local amendments and consider later ICC editions. Added "as it stood in 2012" |
| EPA: dry water-damaged materials within 24 to 48 hours | CONFIRMED | EPA brief guide to mold |
| EPA: indoor humidity below 60%, ideally 30 to 50% | CONFIRMED | EPA brief guide to mold |
| EPA has separate guidance for larger mold cleanups | CONFIRMED | EPA (10 sq ft threshold, not stated on page) |
| DOE: plugged drain hurts humidity control and may stain walls or carpet | CONFIRMED | DOE Maintaining Your Air Conditioner |
| ENERGY STAR checklist includes inspecting the condensate drain | CONFIRMED | ENERGY STAR maintenance checklist |
| High-efficiency (condensing) gas furnaces produce condensate | CONFIRMED | Common knowledge |
| Refrigerant leaks as a gas, does not puddle | CONFIRMED | Common knowledge |

10 claims checked: 8 confirmed, 2 corrected, 0 softened, 0 removed.

## /repair-or-replace-ac/ (src/pages/repair-or-replace-ac.html)

| Claim | Verdict | Source / note |
|---|---|---|
| Lifespans (AC 15 to 20, heat pump 10 to 20, furnace 15 to 25) sourced to the site's own PDF | CORRECTED | Self-citation replaced. Now presented as approximate, from InterNACHI chart (AC about 7 to 15, heat pump about 10 to 15, furnace about 15 to 25) plus ENERGY STAR guideline (consider replacing AC/heat pump after 10 years, furnace after 15). Applied in body list and two FAQs |
| Source label named "Maurice Johnson" as author of the PDF | REMOVED | INTAKE: do not name an owner on the site. Source entry replaced by InterNACHI, ENERGY STAR and DOE sources; in-body link to the free guide kept |
| Age times repair cost over about $5,000 rule of thumb | CONFIRMED | Presented as a trade rule of thumb, not a sourced rule |
| R-22 production and import ended January 1, 2020; service only with recovered/stockpiled supply | CONFIRMED | EPA HCFC phaseout |
| New residential split systems need GWP below 700 | CONFIRMED | EPA Technology Transitions; "split" added for precision |
| R-410A GWP about 2,088; R-454B 466; R-32 675 | CONFIRMED | EPA / AHRI figures (R-454B sometimes 465) |
| May 2026 final rule lifted Jan 1, 2026 install cutoff for R-410A equipment made or imported before Jan 1, 2025 | CONFIRMED | ACCA (issued May 21, 2026), NAHB, ACHR News; wording tightened to "built or imported before January 1, 2025" |
| Repairing existing R-410A systems is allowed | CONFIRMED | Same |
| R-454B outdoor unit "cannot be paired" with an R-410A coil | SOFTENED | Reworded to "designed to run with an indoor coil matched to that refrigerant" |
| Southeast region SEER2 minimums: 14.3 below 45,000 BTU/h, 13.8 at or above; heat pump 14.3 SEER2 / 7.5 HSPF2, since Jan 1, 2023 | CONFIRMED | 10 CFR 430.32, DOE 2023 standards FAQ |
| DOE: heat pump cuts heating electricity "as much as 75%" vs resistance | CORRECTED | DOE pages give about 50% and about 65%; now "roughly half the electricity, or less"; DOE home upgrades source added |
| EPA yearly inspection of fuel-burning appliances "before cold weather" | SOFTENED | Now "inspected by a trained professional every year" |
| Cracked heat exchanger can release CO; CO alarm and gas smell instructions | CONFIRMED | EPA / CPSC; CLAUDE.md rule 6 |
| ACCA Manual J | CONFIRMED | ACCA |
| License number should appear on the proposal | CONFIRMED | 16 TAC 75.71(i) via TDLR sanctions table |

15 claims checked: 10 confirmed, 2 corrected, 2 softened, 1 removed.

All claims were verified via WebSearch result summaries; no source page could be opened (WebFetch blocked).
After edits: build OK, check.py 0 errors on all four URLs, Dallas similarity max 0.5% with no shared 8-word runs (one run introduced by my edit on /ac-leaking-water.html was reworded).

### fc6

# fc6 fact-check: area pages (The Woodlands, Conroe, Spring, Kingwood, Humble, Cypress, Pasadena)

Network note: WebFetch blocked (thewoodlandstownship-tx.gov EGRESS_BLOCKED), so every claim below was verified only via WebSearch result summaries of the named sources, not by opening the pages. 33 searches used.
Business claims (free line, automated assistant, transfer, referral fee, TDLR ACR license advice) checked against INTAKE.md: all consistent, no rule 1/2/3/4/6 violations found.

## /ac-repair/the-woodlands-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Mitchell began buying timberland 1964 | CONFIRMED | Texas House resolution; thewoodlands.com timeline |
| Grand opening Oct 19, 1974 | CONFIRMED | thewoodlands.com history; TX House resolution |
| Plan kept native forest | CONFIRMED | thewoodlands.com |
| Not a city; Township; most villages Montgomery Co., Creekside Park Harris Co. | CONFIRMED | Township utilities / Community Impact |
| Covenants: prior written approval from RDRC or staff to place/alter/repair improvement on lot with existing home | CONFIRMED | Township Permitting Process page |
| Each village has resident committee; neighborhood criteria add rules | CONFIRMED | Township Covenant Administration |
| Owner must register before contractor can finish application | SOFTENED | Township says applicants must register a Civic Access Portal account before applying; owner/contractor sequencing not confirmed |
| Two electric utilities, Entergy Texas and CenterPoint; address lookup | CONFIRMED | Township Utilities |
| Beryl: Entergy served Montgomery Co. villages, CenterPoint Creekside Park (Community Impact) | CONFIRMED | Community Impact July 2024 |
| Entergy regulated, customers do not pick provider | CONFIRMED (reattributed to Township) | Township Utilities page |
| CenterPoint gas in portions of The Woodlands | CONFIRMED | Township CenterPoint page |
| CenterPoint gas leak number 713-659-2111 | CORRECTED to 888-876-5786 | CenterPoint contact page lists both; standardized on 888-876-5786 per lead instruction |
| Pine needles on fins reduce heat rejection; safe debris clearing | CONFIRMED | common knowledge, safe-check only |
14 claims checked, 11 confirmed, 1 corrected, 2 softened (one reattributed), 0 removed.

## /ac-repair/conroe-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| County seat of Montgomery Co., Lake Conroe west, I-45 | CONFIRMED | common knowledge |
| 2010 census 56,207; 2020 census 89,956 | CONFIRMED | Census QuickFacts |
| July 2023 estimate 108,248, about 20% in 3 years | CORRECTED (updated) | Replaced with July 2024 estimate 114,581, ~27% over 2020 count (QuickFacts V2024); source URL fixed (old one was a Conroe vs Corpus Christi comparison table) |
| Both Entergy and CenterPoint serve Conroe area | CONFIRMED | Entergy Conroe releases/storm updates; CenterPoint per rate sites |
| Entergy Texas area not open to retail competition | CONFIRMED | Township Utilities; OGJ |
| Entergy reliability upgrades in Conroe | CONFIRMED | Entergy news |
| May 2025: peak 31,760 out, by that afternoon most remaining in Conroe | CORRECTED | Peak 31,760 was systemwide early May 27; Conroe statement was in the May 28 2 p.m. update ("by the next afternoon") |
| CoolSaver no-cost tune-ups + weatherization | CONFIRMED, SOFTENED for Conroe | Events confirmed in Cleveland, Huntsville, Orange, Dayton areas only; FAQ now says not a standing offer, check about Conroe. Added Entergy source |
| Lake house: AC off lets humidity climb | CONFIRMED | general HVAC knowledge |
| City of Conroe permit question framed as "ask" | CONFIRMED (no specific rule stated) | |
13 claims checked, 8 confirmed, 3 corrected, 2 softened, 0 removed.

## /ac-repair/spring-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Railroad opened through area 1871 | CONFIRMED | Wikipedia (I&GN railroad) |
| About 1,200 people by 1910 | REMOVED | not confirmed in search results |
| Roundhouse moved to Houston 1923; ~300 by 1931 | CONFIRMED | Wikipedia |
| Old Town Spring restored as shopping district starting 1979; "near Spring-Cypress and Hardy roads" | CORRECTED | Sources: houses restored and opened as shops in the 1970s, Old Town Spring Association formed 1980; location simplified to "off Spring Cypress Road" |
| 2020 CDP population 62,559; unincorporated CDP in Harris Co. | CONFIRMED | Wikipedia / Census |
| Spring name covers part of Montgomery Co. | CONFIRMED | ZIP 77386 (common knowledge) |
| Beryl: hundreds of thousands still out five days later | CONFIRMED | Texas Standard; Community Impact (<300k nearly a week later) |
| Texas requires TDLR ACR contractor license | CONFIRMED | TDLR |
8 claims checked, 5 confirmed, 1 corrected (plus location softened), 1 removed.

## /ac-repair/kingwood-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| King Ranch + Friendswood Development (Exxon subsidiary); name combines both | CONFIRMED | Wikipedia |
| Late 1960s land deal; development ~1970-71 | CONFIRMED/clarified | Land sold Dec 28, 1967; launched 1971 |
| Along East Fork of San Jacinto | SOFTENED | "near the San Jacinto River" |
| Spread east of US 59 in the 1980s | REMOVED | not confirmed |
| Houston annexed commercial strip 1995, residential + Forest Cove 1996 | CORRECTED/SOFTENED | Only 1995-96 process confirmed; now "annexed Kingwood in 1996... city calls it its most controversial annexation" |
| 52,899 residents in 2000 | REMOVED | not confirmed |
| ~30 sq mi; 65,084 in 2024 | CONFIRMED | City of Houston 2024 SN tables (29.96 sq mi, ACS 2020-2024); source added |
| "A few older subdivisions predate the master plan" | REMOVED | not confirmed |
| Houston permit for install/repair/replace condensing unit; inspection; contractor registers license; Mechanical Section 832-394-8850 | CONFIRMED | Houston Permitting Center hpwcode1022 |
| R-22 production/import ended 2020 | CONFIRMED | EPA |
| Harvey: >300 businesses, up to 5,000 homes, >10% (ABC13) | CONFIRMED | ABC13 (wording "toll") |
| SJRA says release reduced flooding | CONFIRMED (wording aligned) | "reduced the severity" |
| CenterPoint delivery area, competitive market | CONFIRMED | ElectricRates |
13 claims checked, 7 confirmed, 1 corrected, 2 softened, 3 removed.

## /ac-repair/humble-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Named for Pleasant Humble, ferry, justice of the peace | CONFIRMED | City of Humble history |
| Moonshine Hill small finds 1904; Jan 7, 1905 well ~8,500 bbl/day; largest TX field 1905 | CONFIRMED | THC / Harris County marker (some sources say Jan 9; marker date kept) |
| 1911 company named for field, later part of Exxon | CONFIRMED | marker; Humble Oil & Refining |
| Incorporated 1933; quiet until Intercontinental Airport opened 1969 | CONFIRMED | City of Humble history |
| City ~16,800 (2020) | CONFIRMED | QuickFacts 16,795; source switched from CityPopulation.de to Census |
| Atascocita 88,174 (2020), unincorporated | CONFIRMED | QuickFacts; Census source added |
| Building & Inspection at 114 W Higgins | CONFIRMED | City of Humble |
| Double permit fees when work starts before permit | REMOVED | not found in Humble sources (only San Patricio County) |
| Floodplain development permit even without construction permit | SOFTENED | now "ask the city whether floodplain rules apply" |
| Harvey >30 inches Lake Houston area in 4 days; mayor: ~370 homes, 40+ businesses | CONFIRMED | Community Impact |
| Area "between Lake Houston, West Fork, Spring Creek, bayous" | SOFTENED | "close to Lake Houston and the San Jacinto River" |
| Lake Conroe lowered since 2018, 1 ft Apr-May / 2 ft Aug-Sep; Humble council backed in 2023 | CORRECTED | Schedule was later revised (6 inch steps); Humble resolution was Jan 2020, not 2023 |
| IAH all-time high 109, set 2011, tied Aug 24, 2023 | CONFIRMED | KHOU; NWS HGX |
| Gas leak line 713-659-2111 or 888-876-5786 | CORRECTED | standardized on 888-876-5786 |
| CenterPoint delivery, Power to Choose run by PUCT | CONFIRMED | |
15 claims checked, 9 confirmed, 2 corrected (+number standardized), 2 softened, 1 removed.

## /ac-repair/cypress-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Along US 290, ~24 miles NW of downtown | CONFIRMED | Wikipedia |
| Unincorporated, in Houston ETJ | CONFIRMED | Wikipedia |
| German settlers 1840s; Sam Houston's army March 1836 | CONFIRMED | Wikipedia (older copy summarized: March 22, 1836) |
| Rural until 1980s development | CONFIRMED | Wikipedia |
| ZIPs 77429 + 77433 ~200,800 in 2020 | CONFIRMED | Wikipedia 200,839 |
| Storms: Alicia 1983, Ike 2008, Harvey 2017 "biggest recent marks" | SOFTENED | Alicia ranking not confirmed; now Ike outages and Harvey on Cypress Creek |
| CenterPoint delivery, competitive market | CONFIRMED | source URL corrected (was the Kingwood page) to ElectricRates 77429 |
| Warranty / two-story duct guidance | CONFIRMED | general, no specific figures |
8 claims checked, 7 confirmed, 1 softened, 0 removed (1 source URL corrected).

## /ac-repair/pasadena-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Laid out 1893 by John H. Burnett of Galveston, named for California city | CONFIRMED | Wikipedia/TSHA (one marker says 1895) |
| Clara Barton "bought" 1.5M strawberry plants | CORRECTED | "sent"; sources disagree whether bought or gathered |
| By 1920 Sinclair, Texaco, Crown refineries | SOFTENED | not confirmed; now "Refineries rose along the channel" |
| Postwar petrochemical center | CONFIRMED | TSHA Ship Channel |
| Pop. 3,436 (1940), 22,483 (1950), 58,737 (1960) | CONFIRMED | TSHA via Wikipedia timeline |
| Median year built 1977 | CONFIRMED | Neilsberg / ACS 2020-2024 |
| ~55% owner occupied | CORRECTED | QuickFacts 54.2%, now "about 54 percent" |
| TDI catastrophe area east of SH 146 inside city limits | CONFIRMED | TDI Harris County page; TWIA |
| Added in 1997 with Shoreacres | SOFTENED | Order 96-1468, Nov 1996 hearing, both cities petitioned; effective date (March 1997) inferred only |
| "Built or changed after March 1, 1997" inspection rule | SOFTENED | removed date-specific rule |
| TDI lists A/C units among items needing certification | CORRECTED | TDI: separate WPI-8 issued for the A/C unit once installed and inspected; source switched to TDI inspection-process page |
| Condenser pad/anchoring requirements | CONFIRMED/clarified | TDI product evaluation (MEC) |
| Permit Dept at 1149 Ellsworth; fee schedule by tonnage; condenser/air handler/heater entries; contractor registration | SOFTENED | none confirmed; now "own Permit Department, publishes a fee schedule" |
| 2024 UMC and 2024 IECC adoption; Feb 2, 2026 compliance documentation with load calcs | REMOVED | not confirmed (city form names 2021 IECC); replaced with general energy-code paperwork claim from city IECC form |
| CenterPoint wires, competitive market | CONFIRMED | ElectricRates 77506 |
15 claims checked, 7 confirmed, 3 corrected, 4 softened, 1 removed.

All 7 pages: build OK, check.py 0 errors / 0 warnings, similarity max 0.5% city-to-city, max 0.6% vs Dallas, no 8-word shared runs. No em/en dashes added.

### fc7

# fc7 fact-check: Katy, Sugar Land, Missouri City, Pearland, Friendswood, League City, Baytown

Method: WebSearch only (WebFetch blocked by egress proxy on the first try: missouricitytx.gov). About 37 searches. Every verdict below except "common knowledge" and INTAKE checks rests on search-result summaries of the source pages; none of the source pages themselves could be opened.

Business-model claims on all seven pages (free line, automated assistant, transfer to an independent local company, callback info, customer pays the company, referral disclosure, ask for the ACR license and check TDLR) were checked against INTAKE.md: CONFIRMED. No named HVAC companies, no places outside greater Houston, no DIY refrigerant, electrical or gas instructions, no line prices.

## /ac-repair/katy-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Cane Island name, stagecoach stop on San Felipe Road by 1847 | CONFIRMED | Houston History Magazine (Thornock); THC marker |
| Platted 1895, post office and name Jan 1896, MKT line | CONFIRMED | City of Katy history; Houston History Magazine |
| Rice farming | CONFIRMED | Houston History Magazine |
| Incorporated 1945 | CONFIRMED | Houston History Magazine; Katy Times |
| 2020 census 21,894; Harris, Fort Bend, Waller counties | CONFIRMED | Census QuickFacts; Wikipedia |
| Cinco Ranch unincorporated, nearly 17,000 (16,899), about 10 miles SE | CONFIRMED | Census QuickFacts; Wikipedia |
| Corps closed gates "on August 25, 2017" | SOFTENED | Search confirmed gates held closed during Harvey and releases began Aug 28; exact closure date not confirmed. Now "kept the gates closed during the storm" |
| Fort Bend leaders named Canyon Gate, Kelliwood, Cinco Ranch, Mason Road | CONFIRMED | Fort Bend County judge release; Community Impact |
| Court "found the counties knew subdivisions were going up inside the Barker flood pool without doing enough to warn buyers" | CORRECTED | No source shows the court made a county failure-to-warn finding. Replaced with the Dec 2019 Court of Federal Claims takings ruling for upstream properties |
| Katy ISD +14,870 students, 18.6% over five years, most in region | CONFIRMED | Community Impact (PASA study) |
| "Most of that growth" in the northwest | SOFTENED | Article says "huge growth in the northwest"; now "Much of that growth" |
| City permit for AC/heating installs; annual contractor registration | CONFIRMED | City of Katy permits page and registration form |
| "works from the 2021 International codes" | SOFTENED | City says it adopted the 2021 International Building Codes; now worded that way |
| CenterPoint delivers electricity; retail choice | CONFIRMED | Katy EDC; ElectricRates |
| Gas from CenterPoint or SiEnergy depending on address | CONFIRMED | Katy EDC utilities page |
| R-22 no new U.S. production or import since 2020 | CONFIRMED | Common knowledge, EPA phaseout page |
| Gas smell / CO guidance | CONFIRMED | Safe-guidance rule |
16 claims checked: 11 confirmed, 1 corrected, 3 softened, 0 removed (plus the business claims).

## /ac-repair/sugar-land-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Austin land grant to Samuel May Williams 1828, sugarcane | CONFIRMED | Imperial Sugar histories; city documents |
| Imperial Sugar company town with housing, schools, stores, doctors | CONFIRMED | City of Sugar Land history (housing, schools, hospitals, commercial) |
| Homes and land sold after WWII, employees first | CONFIRMED | City publication |
| Incorporated 1959 | CONFIRMED | City history (election Dec 29, 1959) |
| Original refinery stopped refining 2003 | CONFIRMED | Imperial Sugar histories |
| 2020 census 111,026; 2010 78,817; Telfair, Lake Pointe, annexation | CONFIRMED | Sugar Scoop (city) |
| Greatwood and New Territory annexed December 2017 | CONFIRMED | Community Impact (Dec 12, 2017) |
| Homeowner brochure: HVAC system and duct work need a permit | CONFIRMED | City permit brochure |
| Harvey mandatory evacuations LID 1 and 7 | CONFIRMED | Patch; Community Impact |
| About 230 homes, up to 6 inches, Settlers Park and Chimney Stone | CONFIRMED | Patch (city recovery report). Note CI reported 250 to 260 |
| No Fort Bend levee breached or overtopped (engineer) | CONFIRMED | Community Impact (Costello Engineering) |
| "More than 30 inches of rain overwhelming interior drainage" | CORRECTED | The 30-inch figure was general coastal rainfall; officials said rain inside the districts was several times design capacity. Reworded |
| "Two levee districts built a $9.1 million pump project" at Steep Bank Creek | CORRECTED | It is a Fort Bend County expansion of the Steep Bank Creek pump station in Riverstone, $9.1 million, one of the county's most significant since Harvey |
| CenterPoint delivery, retail choice | CONFIRMED | ElectricRates |
| R-22 production/import ended 2020 | CONFIRMED | EPA |
15 claims checked: 13 confirmed, 2 corrected, 0 softened, 0 removed.

## /ac-repair/missouri-city-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| 1890 two Houston investors, marketed in St. Louis, "genial sunshine and eternal summer" | CONFIRMED | THC marker; Wikipedia |
| Name Missouri City 1893 | CONFIRMED | Wikipedia (three years later); marker says platted 1894 |
| Incorporated March 1956, partly to avoid Houston annexation | CONFIRMED | Texas House resolution (March 13, 1956); Wikipedia |
| Mostly Fort Bend, small part Harris | CONFIRMED | Wikipedia; Census |
| 2020 census 74,259; 2010 67,358 | CONFIRMED | Census QuickFacts |
| Zoning "since 1981" | SOFTENED | Only Wikipedia gives 1981; city FAQ confirms zoning. Now "Unlike Houston, it has zoning" |
| Fondren Park "early 1960s" | SOFTENED | Average build year 1966; now "in the 1960s" |
| Quail Valley from 1969 | CONFIRMED | Wikipedia; golf course 1970 |
| Sienna tornado "75 to 100 homes" | CORRECTED | Sheriff/county reported about 50 homes hit in Sienna Plantation; tornadoes Aug 26 confirmed |
| Lake Olympia about 100 homes (mayor) | CONFIRMED | Community Impact |
| Water in Quail Valley and Sienna | CORRECTED | Officials named Lake Olympia, Quail Valley and Riverstone as hardest hit; reworded |
| Brazos at Richmond crested above 55 feet | CONFIRMED | Community Impact (about 56 ft) |
| MCTX Self Service portal; inspections only after permit | CONFIRMED | City mechanical permit form (search summary) |
| $35 application fee plus duct fees | CONFIRMED | City mechanical permit application ($35; duct $35 min plus $2/outlet) |
| CenterPoint delivery, retail choice | CONFIRMED | Base Power |
| R-22 2020 | CONFIRMED | EPA |
16 claims checked: 11 confirmed, 2 corrected, 2 softened (plus 1 reworded within a corrected passage), 0 removed.

## /ac-repair/pearland-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Named for pear trees near an early rail stop; 1900 hurricane wiped out orchards | CONFIRMED | Texas Senate/House resolutions; Community Impact |
| Incorporated 1959 | CONFIRMED | City (November 1959) |
| About 20 miles south of downtown; mostly Brazoria with parts of Harris and Fort Bend | CONFIRMED | City; Pearland EDC |
| 37,640 (2000), 91,252 (2010), 125,828 (2020) | CONFIRMED | City population page; Census |
| About 132,900 by January 2024 (city estimate) | CONFIRMED | City population page |
| 7th fastest growing 50,000+ city, year to July 2015, 2016 release | CONFIRMED | Census cb16-81 |
| Clear Creek 500-year flood at SH 288 | CONFIRMED | Community Impact |
| 1,000+ homes, about 30 businesses, 205 rescued by boat | CONFIRMED | Community Impact (early city estimates) |
| Master drainage plan "with Brazoria County Drainage District No. 4" | SOFTENED | Plan confirmed; partner not confirmed. Now "began work on a master drainage plan" |
| CenterPoint main delivery; TNMP serves a small portion | CONFIRMED | TNMP hurricane-season page and tariff list Pearland |
| CenterPoint is the gas company | CONFIRMED | Pearland EDC |
| City permits for MEP work; contractor registration before permits and inspections | CONFIRMED | City contractor requirements page |
| Gas leak / CO guidance | CONFIRMED | CenterPoint gas leak page (no number given on page) |
13 claims checked: 12 confirmed, 0 corrected, 1 softened, 0 removed.

## /ac-repair/friendswood-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Quakers Frank Brown and T. Hadley Lewis, 1895, Society of Friends | CONFIRMED | Galveston County Museum; Community Impact |
| Only permanent Texas town begun as a Quaker colony | CONFIRMED | Galveston County Museum |
| Figs, "Satsuma oranges and rice fields" | SOFTENED | Fig industry confirmed (THC marker); oranges and rice not confirmed. Now "Farming, fig orchards in particular" |
| Fewer than 500 people through the 1940s | CONFIRMED | Galveston County Museum |
| Incorporated 1960 | CONFIRMED | Galveston County Museum; city history |
| MSC "about 10 miles away", "Hundreds of NASA employees" | CORRECTED / SOFTENED | Sources say seven miles east, opened 1963; now "a few miles to the east"; "NASA families moved in" |
| Mostly Galveston County with part in Harris | CONFIRMED | Common knowledge / Wikipedia |
| "Third or fourth air conditioner" | SOFTENED | Speculative; now "well past their first air conditioner" |
| Roughly 1,000 residents rescued by boat | CONFIRMED | Community Impact |
| City assessment "about 2,800 households flooded" | CORRECTED | Not found; city figures in local reporting: about 2,410 homes damaged (later reports above 2,700). Now "roughly 2,400 damaged homes", sourced to Community Impact |
| 2019 Rice/Bedient study "more than 2,000 single-family homes" | REMOVED | Could not verify; sentence and source removed (acquisition guidelines source also removed) |
| Frenchmans Creek townhome buyout with CDBG-DR, city and county | CONFIRMED | Community Impact |
| TNMP Gulf Coast territory; outage 888-866-7456 option 1; Report Outage online; possible fee | CONFIRMED | TNMP contact, outages and severe weather pages |
| "TNMP owns the lines in Friendswood" / "not CenterPoint's" | SOFTENED | TNMP lists Friendswood; added "your bill names the delivery company for your address" |
| Monthly permit reports list HVAC change outs as mechanical permits | CONFIRMED (not independently re-searched) | City permit report cited; consistent with other cities' reports |
15 claims checked: 8 confirmed, 2 corrected, 4 softened, 1 removed.

## /ac-repair/league-city-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| G. W. Butler from Louisiana 1854, Chigger Bayou and Clear Creek, Butler's Ranch / Clear Creek | CONFIRMED | Texas House H.R. 804; Wikipedia |
| Butler persuaded Galveston financier League to buy land and lay out streets | CONFIRMED | H.R. 804 |
| NASA center in Clear Lake 1960s drove growth | CONFIRMED | Common knowledge |
| About 114,000 in 2020 on about 51 sq mi | CONFIRMED | 2020 census 114,392; 51.4 sq mi |
| "Close to three out of four homes owner occupied" | SOFTENED | Only ZIP-level third-party figure (about 75%) found; now "most homes are owner occupied" |
| TNMP / CenterPoint split, 77573 split | CONFIRMED | ElectricityPlans; TXU; TNMP tariff |
| Galveston one of 14 first tier coastal counties | CONFIRMED | TDI / TDLR list |
| AC units on TDI certification list; pad rules; WPI-8 by TDI inspector or appointed engineer; TWIA requires it | CONFIRMED | TDI general questions, product evaluation reqs, Klopfenstein deck |
| "Independent HVAC company with its own crews" | SOFTENED | Unverifiable claim about partners; now "serving homes around League City" |
9 claims checked: 7 confirmed, 0 corrected, 2 softened, 0 removed.

## /ac-repair/baytown-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Oil found at Goose Creek June 2, 1908; Aug 23, 1916 gusher at 2,017 ft, about 10,000 bbl | CONFIRMED | Handbook of Texas / Visit Baytown timeline |
| Humble refinery begun fall 1919, completed April 1921, plant and town named Baytown | CONFIRMED | Handbook of Texas |
| Pelly annexed Baytown 1945; 1947 merger vote; City of Baytown Jan 24, 1948 | CONFIRMED | Handbook of Texas (Dec 1945 annexation); Texas resolution |
| Reaches into Chambers County | CONFIRMED | TDI / common knowledge |
| Cracks at the field about 1918, first sign of regional subsidence | CONFIRMED | HGSD; added that those came from oil and gas withdrawal |
| Brownwood 1937 by Humble executives, between Burnet, Crystal and Scott bays | CONFIRMED | UH thesis; Houston History Magazine |
| Carla 1961 first clear sign | CONFIRMED | UH thesis |
| HGSD created by Legislature 1975 | CONFIRMED | HGSD |
| Alicia 1983, Brownwood sunk about 10 ft, abandoned, became Baytown Nature Center | CONFIRMED | UH thesis; Houston History Magazine |
| HGSD "estimates more than ten feet ... in eastern Harris County" | CORRECTED | Not confirmed in that form; replaced with the confirmed Brownwood ten-foot figure |
| "District reports its limits have worked in Galveston County and central and SE Harris" | SOFTENED | Not confirmed in search; now "The district was created to limit that pumping" |
| Harris side: TDI catastrophe area only east of SH 146 in La Porte, Morgan's Point, Pasadena, Seabrook, Shoreacres; Baytown not listed | CONFIRMED | TDI Harris County page |
| Chambers is a first tier county | CONFIRMED | TDI / TDLR |
| AC units certified; condenser pad rules; WPI-8 | CONFIRMED | TDI sources |
| Residential permit list includes heating/AC installs and replacements, water heater and boiler | CONFIRMED | City of Baytown permit page |
| CSS portal: register, professional license (contractors), apply, inspections | CONFIRMED | City Building Permits page |
| Owner occupied "about 52 percent" | CORRECTED | QuickFacts 2019-2023: 53.1%; now "about 53 percent" |
17 claims checked: 13 confirmed, 3 corrected, 1 softened, 0 removed.

## Other notes
- CenterPoint gas leak number: confirmed CenterPoint lists 888-876-5786 (and 713-659-2111) for Houston. None of these seven pages prints a gas leak number, so nothing to change.
- Build: `python3 build.py --out /tmp/claude-0/fc/fc7/dist` OK; check.py 0 errors for all seven URLs; similarity: area max 1.7%, Dallas max 0.6%. One 8-word run with Dallas /services/ that my League City edit introduced ("to an independent hvac company that works in") was reworded; now 0.

### fc8

# fc8 fact-check: Tomball, Fulshear, Fresno, Richmond (/ac-repair/<slug>.html)

All verification used WebSearch result summaries. WebFetch was blocked (census.gov egress blocked), so no source page could be opened directly. Every claim below was verified from search summaries only.

## /ac-repair/tomball-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| 2010 count 10,753; 2020 count 12,341 | CONFIRMED | Census QuickFacts (summary) |
| July 2025 estimate 15,768 | CORRECTED | Only Wikipedia had it; replaced with the QuickFacts V2023 estimate 14,201; source URL now PST045223 |
| Began as Peck, renamed Tomball 1907 for Thomas Ball | CONFIRMED | tomballtx.gov/113/History-of-City (Dec 2, 1907); THC marker |
| Oil struck 1933, incorporated 1933 | CONFIRMED | TSHA (oil May 27 1933, incorporated July 1933) |
| "Highest point in Harris County", trains rolling downhill | REMOVED | No source found; Depot Museum source removed |
| City history source URL /113/History-of-Tomball | CORRECTED | Live page is /113/History-of-City |
| City owns and runs gas system in city limits, bills it | CONFIRMED | tomballtx.gov/128/Gas, utility billing page |
| City does not furnish electricity, points to Power to Choose | CONFIRMED | tomballtx.gov/128/Gas |
| CenterPoint electric delivery includes Tomball | CONFIRMED | CenterPoint service-centers.pdf (Cypress service area) |
| Gas leak: do not call from inside | CONFIRMED | City gas FAQ |
| HVAC needs its own permit "separate from a building permit" (forms say) | SOFTENED | Now: city has its own mechanical permit application |
| Double fees for work without a permit (attributed to the form) | CORRECTED | Attributed to FY 2025-26 Master Fee Schedule (added as source) |
| Permit void if work not started within 6 months | CONFIRMED | Mechanical Permit Application |
| Hurricane Beryl July 2024 long outages | CONFIRMED | common knowledge / Texas Standard source |
| No line-does-work, no named companies, safety advice OK | CONFIRMED | Rules 1, 3, 6 |

14 claims checked: 9 confirmed, 3 corrected, 1 softened, 1 removed.

## /ac-repair/fulshear-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| 2010 count 1,134; 2020 count 16,856 | CONFIRMED | Census QuickFacts / data.census.gov profile |
| July 2025 estimate 64,630 | CONFIRMED | Census QuickFacts V2025; source URL changed to PST045225 |
| 2nd fastest growing US city of 20,000+, 2024 to 2025 | CONFIRMED | Census Vintage 2025 release, Spectrum News |
| Churchill Fulshear, Old Three Hundred, Mexican grant 1824 | CONFIRMED | fulsheartexas.gov history (July 16, 1824) |
| Son gave railroad right of way 1888; town laid out 1890 | CONFIRMED | Fulshear history sources (Churchill Jr., SA&AP Railway) |
| A few hundred people for most of 20th century | CONFIRMED | ~250 peak early 1900s |
| Incorporated 1977, now home rule | CONFIRMED | city / history summaries |
| CenterPoint electric delivery; city points to Power to Choose; city sells no power | CONFIRMED | Fulshear Resident Guide; CenterPoint service-centers.pdf (Katy/Sealy) |
| Two gas companies: CenterPoint and Si Energy | CONFIRMED | Fulshear Resident Guide |
| City bills water, sewer, trash | CONFIRMED | Utility Billing page |
| CenterPoint gas leak 888-876-5786 | CONFIRMED | centerpointenergy.com/en-us/safety/reporting/gas-leak (source URL replaced; old contact-us URL dropped) |
| Permit to replace mechanical system in city and ETJ; narrow exemptions | CONFIRMED | Planning Services page |
| Trade permits (HVAC) via online portal (GovWell) | CONFIRMED | Applications/Forms page |
| Inspectors work weekdays | CONFIRMED | Inspections: Mon to Thu 8 to 3, Fri to 2 |

14 claims checked: 14 confirmed, 0 corrected (2 source URL fixes), 0 softened, 0 removed.

## /ac-repair/fresno-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Census designated place, unincorporated | CONFIRMED | Census/TSHA |
| 2020 count 24,486; 2010 19,069; ~8.5 sq mi land | CONFIRMED | QuickFacts (8.52 sq mi) |
| More people than Richmond (11,627) in 2020 | CONFIRMED | arithmetic |
| "northeastern Fort Bend County, south of Houston" | CORRECTED | now "eastern Fort Bend County, southwest of downtown Houston" |
| Land patented 1824, cotton plantations | CONFIRMED | TSHA |
| Name "most likely" from Fresno, California settler | SOFTENED | TSHA says "reportedly" |
| Post office 1910; 10 residents, 1 business 1933 | CONFIRMED | TSHA |
| Around a hundred people 1940s to 1960s | REMOVED | not in search summary |
| Houston growth 1970s and 1980s; 3,182 (1990), 6,603 (2000) | CONFIRMED | TSHA |
| "roughly tripled again by 2010" | CORRECTED | "nearly tripled" (6,603 to 19,069) |
| CenterPoint electric delivery includes Fresno | CONFIRMED | service-centers.pdf (H.O. Clarke area) |
| County development permit at 400 sq ft new structure or addition; permits group | CONFIRMED | Fort Bend County Engineering permit pages |
| Fresno Plan: flood protection, ditches, Mustang Bayou | CONFIRMED | Precinct 2 10 Point Plan |
| Regional detention via federal grant with GLO help | CONFIRMED | 10 Point Plan; added county Aug 2024 GLO press release as source |
| 2019 bond with money for Mustang Bayou | CONFIRMED | 10 Point Plan |
| Gas/CO safety, no DIY | CONFIRMED | rule 6 |

16 claims checked: 11 confirmed, 2 corrected, 1 softened, 1 removed (plus 1 source added).

## /ac-repair/richmond-tx.html
| Claim | Verdict | Source / note |
|---|---|---|
| Old Three Hundred log fort at bend of Brazos "in 1822" | SOFTENED | City says settlers arrived early 1822; marker dates fort to Nov 1821. Now "settled here in 1822 around a log fort" |
| Handy and Lusk laid out town 1837; Republic incorporated it May 1837 | CONFIRMED | TSHA, city history |
| Voters made it county seat January 1838 | CORRECTED | TSHA: became seat when county created December 1837 |
| Steamboats and barges carried cotton toward Galveston | REMOVED | unverified |
| 2020 count 11,627 | CONFIRMED | QuickFacts |
| "Density fell from 2010 as the city took in more land" | CORRECTED | now "a little below the 11,679 counted in 2010" |
| July 2025 estimate 13,389 (+15%) | CORRECTED | not found anywhere; replaced with QuickFacts V2023 estimate 12,816 |
| City bills water, wastewater, trash; MUD areas | CONFIRMED | city utility page (source as cited) |
| Harvey: San Bernard mandatory first, Brazos voluntary, then mandatory | CONFIRMED | Community Impact; Fort Bend County order |
| Crest 55.18 ft "the county judge said" | CORRECTED | NWS gauge RMOT2 record 55.19 ft (9/2017); NWS source added |
| 59 ft forecast; "800 year flood that no levee is designed to stop" | CORRECTED | now: judge called forecast flood an 800 year event exceeding the design of county levees (Fort Bend County order, added as source); 59 ft dropped |
| More than 5,000 evacuations | REMOVED | not found; panel now says county ordered evacuations for many levee improvement districts (confirmed) |
| Patch source | REMOVED | content unverifiable; replaced with NWS + county order |
| Levee improvement districts description | CONFIRMED | common / Community Impact |
| SEER2 since Jan 1 2023; Southeast 14.3 under 45k, 13.8 at/above | CONFIRMED | DOE standards (well established) |
| R-22 not made or imported in US since 2020 | CONFIRMED | EPA HCFC phaseout |
| CenterPoint electric delivery includes Richmond | CONFIRMED | service-centers.pdf (Fort Bend/Wharton) |
| CenterPoint gas serves Richmond, "Texas Coast division" | SOFTENED | division mapping ambiguous across CenterPoint docs; now "list Richmond among the Texas cities it serves" |
| CenterPoint gas leak 888-876-5786 | CONFIRMED | CenterPoint gas-leak page (source URL replaced) |
| MyGovernmentOnline portal for permits and inspections | CONFIRMED | richmondtx.gov (effective Oct 14 2024) |
| Contractor must register with city before pulling a permit | CONFIRMED | city news item 3659 |
| City adopted codes include mechanical code | CONFIRMED | 2024 I-codes adopted |

22 claims checked: 11 confirmed, 6 corrected, 2 softened, 3 removed.

Build, check.py (0 errors, 0 warnings) and similarity.py (max 0.5% internal, 0.4% vs Dallas, no 8-word runs) pass for all four pages.
