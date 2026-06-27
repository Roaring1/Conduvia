/*
 * Conduvia reveal-on-scroll animations.
 * Self-hosted, zero-dependency, and FAIL-SAFE: content is visible by default.
 * Elements only start hidden once we KNOW JS + IntersectionObserver work, so a
 * blocked CDN, slow network, or disabled JS can never leave the page blank.
 */
(function () {
  "use strict";
  var SELECTOR = ".md-typeset h2, .md-typeset h3, .visual-placeholder, " +
    ".recipe-card, .station-card, .start-card, .rung, .field-card";

  function enable() {
    // Respect reduced-motion preference: leave everything visible, no motion.
    var reduce = window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce || !("IntersectionObserver" in window)) return;

    var els = Array.prototype.slice.call(document.querySelectorAll(SELECTOR));
    if (!els.length) return;

    // Mark <html> so CSS knows the reveal system is live; only NOW do the
    // targeted elements get their start (hidden) state.
    document.documentElement.classList.add("anim-ready");
    els.forEach(function (el) { el.classList.add("reveal"); });

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("in");
          io.unobserve(e.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.02 });

    els.forEach(function (el) { io.observe(el); });

    // Safety net: if anything is still hidden after 1.5s (e.g. tall page,
    // observer hiccup), force it visible so content is never lost.
    setTimeout(function () {
      els.forEach(function (el) { el.classList.add("in"); });
    }, 1500);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", enable);
  } else {
    enable();
  }
})();
