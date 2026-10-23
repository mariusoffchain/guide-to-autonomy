# Translating the book

A language is a folder under `content/`. The English folder is the reference. A translation is an adaptation under CC BY-SA 4.0, with credit to the base, like any other edition.

## Set up the folder

```bash
cp -r content/en content/fr
```

Then in `edition.json`:

```json
"language": {"code": "fr", "name": "Français", "direction": "ltr", "content_dir": "content/fr", "locale": "fr_FR"}
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

Translate meaning, not words, and keep the tone: short sentences, concrete, several options, sources named. Check every factual statement still holds in your country (laws, banks, prices, availability of tools) and replace examples that do not travel: the base text names Lithuania and the euro area in places, because that is where it was written. Machine translation is a draft, not a text: have a native reader go through every chapter, and keep the dates of verification.

## Right-to-left scripts

Set `"direction": "rtl"`. The page direction, text alignment and the previous/next links follow. The decorative details (the outline title, the big chapter number, the side table of contents) have not been tuned for RTL scripts yet; `custom.css` is the place to adjust them, and a pull request to `theme/styles.css` is welcome.

## Fonts and scripts

System fonts cover most scripts. If your script needs a specific font (or you want one), see `fonts` in `CONFIGURATION.md`; prefer fonts under the SIL OFL and subset them to your script to keep the files small.

## Several languages on one site

Build each language as its own edition (its own `edition.json` under `examples/<lang>/` or in separate branches), publish them under `/en/`, `/fr/`, and list each in the other's `other_editions`. The language button of the header and the `hreflang` links come from that list.

## Translations that exist outside this repository

- Lithuanian: the translation of the first edition. It still carries references to the original conference and must be neutralised like the English before it can join the base.
- French: a complete draft made in October 2026 from the English as it stood before the corrections of 2026-10-22. Before it can join the base, it needs the section ids above, a `strings.json`, the neutralisation of about 13 passages, and the retranslation of about 100 corrected passages in 21 files, including 6 reworded actions and the safety steps of the seed, hardware wallet, email and password chapters. Its 90 action ids already match the base.

A translation joins the base only once it follows the current English, or says precisely which version it follows and which passages are pending.

## Offering the translation upstream

Open a pull request adding `content/<lang>/` to the base. The base keeps the English text as the reference and merges translations as they come; it does not promise to keep every translation up to date when the English text changes, so each translation names, in its `book.json`, the version or date of the English text it follows.
