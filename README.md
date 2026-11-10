# Feroz & Shajiya — Python-assisted static wedding invitation

This project uses **Option A**: Python generates/validates the static site assets; GitHub Pages serves the resulting HTML, CSS, JavaScript, images and audio. GitHub Pages does not execute Python on its server.

## Important files
- `index.html`, `styles.css`, `script.js` — static invitation website
- `feroz-shajiya-arabic-logo.png` — logo at repository root for a simple, reliable relative path
- `assets/images/feroz-shajiya-arabic-logo.png` — duplicate fallback logo
- `assets/images/islamic-geometric-tile.svg` — Python-generated ornamental texture
- `assets/music/wedding-music.mp3` — supplied nasheed
- `build.py` — validates assets and creates a deployable `dist/` folder

## Build locally (optional)
Run:
```bash
python build.py
```
Then upload the **contents of `dist/`** to the root of the GitHub Pages repository.

## GitHub Pages update
Upload/replace `index.html`, `styles.css`, `script.js`, `feroz-shajiya-arabic-logo.png`, and the complete `assets/` folder in the repository root. Commit the changes. Keep the repository's existing Pages configuration (`main` / root).

## Family wording
Feroz Khan — S/O Mr. S. I. Syed Ismail & Mrs. N. K. Samsath Begum
Shajiya Thabasum — D/o Mr. M. Usman Baig & Mrs. U. Rasul Nisha

No "Groom" or "Bride" labels are displayed.


## Music troubleshooting
The music is user-initiated (tap the Music button; browsers block unsolicited autoplay). The player tries `wedding-music.mp3` in the repository root first, then `assets/music/wedding-music.mp3`. Upload both copies or at least keep the complete `assets/` folder. If it still fails, open the direct audio URL:
`https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/wedding-music.mp3`
If that URL returns 404, the audio file was not uploaded to the repository root.

## Calendar
The Save the Date section includes a Google Calendar event link and a downloadable `.ics` event. The calendar entry spans 10:30 AM–3:00 PM IST and lists each function's individual timing in the description.
