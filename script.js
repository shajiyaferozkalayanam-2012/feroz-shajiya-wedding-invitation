(() => {
  const weddingDate = new Date('2026-12-20T00:00:00+05:30').getTime();
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
  musicToggle.addEventListener('click', async () => {
    if (music.paused) {
      try {
        await music.play();
        musicLabel.textContent = 'Music on';
        musicToggle.setAttribute('aria-label', 'Pause background music');
      } catch (error) {
        musicLabel.textContent = 'Add music file';
      }
    } else {
      music.pause();
      musicLabel.textContent = 'Music off';
      musicToggle.setAttribute('aria-label', 'Play background music');
    }
  });

  // Optional: enter the WhatsApp number in international format, digits only.
  // Leave empty to keep RSVP as an on-page selection only.
  const whatsappNumber = '';
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
