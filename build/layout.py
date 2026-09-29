"""Shared layout for 4GNet.com static pages."""
import json

DOMAIN = "https://4gnet.com"
INTEREST = "https://web.works/contact"
UPDATED = "September 2026"

LOGO = ('<svg viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#06b6d4"/><stop offset="1" stop-color="#7c3aed"/></linearGradient></defs>'
        '<rect width="40" height="40" rx="11" fill="url(#lg)"/>'
        '<rect x="8" y="24" width="4.5" height="8" rx="1.5" fill="#fff" opacity=".55"/>'
        '<rect x="15" y="19" width="4.5" height="13" rx="1.5" fill="#fff" opacity=".7"/>'
        '<rect x="22" y="13" width="4.5" height="19" rx="1.5" fill="#fff" opacity=".85"/>'
        '<rect x="29" y="7" width="4.5" height="25" rx="1.5" fill="#fff"/></svg>')

NAV = [
    ("Tools", "tools.html", [
        ("Internet Speed Test", "speed-test.html"), ("LTE/5G Band Checker", "band-checker.html"),
        ("APN Settings Finder", "apn-settings.html"), ("Signal Strength Analyzer", "signal-analyzer.html"),
        ("Bandwidth Calculator", "bandwidth-calculator.html"), ("Data Usage Calculator", "data-calculator.html"),
        ("Plan Finder Quiz", "plan-finder.html")]),
    ("Internet", "home-internet.html", [
        ("4G/5G Home Internet", "home-internet.html"), ("Rural Internet", "rural-internet.html"),
        ("Business & IoT", "business.html"), ("Travel eSIM", "esim.html"), ("Routers & Hotspots", "routers.html")]),
    ("Learn", "learn.html", [
        ("All Guides", "learn.html"), ("Video Hub", "videos.html"), ("4G vs 5G", "guide-4g-vs-5g.html"),
        ("LTE Bands Explained", "guide-lte-bands.html"), ("Boost Weak Signal", "guide-boost-signal.html"),
        ("eSIM Explained", "guide-esim.html")]),
    ("Community", "support.html", [
        ("Support Us / Donate", "support.html"), ("Contests & Prizes", "contests.html"),
        ("Careers & Talent", "careers.html"), ("Advertise & Sponsor", "advertise.html"), ("Contact", "contact.html")]),
]


def nav_html():
    items = []
    for label, href, sub in NAV:
        subs = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in sub)
        items.append(f'<li><a href="{href}">{label}</a><ul class="dropdown">{subs}</ul></li>')
    return "".join(items)


FOOTER = f"""
<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div>
        <a class="logo" href="index.html" style="color:#fff">{LOGO}<span>4GNet<small>Wireless Internet Hub</small></span></a>
        <p style="margin-top:14px">Free tools, independent guides and matched quotes for 4G LTE, 5G, home wireless, business connectivity and travel eSIM.</p>
        <a class="btn btn-primary btn-sm" href="get-matched.html">Get matched free →</a>
      </div>
      <div><h4>Tools</h4><ul>
        <li><a href="speed-test.html">Speed Test</a></li><li><a href="band-checker.html">Band Checker</a></li>
        <li><a href="apn-settings.html">APN Settings</a></li><li><a href="signal-analyzer.html">Signal Analyzer</a></li>
        <li><a href="bandwidth-calculator.html">Bandwidth Calculator</a></li><li><a href="data-calculator.html">Data Calculator</a></li></ul></div>
      <div><h4>Internet</h4><ul>
        <li><a href="home-internet.html">4G/5G Home Internet</a></li><li><a href="rural-internet.html">Rural Internet</a></li>
        <li><a href="business.html">Business &amp; IoT</a></li><li><a href="esim.html">Travel eSIM</a></li>
        <li><a href="routers.html">Routers &amp; Hotspots</a></li><li><a href="plan-finder.html">Plan Finder</a></li></ul></div>
      <div><h4>Community</h4><ul>
        <li><a href="support.html">Support / Donate</a></li><li><a href="contests.html">Contests &amp; Prizes</a></li>
        <li><a href="careers.html">Careers</a></li><li><a href="advertise.html">Advertise &amp; Sponsor</a></li>
        <li><a href="videos.html">Video Hub</a></li><li><a href="contact.html">Contact</a></li></ul></div>
      <div><h4>Company &amp; Legal</h4><ul>
        <li><a href="about.html">About &amp; Methodology</a></li><li><a href="privacy.html">Privacy Policy</a></li>
        <li><a href="terms.html">Terms of Use</a></li><li><a href="disclosure.html">Trademark, Copyright &amp; Affiliate Disclosure</a></li>
        <li><a href="{INTEREST}" target="_blank" rel="noopener">Buy / partner on this domain</a></li></ul></div>
    </div>
    <p class="foot-legal">4GNet.com is an independent information and comparison website. It is not affiliated with, endorsed by, or sponsored by any mobile network operator, equipment maker, or any business using a similar name. "LTE" is a trademark of ETSI. All carrier, product and brand names are trademarks of their respective owners and are used only to identify their products (nominative use). We may earn a commission or referral fee when you click links or request quotes; this never changes the price you pay. See our <a href="disclosure.html">full disclosure</a>.</p>
    <div class="foot-bottom"><span>© <span data-year>2026</span> 4GNet.com. Original content and design. All rights reserved.</span>
      <span><a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a> · <a href="disclosure.html">Disclosure</a> · <a href="sitemap.xml">Sitemap</a></span></div>
  </div>
</footer>
<div class="cookie" role="dialog" aria-label="Cookie consent">
  <b>Cookies &amp; ads</b><br>We use essential cookies, and with your consent, analytics and personalised ads (Google AdSense). <a href="privacy.html">Learn more</a>.
  <div class="btns"><button class="btn btn-primary btn-sm" data-cookie="all">Accept all</button><button class="btn btn-ghost btn-sm" data-cookie="essential">Essential only</button></div>
</div>
<div class="mobile-cta"><a class="btn btn-primary btn-block" href="get-matched.html">⚡ Find faster internet — free quotes</a></div>
<button class="icon-btn totop" aria-label="Back to top">↑</button>
"""


def ad(pos="content"):
    return f'<div class="ad-slot container" data-pos="{pos}" aria-label="Advertisement">Advertisement</div>'


def page(filename, title, desc, body, scripts=("main",), schema=None):
    canonical = f"{DOMAIN}/{'' if filename == 'index.html' else filename}"
    ld = [{"@context": "https://schema.org", "@type": "WebSite", "name": "4GNet", "url": DOMAIN + "/"},
          {"@context": "https://schema.org", "@type": "Organization", "name": "4GNet", "url": DOMAIN + "/",
           "logo": DOMAIN + "/assets/img/logo.svg"}]
    if schema:
        ld.extend(schema if isinstance(schema, list) else [schema])
    js = "".join(f'<script src="assets/js/{s}.js" defer></script>' for s in ("config",) + tuple(scripts))
    full_title = title if "4GNet" in title else f"{title} | 4GNet"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#0b1020">
<meta property="og:type" content="website"><meta property="og:site_name" content="4GNet">
<meta property="og:title" content="{full_title}"><meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}"><meta property="og:image" content="{DOMAIN}/assets/img/og.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/logo.svg" type="image/svg+xml">
<link rel="manifest" href="manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>try{{var t=localStorage.getItem("theme");if(t)document.documentElement.setAttribute("data-theme",t)}}catch(e){{}}</script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
{js}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar">Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership → <a href="{INTEREST}" target="_blank" rel="noopener">web.works/contact</a></div>
<header class="site-header">
  <div class="container nav">
    <a class="logo" href="index.html" aria-label="4GNet home">{LOGO}<span>4GNet<small>Wireless Internet Hub</small></span></a>
    <ul class="menu" id="menu">{nav_html()}</ul>
    <div class="nav-actions">
      <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode">◐</button>
      <a class="btn btn-primary btn-sm" href="get-matched.html">Get Matched</a>
      <button class="icon-btn burger" aria-label="Open menu" aria-controls="menu" aria-expanded="false">☰</button>
    </div>
  </div>
</header>
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
"""


def hero(title, sub, crumb=None):
    c = f'<div class="crumbs"><a href="index.html">Home</a> › {crumb}</div>' if crumb else ""
    return f'<section class="page-hero"><div class="container">{c}<h1>{title}</h1><p>{sub}</p></div></section>'


def faq(items):
    html = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in items)
    schema = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}
    return html, schema


def honey():
    return '<input class="hp" type="text" name="_honey" tabindex="-1" autocomplete="off" aria-hidden="true">'


def consent(text="I agree to be contacted about my request and accept the <a href='privacy.html'>Privacy Policy</a>."):
    return f'<label class="check"><input type="checkbox" name="consent" value="yes" required> <span>{text}</span></label>'


def cta_band(title="Paying too much for slow internet?", sub="Tell us your address and needs. We match you with 4G, 5G and fixed-wireless providers that actually serve you — free, no obligation.", href="get-matched.html", label="Get free quotes →"):
    return f'<section><div class="container"><div class="cta-band"><div><h2 style="margin:0 0 6px">{title}</h2><p>{sub}</p></div><a class="btn btn-light" href="{href}">{label}</a></div></div></section>'


VIDEOS = [
    ("wiWXQEkO5ws", "4G and LTE: Explained!", "Marques Brownlee"),
    ("-g5ek_9Dipc", "Explained: 1G, 2G, 3G, 4G (LTE) & 5G Mobile Tech", "Babbling Boolean"),
    ("dB6VHPYUrNA", "5G vs 4G: The difference explained", "Which?"),
    ("-Rs8xyt7400", "4G vs. 5G: What's the Actual Difference?", "History of Simple Things"),
    ("GEx_d0SjvS0", "Everything You Need to Know About 5G", "IEEE Spectrum"),
    ("fW62mzey0f4", "What is an eSIM and How Does it Work?", "Gary Explains"),
    ("qIxKdVfaZI0", "What's an eSIM? How does it work?", "Simply Mobile"),
    ("0faCad2kKeg", "How Cell Service Actually Works", "Wendover Productions"),
    ("MT8oXJXtzq4", "How Do Cell Towers Actually Work?", "History of Simple Things"),
    ("rsRCJmWFNCg", "I Tested 5G Routers for a Month — the Best One", "wiredtech"),
    ("KEXUQ-UHrsY", "Best SIM WiFi Routers – 4G/5G Picks for Home & Travel", "Technico Himanshu"),
]


def video(vid, title, channel):
    return f'<div class="vcard"><div class="yt" data-id="{vid}" data-title="{title}"></div><h3>{title}</h3><p class="muted" style="margin:0;font-size:.85rem">{channel} · via YouTube</p></div>'
