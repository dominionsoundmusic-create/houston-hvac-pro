# Decisions log (Playbook 2.0 rebuild, Oct 8 2026)

Maurice was not available to approve anything during this run (CLAUDE.md: run straight through). Each
decision below was made from INTAKE.md, CLAUDE.md, the keyword data and the live site, and can be
reversed later.

## Build system and structure
1. **Build system copied from Dallas Air & Heating, words not copied.** build.py, scripts/check.py, the
   Jinja templates, macros, CSS, JS, self-hosted Inter font, site.json structure and netlify.toml
   (`publish = "dist"`) came from dominionsoundmusic-create/dallas-hvac-pro (main). The speed work is
   unchanged: WebP srcset at 480/800/1200/1600/1920, preloaded hero with fetchpriority high, woff2 font.
   The shared template text (how-it-works strip, license note, call band, call box) was rewritten for
   Houston so no Dallas sentence appears on this site. scripts/similarity.py fails any Houston page that
   shares an 8-word run with any Dallas page.
2. **Old live site moved to docs/old-site/.** It stays in the repo as the reference for every old URL
   (scripts/check_old_urls.py reads it). Netlify publishes dist/ only.
3. **URLs.** Every old URL keeps its exact path: city pages stay at /ac-repair/<city>-tx.html, the old
   guides keep their .html URLs (/ac-not-cooling.html, /ac-leaking-water.html, /ac-repair-cost.html,
   /water-heater-repair.html), privacy and terms keep .html. New pages use the folder style the live
   site already used (/furnace-repair/, /heating-repair/ etc.).
4. **Redirects.** The Sep 11 wildcards for retired templated sub-pages are kept (Netlify serves a real
   file before a rule without "!", so /ac-repair/* never hides the city pages; check.py now fails only
   a forced rule). Removed: `/furnace-repair/ -> /ac-repair/`, `/furnace-repair/* -> /ac-repair/`,
   `/air-conditioning-repair/ -> /ac-repair/` and its wildcard, because both are real pages again.
   Retired blog-post rules kept; their targets now point at the exact .html guide URLs
   (/ac-not-cooling.html, /ac-repair-cost.html) and at the closer new guides (/repair-or-replace-ac/,
   /is-hvac-tune-up-worth-it/). Added: /contact/thanks/ and /free-ac-guide/thanks/ (with and without the
   trailing slash) 301 to /contact/ and /free-ac-guide/ because the site is phone only.

## Pages
5. **Service pages (8).** From the keyword data: AC repair (2,900/mo), air conditioning repair
   (5,400/mo at SD 17, built as its own page with a different angle: the component-by-component repair
   guide, while /ac-repair/ is the symptom triage and city hub), emergency/24 hour AC repair (720/mo),
   AC installation (590/mo), furnace repair (210/mo), heating repair (90/mo, plus 40,500 national "near
   me"), HVAC tune-up (170 + 590 + question rows), commercial HVAC (140 + 70).
6. **Heat pumps get no page of their own.** The data has no heat pump keyword. Heat pumps and electric
   strip heat are covered on /heating-repair/, gas furnaces on /furnace-repair/, so the two heating
   pages do not compete.
7. **Guides (8 plus the book page).** Cost, not cooling, leaking water (existing URLs), repair or
   replace, is a tune-up worth it, what a tune-up includes (question rows 140 and 110+70/mo), how to
   choose an HVAC company (hvac companies in houston 1,600/mo; houston hvac companies 1,300/mo), water
   heater (see 9) and the free refrigerant book.
8. **City pages.** All 18 existing city URLs are rebuilt. Ten have 30+/mo keywords. No other
   Houston-area place in the data reaches 30/mo, so no new city pages were added. "spring branch tx"
   (could be Spring Branch in Comal County) and "furnace repair westpark" are ambiguous and left unused.
9. **/water-heater-repair.html stays as an honest guide, not a 301.** It has real demand (water heater
   repair houston tx, 590/mo, SD 20) and is indexed. The line does not take water heater calls
   (INTAKE: plumbing not offered), so the page says so plainly, explains that water heater work is
   plumbing licensed by the Texas State Board of Plumbing Examiners, and shows how to verify a plumber.
   Its call band is limited to heating and cooling problems.
10. **New core pages:** /service-areas/ (Prompt 10 hub) and /how-it-works/ (secondary CTA target).
11. **FAQ page.** CLAUDE.md caps FAQs at 3 to 6 per page, so /faq/ has 6 in the FAQ block (visible and
    in FAQPage JSON-LD) and the rest as ordinary question headings in the page body.
12. **Phone only.** No forms anywhere (check.py fails a form). /contact/ is a phone page; the free guide
    is a one-click PDF download.

## Brand and media
13. **Palette.** Brand blue #0b5ea8 header and first color band (cool), deep heating red #a4232f second
    band (warm), deep Gulf blue #0b3a63/#06243f for the call band and footer, amber #ffb21e call buttons
    with dark text. Clearly different from Dallas (navy and burnt orange). Sections stay white between
    the bands; no pale tinted sections.
14. **Logo.** New SVG "Houston Air & Heating" with a split cool/warm badge (snowflake and flame), text
    converted to outlines so it renders the same everywhere; favicon.svg/.ico and apple-touch-icon made
    from the badge. A dark-text variant is in images/logo-dark.svg.
15. **Photos.** The 13 Houston photos are reused first. Eleven generic photos from the Dallas build (same
    owner; no Dallas landmarks: thermostat, attic air handler, furnace, homeowner on the phone, couple at
    a table, installers, technicians at condensers, two homes) were copied with neutral file names.
    Dallas city photos and the Dallas skyline photo were not copied. Every planned photo is listed in
    docs/image-list.md and pages show an existing photo until it arrives.
16. **The free guide PDF** (free-ac-guide/files/refrigerant-changeover-maurice-johnson.pdf) still says
    "Courtesy of Houston HVAC Pro" on its first page. Per INTAKE.md it was NOT edited. Maurice should
    replace it with a corrected PDF at the same file name when convenient.

## Content rules applied
17. Company names, prices as the line's prices, licenses, insurance, reviews and response times never
    appear. Published third-party cost ranges appear only on the cost guide and only with the source
    named on the page and a note that quotes vary.
18. Each page was researched and written by a separate writer for its own keyword; facts carry sources
    on the page. Duplication is measured with scripts/similarity.py (docs/qa.md).

## Verification
19. **Fact-checking under a restricted network.** The environment blocked direct fetches of nearly all
    source sites, and web search was capped per turn. Writers and the eight independent fact-checkers
    verified claims through search-result summaries of the cited official pages; anything not
    confirmable was softened or removed. Recorded in docs/fact-check.md.
20. **One gas leak number.** CenterPoint lists more than one number; every page that prints one uses
    888-876-5786, the number on CenterPoint's gas leak page.
