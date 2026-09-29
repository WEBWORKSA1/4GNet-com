# 4GNet.com — Wireless Internet Hub

Static, GitHub-Pages-ready website for **4GNet.com**: free 4G/5G tools (speed test, LTE band checker, APN finder, signal analyzer, bandwidth & data calculators, plan finder), independent guides, a video hub, a multi-step lead-generation funnel, B2B/IoT quotes, travel eSIM affiliate hub, donations, contests, careers and advertising/sponsorship pages.

- Phase-wise build prompt & research: [`docs/BUILD-PROMPT.md`](docs/BUILD-PROMPT.md)
- Source generator: `build/` (Python 3, no dependencies) → `python3 build/build.py` regenerates all HTML in the repo root.
- Runtime: plain HTML + `assets/css/style.css` + `assets/js/{config,main,tools}.js`. No build step needed to host.

## Configure (edit `assets/js/config.js` only)
| Key | Purpose |
|---|---|
| `adsenseClient`, `adSlots` | Google AdSense publisher ID + slot IDs. Ads load only when set. Also update `ads.txt`. |
| `ga4` | Google Analytics 4 ID (optional) |
| `formAlias` | FormSubmit random alias (see below) |
| `donate.*` | PayPal / Stripe / Ko-fi / Buy Me a Coffee links — buttons appear automatically when set |
| `affiliates.*` | Your tracked eSIM affiliate links |

## Forms
All forms (lead gen, business, donation pledge, contest, careers, advertising, contact, newsletter, APN request) post via AJAX to FormSubmit. The destination address is never written in HTML or visible text — it is stored encoded in `config.js` and assembled at submit time.
1. Submit any form once on the live site → FormSubmit sends an **activation email**; click to confirm.
2. FormSubmit then provides a random alias string — paste it into `formAlias` to remove the encoded address entirely.

## Publishing (GitHub Pages, free plan)
The site is served from the `gh-pages` branch (root). If Pages is not yet active: **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `gh-pages` / `(root)` → Save.** Live URL: `https://webworksa1.github.io/4gnet-com/`.

## Custom domain
Once DNS for 4gnet.com is ready: add A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` and `www` CNAME → `webworksa1.github.io`, then set the custom domain in **Settings → Pages** (this creates the `CNAME` file).

## Before launch
- Adjust contest prizes/dates in `build/pages_community.py` and donation tiers to amounts you will honour.
- Replace affiliate URLs with tracked links; apply to AdSense after the site is live on the custom domain.

## Legal
Independent website; not affiliated with any business named "4GNet"/"4G Net". "LTE" is a trademark of ETSI. All other trademarks belong to their owners. See `disclosure.html`.
