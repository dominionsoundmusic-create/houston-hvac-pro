#!/usr/bin/env python3
"""Duplicate-content check: Jaccard similarity on 5-word shingles between built pages.

Text compared: the page's own copy (the content block and its FAQ answers). Shared template parts
that are the same on every page by design (header, footer, call band, breadcrumbs, the how-it-works
strip, the disclosure and license notes, link pills, cards, sources) are removed first.

Also compares every Houston page with every page of the Dallas Air & Heating build (if a checkout is
given) and reports any shared run of 8 or more words, because Dallas page text must never be copied.

Usage:
  python3 scripts/similarity.py [--dist dist] [--dallas ../dallas-hvac-pro/dist] [--only /ac-repair/x.html]
           [--limit 0.15] [--report docs/qa-similarity.md]
Exit code 1 if any city/city or service/service pair is above the limit, or Dallas text is reused.
"""
import argparse
import html
import itertools
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DROP = [r'<ol class="how-strip">.*?</ol>', r'<div class="note">\s*<p><strong>(?:About this line|Verify the license|How this line works|Check the license).*?</div>',
        r'<aside class="sources".*?</aside>', r'<ul class="pill-list">.*?</ul>', r'<div class="cards">.*?</div>\s*</div>\s*</article>\s*</div>',
        r'<div class="note note--orange">.*?</div>', r'<script.*?</script>', r'<style.*?</style>', r'<!--.*?-->',
        r'<figure.*?</figure>', r'<table.*?</table>']


def page_text(raw):
    m = re.search(r'<div class="page-content"[^>]*>(.*)</main>', raw, re.S)
    body = m.group(1) if m else raw
    body = re.sub(r'<section class="band band--navy cta".*?</section>', " ", body, flags=re.S)
    for pat in DROP:
        body = re.sub(pat, " ", body, flags=re.S)
    body = re.sub(r'<div class="cards">.*?(?=<section|</section>)', " ", body, flags=re.S)
    txt = html.unescape(re.sub(r"<[^>]+>", " ", body)).lower()
    txt = re.sub(r"(houston|dallas) air (&|and) heating", "the line", txt)
    txt = re.sub(r"\(\d{3}\) \d{3}-\d{4}", "phone", txt)
    return re.findall(r"[a-z0-9']+", txt)


def shingles(words, n=5):
    return {" ".join(words[i:i + n]) for i in range(len(words) - n + 1)}


def url_of(path, dist):
    rel = path.relative_to(dist).as_posix()
    if rel == "index.html":
        return "/"
    return "/" + rel[:-len("index.html")] if rel.endswith("/index.html") else "/" + rel


def kind(raw):
    m = re.search(r'<body class="type-([a-z]+)', raw)
    return m.group(1) if m else "page"


def load(dist):
    pages = {}
    for f in sorted(dist.rglob("*.html")):
        raw = f.read_text()
        if 'name="robots" content="noindex' in raw:
            continue
        words = page_text(raw)
        pages[url_of(f, dist)] = (kind(raw), words, shingles(words))
    return pages


def jac(a, b):
    return len(a & b) / len(a | b) if a and b else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--dallas", default="")
    ap.add_argument("--only", default="")
    ap.add_argument("--limit", type=float, default=0.15)
    ap.add_argument("--report", default="")
    args = ap.parse_args()
    pages = load(Path(args.dist))
    fails, rows = [], []
    for (u1, (k1, w1, s1)), (u2, (k2, w2, s2)) in itertools.combinations(pages.items(), 2):
        if args.only and args.only not in (u1, u2):
            continue
        j = jac(s1, s2)
        group = k1 if k1 == k2 and k1 in ("area", "service", "guide") else ""
        rows.append((j, u1, u2, k1, k2))
        if group in ("area", "service") and j > args.limit:
            fails.append(f"{group} pair above {args.limit:.0%}: {u1} vs {u2} = {j:.1%}")
    rows.sort(reverse=True)
    by_group = {}
    for j, u1, u2, k1, k2 in rows:
        g = k1 if k1 == k2 else "mixed"
        by_group.setdefault(g, []).append(j)
    print("Houston page pairs (Jaccard, 5-word shingles):")
    for g, js in sorted(by_group.items()):
        print(f"  {g:8s} pairs={len(js):4d} max={max(js):.1%} mean={sum(js)/len(js):.1%} min={min(js):.1%}")
    print("Top 10 pairs:")
    for j, u1, u2, k1, k2 in rows[:10]:
        print(f"  {j:.1%}  {u1}  {u2}")
    dallas_fail = []
    if args.dallas:
        dpages = load(Path(args.dallas))
        worst = []
        for u, (k, w, s) in pages.items():
            if args.only and u != args.only:
                continue
            s8 = shingles(w, 8)
            for du, (dk, dw, ds) in dpages.items():
                j = jac(s, ds)
                shared8 = s8 & shingles(dw, 8)
                worst.append((j, len(shared8), u, du, sorted(shared8)[:3]))
                if shared8:
                    dallas_fail.append(f"shares {len(shared8)} 8-word run(s) with Dallas {du}: {u}: {sorted(shared8)[:3]}")
        worst.sort(reverse=True)
        print(f"Against Dallas ({len(dpages)} pages): max Jaccard {worst[0][0]:.1%} ({worst[0][2]} vs {worst[0][3]}); "
              f"pages sharing an 8-word run: {len({d.split(': ')[1] for d in dallas_fail}) if dallas_fail else 0}")
    for f in fails + dallas_fail:
        print("FAIL", f)
    if args.report:
        out = ["| Group | Pairs | Max | Mean | Min |", "|---|---:|---:|---:|---:|"]
        for g, js in sorted(by_group.items()):
            out.append(f"| {g} | {len(js)} | {max(js):.1%} | {sum(js)/len(js):.1%} | {min(js):.1%} |")
        out += ["", "Top 15 pairs:", "", "| Jaccard | Page | Page |", "|---:|---|---|"]
        out += [f"| {j:.1%} | {u1} | {u2} |" for j, u1, u2, k1, k2 in rows[:15]]
        Path(args.report).write_text("\n".join(out) + "\n")
    return 1 if fails or dallas_fail else 0


if __name__ == "__main__":
    sys.exit(main())
