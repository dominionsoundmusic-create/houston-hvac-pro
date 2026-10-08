# Houston Air & Heating (houstonairandheating.com): PLAYBOOK 2.0 REBUILD. INSTRUCTIONS FOR CLAUDE CODE

You are rebuilding a LIVE static lead-generation website for Maurice Johnson by running
Dominic & Dalton's Website Builder Prompt Playbook 2.0 (PLAYBOOK.md), Prompts 1 to 20, in full.
The site already ranks for some terms, so the rebuild must keep every URL Google knows.

## RUN STRAIGHT THROUGH. DO NOT STOP.
Maurice is not watching this session and cannot approve anything. Do NOT pause at the end of each
playbook phase, do NOT ask "continue?", do NOT wait for input. Make reasonable decisions yourself,
write them down in docs/decisions.md, and keep going until Prompt 20 is finished and every check
below passes. The only reason to stop early is if something would require paying money, deploying,
or changing a repository other than this one.

## Source files (read all of them first)
- INTAKE.md: the facts. It wins over anything else. UNKNOWN means leave it off the site.
- PLAYBOOK.md: the playbook (Operating Rules, then Prompts 1 to 20). It was written for GHL AI
  Studio; apply its rules and its 20 steps to this static build system.
- keywords/Houston-AC-Heating-Keywords.xlsx: Ubersuggest, United States, pulled Oct 8 2026. 577
  unique keywords, a tab per seed plus an ALL tab, each row typed Suggestion or Question. Every
  Houston-area keyword must be assigned to a page as a target or supporting keyword, or listed in
  docs/keyword-plan.md as deliberately unused with a one-line reason. "Near me" terms are national
  volume: supporting keywords only, never proof of Houston demand. Off-topic rows (for example
  "outlets in cypress tx", "ac plastics houston", "is the woodlands tx safe") go in the unused list.
- The current live site (this repo's main branch, the root-level .html files). Read every page
  before writing. Keep useful verified facts, but do NOT copy its paragraphs: every page is written
  fresh. Its photos in images/ are reused first.

## Copy the build system from Dallas Air & Heating (NOT its words)
The repository dominionsoundmusic-create/dallas-hvac-pro (branch main, which is the same as its
`build` branch) holds the same kind of site: an HVAC referral line rebuilt with Playbook 2.0 on
Oct 3 2026 and live on dallasairandheating.com. Clone it and copy its BUILD SYSTEM: build.py,
scripts/check.py, scripts/similarity.py if present, src/templates/, the CSS/JS, the macros (img,
faqs, sources, disclosure), the site.json structure, netlify.toml (publish = "dist") and the
docs/playbook/ document set as a pattern. Adapt every Dallas value to Houston.
NEVER copy page text, paragraphs, FAQs or sentence runs from Dallas. No Dallas, Fort Worth or DFW
place names, no Oncor, no North Texas facts. Research Houston equivalents instead (CenterPoint
Energy, City of Houston permits and code, Harris and Fort Bend counties, Gulf Coast humidity and
heat, hurricane season and power outages, Houston freezes such as February 2021).
The build system already does the speed fix (WebP 480/800/1200/1600/1920 srcset, preloaded hero
with fetchpriority high, self-hosted woff2 font). Keep it exactly.

## URLs: keep every live URL (this is a rebuild of an indexed site)
Every URL in the current sitemap.xml and every page file on main must still resolve on the new
site, either as a rebuilt page at the SAME path or a 301 to the closest new page (record each in
docs/decisions.md). That includes /ac-repair/<city>-tx.html for all 18 cities, /ac-not-cooling.html,
/ac-leaking-water.html, /ac-repair-cost.html, /water-heater-repair.html, /privacy-policy.html,
/terms.html and the folder pages. Keep the existing _redirects rules that still make sense and
copy _redirects into dist/. REMOVE the old rules that send /furnace-repair/ and
/air-conditioning-repair/ to /ac-repair/ if you build real pages at those paths (the new keyword
data supports both: "air conditioning repair in houston" 5,400/mo at SEO difficulty 17).
/contact/thanks/ and /free-ac-guide/thanks/ become 301s (see forms below).

## Pages to build (decide the exact list from the keywords, then follow it)
- Home, services overview, service areas overview, how it works, about, FAQ, contact, privacy,
  terms, 404, and the free AC guide page.
- Service pages: one per real service with Houston demand. Cooling AND heating: it is October and
  heating searches are climbing, so furnace repair, heating repair and heat pump work get real
  pages if the data supports them. Also AC repair, air conditioning repair, emergency AC repair,
  AC installation/replacement, HVAC tune-up, plus any other service the data shows.
- Guide pages for the strongest question keywords (cost, not cooling, leaking water, tune-up worth
  it, what a tune-up includes, repair or replace), each researched and sourced.
- City pages: one per Houston-area city/suburb with at least one keyword of 30+ searches a month
  in the data, AND every one of the 18 existing city URLs (keep them even if under 30).
- Write SERVICES.md (every page, URL, target keyword with volume/SEO difficulty) and
  docs/keyword-plan.md before writing pages.

## Hard rules for every page
1. Never "our technicians", "our trucks", "we repair", "we install", "we are licensed/insured" or
   anything implying the line does HVAC work.
2. Never invent licenses, certifications, insurance, reviews, ratings, prices, years in business,
   team members, job counts, guarantees, awards or statistics. Tell readers to ASK for the
   company's Texas ACR license number and to verify it on the TDLR license search
   (https://www.tdlr.texas.gov/LicenseSearch/). Research and state accurately what Texas requires.
3. Never name a specific HVAC company.
4. Only greater-Houston places. No other Texas metros.
5. No em dashes or en dashes in visible copy. No eyebrow labels. American spelling.
6. No DIY refrigerant, electrical, gas or furnace-burner instructions. Safe homeowner checks only
   (thermostat setting and batteries, filter, breaker reset once, clear the outdoor unit, a gas
   smell means leave the house and call the gas utility or 911, carbon monoxide alarm means get out
   and call 911).
7. No prices presented as the line's prices. Cost guides cite published, sourced ranges and say
   real quotes vary.
8. Every page except privacy, terms and 404 has 3 to 6 FAQs written the way people ask (use the
   Question rows), rendered visibly AND as FAQPage JSON-LD.
9. Every page has a full-width hero image plus at least two in-body images, each with filename,
   alt, width, height and loading="lazy" (hero eager). Reuse this repo's images/ first.
10. Facts must be real and current. Research each page on the web and cite every source in the
    page's sources list. If you cannot verify a fact, leave it out.
11. Each page is written for its own keyword. Never reuse paragraphs between pages with names
    swapped. Measure: Jaccard similarity on 5-word shingles between every pair of pages; any pair
    of city pages or service pages above 15% gets rewritten. Record the numbers in docs/qa.md.
12. The referral disclosure appears on every page (wording in INTAKE.md).
13. Banned phrases: "your trusted partner", "one-stop solution", "look no further", "unmatched
    excellence", "we've got you covered", plus the WORDS TO AVOID in INTAKE.md.
14. Mark every page with the HTML comment `dwdp:handwritten 2026-10-08` in the first 4KB.

## Design (Maurice's standing rules, check each one)
- Header/menu bar in a real brand color, never dull gray. EN/ES language toggle in the header on
  every page (Google Translate widget, top right, lazy-loaded, as the Dallas build does).
- Hero stretches edge to edge on every page: full-strength photo, dark left-to-right scrim behind
  the headline, logo/headline/buttons aligned to a left rail (`--rail: clamp(22px, 5.5vw, 140px)`)
  at 1440, 1920 and 2560 wide, not boxed in a narrow centered strip. Hero stays above the fold
  (max-height about 700px) with the call button visible.
- Mostly WHITE sections broken by occasional bold color bands (hero, white, brand-blue band,
  white, a second band in another color that suits the site). Never pale off-white tints. Never
  every section tinted.
- Body text in a centered reading column with the text itself left-aligned.
- No white text or white boxes on white. Every card, box and button has clear contrast.
- Logo: SVG matching the name Houston Air & Heating, plus favicon.

## Before you finish (all must pass)
- `python3 build.py` then `python3 scripts/check.py`: 0 errors.
- Every old URL (list it from main's sitemap.xml and file tree) resolves on the built site or has a
  301 in dist/_redirects. Write a script for this and record the result in docs/qa.md.
- Grep the built site for: em/en dashes in visible text, "we repair", "our technicians",
  "licensed and insured", "free estimate", "same-day", "Houston HVAC Pro", "Dallas", "Fort Worth",
  "Oncor", "(469)". Fix every hit.
- No horizontal overflow at 1440, 1024, 768 and 390 px wide.
- Independent fact-check: start a separate sub-agent that did not write the pages, have it check
  every factual claim and source on every page, and fix what it finds. Record it in
  docs/fact-check.md. Never say "fact-checked" unless this was actually run.
- docs/image-list.md lists every image still needed: File name, Size, then an Artistly prompt
  (bright, clearly visible, Houston-area homes, no text, no logos, no recognizable faces, "wide
  cinematic landscape shot, subject positioned on right third of frame, well lit"). Missing images
  must never show as broken: pages use an existing photo until the new one arrives.

## Git
- Work on the branch `build`. Commit as you go with clear messages.
- Push to origin `build` ONCE, at the very end. Every push can start a paid Netlify build.
- Do NOT merge to main, do NOT deploy, do NOT touch Netlify settings, do NOT pay for anything.

## Final report (Maurice reads on his phone, 5 lines max)
Pages built (count by type), checks passed, duplication range, fact-check result, and how many
images still need Artistly.
