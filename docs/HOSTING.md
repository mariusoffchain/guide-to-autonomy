# Hosting an edition

The build produces a folder of static files (`dist/` by default): HTML pages, 1 stylesheet, scripts that run in the reader's browser, fonts and images, the page "Licences, credits and source" with the full licence and notice texts (`legal/`), a ZIP of the edition's source (`source/`), `release-manifest.json`, and optionally `sw.js`, `sitemap.xml` and `robots.txt`. Any service that serves static files can host it. No server-side language, no database, no environment variable, no secret.

## Upload only the clean export

`dist/` can hold files that are not part of the current build: pages of a chapter you removed, an older `build-report.json` written there by a previous version of the build. The build never deletes them. So do not upload `dist/` itself. Make a clean export:

```bash
python3 release.py --edition edition.json --out dist --dest publish
```

It builds the edition, then copies into `publish/` exactly the files listed in `dist/release-manifest.json` after checking their SHA-256, and names the files of `dist/` it left out. `publish/` must not exist or must be empty: the command refuses to write into a folder that already holds files, and never removes anything. For the next release, use a new folder name or empty `publish/` yourself. **Upload the contents of `publish/` and nothing else.** For a folder edition: `python3 release.py --edition examples/<slug>/edition.json --out dist-<slug> --dest publish-<slug>`.

The internal build report is written next to the output folder (`dist.build-report.json`), never inside it, and is not published. It is ignored by Git.

The export publishes your edition's code to its readers, so it carries what they are entitled to: the licences, `NOTICE`, the notices of the fonts it serves, the credit to the original work, and the ZIP of the exact source it was built from, linked from every page footer. Describe your changes in `edition.changes` and `edition.modified` (see `CONFIGURATION.md`). A public repository is welcome but does not replace those files.

Before publishing, set `site.url` (and `site.base_path` if the book is not at the root) in `edition.json` and rebuild, so that the canonical links and the sitemap carry the real address. The GitHub Pages workflow below does it for you. Elsewhere, if you do not know the address yet, publish once with `url` empty, then set it and publish again, or pass the address for 1 build: `python3 release.py --edition edition.json --out dist --dest publish --site-url https://guide.example.org --base-path /`.

Two things to get right whatever the host:

1. **Serve the export at exactly `base_path`.** Internal links are absolute from that path. At the root of a domain, `base_path` is `/` and you upload the contents of `publish/`. Under `https://example.org/guide/`, `base_path` is `/guide/` and the contents of `publish/` must land in the `guide` folder.
2. **Folder addresses must serve `index.html`.** Every page is `…/chapter-id/index.html`. All the hosts below do this by default.

HTTPS is needed for the offline copy (`site.offline`) and is a good idea anyway; every host below provides it.

## Option A: build on your computer, upload the folder

The simplest and the most portable. Make the clean export, then copy `publish/` to the host.

- **Any web server you rent or run** (nginx, Apache, Caddy, a shared host with FTP/SFTP): upload the contents of `publish/` into the document root or the chosen folder. Nothing to configure. If you can set headers, add `Cache-Control: no-cache` on `*.html` and `sw.js`, and a long `max-age` on `/assets/` (their addresses change with their content). When you replace an older upload, remove the files on the server that are not in the new `release-manifest.json`.
- **Netlify, Cloudflare Pages, Vercel (drag and drop)**: create a project, choose "deploy manually" or "upload folder", drop `publish/`. Each service gives you a `*.pages.dev` / `*.netlify.app` address and lets you attach your domain later.
- **A Nextcloud, Synology or home server**: put the folder behind any static file server. The book has no dependency on a domain name.

Repeat after each change. This option leaves nothing of the build on the host and needs no account on a forge.

## Option B: let the forge build it (GitHub Pages, Codeberg Pages, Gitea)

Your fork already lives on a forge; it can also build and publish the pages when you ask it to.

### From your computer to your fork

If your edition lives in a clone of the base or in a local repository, put it on your own fork before publishing:

1. On the base repository's page, click **Fork** (keep the default name or choose one; GitHub forks are public).
2. In your folder, keep the base as `upstream` and point `origin` at your fork:

   ```bash
   git remote rename origin upstream
   git remote add origin https://github.com/<you>/<repository>.git
   git push -u origin main
   ```

   Without any remote yet, skip the rename. If your edition was committed on another branch, merge it into `main` first: the workflow and GitHub Pages use the default branch.
3. Set `edition.repository` to the fork's address, commit and push.

### GitHub Pages

The repository ships `.github/workflows/pages.yml`. It installs Python-Markdown, runs the tests, builds with `release.py` and publishes the clean export `publish/`, never `dist/`. It runs only when started by hand; a push does not trigger it, and it needs no secret.

1. In a fork, open the Actions tab once and enable workflows (GitHub disables them in new forks).
2. Settings > Pages > Build and deployment > Source: **GitHub Actions**.
3. Actions tab > "Build and publish the edition" > **Run workflow**, on the default branch (the only one GitHub Pages deploys from unless you change the rules of the `github-pages` environment). 2 choices:
   - `edition`: the edition file, `edition.json` by default, or `examples/<slug>/edition.json`.
   - `address`: `github-pages` (default) writes the address GitHub gives this site into the canonical links and the sitemap: `https://<user>.github.io/<repository>/`, or your custom domain once it is set in Settings > Pages. `edition.json` uses `site.url` and `site.base_path` of the edition file unchanged.
4. When the run is green, its summary shows the address. Check it with the list at the end of this page.

The address is right from the first run, even with an empty `site.url`. The source ZIP of that build says which address was used (`SOURCE-README.txt`), so the same pages can be rebuilt. With the `gh` command-line tool, step 3 is `gh workflow run pages.yml -f edition=edition.json -f address=github-pages`.

Custom domain: set it in Settings > Pages (GitHub adds a `CNAME` record on its side; follow its DNS instructions), then run the workflow again. With `address: github-pages`, the pages then carry the custom domain and `base_path` `/`.

A second workflow, `.github/workflows/checks.yml`, runs the tests and `build.py --check` on pull requests or when started by hand. It publishes nothing.

### Codeberg Pages

Codeberg serves the content of a branch named `pages` of a public repository at `https://<user>.codeberg.page/<repository>/`. Its documentation, read on 2026-10-23, says the service moved to a new codebase (git-pages) and that publishing is triggered by a webhook filtered on the `pages` branch, or by Forgejo Actions: follow https://docs.codeberg.org/codeberg-pages/ for that one-time setup, which may change. The simplest route with no CI: make the clean export locally, then push `publish/` to the `pages` branch. A small script does it (`rsync --delete` removes, in the `pages` worktree only, the files of the previous publication that are not in the new export):

```bash
python3 release.py --edition edition.json --out dist --dest publish
git worktree add -B pages ../pages-worktree
rsync -a --delete --exclude .git publish/ ../pages-worktree/
cd ../pages-worktree && git add -A && git commit -m "Publish" && git push -u origin pages
```

Set `site.base_path` to `/<repository>/`. With Woodpecker CI enabled on your account, the same steps can run when you start them; the `pages.yml` workflow is a starting point to translate.

### Gitea or Forgejo you host yourself

Recent Forgejo and Gitea versions can serve static sites with Forgejo Actions (GitHub-compatible syntax: `.github/workflows/pages.yml` runs mostly unchanged with a runner) or with a separate pages server. If that is not set up, Option A against the same machine's web server is 1 `rsync` away and just as valid.

## Caching and the offline copy

Pages and `sw.js` should not be cached for long by the browser or a CDN; assets under `/assets/` can be cached for a year because their file names change with their content (`?v=`). The offline copy includes the legal page and the licence and notice texts, but not the source ZIP, which is downloaded only on demand. When `site.offline` is on, a reader who already has the offline copy sees the previous version on the first load after you publish, while the new copy is saved; the colophon states it. If you cannot explain that to your readers, leave `offline` off: the pages are small and load fast anyway.

## Several editions, one domain

Give each edition its own `base_path` (`/en/`, `/lt/`, `/guide/`) and its own `storage_key`, so that ticks never mix. List the others in each edition's `other_editions` so readers can switch.

## Headers, if you can set them

Not required. On a server you control: `Cache-Control: no-cache` on `*.html`, `sw.js` and `release-manifest.json`; `Cache-Control: max-age=31536000, immutable` on `/assets/` (their addresses carry a version); `X-Content-Type-Options: nosniff`; `Referrer-Policy: no-referrer`. The pages already carry their Content-Security-Policy in a `<meta>` tag; a stricter header of your own must still allow what the cover needs when recordings are enabled (see `CONFIGURATION.md`, recordings).

## Checking a deployment

Open the public address and check: the cover, 1 chapter, the footer link "Licences, credits and source" and the ZIP it offers, a tick that survives a reload, the search, the address of the canonical link in the page source (View source, search `canonical`), and `…/sitemap.xml` if `site.url` is set. On a phone, open a chapter and the "On this page" button. That is the whole acceptance test. For a first publication or after an update of the base, also:

- a private window: the counters of the cover say 0 and nothing is ticked;
- the keyboard only: Tab reaches the skip link, the contents button and the search; `/` opens the search, Escape closes it; a chapter's checkbox toggles with Space;
- a narrow window (about 390 px): no sideways scrolling of the page, tables scroll inside their frame;
- the browser console: no error.
