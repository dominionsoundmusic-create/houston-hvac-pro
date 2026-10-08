# Writing guide for houstonairandheating.com pages (Playbook 2.0 rebuild, Oct 8 2026)

Repo: /home/user/houston-hvac-pro (branch `build`). Read these first, in full:
1. `CLAUDE.md` (the hard rules) and `INTAKE.md` (the facts; it wins over everything; read "WHAT THE
   BUSINESS ACTUALLY IS" twice).
2. `SERVICES.md` and `docs/keyword-plan.md` (your page's URL, TARGET keyword and supporting keywords,
   including the Question rows to turn into FAQs).
3. `src/data/site.json` (names and URLs of services, guides and areas).
4. `src/templates/macros.html` (service_cards, guide_cards, area_pills, related, call_box,
   how_it_works_short, disclosure, license_check, sources).
5. STRUCTURE MODELS ONLY: pages of the sister site Dallas Air & Heating, built with the same system:
   `/home/user/dominionsoundmusic-create/dallas-hvac-pro/src/pages/ac-repair.html` (service),
   `.../furnace-repair.html` (service), `.../plano-ac-repair.html` (area). Match their depth, section rhythm
   and component use. NEVER copy their wording, sentences, FAQs or facts. `scripts/similarity.py` compares
   every Houston page with every Dallas page and FAILS on any shared run of 8 words. Write from scratch.
6. The old Houston page for your URL in `docs/old-site/` (if any) for research leads only. Keep useful
   facts only after you verify them; do not copy or lightly reword its paragraphs (it was written in
   contractor voice and is being replaced).

## The business, in one paragraph
Houston Air & Heating is a free phone line and website, NOT an HVAC company. An automated assistant
answers (832) 662-4107 any hour, asks what the caller needs (the same line also takes roofing and
pressure washing calls, so it asks first), asks briefly what is going on with the heating or cooling,
then transfers the call to an independent, locally owned HVAC company serving the Houston area. That
company hears a short summary before it picks up. If it cannot answer, the caller's name, callback
number, area and problem are passed along for a call back. The company inspects, quotes, does the work
and is paid directly by the customer. The line never repairs, installs, services, quotes or schedules
anything, holds no license, never charges the caller, and may be paid a referral fee by the companies.
Write "the company you are put through to", "the HVAC company", "a careful technician". Never "our
technicians", "our trucks", "we repair", "we install", "we are licensed/insured", "we'll send someone".
Never say the connected companies are licensed, insured, certified or rated. Tell readers to ASK for the
company's Texas ACR license number and check it on the TDLR license search.
Never name any HVAC company. Avoid equipment brand names.

## Hard rules (scripts/check.py enforces most of them)
- No em dashes or en dashes anywhere (copy, titles, descriptions, FAQs, alt text). Use commas, colons,
  periods or "to" ("95 to 100 degrees"). American spelling. No eyebrow labels or badges.
- Only greater-Houston places (Harris, Fort Bend, Montgomery, Brazoria, Galveston, Waller, Chambers
  counties). Never Dallas, Fort Worth, DFW, Austin, San Antonio or any other Texas metro, not even as a
  comparison. Never Oncor or North Texas facts.
- Never invent licenses, insurance, reviews, ratings, prices, years in business, team members, job
  counts, statistics, response times, guarantees or awards. Public statistics are fine with the source
  named and listed. Prices: explain what drives price; a published range only with its source named on
  the page and a note that real quotes vary. Never present a price as the line's price.
- Banned (checker fails): "free estimate(s)", "same-day", "guarantee(d)", "best price", "cheapest",
  "top-rated", "years of experience", "#1", "number one", "licensed and insured", "your trusted partner",
  "one-stop solution", "look no further", "unmatched excellence", "we've got you covered", response-time
  promises ("within 2 hours").
- No DIY for refrigerant, electrical internals (capacitors, contactors, panels), gas or furnace burners.
  Safe homeowner checks only: thermostat mode, setting and batteries; the air filter; reset a tripped
  breaker ONCE (if it trips again, stop and call); clear leaves and debris away from the outdoor unit;
  look for water at the indoor unit or a tripped float switch. Gas smell: leave the house, then call the
  gas utility's emergency line or 911 from outside (CenterPoint Energy is the gas utility for most of the
  Houston area; verify for your town; its gas leak number must come from centerpointenergy.com). Carbon
  monoxide alarm: get everyone out and call 911.
- Every fact that is not common knowledge carries a source in the page's Sources list with a real URL
  you opened. If you cannot verify it, leave it out.

## Voice
Plain, specific, warm, Houston-local. Second person. Short paragraphs, roughly 7th to 8th grade reading
level; explain a technical word the first time. Explain why. No filler, no superlatives, no keyword
stuffing. The target keyword appears naturally in the title, H1, first paragraph, one H2 and the meta
description. Use "in Houston" / "in [City], TX" phrasing where it reads naturally.

## Page file format
`src/pages/<file>.html` with YAML front matter, then `{% block content %}...{% endblock %}`.

```yaml
---
type: service            # service | guide | area
url: "/ac-repair/katy-tx.html"   # ONLY for pages whose live URL ends in .html (city pages, old guides)
title: "..."             # 50 to 65 chars, unique, keyword near the front
description: "..."       # 120 to 160 chars, unique, no dashes
h1: "..."                # one H1, unique
crumb: "Katy"
keyword: "a c repair katy"
city_name: "Katy"        # area pages only
published: "2026-10-08"  # guides only
hero:
  image: katy-tx-hero.jpg        # planned 1920x1080 photo, OR an existing photo used directly
  alt: "..."
  desc: "Artistly prompt (only for a planned photo)."
  fallback: hvac-01-hero.jpg      # existing photo shown until the planned one exists
  fallback_alt: "..."             # accurate alt for the fallback photo
  lead: "One or two sentences under the H1."
  secondary_label: "..."          # optional, a real page or an in-page anchor, never a form
  secondary_href: "/..."
schema_service:          # service and area pages
  name: "Free connection to a local AC repair company in Katy, Texas"
  type: "Air conditioning repair referral"
cta_title: "..."         # short, specific to the page
faqs:                    # 3 to 6 (never more), phrased the way people ask (use the Question rows)
  - q: "..."
    a: "<p>...</p>"
---
```
Quote YAML strings that contain a colon. Inside FAQ answers use `&amp;` or the word "and" for "&".

## Building blocks (existing classes only; do not edit CSS, templates, build.py, check.py or site.json)
- Reading column: `<section class="prose">...</section>`. Plain paragraphs, h2, h3, lists.
- Color band: `<section class="band band--tint"><div class="wide">...</div></section>`. The build turns
  these into bold brand-blue / heating-red bands with white text. Use ONE (at most two) per page, with
  white prose sections between; never two bands in a row; the FAQ band and the final call band are added
  automatically after your content, so do not end your content with a band.
- Two columns, text and photo: inside `.prose`, `<div class="split"><div>text</div>{{ img(...) }}</div>`.
- `<ol class="steps">` numbered process; `<ul class="checks">` checklist; `<div class="grid-2">` /
  `<div class="grid-3">` of `<div class="panel">` (add `panel--do` / `panel--dont`); `<ul class="facts">`
  of `<li><strong>label</strong>text</li>`; tables in `<div class="table-wrap"><table>` with
  `<caption class="sr">`, `<thead>`, `scope` on th; `<div class="note">` callout,
  `<div class="note note--orange">` warning.
- Macros: `{{ m.how_it_works_short() }}`, `{{ m.disclosure() }}`, `{{ m.license_check() }}`,
  `{{ m.call_box('text') }}`, `{{ m.service_cards(['slug', ...]) }}`, `{{ m.guide_cards(['slug']) }}`,
  `{{ m.area_pills(exclude='katy-tx') }}`, `{{ m.related(['slug','guide:slug','area:slug'], 'Title') }}`,
  `{{ m.sources([{'label': '...', 'url': '...'}, ...]) }}` (always last, inside the last prose section).
- Links: service pages `/ac-repair/`, `/air-conditioning-repair/`, `/emergency-ac-repair/`,
  `/ac-installation/`, `/furnace-repair/`, `/heating-repair/`, `/hvac-tune-up/`, `/commercial-hvac/`;
  guides `/ac-repair-cost.html`, `/ac-not-cooling.html`, `/ac-leaking-water.html`,
  `/repair-or-replace-ac/`, `/is-hvac-tune-up-worth-it/`, `/hvac-tune-up-checklist/`, `/hvac-company/`,
  `/water-heater-repair.html`, `/free-ac-guide/`; cities `/ac-repair/<slug>.html`; core `/how-it-works/`,
  `/service-areas/`, `/services/`, `/about/`, `/faq/`, `/contact/`. Link to 3+ related pages naturally.

## Images
Call: `{{ img('file.jpg', 'alt', 1200, 800, desc='prompt', fallback='existing.jpg', fallback_alt='...') }}`.
An existing photo used directly needs no desc/fallback: `{{ img('attic-air-handler.jpg', 'alt', 1200, 686) }}`.
Every content page: a hero plus at least two in-body images; no photo repeated within one page.
Alt text with technicians must not imply they work for the line ("A technician checks...").

Existing photos in src/static/images (use first):
Heroes 1920x800: `hvac-hero.jpg` (technician working on a condenser beside a brick wall at sunrise),
`hvac-01-hero.jpg` (technician in gloves reading a gauge manifold at an outdoor unit, flower bed),
`hvac-02-hero.jpg` (two technicians servicing a condenser beside a white siding house, evening light),
`hvac-03-hero.jpg` (technician kneeling at large indoor air handlers with a multimeter, city view),
`hvac-04-hero.jpg` (large rooftop HVAC units, worker in a hard hat, downtown skyline),
`hvac-05-hero.jpg` (technician checking an indoor air handler and foil duct, close),
`hvac-06-hero.jpg` (technician walking with a tool bag to a red service van in a driveway at dusk),
`homeowner-thermostat-window.jpg` (woman looking at a wall thermostat by a sunny patio door).
Cards 1200x675 (same scenes cropped): `hvac-01-card.jpg` to `hvac-06-card.jpg`.
1344x768: `thermostat-warm-light.jpg` (finger pressing a wall thermostat, warm lamp light),
`homeowner-phone-call.jpg` (smiling woman on a phone call in a bright living room),
`couple-reviewing-papers.jpg` (older couple with papers and a tablet at a kitchen table, mini-split on wall),
`installers-new-condenser.jpg` (two installers setting a new condenser beside a stone and brick home),
`technician-gauges-condenser.jpg` (technician reading gauges at a condenser, brick home, wood fence),
`technician-crouched-condenser.jpg` (technician crouched at a condenser beside a brick wall, wood fence),
`two-story-siding-home.jpg` (two-story blue siding home, condenser beside it, big lawn, sunny),
`two-condensers-brick-home.jpg` (two condensers beside a red brick home, green lawn).
1200x686: `attic-air-handler.jpg` (attic air handler, flex ducts, pink insulation),
`gas-furnace-open-panel.jpg` (gas furnace with its front panel off, flashlight).

Planned new photos (Maurice generates them in Artistly later): only where no existing photo fits. Each
needs a unique descriptive filename, a `desc=` prompt and a `fallback=` existing photo. Prompt style:
"Wide cinematic landscape shot, subject positioned on the right third of frame, well lit," then a
specific, bright, realistic Houston-area scene (the town's real housing: e.g. two-story brick and
siding suburban homes, raised slab homes, live oaks, loblolly pines in the north suburbs, crape
myrtles, St. Augustine lawns, wood privacy fences, condensers on raised stands in flood-prone areas,
humid hazy Gulf Coast sky), then "realistic photo, no text, no logos, no house numbers, no recognizable
faces". Never use the word "penetration" (Artistly blocks it).
- Area pages: hero = PLANNED `<slug>-hero.jpg` (1920x1080) with the fallback given in your brief, plus
  ONE planned in-body local photo (with fallback) and at least one existing photo used directly.
- Service and guide pages: hero = the existing photo in your brief, used directly. In-body: existing
  photos; at most ONE planned in-body photo where nothing existing fits (with fallback).

## Content each page needs
Service and guide pages (Prompt 9): what it is; who it is for; common problems; what a careful
technician does and why; what to expect; options; Houston-specific context (verified only: Gulf Coast
heat and humidity, NWS Houston/Galveston climate data, hurricane season and long power outages such as
Hurricane Beryl in July 2024, the February 2021 freeze, CenterPoint Energy as the electric wires
company and main gas utility in much of the area with retail electric choice, City of Houston permits
for HVAC work, flooding history); safe homeowner checks where relevant; what to ask; related pages; 3 to
6 FAQs; at least one distinctive design treatment (symptom table, decision panels, timeline, checklist,
comparison table). About 1,500 to 2,200 words of page-specific copy. Sources list at the end.

Area pages (Prompt 11): hero; FIRST H2 names the town ("Katy: ..."), with two local paragraphs and a
photo beside them (split); services genuinely relevant there (`m.service_cards([...])`); a section
titled "Why [Town] homeowners call the line" with FOUR distinct local reasons as
`<div class="grid-2">` of four `<div class="panel"><h3>..</h3><p>..</p></div>`, built only from facts on
that page plus what the line truly does (free, 24/7, transfers to an independent local company, caller
pays the company not the line, the site explains the TDLR license check); verified local context
(electric delivery company and whether retail choice applies there, gas utility, county, housing age
and growth from Census or city data, flood and storm history, the city's permit rules for HVAC
replacement, any utility or city rebate, local climate facts); area FAQs; `m.how_it_works_short()`;
nearby areas (`m.area_pills(exclude='<slug>')`); sources. Never claim an office, address, job history,
customer count or travel time. Each city page must be built around what is actually different there.
Two city pages must not share paragraphs: the checker fails any pair of city pages above 15% overlap.

## Research standard
- Research each page on the web BEFORE writing (WebSearch, then WebFetch the pages). Prefer primary
  sources: city and county websites (houstontx.gov, houstonpermittingcenter.org, cityofkatytx.com,
  sugarlandtx.gov, pearlandtx.gov, etc.), TDLR (tdlr.texas.gov) and Texas statutes, CenterPoint Energy,
  Entergy Texas, TNMP, electric co-ops, ERCOT, PUC of Texas, NWS Houston/Galveston (weather.gov/hgx),
  NOAA, U.S. Census QuickFacts, EPA, DOE (energy.gov), ENERGY STAR, Texas A&M, Harris County Flood
  Control District. Today's date is Oct 8 2026: check facts are current.
- Every number, date, rule, phone number, fee and named program comes from a source you opened; that
  source goes in the Sources list with its real URL. If you cannot verify it, leave it out.
- Facts shared by many pages (the Beryl outage, the 2021 freeze): say them in your own words, only where
  they matter to that page, never the same paragraph twice.

## Validation (from the repo root; NEVER a plain `python3 build.py`, it writes dist/ and docs/)
```
python3 build.py --out /tmp/<your-name>/dist
python3 scripts/check.py --dist /tmp/<your-name>/dist --skip-links --only <your page URL>
python3 scripts/similarity.py --dist /tmp/<your-name>/dist --dallas /home/user/dominionsoundmusic-create/dallas-hvac-pro/dist --only <your page URL>
```
(build.py may print FAILED for other writers' half-finished pages; ignore those, fix your own.) Fix every
ERROR and FAIL for your pages. A WARN about word count under 1500 (which includes the template) means
the page is thin: add substance, not filler. Do not edit shared files or anyone else's pages. Do not
commit or push.

When done, report: files written, word counts, for area pages a one-sentence factual summary of the
town (max 22 words, no dashes, for the service-areas page), and any fact you could not verify and
therefore left out.
