CLIENT WEBSITE QUESTIONNAIRE: HOUSTON AIR & HEATING (houstonairandheating.com)

Filled in Oct 8 2026 from what Maurice Johnson has stated. This is the factual source of truth for
Playbook 2.0. Anything marked UNKNOWN stays off the site. Never fill a gap by guessing.

1. BUSINESS BASICS
OFFICIAL BUSINESS NAME: Houston Air & Heating (a d/b/a of Dominion Digital Group)
  The old site called itself "Houston HVAC Pro". The name now matches the domain, the same way
  Dallas Air & Heating matches dallasairandheating.com. Replace the old name everywhere.
SHORT BUSINESS NAME: Houston Air & Heating
PRIMARY CITY: Houston
STATE: Texas
FULL BUSINESS ADDRESS: DO NOT DISPLAY
PHONE: (832) 662-4107 / tel:+18326624107. Lives in ONE place only (src/data/site.json); never
  hard-coded in a page. The same line also takes Houston roofing and pressure washing calls; this
  site only talks about heating and cooling.
PUBLIC EMAIL: UNKNOWN (do not display an email)
YEAR ESTABLISHED: do not display
OWNER: Owned by Dominion Digital Group. Do not name an owner on the site.
HOURS: The phone line is answered 24 hours a day, 7 days a week by an automated assistant.

WHAT THE BUSINESS ACTUALLY IS (read this twice):
Houston Air & Heating is a FREE PHONE LINE and website, NOT an HVAC company. It has no technicians,
trucks, equipment, license or certification, and never repairs, installs, services, quotes or
schedules anything itself. When someone calls:
- An automated assistant answers, any hour, and asks what the caller needs.
- For heating and cooling it asks briefly what is going on, then transfers the call to an
  independent, locally owned, licensed HVAC company serving the Houston area. That company hears a
  short summary before it picks up.
- If that company cannot answer, the caller's name, callback number, area and problem are taken
  and passed along for a call back.
The company inspects, quotes, does the work and is paid directly by the customer. The line never
charges the customer. The companies may pay the line a referral fee (always disclose this).
The site must NOT claim partner companies are insured, certified or rated. It tells callers to ask
for the company's Texas ACR license number and check it on the TDLR license search.
Never name a partner company. Never say "our technicians", "our trucks", "we repair", "we install",
"we are licensed/insured" or anything implying the line does the work.

REFERRAL DISCLOSURE (footer of every page, adapt lightly but keep the meaning):
"Houston Air & Heating is a free phone line, not an HVAC contractor. It answers your call and
connects you with an independent local heating and air conditioning company, which inspects,
quotes and does the work, and which you pay directly. Companies may pay a referral fee."

2. SERVICES
PRIMARY CATEGORY: Heating and air conditioning referral line for the Houston area.
ALL SERVICES: choose from the keyword research (rules in CLAUDE.md). Heating AND cooling.
SERVICES NOT OFFERED: plumbing, electrical work, duct cleaning sold as a separate trade, roofing,
  pressure washing, appliance repair. (The old site has /water-heater-repair.html: keep the URL
  working, but decide in docs/decisions.md whether it stays as an honest guide or 301s.)

3. SERVICE AREA
PRIMARY AREA: Houston, Texas and its suburbs (Harris, Fort Bend, Montgomery, Brazoria, Galveston
  counties). Maurice used to live in Missouri City and Katy and knows these suburbs.
EXISTING CITY PAGES (keep every URL): Baytown, Conroe, Cypress, Fresno, Friendswood, Fulshear,
  Humble, Katy, Kingwood, League City, Missouri City, Pasadena, Pearland, Richmond, Spring,
  Sugar Land, The Woodlands, Tomball.
LOCATIONS NOT TO CLAIM: anywhere outside greater Houston.

4. BRANDING
LOOK: heating and air. Clearly its own palette, not a copy of Dallas Air & Heating's navy and
  orange. A strong cool blue plus a warm heating accent works; the header must be a real color.
BACKGROUND: mostly WHITE sections with occasional bold color bands. Never pale off-white tints.
LOGO: design an SVG logo for "Houston Air & Heating" and a favicon.
STYLE: bright, clearly visible photos. Full-width hero edge to edge with a dark fade behind the
  headline. Body text in a centered reading column (text left-aligned). No white on white. No
  eyebrow labels. No em dashes or en dashes in visible copy.
TOP OF EVERY PAGE: "John 3:16" at the left and the quote, EXACTLY: "I believe the unbelievable, I
  receive the impossible, because it's doable." credited "— Jesse Duplantis". (This attribution
  dash is the one dash allowed.)
FOOTER OF EVERY PAGE: "© 2026 Dominion Digital Group. All rights reserved." and the linked credit
  "Designed by Dominion Web Design Pro" to https://dominionwebdesignpro.com.
LANGUAGE: EN / ES toggle in the header.

5. CALLS TO ACTION
MAIN CTA: Call the phone number. THE SITE IS PHONE ONLY. Retire the contact form and the guide
  sign-up form (the same choice made on Dallas Air & Heating): /contact/ becomes a phone page and
  /contact/thanks/ 301s to /contact/.
FREE AC GUIDE: keep /free-ac-guide/ as a one-click download of the PDF already in
  free-ac-guide/files/ (no form). /free-ac-guide/thanks/ 301s to /free-ac-guide/. If the PDF
  mentions "Houston HVAC Pro", note it in docs/decisions.md; do not edit the PDF.
SECONDARY CTA: a real page (How it works, a guide). Never a form.

6. SOCIAL PROFILES
None. Icon slots are data-driven and stay hidden until URLs are added.

7. TRUST
DIFFERENTIATORS: free to call, answered 24/7, one number for heating and cooling across greater
  Houston, live transfer to a local licensed company, and the site teaches callers how to check a
  Texas ACR license on TDLR.
LICENSES / GUARANTEES / REVIEWS / TEAM: none. Do not invent any.

8. WORDS TO AVOID
"free estimate(s)", "same-day", "guarantee", "best price", "cheapest", "top-rated",
"licensed and insured", "years of experience", "#1". No DIY refrigerant, electrical or gas work.

9. WEBSITE
DOMAIN: https://houstonairandheating.com (live on Netlify, production branch main)
PHOTOS: 13 in images/ (hvac-01 to 06 hero and card, hvac-hero.jpg). Reuse first; list every other
  image in docs/image-list.md with File name, Size and an Artistly prompt.
NETLIFY: do not deploy, do not change settings. Work stays on the `build` branch.
