/* 4GNet.com — global behaviour: theme, nav, cookies, ads, video facades, forms, steppers */
(function () {
  "use strict";
  var C = window.SITE_CONFIG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} }
  };

  /* Theme */
  var saved = store.get("theme");
  if (saved) document.documentElement.setAttribute("data-theme", saved);
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-theme-toggle]");
    if (!t) return;
    var cur = document.documentElement.getAttribute("data-theme");
    if (!cur) cur = window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
    var next = cur === "dark" ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    store.set("theme", next);
  });

  document.addEventListener("DOMContentLoaded", function () {
    /* Mobile menu */
    var burger = $(".burger"), menu = $(".menu");
    if (burger && menu) burger.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      burger.setAttribute("aria-expanded", open ? "true" : "false");
    });

    /* Current page */
    var here = location.pathname.split("/").pop() || "index.html";
    $$(".menu > li > a").forEach(function (a) { if (a.getAttribute("href") === here) a.setAttribute("aria-current", "page"); });

    /* Year */
    $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });

    /* Cookie consent */
    var ck = $(".cookie");
    if (ck && !store.get("cookie-ok")) ck.classList.add("show");
    $$("[data-cookie]").forEach(function (b) {
      b.addEventListener("click", function () {
        store.set("cookie-ok", b.getAttribute("data-cookie"));
        ck.classList.remove("show");
        if (b.getAttribute("data-cookie") === "all") loadThirdParty();
      });
    });
    if (store.get("cookie-ok") === "all") loadThirdParty();
    else if (store.get("cookie-ok") === "essential") { /* no personalised ads */ loadAds(true); }

    /* Back to top */
    var tt = $(".totop");
    if (tt) {
      window.addEventListener("scroll", function () { tt.classList.toggle("show", window.scrollY > 700); }, { passive: true });
      tt.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
    }

    /* YouTube lite facades */
    $$(".yt[data-id]").forEach(function (el) {
      var id = el.getAttribute("data-id");
      el.innerHTML = '<img loading="lazy" alt="" src="https://i.ytimg.com/vi/' + id + '/hqdefault.jpg"><div class="play"><span>▶</span></div>';
      el.setAttribute("role", "button");
      el.setAttribute("tabindex", "0");
      el.setAttribute("aria-label", "Play video: " + (el.getAttribute("data-title") || "video"));
      var play = function () {
        el.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="' + (el.getAttribute("data-title") || "YouTube video") + '" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
      };
      el.addEventListener("click", play, { once: true });
      el.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); play(); } });
    });

    /* Affiliate links from config */
    $$("[data-aff]").forEach(function (a) {
      var u = (C.affiliates || {})[a.getAttribute("data-aff")];
      if (u) a.href = u;
      a.rel = "sponsored nofollow noopener";
      a.target = "_blank";
    });

    /* Donation buttons from config */
    $$("[data-donate]").forEach(function (a) {
      var u = (C.donate || {})[a.getAttribute("data-donate")];
      if (u) { a.href = u; a.target = "_blank"; a.rel = "noopener"; a.hidden = false; }
      else a.hidden = true;
    });

    initSteppers();
    initForms();
    initCountdowns();
    initTabs();
    initAmountPickers();
  });

  /* Third-party (ads + analytics) */
  var adsLoaded = false;
  function loadAds(nonPersonalised) {
    if (adsLoaded || !C.adsenseClient) return;
    adsLoaded = true;
    var s = document.createElement("script");
    s.async = true;
    s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient;
    document.head.appendChild(s);
    window.adsbygoogle = window.adsbygoogle || [];
    if (nonPersonalised) window.adsbygoogle.requestNonPersonalizedAds = 1;
    $$(".ad-slot").forEach(function (slot) {
      var pos = slot.getAttribute("data-pos") || "content";
      slot.classList.add("filled");
      slot.innerHTML = '<ins class="adsbygoogle" style="display:block" data-ad-client="' + C.adsenseClient + '"' +
        ((C.adSlots || {})[pos] ? ' data-ad-slot="' + C.adSlots[pos] + '"' : "") +
        ' data-ad-format="auto" data-full-width-responsive="true"></ins>';
      try { window.adsbygoogle.push({}); } catch (e) {}
    });
  }
  function loadThirdParty() {
    loadAds(false);
    if (C.ga4) {
      var g = document.createElement("script");
      g.async = true; g.src = "https://www.googletagmanager.com/gtag/js?id=" + C.ga4;
      document.head.appendChild(g);
      window.dataLayer = window.dataLayer || [];
      window.gtag = function () { window.dataLayer.push(arguments); };
      window.gtag("js", new Date()); window.gtag("config", C.ga4);
    }
  }
  /* If no consent banner decision yet, still show contextual (non-personalised) ads after interaction-free delay */
  window.addEventListener("load", function () { if (!store.get("cookie-ok")) setTimeout(function () { loadAds(true); }, 2500); });

  /* Multi-step forms */
  function initSteppers() {
    $$("[data-stepper]").forEach(function (wrap) {
      var steps = $$(".step", wrap), i = 0, bar = $(".progress i", wrap), label = $("[data-step-label]", wrap);
      function show(n) {
        steps.forEach(function (s, k) { s.classList.toggle("active", k === n); });
        if (bar) bar.style.width = ((n + 1) / steps.length * 100) + "%";
        if (label) label.textContent = "Step " + (n + 1) + " of " + steps.length;
        i = n;
      }
      function valid(step) {
        var ok = true;
        $$("input,select,textarea", step).forEach(function (f) {
          if (!f.checkValidity()) { ok = false; }
        });
        if (!ok) { var bad = $(":invalid", step); if (bad) bad.reportValidity(); }
        var group = step.getAttribute("data-require-choice");
        if (ok && group && !$('input[name="' + group + '"]:checked', step)) {
          ok = false; alert("Please choose an option to continue.");
        }
        return ok;
      }
      $$("[data-next]", wrap).forEach(function (b) { b.addEventListener("click", function () { if (valid(steps[i])) show(Math.min(i + 1, steps.length - 1)); }); });
      $$("[data-prev]", wrap).forEach(function (b) { b.addEventListener("click", function () { show(Math.max(i - 1, 0)); }); });
      /* Prefill ZIP from query */
      var q = new URLSearchParams(location.search);
      $$("input[name]", wrap).forEach(function (f) { if (q.get(f.name) && f.type !== "radio" && f.type !== "checkbox") f.value = q.get(f.name); });
      if (q.get("need")) { var r = $('input[name="need"][value="' + q.get("need") + '"]', wrap); if (r) r.checked = true; }
      show(0);
    });
  }

  /* Forms → FormSubmit AJAX (address never rendered in HTML) */
  function endpoint() {
    var id = C.formAlias || atob((C._r || []).slice().reverse().join(""));
    return "https://formsubmit.co/ajax/" + id;
  }
  function initForms() {
    $$("form[data-form]").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        if (!form.checkValidity()) { form.reportValidity(); return; }
        var msg = $(".form-msg", form);
        var btn = $('[type="submit"]', form);
        var hp = $('input[name="_honey"]', form);
        if (hp && hp.value) return;
        var data = {};
        new FormData(form).forEach(function (v, k) {
          if (k === "_honey") return;
          data[k] = data[k] ? data[k] + ", " + v : v;
        });
        data._subject = "[4GNet] " + (form.getAttribute("data-form") || "Form") + " submission";
        data._template = "table";
        data._captcha = "false";
        data.page = location.href;
        data.submitted = new Date().toISOString();
        if (btn) { btn.disabled = true; btn.dataset.t = btn.textContent; btn.textContent = "Sending…"; }
        fetch(endpoint(), {
          method: "POST",
          headers: { "Content-Type": "application/json", "Accept": "application/json" },
          body: JSON.stringify(data)
        }).then(function (r) { return r.json().catch(function () { return {}; }).then(function (j) { return { ok: r.ok, j: j }; }); })
          .then(function (res) {
            if (!res.ok || res.j.success === "false" || res.j.success === false) throw new Error(res.j.message || "Failed");
            done(true);
          }).catch(function () { done(false); });
        function done(ok) {
          if (btn) { btn.disabled = false; btn.textContent = btn.dataset.t; }
          if (msg) {
            msg.className = "form-msg " + (ok ? "ok" : "err");
            msg.textContent = ok ? (form.getAttribute("data-success") || "Thank you! We received your message and will reply within 1 business day.")
              : "Sorry, something went wrong. Please try again in a minute.";
          }
          if (ok) {
            form.reset();
            if (window.gtag) window.gtag("event", "generate_lead", { form: form.getAttribute("data-form") });
            var st = form.closest("[data-stepper]");
            if (st) { var s = $$(".step", st); s.forEach(function (x) { x.classList.remove("active"); }); var d = $(".step-done", st); if (d) d.style.display = "block"; var p = $(".progress i", st); if (p) p.style.width = "100%"; }
          }
        }
      });
    });
  }

  function initCountdowns() {
    $$("[data-countdown]").forEach(function (el) {
      var end = new Date(el.getAttribute("data-countdown")).getTime();
      function tick() {
        var d = Math.max(0, end - Date.now());
        var p = [Math.floor(d / 864e5), Math.floor(d / 36e5) % 24, Math.floor(d / 6e4) % 60, Math.floor(d / 1e3) % 60];
        el.innerHTML = ["Days", "Hours", "Min", "Sec"].map(function (l, k) { return "<div><b>" + p[k] + "</b>" + l + "</div>"; }).join("");
      }
      tick(); setInterval(tick, 1000);
    });
  }

  function initTabs() {
    $$("[data-tabs]").forEach(function (w) {
      var btns = $$("[data-tab]", w);
      btns.forEach(function (b) {
        b.addEventListener("click", function () {
          btns.forEach(function (x) { x.classList.remove("btn-primary"); x.classList.add("btn-ghost"); });
          b.classList.add("btn-primary"); b.classList.remove("btn-ghost");
          $$("[data-panel]", w).forEach(function (p) { p.hidden = p.getAttribute("data-panel") !== b.getAttribute("data-tab"); });
        });
      });
    });
  }

  function initAmountPickers() {
    $$("[data-amount]").forEach(function (b) {
      b.addEventListener("click", function () {
        var f = $('input[name="amount"]'); if (f) { f.value = b.getAttribute("data-amount"); f.focus(); }
        var t = $('select[name="tier"]'); if (t && b.getAttribute("data-tier")) t.value = b.getAttribute("data-tier");
        var sec = document.getElementById("pledge"); if (sec) sec.scrollIntoView({ behavior: "smooth" });
      });
    });
  }
})();
