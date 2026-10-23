# Third-party resources

Review update, 2026-10-22: the Python-Markdown 3.9 BSD-3-Clause licence is verified from its official PyPI source archive. The full official font notices are in `theme/fonts/OFL-*.txt`. Every built edition ships `LICENSE`, `LICENSE-CONTENT`, `NOTICE`, this file, the full notices of the fonts it serves, a page "Licences, credits and source" and a ZIP of its source (`build.py`, `release.py`). The detailed review notes stayed with the maintainers and are not part of this repository. This update does not change either project licence.

Everything in this repository that was not written for it, with its real licence, where it comes from, how it is used, and what remains to be verified. The 2 project licences (CC BY-SA 4.0 for the text, AGPL-3.0-or-later for the code, see `NOTICE`) do not relicense any of this.

Status column: **verified** means the licence text or notice was read at the source named; **to verify** means the licence is believed but was not checked at the source during the preparation of this repository (2026-10-22). Nothing below is guessed: where a licence could not be confirmed, it says so.

## Bundled in this repository

| Resource | Files | Licence | Source | Use | Status |
|---|---|---|---|---|---|
| JetBrains Mono (font) | `theme/fonts/jetbrainsmono-latin.woff2`, `theme/fonts/jetbrainsmono-latin-ext.woff2` | SIL Open Font License 1.1 (OFL-1.1). Copyright 2020 The JetBrains Mono Project Authors | https://github.com/JetBrains/JetBrainsMono (the WOFF2 subsets come from the Google Fonts build of the family) | Optional. Not used by the default edition. Used by `examples/riverside-meetup/` as heading font | Verified against the official `OFL.txt` of google/fonts (`ofl/jetbrainsmono/`), copied byte for byte to `theme/fonts/OFL-JetBrainsMono.txt`. The WOFF2 metadata carries the copyright and an OFL address but not the full licence text. The subsetting was done upstream (Google Fonts), not here |
| Righteous (font) | `theme/fonts/righteous-latin.woff2`, `theme/fonts/righteous-latin-ext.woff2` | SIL Open Font License 1.1 (OFL-1.1). Copyright (c) 2011 by Brian J. Bonislawsky DBA Astigmatic (AOETI), Reserved Font Name "Righteous" | https://github.com/google/fonts/tree/main/ofl/righteous | Optional. Not used by any edition in this repository; kept because the first (PROOF) edition used it | Verified against the official `OFL.txt` of google/fonts (`ofl/righteous/`), copied byte for byte to `theme/fonts/OFL-Righteous.txt`. Reserved Font Name: a Modified Version may not use the name "Righteous" without the holder's written permission |
| Checkbox tick, header icons (SVG) | inline in `build.py` and `theme/styles.css` | Drawn for this project, AGPL with the code | this repository | Interface | Not third-party |
| Demo logo and demo poster | `examples/riverside-meetup/assets/logo.svg`, `examples/riverside-meetup/assets/talk-poster.svg` | Drawn for the demo, CC0 (do what you want) | this repository | Example only. Fictional meetup | Not third-party |

OFL note: the OFL allows the fonts to be bundled with, and sold with, software and documents under any licence, as long as the fonts themselves stay under the OFL and each copy contains the copyright notice and the licence (`theme/fonts/README.md`). The build copies the full notice of every font an edition serves into the site (`legal/fonts/`) and the source archive, and stops when a configured font has no notice. The fonts are served as separate files, not merged into the program. If an edition converts, subsets or otherwise modifies a font, the OFL applies to the result; a Reserved Font Name, where the font has one (Righteous does), may not be used for the Modified Version without the holder's written permission. Fonts without a Reserved Font Name do not need to be renamed for that reason.

## Needed to build, not bundled

| Resource | Licence | Source | Use | Status |
|---|---|---|---|---|
| Python 3 (3.9 or later) | Python Software Foundation License (PSF-2.0) | https://www.python.org/ | Runs `build.py` | Verified (well-known licence); not redistributed |
| Python-Markdown 3.9 | BSD 3-Clause | https://github.com/Python-Markdown/markdown (file `LICENSE.md`) | Markdown to HTML in `build.py`, extensions `tables`, `toc`, `fenced_code`, `sane_lists`, `attr_list` | Verified on 2026-10-22 from `LICENSE.md` inside the official PyPI source distribution of Markdown 3.9, whose archive digest was checked against the PyPI metadata. The library is neither in this repository nor in the source archive nor in a built edition; its notice must be kept by whoever redistributes it |

No third-party JavaScript library, CSS framework, icon set, analytics script or web font service is used. The generated pages load nothing from another domain (the build checks it), except, when an edition enables recordings, the player a reader starts by clicking; their own scripts (`guide.js`, the generated data files and the optional `sw.js`) are part of this project.

## Content: sources, tools, brands

| Resource | How it appears | Licence or right | Status |
|---|---|---|---|
| Cited sources (articles, reports, documentation, studies) | Links in the text, in "Sources" lists and in "Cited in this section" boxes. Short factual statements and figures drawn from them, with attribution | Not redistributed. Quotation of facts with attribution; no article is reproduced | The chapters' sources were checked by the authors in September 2026, and an editorial check on 2026-10-22 has its own reports and limits. Neither is a guarantee that every link is still available or that every inline quotation is cleared. A fork that adds long quotations must check the right to quote in its jurisdiction |
| Names of tools, companies and products (Signal, Bitwarden, Proton, GrapheneOS, Bitcoin Core, Phoenix, Bringin...) | Named and compared in tables and tutorials; `content/en/links.json` holds their official addresses | Trademarks belong to their owners. Nominative use to describe and compare the products | No logo of any tool is used. One row of the comparison tables (Bringin) was added when the company sponsored the first conference; the sponsor notices were removed from this base, the row stays as 1 option among others. Each edition may keep, edit or remove it |
| Names "PROOF", "Cypher Baltics" | In `NOTICE`, this file, and the credit to the original work that every built edition carries (footer, colophon, page "Licences, credits and source") | Names of organisations, not licensed. Used only to credit the origin of the book | Not used as branding of any edition |
| Talk recordings (optional, `recordings` in `edition.json`) | Off by default. When an edition lists recordings, the cover shows cards with links; a video file or a YouTube frame (youtube-nocookie.com) is loaded only after the reader clicks | The recordings and their posters keep the rights of their authors and hosts. Neither project licence covers them. The base ships no recording; the poster in `examples/riverside-meetup/` is drawn for the demo (CC0) | An edition that lists recordings must have the right to show their posters and link or embed them, and states the outside sites in its own privacy information if it has any |
| Example addresses | `example.org` domains in `examples/riverside-meetup/` | Reserved by RFC 2606 for documentation | Nothing is fetched from them |

## Compatibility notes

- **Text under CC BY-SA 4.0 and code under AGPL-3.0-or-later side by side.** In the sources, the 2 layers mostly sit in different files, but not always: `build.py` holds default English interface strings, and the JSON files mix editorial values (CC BY-SA) with a data structure (AGPL), as `NOTICE` explains. The generated HTML combines both layers on every page; that does not relicense the book text. Creative Commons lists BY-SA 4.0 as one-way compatible with GPLv3; the list (https://creativecommons.org/compatible-licenses/) does not name AGPLv3. Keep the text and the code under their respective licences.
- **AGPL and a published edition.** A built edition is not only output: its browser scripts (`guide.js`, the optional `sw.js`) are code of this project, transferred to and run by every reader. Sections 1, 2, 4 to 6 (conveying, notices, corresponding source) and 13 (remote network interaction with a modified version) are the relevant ones. A public repository helps but is not, by itself, a guarantee of compliance: keep the notices, mark the changes and offer the source matching what is published. Every edition built with `build.py` carries its licences, notices and a ZIP of its source to help with that; it is not legal advice.
- **CC BY-SA and a paid or printed edition.** Allowed. The adaptation of the text must stay under CC BY-SA 4.0 with credit; the price, the paper and the logo are the edition's own.

## What was not done

- No legal review. This inventory is a careful reading of notices and licences by the people who prepared the repository, not legal advice.
- The links to external sources were not systematically rechecked for availability or for changed terms (see the table above).
- The CC BY-SA 4.0 text in `LICENSE-CONTENT` was compared with the official HTML legal code, not byte for byte with the official plain-text download.
