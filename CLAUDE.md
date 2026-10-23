# CLAUDE.md

Read `AGENTS.md`: it holds the complete instructions for helping someone create and publish their community's edition of this book, the rules (permissions with a scope, never asked twice; no secrets, no deletion, licences untouched) and the order of questions to ask.

Quick facts for any session in this repository:

- Build: `python3 build.py --check` (verify, write nothing), `python3 build.py --serve` (build `dist/` and preview on http://127.0.0.1:8000/). Only dependency: `python3 -m pip install -r requirements.txt`.
- Configuration lives in `edition.json`; every key is documented in `docs/CONFIGURATION.md`. Text lives in `content/<lang>/`. Theme in `theme/`. Example edition in `examples/riverside-meetup/`.
- Licences: text CC BY-SA 4.0 (`LICENSE-CONTENT`), code AGPL-3.0-or-later (`LICENSE`), third-party inventory in `THIRD-PARTY.md`. Keep headers and attributions.
- Tests: `python3 -m unittest discover tests`. `tests/reference-ids.json` guards the 18 chapter ids and 90 action ids.
- Numbers in digits, no marketing tone, no em dashes in the text you write.
