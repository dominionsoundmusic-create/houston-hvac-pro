#!/usr/bin/env python3
"""Every URL the live site had must still work on the rebuilt site.

The old site (main branch, saved in docs/old-site/) is read for its URLs: every <loc> in its
sitemap.xml, every file in its tree (pages, the guide PDF, images, icons) and every URL its
_redirects file already redirected. Each URL must either be
served by a file in dist/ or be caught by a 301 rule in dist/_redirects whose target exists in dist/.

Usage: python3 scripts/check_old_urls.py [--dist dist] [--report docs/qa-old-urls.md]
Exit code 1 if any old URL would 404.
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD = ROOT / "docs" / "old-site"
# Files of the old site that were not public pages or are replaced on purpose (same path, new file).
SKIP = {"/_redirects"}
OLD_ROOT_FILES = {"/favicon.ico", "/favicon.svg", "/apple-touch-icon.png", "/images/logo.svg"}


def old_urls():
    urls = set(re.findall(r"<loc>https://houstonairandheating\.com(/[^<]*)</loc>", (OLD / "sitemap.xml").read_text()))
    for f in OLD.rglob("*"):
        if f.is_file():
            rel = "/" + f.relative_to(OLD).as_posix()
            if rel == "/logo.svg":
                rel = "/images/logo.svg"
            elif rel in ("/favicon.ico", "/favicon.svg", "/apple-touch-icon.png"):
                pass
            if rel.endswith("/index.html"):
                rel = rel[: -len("index.html")]
            if rel == "/index.html":
                rel = "/"
            urls.add(rel)
    # URLs the old site already redirected (retired blog posts etc.) must keep redirecting.
    for line in (OLD / "_redirects").read_text().splitlines():
        parts = line.split()
        if parts and not parts[0].startswith("#") and "*" not in parts[0]:
            urls.add(parts[0])
    for img in ["hvac-01-card.jpg", "hvac-01-hero.jpg", "hvac-02-card.jpg", "hvac-02-hero.jpg", "hvac-03-card.jpg",
                "hvac-03-hero.jpg", "hvac-04-card.jpg", "hvac-04-hero.jpg", "hvac-05-card.jpg", "hvac-05-hero.jpg",
                "hvac-06-card.jpg", "hvac-06-hero.jpg", "hvac-hero.jpg"]:
        urls.add("/images/" + img)
    return sorted(u for u in urls | OLD_ROOT_FILES if u not in SKIP)


def served(url, dist):
    p = dist / url.lstrip("/")
    if url.endswith("/"):
        return (p / "index.html").exists()
    return p.exists()


def rules(dist):
    out = []
    for line in (dist / "_redirects").read_text().splitlines():
        parts = line.split()
        if parts and not parts[0].startswith("#"):
            out.append((parts[0], parts[1], parts[2] if len(parts) > 2 else "301"))
    return out


def redirected(url, rs):
    for src, dst, code in rs:
        if src == url or ("*" in src and url.startswith(src.split("*")[0]) and url != src.split("*")[0]):
            return src, dst, code
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dist", default=str(ROOT / "dist"))
    ap.add_argument("--report", default="")
    args = ap.parse_args()
    dist = Path(args.dist)
    rs = rules(dist)
    rows, bad = [], 0
    for u in old_urls():
        if served(u, dist):
            # a served file wins over any rule without "!" on Netlify
            rows.append((u, "200", "served by a rebuilt page or file at the same path"))
            continue
        r = redirected(u, rs)
        if r and served(r[1], dist):
            rows.append((u, r[2], f"redirect to {r[1]} (rule {r[0]})"))
        else:
            bad += 1
            rows.append((u, "404", "NOT FOUND"))
    for u, code, how in rows:
        print(f"{code}  {u}  {how}")
    print(f"\n{len(rows)} old URLs checked, {bad} would 404")
    if args.report:
        lines = ["| Old URL | Result | How |", "|---|---|---|"] + [f"| {u} | {c} | {h} |" for u, c, h in rows]
        lines.append(f"\n{len(rows)} old URLs checked, {bad} would 404.")
        Path(args.report).write_text("\n".join(lines) + "\n")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
