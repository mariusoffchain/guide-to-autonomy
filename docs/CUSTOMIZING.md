# Beyond the configuration

`edition.json` covers the usual changes. Everything else is in files you own too. This page says where, and what to keep intact so that the build and the licences stay happy.

## Content

The text of a language lives in `content/<lang>/`. Files:

- `book.json`: the structure. `parts` (number, file, id, slug, title, optional `short_title` for the cover and menus), `introduction`, `glossary`, `chapters` (number, id, part, file, title) and `slugs` for the 3 generated pages (`start`, `actions`, `editions`). Ids are used in addresses and in the browser storage: choose them once.
- `NN-name.md`: 1 Markdown file per chapter, part opening, introduction and glossary.
- `strings.json`: every sentence of the interface.
- `actions.json`: the stable IDs of the checklist actions.
- `links.json`: official address of each tool named in the book, used to link tool names inside comparison tables.

### Anatomy of a chapter

```markdown
# Chapter 4: Your email and your aliases

## In brief
1 or 2 paragraphs. The first sentences become the page description.

## What goes wrong today
## The idea
Explanations. Any heading works; external links get a "Cited in this section" box.

## Choosing a tool
A Markdown table. Rows become search results; tool names in cells are linked from links.json.

## Step by step
1. **Short name of the step.** Explanation.
2. **Next step.** …

## Mistakes to avoid
- Bullet list.

## Go further
- [Title](https://…), author, date.

## Sources
- [Title](https://…), publisher, date.

## Your checklist
- [ ] Action, one line, ending with its effort in parentheses (5 min)
- [ ] Another action (1 hour)
- [ ] A project for a free day (weekend)
```

Rules the build enforces: exactly 1 `#` title, matching `book.json`; sections are `##`; `### ` subheadings are allowed and indexed; checklist actions are `- [ ] ` lines under `## Your checklist` only; the effort tag is the last parenthesis of the line and is free text. Section kinds are recognised by their heading ids: `in-brief`, `step-by-step`, `mistakes-to-avoid`, `go-further`, `sources`, `your-checklist` (the id is the heading text lowercased with hyphens). In another language, the kinds are recognised the same way, so give those sections the same English ids by writing the heading in your language followed by an explicit id: Python-Markdown's `toc` extension accepts `## Votre liste d'actions {#your-checklist}`.

Tables are compared tool by tool: the first column is the name. Steps are numbered lists under "Step by step". Glossary terms are paragraphs that start with a bold term.

### Add or remove a chapter

1. Create or delete the Markdown file (deleting is your call; the build never deletes).
2. Edit `chapters` in `book.json`: numbers must be unique and in reading order, `part` must exist.
3. Run `python3 build.py --update-actions` once: new actions get IDs, actions of a removed chapter are retired in `actions.json` (kept, marked, never reused).
4. Update `book.start_paths` in `edition.json` if a path named the chapter.
5. Update `tests/reference-ids.json` (it guards the 18 chapters and 90 actions of the base): regenerate its lists from your `book.json` and `actions.json`, or delete the file in your fork if you do not want that guard. The tests then pass again.

The other tests build `tests/base-edition.json`, a copy of the edition shipped with the base, so your own `edition.json` (dark colours, recordings, an address) never makes them fail. They still fail if you break the generator, the theme or the structure of the text, which is their purpose. The GitHub Pages workflow runs them before publishing.

### Reword an action

The build stops: "no entry in actions.json for …". Either update the `text` of the entry to the new wording (the reader's tick stays), or add the old wording to a `previous_texts` list of the entry. Use `--update-actions` only when the action is really new or gone.

### Add a part

Add it to `parts` in `book.json` with its opening essay, give its chapters `part: 4`, add a 4th colour to `colors.parts` in `edition.json`.

### Placeholders

`{{community}}`, `{{contact}}`, `{{community_url}}`, `{{edition_name}}`, `{{book_title}}` are filled from `edition.json`. Use them where the text must name the publisher. An unknown placeholder stops the build.

## Look

Order of preference:

1. `edition.json` → `colors`, `fonts`, `layout`.
2. `custom.css` next to `edition.json`: appended after the theme. Override any rule; the variables available are listed at the top of the generated `dist/assets/guide.css` (`--bg`, `--fg`, `--text`, `--muted`, `--line`, `--part-1`…, `--accent`, `--heading`, `--body`, `--measure`, `--caps`).
3. `theme/styles.css`: the full stylesheet, about 900 lines, commented by block (header, cover, page layout, chapter, prose, tables, steps, checklist, dialogs, footer, print). Keep the variables; a fork that hard-codes colours loses the configuration.

Class names worth knowing: `.part-1`, `.part-2`, `.part-3` on the elements that take a part colour; `.sec--brief`, `.sec--explain`, `.sec--compare`, `.sec--steps`, `.sec--pitfalls`, `.sec--further`, `.sec--sources`, `.sec--checklist` on the sections of a chapter; `.is-home`, `.is-chapter`, `.is-start`, `.is-actions`, `.is-directory` on the page layout.

## Structure, navigation, behaviour

- `build.py`: the `Guide` class builds every page from the content and the strings. `view_home`, `view_chapter`, `view_page`, `view_start`, `view_actions`, `view_directory` are the templates; `page_html` and `head_html` the shell. `page_list` decides which pages exist. Keep: 1 `h1` per page, ids unique, internal links to existing pages (the build checks all of this and stops otherwise).
- `theme/app.js`: enhancements only (ticks, progress, search, dialogs, table of contents, offline state). The pages are complete without it. Strings used at run time come from `strings.json` through `site-data.js`.
- `theme/sw.template.js`: the optional service worker.

If you change the markup of actions, tables or steps in `build.py`, check `theme/app.js` and `theme/styles.css` for the same class names.

## What to keep

- The licence headers of `build.py`, `theme/*.js`, `theme/styles.css`.
- The attribution in the footer and colophon (the `licence_line`, `licence_note` and `about_text` strings may be translated, not removed).
- `NOTICE`, `LICENSE`, `LICENSE-CONTENT`, `THIRD-PARTY.md`, updated if you add resources.

Everything else is yours to change. If the change would help other editions, see `CONTRIBUTING.md`.
