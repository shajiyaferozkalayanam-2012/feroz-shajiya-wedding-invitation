(() => {
  // Always open shared/reloaded invitation URLs at the first landing screen.
  // The Enter Our Story button still navigates to #invitation after the visitor taps it.
  if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
  function resetSharedLandingUrl() {
    if (window.location.hash) {
      history.replaceState(null, document.title, window.location.pathname + window.location.search);
      window.scrollTo(0, 0);
    }
  }
  window.addEventListener('pageshow', resetSharedLandingUrl);
  resetSharedLandingUrl();


  // Logo fallback: try the repository-root image first, then the assets path.
  const coupleLogo = document.getElementById('coupleLogo');
  if (coupleLogo) {
    coupleLogo.addEventListener('error', () => {
      if (coupleLogo.dataset.fallbackTried !== 'true') {
        coupleLogo.dataset.fallbackTried = 'true';
        coupleLogo.src = './assets/images/feroz-shajiya-arabic-logo.png';
      }
    });
  }

  const weddingDate = new Date('2026-12-20T09:30:00+05:30').getTime();
  const fields = {
    days: document.getElementById('days'),
    hours: document.getElementById('hours'),
    minutes: document.getElementById('minutes'),
    seconds: document.getElementById('seconds')
  };
  const pad = value => String(value).padStart(2, '0');
  function updateCountdown() {
    let remaining = Math.max(0, weddingDate - Date.now());
    const day = Math.floor(remaining / 86400000); remaining %= 86400000;
    const hour = Math.floor(remaining / 3600000); remaining %= 3600000;
    const minute = Math.floor(remaining / 60000); remaining %= 60000;
    const second = Math.floor(remaining / 1000);
    fields.days.textContent = String(day);
    fields.hours.textContent = pad(hour);
    fields.minutes.textContent = pad(minute);
    fields.seconds.textContent = pad(second);
  }
  updateCountdown();
  setInterval(updateCountdown, 1000);

  const hero = document.querySelector('.hero');
  const enterLink = document.querySelector('.hero .gold-button[href="#invitation"]');
  enterLink.addEventListener('click', () => hero.classList.add('entered'));

  const music = document.getElementById('weddingMusic');
  const musicToggle = document.getElementById('musicToggle');
  const musicLabel = document.getElementById('musicLabel');
  const musicSources = ['./wedding-music.mp3', './assets/music/wedding-music.mp3'];
  let musicSourceIndex = 0;

  function setMusicLabel(label, ariaLabel) {
    musicLabel.textContent = label;
    musicToggle.setAttribute('aria-label', ariaLabel);
  }

  music.addEventListener('error', () => {
    if (musicSourceIndex < musicSources.length - 1) {
      musicSourceIndex += 1;
      music.src = musicSources[musicSourceIndex];
      music.load();
    } else {
      setMusicLabel('Audio unavailable', 'Wedding music could not be loaded');
    }
  });

  music.addEventListener('playing', () => setMusicLabel('Music on', 'Pause background music'));
  music.addEventListener('pause', () => {
    if (!music.ended && !music.error) setMusicLabel('Music off', 'Play background music');
  });

  musicToggle.addEventListener('click', async () => {
    if (!music.paused) {
      music.pause();
      return;
    }
    try {
      if (music.readyState === 0) {
        music.src = musicSources[musicSourceIndex];
        music.load();
      }
      await music.play();
      setMusicLabel('Music on', 'Pause background music');
    } catch (error) {
      // If the root-level audio file is absent, try the assets folder once.
      if (musicSourceIndex < musicSources.length - 1) {
        musicSourceIndex += 1;
        music.src = musicSources[musicSourceIndex];
        music.load();
        try {
          await music.play();
          setMusicLabel('Music on', 'Pause background music');
          return;
        } catch (fallbackError) {
          setMusicLabel('Tap to retry', 'Retry wedding music');
        }
      } else {
        setMusicLabel('Tap to retry', 'Retry wedding music');
      }
    }
  });


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

  // Optional: enter the WhatsApp number in international format, digits only.
  // Leave empty to keep RSVP as an on-page selection only.
  const whatsappNumber = '918925019882';
  const rsvpNote = document.getElementById('rsvpNote');
  document.querySelectorAll('.rsvp-button').forEach(button => {
    button.addEventListener('click', () => {
      const response = button.dataset.response;
      rsvpNote.textContent = `Your response: ${response}. JazakAllah Khair.`;
      if (whatsappNumber) {
        const message = `Wedding RSVP for Feroz Khan & Shajiya Thabasum (20 December 2026): ${response}`;
        window.open(`https://wa.me/${whatsappNumber}?text=${encodeURIComponent(message)}`, '_blank', 'noopener');
      }
    });
  });
})();
