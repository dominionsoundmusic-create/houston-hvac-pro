# QA record (Oct 8 2026, final run on the `build` branch)

All commands run from the repo root against the production build in dist/.

| Check | Command | Result |
|---|---|---|
| Build | `python3 build.py` | 45 pages built; 40 planned photos listed in docs/image-list.md (each page shows an existing photo meanwhile) |
| Rules and SEO | `python3 scripts/check.py` | 45 pages checked, **0 errors, 0 warnings** (banned phrases, dashes, other metros, forms, eyebrow labels, quote bar, footer, disclosure, handwritten marker, one H1, unique titles/descriptions, canonical, OG tags, one valid JSON-LD block, 3 to 6 FAQs visible and in FAQPage JSON-LD, hero plus 2 in-body images with lazy loading, alt/width/height, internal links, sitemap, _redirects targets) |
| Old URLs | `python3 scripts/check_old_urls.py` | **71 old URLs checked, 0 would 404** (table below) |
| CLAUDE.md grep | `python3 scripts/grep_check.py` | **0 hits** for em/en dashes, "we repair", "our technicians", "licensed and insured", "free estimate", "same-day", "Houston HVAC Pro", "Dallas", "Fort Worth", "Oncor", "(469)" in visible text, titles, meta and alt text |
| Duplication | `python3 scripts/similarity.py --dallas ../dallas-hvac-pro/dist` | City pairs max **1.7%**, service pairs max **0.6%** (limit 15%); no Houston page shares an 8-word run with any Dallas page (table below) |
| Browser | `node scripts/responsive_check.js` (dist served on :8765, Chromium) | 186 page loads: every page at 1440, 1024, 768 and 390 px plus samples at 1920 and 2560: **0 problems** (no horizontal overflow, no JS errors, no broken images, hero edge to edge, hero at most 700px tall with the call button above the fold, headline on the left rail) |
| Fact-check | 8 independent sub-agents | 546 claims checked; 64 corrected, 53 softened, 20 removed (docs/fact-check.md) |

Not verified here (needs the live site): Netlify's 404 status and redirect behavior in production, the
Google Translate ES toggle loading on the real domain, and the phone line's routing.

## Duplication (Jaccard on 5-word shingles, page copy and FAQ answers; shared template parts excluded)

| Group | Pairs | Max | Mean | Min |
|---|---:|---:|---:|---:|
| area | 153 | 1.7% | 0.4% | 0.0% |
| guide | 36 | 0.5% | 0.1% | 0.0% |
| legal | 1 | 0.7% | 0.7% | 0.7% |
| mixed | 722 | 1.4% | 0.1% | 0.0% |
| page | 6 | 1.0% | 0.2% | 0.0% |
| service | 28 | 0.6% | 0.2% | 0.0% |

Top 15 pairs:

| Jaccard | Page | Page |
|---:|---|---|
| 1.7% | /ac-repair/richmond-tx.html | /ac-repair/sugar-land-tx.html |
| 1.7% | /ac-repair/missouri-city-tx.html | /ac-repair/richmond-tx.html |
| 1.5% | /ac-repair/cypress-tx.html | /ac-repair/kingwood-tx.html |
| 1.4% | /ac-repair/katy-tx.html | /ac-repair/sugar-land-tx.html |
| 1.4% | /about/ | / |
| 1.4% | /ac-repair/katy-tx.html | /ac-repair/richmond-tx.html |
| 1.3% | /ac-repair/fresno-tx.html | /ac-repair/pearland-tx.html |
| 1.3% | /ac-repair/katy-tx.html | /ac-repair/kingwood-tx.html |
| 1.2% | /contact/ | /how-it-works/ |
| 1.2% | /ac-repair/humble-tx.html | /ac-repair/kingwood-tx.html |
| 1.2% | /contact/ | /faq/ |
| 1.2% | /ac-repair/katy-tx.html | /ac-repair/missouri-city-tx.html |
| 1.1% | /ac-repair/missouri-city-tx.html | /ac-repair/sugar-land-tx.html |
| 1.0% | /ac-repair/league-city-tx.html | /ac-repair/pasadena-tx.html |
| 1.0% | /commercial-hvac/ | /hvac-company/ |

Against Dallas Air & Heating (32 indexable pages): max Jaccard 2.4% (terms vs terms), 0 shared 8-word runs. Only runs made of proper names (TDLR, Dominion Digital Group, statute names) are exempt.

## Old URLs

| Old URL | Result | How |
|---|---|---|
| / | 200 | served by a rebuilt page or file at the same path |
| /about/ | 200 | served by a rebuilt page or file at the same path |
| /ac-installation/ | 200 | served by a rebuilt page or file at the same path |
| /ac-leaking-water.html | 200 | served by a rebuilt page or file at the same path |
| /ac-not-cooling.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair-cost.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/ | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/baytown-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/conroe-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/cypress-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/fresno-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/friendswood-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/fulshear-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/humble-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/katy-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/kingwood-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/league-city-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/missouri-city-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/pasadena-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/pearland-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/richmond-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/spring-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/sugar-land-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/the-woodlands-tx.html | 200 | served by a rebuilt page or file at the same path |
| /ac-repair/tomball-tx.html | 200 | served by a rebuilt page or file at the same path |
| /air-conditioning-repair/ | 200 | served by a rebuilt page or file at the same path |
| /apple-touch-icon.png | 200 | served by a rebuilt page or file at the same path |
| /blog | 301 | redirect to / (rule /blog) |
| /blog/emergency-ac-repair-what-to-do-while-you-wait-1786023856712 | 301 | redirect to /emergency-ac-repair/ (rule /blog/emergency-ac-repair-what-to-do-while-you-wait-1786023856712) |
| /blog/emergency-ac-repair-what-to-do-while-you-wait-1786023856712.html | 301 | redirect to /emergency-ac-repair/ (rule /blog/emergency-ac-repair-what-to-do-while-you-wait-1786023856712.html) |
| /blog/how-annual-hvac-maintenance-cuts-your-power-bill-1785851396017 | 301 | redirect to /is-hvac-tune-up-worth-it/ (rule /blog/how-annual-hvac-maintenance-cuts-your-power-bill-1785851396017) |
| /blog/how-annual-hvac-maintenance-cuts-your-power-bill-1785851396017.html | 301 | redirect to /is-hvac-tune-up-worth-it/ (rule /blog/how-annual-hvac-maintenance-cuts-your-power-bill-1785851396017.html) |
| /blog/how-much-does-ac-replacement-cost-in-houston-1785707449538 | 301 | redirect to /ac-repair-cost.html (rule /blog/how-much-does-ac-replacement-cost-in-houston-1785707449538) |
| /blog/how-much-does-ac-replacement-cost-in-houston-1785707449538.html | 301 | redirect to /ac-repair-cost.html (rule /blog/how-much-does-ac-replacement-cost-in-houston-1785707449538.html) |
| /blog/how-to-size-an-air-conditioner-for-your-home-1785937526639 | 301 | redirect to /ac-installation/ (rule /blog/how-to-size-an-air-conditioner-for-your-home-1785937526639) |
| /blog/how-to-size-an-air-conditioner-for-your-home-1785937526639.html | 301 | redirect to /ac-installation/ (rule /blog/how-to-size-an-air-conditioner-for-your-home-1785937526639.html) |
| /blog/signs-your-air-conditioner-needs-repair-not-replacement-1786970395715 | 301 | redirect to /repair-or-replace-ac/ (rule /blog/signs-your-air-conditioner-needs-repair-not-replacement-1786970395715) |
| /blog/signs-your-air-conditioner-needs-repair-not-replacement-1786970395715.html | 301 | redirect to /repair-or-replace-ac/ (rule /blog/signs-your-air-conditioner-needs-repair-not-replacement-1786970395715.html) |
| /blog/why-ac-units-fail-in-houston-summer-heat-1786278660422 | 301 | redirect to /ac-not-cooling.html (rule /blog/why-ac-units-fail-in-houston-summer-heat-1786278660422) |
| /blog/why-ac-units-fail-in-houston-summer-heat-1786278660422.html | 301 | redirect to /ac-not-cooling.html (rule /blog/why-ac-units-fail-in-houston-summer-heat-1786278660422.html) |
| /contact/ | 200 | served by a rebuilt page or file at the same path |
| /contact/thanks/ | 301 | redirect to /contact/ (rule /contact/thanks/) |
| /emergency-ac-repair/ | 200 | served by a rebuilt page or file at the same path |
| /faq/ | 200 | served by a rebuilt page or file at the same path |
| /favicon.ico | 200 | served by a rebuilt page or file at the same path |
| /favicon.svg | 200 | served by a rebuilt page or file at the same path |
| /free-ac-guide/ | 200 | served by a rebuilt page or file at the same path |
| /free-ac-guide/files/refrigerant-changeover-maurice-johnson.pdf | 200 | served by a rebuilt page or file at the same path |
| /free-ac-guide/thanks/ | 301 | redirect to /free-ac-guide/ (rule /free-ac-guide/thanks/) |
| /furnace-repair/ | 200 | served by a rebuilt page or file at the same path |
| /hvac-tune-up/ | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-01-card.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-01-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-02-card.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-02-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-03-card.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-03-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-04-card.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-04-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-05-card.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-05-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-06-card.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-06-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/hvac-hero.jpg | 200 | served by a rebuilt page or file at the same path |
| /images/logo.svg | 200 | served by a rebuilt page or file at the same path |
| /privacy-policy.html | 200 | served by a rebuilt page or file at the same path |
| /robots.txt | 200 | served by a rebuilt page or file at the same path |
| /services/ | 200 | served by a rebuilt page or file at the same path |
| /sitemap.xml | 200 | served by a rebuilt page or file at the same path |
| /terms.html | 200 | served by a rebuilt page or file at the same path |
| /water-heater-repair.html | 200 | served by a rebuilt page or file at the same path |

71 old URLs checked, 0 would 404.
