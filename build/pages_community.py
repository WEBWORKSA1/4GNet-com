from layout import page, hero, ad, faq, honey, consent, cta_band, UPDATED, INTEREST
from pages_core import reg

# ---------------------------------------------------------------- SUPPORT / DONATE
alloc = [("Operations — servers, test infrastructure, data licences", 35), ("Promotion & marketing — reaching people stuck on slow internet", 25),
         ("Hiring talent — writers, video creators, developers", 25), ("Contests & prizes — community rewards", 15)]
alloc_html = "".join(f'<div><div style="display:flex;justify-content:space-between;font-weight:600"><span>{t}</span><span>{p}%</span></div><div class="bar"><i style="width:{p}%"></i></div></div>' for t, p in alloc)
tiers = [("Supporter", 5, "🌱", ["Name on supporters wall (optional)", "Monthly thank-you update"], False),
         ("Booster", 25, "🚀", ["Everything in Supporter", "Early access to new tools", "Vote on next tool we build"], True),
         ("Tower", 100, "📡", ["Everything in Booster", "Logo/link on supporters page", "Quarterly strategy call"], False)]
tier_html = "".join(f'<div class="card tier {"featured" if f else ""}">{"<span class=tag>Most popular</span>" if f else ""}<div style="font-size:2rem">{i}</div><h3>{n}</h3><div class="price">${p}<span class="muted" style="font-size:1rem">/mo</span></div><ul class="list-check" style="text-align:left">{"".join(f"<li>{x}</li>" for x in perks)}</ul><button class="btn {"btn-primary" if f else "btn-ghost"} btn-block" data-amount="{p}" data-tier="{n}">Choose {n}</button></div>' for n, p, i, perks, f in tiers)
reg("support.html", "Support 4GNet — Donate & Sponsor Free Internet Tools", "Support independent 4G/5G tools and guides. Donations fund operations, promotion, hiring talent, and community contests and prizes.",
    hero("Keep the tools free — support 4GNet", "Every contribution funds operations, promotion &amp; marketing, hiring talent, and contests with real prizes.", "Support") + f"""
<section><div class="container"><div class="grid g3">{tier_html}</div>
<p class="center" style="margin-top:20px"><button class="btn btn-ghost" data-amount="" data-tier="One-time">Make a one-time or custom contribution</button></p></div></section>
<section class="section-alt"><div class="container"><div class="grid g2" style="align-items:start">
  <div><h2>Where your support goes</h2>{alloc_html}<p class="muted">We publish a short transparency update each quarter.</p>
    <div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:16px">
      <a class="btn btn-primary" data-donate="paypal" href="#" hidden>Donate with PayPal</a><a class="btn btn-primary" data-donate="stripe" href="#" hidden>Donate by card</a>
      <a class="btn btn-ghost" data-donate="kofi" href="#" hidden>Ko-fi</a><a class="btn btn-ghost" data-donate="buymeacoffee" href="#" hidden>Buy us a coffee</a></div></div>
  <div id="pledge"><form class="tool" data-form="Donation Pledge" data-success="Thank you for your support! We'll email secure payment details and a receipt within 1 business day.">
    <h3>Pledge your support</h3>{honey()}
    <div class="row"><div class="field"><label>Tier<select name="tier"><option>One-time</option><option>Supporter</option><option>Booster</option><option>Tower</option><option>Corporate sponsor</option></select></label></div>
    <div class="field"><label>Amount (USD)<input name="amount" type="number" min="1" step="1" placeholder="25" required></label></div></div>
    <div class="row"><div class="field"><label>Name<input name="name" required autocomplete="name"></label></div><div class="field"><label>Email<input type="email" name="email" required autocomplete="email"></label></div></div>
    <div class="field"><label>Direct my support to<select name="allocation"><option>Wherever it's needed most</option><option>Operations</option><option>Promotion & marketing</option><option>Hiring talent</option><option>Contests & prizes</option></select></label></div>
    <label class="check"><input type="checkbox" name="public_listing" value="yes"> <span>List my name on the supporters wall</span></label>
    <div class="field" style="margin-top:10px"><label>Message (optional)<textarea name="message" style="min-height:80px"></textarea></label></div>
    <button class="btn btn-primary btn-block" type="submit">Pledge support 💙</button><div class="form-msg" role="status"></div>
    <p class="muted" style="font-size:.78rem;margin-top:10px">4GNet is not a registered charity; contributions are not tax-deductible. We never store card details on this site.</p>
  </form></div>
</div></div></section>
<section><div class="container center"><h2>Corporate sponsorship</h2><p class="muted">Carriers, MVNOs and hardware brands can sponsor tools, contests or the video series.</p><a class="btn btn-primary" href="advertise.html">See sponsorship packages</a></div></section>
""")

# ---------------------------------------------------------------- CONTESTS
c_faq, c_ld = faq([
    ("Is there an entry fee?", "No. No purchase or payment is necessary to enter or win."),
    ("How are winners chosen?", "A panel scores entries on usefulness (40%), originality (30%), clarity (20%) and evidence such as before/after speed tests (10%)."),
    ("When are winners announced?", "Within 14 days of the contest closing, on this page and by email."),
])
reg("contests.html", "Contests & Prizes — Win Gear for Your Best Signal Hack", "Enter the 4GNet monthly contest: share your best 4G/5G signal or speed hack with before/after results and win prizes.",
    hero("Contests &amp; prizes", "Show us how you beat bad signal. Best hacks win.", "Contests") + f"""
<section style="background:var(--hero);color:#e6ecf8;padding-top:0"><div class="container center">
  <span class="pill">🏆 Current contest</span>
  <h2 style="margin-top:12px">The Signal Hack Challenge</h2>
  <p style="color:#b8c4dc;max-width:40em;margin:0 auto">Share your cleverest way to improve 4G/5G speed or signal — antenna builds, placement tricks, band locking, router settings. Include before/after speed tests.</p>
  <div class="countdown" data-countdown="2026-12-31T23:59:59Z"></div>
  <div class="grid g3" style="max-width:820px;margin:20px auto 0;text-align:center">
    <div class="card"><div style="font-size:2rem">🥇</div><h3>1st prize</h3><p>$250 gear voucher</p></div>
    <div class="card"><div style="font-size:2rem">🥈</div><h3>2nd prize</h3><p>$100 gear voucher</p></div>
    <div class="card"><div style="font-size:2rem">🥉</div><h3>3rd prize</h3><p>$50 gift card</p></div>
  </div>
</div></section>
{ad()}
<section><div class="container"><div class="layout">
  <form class="tool" data-form="Contest Entry" data-success="Entry received! Good luck — winners are announced within 14 days of the close date.">
    <h2>Submit your entry</h2>{honey()}
    <div class="row"><div class="field"><label>Name<input name="name" required></label></div><div class="field"><label>Email<input type="email" name="email" required></label></div></div>
    <div class="row"><div class="field"><label>Country<input name="country" required></label></div><div class="field"><label>Carrier / ISP<input name="carrier"></label></div></div>
    <div class="field"><label>Hack title<input name="title" required maxlength="100"></label></div>
    <div class="field"><label>Describe your hack (steps, hardware, settings)<textarea name="description" required minlength="80"></textarea></label></div>
    <div class="row"><div class="field"><label>Before (Mbps)<input name="before_mbps" type="number" min="0" step="0.1"></label></div><div class="field"><label>After (Mbps)<input name="after_mbps" type="number" min="0" step="0.1"></label></div></div>
    <div class="field"><label>Link to photos/video (optional)<input name="media_url" type="url" placeholder="https://"></label></div>
    {consent("I confirm this is my original work, I am 18+ (or the age of majority where I live), and I accept the contest rules below.")}
    <button class="btn btn-primary" type="submit" style="margin-top:12px">Submit entry</button><div class="form-msg" role="status"></div>
  </form>
  <aside class="sidebar"><div class="card"><h3>Upcoming contests</h3><ul class="list-check"><li>Best Rural Setup Photo</li><li>Speed-Test World Map Challenge</li><li>Router Review Writing Prize</li></ul><p class="muted">Want to sponsor a contest? <a href="advertise.html">Talk to us</a>.</p></div></aside>
</div></div></section>
<section class="section-alt"><div class="container prose" style="max-width:860px"><h2>Official rules (summary)</h2>
<ul><li>No purchase necessary. Void where prohibited or restricted by law.</li><li>Open to individuals 18+ (or age of majority) in jurisdictions where permitted. Employees of sponsors are ineligible.</li><li>Entries close on the date shown by the countdown (23:59 UTC). One entry per person per contest.</li><li>Entries must be original and must not infringe third-party rights. By entering you grant 4GNet a non-exclusive licence to publish your entry with credit.</li><li>Prizes are non-transferable; no cash alternative unless required by law; the organiser may substitute a prize of equal or greater value. Winners are responsible for applicable taxes.</li><li>Winners are selected by a judging panel under the criteria in the FAQ and notified by email; if unreachable within 14 days, an alternate may be chosen.</li><li>Personal data is used only to administer the contest under our <a href="privacy.html">Privacy Policy</a>.</li></ul>
<h2>FAQ</h2>{c_faq}</div></section>
""", schema=c_ld)

# ---------------------------------------------------------------- CAREERS
roles = [("Telecom Content Writer", "Remote · Freelance", "Write guides, reviews and comparisons about 4G/5G, eSIM and home internet."),
         ("Video Creator / Editor", "Remote · Freelance", "Produce YouTube explainers, Shorts and speed-test videos."),
         ("SEO & Growth Specialist", "Remote · Part-time", "Scale programmatic location pages, rankings and conversion."),
         ("Front-end Developer", "Remote · Contract", "Build new tools (coverage maps, comparison engines) in modern JS."),
         ("Partnerships Manager", "Remote · Commission", "Sign carriers, MVNOs, eSIM brands and hardware affiliates."),
         ("Community Moderator", "Remote · Volunteer/Paid", "Run contests, answer questions and grow our community.")]
role_html = "".join(f'<div class="card"><span class="tag">{loc}</span><h3>{t}</h3><p>{d}</p></div>' for t, loc, d in roles)
role_opts = "".join(f"<option>{t}</option>" for t, _, _ in roles)
reg("careers.html", "Careers — Join the 4GNet Team", "Remote roles for telecom writers, video creators, SEO specialists, developers, partnership managers and community moderators.",
    hero("Build the internet's most useful wireless hub", "We hire remote talent worldwide — freelance, part-time and contract.", "Careers") + f"""
<section><div class="container"><div class="grid g3">{role_html}</div></div></section>
<section class="section-alt"><div class="container" style="max-width:860px">
<form class="tool" data-form="Job Application" data-success="Application received. We review every application and reply within 7 days.">
  <h2>Apply now</h2>{honey()}
  <div class="row"><div class="field"><label>Full name<input name="name" required autocomplete="name"></label></div><div class="field"><label>Email<input type="email" name="email" required autocomplete="email"></label></div></div>
  <div class="row"><div class="field"><label>Role<select name="role">{role_opts}<option>Other / open application</option></select></label></div><div class="field"><label>Location / time zone<input name="location" required></label></div></div>
  <div class="row"><div class="field"><label>Portfolio / LinkedIn / GitHub URL<input name="portfolio" type="url" placeholder="https://" required></label></div><div class="field"><label>Availability<select name="availability"><option>&lt;10 hrs/week</option><option>10–20 hrs/week</option><option>20–40 hrs/week</option><option>Full-time</option></select></label></div></div>
  <div class="field"><label>Expected rate (USD/hr or per piece)<input name="rate"></label></div>
  <div class="field"><label>Why you? (what would you build or create first?)<textarea name="pitch" required></textarea></label></div>
  {consent()}
  <button class="btn btn-primary" type="submit" style="margin-top:12px">Send application</button><div class="form-msg" role="status"></div>
</form></div></section>
""")

# ---------------------------------------------------------------- ADVERTISE
pk = [("Display & native", "From $500/mo", ["Homepage + tools placements", "Guaranteed impressions", "Monthly performance report"]),
      ("Tool sponsorship", "From $1,500/mo", ["'Powered by' branding on a tool", "Exclusive category", "Lead-form integration"]),
      ("Contest / video partner", "From $2,500/campaign", ["Branded contest & prizes", "Video integration", "Newsletter + social push"])]
pk_html = "".join(f'<div class="card tier"><h3>{t}</h3><div class="price" style="font-size:1.6rem">{p}</div><ul class="list-check" style="text-align:left">{"".join(f"<li>{x}</li>" for x in xs)}</ul></div>' for t, p, xs in pk)
reg("advertise.html", "Advertise, Sponsor & Partner with 4GNet", "Reach people actively choosing mobile plans, 4G/5G home internet, routers and travel eSIMs. Display ads, tool sponsorships, lead partnerships and contests.",
    hero("Advertise, sponsor &amp; partner", "Reach buyers at the exact moment they're testing, comparing and choosing connectivity.", "Advertise") + f"""
<section><div class="container">
  <div class="grid g4" style="text-align:center">
    <div class="card"><h3>🎯 High intent</h3><p>Visitors run tests and compare plans before buying.</p></div>
    <div class="card"><h3>🌍 Multi-market</h3><p>US, Canada, UK, India, Australia &amp; travellers worldwide.</p></div>
    <div class="card"><h3>🤝 Lead partnerships</h3><p>CPL/CPA deals for ISPs, MVNOs, eSIM and IoT providers.</p></div>
    <div class="card"><h3>📈 Transparent</h3><p>Clear labelling and reporting; no fake reviews.</p></div>
  </div>
  <h2 class="center" style="margin-top:48px">Packages</h2><div class="grid g3">{pk_html}</div>
  <p class="center muted" style="margin-top:12px">Custom packages available. Interested in acquiring the whole website or domain? <a href="{INTEREST}" target="_blank" rel="noopener">Contact via web.works</a>.</p>
</div></section>
<section class="section-alt"><div class="container" style="max-width:860px">
<form class="tool" data-form="Advertising / Sponsorship / Partnership" data-success="Thanks! Our partnerships team will send the media kit and availability within 1 business day.">
  <h2>Request the media kit</h2>{honey()}
  <div class="row"><div class="field"><label>Company<input name="company" required></label></div><div class="field"><label>Your name<input name="name" required></label></div></div>
  <div class="row"><div class="field"><label>Work email<input type="email" name="email" required></label></div><div class="field"><label>Website<input name="website" type="url" placeholder="https://"></label></div></div>
  <div class="row"><div class="field"><label>Interest<select name="interest"><option>Display advertising</option><option>Tool sponsorship</option><option>Lead-generation partnership</option><option>Affiliate program</option><option>Contest / video sponsorship</option><option>Website / domain acquisition</option><option>Other partnership</option></select></label></div>
  <div class="field"><label>Budget<select name="budget"><option>&lt; $1,000</option><option>$1,000–$5,000</option><option>$5,000–$25,000</option><option>$25,000+</option><option>Performance-based</option></select></label></div></div>
  <div class="field"><label>Goals &amp; target markets<textarea name="goals"></textarea></label></div>
  {consent()}
  <button class="btn btn-primary" type="submit" style="margin-top:12px">Send request</button><div class="form-msg" role="status"></div>
</form></div></section>
""")

# ---------------------------------------------------------------- CONTACT
reg("contact.html", "Contact 4GNet", "Contact the 4GNet team for questions, corrections, partnerships, press and support.",
    hero("Contact us", "Questions, corrections, partnership ideas or press — we read everything.", "Contact") + f"""
<section><div class="container"><div class="layout">
<form class="tool" data-form="General Contact" data-success="Message sent! We usually reply within 1 business day.">
  {honey()}
  <div class="row"><div class="field"><label>Name<input name="name" required autocomplete="name"></label></div><div class="field"><label>Email<input type="email" name="email" required autocomplete="email"></label></div></div>
  <div class="field"><label>Topic<select name="topic"><option>General question</option><option>Help choosing internet</option><option>Correction / data update</option><option>Advertising / sponsorship</option><option>Partnership</option><option>Website / domain acquisition</option><option>Press</option><option>Privacy request</option></select></label></div>
  <div class="field"><label>Message<textarea name="message" required></textarea></label></div>
  {consent()}
  <button class="btn btn-primary" type="submit" style="margin-top:12px">Send message</button><div class="form-msg" role="status"></div>
</form>
<aside class="sidebar"><div class="card"><h3>Faster routes</h3><div class="toc"><a href="get-matched.html">⚡ Get internet quotes</a><a href="business.html">🏢 Business &amp; IoT quote</a><a href="advertise.html">📣 Advertising &amp; media kit</a><a href="careers.html">💼 Apply for a role</a><a href="{INTEREST}" target="_blank" rel="noopener">🌐 Buy / partner on this domain</a></div></div></aside>
</div></div></section>
""")
