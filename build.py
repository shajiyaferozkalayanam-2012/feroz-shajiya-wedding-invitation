#!/usr/bin/env python3
"""Build and validate the static GitHub Pages edition of the wedding invitation."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
REQUIRED = [
    ROOT / "index.html",
    ROOT / "styles.css",
    ROOT / "script.js",
    ROOT / "feroz-shajiya-arabic-logo.png",
    ROOT / "assets/images/feroz-shajiya-arabic-logo.png",
    ROOT / "assets/images/islamic-geometric-tile.svg",
    ROOT / "assets/music/wedding-music.mp3",
]
missing = [str(p.relative_to(ROOT)) for p in REQUIRED if not p.is_file()]
if missing:
    raise SystemExit("Missing required files: " + ", ".join(missing))

if DIST.exists():
    shutil.rmtree(DIST)
DIST.mkdir(parents=True)
for name in ["index.html", "styles.css", "script.js", "feroz-shajiya-arabic-logo.png", "assets"]:
    src = ROOT / name
    dst = DIST / name
    if src.is_dir():
        shutil.copytree(src, dst)
    else:
        shutil.copy2(src, dst)

print(f"Built static site at: {DIST}")
print("Validated logo and music assets.")
print("Upload the CONTENTS of dist/ to the GitHub Pages repository root.")
