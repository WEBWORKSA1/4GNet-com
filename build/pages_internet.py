from layout import page, hero, ad, faq, honey, consent, cta_band, UPDATED
from pages_core import PAGES, reg, lead_form

# ---------------------------------------------------------------- HOME INTERNET
hi_faq, hi_ld = faq([
    ("Is 4G/5G home internet unlimited?", "Most dedicated home-internet plans advertise no hard data cap, but many can deprioritise home users behind phone users during congestion. Check the plan's network-management policy."),
    ("Can I use my phone's hotspot instead?", "For light use, yes. But phone plans usually cap hotspot data (often 5–50 GB at full speed) and phones throttle when hot. A dedicated router with better antennas is more reliable."),
    ("Do I need an outdoor antenna?", "If your indoor RSRP is worse than about −100 dBm or SINR below 5 dB, an outdoor or window-mounted MIMO antenna usually delivers the single biggest improvement."),
])
reg("home-internet.html", "4G LTE & 5G Home Internet — Compare Wireless Home Internet", "Compare 4G LTE and 5G home internet: speeds, prices, data policies and equipment. Check availability at your address and get matched free.",
    hero("4G LTE &amp; 5G home internet", "Plug-and-play wireless broadband with no cable install. Compare options at your address.", "Home Internet") + f"""
<section><div class="container"><div class="layout"><div class="prose">
  <h2>Is wireless home internet right for you?</h2>
  <p>Fixed wireless access (FWA) uses the same 4G LTE and 5G networks as your phone, delivered through a dedicated indoor or outdoor router. It has become one of the fastest-growing ways to get broadband because it installs in minutes, rarely needs a contract, and often costs less than cable.</p>
  <div class="table-wrap"><table><tr><th></th><th>4G LTE home</th><th>5G home</th><th>Cable</th><th>Fiber</th></tr>
  <tr><td>Typical download</td><td>15–100 Mbps</td><td>100–400 Mbps</td><td>100–1000 Mbps</td><td>300–5000 Mbps</td></tr>
  <tr><td>Typical upload</td><td>3–20 Mbps</td><td>10–50 Mbps</td><td>10–50 Mbps</td><td>Symmetrical</td></tr>
  <tr><td>Install</td><td>Self, minutes</td><td>Self, minutes</td><td>Technician</td><td>Technician</td></tr>
  <tr><td>Contract</td><td>Usually none</td><td>Usually none</td><td>Often</td><td>Sometimes</td></tr>
  <tr><td>Best for</td><td>1–3 people, rural</td><td>Families, cord-cutters</td><td>Heavy use</td><td>Everything</td></tr></table></div>
  <h2>Checklist before you order</h2>
  <ul class="list-check"><li>Run our <a href="speed-test.html">speed test</a> on your phone from the room where the router will sit.</li><li>Confirm the plan's data-management policy (priority vs. deprioritised).</li><li>Check upload speed if you work from home or stream to others.</li><li>Ask about the trial/return window — 15–30 days is common.</li><li>If signal is marginal, budget for a window or outdoor antenna.</li></ul>
  {ad()}
  <h2>FAQ</h2>{hi_faq}
</div><aside class="sidebar"><div class="card"><h3>Check availability</h3><p>Get the providers that serve your address.</p><a class="btn btn-primary btn-block" style="margin-top:12px" href="get-matched.html?need=home">Get matched →</a></div>{ad("sidebar")}</aside></div></div></section>
<section class="section-alt"><div class="container" style="max-width:900px"><h2 class="center">Get free home internet quotes</h2>{lead_form("home")}</div></section>
""", schema=hi_ld)

# ---------------------------------------------------------------- RURAL
reg("rural-internet.html", "Rural Internet Options — 4G LTE, Fixed Wireless & Satellite", "Best rural internet options compared: 4G/5G with external antennas, fixed wireless, LEO and GEO satellite, and DSL. Get matched with rural providers.",
    hero("Rural internet that actually works", "No cable, no fiber? You still have real options. Compare them honestly.", "Rural Internet") + f"""
<section><div class="container"><div class="layout"><div class="prose">
  <h2>Your rural options, ranked by what usually works best</h2>
  <ol>
  <li><b>5G/4G home internet + outdoor antenna.</b> If any carrier reaches you with RSRP better than about −110 dBm outdoors, a directional antenna on a mast can turn "one bar" into 20–100 Mbps.</li>
  <li><b>Local fixed-wireless ISP (WISP).</b> Regional providers beam internet from towers or silos to a dish on your roof. Latency is low and plans are often unlimited.</li>
  <li><b>Low-Earth-orbit (LEO) satellite.</b> Available almost anywhere with a clear sky view; 50–250 Mbps and low latency, but higher equipment cost.</li>
  <li><b>Geostationary satellite.</b> Wide availability, but ~600 ms latency makes gaming and calls difficult; data policies can be restrictive.</li>
  <li><b>DSL.</b> Usable only close to the exchange; often under 10 Mbps in rural areas.</li></ol>
  <div class="callout"><b>Pro tip:</b> Test every carrier. The best rural network varies by valley and hill. A $10 prepaid SIM from each carrier is the cheapest site survey you'll ever do.</div>
  <h2>Antenna quick guide</h2>
  <div class="table-wrap"><table><tr><th>Antenna</th><th>Gain</th><th>Use when</th></tr><tr><td>Window MIMO panel</td><td>6–10 dBi</td><td>Signal fair indoors, tower direction known</td></tr><tr><td>Outdoor directional (Yagi/LPDA)</td><td>9–13 dBi</td><td>Distant single tower</td></tr><tr><td>Outdoor omni</td><td>3–7 dBi</td><td>Multiple towers, vehicles</td></tr><tr><td>Parabolic grid</td><td>18–24 dBi</td><td>Very distant tower, line of sight</td></tr></table></div>
  {ad()}
</div><aside class="sidebar"><div class="card"><h3>Stuck with slow internet?</h3><p>Tell us where you are — we'll check carriers, WISPs and satellite for your location.</p><a class="btn btn-primary btn-block" style="margin-top:12px" href="get-matched.html?need=rural">Check rural options →</a></div></aside></div></div></section>
<section class="section-alt"><div class="container" style="max-width:900px"><h2 class="center">Get rural internet quotes</h2>{lead_form("rural")}</div></section>
""")

# ---------------------------------------------------------------- BUSINESS
reg("business.html", "Business 4G/5G Internet, Failover & IoT Connectivity", "4G/5G business internet, LTE failover for POS and VoIP, bonded SD-WAN, and IoT/M2M SIMs for fleets and devices. Request a free B2B connectivity quote.",
    hero("Business wireless: primary, failover &amp; IoT", "Keep every site, terminal and vehicle online. Independent sourcing across carriers and hardware vendors.", "Business &amp; IoT") + f"""
<section><div class="container">
  <div class="grid g3">
    <div class="card"><div class="ic">🛡️</div><h3>4G/5G failover</h3><p>Automatic backup for when fiber or cable drops. Protect card payments, VoIP and cloud apps. Typical switchover in seconds.</p></div>
    <div class="card"><div class="ic">🚀</div><h3>Primary 5G &amp; pop-up sites</h3><p>Construction sites, events, kiosks and new branches online in days — not the weeks a wired circuit takes.</p></div>
    <div class="card"><div class="ic">📡</div><h3>IoT / M2M SIMs</h3><p>Multi-network SIMs, pooled data, LTE-M/NB-IoT for trackers, sensors, vending, telematics and signage.</p></div>
    <div class="card"><div class="ic">🔗</div><h3>Bonded SD-WAN</h3><p>Combine multiple carriers plus wired links for resilience and throughput with a single policy.</p></div>
    <div class="card"><div class="ic">🚚</div><h3>Fleet &amp; vehicle Wi-Fi</h3><p>Rugged routers with GPS, dual SIM and roof antennas for buses, trucks and emergency vehicles.</p></div>
    <div class="card"><div class="ic">🧾</div><h3>Bill audit</h3><p>Send us your current telecom bill; we'll benchmark it against current business pricing.</p></div>
  </div>
</div></section>
{ad()}
<section class="section-alt"><div class="container"><div class="layout">
  <div><span class="eyebrow">B2B quote</span><h2>Request a business connectivity proposal</h2>
  <form class="tool" data-form="Lead - Business/IoT" data-success="Thanks! A B2B connectivity specialist will respond within 1 business day.">
    {honey()}
    <div class="row"><div class="field"><label>Company name<input name="company" required autocomplete="organization"></label></div><div class="field"><label>Your name<input name="name" required autocomplete="name"></label></div></div>
    <div class="row"><div class="field"><label>Work email<input type="email" name="email" required autocomplete="email"></label></div><div class="field"><label>Phone<input type="tel" name="phone" autocomplete="tel"></label></div></div>
    <div class="row"><div class="field"><label>Solution<select name="solution"><option>4G/5G failover</option><option>Primary 5G internet</option><option>IoT / M2M SIMs</option><option>Fleet / vehicle</option><option>SD-WAN / bonded</option><option>Bill audit</option><option>Other</option></select></label></div>
    <div class="field"><label>Number of sites / devices<select name="scale"><option>1</option><option>2–5</option><option>6–25</option><option>26–100</option><option>100–1,000</option><option>1,000+</option></select></label></div></div>
    <div class="row"><div class="field"><label>Country / region<input name="region" required></label></div><div class="field"><label>Timeline<select name="timeline"><option>ASAP</option><option>This quarter</option><option>Next 6 months</option><option>Budgeting</option></select></label></div></div>
    <div class="field"><label>Monthly budget (approx.)<select name="budget"><option>Under $250</option><option>$250–$1,000</option><option>$1,000–$5,000</option><option>$5,000+</option></select></label></div>
    <div class="field"><label>Requirements<textarea name="requirements" placeholder="Current ISP, uptime targets, data per SIM, hardware preferences…"></textarea></label></div>
    {consent()}
    <button class="btn btn-primary" type="submit" style="margin-top:12px">Request proposal</button>
    <div class="form-msg" role="status"></div>
  </form></div>
  <aside class="sidebar"><div class="card"><h3>Why businesses use us</h3><ul class="list-check"><li>Carrier-neutral recommendations</li><li>Hardware + SIM + plan in one proposal</li><li>Multi-country IoT sourcing</li><li>Response within 1 business day</li></ul></div>{ad("sidebar")}</aside>
</div></div></section>
""")

# ---------------------------------------------------------------- ESIM
es_faq, es_ld = faq([
    ("Does my phone support eSIM?", "Most flagship phones since around 2019 do, including recent iPhones, Pixels and Galaxy S models. On iPhone check Settings → Cellular → Add eSIM; on Android, Settings → SIMs → Add eSIM. Carrier-locked phones may block third-party eSIMs."),
    ("Will I keep my WhatsApp and number?", "Yes. Keep your home SIM active for calls/SMS (turn off its data roaming) and use the travel eSIM for data. WhatsApp stays tied to your number."),
    ("When should I install the eSIM?", "Install it before you fly while you have Wi-Fi, but only activate it (or let validity start) when you land, depending on the provider's rules."),
    ("Can I hotspot from a travel eSIM?", "Many allow it, some don't. Check the plan's tethering policy before buying if you'll share data with a laptop."),
])
prov = [("airalo", "Airalo", "Huge destination catalogue, low-cost small packs, regional and global plans.", "Short trips, budget travellers"),
        ("holafly", "Holafly", "Unlimited-data style plans for many countries; subscriptions available.", "Heavy users who don't want to track GB"),
        ("saily", "Saily", "Simple app with security features; flexible data packs.", "Security-conscious travellers"),
        ("nomad", "Nomad", "Transparent price-per-GB packs with top-ups.", "Value seekers, multi-country trips"),
        ("esimdb", "eSIMDB (comparison)", "Search engine across hundreds of eSIM brands and plans.", "Finding the absolute cheapest plan")]
cards = "".join(f'<div class="card"><span class="tag">Partner</span><h3>{n}</h3><p>{d}</p><p style="margin:10px 0"><b>Best for:</b> <span class="muted">{b}</span></p><a class="btn btn-primary btn-sm" data-aff="{k}" href="#">Check prices →</a></div>' for k, n, d, b in prov)
reg("esim.html", "Best Travel eSIM — Compare eSIM Data Plans by Destination", "Compare travel eSIM providers for 190+ destinations: data packs, unlimited plans, validity, hotspot rules and device compatibility.",
    hero("Travel eSIM comparison", "Land connected in 190+ countries. Compare providers, then buy direct.", "Travel eSIM") + f"""
<section><div class="container">
  <div class="callout" style="margin-top:0">Affiliate disclosure: we may earn a commission when you buy through these links, at no extra cost to you. Prices change daily — always confirm on the provider's site. <a href="disclosure.html">Learn more</a>.</div>
  <div class="grid g3">{cards}</div>
</div></section>
{ad()}
<section class="section-alt"><div class="container"><div class="layout"><div class="prose">
  <h2>How to choose a travel eSIM</h2>
  <div class="table-wrap"><table><tr><th>Trip type</th><th>What to buy</th><th>Typical data</th></tr>
  <tr><td>Weekend city break</td><td>Country pack, 7 days</td><td>1–3 GB</td></tr><tr><td>1–2 week holiday</td><td>Country or regional pack</td><td>5–10 GB</td></tr>
  <tr><td>Multi-country Europe/Asia</td><td>Regional plan</td><td>10–20 GB</td></tr><tr><td>Digital nomad / remote work</td><td>Unlimited or 50 GB+ with hotspot</td><td>50 GB+</td></tr></table></div>
  <p>Not sure how much you need? Use the <a href="data-calculator.html">data usage calculator</a>. Planning to use a travel router? Check its bands with the <a href="band-checker.html">band checker</a>.</p>
  <h2>FAQ</h2>{es_faq}
</div><aside class="sidebar"><div class="card"><h3>Need a group or business plan?</h3><p>Teams, tour operators and fleets: get pooled multi-country data.</p><a class="btn btn-primary btn-block" style="margin-top:12px" href="get-matched.html?need=travel">Request a quote →</a></div></aside></div></div></section>
""", schema=es_ld)

# ---------------------------------------------------------------- ROUTERS
reg("routers.html", "Best 4G LTE & 5G Routers and Hotspots — Buying Guide", "How to choose a 4G LTE or 5G router or mobile hotspot: LTE category, 5G bands, Wi-Fi 6/7, external antenna ports, dual SIM and more.",
    hero("4G/5G routers &amp; hotspots buying guide", "Specs that actually matter — and the ones marketing exaggerates.", "Routers &amp; Hotspots") + f"""
<section><div class="container"><div class="layout"><div class="prose">
  <h2>Pick the right class of device</h2>
  <div class="table-wrap"><table><tr><th>Use case</th><th>Device class</th><th>Look for</th></tr>
  <tr><td>Travel / commuting</td><td>Pocket hotspot</td><td>Battery 8+ hrs, eSIM or unlocked, global bands</td></tr>
  <tr><td>Apartment, good signal</td><td>Indoor 4G Cat 6+ or 5G gateway</td><td>Carrier aggregation, Wi-Fi 6, Ethernet ports</td></tr>
  <tr><td>House, fair/weak signal</td><td>Indoor router with antenna ports</td><td>2×/4× SMA or TS-9 ports, MIMO, band locking</td></tr>
  <tr><td>Rural / farm</td><td>Outdoor (ODU) 5G/4G unit</td><td>IP65+, PoE, high-gain integrated antenna</td></tr>
  <tr><td>RV / boat / fleet</td><td>Vehicle router</td><td>12V input, dual SIM, GPS, roof antenna</td></tr>
  <tr><td>Business failover</td><td>Enterprise router</td><td>Auto failover, dual modem, VPN, remote management</td></tr></table></div>
  <h2>Spec cheat sheet</h2>
  <ul><li><b>LTE Category:</b> Cat 4 (150 Mbps max) is basic; Cat 6/12/18/20 add carrier aggregation for 300 Mbps–2 Gbps theoretical.</li>
  <li><b>5G bands:</b> ensure your carrier's n-bands (e.g. n41, n71, n77, n78) are listed — not just "5G".</li>
  <li><b>SA vs NSA:</b> standalone 5G support future-proofs the device.</li>
  <li><b>Antenna ports:</b> the cheapest upgrade path if signal is weak.</li>
  <li><b>Wi-Fi:</b> Wi-Fi 6 is the sensible minimum; Wi-Fi 7 helps only if your wireless link exceeds ~500 Mbps.</li>
  <li><b>Unlocked:</b> carrier-locked devices can't switch networks — check before buying used.</li></ul>
  <div class="callout">We don't take payment for rankings. When we link to retailers we may earn a commission — see our <a href="disclosure.html">disclosure</a>.</div>
  {ad()}
</div><aside class="sidebar"><div class="card"><h3>Want a recommendation?</h3><p>Tell us your address and use-case; we'll suggest hardware + plan together.</p><a class="btn btn-primary btn-block" style="margin-top:12px" href="get-matched.html">Get matched →</a></div>{ad("sidebar")}</aside></div></div></section>
""")
