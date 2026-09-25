gsap.registerPlugin(ScrollTrigger);

const $ = (s) => document.querySelector(s);
const $$ = (s) => [...document.querySelectorAll(s)];

const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

// Scroll progress
window.addEventListener("scroll", () => {
  const max = document.documentElement.scrollHeight - window.innerHeight;
  const pct = max > 0 ? (window.scrollY / max) * 100 : 0;
  $("#progress").style.width = `${pct}%`;
}, { passive: true });

// Floating gold particles
const particleRoot = $("#particles");
for (let i = 0; i < 42; i++) {
  const p = document.createElement("span");
  p.className = "particle";
  p.style.left = `${Math.random() * 100}%`;
  p.style.top = `${Math.random() * 100}%`;
  p.style.transform = `scale(${0.4 + Math.random() * 1.7})`;
  particleRoot.appendChild(p);

  if (!reduceMotion) {
    gsap.to(p, {
      opacity: 0.15 + Math.random() * 0.45,
      duration: 1.5 + Math.random() * 2.5,
      delay: Math.random() * 2,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut"
    });
    gsap.to(p, {
      x: (Math.random() - .5) * 100,
      y: (Math.random() - .5) * 160,
      duration: 8 + Math.random() * 10,
      repeat: -1,
      yoyo: true,
      ease: "sine.inOut"
    });
  } else {
    p.style.opacity = ".12";
  }
}

// Hero cinematic reveal
const intro = gsap.timeline({ defaults: { ease: "power3.out" } });
intro
  .to("#logoStage", { opacity: 1, y: 0, scale: 1, duration: 1.7, ease: "expo.out" })
  .fromTo(".wedding-logo", { rotateX: 18, rotateY: -18, z: -80 }, { rotateX: 0, rotateY: 0, z: 0, duration: 1.8, ease: "power4.out" }, "<")
  .to(".light-sweep", { opacity: .9, x: "950%", duration: 1.0, ease: "power2.inOut" }, "-=.35")
  .to(".bismillah", { opacity: 1, y: 0, duration: .8 }, "-=.2")
  .to(".micro", { opacity: 1, y: 0, duration: .7 }, "-=.45")
  .to(".hero-names", { opacity: 1, y: 0, duration: 1.0 }, "-=.25")
  .to(".hero-sub", { opacity: 1, y: 0, duration: .7 }, "-=.55")
  .to(".hero-date", { opacity: 1, y: 0, duration: .6 }, "-=.35")
  .to(".enter-btn", { opacity: 1, y: 0, duration: .7 }, "-=.25");

if (reduceMotion) intro.progress(1);

// Generic scroll reveals
if (!reduceMotion) {
  $$(".dark-section .eyebrow, .dark-section h2, .dark-section .lead, .dark-section .couple-block, .dark-section .body-copy, .section-date, .countdown-grid, .sticky-title, .day-copy, .date-card, .celebration-item, .venue-section .eyebrow, .venue-section h2, .venue-mark, .venue-section h3, .venue-section p, .gold-button, .rsvp-actions, .arabic-closing, .translation, .closing-rule, .closing-copy, .closing-logo-wrap, .final-names, .final-date, .alhamdulillah")
    .forEach((el) => {
      gsap.from(el, {
        scrollTrigger: { trigger: el, start: "top 82%", once: true },
        opacity: 0,
        y: 30,
        duration: 1.0,
        ease: "power3.out"
      });
    });

  gsap.from(".gold-line", {
    scrollTrigger: { trigger: ".gold-line", start: "top 80%", once: true },
    scaleY: 0,
    transformOrigin: "top center",
    duration: 1.3,
    ease: "power3.out"
  });

  gsap.to(".wedding-logo", {
    scrollTrigger: { trigger: "#opening", start: "top top", end: "bottom top", scrub: 1 },
    y: -45,
    scale: .94,
    rotateY: 4
  });
}

// Countdown
const target = new Date("2026-12-20T00:00:00+05:30").getTime();
function updateCountdown() {
  const diff = target - Date.now();
  if (diff <= 0) {
    $("#days").textContent = "000";
    $("#hours").textContent = "00";
    $("#minutes").textContent = "00";
    $("#seconds").textContent = "00";
    return;
  }
  const sec = Math.floor(diff / 1000);
  const days = Math.floor(sec / 86400);
  const hours = Math.floor((sec % 86400) / 3600);
  const mins = Math.floor((sec % 3600) / 60);
  const secs = sec % 60;

  $("#days").textContent = String(days).padStart(3, "0");
  $("#hours").textContent = String(hours).padStart(2, "0");
  $("#minutes").textContent = String(mins).padStart(2, "0");
  $("#seconds").textContent = String(secs).padStart(2, "0");
}
updateCountdown();
setInterval(updateCountdown, 1000);

// Simple sound UI placeholder. No audio file is included yet.
$("#soundBtn").addEventListener("click", () => {
  $("#soundBtn").classList.toggle("active");
});

// Smooth anchor links
$$('a[href^="#"]').forEach(a => {
  a.addEventListener("click", (e) => {
    const targetEl = document.querySelector(a.getAttribute("href"));
    if (!targetEl) return;
    e.preventDefault();
    targetEl.scrollIntoView({ behavior: reduceMotion ? "auto" : "smooth" });
  });
});
