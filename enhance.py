from pathlib import Path
p=Path(__file__).parent
html=(p/'index.html').read_text()
css=(p/'styles.css').read_text()
# Add a subtle ornamental medallion layer to the opening scene.
html=html.replace('<div class="hero-glow"></div>', '<div class="hero-glow"></div>\n      <div class="hero-medallion" aria-hidden="true"></div>\n      <div class="ambient-particles" aria-hidden="true"></div>')
# Add a small ornamental separator before the countdown and between later chapters.
html=html.replace('<section class="countdown-section section" id="countdown">', '<section class="countdown-section section" id="countdown">\n      <div class="section-ornament" aria-hidden="true">✧</div>')
html=html.replace('<section class="section our-day">', '<section class="section our-day">\n      <div class="section-ornament" aria-hidden="true">❋</div>')
html=html.replace('<section class="event-section section" id="event">', '<section class="event-section section" id="event">\n      <div class="section-ornament" aria-hidden="true">✧</div>')
html=html.replace('<section class="section celebration">', '<section class="section celebration">\n      <div class="section-ornament" aria-hidden="true">❋</div>')
html=html.replace('<section class="venue-section section" id="venue">', '<section class="venue-section section" id="venue">\n      <div class="section-ornament" aria-hidden="true">✧</div>')
html=html.replace('<section class="rsvp-section section" id="rsvp">', '<section class="rsvp-section section" id="rsvp">\n      <div class="section-ornament" aria-hidden="true">❋</div>')
(p/'index.html').write_text(html)

extra_css=r'''

/* ROYAL EMERALD EXPERIENCE — ornamental detailing and motion */
:root{--gold-foil:#e9c777;--gold-soft:rgba(233,199,119,.16);--panel:rgba(8,48,39,.72)}
body{background-color:#041f1a}
body:before{opacity:.19;background-image:
  radial-gradient(circle at 1px 1px,rgba(236,202,132,.22) 1px,transparent 1.3px),
  repeating-linear-gradient(45deg,transparent 0 26px,rgba(215,173,88,.055) 27px 28px,transparent 29px 52px),
  repeating-linear-gradient(-45deg,transparent 0 26px,rgba(215,173,88,.045) 27px 28px,transparent 29px 52px);
  background-size:34px 34px,74px 74px,74px 74px;mask-image:linear-gradient(to bottom,black 0%,black 55%,transparent 100%)}
.hero{background:
  radial-gradient(ellipse at 50% 37%,rgba(37,111,82,.38),transparent 48%),
  radial-gradient(ellipse at 50% 100%,rgba(192,139,52,.10),transparent 42%),
  linear-gradient(145deg,#031a16 0%,#07372c 48%,#031b17 100%)}
.hero:before{inset:16px;border:1px solid rgba(233,199,119,.38);box-shadow:inset 0 0 35px rgba(215,173,88,.035),0 0 30px rgba(215,173,88,.035)}
.hero:after{inset:25px;border:1px solid rgba(233,199,119,.16)}
.hero-medallion{position:absolute;left:50%;top:50%;width:min(94vw,760px);aspect-ratio:1;transform:translate(-50%,-50%);border:1px solid rgba(233,199,119,.09);border-radius:50%;pointer-events:none;opacity:.65}
.hero-medallion:before,.hero-medallion:after{content:"";position:absolute;inset:7%;border:1px solid rgba(233,199,119,.10);transform:rotate(45deg);border-radius:23%}
.hero-medallion:after{inset:15%;transform:rotate(22.5deg);border-radius:18%}
.arch-outer{width:min(82vw,610px);top:5%;height:91%;border-color:rgba(233,199,119,.42);box-shadow:0 0 55px rgba(215,173,88,.075),inset 0 0 45px rgba(215,173,88,.045)}
.arch-inner{inset:17px;border-color:rgba(233,199,119,.22)}
.door{background:
  radial-gradient(ellipse at 50% 50%,rgba(16,74,56,.42),transparent 65%),
  repeating-linear-gradient(45deg,transparent 0 34px,rgba(222,183,105,.055) 35px 36px,transparent 37px 68px),
  linear-gradient(90deg,rgba(2,25,20,.99),rgba(5,48,38,.98));
  box-shadow:inset 0 0 35px rgba(0,0,0,.24)}
.door:after{content:"✧";position:absolute;top:50%;color:rgba(233,199,119,.36);font:28px var(--serif)}
.door-left:after{right:22px}.door-right:after{left:22px}
.couple-logo-wrap{width:min(76vw,330px);margin-bottom:22px}
.couple-logo{filter:drop-shadow(0 0 11px rgba(244,217,149,.28)) drop-shadow(0 0 32px rgba(214,165,76,.18)) drop-shadow(0 15px 22px rgba(0,0,0,.35));animation:logoFoil 5.5s ease-in-out infinite}
.logo-halo{inset:8% 4%;background:radial-gradient(ellipse,rgba(230,183,88,.27),rgba(205,150,52,.07) 45%,transparent 72%);filter:blur(30px);animation:breathe 5.5s ease-in-out infinite}
.hero-names{text-shadow:0 0 1px #fff1c4,0 4px 30px rgba(0,0,0,.5);letter-spacing:.015em}
.hero-subtitle{color:#f0e5ce}
.gold-button{background:linear-gradient(115deg,#98651f 0%,#d4a84f 25%,#f5dfa0 50%,#c2923d 76%,#95621d 100%);background-size:200% 100%;box-shadow:0 8px 28px rgba(0,0,0,.22),inset 0 1px rgba(255,255,255,.38);border-color:#f0d38d}
.gold-button:hover{background-position:100% 0;box-shadow:0 12px 32px rgba(0,0,0,.28),0 0 22px rgba(215,173,88,.16)}
.outline-button{border-color:rgba(233,199,119,.72);background:rgba(5,40,32,.4)}
.section{isolation:isolate;overflow:hidden}
.section:before{content:"";position:absolute;inset:13px 14px;border:1px solid rgba(215,173,88,.12);pointer-events:none;z-index:-1}
.section:after{content:"";position:absolute;inset:0;pointer-events:none;z-index:-2;opacity:.35;background:
  radial-gradient(circle at 0 0,rgba(215,173,88,.10),transparent 24%),
  radial-gradient(circle at 100% 100%,rgba(215,173,88,.08),transparent 25%)}
.section-ornament{position:relative;width:48px;height:48px;margin:0 auto 18px;display:grid;place-items:center;color:var(--gold-light);font-size:23px}
.section-ornament:before{content:"";position:absolute;inset:3px;border:1px solid rgba(233,199,119,.42);transform:rotate(45deg)}
.section-ornament:after{content:"";position:absolute;inset:9px;border:1px solid rgba(233,199,119,.2);transform:rotate(0deg)}
.eyebrow{color:#e1bd70;text-shadow:0 1px 15px rgba(215,173,88,.14)}
.gold-rule{width:90px;height:2px;background:linear-gradient(90deg,transparent,#a8782b,#f1d58f,#a8782b,transparent);position:relative}
.gold-rule:after{content:"✦";position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);padding:0 7px;background:#073127;color:#e7c475;font-size:11px}
.invitation{background:
  radial-gradient(ellipse at 50% 48%,rgba(20,91,66,.43),transparent 65%),
  linear-gradient(180deg,#062b23,#07352a 50%,#05271f)}
.parent-details{border:1px solid rgba(215,173,88,.28);outline:1px solid rgba(215,173,88,.08);outline-offset:5px;background:linear-gradient(135deg,rgba(13,66,51,.72),rgba(3,29,24,.68));box-shadow:0 18px 50px rgba(0,0,0,.16);position:relative}
.parent-details:before,.parent-details:after{content:"✧";position:absolute;color:var(--gold);font-size:13px;top:50%;transform:translateY(-50%)}
.parent-details:before{left:10px}.parent-details:after{right:10px}
.couple-names{ text-shadow:0 2px 20px rgba(215,173,88,.12)}
.countdown-section{background:
  radial-gradient(ellipse at 50% 45%,rgba(22,94,68,.42),transparent 62%),
  repeating-linear-gradient(45deg,rgba(215,173,88,.025) 0 1px,transparent 1px 30px),
  linear-gradient(135deg,#031d18,#0a3b2e 50%,#031e18)}
.countdown{width:min(100%,620px);padding:25px 14px;border-top:1px solid rgba(215,173,88,.34);border-bottom:1px solid rgba(215,173,88,.34);background:linear-gradient(90deg,transparent,rgba(215,173,88,.055),transparent)}
.countdown div{position:relative;padding:8px 4px}.countdown div:after{content:"";position:absolute;inset:0;border-left:1px solid rgba(215,173,88,.12);pointer-events:none}.countdown div:first-child:after{border-left:0}
.countdown strong{text-shadow:0 0 24px rgba(215,173,88,.16)}
.event-section{background:
  radial-gradient(ellipse at 50% 50%,rgba(20,78,59,.28),transparent 65%),
  linear-gradient(180deg,#041f1a,#062d24)}
.event-card,.venue-card{position:relative;border:1px solid rgba(233,199,119,.38);outline:1px solid rgba(233,199,119,.10);outline-offset:6px;background:
  linear-gradient(135deg,rgba(18,76,58,.85),rgba(3,28,23,.9)),
  repeating-linear-gradient(45deg,transparent 0 22px,rgba(215,173,88,.06) 23px 24px,transparent 25px 46px);
  box-shadow:0 24px 65px rgba(0,0,0,.24),inset 0 1px rgba(255,255,255,.035)}
.event-card:before,.event-card:after,.venue-card:before,.venue-card:after{content:"✦";position:absolute;color:rgba(233,199,119,.7);font-size:12px}
.event-card:before,.venue-card:before{top:12px;left:14px}.event-card:after,.venue-card:after{bottom:12px;right:14px}
.event-icon,.venue-ornament{display:inline-grid;place-items:center;width:54px;height:54px;border:1px solid rgba(233,199,119,.42);border-radius:50%;box-shadow:0 0 0 6px rgba(215,173,88,.055),0 0 24px rgba(215,173,88,.09);font-size:24px}
.celebration{background:radial-gradient(ellipse at 50% 40%,rgba(22,87,64,.42),transparent 70%),linear-gradient(180deg,#0a392e,#05271f)}
.celebration-list{position:relative;padding:8px 0}
.celebration-list:before{content:"";position:absolute;left:21px;top:24px;bottom:24px;width:1px;background:linear-gradient(180deg,transparent,#c99a48 12%,#c99a48 88%,transparent)}
.celebration-list article{position:relative;gap:22px;padding:27px 18px 27px 0;margin:10px 0;border:1px solid rgba(215,173,88,.20);border-left:0;background:linear-gradient(90deg,rgba(215,173,88,.07),rgba(3,29,24,.16));transition:transform .35s,border-color .35s,background .35s}
.celebration-list article:hover{transform:translateX(5px);border-color:rgba(233,199,119,.48);background:linear-gradient(90deg,rgba(215,173,88,.12),rgba(3,29,24,.22))}
.celebration-list article>span{position:relative;z-index:1;flex:0 0 43px;width:43px;height:43px;display:grid;place-items:center;border:1px solid rgba(233,199,119,.58);border-radius:50%;background:#073127;box-shadow:0 0 0 5px rgba(215,173,88,.055);font:italic 17px var(--serif)}
.celebration-list h3{font-size:19px;letter-spacing:.14em}
.event-time{display:inline-block!important;padding:4px 10px;border:1px solid rgba(215,173,88,.25);background:rgba(215,173,88,.07);font-size:12px!important}
.venue-section{background:radial-gradient(ellipse at 50% 50%,rgba(20,78,59,.32),transparent 68%),#041f1a}
.rsvp-section{background:radial-gradient(ellipse at 50% 42%,rgba(27,97,69,.44),transparent 68%),linear-gradient(180deg,#062c23,#041f1a)}
.rsvp-actions .gold-button,.rsvp-actions .outline-button{min-height:52px;box-shadow:0 8px 28px rgba(0,0,0,.18)}
.closing-section{background:
  radial-gradient(ellipse at 50% 0%,rgba(28,91,67,.35),transparent 54%),
  repeating-linear-gradient(45deg,rgba(215,173,88,.025) 0 1px,transparent 1px 32px),
  linear-gradient(180deg,#062b24,#021813)}
.closing-arabic{padding:24px 15px;border-top:1px solid rgba(215,173,88,.24);border-bottom:1px solid rgba(215,173,88,.24);text-shadow:0 0 22px rgba(215,173,88,.12)}
.hashtag{display:inline-block;padding:5px 14px;border:1px solid rgba(215,173,88,.25);border-radius:30px;background:rgba(215,173,88,.045)}
.music-toggle{box-shadow:0 5px 24px rgba(0,0,0,.24),inset 0 1px rgba(255,255,255,.04)}
.music-toggle:hover{border-color:rgba(244,217,149,.7);box-shadow:0 0 22px rgba(215,173,88,.12)}
.ambient-particles{position:absolute;inset:0;pointer-events:none;overflow:hidden;z-index:2}
.ambient-particles i{position:absolute;bottom:-12px;width:3px;height:3px;border-radius:50%;background:#f2d58d;box-shadow:0 0 9px 2px rgba(235,196,111,.42);opacity:0;animation:floatParticle var(--duration,12s) linear var(--delay,0s) infinite}
@keyframes floatParticle{0%{transform:translate3d(0,0,0) scale(.5);opacity:0}12%{opacity:.7}75%{opacity:.45}100%{transform:translate3d(var(--drift,20px),-105vh,0) scale(1.25);opacity:0}}
@keyframes logoFoil{0%,100%{filter:drop-shadow(0 0 8px rgba(244,217,149,.22)) drop-shadow(0 13px 22px rgba(0,0,0,.32))}50%{filter:drop-shadow(0 0 18px rgba(244,217,149,.48)) drop-shadow(0 13px 25px rgba(0,0,0,.34))}}
.motion-ready .reveal-item{opacity:0;transform:translateY(24px);transition:opacity .85s ease,transform .85s cubic-bezier(.2,.7,.2,1)}
.motion-ready .reveal-item.is-visible{opacity:1;transform:translateY(0)}
.motion-ready .reveal-item:nth-child(2){transition-delay:.08s}.motion-ready .reveal-item:nth-child(3){transition-delay:.14s}.motion-ready .reveal-item:nth-child(4){transition-delay:.2s}
@media(max-width:560px){
  .hero{padding-top:72px;padding-bottom:92px}
  .couple-logo-wrap{width:min(76vw,285px);margin-bottom:18px}
  .hero-medallion{width:112vw}
  .section{padding:88px 22px}
  .section:before{inset:9px}
  .section-ornament{margin-bottom:13px}
  .celebration-list article{gap:15px;padding-right:8px}
  .celebration-list h3{font-size:16px}
  .countdown{padding:20px 5px;gap:4px}
  .countdown div{min-width:0;flex:1}
  .countdown strong{font-size:clamp(29px,8vw,38px)}
  .countdown span{letter-spacing:.1em}
}
@media(prefers-reduced-motion:reduce){.couple-logo,.logo-halo,.ambient-particles i{animation:none!important}.motion-ready .reveal-item{opacity:1!important;transform:none!important}}
'''
(p/'styles.css').write_text(css+extra_css)

js=(p/'script.js').read_text()
insert=r'''

  // Refined entrance effects: reveal content as each chapter enters view.
  const revealTargets = document.querySelectorAll(
    '.section > .eyebrow, .section > h2, .section > p, .section > .gold-rule, .section > .couple-names, .section > .parent-details, .section > .countdown, .section > .event-card, .section > .celebration-list, .section > .venue-card, .section > .rsvp-actions, .closing-section > *'
  );
  if ('IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    revealTargets.forEach(el => el.classList.add('reveal-item'));
    document.body.classList.add('motion-ready');
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -35px 0px' });
    revealTargets.forEach(el => revealObserver.observe(el));
  }

  // Fine golden dust drifting through the opening scene.
  const particleLayer = document.querySelector('.ambient-particles');
  if (particleLayer && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    for (let i = 0; i < 22; i++) {
      const particle = document.createElement('i');
      particle.style.left = `${(i * 47 + 9) % 100}%`;
      particle.style.setProperty('--duration', `${10 + (i % 7) * 2.1}s`);
      particle.style.setProperty('--delay', `${-(i % 11) * 1.7}s`);
      particle.style.setProperty('--drift', `${((i % 5) - 2) * 22}px`);
      particleLayer.appendChild(particle);
    }
  }
'''
js=js.replace("  // Optional: enter the WhatsApp number", insert+"\n  // Optional: enter the WhatsApp number")
(p/'script.js').write_text(js)
