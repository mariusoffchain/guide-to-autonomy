# Changelog

What changed in each version of the base, for the people who maintain an edition. Versions follow `MAJOR.MINOR.PATCH`: a patch fixes, a minor version adds without breaking an edition, a major version may need changes in editions (always listed under "Needs your attention"). Each version has a Git tag `v<version>`. How to take an update: [docs/UPDATING.md](docs/UPDATING.md).

## 1.0.1, 2026-10-28

### Building and publishing

- GitHub workflows use the current major versions of their actions, which run on Node.js 24: `actions/checkout@v7`, `actions/setup-python@v7`, `actions/configure-pages@v6`, `actions/upload-pages-artifact@v5`, `actions/deploy-pages@v5`. GitHub had warned that the previous versions targeted Node.js 20, which is deprecated.
- The checks workflow runs on `ubuntu-24.04` instead of `ubuntu-latest`: Python 3.9, the oldest version the kit supports, is not built for Ubuntu 26.04, which `ubuntu-latest` is moving to.

### Needs your attention

- If you edited `.github/workflows/pages.yml` or `checks.yml` in your edition, merge these lines by hand. Nothing else changes: same text, same 90 action ids, same configuration keys.
- `upload-pages-artifact` leaves out files whose name starts with a dot, as it did since its version 4. The export of `release.py` contains none.

## 1.0.0, 2026-10-23

First public version of the base.

### Book

- English text of *A Guide to Autonomy*: introduction, 3 part openings, 18 chapters, glossary, 90 checklist actions with stable ids. It includes the corrections reviewed on 2026-10-22 (backups and recovery, exposed seeds, multisig, 2FA fallback, Nostr relays and signers, cloud deletion, GDPR portability, containers, AI retention, Bitcoin privacy, node wallets). References to the original conference are neutral (`{{community}}` and generic examples).

### Editions

- 1 configuration file, `edition.json`: identity, logo, colours, fonts, cover text, reading paths, language, other editions, layout, address, offline copy, indexing, storage key, directory, recordings.
- Every edition carries the credit to the original work, a page "Licences, credits and source", the licence and notice texts and a ZIP of its exact source.
- Optional "Other editions" page, fed by a hand-kept `editions.json`; entries need the consent of the listed edition, a public https address, and are unique.
- Optional recordings of talks on the cover: off by default, no video in the base, the player is created only after a click and only the cover's Content-Security-Policy is widened to the addresses listed.
- `site.indexing: false` for drafts: `noindex` on every page and a `robots.txt` that disallows crawling.
- The build prints a note when a text colour has less than 4.5:1 contrast with the background, names the edition file in its errors and lists the valid chapter ids when one is unknown.
- Comparison tables give row headers to their first column (from `row_header_columns` in `strings.json`).

### Building and publishing

- `build.py` checks links, ids, titles, placeholders, outside resources and local paths before writing anything, and never deletes a file.
- `--site-url` and `--base-path` set the address for 1 build; the source archive records them.
- `release.py` exports exactly the files of a build into a new folder. The source ZIP is stored uncompressed, so its bytes depend only on its inputs.
- GitHub Pages workflow, started by hand only, which writes the address GitHub gives the site. Checks workflow for pull requests. Issue forms for corrections and for the directory.
- The offline copy keeps, across an update, the files a reader's browser had added while browsing.

### Needs your attention

Nothing: first version.
