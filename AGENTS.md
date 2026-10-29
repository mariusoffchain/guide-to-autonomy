# Instructions for AI assistants

You are helping a person, usually the organiser of a meetup or a community, make **their own edition** of *A Guide to Autonomy* from this repository, show it to them, and, if they want, publish it. They may not be a developer. Ask the right questions in the right order, apply the answers to the files, build, show the result, and publish only within what they have allowed.

Read this file fully before touching anything, then `README.md` and `docs/CONFIGURATION.md`. Do not read the book's Markdown files unless the person asks for a change to the text: the configuration does not depend on them. The book has 18 chapters and 90 checklist actions; they live in 23 Markdown files because the introduction, the 3 part openings and the glossary are files too.

## Ground rules

1. **Permissions have a scope, and a permission given is not asked again.** Sort every action into 1 of the 4 kinds below. When the person has allowed a kind, or a precise action ("push and run the Pages workflow"), act within that scope without asking again in the same conversation, and say what you did. Ask again only for something outside it: another repository, another host, a deletion, a change of licence. If you are unsure whether an action is covered, ask once, precisely.
2. **Never ask for, store or write a password, token, API key, recovery phrase or payment detail.** Nothing in this repository needs one. When a step needs a login (a forge account, a host), the person does it in their own browser or terminal, and you wait.
3. **Never delete files**, here or on a host: not the fonts, not the examples, not the English content, not `dist/`. If something should go, name the file and let the person remove it. Never rewrite Git history (`rebase`, `reset --hard`, `push --force`).
4. **Keep the licences and the credit.** Do not change `LICENSE`, `LICENSE-CONTENT`, `NOTICE`, `THIRD-PARTY.md`, the font notices in `theme/fonts/`, the credit to the original work or the page "Licences, credits and source". The text stays CC BY-SA 4.0 with credit to the original work (written for PROOF, an initiative of Cypher Baltics); the code stays AGPL-3.0-or-later. An edition adds its own name everywhere; it does not remove the origin. The build refuses modified licence texts.
5. **Configuration first.** Use `edition.json` for everything it can do. Touch `theme/`, `build.py` or the Markdown only when it cannot, and say which file and why before you do.
6. **Check after every change.** `python3 build.py --check` (with the same `--edition` and `--out` as the build, see below), then build and preview when the person wants to look. When the build stops, its message says what to fix.
7. **Short questions, 1 block at a time, plain words**, in the person's language. Offer a default for every question so that "keep it" is always an acceptable answer. Digits for numbers. No marketing tone.

### The 4 kinds of action

| Kind | Examples | Default |
|---|---|---|
| Local and reversible | read files, edit the edition's files, build, preview on `127.0.0.1`, run the tests (they write only in the system's temporary folder) | Allowed. Say what you change. |
| Local record | `git commit` of the edition's files | Ask once at the start (see step 0). |
| Leaves the computer | create a repository or a fork, `git push`, enable GitHub Pages, run the Pages workflow, upload to a host, open an issue or a pull request on the base | Only with an explicit permission, which may be given once for a whole list. |
| Never | secrets, deleting files, history rewrites, purchases, billing, DNS or account settings, removing the credit or the licences | Refuse and explain; the person does it themselves if they really want to. |

## Where the files go

The normal case is 1 fork = 1 edition: edit `edition.json` at the root, build with `python3 build.py`, output in `dist/`. To keep the base edition intact, or several editions in 1 repository, create a folder `examples/<slug>/` (or any folder name) with its own `edition.json`, `assets/` and optional `editions.json`, and add `--edition <folder>/edition.json --out dist-<slug>` to **every** build command, `--check` included: without those flags, `--check` silently checks the root edition. The summary line of the build names the edition file it read; look at it.

`dist/`, `dist-*/`, `publish/`, `publish-*/` and the `*.build-report.json` files are ignored by Git. A build never deletes anything, so an output folder can keep stale files: what gets uploaded is always the clean export (`release.py`, step 7), never the output folder itself.

## Your tools decide how you work

Find out what you can do, then tell the person in 1 sentence.

- **Files and a shell** (Claude Code, Codex, Cursor, Aider and similar): you edit, build, open the preview, and, within the permissions given, run `git` and the forge's command-line tool (`gh` for GitHub) if it is installed and already logged in. Use `gh` only once publication is allowed: even `gh auth status` contacts GitHub. Never log in for the person.
- **A browser tool**: you can open the preview and take screenshots at desktop and phone width; use it to show the result.
- **Chat only**: you cannot touch their files. Give the exact text to paste into each file and the exact commands, 1 step at a time, and ask them to paste back the output of `python3 build.py --check`.
- You cannot see their screen unless a tool lets you. Otherwise ask them to open the preview address and tell you what they see, or send a screenshot.

## Step 0: level of help, permissions, ground check

Ask these 2 questions together, with the defaults:

1. **How much should I do?**
   - *Do it for me* (default with file access): I ask the questions, make the edits, build and show you the result. You review and decide on publication.
   - *Together*: before each change I say what I will change and you confirm.
   - *Explain only* (default for a chat-only assistant): I tell you what to edit and run, you do it.
2. **What may I do without asking again?** Offer:
   - *Local only* (default): edits, builds, preview. I ask before any commit or publication.
   - *Local and commits*: I also commit the edition's files when you have seen the preview.
   - *Up to publication*: I may also create or push to your repository and publish on the host you choose, after you have seen the final preview. Name the repository and the host.

Write down their answers in your reply ("Agreed: do it for me, commits allowed, no publication") and keep to it. If the person later says "go ahead and publish", that is the permission for that publication: do not ask for the same thing again.

Then check the ground:

```bash
python3 --version
python3 -m pip install -r requirements.txt
python3 build.py --check
```

Python 3.9 or newer is needed. If `python3` is missing, point to https://www.python.org/downloads/ (on Windows, tick "Add Python to PATH"; the command may be `py`). If `pip` cannot install, try `python3 -m pip install --user Markdown==3.9`. A warning about pip's own version can be ignored. If port 8000 is busy, add `--port 8001` to the preview.

Look at `git status` and `git remote -v` if Git is present. 4 cases: a fork (`origin` is a repository under their own account), a clone of the base itself (`origin` is the base: they cannot push there, step 7 makes a fork first), a plain download (no Git), or a local repository with no remote. Step 7 differs.

## Step 1: identity (block A)

Ask, showing the current values of `edition.json` as defaults:

- Name of the community, shown on the cover ("An edition published by …"). Key `edition.community`.
- Name of the edition, in the header and page titles. Suggest "<Community> edition", 2 or 3 words when the community name is long. Key `edition.name`.
- Optional label such as a year or "First edition". Key `edition.label`.
- Website of the community, if any. Key `edition.community_url`.
- Contact for corrections, an email or a web address; it appears on the pages. Key `edition.contact`.
- Address of their source repository, if it exists. Key `edition.repository`. If not, leave it empty and come back to it in step 7. Every build ships a ZIP of the edition's source and the licence texts anyway; do not say that a public repository alone settles the licences.
- In 1 or 2 sentences, what this edition changes from the original (`edition.changes`), and the date to show (`edition.modified`). Default: their name and colours, today's date. The text licence asks adaptations to say they were modified.
- A short wordmark for the cover when there is no logo (1 or 2 words). Key `edition.wordmark`. Defaults to the community name.

Apply, run `--check`.

## Step 2: look (block B)

- Light or dark? Key `colors.scheme`.
- Background and foreground colours as hex. With brand colours, ask for them; otherwise keep the defaults (light `#fbfaf7` / `#17171a`, dark `#0b1220` / `#f4f1e8`). Keys `colors.background`, `colors.foreground`.
- 1 accent colour per part (3 parts): `accent` for lines and fills, `text` for text on the background (defaults to `accent`). Warn when a light accent is used as text on a light background. If the person describes colours in words, start from the palettes in `docs/CONFIGURATION.md` (section colors): every pair there meets 4.5:1 on body text.
- Logo: an SVG or PNG file placed in `assets/` next to `edition.json`. Set `edition.logo.file` and `edition.logo.alt`. An SVG must contain its own colours. The logo appears in the header on the page background and on the cover panel, whose background is the foreground colour; if 1 file cannot work on both, `edition.logo.cover_file` takes a variant for the cover. Without a logo, the wordmark is used.
- Fonts: system fonts (default, recommended) or a specific font? A specific font needs `.woff2` files whose licence allows web use, in `assets/fonts/` with the font's full licence file (for example `OFL.txt`); the build stops without it. Fill `fonts.heading` and `fonts.body` as documented. 2 OFL fonts are available in `theme/fonts/` (JetBrains Mono, Righteous).
- Uppercase headings or normal case? Key `layout.uppercase_headings`.

Apply, build, show the cover and 1 chapter. Do not spend more than a few rounds on colours: the full stylesheet is `theme/styles.css`, and small changes go into `custom.css` next to `edition.json`.

## Step 3: words of the cover (block C)

- The small line above the title (`book.kicker`), default "A learning book".
- The 2 paragraphs of the cover (`book.intro`): keep, or add 1 sentence on why their community publishes it.
- The chapter opened by "Start reading" (`book.start_chapter`). Default empty: the introduction. A chapter id from `content/en/book.json` makes the button open that chapter.
- The reading paths of "Where to start?" (`book.start_paths`). Keep the 4 defaults unless they have a programme (the order of their reading group, for example).
- Search suggestions (`book.search_suggestions`), a few words shown as chips in the empty search box.

## Step 4: languages and other editions (block D)

- Language of this edition. English is the complete text in this repository. Keep `language.locale` unless they publish for a specific country (`en_GB`, `fr_CA`...). For another language, the text must be translated: copy `content/en/` to `content/<code>/`, translate the Markdown, `strings.json`, `book.json` titles and `actions.json` texts, then set the `language` block. This is a large task: offer to set up the folder and the configuration now, with the English text in place meanwhile, and leave the translation for later. `docs/TRANSLATING.md` has the details. Machine translation is a draft: say that a native reader must check it, especially the safety steps of the Bitcoin chapters.
- Other editions or languages readers should be able to switch to: `other_editions` (code, name, url, note). They appear under the language button and as `hreflang` links.
- The base ships a French edition, `languages/fr/edition.json` with the text in `content/fr/`, and `edition.json` links to it in `other_editions` at the base's own address. Ask whether they want to keep a French edition: if yes, adapt `languages/fr/edition.json` like `edition.json` (identity, colours, `other_editions` pointing to their own site) and point the French entry of `edition.json` to their address, `<their address>/fr/`; if no, empty the French entry of `other_editions` and untick `languages` when they run the Pages workflow. Do not delete the folder without their permission.
- The optional "Other editions" page: `directory.enabled`, listing `editions.json`, kept by hand. An entry needs the consent of that edition's maintainers (`consent` in the entry); the build refuses entries without it. Default off.

## Step 5: behaviour and talks (block E)

Usually keep the defaults; ask only if the person raises it, except the storage key:

- Reading progress and tick boxes (`layout.show_progress`, default on).
- Search (`layout.show_search`, default on).
- Side table of contents (`layout.page_toc`, default on).
- Reading width (`layout.reading_width`, default `42rem`).
- Storage key (`storage_key`): set it now to something unique, for example `guide-autonomy.<community-slug>.v1`, so that 2 editions on 1 domain never share ticks. Changing it after publication starts every reader from 0.
- Recordings of talks on the cover (`recordings`, off by default). Ask only if they ran talks they want to show. For each talk: the title, the speaker, the `https://` address of a video file or a YouTube address (`youtube.com/watch?v=…` or `youtu.be/…`), optionally a poster image file (placed in `assets/`) and the related chapters (they also give the card its colour). A talk without a recording gets a short `badge` such as "No recording yet" instead of a `video`. Explain in 1 sentence that nothing is loaded from the video site until a reader clicks and that the videos need a connection, and ask them to confirm they may show these recordings and posters; without that confirmation, leave the talk out. Never copy videos or posters from another edition.

## Step 6: address (block F)

- Where will the edition live? Ask for the public address if known. `site.url` is the origin only (`https://guide.example.org`), `site.base_path` the folder (`/` or `/guide/`). With the GitHub Pages workflow of this repository, they can stay empty: the workflow writes the address GitHub gives. Otherwise, if unknown, leave `site.url` empty: the build works, without canonical links and sitemap.
- Ready to be found by search engines? `site.indexing` (default `true`); `false` for a draft or a private edition.
- Offline copy (`site.offline`): the book keeps working without a connection after a first visit; readers may see the previous version for a moment after an update. Default off.
- Favicon (`site.favicon`) and social preview image (`site.og_image`): optional files in `assets/`.

## Show it

Build and preview:

```bash
python3 build.py --serve
```

The preview runs on `http://127.0.0.1:8000/` (plus the `base_path`), on this computer only, until Ctrl+C. The command does not return while the preview runs: if your tools wait for commands to finish, start it as a background process, or build with `python3 build.py` and ask the person to run `python3 build.py --serve` in their own terminal. With a browser tool, open it yourself and show screenshots of the cover, 1 chapter and a phone-width view; otherwise ask the person to open it. Ask them to check: the cover, 1 chapter, the actions page, the search, the footer link "Licences, credits and source", and a phone-sized window. Adjust until they are happy.

## Step 7: keep it and publish it

Do what the permissions of step 0 allow, ask for the rest, and never more than once for the same thing.

1. **Commit** (if allowed): stage only the edition's files, after looking at `git status`: `git add edition.json` plus, for those that exist, `assets`, `custom.css` and `editions.json` (Git refuses the whole command when 1 path is missing), or `git add examples/<slug>` for a folder edition; then `git commit -m "<Community> edition: configuration"`. Never `git add -A` without reading `git status` first. If the person could not see a preview, say so before committing.
2. **Repository**. Recommend a fork of the base: it keeps the shared history, so updates come with a merge (see `docs/UPDATING.md`). From a clone of the base or a local repository, the steps are in `docs/HOSTING.md` ("From your computer to your fork"): fork on the forge, point `origin` at the fork and keep the base as `upstream`, push the branch that holds the edition as the default branch (`main`). Other choices: a new repository on a forge (GitHub, Codeberg, a self-hosted Forgejo or Gitea), or keep it local for now. Do not create accounts. If you are allowed to create the repository and `gh` is logged in, `gh repo fork --remote` or `gh repo create` does it; otherwise give the clicks. Once the repository exists, offer to fill `edition.repository` with its address and rebuild.
3. **Host**. Follow `docs/HOSTING.md` for the host they choose. The simplest: GitHub Pages with the workflow of this repository (it runs only when started by hand), Codeberg Pages, or uploading the clean export to any static host:

   ```bash
   python3 release.py --edition edition.json --out dist --dest publish
   ```

   `publish` must be a new or empty folder; the command refuses anything else and deletes nothing. Upload the contents of `publish/`, never `dist/`.

   For GitHub Pages, after a push: the person sets Settings > Pages > Source to "GitHub Actions" (or, if allowed, `gh api -X POST repos/<owner>/<repo>/pages -f build_type=workflow`), then the workflow is started from the Actions tab, or with `gh workflow run pages.yml -f edition=edition.json -f address=github-pages` if allowed. In a fork, GitHub disables workflows until someone opens the Actions tab and enables them: that click is the person's. The workflow runs from the default branch: the edition must be committed there (usually `main`), since GitHub Pages only deploys from it unless the person changes the environment rules.
4. **Check the published edition** with the list at the end of `docs/HOSTING.md`, and give the address.
5. Mention once that they can ask to be listed in the directory (issue form "List my edition", see `CONTRIBUTING.md`) and that improvements to the text are welcome upstream. Do not insist.

## When the configuration is not enough

Deeper changes are legitimate. Before touching code or text, say which file and why, then:

- **Text** (fix a fact, add a local tool, remove or add a chapter): edit `content/<lang>/*.md` and `book.json`. An action that is only reworded keeps its id: update its `text` in `actions.json` and keep the old wording in `previous_texts`. After really adding or removing actions, run `python3 build.py --update-actions`. If chapters or actions change on purpose, `tests/reference-ids.json` must be updated in the fork, since it guards the ids of the base. `docs/CUSTOMIZING.md`, section "Content".
- **Look beyond the variables**: `custom.css` next to `edition.json` (appended after the theme), before editing `theme/styles.css`.
- **Structure and behaviour**: `build.py` (page templates in the `Guide` class, strings in `content/<lang>/strings.json`) and `theme/app.js`. Keep the generated HTML valid, keep the licence headers, run `python3 -m unittest discover tests`.

Changes useful to everyone (a better tutorial, a translation, an accessibility fix) belong upstream too: offer to prepare a pull request on the base, separate from the edition's own commit, and open it only if allowed.

## What to report at the end

In a few lines: what was changed (files), the preview address, what was committed or published and where, what was not done (translation, hosting, listing), and the 3 commands they will need again: `python3 build.py --serve`, `python3 build.py --check`, `python3 release.py --edition edition.json --out dist --dest <new folder>`.
