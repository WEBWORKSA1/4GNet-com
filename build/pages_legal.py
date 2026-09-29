from layout import page, hero, ad, UPDATED, INTEREST
from pages_core import reg, PAGES


def legal(fn, title, desc, body):
    reg(fn, title, desc, hero(title, desc, title) + f'<section><div class="container prose" style="max-width:860px"><p class="meta">Last updated: {UPDATED}</p>{body}</div></section>')


legal("about.html", "About 4GNet & Our Methodology", "Who we are, how we test and compare, and how 4GNet makes money.", """
<h2>Our mission</h2><p>4GNet helps people and businesses get fast, reliable wireless internet — whether that's a better phone plan, 4G/5G home internet, rural connectivity, business failover or a travel eSIM. We build free tools and write independent guides so you can make decisions from data rather than marketing.</p>
<h2>How we research</h2><ul><li>We benchmark providers and tools against public information, regulator data, manufacturer specifications and our own tests.</li><li>Technical figures (speeds, latency, bands) are expressed as typical real-world ranges and reviewed regularly.</li><li>Every guide shows a "last updated" date. Found an error? <a href="contact.html">Tell us</a> and we'll fix it.</li></ul>
<h2>How we make money</h2><p>We earn from display advertising (e.g. Google AdSense), affiliate commissions, referral fees when you request quotes, sponsorships and reader support. Commercial relationships never determine our editorial conclusions; sponsored placements are always labelled.</p>
<h2>Independence</h2><p>4GNet is independent and is not owned by, or affiliated with, any mobile network operator, equipment maker, or any other business using a similar name.</p>""")

legal("privacy.html", "Privacy Policy", "How 4GNet collects, uses and protects your information.", """
<h2>What we collect</h2><ul><li><b>Information you submit</b> in forms (e.g. name, email, phone, ZIP/postcode, usage preferences, messages).</li><li><b>Technical data</b> such as browser type, device, pages visited and approximate location, via cookies and analytics if you consent.</li><li><b>Speed-test measurements</b> run in your browser against Cloudflare's public speed-test endpoints; we do not store your results on our servers.</li></ul>
<h2>How we use it</h2><ul><li>To respond to your request, including sharing lead details with relevant connectivity providers you ask to be matched with.</li><li>To operate, secure and improve the site.</li><li>To show advertising (including personalised ads where you consent).</li><li>To send newsletters you subscribe to (unsubscribe anytime).</li></ul>
<h2>Processors</h2><p>Form submissions are delivered through a third-party form-processing service (FormSubmit). Advertising is provided by Google AdSense; analytics by Google Analytics where enabled. Video embeds load from YouTube (privacy-enhanced mode) only when you click play. Hosting is provided by GitHub Pages.</p>
<h2>Cookies & advertising</h2><p>Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on your visits. You can opt out of personalised advertising at Google's Ads Settings, or choose "Essential only" in our cookie banner.</p>
<h2>Your rights</h2><p>Depending on where you live (e.g. GDPR, UK GDPR, CCPA/CPRA, PIPEDA, India's DPDP Act), you may request access, correction, deletion or restriction of your data, and object to processing. Use our <a href="contact.html">contact form</a> and choose "Privacy request".</p>
<h2>Retention & security</h2><p>We keep lead and contact data only as long as needed for the purpose collected (typically up to 24 months) and use reasonable safeguards. No website can guarantee absolute security.</p>
<h2>Children</h2><p>This site is not directed to children under 16, and we do not knowingly collect their data.</p>""")

legal("terms.html", "Terms of Use", "The terms that apply when you use 4GNet.com.", """
<h2>Use of the site</h2><p>By using 4GNet.com you agree to these terms. Content and tools are provided for general information only and do not constitute professional, legal or financial advice.</p>
<h2>Accuracy</h2><p>Speeds, prices, bands, APNs and availability change frequently. Tool results are estimates. Always confirm details with the provider before purchasing. We are not liable for decisions made based on site content.</p>
<h2>Third parties</h2><p>We link to and embed third-party websites and services. We are not responsible for their content, products, pricing or privacy practices.</p>
<h2>User submissions</h2><p>You agree not to submit unlawful, infringing or misleading content. By submitting contest entries or feedback you grant us a non-exclusive, royalty-free licence to use and publish it with attribution.</p>
<h2>Intellectual property</h2><p>The site's original text, design, code and graphics are protected by copyright. You may share links and short quotations with attribution; other reproduction requires permission.</p>
<h2>Limitation of liability</h2><p>To the maximum extent permitted by law, the site is provided "as is" without warranties, and we are not liable for indirect or consequential losses arising from its use.</p>
<h2>Changes</h2><p>We may update these terms; continued use means acceptance of the updated terms.</p>""")

legal("disclosure.html", "Trademark, Copyright & Affiliate Disclosure", "Independence, trademark, copyright, advertising and affiliate disclosures for 4GNet.com.", f"""
<h2>Trademark disclosure</h2>
<ul><li>4GNet.com is an independent information website. The name refers descriptively to "4G" (fourth-generation mobile) networks and the internet. It is <b>not affiliated with, endorsed by, sponsored by, or connected to any company, product, or service named "4GNet", "4G Net", "4G-Net" or similar</b>, in any country.</li>
<li>"4G" and "5G" are generic industry terms for mobile network generations. "LTE" is a trademark of ETSI (European Telecommunications Standards Institute), used here to refer to the standard.</li>
<li>All carrier, operator, manufacturer, product and service names (for example, mobile network operators, eSIM providers, router makers and platforms such as YouTube and Google) are trademarks or registered trademarks of their respective owners. They are used only to identify products and services (nominative fair use) and do not imply endorsement.</li>
<li>If you believe any content infringes your trademark, <a href="contact.html">contact us</a> and we will review promptly.</li></ul>
<h2>Copyright disclosure</h2>
<ul><li>All original text, tools, code, graphics and the site design are © 4GNet.com. All rights reserved.</li><li>Embedded YouTube videos remain the property of their creators and are displayed using YouTube's standard embed functionality under YouTube's Terms of Service.</li><li>Third-party data sources are credited where used. Band and APN data are compiled from publicly available information and may change.</li><li>DMCA / copyright notices: use our <a href="contact.html">contact form</a> with the URL, the work concerned and your contact details; we act promptly on valid notices.</li></ul>
<h2>Affiliate & advertising disclosure</h2>
<ul><li>Some links are affiliate links (marked "Partner" or with a disclosure). If you buy through them we may earn a commission at no extra cost to you.</li><li>When you request quotes, we may receive a referral fee from providers we connect you with. This never changes your price.</li><li>We display ads from Google AdSense and may run labelled sponsored placements. Advertisers do not control editorial content.</li></ul>
<h2>Domain & website availability</h2><p>Interested in this website, the domain name, sponsorship, advertising or partnership? <a href="{INTEREST}" target="_blank" rel="noopener">Contact via web.works</a>.</p>""")

PAGES["404.html"] = page("404.html", "Page not found", "The page you're looking for doesn't exist.",
    '<section class="page-hero"><div class="container center"><h1>404 — no signal here</h1><p style="margin:0 auto 20px">That page dropped off the network. Try one of these instead.</p><a class="btn btn-lime" href="index.html">Home</a> <a class="btn btn-ghost" style="color:#fff" href="speed-test.html">Speed test</a></div></section>')
