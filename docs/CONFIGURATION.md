# edition.json, key by key

The single configuration file of an edition. Every key is optional: a missing key takes the default shown here. An unknown key stops the build with its name, which catches typos. Values are JSON: strings in double quotes, `true`/`false` without quotes, lists in square brackets, no comma after the last item.

Two keys are free comments and are ignored by the build: `about` at the top level, and any key starting with `$`. Use them for notes to yourself.

```bash
python3 build.py --check      # tells you where the JSON or a value is wrong
```

## edition

| Key | Default | Meaning |
|---|---|---|
| `name` | `"Community edition"` | Name of the edition. Header, page titles, colophon, footer. |
| `label` | `""` | Optional second line on the cover: a year, "First edition", a city. |
| `community` | `"your community"` | Who publishes the edition. Cover ("An edition published by …"), colophon, footer, and the `{{community}}` placeholder in the text. |
| `community_url` | `""` | Link put on the community name. |
| `contact` | `""` | Email or web address for corrections. Shown in the colophon and footer, and used by the `{{contact}}` placeholder. Empty hides the sentence. |
| `repository` | `""` | Public address of the source repository of this edition, if any. Shown in the colophon, the footer and the page "Licences, credits and source". Optional: every build also ships a ZIP of the exact source of the edition (`source/`), which is what the legal page offers first. A repository alone is not a guarantee that the licences' conditions are met. |
| `changes` | `""` | 1 or 2 sentences describing what this edition changed from the original work (for example "Edition name, colours and reading paths; chapter 31 adapted to Lithuanian banks."). Shown on the page "Licences, credits and source". Empty shows a sentence pointing to the source archive. Under CC BY-SA, an adaptation must indicate that it was modified. |
| `modified` | `""` | Date of the last change, as you want it shown (`"2026-10-22"`). Shown on the same page. Empty says that no date is stated. |
| `wordmark` | `""` | Short word or 2 shown large on the cover when there is no logo. Empty uses `community`; set it when the community name is long. |
| `logo.file` | `""` | Path of an SVG or PNG, relative to the folder of `edition.json` (for example `assets/logo.svg`). Shown on the cover and in the header instead of the wordmark and the text title. An SVG must contain explicit colours. |
| `logo.cover_file` | `""` | Optional variant of the logo for the cover panel, whose background is the `foreground` colour (the panel is inverted). Use it when the main logo only works on the page background. |
| `logo.alt` | `""` | Text alternative of the logo. Defaults to `community`. |

## book

| Key | Default | Meaning |
|---|---|---|
| `title` | `"A Guide to Autonomy"` | Title of the book. Page titles, header, footer. |
| `title_lines` | `[]` | The title split in lines for the cover, for example `["A Guide", "to", "Autonomy"]`. Empty uses `title` on 1 line. |
| `outlined_line` | `-1` | Index (from 0) of the line drawn in outline on the cover. `-1` for none. |
| `kicker` | `"A learning book"` | Small line above the cover title. |
| `intro` | `[]` | Paragraphs of the cover, 1 string each. 2 is a good number. |
| `start_chapter` | `""` | Id of the chapter opened by the big "Start reading" button. Ids are in `content/<lang>/book.json`. Empty opens the introduction, or the first chapter if there is no introduction. An explicit chapter id overrides this. |
| `start_paths` | `[]` | Reading paths of the "Where to start?" page. Each path: `{"id": "path-x", "title": "…", "text": "…", "chapters": ["id", …], "deeper_title": "…", "deeper": ["id", …]}`. `deeper` is optional. |
| `search_suggestions` | `[]` | Words proposed when the search box is empty. |

## language

| Key | Default | Meaning |
|---|---|---|
| `code` | `"en"` | BCP 47 code written in `<html lang>`. |
| `name` | `"English"` | Name of the language in its own language, shown in the language panel and the colophon. |
| `direction` | `"ltr"` | `"ltr"` or `"rtl"`, written in `<html dir>`. The layout follows the direction; right-to-left typography has not been tuned in detail, see `docs/TRANSLATING.md`. |
| `content_dir` | `"content/en"` | Folder, relative to the repository root, holding the Markdown files, `book.json`, `strings.json`, `actions.json` and `links.json` of this language. |
| `locale` | `"en_US"` | Open Graph locale. |

## other_editions

A list, empty by default. Each entry: `{"code": "lt", "name": "Lietuvių", "url": "https://…", "note": "optional sentence"}`. They appear under a language button in the header, as links in the footer, and as `hreflang` alternates on the cover when `site.url` is set. Use it for your own translations and for sister editions you trust.

## colors

| Key | Default | Meaning |
|---|---|---|
| `scheme` | `"light"` | `"light"` or `"dark"`. Sets the browser colour scheme (form controls, scrollbars) and the strength of shadows. Choose it to match `background`. |
| `background` | `"#fbfaf7"` in the shipped `edition.json` (`"#ffffff"` if the key is removed) | Page background, 6-digit hex. |
| `foreground` | `"#17171a"` in the shipped `edition.json` (`"#141414"` if the key is removed) | Text and lines, 6-digit hex. Every intermediate shade (muted text, hairlines, raised panels, hover states) is computed from these 2 colours at build time, so a light or a dark edition only needs these 2 values. The cover's right-hand panel inverts them. |
| `parts` | 3 entries | 1 object per part of the book, in order: `{"accent": "#hex", "text": "#hex"}`. `accent` colours bars, borders, numbers and the checked boxes; `text` colours small text on the page background, so pick a darker (light scheme) or lighter (dark scheme) variant when the accent is too pale. `text` defaults to `accent`. The list must have at least as many entries as `book.json` has parts. |

Ready-made palettes, each pair checked at 4.5:1 or better for the `text` colours on the background:

| Scheme | background | foreground | part 1 accent / text | part 2 accent / text | part 3 accent / text |
|---|---|---|---|---|---|
| Light, neutral (default) | `#fbfaf7` | `#17171a` | `#0f766e` / `#0b5e58` | `#4f46e5` / `#4338ca` | `#b45309` / `#92400e` |
| Light, warm | `#faf6ef` | `#2b1d14` | `#2e8b74` / `#1f6b58` | `#1f4e8c` / `#173d6e` | `#b7472a` / `#94381f` |
| Light, cool | `#f6f8fb` | `#101828` | `#0369a1` / `#075985` | `#6d28d9` / `#5b21b6` | `#be123c` / `#9f1239` |
| Dark, navy | `#0b1220` | `#f4f1e8` | `#7dd3fc` / `#a5e3ff` | `#f0b429` / `#f6c75a` | `#fb7185` / `#fda4b4` |
| Dark, neutral | `#111111` | `#f2f2f2` | `#34d399` / `#6ee7b7` | `#a78bfa` / `#c4b5fd` | `#fbbf24` / `#fcd34d` |
| Dark, forest | `#0f1a14` | `#eef3ea` | `#86efac` / `#bbf7d0` | `#93c5fd` / `#bfdbfe` | `#fdba74` / `#fed7aa` |

The accent and `text` colours are used on the page background only; the inverted cover panel uses `background` and `foreground` alone. A pair taken from another row of the table was checked on that row's background, not on yours: the build checks it for you. It prints a note when the foreground or a part's `text` colour has less than 4.5:1 contrast with the background, with the ratio, and builds anyway. Words such as "forest green" or "sky blue" are best matched by a row of the same scheme, then adjusted until the build prints no note.

## fonts

Two roles, `heading` and `body`, with the same keys:

| Key | Default | Meaning |
|---|---|---|
| `family` | `""` | Name of the font family as it must appear in CSS, for example `"JetBrains Mono"`. Empty means system fonts only. |
| `fallback` | system stack | CSS fallback list used after `family`. Keep a generic family at the end (`sans-serif`, `serif`, `monospace`). |
| `weight` (heading only) | `"700"` | Weight of the headings. System fonts look right at `700`; display fonts that only ship 1 weight usually want `"400"`. |
| `files` | `[]` | The `.woff2` files that make up the family, 1 object each: `{"file": "assets/fonts/x.woff2", "weight": "400", "style": "normal", "unicode_range": "optional", "preload": true, "license": "optional"}`. `file` is relative to the folder of `edition.json`, or to the repository root (so `theme/fonts/jetbrainsmono-latin.woff2` works from any edition). `weight` may be a range such as `"300 500"` for a variable font. `preload: true` adds a `<link rel=preload>`: use it for the 1 or 2 files needed above the fold. `license` names the font's licence file, looked up like `file`; without it the build uses the official notice for the fonts of `theme/fonts/`, otherwise the file next to the font whose name starts with `OFL`, `LICENSE`, `LICENCE`, `COPYING` or `NOTICE` (if there are several, the ones containing the start of the font's file name; if that is ambiguous the build stops and asks for `license`). |

Only `.woff2` files are supported: it is the format every current browser reads and the smallest. Convert other formats with a tool such as `fonttools` before adding them. Check the licence of each font allows web embedding and keep its full licence file next to the files: the build copies it into the site (`legal/fonts/`) and into the source archive, and stops when a configured font has no licence file. Under the SIL OFL, a modified font may not use a Reserved Font Name, where the font declares one, without permission.

## layout

| Key | Default | Meaning |
|---|---|---|
| `reading_width` | `"42rem"` | Maximum width of the text column. |
| `page_toc` | `true` | "On this page" table of contents: on the side on wide screens, behind a button on narrow ones. |
| `uppercase_headings` | `true` | Headings, kickers and buttons in capitals. `false` for normal case. |
| `cover_part_bars` | `true` | Legacy setting accepted for compatibility. Both values now use the same small colour marker for each part; it does not indicate progress. |
| `show_progress` | `true` | Tick boxes on actions, "I have read this chapter", progress counts, the "All actions" page and the "Your progress" section. `false` turns the book into a plain book: actions are listed without boxes and nothing is stored in the browser. |
| `show_search` | `true` | Search button and dialog. |

## site

| Key | Default | Meaning |
|---|---|---|
| `url` | `""` | Public origin of the edition, `https://host` without a path (the build refuses a path here: put it in `base_path`). Enables the canonical link, Open Graph tags, `sitemap.xml`, `robots.txt` and `hreflang` links. Leave empty while the address is unknown; the pages work without it. |
| `base_path` | `"/"` | Folder under which the pages are served, with slashes: `"/"` at the root, `"/guide/"` in a sub-folder. Every internal link is absolute from this path, so the built folder must be served exactly there. `python3 build.py --serve` mirrors the path for the local preview. |
| `offline` | `false` | Generates `sw.js`, a service worker that saves the whole edition in the reader's browser after the first visit, so that every page opens without a connection. Caveat: after you publish an update, a reader may see the previous version until the new copy has been saved in the background; the colophon shows the state of the offline copy. Needs HTTPS (or `127.0.0.1`). |
| `sitemap` | `true` | Write `sitemap.xml` and `robots.txt` when `url` is set. |
| `indexing` | `true` | `false` for a draft or a private edition: every page says `noindex`, `robots.txt` asks crawlers to stay away and no sitemap is written. Set it back to `true` when the edition is ready to be found. |
| `og_image` | `""` | Image used by social networks when a page is shared (1200 × 630 px recommended), relative to the edition folder. |
| `favicon` | `""` | Icon of the tab, SVG or PNG, relative to the edition folder. |

### Address for 1 build only

`python3 build.py --site-url https://octocat.github.io --base-path /guide-to-autonomy/` (also accepted by `release.py`) uses that address instead of `site.url` and `site.base_path`, without changing `edition.json`. The GitHub Pages workflow uses it to write the address GitHub gives the site. The source archive of that build records the flags in its `SOURCE-README.txt`, so the same pages can be rebuilt.

## storage_key

Default `"guide-autonomy.v1"`. Prefix of the keys under which the reader's ticks and read marks are stored in their browser. Browsers keep this storage per origin (scheme, host and port): 2 editions on different domains never share ticks, but 2 editions under the same domain do when they use the same prefix. Set it to something unique to your edition (`"guide-autonomy.harbour.v1"`), ideally before the first publication. Changing it later starts every reader from an empty state; the old keys are left in place, not deleted.

## directory

| Key | Default | Meaning |
|---|---|---|
| `enabled` | `false` | Adds an "Other editions" page, linked from the contents drawer, listing the entries of `file`. |
| `file` | `"editions.json"` | Looked up next to `edition.json`, then at the repository root. Hand-maintained. |

Format of the directory file: an object with an `editions` array; every other key (`about`, `entry_format`) is a comment and is ignored. Each entry:

```json
{"name": "Harbour edition", "community": "Harbour Bitcoin Meetup", "languages": ["en"],
 "site": "https://guide.harbour.example.org/", "repository": "https://codeberg.org/harbour/guide-to-autonomy",
 "description": "1 or 2 sentences, optional",
 "consent": {"public_listing": true, "date": "2026-10-23", "reference": "address of the request"}}
```

`name`, `site` and `consent` are required. The build refuses an entry without consent, a `site` or `repository` that is not `https://` on a public domain name (no IP address, `localhost`, `.local` or similar), and a site listed twice. An empty array is valid: the page then says that no other edition is listed yet. Requests to be listed arrive through the issue form `.github/ISSUE_TEMPLATE/edition.yml` or a pull request; nothing is added automatically.

## recordings

Optional section of the cover listing recordings of talks, for example the talks of the event where the edition is handed out. Off and empty by default: the base ships no recording.

| Key | Default | Meaning |
|---|---|---|
| `enabled` | `false` | Shows the section on the cover when `items` is not empty, with an entry in the cover's table of contents and in the search. |
| `kicker`, `title`, `intro` | `""` | Small line, heading and 1 paragraph. Empty `kicker` and `title` take `recordings_kicker` and `recordings_title` from `strings.json` ("Talks", "Talk recordings"). |
| `media_origins` | `[]` | Extra `https://` origins a video file may be redirected to by its host (for example a CDN). The origins of the `video` addresses are added automatically. |
| `items` | `[]` | The recordings, in order. |

Each item:

| Key | Meaning |
|---|---|
| `title` | Required. Title of the talk. |
| `speaker`, `note` | Shown under the title, for example the name and "in Lithuanian". |
| `video` | `https://` address of a video file (`.mp4`, `.webm`) or a YouTube address (`youtube.com/watch?v=…`, `youtu.be/…`). Without it, the card has no player. |
| `video_type` | Media type of the file, for example `video/mp4; codecs="hvc1"`, so that the browser can skip a format it cannot play. |
| `video_sd`, `video_sd_type` | A second, lighter file offered after the first one. |
| `poster` | Image file next to `edition.json` (for example `assets/talk-1.jpg`), 16:9. Never an outside address: the cover loads nothing from another site before a click. |
| `chapters` | Chapter or page ids the talk relates to; shown as "In the book:" links. The first chapter also gives the card its part colour, unless `part` (1 to 3) is set. |
| `links` | `[{"label": "PeerTube", "href": "https://…"}]`, other places to watch it. |
| `kicker` | Small line above the title; marks the card as a closing talk. |
| `badge` | Short label shown instead of a player when there is no `video`, for example "No recording". |

How it behaves. Without JavaScript, "Watch the recording" and the poster are plain links to the file. With JavaScript, a click creates the player in place: a `<video>` for a file, or a `youtube-nocookie.com` frame for YouTube. Before that click, the cover requests nothing from another site; after it, that site receives the reader's request like any visit. Only the cover's Content-Security-Policy is widened, and only to the addresses of its own recordings (`media-src` for files, `frame-src https://www.youtube-nocookie.com` for YouTube); every other page keeps `frame-src 'none'`. The pages send no referrer, except the clicked YouTube frame, which sends the site's origin as YouTube requires. Recordings need a connection: their player and posters are not part of the offline copy. The recordings and posters keep the rights of their authors and are not covered by the book's licences; list only what you may show.

## licence

The 2 licences of the project, used in the footer and colophon. Defaults are CC BY-SA 4.0 for the text and AGPL-3.0-or-later for the code. Do not change them: they are the terms under which you received the book. The key exists so that the labels and links can be translated.

## What every edition carries, whatever the configuration

The build adds these to every edition; no key turns them off:

- A credit to the original work on the page "Licences, credits and source": *A Guide to Autonomy*, originally written for PROOF, an initiative of Cypher Baltics, with a link to https://proofconference.com/book/en/, and the name of the community that adapted it. Every footer and the colophon of the cover link to that page; the credit itself is not repeated on every page.
- A page "Licences, credits and source" (`legal/`), linked from every footer and from the contents: original work, this edition and its changes (`edition.changes`, `edition.modified`), licences, font notices, source, names and logos.
- The full texts `legal/LICENSE.txt`, `legal/LICENSE-CONTENT.txt`, `legal/NOTICE.txt`, `legal/THIRD-PARTY.txt`, and `legal/fonts/` with the full notice of each font the edition serves.
- `source/guide-to-autonomy-source.zip`: the source of the edition, made by `release.py` from an explicit list (generator, packager, tests, theme, text of the configured language, docs, licences, the edition file with its `assets/`, `custom.css` and `editions.json`, and every file the configuration references). The same inputs give the same bytes. It never contains Git data, CI workflows, internal reports, built output or other editions. A referenced file outside the repository or behind a symbolic link stops the build.
- `release-manifest.json`: every file of this build with its relative path, size and SHA-256. `release.py` exports exactly these.

The page sentences have English defaults in `build.py`; a translation can override them in `strings.json` with the keys `original_credit`, `legal_link`, `legal_title` and `legal_*` used in `build.py`.

## Files next to edition.json

- `assets/`: logo, favicon, social image, fonts and their licence files. The build copies what the configuration references into `dist/assets/` with a versioned address, and puts the whole `assets/` folder into the source archive.
- `custom.css`: optional. Appended after the theme in the generated stylesheet. The right place for small visual changes before editing `theme/styles.css`.
- `editions.json`: optional local directory, when `directory.file` points at it.

## Placeholders in the text

In the Markdown files, `{{community}}`, `{{contact}}`, `{{community_url}}`, `{{edition_name}}` and `{{book_title}}` are replaced at build time from this configuration. The build stops if a placeholder it does not know remains in a page.

### Cover and personal progress

“In this guide” gives plain counts of available chapters and checklist actions. Only “Your progress” uses completion counters and bars. The introduction is the default reading entry; “Open a checklist” opens the first chapter checklist, or the explicitly configured start chapter. Existing action IDs and browser storage keys are preserved.
