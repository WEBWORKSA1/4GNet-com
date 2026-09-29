/* 4GNet.com — interactive tools. Each init runs only if its container exists. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var fmt = function (n, d) { return Number(n).toFixed(d == null ? 1 : d); };

  /* ---------------- SPEED TEST ---------------- */
  function initSpeed() {
    var root = $("#speedtest"); if (!root) return;
    var BASE = "https://speed.cloudflare.com";
    var btn = $("#st-start"), needle = $("#st-needle"), val = $("#st-val"), unit = $("#st-unit"), phase = $("#st-phase");
    var out = { down: $("#m-down"), up: $("#m-up"), ping: $("#m-ping"), jit: $("#m-jit") };
    function setGauge(mbps) {
      var max = 1000, v = Math.min(mbps, max);
      var pct = Math.log10(1 + v) / Math.log10(1 + max); /* log scale */
      needle.setAttribute("transform", "rotate(" + (-120 + 240 * pct) + " 160 160)");
      val.textContent = mbps >= 100 ? Math.round(mbps) : fmt(mbps, 1);
    }
    function now() { return performance.now(); }
    function ping(n) {
      var times = [], i = 0;
      return new Promise(function (res, rej) {
        (function next() {
          if (i++ >= n) return res(times);
          var t = now();
          fetch(BASE + "/__down?bytes=0&r=" + Math.random(), { cache: "no-store" })
            .then(function (r) { return r.arrayBuffer(); })
            .then(function () { times.push(now() - t); next(); }).catch(rej);
        })();
      });
    }
    function down(bytes) {
      var t = now(), got = 0;
      return fetch(BASE + "/__down?bytes=" + bytes + "&r=" + Math.random(), { cache: "no-store" }).then(function (r) {
        if (!r.body || !r.body.getReader) return r.arrayBuffer().then(function (b) { got = b.byteLength; return got * 8 / ((now() - t) / 1000) / 1e6; });
        var reader = r.body.getReader();
        return (function pump() {
          return reader.read().then(function (x) {
            if (x.done) return got * 8 / ((now() - t) / 1000) / 1e6;
            got += x.value.length;
            var el = (now() - t) / 1000; if (el > .15) setGauge(got * 8 / el / 1e6);
            return pump();
          });
        })();
      });
    }
    function up(bytes) {
      var data = new Uint8Array(bytes), t = now();
      return fetch(BASE + "/__up?r=" + Math.random(), { method: "POST", body: data, cache: "no-store" })
        .then(function (r) { return r.text(); })
        .then(function () { return bytes * 8 / ((now() - t) / 1000) / 1e6; });
    }
    function median(a) { var s = a.slice().sort(function (x, y) { return x - y; }); var m = Math.floor(s.length / 2); return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2; }
    function verdict(d, u, p) {
      var rows = [
        ["4K streaming", d >= 25], ["HD streaming", d >= 5], ["HD video calls", d >= 4 && u >= 3 && p < 150],
        ["Online gaming", d >= 3 && p < 60], ["Work from home", d >= 15 && u >= 5], ["Large uploads", u >= 20]
      ];
      $("#st-verdict").innerHTML = rows.map(function (r) { return "<div class='" + (r[1] ? "v-good" : "v-bad") + "'>" + (r[1] ? "✓ " : "✗ ") + r[0] + "</div>"; }).join("");
      var grade = d >= 100 ? "Excellent" : d >= 25 ? "Good" : d >= 10 ? "Fair" : "Poor";
      $("#st-grade").textContent = grade + " connection";
      $("#st-after").classList.add("show");
    }
    btn.addEventListener("click", function () {
      btn.disabled = true; btn.textContent = "Testing…";
      ["down", "up", "ping", "jit"].forEach(function (k) { out[k].textContent = "–"; });
      $("#st-after").classList.remove("show"); $("#st-err").hidden = true;
      var res = {};
      phase.textContent = "Measuring latency…"; unit.textContent = "ms";
      ping(12).then(function (t) {
        t.shift(); /* drop connection setup */
        res.ping = median(t);
        var diffs = t.slice(1).map(function (x, i) { return Math.abs(x - t[i]); });
        res.jit = diffs.reduce(function (a, b) { return a + b; }, 0) / (diffs.length || 1);
        out.ping.textContent = fmt(res.ping, 0); out.jit.textContent = fmt(res.jit, 1);
        phase.textContent = "Testing download…"; unit.textContent = "Mbps";
        var sizes = [1e5, 1e6, 1e7, 2.5e7], results = [];
        return sizes.reduce(function (p, s) {
          return p.then(function () { return down(s).then(function (m) { results.push(m); setGauge(m); }); });
        }, Promise.resolve()).then(function () { res.down = Math.max(results[2] || 0, results[3] || 0, results[1] || 0); });
      }).then(function () {
        out.down.textContent = fmt(res.down, 1); setGauge(0);
        phase.textContent = "Testing upload…";
        var sizes = [1e5, 1e6, 5e6], results = [];
        return sizes.reduce(function (p, s) {
          return p.then(function () { return up(s).then(function (m) { results.push(m); setGauge(m); }); });
        }, Promise.resolve()).then(function () { res.up = Math.max.apply(null, results.slice(1)); });
      }).then(function () {
        out.up.textContent = fmt(res.up, 1);
        setGauge(res.down); phase.textContent = "Complete — download result shown";
        verdict(res.down, res.up, res.ping);
      }).catch(function () {
        $("#st-err").hidden = false; phase.textContent = "Test could not complete";
      }).then(function () { btn.disabled = false; btn.textContent = "Run again"; });
    });
  }

  /* ---------------- BAND CHECKER ---------------- */
  var CARRIERS = {
    "United States": { "Verizon": [2, 4, 5, 13, 48, 66], "AT&T": [2, 4, 5, 12, 14, 17, 29, 30, 66], "T-Mobile": [2, 4, 5, 12, 66, 71] },
    "Canada": { "Rogers": [2, 4, 7, 12, 13, 17, 29, 66], "Bell": [2, 4, 5, 7, 12, 13, 17, 29, 66], "Telus": [2, 4, 5, 7, 12, 13, 17, 29, 66] },
    "United Kingdom": { "EE": [1, 3, 7, 20, 38], "Vodafone UK": [1, 3, 7, 8, 20, 32, 38], "O2 UK": [1, 3, 8, 20, 40], "Three UK": [1, 3, 20, 32] },
    "India": { "Jio": [3, 5, 40], "Airtel": [1, 3, 8, 40, 41], "Vi (Vodafone Idea)": [1, 3, 8, 40, 41] },
    "Australia": { "Telstra": [1, 3, 7, 8, 28, 40], "Optus": [1, 3, 7, 8, 28, 40], "Vodafone AU": [1, 3, 5, 8, 28] },
    "Germany": { "Telekom": [1, 3, 7, 8, 20, 28, 32], "Vodafone DE": [1, 3, 7, 8, 20, 28, 32], "O2 DE": [1, 3, 7, 8, 20, 28] },
    "Japan": { "NTT docomo": [1, 3, 19, 21, 28, 42], "au (KDDI)": [1, 11, 18, 26, 28, 41, 42], "SoftBank": [1, 3, 8, 11, 28, 41, 42] }
  };
  var CORE = { "Verizon": [13, 66, 2], "AT&T": [2, 12, 17, 66], "T-Mobile": [2, 66, 12, 71], "Rogers": [4, 7, 12, 66], "Bell": [4, 7, 12, 66], "Telus": [4, 7, 12, 66],
    "EE": [3, 20, 7], "Vodafone UK": [20, 3, 1], "O2 UK": [20, 8, 3], "Three UK": [3, 20], "Jio": [3, 5, 40], "Airtel": [3, 40, 1], "Vi (Vodafone Idea)": [3, 40, 1],
    "Telstra": [3, 28], "Optus": [3, 28, 40], "Vodafone AU": [3, 5, 28], "Telekom": [3, 20, 7], "Vodafone DE": [3, 20, 7], "O2 DE": [3, 20, 8],
    "NTT docomo": [1, 19, 3], "au (KDDI)": [1, 18, 26], "SoftBank": [1, 3, 8] };
  var ALL_BANDS = [1, 2, 3, 4, 5, 7, 8, 11, 12, 13, 14, 17, 18, 19, 20, 21, 25, 26, 28, 29, 30, 32, 38, 39, 40, 41, 42, 46, 48, 66, 71];
  function initBands() {
    var root = $("#bandchecker"); if (!root) return;
    var cSel = $("#bc-country"), kSel = $("#bc-carrier"), grid = $("#bc-bands"), paste = $("#bc-paste"), outBox = $("#bc-result");
    var mine = {};
    Object.keys(CARRIERS).forEach(function (c) { cSel.add(new Option(c, c)); });
    function fillCarriers() { kSel.innerHTML = ""; Object.keys(CARRIERS[cSel.value]).forEach(function (k) { kSel.add(new Option(k, k)); }); showCarrierBands(); }
    function showCarrierBands() {
      var b = CARRIERS[cSel.value][kSel.value], core = CORE[kSel.value] || [];
      $("#bc-carrier-bands").innerHTML = b.map(function (x) { return "<span class='band on" + (core.indexOf(x) > -1 ? " core" : "") + "'>B" + x + "</span>"; }).join("");
    }
    grid.innerHTML = ALL_BANDS.map(function (b) { return "<span class='band' data-b='" + b + "' role='checkbox' aria-checked='false' tabindex='0'>B" + b + "</span>"; }).join("");
    grid.addEventListener("click", function (e) {
      var t = e.target.closest(".band"); if (!t) return;
      var b = +t.getAttribute("data-b"); mine[b] = !mine[b];
      t.classList.toggle("on", mine[b]); t.setAttribute("aria-checked", mine[b] ? "true" : "false");
    });
    grid.addEventListener("keydown", function (e) { if (e.key === " " || e.key === "Enter") { e.preventDefault(); e.target.click(); } });
    paste.addEventListener("input", function () {
      mine = {};
      (paste.value.match(/\d+/g) || []).forEach(function (n) { mine[+n] = true; });
      $$(".band", grid).forEach(function (el) { var on = !!mine[+el.getAttribute("data-b")]; el.classList.toggle("on", on); el.setAttribute("aria-checked", on); });
    });
    cSel.addEventListener("change", fillCarriers); kSel.addEventListener("change", showCarrierBands);
    fillCarriers();
    $("#bc-check").addEventListener("click", function () {
      var need = CARRIERS[cSel.value][kSel.value], core = CORE[kSel.value] || [];
      var have = need.filter(function (b) { return mine[b]; }), coreHave = core.filter(function (b) { return mine[b]; });
      var miss = need.filter(function (b) { return !mine[b]; });
      if (!Object.keys(mine).some(function (k) { return mine[k]; })) { outBox.className = "result-box show"; outBox.innerHTML = "Select or paste the LTE bands your phone supports first (find them on the manufacturer spec sheet)."; return; }
      var score = coreHave.length / core.length, cls, title;
      if (score === 1 && have.length >= need.length * 0.6) { cls = "v-good"; title = "✓ Full compatibility"; }
      else if (score >= 0.5) { cls = "v-mid"; title = "◐ Partial compatibility"; }
      else { cls = "v-bad"; title = "✗ Poor compatibility"; }
      outBox.className = "result-box show";
      outBox.innerHTML = "<h3 class='" + cls + "'>" + title + " on " + kSel.value + "</h3>" +
        "<p>Your phone supports <b>" + have.length + " of " + need.length + "</b> of this carrier's 4G LTE bands, including <b>" + coreHave.length + " of " + core.length + "</b> core coverage/capacity bands.</p>" +
        (miss.length ? "<p class='muted'>Missing: " + miss.map(function (b) { return "B" + b; }).join(", ") + ". Missing low bands (B5, B8, B12, B13, B17, B20, B28, B71) mainly hurts indoor and rural coverage.</p>" : "<p class='muted'>Every listed band is supported.</p>") +
        "<p><a class='btn btn-primary btn-sm' href='get-matched.html?need=home'>Get matched with a plan that works on your device →</a></p>";
    });
  }

  /* ---------------- APN FINDER ---------------- */
  var APN = [
    ["United States", "T-Mobile", "fast.t-mobile.com", "", "", "default,supl,mms", "http://mms.msg.eng.t-mobile.com/mms/wapenc"],
    ["United States", "AT&T (phones)", "nxtgenphone", "", "", "default,mms,supl,fota,hipri", "http://mmsc.mobile.att.net"],
    ["United States", "AT&T (hotspots/tablets)", "broadband", "", "", "default", ""],
    ["United States", "Verizon", "vzwinternet", "", "", "default,supl", "http://mms.vtext.com/servlets/mms"],
    ["Canada", "Rogers", "ltemobile.apn", "", "", "default,supl,mms", "http://mms.gprs.rogers.com"],
    ["Canada", "Fido", "ltemobile.apn", "", "", "default,supl,mms", "http://mms.fido.ca"],
    ["Canada", "Bell", "pda.bell.ca", "", "", "default,mms,supl", "http://mms.bell.ca/mms/wapenc"],
    ["Canada", "Telus", "sp.telus.com", "", "", "default,mms,supl", "http://aliasredirect.net/proxy/mmsc"],
    ["United Kingdom", "EE", "everywhere", "eesecure", "secure", "default,supl,mms", "http://mms/"],
    ["United Kingdom", "O2 UK", "mobile.o2.co.uk", "o2web", "password", "default,supl", ""],
    ["United Kingdom", "Vodafone UK (PAYG)", "pp.vodafone.co.uk", "wap", "wap", "default,supl,mms", "http://mms.vodafone.co.uk/servlets/mms"],
    ["United Kingdom", "Vodafone UK (contract)", "wap.vodafone.co.uk", "wap", "wap", "default,supl,mms", "http://mms.vodafone.co.uk/servlets/mms"],
    ["United Kingdom", "Three UK", "three.co.uk", "", "", "default,supl,mms", "http://mms.um.three.co.uk:10021/mmsc"],
    ["India", "Jio", "jionet", "", "", "default,supl", ""],
    ["India", "Airtel", "airtelgprs.com", "", "", "default,supl", ""],
    ["India", "Vi (Vodafone Idea)", "www", "", "", "default,supl", ""],
    ["India", "BSNL", "bsnlnet", "", "", "default,supl", ""],
    ["Australia", "Telstra", "telstra.internet", "", "", "default,supl", ""],
    ["Australia", "Optus", "yesinternet", "", "", "default,supl", ""],
    ["Australia", "Vodafone AU", "live.vodafone.com", "", "", "default,supl", ""],
    ["Germany", "Telekom", "internet.telekom", "telekom", "tm", "default,supl", ""],
    ["Germany", "Vodafone DE", "web.vodafone.de", "", "", "default,supl", ""],
    ["Germany", "O2 DE", "internet", "", "", "default,supl", ""]
  ];
  function initApn() {
    var root = $("#apnfinder"); if (!root) return;
    var cSel = $("#apn-country"), q = $("#apn-q"), body = $("#apn-body");
    Array.from(new Set(APN.map(function (r) { return r[0]; }))).forEach(function (c) { cSel.add(new Option(c, c)); });
    function cp(v) { return v ? "<code>" + v + "</code><button class='copy' data-copy='" + v + "' type='button'>Copy</button>" : "<span class='muted'>(blank)</span>"; }
    function render() {
      var term = q.value.trim().toLowerCase();
      var rows = APN.filter(function (r) { return (!cSel.value || r[0] === cSel.value) && (!term || r.join(" ").toLowerCase().indexOf(term) > -1); });
      body.innerHTML = rows.map(function (r) {
        return "<tr><td>" + r[0] + "</td><td><b>" + r[1] + "</b></td><td>" + cp(r[2]) + "</td><td>" + cp(r[3]) + "</td><td>" + cp(r[4]) + "</td><td><code>" + r[5] + "</code></td><td style='word-break:break-all'>" + (r[6] ? cp(r[6]) : "<span class='muted'>—</span>") + "</td></tr>";
      }).join("") || "<tr><td colspan='7'>No match. Request it below and we'll add it.</td></tr>";
    }
    cSel.addEventListener("change", render); q.addEventListener("input", render); render();
    root.addEventListener("click", function (e) {
      var b = e.target.closest("[data-copy]"); if (!b) return;
      var v = b.getAttribute("data-copy");
      (navigator.clipboard ? navigator.clipboard.writeText(v) : Promise.reject()).then(function () { b.textContent = "Copied"; setTimeout(function () { b.textContent = "Copy"; }, 1200); }).catch(function () { prompt("Copy:", v); });
    });
  }

  /* ---------------- SIGNAL ANALYZER ---------------- */
  function initSignal() {
    var root = $("#signal"); if (!root) return;
    function grade(v, t) { return v >= t[0] ? [3, "Excellent"] : v >= t[1] ? [2, "Good"] : v >= t[2] ? [1, "Fair"] : [0, "Poor"]; }
    $("#sig-go").addEventListener("click", function () {
      var rsrp = parseFloat($("#sig-rsrp").value), rsrq = parseFloat($("#sig-rsrq").value), sinr = parseFloat($("#sig-sinr").value);
      if (isNaN(rsrp)) { $("#sig-rsrp").focus(); return; }
      var g = [["RSRP (signal strength)", rsrp + " dBm", grade(rsrp, [-80, -90, -100])]];
      if (!isNaN(rsrq)) g.push(["RSRQ (signal quality)", rsrq + " dB", grade(rsrq, [-10, -15, -20])]);
      if (!isNaN(sinr)) g.push(["SINR (noise ratio)", sinr + " dB", grade(sinr, [20, 13, 0])]);
      var cls = ["v-bad", "v-mid", "v-good", "v-good"];
      var worst = Math.min.apply(null, g.map(function (x) { return x[2][0]; }));
      var tips = {
        0: "Signal is weak. Move the router to a window facing the nearest tower, get off the ground floor, or add an outdoor directional (Yagi/panel) antenna with 5–10 m of low-loss cable. Band-locking to a low band (B12/B13/B20/B28/B71) can improve stability.",
        1: "Usable but inconsistent. Try relocating the device 1–2 m at a time and re-test. MIMO antennas on the window typically add 5–15 dB. Check whether a less congested band is available.",
        2: "Solid signal. Speed limits are likely from tower congestion or your plan, not coverage. Test at off-peak hours to compare.",
        3: "Excellent signal. You should see near-maximum speeds for your plan and device category."
      };
      var o = $("#sig-result");
      o.className = "result-box show";
      o.innerHTML = "<div class='verdict'>" + g.map(function (x) { return "<div><span class='muted'>" + x[0] + "</span><br><b class='" + cls[x[2][0]] + "'>" + x[2][1] + "</b> · " + x[1] + "</div>"; }).join("") + "</div><p style='margin-top:14px'>" + tips[worst] + "</p><a class='btn btn-primary btn-sm' href='get-matched.html?need=rural'>Ask for a better provider in your area →</a>";
    });
  }

  /* ---------------- BANDWIDTH CALCULATOR ---------------- */
  function initBandwidth() {
    var root = $("#bandwidth"); if (!root) return;
    var rates = { people: 2, uhd: 25, hd: 6, calls: 4, gaming: 5, wfh: 10, iot: 0.3, cloud: 10 };
    function calc() {
      var total = 0;
      $$("input[data-rate]", root).forEach(function (i) { total += (parseFloat(i.value) || 0) * rates[i.getAttribute("data-rate")]; });
      var rec = Math.max(10, Math.ceil(total * 1.3 / 5) * 5);
      $("#bw-out").textContent = rec;
      var tier = rec <= 25 ? "Most 4G LTE home plans can handle this." : rec <= 100 ? "Strong 4G LTE-Advanced or any 5G home internet plan fits." : rec <= 300 ? "Look at 5G home internet or cable/fiber." : "You need fiber or high-tier 5G (mmWave/C-band).";
      $("#bw-tier").textContent = tier;
    }
    root.addEventListener("input", calc); calc();
  }

  /* ---------------- DATA USAGE CALCULATOR ---------------- */
  function initData() {
    var root = $("#datacalc"); if (!root) return;
    var gbh = { sd: 0.7, hd: 3, uhd: 7, music: 0.15, social: 0.8, calls: 1.2, web: 0.08, gaming: 0.1 };
    function calc() {
      var day = 0;
      $$("input[data-gbh]", root).forEach(function (i) { day += (parseFloat(i.value) || 0) * gbh[i.getAttribute("data-gbh")]; });
      var month = day * 30;
      $("#dc-day").textContent = fmt(day, 2); $("#dc-month").textContent = fmt(month, 0);
      var tip = month < 5 ? "A small 5 GB plan is enough." : month < 20 ? "A 20 GB plan covers you with room to spare." : month < 50 ? "Choose a 50 GB plan or an unlimited plan with a high priority-data cap." : "Go unlimited — and check the deprioritisation threshold and hotspot cap.";
      $("#dc-tip").textContent = tip;
    }
    root.addEventListener("input", calc); calc();
  }

  /* ---------------- PLAN FINDER QUIZ ---------------- */
  function initQuiz() {
    var root = $("#planquiz"); if (!root) return;
    $("#pq-go").addEventListener("click", function () {
      var use = (root.querySelector("input[name=pq_use]:checked") || {}).value;
      var data = (root.querySelector("input[name=pq_data]:checked") || {}).value;
      var budget = (root.querySelector("input[name=pq_budget]:checked") || {}).value;
      if (!use || !data || !budget) { alert("Answer all three questions."); return; }
      var rec = {
        phone: { low: "Prepaid or MVNO plan on a major network (typically the best value per GB).", mid: "Mid-tier unlimited from an MVNO or a major carrier's prepaid brand.", high: "Premium postpaid unlimited with priority data, 5G, and international roaming." },
        home: { low: "4G LTE home internet or a fixed-wireless plan — no install, no contract.", mid: "5G home internet (C-band/mid-band) — usually 100–300 Mbps.", high: "Premium 5G home internet with an outdoor receiver, or fiber if available." },
        travel: { low: "Pay-as-you-go regional eSIM with a small data pack.", mid: "Country or regional eSIM with 10–20 GB.", high: "Unlimited travel eSIM or a global eSIM subscription." },
        business: { low: "Single-line business data SIM for backup.", mid: "4G/5G failover router with a business data plan.", high: "Dual-carrier SD-WAN / bonded 5G primary + failover with SLA." },
        rv: { low: "Unlimited phone plan with a generous hotspot allowance.", mid: "Dedicated 5G hotspot/router plan + roof antenna.", high: "Dual-carrier router, roof MIMO antenna, and satellite backup." }
      }[use][budget];
      var gb = { light: "under 10 GB", medium: "10–50 GB", heavy: "50 GB+ / unlimited" }[data];
      var o = $("#pq-result");
      o.className = "result-box show";
      o.innerHTML = "<span class='tag'>Your match</span><h3>" + rec + "</h3><p class='muted'>Data target: " + gb + ". Prices and availability vary by address — get free quotes from providers that serve you.</p>" +
        "<a class='btn btn-primary' href='get-matched.html?need=" + (use === "phone" ? "home" : use) + "'>Get free quotes →</a> " + (use === "travel" ? "<a class='btn btn-ghost' href='esim.html'>Compare travel eSIMs</a>" : "");
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    initSpeed(); initBands(); initApn(); initSignal(); initBandwidth(); initData(); initQuiz();
  });
})();
