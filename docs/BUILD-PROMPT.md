# 4GNet.com — Phase-Wise Master Build Prompt

> Concept: **4GNet.com — the Wireless Internet Intelligence Hub.**
> Free tools + honest guides for 4G LTE / 5G mobile, home & business wireless internet, eSIM and travel data — monetized by AdSense, YouTube, affiliate/CPA, lead generation, sponsorships and community support.

---

## 0. Why this idea (the numbers)

| Revenue stream | Benchmark (researched Sep 2026) | Why it fits "4G Net" |
|---|---|---|
| ISP / wireless lead gen (CPA) | T-Mobile Home Internet ~$40/lead-sale · AT&T ~$85/lead · Frontier ~$100/plan · HughesNet ~$144/sub (FlexOffers/TapRefer listings) | "4G/5G home internet", "rural internet", "business failover" are high-intent searches |
| Business internet CPC (AdSense side) | "business internet package" ~$55 CPC · "high speed business internet" ~$56 (ppc.io, Jul 2026) · Business-services CPL ~$104 (WordStream 2025) | B2B pages carry the highest-paying ad inventory |
| eSIM affiliate | Airalo 10–12% · Saily 15% · Roamzy/eSIMfly 10–20% lifetime | Travel data is the fastest-growing "4G" consumer use case |
| Display (AdSense) on tools | Speed test, APN, band checker = repeat-visit utility pages with huge pageview counts | Tools rank and get bookmarked |
| YouTube | Embedded explainers → own channel later (speed-test shorts, router reviews) | Video raises dwell time + RPM |
| Sponsorship / promoted slots / pay-per-call | Industry standard on WhistleOut, Uswitch, Allconnect | Media kit + advertise page from day one |

**Positioning:** Neutral, tool-first. Tools pull the traffic, guides earn trust, the lead form earns the money.

---

## 1. Competitive research (42 sites benchmarked)

Speed/coverage: speedtest.net, fast.com, speed.cloudflare.com, nperf.com, opensignal.com, cellmapper.net, coveragemap.com, rootmetrics.com, ofcom checker, downdetector.com
ISP comparison / lead gen: broadbandnow.com, highspeedinternet.com, allconnect.com, cabletv.com, broadbandsearch.net, t-mobile.com/home-internet, waveform.com
Plan comparison: whistleout.com / .com.au / .co.uk, bestphoneplans.net, moneysavingpro.com, uswitch.com, cable.co.uk, 4g.co.uk, 5g.co.uk
eSIM: airalo.com, holafly.com, nomadesim.com, saily.com, esimdb.com
Devices/bands/APN: gsmarena.com, frequencycheck.com, willmyphonework.net, kimovil.com, apnsettings.org
News/education: lightreading.com, fierce-network.com, rcrwireless.com, gsma.com, rvmobileinternet.com, phonearena.com, androidauthority.com

**Patterns adopted:** zip-first hero (BroadbandNow), multi-step "household → priorities → contact" funnel (Allconnect), 3-question plan quiz (WhistleOut), device × carrier compatibility with ✓/partial/✗ (WillMyPhoneWork), country→carrier→OS APN tree with copy buttons (apnsettings), quality score for streaming/gaming/calls (Cloudflare), price-per-GB thinking (Nomad), compensation disclosure near results (all majors), promoted-slot labels (Uswitch), "last updated" + methodology (trust).

---

## PHASE 1 — Foundation & brand

**Prompt:**
> Build a static, GitHub-Pages-compatible (free plan) multi-page website for the domain 4GNet.com. No server, no build step required at runtime. Plain HTML5 + one CSS file + vanilla JS modules. Relative URLs everywhere so it works at `username.github.io/4gnet-com/` and at a custom domain.
> Brand: "4GNet" wordmark with a signal-bar icon (original SVG). Palette: deep navy `#0b1020`, electric cyan `#22d3ee`, violet `#8b5cf6`, lime accent `#a3e635`. Font: Inter (Google Fonts). Light + dark theme toggle with `prefers-color-scheme` default. Mobile-first; nav collapses to a drawer < 900px.
> **Every page** starts with a slim top bar: "Contact, if you are interested in this website / domain name / Sponsorship / Advertisement / Partnership" → `https://web.works/contact` (new tab).
> Global: sticky header, mega-footer (Tools, Learn, Internet, Community, Legal), cookie-consent banner, back-to-top, skip-link, schema.org Organization + WebSite JSON-LD.

## PHASE 2 — Free tools (traffic engine)

> 1. **Speed test** — download/upload/latency/jitter via Cloudflare's public `speed.cloudflare.com/__down` & `__up` endpoints, animated gauge, quality verdict for HD/4K streaming, gaming, video calls, WFH. Graceful error state if blocked. Show "uses ~25–60 MB" warning.
> 2. **LTE/5G band compatibility checker** — pick country + carrier → bands; tick bands your phone supports (or paste list) → ✓ full / ◐ partial / ✗ result with core-band explanation.
> 3. **APN settings finder** — country → carrier → APN, MMSC, proxy, type fields, copy-to-clipboard, iOS/Android steps.
> 4. **Signal quality analyzer** — enter RSRP/RSRQ/SINR → excellent/good/fair/poor with actionable fixes (antenna, window, band lock).
> 5. **Bandwidth calculator** — household devices & activities → recommended Mbps.
> 6. **Mobile data usage calculator** — hours of streaming/social/calls → GB/month.
> 7. **Plan finder quiz** — lines, data, budget, use-case → recommended plan type + lead CTA.
> 8. **Hotspot/router picker** — use-case → router class (CAT class, 5G/4G, external antenna ports).

## PHASE 3 — Lead generation (money engine)

> Dedicated `/get-matched` page + inline hero widget on the home page.
> Multi-step form with progress bar: (1) ZIP/postcode + country → (2) need: home, rural, business, IoT/fleet, RV/travel → (3) household/usage (devices, streaming, gaming, WFH) → (4) priorities (price, speed, no contract, installation) + current provider & speed → (5) contact (name, email, phone optional, best time, consent checkbox). Hidden honeypot. Instant success screen with next steps.
> Business/IoT variant: company, locations, primary vs failover, SIM count, budget, timeline.
> Trust: "Free, no obligation", response time promise, compensation disclosure, privacy link.
> Secondary capture: newsletter ("Weekly deal & coverage alerts"), exit-intent-free sticky CTA bar on mobile.

## PHASE 4 — Content & SEO

> Learn hub with long-form guides (1,000+ words each, FAQ schema): 4G vs 5G, LTE bands explained, boost weak signal, eSIM explained, choosing a 4G/5G router, rural internet options, fixed wireless vs cable vs satellite, business failover.
> Programmatic roadmap: `/internet/{country}/{state}/{city}`, `/esim/{country}`, `/apn/{carrier}`, `/compare/{a}-vs-{b}`.
> Every page: unique title/description, canonical, OG/Twitter tags, breadcrumb, "last updated".
> `sitemap.xml`, `robots.txt`, `ads.txt` (placeholder), `404.html`.

## PHASE 5 — Monetization wiring

> **AdSense:** central `config.js` → `ADSENSE_CLIENT`; loader injects `adsbygoogle.js` only when set. Responsive ad slots: under hero, in-content (every ~3 sections), sidebar on desktop, above footer. Label "Advertisement". No ads inside forms.
> **YouTube:** Video hub + per-guide embeds using lite facades (thumbnail → click-to-load `youtube-nocookie.com`) for speed. Channel CTA.
> **Affiliate:** eSIM & router cards with `rel="sponsored nofollow"` links driven from config; disclosure block on each.
> **Sponsorship/advertising:** media kit page (audience, formats, pricing tiers), inquiry form.

## PHASE 6 — Community & support

> **Support/Donate:** tiers (Supporter $5, Booster $25, Tower $100, Custom) with allocation chart: operations, promotion & marketing, hiring talent, contests & prizes. Pledge form + configurable PayPal/Ko-fi/Stripe links.
> **Contests:** active contest card, prize pool, rules, countdown, entry form, past winners placeholder.
> **Careers / hiring talent:** open roles (writer, video creator, SEO, dev, community mod), application form.
> **Partners:** partnership/API/data inquiries.

## PHASE 7 — Forms & privacy of the owner's email

> All forms POST via fetch to FormSubmit AJAX. The destination email is **never** written in HTML/visible text: it's stored split + encoded in JS and assembled at submit time. After first submission, replace with FormSubmit's random alias for full concealment. No `mailto:` anywhere. Each form sets `_subject`, `_template=table`, `_captcha=false`, honeypot `_honey`.

## PHASE 8 — Legal & trust

> Privacy, Terms, Cookie, Affiliate & Advertising Disclosure, **Trademark & Copyright Disclosure** (independent site; not affiliated with any business named "4G Net/4GNet"; LTE is a trademark of ETSI; carrier & brand names belong to their owners; nominative use only), Accessibility statement, Editorial methodology.

## PHASE 9 — QA, deploy, grow

> Lighthouse ≥ 90, WCAG AA contrast, test 360px/768px/1440px. Push to GitHub `webworksa1/4gnet-com`, publish with GitHub Pages (branch `gh-pages`, root). Add `CNAME` only once DNS for 4gnet.com points to GitHub (A: 185.199.108–111.153; `www` CNAME → webworksa1.github.io).
> Growth: submit sitemap to Search Console, apply AdSense after ~20 quality pages, join FlexOffers/Impact/Travelpayouts, launch YouTube shorts from speed-test data, monthly contest to build email list.
