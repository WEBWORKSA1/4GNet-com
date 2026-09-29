from layout import page, hero, ad, faq, cta_band, video, VIDEOS, UPDATED
from pages_core import reg

GUIDES = []


def guide(fn, title, desc, tag, body, vid=None, faqs=None):
    GUIDES.append((fn, title, desc, tag))
    f_html, f_ld = faq(faqs) if faqs else ("", None)
    art = {"@context": "https://schema.org", "@type": "Article", "headline": title, "description": desc,
           "author": {"@type": "Organization", "name": "4GNet Editorial Team"}, "dateModified": "2026-09-29"}
    v = video(*vid) if vid else ""
    reg(fn, title, desc, hero(title, desc, f'<a href="learn.html">Learn</a> › {tag}') + f"""
<section><div class="container"><div class="layout"><article class="prose">
<p class="meta">By the 4GNet Editorial Team · Updated {UPDATED} · <a href="about.html">Methodology</a></p>
{body}
{('<h2>Watch</h2>' + v) if v else ''}
{ad()}
{('<h2>FAQ</h2>' + f_html) if f_html else ''}
</article>
<aside class="sidebar"><div class="card"><h3>Free tools</h3><div class="toc"><a href="speed-test.html">⚡ Speed test</a><a href="band-checker.html">📶 Band checker</a><a href="signal-analyzer.html">📡 Signal analyzer</a><a href="apn-settings.html">⚙️ APN settings</a><a href="data-calculator.html">📊 Data calculator</a></div>
<a class="btn btn-primary btn-block" style="margin-top:14px" href="get-matched.html">Get matched free →</a></div>{ad("sidebar")}</aside></div></div></section>
{cta_band()}""", schema=[art] + ([f_ld] if f_ld else []))


guide("guide-4g-vs-5g.html", "4G vs 5G: The Real-World Differences in 2026", "Speed, latency, coverage, battery and cost — what actually changes when you move from 4G LTE to 5G, and when 4G is still the better choice.", "4G vs 5G", """
<p><b>Short answer:</b> 5G is faster and more responsive where it's deployed on mid-band spectrum, but 4G LTE still carries a large share of traffic worldwide and often has better coverage indoors and in rural areas. Most 5G phones and routers seamlessly fall back to 4G, so the practical question isn't "4G or 5G" — it's which bands and which network work best where you are.</p>
<h2>The three "flavours" of 5G</h2>
<div class="table-wrap"><table><tr><th>Type</th><th>Spectrum</th><th>Real-world speed</th><th>Coverage</th></tr>
<tr><td>Low-band 5G</td><td>600–900 MHz (n71, n5, n28)</td><td>Often similar to good 4G: 50–150 Mbps</td><td>Very wide</td></tr>
<tr><td>Mid-band 5G</td><td>2.5–4.2 GHz (n41, n77, n78)</td><td>150–800 Mbps</td><td>City + suburbs, growing</td></tr>
<tr><td>mmWave 5G</td><td>24–40 GHz (n258, n260, n261)</td><td>1–3 Gbps</td><td>Stadiums, dense downtowns, line of sight</td></tr></table></div>
<p>If a carrier's "5G" icon appears but speeds look like 4G, you're probably on low-band 5G or non-standalone 5G sharing capacity with LTE.</p>
<h2>Latency and responsiveness</h2>
<p>Good 4G networks deliver 30–60 ms latency; mid-band 5G typically 15–35 ms. The gap matters for cloud gaming, video calls and remote desktop. For streaming video, the difference is barely noticeable because video buffers ahead.</p>
<h2>Coverage: where 4G still wins</h2>
<p>Higher frequencies carry more data but travel less far and penetrate walls poorly. That's why a 4G LTE signal on band 12, 13, 20 or 28 can hold up in a basement or a valley where mid-band 5G has already dropped. In rural areas, a strong 4G signal often beats a weak 5G one.</p>
<h2>Battery and heat</h2>
<p>Early 5G modems drew noticeably more power. Current-generation chipsets have narrowed the gap, but weak 5G signal still drains batteries faster as the phone hunts between networks. If battery life matters more than speed, setting "LTE only" or "5G Auto" can help.</p>
<h2>Should you upgrade?</h2>
<ul class="list-check"><li><b>Upgrade</b> if mid-band 5G is available where you spend most time and you stream 4K, game, or work from home over mobile.</li><li><b>Upgrade</b> if you're replacing a device anyway — nearly all new phones are 5G.</li><li><b>Stay on 4G</b> if your area has only low-band 5G and your current device supports the carrier's core LTE bands.</li><li><b>Consider 5G home internet</b> if you're on slow DSL or 4G home internet and mid-band 5G reaches your address.</li></ul>
<p>Test it yourself: run our <a href="speed-test.html">speed test</a> with 5G on and off, and compare.</p>
""", vid=VIDEOS[2], faqs=[("Will 4G be shut down?", "Not soon in most markets. Carriers are shutting 2G and 3G first. 4G LTE is expected to remain for many years because it carries voice (VoLTE) and provides fallback coverage."),
                          ("Is 5G safe?", "5G uses non-ionising radio frequencies within international exposure guidelines set by bodies such as ICNIRP; health agencies including the WHO have found no established health effects at these levels.")])

guide("guide-lte-bands.html", "LTE Bands Explained: Why Your Phone Works in One Place and Not Another", "A plain-English guide to 4G LTE frequency bands, FDD vs TDD, carrier aggregation, and why low bands matter for coverage.", "LTE Bands", """
<p>Every 4G LTE network is built on numbered <b>bands</b> — slices of radio spectrum licensed to carriers. Your phone must support the bands your carrier uses, or it will get poor coverage (or none at all), even if the phone is "unlocked" and "4G".</p>
<h2>Low, mid and high bands</h2>
<div class="table-wrap"><table><tr><th>Group</th><th>Example bands</th><th>Frequency</th><th>Strength</th></tr>
<tr><td>Low band</td><td>B5, B8, B12, B13, B17, B20, B28, B71</td><td>600–900 MHz</td><td>Long range, great indoors, lower capacity</td></tr>
<tr><td>Mid band</td><td>B1, B2, B3, B4, B66, B25</td><td>1.7–2.1 GHz</td><td>Balance of range and capacity</td></tr>
<tr><td>Upper mid</td><td>B7, B38, B40, B41</td><td>2.3–2.7 GHz</td><td>High capacity, shorter range</td></tr>
<tr><td>Shared/unlicensed</td><td>B46 (LAA), B48 (CBRS)</td><td>3.5–5 GHz</td><td>Extra capacity in busy areas</td></tr></table></div>
<h2>FDD vs TDD</h2>
<p><b>FDD</b> bands (like B3 or B20) use separate frequencies for upload and download. <b>TDD</b> bands (like B40 or B41) share one frequency and alternate in time. Both are "4G" — your device simply needs to list them.</p>
<h2>Carrier aggregation (CA)</h2>
<p>LTE-Advanced combines two or more bands at once — for example B3 + B7 + B20 — to multiply speed. Devices advertise this as a higher LTE "Category" (Cat 6, 12, 18, 20…). A Cat 4 device can't aggregate and tops out at 150 Mbps theoretical.</p>
<h2>Regional differences</h2>
<p>North America leans on B2, B4, B12, B13, B66 and B71; Europe and much of Asia and Africa on B1, B3, B7, B8 and B20; India heavily on B3, B5 (Jio), B40 and B41; Japan on B1, B3, B19, B21 and B28. That's why a phone bought in one region can struggle in another — model variants support different sets.</p>
<p><a class="btn btn-primary btn-sm" href="band-checker.html">Check your device against a carrier →</a></p>
""", vid=VIDEOS[0], faqs=[("How do I know which band I'm connected to?", "On Android, network-info apps show the active band. On iPhone, Field Test mode (*3001#12345#*) shows the frequency channel (EARFCN), which maps to a band."),
                          ("Can I lock my router to a band?", "Many 4G/5G routers support band locking in the admin panel. Locking to a less congested or stronger band can improve stability, but test carefully.")])

guide("guide-boost-signal.html", "12 Proven Ways to Boost a Weak 4G/5G Signal", "From free placement tricks to antennas, band locking and boosters — how to improve weak 4G LTE and 5G signal at home, in the car and in rural areas.", "Boost Signal", """
<p>Before spending money, measure. Note your RSRP and SINR (see the <a href="signal-analyzer.html">signal analyzer</a>) and run a <a href="speed-test.html">speed test</a>. Change one thing at a time and re-measure.</p>
<h2>Free fixes</h2>
<ol><li><b>Move up and to a window.</b> Each floor and each wall costs signal. Upper-floor windows facing the tower can gain 10–20 dB.</li>
<li><b>Find the tower.</b> Crowd-sourced tower maps show likely sites. Point the router's flat face toward it.</li>
<li><b>Avoid metal and low-E glass.</b> Foil-backed insulation, metal roofs and coated windows block signal. Try a different window.</li>
<li><b>Restart and update.</b> Firmware updates often improve modem performance and add bands.</li>
<li><b>Toggle network mode.</b> On weak 5G, forcing LTE can be more stable; on congested LTE, 5G may be faster.</li>
<li><b>Test off-peak.</b> If speed recovers at 6 a.m., the problem is congestion, not signal.</li></ol>
<h2>Low-cost upgrades</h2>
<ol start="7"><li><b>Band locking.</b> Lock a router to the band with the best SINR, not just the strongest RSRP.</li>
<li><b>Window MIMO antenna.</b> Two-port panel antennas stuck to glass typically add 5–10 dB.</li>
<li><b>Outdoor directional antenna.</b> Mounted high and aimed at the tower — often the biggest single improvement. Keep cable runs short and low-loss.</li>
<li><b>Outdoor 5G/4G unit (ODU).</b> Puts the modem outside with the antenna; runs Ethernet/PoE inside — no cable loss.</li></ol>
<h2>Bigger options</h2>
<ol start="11"><li><b>Certified signal booster.</b> Amplifies outside signal indoors. Buy only carrier-approved/regulator-certified models; improper boosters can interfere with networks and are illegal in some countries.</li>
<li><b>Switch carrier or technology.</b> Sometimes the answer is a different network, fixed wireless, or satellite. <a href="get-matched.html?need=rural">We can check your address.</a></li></ol>
""", vid=VIDEOS[8], faqs=[("Do phone signal booster stickers work?", "No. Passive stickers and 'antenna boosters' that attach to phones have no measurable effect."),
                          ("Are Wi-Fi calling and signal boosting the same?", "No. Wi-Fi calling routes calls over your internet connection instead of the cell network — a good fix for weak indoor signal if you have broadband.")])

guide("guide-esim.html", "eSIM Explained: How It Works, Pros, Cons and Travel Tips", "What an eSIM is, how to install and switch profiles, which devices support it, and how to save money with travel eSIMs.", "eSIM", """
<p>An <b>eSIM</b> is a SIM card built into your device's hardware. Instead of inserting plastic, you download a carrier "profile" by scanning a QR code or through an app. Most eSIM phones store several profiles and can use two lines at once (dual SIM).</p>
<h2>Advantages</h2>
<ul class="list-check"><li>Switch carriers or add a travel plan in minutes, without a store visit</li><li>Keep your home number active while using local data abroad</li><li>No SIM tray to lose or swap; harder for thieves to remove</li><li>Great for tablets, laptops and watches</li></ul>
<h2>Drawbacks</h2>
<ul><li>Moving a line to a new phone can require carrier steps or support.</li><li>Carrier-locked devices may refuse third-party eSIMs.</li><li>Some budget or regional phone models lack eSIM.</li></ul>
<h2>How to install a travel eSIM</h2>
<ol><li>Confirm your phone is unlocked and supports eSIM.</li><li>Buy a plan for your destination (see our <a href="esim.html">eSIM comparison</a>).</li><li>Install it on Wi-Fi before departure; label it "Travel".</li><li>On arrival: set the travel eSIM as the data line and enable roaming <i>on that eSIM only</i>.</li><li>Keep your home line on for calls/SMS, but turn off its data roaming to avoid charges.</li></ol>
<div class="callout">iSIM is the next step: the SIM function is integrated into the device's main chip, saving space and power — especially for IoT devices.</div>
""", vid=VIDEOS[5], faqs=[("Can I use eSIM and a physical SIM together?", "Yes, on most dual-SIM phones. One line can be physical and the other eSIM."),
                          ("Is an eSIM more secure?", "It can't be physically removed, which helps if your phone is stolen, but you should still set a SIM PIN and strong device lock.")])

guide("guide-choose-router.html", "How to Choose a 4G/5G Router: 2026 Checklist", "A step-by-step checklist for choosing a 4G LTE or 5G router or gateway for home, rural, RV or business use.", "Choosing a Router", """
<p>The right router depends on three things: <b>your signal</b>, <b>your carrier's bands</b>, and <b>where you'll use it</b>. Here's the order to decide in.</p>
<h2>1. Measure your signal first</h2><p>Use a phone on the same carrier to record RSRP and SINR where the router will go. Excellent/good signal → any indoor router works. Fair/poor → prioritise antenna ports or an outdoor unit.</p>
<h2>2. Match the bands</h2><p>Compare the router's LTE and 5G band list with your carrier's using our <a href="band-checker.html">band checker</a>. Missing the low band is the most common cause of disappointment.</p>
<h2>3. Choose the modem class</h2><ul><li>LTE Cat 4: basic, fine for 1–2 people</li><li>LTE Cat 6–12: carrier aggregation, good value</li><li>LTE Cat 18–20 or 5G: households, WFH, streaming 4K</li><li>5G SA-capable: future-proof</li></ul>
<h2>4. Check Wi-Fi and ports</h2><p>Wi-Fi 6 minimum, at least one gigabit Ethernet port (two if you want a mesh system), and ideally a WAN port to use it as failover for wired internet.</p>
<h2>5. Unlocked vs carrier-supplied</h2><p>Carrier gateways are free or cheap but locked and often limited in settings. Unlocked routers cost more but let you change carriers, lock bands and add antennas.</p>
<h2>6. Extras that matter for specific cases</h2><ul><li>RV/boat: 12V input, GPS, dual SIM</li><li>Business: dual modem, VPN, remote management, failover</li><li>Travel: battery hotspot with eSIM support</li></ul>
<p>Next: see our <a href="routers.html">routers &amp; hotspots guide</a>.</p>
""", vid=VIDEOS[9])

guide("guide-rural-internet.html", "Rural Internet Options Compared: LTE, Fixed Wireless and Satellite", "An honest comparison of rural broadband options: 4G/5G with antennas, WISPs, LEO and GEO satellite and DSL — speed, latency, cost and reliability.", "Rural Internet", """
<p>Rural broadband is about trade-offs. The right answer depends on line of sight, the nearest towers and how you use the internet.</p>
<div class="table-wrap"><table><tr><th>Option</th><th>Speed</th><th>Latency</th><th>Upfront cost</th><th>Watch out for</th></tr>
<tr><td>4G/5G + antenna</td><td>10–300 Mbps</td><td>30–60 ms</td><td>Low–medium</td><td>Tower congestion, deprioritisation</td></tr>
<tr><td>Fixed wireless ISP</td><td>25–500 Mbps</td><td>10–40 ms</td><td>Low–medium</td><td>Needs line of sight to the provider's tower</td></tr>
<tr><td>LEO satellite</td><td>50–250 Mbps</td><td>25–60 ms</td><td>Medium–high</td><td>Clear sky view needed; equipment cost</td></tr>
<tr><td>GEO satellite</td><td>25–150 Mbps</td><td>550–700 ms</td><td>Low</td><td>High latency; data policies</td></tr>
<tr><td>DSL</td><td>1–25 Mbps</td><td>20–50 ms</td><td>Low</td><td>Distance from exchange</td></tr></table></div>
<h2>Decision tree</h2>
<ol><li>Does any carrier give you RSRP better than −110 dBm outdoors at roof height? → Try 4G/5G with an outdoor antenna.</li><li>Is there a WISP tower visible from your roof? → Get a WISP survey (often free).</li><li>Neither? → LEO satellite is typically the best performer; GEO if budget is the priority.</li><li>Need 99.9% uptime (farm business, remote work)? → Combine two: e.g. LTE + satellite with an automatic failover router.</li></ol>
<p>Let us check your address: <a href="get-matched.html?need=rural">get rural options →</a></p>
""", vid=VIDEOS[7])

# ---------------------------------------------------------------- LEARN HUB
cards = "".join(f'<a class="card" href="{fn}"><span class="tag">{tag}</span><h3>{t}</h3><p>{d}</p></a>' for fn, t, d, tag in GUIDES)
reg("learn.html", "Learn — 4G, 5G, LTE & eSIM Guides", "Independent, plain-English guides to 4G LTE, 5G, LTE bands, signal boosting, eSIM, routers and rural internet.",
    hero("Wireless guides, minus the jargon", "Independent explainers written to help you decide — not to sell you.", "Learn") +
    f'<section><div class="container"><div class="grid g3">{cards}</div></div></section>{ad()}{cta_band()}')

# ---------------------------------------------------------------- VIDEOS
reg("videos.html", "Video Hub — 4G, 5G, eSIM & Router Explainers", "Curated videos explaining 4G LTE, 5G, eSIM, how cell towers work and how to choose a 4G/5G router.",
    hero("Video hub", "Curated explainers from respected creators. Click to play — videos load only when you choose.", "Videos") + f"""
<section><div class="container"><div class="grid g3">{"".join(video(*v) for v in VIDEOS)}</div>
<p class="meta" style="margin-top:20px">Videos are embedded from YouTube and remain the property of their creators. Embedding does not imply endorsement. Want your video featured? <a href="contact.html">Suggest one</a>.</p></div></section>
{ad()}
<section class="section-alt"><div class="container center"><h2>Creators: partner with 4GNet</h2><p class="muted">We sponsor reviews, speed-test challenges and explainers. Talk to us about collaborations.</p><a class="btn btn-primary" href="advertise.html">Partner with us</a> <a class="btn btn-ghost" href="careers.html">Join as a video creator</a></div></section>
""")
