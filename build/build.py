"""Generate the 4GNet.com static site into the repository root.
Usage:  python3 build/build.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from layout import DOMAIN, LOGO
import pages_core, pages_internet, pages_learn, pages_community, pages_legal  # noqa: F401 (registers pages)
from pages_core import PAGES

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def w(rel, content):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)


for fn, html in PAGES.items():
    w(fn, html)

urls = [u for u in PAGES if u != "404.html"]
w("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
  "".join(f"  <url><loc>{DOMAIN}/{'' if u == 'index.html' else u}</loc><lastmod>2026-09-29</lastmod><priority>{'1.0' if u in ('index.html','get-matched.html') else '0.8'}</priority></url>\n" for u in urls) + "</urlset>\n")
w("robots.txt", f"User-agent: *\nAllow: /\nDisallow: /build/\nDisallow: /docs/\n\nSitemap: {DOMAIN}/sitemap.xml\n")
w("ads.txt", "# Replace pub-0000000000000000 with your AdSense publisher ID once approved.\n# google.com, pub-0000000000000000, DIRECT, f08c47fec0942fa0\n")
w(".nojekyll", "")
w("manifest.webmanifest", '{"name":"4GNet — Wireless Internet Hub","short_name":"4GNet","start_url":"index.html","display":"standalone","background_color":"#0b1020","theme_color":"#0b1020","icons":[{"src":"assets/img/logo.svg","sizes":"any","type":"image/svg+xml"}]}\n')
w("assets/img/logo.svg", LOGO.replace('aria-hidden="true"', 'xmlns="http://www.w3.org/2000/svg"'))
w("assets/img/og.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#06b6d4"/><stop offset="1" stop-color="#7c3aed"/></linearGradient></defs><rect width="1200" height="630" fill="#0b1020"/><rect x="80" y="330" width="40" height="120" rx="10" fill="url(#g)" opacity=".6"/><rect x="140" y="270" width="40" height="180" rx="10" fill="url(#g)" opacity=".75"/><rect x="200" y="210" width="40" height="240" rx="10" fill="url(#g)" opacity=".9"/><rect x="260" y="150" width="40" height="300" rx="10" fill="url(#g)"/><text x="360" y="330" font-family="Inter,Arial" font-size="120" font-weight="800" fill="#fff">4GNet</text><text x="364" y="400" font-family="Inter,Arial" font-size="40" fill="#9aa8c3">Speed tests · Coverage tools · Free provider matching</text></svg>')
print(f"Built {len(PAGES)} pages into {ROOT}")
