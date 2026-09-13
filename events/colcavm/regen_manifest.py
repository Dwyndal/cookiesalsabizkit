#!/usr/bin/env python3
"""
Regenerates manifest.js by listing every file currently in the photos/
folder, sorted alphabetically. Run this any time photos are added or
removed by hand (outside of a Claude-provided drop-in zip) so the
carousel picks up the current file list.

Usage (from inside the event folder, e.g. events/colcavm/):
    python3 regen_manifest.py
"""
import os

PHOTOS_DIR = "photos"
OUTPUT_FILE = "manifest.js"
VALID_EXT = (".jpg", ".jpeg", ".png")

files = sorted(f for f in os.listdir(PHOTOS_DIR) if f.lower().endswith(VALID_EXT))

lines = [
    "// Drop new photo files into the /photos folder, then list the filenames here.",
    "// Order in this list has no effect on playback order (that's shuffled) —",
    "// it only sets each photo's permanent reference number.",
    "const PHOTO_FILES = [",
]
lines += [f'  "photos/{f}",' for f in files]
lines.append("];")

with open(OUTPUT_FILE, "w") as out:
    out.write("\n".join(lines) + "\n")

print(f"{OUTPUT_FILE} regenerated with {len(files)} photos.")
