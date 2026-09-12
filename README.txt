HOW TO TEST THIS RIGHT NOW
---------------------------
1. Unzip this folder anywhere on your computer.
2. Double-click index.html — it opens directly in your browser. No install,
   no server, no internet required except to load the two fonts.
3. Open the same index.html on a second device (or a second browser tab)
   and watch them land on the same photo — that's the sync working.

SWAPPING IN YOUR OWN PHOTOS
----------------------------
1. Drop your image files into the "photos" folder (jpg or png, any size —
   the page resizes everything automatically).
2. Open "manifest.js" in any text editor (Notepad, TextEdit, VS Code, etc.)
   and add a line for each new file, matching the existing format:
       "photos/your-filename.jpg",
   You can remove the dummy photo_01.jpg ... photo_20.jpg lines once you
   don't need them anymore.
3. Save, then reopen (or refresh) index.html.

That's the whole workflow — no rebuilding, no code changes needed for new
photos going forward.

WHAT'S STILL PLACEHOLDER
--------------------------
- The header currently reads "[ Name ] — A Celebration of Life" — send me
  her name and the dates and I'll drop them in.
- START_TIME in index.html is set to "3 minutes ago" so the demo is always
  mid-rotation when you open it. Before the real event, this gets changed
  to the actual date/time (09/19/26, noon) — one line, I'll handle it.

NEXT STEP
----------
Once you're happy with real photos in here, I'll push this same folder to
GitHub Pages, which gives you a real, permanent, unlisted link (and a QR
code for it) to send around and load on the TV — no more zip files.
