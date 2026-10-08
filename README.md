# houston-hvac-pro

Source for houstonairandheating.com (Houston Air & Heating, a free heating and AC referral phone line).

- `python3 build.py` builds the static site into `dist/` (Netlify publishes `dist`, see netlify.toml)
  and refreshes docs/image-list.md.
- `python3 scripts/check.py` checks every built page against the rules in CLAUDE.md.
- `python3 scripts/similarity.py --dallas <dallas checkout>/dist` measures duplicate copy.
- `python3 scripts/check_old_urls.py` confirms every URL of the old live site still resolves.
- `node scripts/responsive_check.js` (with dist served on :8765) checks overflow and the hero in a browser.
- `python3 scripts/keyword_plan.py` regenerates docs/keyword-plan.md from the keyword spreadsheet.

Pages: src/pages (Jinja + YAML front matter). Shared data: src/data/site.json. Docs: SERVICES.md,
docs/decisions.md, docs/qa.md, docs/fact-check.md, docs/image-list.md, docs/playbook/.
