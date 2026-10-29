# Translating the book

A language is a folder under `content/`. The English folder is the reference. A translation is an adaptation under CC BY-SA 4.0, with credit to the base, like any other edition.

The base ships 2 languages: English (`content/en/`, built by `edition.json`) and French (`content/fr/`, built by `languages/fr/edition.json`). The French folder is a complete model of everything a translation contains: `strings.json`, `book.json`, `actions.json` with the same 90 ids, and the section ids described below.

## Set up the folder

For a new language, German for example:

```bash
cp -r content/en content/de
```

Then in the edition file of that language (`edition.json` if it is your only language, `languages/de/edition.json` next to the English, see "Several languages on one site"):

```json
"language": {"code": "de", "name": "Deutsch", "direction": "ltr", "content_dir": "content/de", "locale": "de_DE"}
```

The build works immediately, with the English text in the new folder, so you can translate file by file and check as you go.

## What to translate

1. **`strings.json`**: every sentence of the interface, about 170 short entries. Keep the `{placeholders}` and the `_one`/`_many` pairs. The `anatomy` list holds the 4 items of "How each chapter works". Translate the licence labels only if your language has an official name for them; the links stay.
2. **The 23 Markdown files.** Keep the structure: 1 `#` title, `##` sections, `- [ ]` actions with the effort in parentheses at the end of the line, the links.
3. **`book.json`**: the `title` of each part, chapter, the introduction and the glossary must match the `#` lines of the files exactly. Translate `slug` values if you want translated addresses (`/mots-de-passe/`), and the 3 `slugs` of the generated pages (`start`, `actions`, `editions`). Chapter and part **ids** are addresses too but also storage keys: translating them is possible (`"id": "mots-de-passe"`) as long as the same ids are used in `actions.json` and `edition.json`.
4. **`actions.json`**: the `text` of each action must match the translated action lines. Run `python3 build.py`: it lists every action it cannot match. Update the texts (keep the ids), or run `--update-actions` once for the whole file if you accept new ids in the new language (readers of the English edition are not affected: each language edition has its own storage).
5. **`links.json`**: usually unchanged; add tools you introduce.
6. **Section ids.** The build recognises the kind of a section by its id: `in-brief`, `step-by-step`, `mistakes-to-avoid`, `go-further`, `sources`, `your-checklist`. In another language, write the heading in your language and add the English id in braces, which Python-Markdown understands:

   ```markdown
   ## Votre liste d'actions {#your-checklist}
   ```

   Do the same for the other 5. Other headings get their id from their text and need nothing.

7. **The chapter title prefix** ("Chapter 4: ") and the part prefix come from `strings.json` (`chapter_prefix`, `part_prefix`), so write your titles as `# Chapitre 4 : Vos e-mails et vos alias` and set `"chapter_prefix": "Chapitre {n} : "`.

## Working with translators and AI

Translate meaning, not words, and keep the tone: short sentences, concrete, several options, sources named. Check every factual statement still holds in your country (laws, banks, prices, availability of tools) and replace examples that do not travel: part 3 uses examples from the European Union and the euro area (deposit guarantee, cash limits, inflation figures, exchanges, payment rules); adapt them as described in `docs/CUSTOMIZING.md`, section "Outside the European Union". Machine translation is a draft, not a text: have a native reader go through every chapter, and keep the dates of verification.

## Right-to-left scripts

Set `"direction": "rtl"`. The page direction, text alignment and the previous/next links follow. The decorative details (the outline title, the big chapter number, the side table of contents) have not been tuned for RTL scripts yet; `custom.css` is the place to adjust them, and a pull request to `theme/styles.css` is welcome.

## Fonts and scripts

System fonts cover most scripts. If your script needs a specific font (or you want one), see `fonts` in `CONFIGURATION.md`; prefer fonts under the SIL OFL and subset them to your script to keep the files small.

## Several languages on one site

Each language is its own edition, with its own edition file, its own `storage_key` and its own address. The convention of the base:

- the main edition (`edition.json`) is served at the root of the site;
- each other language has an edition file `languages/<code>/edition.json`, served under `<root>/<code>/`. Its `language` block points to `content/<code>/`, its `site.base_path` is `"/<code>/"` (the address used by `python3 build.py --edition languages/<code>/edition.json --serve` and by the workflow's `address: edition.json`), and its `storage_key` differs from the main edition's, because both live on the same origin;
- each edition lists the others in `other_editions`, with their full public address. The language button of the header, the footer links and the `hreflang` links come from that list. The addresses are absolute, so they do not follow a fork: if you publish your own copy, point them at your own site or empty the list.

The GitHub Pages workflow builds the main edition, then every `languages/<code>/edition.json` into the same upload, in the folder `<code>/` (input `languages`, on by default; see `docs/HOSTING.md`). The checks workflow runs `build.py --check` on each of them, and `tests/test_kit.py` checks that they keep the 90 action ids of the base.

To add a language: copy `languages/fr/` to `languages/<code>/`, change `language`, `site.base_path`, `storage_key`, the texts of `edition` and `book`, and the `other_editions` of every edition. Elsewhere than GitHub Pages, build each edition with `release.py` and upload each export into its folder (`docs/HOSTING.md`, "Several editions, one domain").

## Translations in this repository

- French (`content/fr/`, edition `languages/fr/edition.json`): follows the English text of 2026-10-29, that is version 1.1.0 with the corrections of the same day, with the same 90 action ids. Made from a complete draft of October 2026, then brought up to date passage by passage with assistance from an AI; a full reading by a native French reader is still welcome, especially for the safety steps of the seed, hardware wallet, email and password chapters. When the English changes, the French is updated in the same pull request or its `book.json` (`follows`) says which version it follows.

## Translations that exist outside this repository

- Lithuanian: the translation of the first edition. It still carries references to the original conference and must be neutralised like the English before it can join the base.

A translation joins the base only once it follows the current English, or says precisely which version it follows and which passages are pending.

## Offering the translation upstream

Open a pull request adding `content/<lang>/` to the base. The base keeps the English text as the reference and merges translations as they come; it does not promise to keep every translation up to date when the English text changes, so each translation names, in its `book.json`, the version or date of the English text it follows.
