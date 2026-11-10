# Feroz & Shajiya — Marriage E-Invitation

A responsive static HTML/CSS/JavaScript wedding invitation in the Emerald Heritage theme.

## Project files
- `index.html` — invitation content and page structure
- `styles.css` — emerald/gold theme, Islamic geometric texture, responsive layout and opening animation
- `script.js` — live countdown, background music control and RSVP interaction
- `assets/images/feroz-shajiya-arabic-logo.png` — the supplied gold Arabic calligraphy couple logo
- `assets/music/` — add your MP3 here as `wedding-music.mp3`

## Logo treatment
The supplied Arabic calligraphy artwork is used as-is with its transparent background. It is centred on the opening screen and styled with a soft gold halo and subtle drop shadow so it sits naturally against the emerald texture. To replace it later, overwrite `assets/images/feroz-shajiya-arabic-logo.png` with another transparent PNG using the same filename.

## Before publishing
1. (Optional) Add your background music at `assets/music/wedding-music.mp3`.
2. (Optional) To send RSVP choices to WhatsApp, open `script.js` and set `whatsappNumber` to the destination number in international format, digits only (example: `919876543210`). Leave it empty for on-page RSVP confirmation only.
3. The venue button currently opens a Google Maps search for Food Village Banquet Hall, Injambakkam, Chennai. Replace the URL in `index.html` with the exact venue pin if available.

## Publish with GitHub Pages
1. Create a GitHub repository, for example `feroz-shajiya-wedding`.
2. Upload the **contents** of this folder (not the containing folder itself) to the repository root.
3. In GitHub, open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**, select `main` and `/ (root)`, then save.
5. Wait for GitHub Pages to publish and open the generated URL.

No build step or framework is required. Google Fonts require an internet connection; the site otherwise runs as a static website.
