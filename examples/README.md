# Example editions

Complete, buildable editions to copy from. Everything in them is fictional: the communities do not exist and the addresses are `example.org` domains reserved for documentation.

- `riverside-meetup/`: a dark edition with a logo, a bundled heading font (JetBrains Mono, OFL), a serif body font, normal-case headings, a sub-folder address (`/guide/`), the offline copy, a second language in the header and the optional "Other editions" page. `python3 build.py --edition examples/riverside-meetup/edition.json --out dist-riverside --serve`
- `harbour-circle/`: the second test edition, created by following `AGENTS.md` only (an AI assistant working from the instructions, without reading the generator). Light, no logo, minimal changes. See its `NOTES.md` for what was unclear in the instructions at the time and what was fixed as a result.

To start your own edition, you do not copy an example: edit `edition.json` at the root of your fork. Copy an example only if you want to keep several editions in 1 repository.
