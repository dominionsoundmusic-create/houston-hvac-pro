# Prompts 4 to 20 (Oct 8 2026)

**4 Business data.** Every shared value lives in src/data/site.json: name, d/b/a, phone in display and
tel formats (the number appears in no page source), 24/7 hours, CTA labels, origin, disclosures,
empty social and analytics slots, and the service, guide and area lists with their URLs. The old name
"Houston HVAC Pro" appears nowhere in the built HTML (grep_check.py); it remains only on the cover of
the unedited PDF (docs/decisions.md item 16).
**5 Brand.** Tokens in site.css: brand blue #0b5ea8 header and first band, heating red #a4232f second
band, deep blue #0b3a63/#06243f call band and footer, amber #ffb21e buttons with dark text. New SVG
logo (text as outlines), favicon.svg, favicon.ico, apple-touch-icon. Contrast: white on all bands,
dark text on amber, no white boxes on white (panels and cards carry colored edges).
**6 Navigation.** Services, Service Areas, Guides, How It Works, About, FAQ, Contact; EN/ES toggle and
call button top right; keyboard-operable submenus; footer with disclosure, quote bar on every page.
**7 Homepage.** Full-width hero (hvac-hero.jpg), H1 "HVAC in Houston: One Free Phone Line for Heating
and Air Conditioning Help", two CTAs. No video exists, so the hero is a preloaded photo.
**8 Services overview.** /services/ with a problem-to-page table and every service and guide.
**9 Services and guides (17 pages).** Each researched and written for its own keyword by a separate
writer, then validated with check.py and similarity.py.
**10 Service areas overview.** /service-areas/ grouped by side of town, with a sourced one-line
summary of each town and the coverage model (no offices).
**11 Area pages (18).** Each built around that town's verified facts, with a "Why [Town] homeowners
call the line" section.
**12 About, FAQ, how it works, privacy, terms.** About names no owner; FAQ keeps 6 FAQPage questions
plus 17 more as headings; legal pages rewritten for a phone-only referral line.
**13 Contact and forms.** Phone only. No forms anywhere (check.py fails any form). The free book is a
one-click PDF download.
**14 Reviews and social.** None exist; none added; icon slots hidden until URLs are set.
**15 Media.** 24 existing photos used (13 Houston, 11 generic from the Dallas build, renamed). 40
planned photos in docs/image-list.md with Artistly prompts; each shows an existing fallback photo.
All photos get WebP srcsets; heroes are preloaded and eager, body images lazy.
**16 SEO.** check.py: 45 pages, 0 errors, 0 warnings (unique titles and descriptions, canonicals on
the production origin, OG and Twitter tags with absolute images, one H1, one JSON-LD graph per page
with Organization, WebPage, BreadcrumbList, Service, Article and FAQPage as relevant; sitemap.xml lists
44 indexable URLs; 404 is noindex and not in the sitemap; robots.txt points to the sitemap).
**17 Remnant sweep.** Old name, old phone formats, Dallas, DFW, Oncor, other metros, placeholders,
forms: none found (grep_check.py, check.py).
**Independent fact-check.** Eight separate agents re-checked 546 claims (docs/fact-check.md): 64
corrected, 53 softened, 20 removed. Limitation: source pages could not be opened directly because of
the environment's network policy; verification used search-result summaries.
**18 Responsive.** Chromium via Playwright, every page at 1440/1024/768/390 and samples at 1920/2560:
no horizontal overflow, hero edge to edge and on the left rail, call button above the fold.
**19 Functional.** All internal links and _redirects targets resolve; every phone link is
tel:+18326624107; FAQ accordions are native details elements; no JS errors. 71 old URLs resolve.
Not verified: live 404 status, translation on the real domain, phone routing.
**20 Handoff.** Code and content are on `build`, pushed once; NOT merged and NOT deployed. To go live,
Maurice merges or points Netlify at the branch (publish "dist", already in netlify.toml). Remaining:
40 photos to generate; a corrected PDF cover; optionally re-run the fact-check with full web access.
