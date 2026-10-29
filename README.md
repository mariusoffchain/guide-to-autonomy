# A Guide to Autonomy

A learning book for everyone about personal and digital autonomy: keeping your conversations and accounts private, choosing the tools you depend on, and holding your own money, including Bitcoin. 18 chapters in 3 parts, 90 concrete actions, an introduction, 3 opening essays and a glossary. Each chapter explains a need, compares tools and their limits, walks through 1 setup step by step, lists the mistakes to avoid and links its sources.

This repository is the **shared base**: the kit a community uses to publish **its own edition** of the book, with its own name, colours, logo, fonts, text, language and hosting. There is no central portal and no central edition. Every edition is independent, and improvements come back to this base only when their authors want to send them.

The text is free under [CC BY-SA 4.0](LICENSE-CONTENT), the code under [AGPL-3.0-or-later](LICENSE). Commercial use is allowed by both. Details in [`NOTICE`](NOTICE) and [`THIRD-PARTY.md`](THIRD-PARTY.md). The original work was written for PROOF, an initiative of Cypher Baltics, for the first PROOF conference (Vilnius, 2026). Your edition chooses its own identity; every built edition keeps a short credit to the original work and says that it is an adapted edition.

## See it live

- **[The base edition](https://mariusoffchain.github.io/guide-to-autonomy/)**, built from this repository as it is, with no identity of its own.
- **[The PROOF edition](https://proofconference.com/book/en/)**, in English and [Lithuanian](https://proofconference.com/book/): the original, with the colours, fonts and logo of the conference it was written for. It shows what an edition with its own identity looks like.

## Make your edition with an AI assistant

Fork this repository (button **Fork**), open your fork with an assistant that can read and edit files and run commands (Claude Code, Codex, Cursor, Aider and similar), and paste:

> Read AGENTS.md and help me make our community's edition of A Guide to Autonomy.

The assistant first asks how much help you want and what it may do without asking again, then asks about your community, look, language and address 1 block at a time, edits the files, builds and shows you the result. It publishes only if you allow it, and never needs a password or a token from you: logins happen in your own browser. A chat-only assistant can follow the same instructions and tell you what to paste, more slowly.

## What you get

- Static HTML pages, 1 per chapter, with a cover, a "Where to start?" page, a page of all actions and an optional "Other editions" page. Scripts run in the reader's browser for search, ticks and the optional offline copy. No server code, no database, no account, no tracker, nothing loaded from another site.
- Reading progress and ticked actions saved in the reader's browser only, starting at 0.
- Full-text search, a table of contents on every page, previous/next links, keyboard and phone friendly.
- A page "Licences, credits and source" in every edition, with the licence texts, the font notices and a ZIP of the exact source the edition was built from.
- Optional: an offline copy, a list of other editions, recordings of talks on the cover (off by default, no video included).
- 1 configuration file for the usual changes ([every key](docs/CONFIGURATION.md)), the full source for everything else.

## Make your edition by hand

You need Python 3.9 or newer (preinstalled on macOS and most Linux; on Windows, install it from [python.org](https://www.python.org/downloads/) and tick "Add Python to PATH"), a text editor, and about 1 hour.

1. **Get a copy.** Fork, then clone your fork. A downloaded ZIP works too, but makes updates harder (see below).
2. **Install the dependency and preview:**

   ```bash
   python3 -m pip install -r requirements.txt
   ```

   ```bash
   python3 build.py --serve
   ```

   Open http://127.0.0.1:8000/. Ctrl+C stops the preview. On Windows, `py` may replace `python3`.
3. **Name it.** In `edition.json`, fill the `edition` block: `name`, `community`, `contact`, `changes` (what your edition changes, which the text licence asks you to state) and `modified`. Keep the JSON valid: double quotes, no comma after the last item. The build names the line when something is wrong.
4. **Look.** `colors` (light or dark, 1 accent per part, [ready palettes](docs/CONFIGURATION.md#colors)), `edition.logo`, `fonts`, `layout.uppercase_headings`. Small visual changes go into a `custom.css` next to `edition.json`.
5. **Words and behaviour.** `book` (cover text, start chapter, reading paths, search suggestions), `layout`, and `storage_key`: give it a value unique to your edition, such as `guide-autonomy.harbour.v1`.
6. **Address.** `site.url` (origin only, `https://guide.example.org`) and `site.base_path` (`/` or `/guide/`). With the GitHub Pages workflow, they can stay empty.
7. **Publish.** `python3 release.py --edition edition.json --out dist --dest publish`, then upload the contents of `publish/` to any static host, or use the provided GitHub Pages workflow, which runs only when you start it. [docs/HOSTING.md](docs/HOSTING.md).

Changing the text, adding a chapter or a language, editing the theme or the generator: [docs/CUSTOMIZING.md](docs/CUSTOMIZING.md) and [docs/TRANSLATING.md](docs/TRANSLATING.md).

## Fork or template

**Fork (recommended).** Your repository keeps the shared history of the base. When the base improves, you see what changed and merge it; your own changes stay in your files, and where both sides changed the same file Git shows the conflict for you to resolve by hand. A fork on GitHub is public; you can also clone the base and push it to any forge.

**Template ("Use this template", if the base has it enabled).** You get a new repository with a single fresh commit and no link to the base. It is cleaner if you plan to diverge a lot, but updates are harder: Git sees no common history, so you compare and copy files yourself, or merge with `--allow-unrelated-histories` and resolve every overlapping file. [docs/UPDATING.md](docs/UPDATING.md) explains both.

## Versions and updates

The base has numbered versions (`1.0.0`, `1.1.0`…) described in [CHANGELOG.md](CHANGELOG.md), with Git tags `v1.0.0`, `v1.1.0`…. The version is written in every generated page (`<meta name="generator">`). Nothing reaches your edition until you pull it, and no update can promise that your customisations survive every merge untouched: [docs/UPDATING.md](docs/UPDATING.md) shows how to see what changed, merge, resolve conflicts and check that the ids of the 90 actions, under which readers' ticks are saved, are still there.

## Repository map

| Path | What it is | Licence |
|---|---|---|
| `edition.json` | Settings of this edition. [Every key](docs/CONFIGURATION.md) | AGPL (structure), CC BY-SA (editorial values) |
| `content/en/` | The English text: 23 Markdown files (introduction, 3 part openings, 18 chapters, glossary), `book.json` (structure), `strings.json` (interface wording), `actions.json` (stable ids of the 90 actions), `links.json` (official sites of the tools) | CC BY-SA (text), AGPL (structure of the JSON files); see `NOTICE` |
| `build.py` | The generator. `python3 build.py --help` | AGPL |
| `release.py` | Source ZIP of an edition and clean export of a build for upload | AGPL |
| `theme/` | Stylesheet, browser scripts, optional service worker, 2 optional fonts | AGPL (code), OFL (fonts) |
| `tests/` | Tests of the generator, the export, the ids and the guards. `python3 -m unittest discover tests` | AGPL |
| `examples/` | 2 complete fictional editions to copy from | AGPL (config), CC0 (demo images) |
| `editions.json` | Hand-kept list for the optional "Other editions" page | AGPL (structure) |
| `docs/` | Configuration, customisation, hosting, translating, updating, releasing | CC BY-SA |
| `AGENTS.md`, `CLAUDE.md` | Instructions for AI assistants | CC BY-SA |
| `.github/` | Manual GitHub Pages workflow, checks for pull requests, issue forms | AGPL |
| `dist/`, `publish/` | Built site and clean export, created by the commands, not versioned | output |

## Commands

```bash
python3 build.py                     # build edition.json into dist/
python3 build.py --serve             # build, then preview on http://127.0.0.1:8000/ (--port 8001 if busy)
python3 build.py --check             # render and check everything, write nothing
python3 build.py --edition examples/riverside-meetup/edition.json --out dist-riverside --serve
python3 build.py --update-actions    # after really adding or removing a checklist action
python3 release.py --edition edition.json --out dist --dest publish   # build, then copy only this build's files into a new folder
python3 -m unittest discover tests   # tests
```

The build never deletes anything. It writes inside the output folder, plus an internal report next to it (`dist.build-report.json`) that is not published. It stops with a message when a link points nowhere, a title does not match, an action has no stable id, the JSON is broken, a page would load something from another site or a local path of your computer would be published.

## Contributing and the directory of editions

Corrections, new tools, translations, accessibility fixes and generator improvements are welcome as issues or pull requests. To appear on the "Other editions" page of the base and of the forks that show it, use the issue form "List my edition". Nothing is aggregated or listed automatically. [CONTRIBUTING.md](CONTRIBUTING.md).
