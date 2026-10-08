# Prompts 1 to 3: fact brief, architecture, baseline (Oct 8 2026)

## 1 Client fact brief
Source: INTAKE.md (Maurice Johnson's statements, filled Oct 8 2026), CLAUDE.md, the live site on main.

| Item | Value | Status |
|---|---|---|
| Name | Houston Air & Heating, d/b/a of Dominion Digital Group (old name "Houston HVAC Pro" retired) | Confirmed |
| Category | Free phone line that transfers heating and cooling callers to independent local HVAC companies | Confirmed |
| Services | 8 service pages, 8 guides plus the free book page (from the Oct 8 keyword data) | Confirmed |
| Areas | Houston plus the 18 existing city pages | Confirmed |
| Address / email | Not displayed / none | Confirmed |
| Phone | (832) 662-4107, tel:+18326624107, only in src/data/site.json | Confirmed |
| Hours | Answered 24/7 by an automated assistant | Confirmed |
| CTA | Call; secondary links to real pages; no forms (contact form and guide form retired) | Confirmed |
| Brand | New palette (brand blue, heating red, amber), new SVG logo and favicon | Decided (docs/decisions.md) |
| Owner name | Not shown (Maurice Johnson appears only as the free book's author) | Confirmed |
| Licenses, insurance, reviews, team, awards | None; never claimed for the line or its partner companies | Confirmed rule |
| Analytics, social, GBP | None yet; slots hidden | Missing, deferrable |
| Domain | https://houstonairandheating.com | Confirmed |

Contradictions: none. Launch blockers: none in content; going live needs Netlify to build from this
branch (not done: no deploys allowed). Deferred: 40 planned photos (pages show existing photos).

## 2 Architecture
Not an SSR framework: a static pre-rendered site (Python + Jinja2 build.py, YAML front matter, central
src/data/site.json), the same system as Dallas Air & Heating. Every title, canonical, heading, body
and JSON-LD block is in the raw HTML; no client rendering. Commands: `python3 build.py`,
`python3 scripts/check.py`. PASS. The playbook's AI Studio, TanStack and form-embed steps do not apply
and were mapped to this build system.

## 3 Baseline and route matrix
The old live site (repo root on main) was moved to docs/old-site/ as the reference. Pre-existing
state: hand-written HTML with no build or checks; old name everywhere; a contact form and a guide
sign-up form; claims of "licensed" partner companies that INTAKE forbids. All 71 old URLs (sitemap,
file tree and retired blog redirects) are kept or redirected (docs/qa.md).

| Route | Type | Source | Nav | Sitemap | Indexable | Status |
|---|---|---|---|---|---|---|
| / | home | src/pages/index.html | logo | yes | yes | rebuilt |
| /services/, /service-areas/, /how-it-works/, /about/, /faq/, /contact/ | core | src/pages/*.html | header | yes | yes | rebuilt; service-areas and how-it-works new |
| 8 service URLs (/ac-repair/ ... /commercial-hvac/) | service | src/pages/<slug>.html | Services menu, footer | yes | yes | 4 rebuilt, 4 new |
| 8 guides + /free-ac-guide/ | guide | src/pages/*.html (.html URLs via `url:`) | Guides menu, footer | yes | yes | 5 rebuilt, 4 new |
| /ac-repair/<city>-tx.html x 18 | area | src/pages/ac-repair/<slug>.html | Service Areas menu, footer | yes | yes | rebuilt |
| /privacy-policy.html, /terms.html | legal | src/pages | footer | yes | yes | rewritten |
| /404.html | error | src/pages/404.html | none | no | noindex | new |
| /contact/thanks/, /free-ac-guide/thanks/ | 301 | src/static/_redirects | none | no | n/a | retired forms |
