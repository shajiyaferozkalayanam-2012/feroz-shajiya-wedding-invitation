# Feroz & Shajiya — Wedding E-Invitation

A cinematic Muslim wedding e-invitation for:

- Feroz Khan
- Shajiya Thabasum
- Sunday, 20 December 2026
- Food Village Banquet Hall, Injambakkam, Chennai

## Run locally

Open `index.html` in a browser, or use a simple local server:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## GitHub Pages

1. Create a GitHub repository.
2. Upload the contents of this folder to the repository root.
3. Go to **Settings → Pages**.
4. Choose **Deploy from a branch**.
5. Select the `main` branch and `/root`.
6. Save.

The invitation will be available at your GitHub Pages URL.

## Notes

- GSAP is loaded from jsDelivr CDN.
- Google Fonts are loaded from Google Fonts.
- The venue button uses the supplied Google Maps short link.
- The two RSVP buttons currently open WhatsApp with prefilled messages. Replace those links with the desired RSVP/WhatsApp destination.
- The uploaded original logo is retained in `assets/logo-original.png`.
- `assets/logo-transparent.png` is the processed transparent-background version used by the site.
