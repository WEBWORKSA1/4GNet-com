from layout import page, hero, ad, faq, honey, consent, cta_band, video, VIDEOS, UPDATED

PAGES = {}


def reg(fn, *a, **k):
    PAGES[fn] = page(fn, *a, **k)


# ---------------------------------------------------------------- LEAD FORM
def lead_form(default_need="home"):
    needs = [("home", "🏠", "Home internet"), ("rural", "🌾", "Rural / no cable"), ("business", "🏢", "Business / failover"),
             ("iot", "📡", "IoT / fleet SIMs"), ("rv", "🚐", "RV / mobile life"), ("travel", "✈️", "Travel eSIM")]
    need_html = "".join(f'<label class="choice"><input type="radio" name="need" value="{v}" {"checked" if v == default_need else ""}><span><i>{i}</i>{t}</span></label>' for v, i, t in needs)
    uses = [("streaming", "📺", "4K/HD streaming"), ("gaming", "🎮", "Online gaming"), ("wfh", "💼", "Work from home"),
            ("calls", "🎥", "Video calls"), ("smart", "💡", "Smart home"), ("basic", "🌐", "Browsing & email")]
    use_html = "".join(f'<label class="choice"><input type="checkbox" name="usage" value="{v}"><span><i>{i}</i>{t}</span></label>' for v, i, t in uses)
    pri = [("price", "💲", "Lowest price"), ("speed", "🚀", "Fastest speed"), ("nocontract", "🔓", "No contract"),
           ("unlimited", "♾️", "Truly unlimited"), ("selfinstall", "🔌", "Self-install"), ("support", "🤝", "Great support")]
    pri_html = "".join(f'<label class="choice"><input type="checkbox" name="priorities" value="{v}"><span><i>{i}</i>{t}</span></label>' for v, i, t in pri)
    return f"""
<div class="stepper" data-stepper id="lead">
  <div class="progress"><i></i></div>
  <p class="muted" style="font-size:.85rem;margin-bottom:18px"><span data-step-label>Step 1 of 5</span> · Takes about 60 seconds · 100% free</p>
  <form data-form="Lead - Get Matched" data-success="You're matched! A connectivity specialist will email your personalised options within 1 business day.">
    {honey()}
    <div class="step" data-require-choice="need">
      <h3>What do you need connectivity for?</h3>
      <div class="choice-grid">{need_html}</div>
      <div class="step-nav"><span></span><button type="button" class="btn btn-primary" data-next>Continue →</button></div>
    </div>
    <div class="step">
      <h3>Where do you need service?</h3>
      <div class="row"><div class="field"><label for="lf-zip">ZIP / postal code</label><input id="lf-zip" name="zip" required autocomplete="postal-code" placeholder="e.g. 90210 or H2X 1Y4"></div>
      <div class="field"><label for="lf-country">Country</label><select id="lf-country" name="country" required>
        <option>United States</option><option>Canada</option><option>United Kingdom</option><option>India</option><option>Australia</option><option>Germany</option><option>United Arab Emirates</option><option>Sri Lanka</option><option>Other</option></select></div></div>
      <div class="row"><div class="field"><label for="lf-city">City / town (optional)</label><input id="lf-city" name="city" autocomplete="address-level2"></div>
      <div class="field"><label for="lf-prop">Property</label><select id="lf-prop" name="property"><option>House – owned</option><option>House – rented</option><option>Apartment / condo</option><option>Farm / acreage</option><option>Office / retail</option><option>Vehicle / RV / boat</option></select></div></div>
      <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div>
    </div>
    <div class="step">
      <h3>How will you use it?</h3>
      <div class="choice-grid">{use_html}</div>
      <div class="row"><div class="field"><label for="lf-people">People / users</label><select id="lf-people" name="users"><option>1</option><option>2</option><option selected>3–4</option><option>5–9</option><option>10–49</option><option>50+</option></select></div>
      <div class="field"><label for="lf-dev">Connected devices</label><select id="lf-dev" name="devices"><option>1–5</option><option selected>6–15</option><option>16–30</option><option>30+</option></select></div></div>
      <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div>
    </div>
    <div class="step">
      <h3>What matters most?</h3>
      <div class="choice-grid">{pri_html}</div>
      <div class="row"><div class="field"><label for="lf-cur">Current provider (optional)</label><input id="lf-cur" name="current_provider" placeholder="e.g. none, DSL, satellite…"></div>
      <div class="field"><label for="lf-speed">Current speed (optional)</label><select id="lf-speed" name="current_speed"><option>Don't know</option><option>Under 10 Mbps</option><option>10–25 Mbps</option><option>25–100 Mbps</option><option>100+ Mbps</option><option>No internet</option></select></div></div>
      <div class="row"><div class="field"><label for="lf-budget">Monthly budget</label><select id="lf-budget" name="budget"><option>Under $30</option><option selected>$30–$60</option><option>$60–$100</option><option>$100–$250</option><option>$250+ (business)</option></select></div>
      <div class="field"><label for="lf-when">When do you want to switch?</label><select id="lf-when" name="timeline"><option>ASAP</option><option>Within 30 days</option><option>1–3 months</option><option>Just researching</option></select></div></div>
      <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="button" class="btn btn-primary" data-next>Continue →</button></div>
    </div>
    <div class="step">
      <h3>Where should we send your matches?</h3>
      <div class="row"><div class="field"><label for="lf-name">Full name</label><input id="lf-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="lf-email">Email</label><input id="lf-email" type="email" name="email" required autocomplete="email"></div></div>
      <div class="row"><div class="field"><label for="lf-phone">Phone (optional, for faster quotes)</label><input id="lf-phone" type="tel" name="phone" autocomplete="tel"></div>
      <div class="field"><label for="lf-time">Best time to reach you</label><select id="lf-time" name="best_time"><option>Any time</option><option>Morning</option><option>Afternoon</option><option>Evening</option><option>Email only</option></select></div></div>
      <div class="field"><label for="lf-notes">Anything else? (optional)</label><textarea id="lf-notes" name="notes" placeholder="Signal issues, number of locations, data caps you've hit…"></textarea></div>
      {consent("I agree that 4GNet and its provider partners may contact me about my request. I accept the <a href='privacy.html'>Privacy Policy</a>. No spam, unsubscribe anytime.")}
      <div class="step-nav"><button type="button" class="btn btn-ghost" data-prev>← Back</button><button type="submit" class="btn btn-primary">Show my matches ⚡</button></div>
    </div>
    <div class="form-msg" role="status" aria-live="polite"></div>
  </form>
  <div class="step-done" style="display:none;text-align:center;padding:10px 0">
    <div style="font-size:3rem">🎉</div><h3>Request received!</h3>
    <p class="muted">While you wait: <a href="speed-test.html">test your current speed</a> so you can compare offers.</p>
  </div>
</div>"""


def hero_zip():
    return """
<form class="hero-card" action="get-matched.html" method="get">
  <span class="tag hot">Free · 60 seconds</span>
  <h3 style="font-size:1.4rem">Find faster 4G / 5G internet at your address</h3>
  <div class="field"><label for="hz-zip">ZIP / postal code</label><input id="hz-zip" name="zip" required placeholder="Enter ZIP or postcode" autocomplete="postal-code"></div>
  <div class="field"><label for="hz-need">I need</label><select id="hz-need" name="need">
    <option value="home">Home internet</option><option value="rural">Rural internet</option><option value="business">Business / failover</option>
    <option value="iot">IoT / fleet SIMs</option><option value="rv">RV / mobile internet</option><option value="travel">Travel eSIM</option></select></div>
  <button class="btn btn-primary btn-block" type="submit">Compare providers →</button>
  <p style="font-size:.78rem;color:#94a3b8;margin:10px 0 0">No obligation. We may earn a referral fee from providers — it never affects your price.</p>
</form>"""


# ---------------------------------------------------------------- HOME
tools = [
    ("⚡", "Speed Test", "Download, upload, ping & jitter with a streaming/gaming verdict.", "speed-test.html"),
    ("📶", "Band Checker", "Will your phone or router work on a carrier? Check LTE bands.", "band-checker.html"),
    ("⚙️", "APN Settings", "Correct APN for 20+ carriers with one-tap copy.", "apn-settings.html"),
    ("📡", "Signal Analyzer", "Turn RSRP/RSRQ/SINR into a grade and fixes.", "signal-analyzer.html"),
    ("🧮", "Bandwidth Calculator", "How many Mbps your household really needs.", "bandwidth-calculator.html"),
    ("📊", "Data Calculator", "Estimate GB per month before you pick a plan.", "data-calculator.html"),
    ("🎯", "Plan Finder", "Three questions → the plan type that fits.", "plan-finder.html"),
    ("🌍", "Travel eSIM", "Compare eSIM providers for 190+ destinations.", "esim.html"),
]
tool_cards = "".join(f'<a class="card" href="{h}"><div class="ic">{i}</div><h3>{t}</h3><p>{d}</p></a>' for i, t, d, h in tools)
home_faq, home_faq_ld = faq([
    ("Is 4G LTE home internet good enough in 2026?", "For 1–3 people who stream HD, browse and video-call, a strong 4G LTE-Advanced signal (typically 25–100 Mbps) is enough. Heavy 4K streaming, large uploads or big households should look at 5G home internet or fiber."),
    ("Is 4GNet free to use?", "Yes. All tools and guides are free. When you request quotes we may receive a referral fee from providers, which never changes your price."),
    ("How does the Get Matched service work?", "You tell us your location, usage and priorities. We compare wireless, fixed-wireless and other providers that serve you and send personalised options, usually within one business day."),
    ("What's the difference between 4G and 5G?", "5G adds new spectrum and a faster radio interface. In real life, mid-band 5G is often 2–5× faster than 4G with lower latency, but 4G still has wider coverage — especially rural and indoors."),
])
reg("index.html", "4GNet — 4G LTE & 5G Internet Speed Test, Coverage Tools & Free Provider Matching",
    "Free 4G/5G speed test, LTE band checker, APN settings, signal analyzer and data calculators. Compare home, rural, business and travel eSIM internet — get matched free.",
    f"""
<section class="hero"><div class="container">
  <div>
    <span class="pill">📶 4G LTE · 5G · Fixed Wireless · eSIM</span>
    <h1>Faster wireless internet starts with <span class="grad-text">the right data.</span></h1>
    <p class="lead">Test your connection, check coverage and device compatibility, and get matched with 4G/5G home, rural, business and travel plans — all free, all in one place.</p>
    <div class="badges"><span class="pill">✓ 8 free tools</span><span class="pill">✓ Independent guides</span><span class="pill">✓ Free provider matching</span></div>
    <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:8px"><a class="btn btn-lime" href="speed-test.html">⚡ Run a speed test</a><a class="btn btn-ghost" style="color:#fff;border-color:#334" href="tools.html">Explore tools</a></div>
  </div>
  {hero_zip()}
</div></section>
{ad("top")}
<section><div class="container">
  <div class="section-head"><span class="eyebrow">Free toolkit</span><h2>Everything you need to diagnose, compare &amp; upgrade</h2><p class="muted">The tools network pros use — simplified for everyone.</p></div>
  <div class="grid g4">{tool_cards}</div>
</div></section>
<section class="section-alt"><div class="container">
  <div class="stats">
    <div><b class="grad-text">8</b><span class="muted">Free tools</span></div>
    <div><b class="grad-text">7</b><span class="muted">Countries in band database</span></div>
    <div><b class="grad-text">20+</b><span class="muted">Carrier APN profiles</span></div>
    <div><b class="grad-text">60s</b><span class="muted">To get matched</span></div>
  </div>
</div></section>
<section><div class="container">
  <div class="section-head"><span class="eyebrow">Get connected</span><h2>Pick your situation</h2></div>
  <div class="grid g3">
    <a class="card" href="home-internet.html"><span class="tag">Most popular</span><h3>🏠 4G/5G Home Internet</h3><p>Cut the cable. Wireless home internet with no install, no data caps on most plans.</p></a>
    <a class="card" href="rural-internet.html"><span class="tag hot">High demand</span><h3>🌾 Rural Internet</h3><p>No cable or fiber? Compare fixed wireless, LTE with antennas, and satellite.</p></a>
    <a class="card" href="business.html"><span class="tag">B2B</span><h3>🏢 Business, Failover &amp; IoT</h3><p>Keep POS and VoIP online with 4G/5G failover, bonded routers and IoT SIMs.</p></a>
    <a class="card" href="esim.html"><h3>✈️ Travel eSIM</h3><p>Land connected. Compare data-only eSIMs by destination, validity and hotspot rules.</p></a>
    <a class="card" href="routers.html"><h3>📦 Routers &amp; Hotspots</h3><p>Choose the right LTE category, 5G modem and external antenna for your space.</p></a>
    <a class="card" href="plan-finder.html"><h3>🎯 Not sure?</h3><p>Take the 3-question plan finder and get a recommendation instantly.</p></a>
  </div>
</div></section>
<section class="section-alt" id="match"><div class="container">
  <div class="layout" style="align-items:start">
    <div><span class="eyebrow">Free provider matching</span><h2>Get personalised 4G/5G internet options</h2>
      <ul class="list-check"><li>Compare providers that actually serve your address</li><li>Home, rural, business, IoT, RV and travel options</li><li>Honest advice on coverage, data caps and contracts</li><li>Free, no obligation, typically answered within 1 business day</li></ul>
      {lead_form()}
    </div>
    <aside class="sidebar"><div class="card"><h3>Why people use 4GNet</h3><p>We combine speed tests, band compatibility and signal data with provider availability so you don't buy a plan your device or location can't support.</p><hr style="border:0;border-top:1px solid var(--line);margin:16px 0"><p><b>Businesses:</b> need failover for multiple sites? <a href="business.html">Request a B2B quote →</a></p></div>{ad("sidebar")}</aside>
  </div>
</div></section>
<section><div class="container">
  <div class="section-head"><span class="eyebrow">Watch &amp; learn</span><h2>Wireless explained in minutes</h2></div>
  <div class="grid g3">{"".join(video(*v) for v in VIDEOS[:3])}</div>
  <p class="center" style="margin-top:20px"><a class="btn btn-ghost" href="videos.html">Open the video hub →</a></p>
</div></section>
{ad("content")}
<section class="section-alt"><div class="container">
  <div class="section-head"><span class="eyebrow">Guides</span><h2>Popular guides</h2></div>
  <div class="grid g3">
    <a class="card" href="guide-4g-vs-5g.html"><span class="tag">Explainer</span><h3>4G vs 5G: real-world differences</h3><p>Speed, latency, coverage and whether upgrading is worth it.</p></a>
    <a class="card" href="guide-lte-bands.html"><span class="tag">Technical</span><h3>LTE bands explained</h3><p>Why low bands travel further and high bands go faster.</p></a>
    <a class="card" href="guide-boost-signal.html"><span class="tag">How-to</span><h3>12 ways to boost a weak 4G signal</h3><p>Placement, antennas, band locking and boosters.</p></a>
  </div>
</div></section>
<section><div class="container">
  <div class="grid g3">
    <div class="card"><h3>🏆 Monthly contest</h3><p>Share your best speed-test hack and win prizes.</p><p style="margin-top:12px"><a href="contests.html">Enter now →</a></p></div>
    <div class="card"><h3>💙 Support independent testing</h3><p>Donations fund servers, new tools, hiring and contest prizes.</p><p style="margin-top:12px"><a href="support.html">Support us →</a></p></div>
    <div class="card"><h3>📣 Reach connected buyers</h3><p>Sponsorships, display ads and partnerships for carriers, MVNOs and hardware brands.</p><p style="margin-top:12px"><a href="advertise.html">Media kit →</a></p></div>
  </div>
</div></section>
<section class="section-alt"><div class="container" style="max-width:860px">
  <div class="section-head"><h2>Frequently asked questions</h2></div>{home_faq}
  <div class="card" style="margin-top:24px"><h3>📬 Deal &amp; coverage alerts</h3><p>One short email a week: new plans, price drops and 5G rollouts.</p>
    <form data-form="Newsletter" data-success="Subscribed! Check your inbox soon." style="margin-top:12px">{honey()}<div class="row"><input type="email" name="email" required placeholder="you@example.com" aria-label="Email"><button class="btn btn-primary" type="submit">Subscribe</button></div><div class="form-msg" role="status"></div></form></div>
</div></section>
{cta_band()}
""", scripts=("main",), schema=home_faq_ld)

# ---------------------------------------------------------------- GET MATCHED
gm_faq, gm_ld = faq([
    ("Is it really free?", "Yes. Providers may pay us a referral fee when you sign up. You pay the provider's normal price — often less, thanks to partner promotions."),
    ("Will I be spammed with calls?", "No. Phone is optional. By default we reply by email with your options, and you choose whether to proceed."),
    ("Which countries do you cover?", "We have the deepest provider coverage in the US, Canada, the UK, India and Australia, and handle travel eSIM requests worldwide."),
])
reg("get-matched.html", "Get Matched — Free 4G/5G Internet Quotes", "Answer 5 quick questions and get matched with 4G LTE, 5G, fixed-wireless and business internet providers that serve your address. Free, no obligation.",
    hero("Get matched with the best wireless internet for you", "Five quick steps. Personalised options from providers that actually serve your address — free and with no obligation.", "Get Matched") + f"""
<section><div class="container"><div class="layout">
  <div>{lead_form()}</div>
  <aside class="sidebar"><div class="card"><h3>What happens next?</h3><ol style="padding-left:1.2em;color:var(--muted)"><li>We check coverage and providers at your location.</li><li>We filter by your usage, budget and device.</li><li>You receive 2–4 clear options by email.</li><li>You decide. Zero pressure.</li></ol>
  <p class="muted" style="font-size:.8rem">Disclosure: we may earn a referral fee from providers. <a href="disclosure.html">Details</a>.</p></div></aside>
</div></div></section>
<section class="section-alt"><div class="container" style="max-width:860px"><h2>Questions</h2>{gm_faq}</div></section>
""", schema=gm_ld)

# ---------------------------------------------------------------- TOOLS HUB
reg("tools.html", "Free 4G/5G Network Tools", "Free 4G LTE and 5G tools: internet speed test, band checker, APN settings, signal analyzer, bandwidth and data calculators, plan finder.",
    hero("Free 4G &amp; 5G network tools", "Diagnose your connection, check compatibility and size your plan — no sign-up required.", "Tools") +
    f'<section><div class="container"><div class="grid g4">{tool_cards}</div></div></section>{ad()}{cta_band()}')

# ---------------------------------------------------------------- SPEED TEST
st_faq, st_ld = faq([
    ("How much data does a speed test use?", "Typically 25–60 MB for a full download and upload run. On a metered mobile plan, run it on purpose rather than repeatedly."),
    ("What is a good 4G speed?", "Real-world 4G LTE usually delivers 10–60 Mbps; LTE-Advanced with carrier aggregation can exceed 100 Mbps. Under 10 Mbps suggests weak signal or a congested cell."),
    ("What's ping and jitter?", "Ping (latency) is the round-trip time in milliseconds. Jitter is how much ping varies. For gaming and calls, aim for ping under 60 ms and jitter under 30 ms."),
    ("Who runs the test servers?", "This tool measures against Cloudflare's public speed-test network, a global edge network close to most users. Results may differ from other test providers."),
])
reg("speed-test.html", "Internet Speed Test — 4G, 5G & Wi-Fi", "Free internet speed test for 4G LTE, 5G and Wi-Fi. Measure download, upload, ping and jitter, then see what your connection can handle.",
    hero("Internet speed test", "Measure download, upload, ping and jitter — then see if your connection handles 4K, gaming and video calls.", '<a href="tools.html">Tools</a> › Speed Test') + f"""
<section><div class="container" style="max-width:900px">
  <div class="tool" id="speedtest">
    <div class="gauge-wrap">
      <svg class="gauge" viewBox="0 0 320 240" aria-hidden="true">
        <defs><linearGradient id="gg" x1="0" x2="1"><stop offset="0" stop-color="#06b6d4"/><stop offset="1" stop-color="#7c3aed"/></linearGradient></defs>
        <path d="M 40 229 A 138 138 0 1 1 280 229" fill="none" stroke="var(--surface2)" stroke-width="22" stroke-linecap="round"/>
        <path d="M 40 229 A 138 138 0 1 1 280 229" fill="none" stroke="url(#gg)" stroke-width="22" stroke-linecap="round" opacity=".9"/>
        <g id="st-needle" transform="rotate(-120 160 160)"><line x1="160" y1="160" x2="160" y2="42" stroke="var(--text)" stroke-width="4" stroke-linecap="round"/><circle cx="160" cy="160" r="10" fill="var(--text)"/></g>
      </svg>
      <div class="gauge-val"><b id="st-val">0</b><span id="st-unit" class="muted">Mbps</span></div>
    </div>
    <p class="center muted" id="st-phase" aria-live="polite">Press start. Uses roughly 25–60 MB of data.</p>
    <p class="center"><button class="btn btn-primary" id="st-start" style="min-width:200px">Start test</button></p>
    <div class="metrics">
      <div class="metric"><span>Download</span><b id="m-down">–</b><span>Mbps</span></div>
      <div class="metric"><span>Upload</span><b id="m-up">–</b><span>Mbps</span></div>
      <div class="metric"><span>Ping</span><b id="m-ping">–</b><span>ms</span></div>
      <div class="metric"><span>Jitter</span><b id="m-jit">–</b><span>ms</span></div>
    </div>
    <p id="st-err" class="form-msg err" hidden>The test server couldn't be reached from your network (a firewall, VPN or ad-blocker may be blocking it). Try disabling blockers or another network.</p>
    <div class="result-box" id="st-after"><h3 id="st-grade"></h3><div class="verdict" id="st-verdict"></div>
      <p style="margin-top:16px">Not happy with the result? <a class="btn btn-primary btn-sm" href="get-matched.html">Find faster internet at your address →</a></p></div>
  </div>
  {ad()}
  <div class="prose"><h2>How to get an accurate 4G/5G speed test</h2>
  <ol><li>Close apps and downloads on every device sharing the connection.</li><li>For a hotspot or router, test on a device close to it — or wired.</li><li>Run 3 tests at different times (peak evening vs. morning) to see congestion.</li><li>Note your signal (RSRP/SINR) and run them through the <a href="signal-analyzer.html">signal analyzer</a>.</li></ol>
  <h2>Typical speeds by technology</h2>
  <div class="table-wrap"><table><tr><th>Technology</th><th>Typical download</th><th>Typical latency</th></tr>
  <tr><td>4G LTE</td><td>10–60 Mbps</td><td>30–60 ms</td></tr><tr><td>4G LTE-Advanced (CA)</td><td>50–200 Mbps</td><td>25–50 ms</td></tr>
  <tr><td>5G low-band</td><td>50–150 Mbps</td><td>25–45 ms</td></tr><tr><td>5G mid-band (C-band / n77/n78)</td><td>150–800 Mbps</td><td>15–35 ms</td></tr>
  <tr><td>5G mmWave</td><td>1–3 Gbps (line of sight)</td><td>10–25 ms</td></tr><tr><td>Geostationary satellite</td><td>25–150 Mbps</td><td>550–700 ms</td></tr><tr><td>LEO satellite</td><td>50–250 Mbps</td><td>25–60 ms</td></tr></table></div>
  <p class="meta">Ranges are indicative real-world values and vary by network, device, load and signal. Last updated {UPDATED}.</p>
  <h2>FAQ</h2>{st_faq}</div>
</div></section>
""", scripts=("main", "tools"), schema=st_ld)

# ---------------------------------------------------------------- BAND CHECKER
reg("band-checker.html", "LTE Band Checker — Will My Phone Work on This Carrier?", "Check 4G LTE band compatibility between your phone or router and carriers in the US, Canada, UK, India, Australia, Germany and Japan.",
    hero("LTE band compatibility checker", "Pick a carrier, tick the bands your phone or router supports, and see whether it will work — before you buy or travel.", '<a href="tools.html">Tools</a> › Band Checker') + f"""
<section><div class="container" style="max-width:960px">
  <div class="tool" id="bandchecker">
    <div class="row" style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
      <div class="field"><label for="bc-country">Country</label><select id="bc-country"></select></div>
      <div class="field"><label for="bc-carrier">Carrier</label><select id="bc-carrier"></select></div>
    </div>
    <p style="margin:0"><b>Carrier's 4G LTE bands</b> <span class="muted" style="font-size:.85rem">(green underline = core coverage/capacity band)</span></p>
    <div class="bands" id="bc-carrier-bands"></div>
    <hr style="border:0;border-top:1px solid var(--line);margin:18px 0">
    <p style="margin:0"><b>Your device's bands</b> — tap to select, or paste from the spec sheet</p>
    <div class="bands" id="bc-bands"></div>
    <div class="field"><label for="bc-paste">Paste bands (e.g. "1, 2, 3, 4, 5, 7, 8, 12, 13, 20, 28, 66, 71")</label><input id="bc-paste" placeholder="LTE bands from GSMArena or the manufacturer page"></div>
    <button class="btn btn-primary" id="bc-check">Check compatibility</button>
    <div class="result-box" id="bc-result" aria-live="polite"></div>
  </div>
  <p class="meta" style="margin-top:12px">Band lists reflect commonly deployed 4G LTE bands and are updated periodically; carriers refarm spectrum over time. Always confirm with the carrier before purchase. Last updated {UPDATED}.</p>
  {ad()}
  <div class="prose"><h2>How to find your phone's LTE bands</h2><ul><li><b>Android:</b> search your exact model number (e.g. SM-S928B vs SM-S928U) on the manufacturer site or a specs database — regional variants support different bands.</li><li><b>iPhone:</b> Apple lists bands per model number at its "LTE and 5G" support page; check Settings → General → About → Model Number.</li><li><b>Routers/hotspots:</b> look for "LTE FDD" and "LTE TDD" band lists on the datasheet.</li></ul>
  <h2>Why "core bands" matter most</h2><p>Carriers rely on one or two <b>low bands</b> (600–900 MHz: B5, B8, B12, B13, B17, B20, B28, B71) for rural and indoor coverage, and <b>mid bands</b> (1.7–2.6 GHz: B1, B2, B3, B4, B7, B66) for capacity. A device missing the carrier's low band may show "full bars" in the city and lose signal indoors or in the countryside. Read <a href="guide-lte-bands.html">LTE bands explained</a> for more.</p></div>
</div></section>{cta_band()}
""", scripts=("main", "tools"))

# ---------------------------------------------------------------- APN
reg("apn-settings.html", "APN Settings Finder — 4G LTE APN for Every Major Carrier", "Find the correct 4G LTE APN settings for T-Mobile, AT&T, Verizon, Rogers, Bell, EE, O2, Jio, Airtel, Telstra and more — with copy buttons and setup steps.",
    hero("APN settings finder", "The correct APN, username, password and MMSC for major carriers — tap to copy.", '<a href="tools.html">Tools</a> › APN Settings') + f"""
<section><div class="container">
  <div class="tool" id="apnfinder">
    <div class="row" style="display:grid;grid-template-columns:1fr 2fr;gap:14px">
      <div class="field"><label for="apn-country">Country</label><select id="apn-country"><option value="">All countries</option></select></div>
      <div class="field"><label for="apn-q">Search carrier</label><input id="apn-q" placeholder="e.g. Jio, EE, Rogers"></div>
    </div>
    <div class="table-wrap"><table class="table"><thead><tr><th>Country</th><th>Carrier</th><th>APN</th><th>Username</th><th>Password</th><th>APN type</th><th>MMSC</th></tr></thead><tbody id="apn-body"></tbody></table></div>
    <p class="meta">Most modern phones configure APNs automatically. Only change these if data isn't working. Settings can change — confirm with your carrier. Last updated {UPDATED}.</p>
  </div>
  {ad()}
  <div class="grid g2" style="margin-top:24px">
    <div class="card"><h3>Android</h3><p>Settings → Network &amp; Internet → SIMs → (your SIM) → Access Point Names → ＋. Enter the fields above, save, and select the new APN. Toggle airplane mode.</p></div>
    <div class="card"><h3>iPhone</h3><p>Settings → Cellular → Cellular Data Network (visible for many carriers/MVNOs). Enter the APN under Cellular Data and Personal Hotspot. Restart the phone.</p></div>
    <div class="card"><h3>4G/5G routers</h3><p>Log in to the router admin page (often 192.168.0.1 or 192.168.8.1) → Mobile/Dial-up → Profile management → New profile. Use IPv4v6 unless your carrier specifies otherwise.</p></div>
    <div class="card"><h3>Missing your carrier?</h3><form data-form="APN Request" data-success="Thanks! We'll add it to the database soon.">{honey()}<div class="field"><input name="carrier" required placeholder="Carrier & country"></div><div class="field"><input type="email" name="email" placeholder="Email (optional, to be notified)"></div><button class="btn btn-primary btn-sm" type="submit">Request APN</button><div class="form-msg" role="status"></div></form></div>
  </div>
</div></section>
""", scripts=("main", "tools"))

# ---------------------------------------------------------------- SIGNAL
reg("signal-analyzer.html", "4G LTE Signal Strength Analyzer (RSRP, RSRQ, SINR)", "Enter your RSRP, RSRQ and SINR readings to grade your 4G LTE signal and get practical fixes for weak or noisy signal.",
    hero("4G LTE signal strength analyzer", "Bars lie. Enter RSRP, RSRQ and SINR from your phone or router to get a real grade — and what to do about it.", '<a href="tools.html">Tools</a> › Signal Analyzer') + f"""
<section><div class="container" style="max-width:900px">
  <div class="tool" id="signal">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:14px">
      <div class="field"><label for="sig-rsrp">RSRP (dBm) *</label><input id="sig-rsrp" type="number" step="1" placeholder="-95"></div>
      <div class="field"><label for="sig-rsrq">RSRQ (dB)</label><input id="sig-rsrq" type="number" step="0.5" placeholder="-12"></div>
      <div class="field"><label for="sig-sinr">SINR (dB)</label><input id="sig-sinr" type="number" step="0.5" placeholder="8"></div>
    </div>
    <button class="btn btn-primary" id="sig-go">Analyze signal</button>
    <div class="result-box" id="sig-result" aria-live="polite"></div>
  </div>
  {ad()}
  <div class="prose">
    <h2>Reference ranges</h2>
    <div class="table-wrap"><table><tr><th>Grade</th><th>RSRP</th><th>RSRQ</th><th>SINR</th></tr>
    <tr><td class="v-good">Excellent</td><td>≥ −80 dBm</td><td>≥ −10 dB</td><td>≥ 20 dB</td></tr>
    <tr><td class="v-good">Good</td><td>−80 to −90</td><td>−10 to −15</td><td>13 to 20</td></tr>
    <tr><td class="v-mid">Fair</td><td>−90 to −100</td><td>−15 to −20</td><td>0 to 13</td></tr>
    <tr><td class="v-bad">Poor</td><td>&lt; −100</td><td>&lt; −20</td><td>&lt; 0</td></tr></table></div>
    <h2>Where to find these numbers</h2>
    <ul><li><b>Android:</b> Settings → About phone → SIM status → Signal strength (or a network-info app).</li><li><b>iPhone:</b> Field Test mode — dial <code>*3001#12345#*</code>, then open "Serving Cell Meas".</li><li><b>Routers:</b> admin page → Device information / Network / Signal.</li></ul>
    <p>Next step: <a href="guide-boost-signal.html">12 ways to boost a weak 4G signal</a>.</p>
  </div>
</div></section>{cta_band("Still weak after trying everything?", "Some addresses are better served by another carrier or fixed wireless. We'll check for you.", "get-matched.html?need=rural")}
""", scripts=("main", "tools"))

# ---------------------------------------------------------------- BANDWIDTH
def num(label, rate, val):
    return f'<div class="field"><label>{label}<input type="number" min="0" value="{val}" data-rate="{rate}"></label></div>'


reg("bandwidth-calculator.html", "Bandwidth Calculator — How Much Internet Speed Do I Need?", "Calculate how many Mbps your household or office needs for 4K streaming, gaming, video calls and working from home.",
    hero("How much internet speed do you need?", "Enter what happens at the same time on your connection at peak hour.", '<a href="tools.html">Tools</a> › Bandwidth Calculator') + f"""
<section><div class="container" style="max-width:900px">
  <div class="tool" id="bandwidth">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:4px 14px">
      {num("People browsing/social", "people", 2)}{num("4K streams at once", "uhd", 1)}{num("HD streams at once", "hd", 1)}{num("Video calls at once", "calls", 1)}
      {num("Gamers online", "gaming", 0)}{num("Remote workers", "wfh", 1)}{num("Smart-home devices", "iot", 10)}{num("Cloud backups / big uploads", "cloud", 0)}
    </div>
    <div class="result-box show center"><span class="muted">Recommended download speed</span><div style="font-size:3rem;font-weight:800" class="grad-text"><span id="bw-out">0</span> Mbps</div><p id="bw-tier" style="margin:0"></p></div>
    <p class="center" style="margin-top:16px"><a class="btn btn-primary" href="get-matched.html">Find plans with this speed →</a></p>
  </div>
  <p class="meta">Per-activity estimates: 4K 25 Mbps, HD 6, video call 4, gaming 5, remote work 10, browsing 2 per person; +30% headroom.</p>
  {ad()}
</div></section>
""", scripts=("main", "tools"))

# ---------------------------------------------------------------- DATA CALC
def dnum(label, key, val):
    return f'<div class="field"><label>{label}<input type="number" min="0" step="0.5" value="{val}" data-gbh="{key}"></label></div>'


reg("data-calculator.html", "Mobile Data Usage Calculator — GB per Month", "Estimate how many GB of mobile data you use per month from streaming, social media, video calls and browsing, and pick the right plan.",
    hero("Mobile data usage calculator", "Hours per day on each activity → GB per month. Pick the right data plan or eSIM pack.", '<a href="tools.html">Tools</a> › Data Calculator') + f"""
<section><div class="container" style="max-width:900px">
  <div class="tool" id="datacalc">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:4px 14px">
      {dnum("SD video (hrs/day)", "sd", 0.5)}{dnum("HD video (hrs/day)", "hd", 0.5)}{dnum("4K video (hrs/day)", "uhd", 0)}{dnum("Music streaming (hrs/day)", "music", 1)}
      {dnum("Social media (hrs/day)", "social", 1)}{dnum("Video calls (hrs/day)", "calls", 0.5)}{dnum("Web & email (hrs/day)", "web", 1)}{dnum("Online gaming (hrs/day)", "gaming", 0)}
    </div>
    <div class="grid g2"><div class="result-box show center"><span class="muted">Per day</span><div style="font-size:2.2rem;font-weight:800"><span id="dc-day">0</span> GB</div></div>
    <div class="result-box show center"><span class="muted">Per month</span><div style="font-size:2.2rem;font-weight:800" class="grad-text"><span id="dc-month">0</span> GB</div></div></div>
    <p class="center" id="dc-tip" style="margin-top:14px;font-weight:600"></p>
    <p class="center"><a class="btn btn-primary" href="plan-finder.html">Find a matching plan →</a> <a class="btn btn-ghost" href="esim.html">Travel eSIM packs</a></p>
  </div>
  <p class="meta">Estimates per hour: SD 0.7 GB, HD 3 GB, 4K 7 GB, music 0.15 GB, social 0.8 GB, video call 1.2 GB, web 0.08 GB, gaming 0.1 GB.</p>
  {ad()}
</div></section>
""", scripts=("main", "tools"))

# ---------------------------------------------------------------- PLAN FINDER
def radios(name, opts):
    return "".join(f'<label class="choice"><input type="radio" name="{name}" value="{v}"><span><i>{i}</i>{t}</span></label>' for v, i, t in opts)


reg("plan-finder.html", "Plan Finder Quiz — Best 4G/5G Plan Type for You", "Answer three questions to find the best mobile, home internet, travel eSIM or business connectivity plan type for your needs and budget.",
    hero("Find your ideal plan in 3 questions", "No sign-up. Instant recommendation.", '<a href="tools.html">Tools</a> › Plan Finder') + f"""
<section><div class="container" style="max-width:900px"><div class="tool" id="planquiz">
  <h3>1. What's it for?</h3><div class="choice-grid">{radios("pq_use", [("phone", "📱", "My phone"), ("home", "🏠", "Home internet"), ("travel", "✈️", "Travel"), ("business", "🏢", "Business"), ("rv", "🚐", "RV / van life")])}</div>
  <h3>2. How much data?</h3><div class="choice-grid">{radios("pq_data", [("light", "🌱", "Light (<10 GB)"), ("medium", "🌿", "Medium (10–50 GB)"), ("heavy", "🌳", "Heavy (50 GB+)")])}</div>
  <h3>3. Budget?</h3><div class="choice-grid">{radios("pq_budget", [("low", "💵", "Keep it cheap"), ("mid", "💳", "Balanced"), ("high", "💎", "Best available")])}</div>
  <button class="btn btn-primary" id="pq-go">See my match</button>
  <div class="result-box" id="pq-result" aria-live="polite"></div>
</div>{ad()}</div></section>
""", scripts=("main", "tools"))
