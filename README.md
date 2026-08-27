# Shruti Murali — AI & Analytics Portfolio (Static Site)

Same design and content as the Streamlit version, rebuilt as plain HTML/CSS so it loads
**instantly** on GitHub Pages — no server, no cold start, nothing for a recruiter to wait on.

Your 4 project demos still live on Streamlit (they need a real Python backend to run) —
this page just links out to them.

## File structure

```
portfolio-site/
├── index.html
├── style.css
└── assets/
    └── profile.jpg
```

## Deploy on GitHub Pages (free, ~5 minutes)

1. **Create a new GitHub repo.** Go to github.com/new. Name it exactly
   `SHRUTI0907.github.io` if you want your portfolio at the shortest possible URL
   (`https://shruti0907.github.io`) — GitHub treats a repo with that exact name as your
   personal site. If you'd rather keep it at a sub-path instead (e.g.
   `https://shruti0907.github.io/portfolio`), name it anything else, like
   `ai-portfolio`, and skip to step 2 — it works the same way either way.

2. **Push these 3 files/folders to that repo:**
   ```bash
   git init
   git add .
   git commit -m "Portfolio site"
   git branch -M main
   git remote add origin https://github.com/SHRUTI0907/SHRUTI0907.github.io.git
   git push -u origin main
   ```
   (Swap the repo name in the URL if you picked something else in step 1.)

3. **Turn on Pages.** In the repo, go to **Settings → Pages**. Under "Build and
   deployment," set Source to **Deploy from a branch**, branch **main**, folder **/(root)**.
   Save.

4. **Wait ~1 minute**, then visit:
   - `https://shruti0907.github.io` (if you used the special repo name), or
   - `https://shruti0907.github.io/ai-portfolio` (if you used a custom repo name)

   That's your permanent, instant-loading portfolio link. Put it on your resume,
   LinkedIn, and email signature.

## Updating content later

Everything is in `index.html` — project descriptions, live demo links, GitHub links,
skills, experience. Edit the text directly, commit, and push; GitHub Pages redeploys
automatically within a minute or so.

## Why this is faster than the Streamlit version

Your Streamlit portfolio has to spin up a small Python server on every cold visit — that's
where the 30–60 second wait came from. This version is just static files served directly
by GitHub's CDN, so it appears instantly, every time, for every visitor. The 4 project
demos (which actually run Python) still live on Streamlit, since real computation needs a
real backend — this page just links out to them.
