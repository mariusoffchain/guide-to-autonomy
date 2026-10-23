# Contributing to the base

Every edition is independent and nobody has to send anything back. When you want to, here is how it works and what it does not do.

## What the base is, and is not

The base repository holds 1 version of the book: the English text, the generator, the theme, the documentation. It is what a community forks. It is **not** a portal, a directory you must register with, a canonical site, or a place where every fork's changes are collected. Nothing is aggregated automatically:

- a change you make in your fork stays in your fork until you open a pull request;
- a change merged into the base reaches another edition only when its maintainer pulls it (see `docs/UPDATING.md`);
- the optional `editions.json` lists the editions that asked to be listed, nothing more, and no script checks whether they are still online.

The base is carried by Cypher Baltics, who review pull requests and keep the repository healthy. That role is coordination, not authority over the forks.

## What is welcome

- **Corrections**: a wrong fact, a dead link, a tool that changed its terms, a typo. Say what changed and give a source with a date.
- **Better tutorials and comparisons**: a step that was unclear, a missing option, a tool that deserves a row in a table. Keep the tone of the book: several options, no single recommendation, the trust question made explicit, sources next to the claims.
- **Translations** of the whole book or of `strings.json` as a new `content/<lang>/` folder (see `docs/TRANSLATING.md`). Partial translations can be proposed as work in progress in a branch.
- **Generator and theme**: accessibility, right-to-left support, build checks, hosting recipes, anything that makes a fork easier. Keep the zero-dependency rule for the pages (no external script, no CDN) and the single Python dependency for the build.
- **Documentation**: everything that made your own fork harder than it should have been.
- **Your edition in the directory**: open the issue form "List my edition", or a pull request adding 1 entry to `editions.json` in the format of its `entry_format`, including `consent` (the date and the address of your request). A maintainer adds entries by hand and may decline one; ask in the same way to be removed. The list is published only by the editions that turn the page on, and no script checks the listed sites later. The repository address is how others can learn from your adaptations; it does not replace the licences, notices and source ZIP that every built edition ships.

## What is not merged into the base

- Identity: a community's name, logo, colours or sponsor references. They belong in the fork's `edition.json`. The base stays neutral so that every fork starts from the same place.
- Local-only content, such as the list of shops in your city or your meetup programme. Keep it in your fork; if the mechanism to hold it (a template, a configuration key) is useful to others, propose the mechanism.
- Recommendations without sources, affiliate links, paid placements.
- Changes that remove the attribution or alter the licences.

## How to send a change

1. Fork the base (or use the fork your edition already is), create a branch, make the change.
2. Run `python3 -m unittest discover tests` and `python3 build.py --check`. If you changed a checklist action, read what the build says about `actions.json` and keep IDs stable (`--update-actions` only for really new or removed actions).
3. Open a pull request with: what changed, why, the sources, which edition it comes from. 1 subject per pull request.
4. By sending it you agree that the text is under CC BY-SA 4.0 and the code under AGPL-3.0-or-later, like the rest of the repository, and that you have the right to contribute it.

Without a forge account, an email to the contact of the base repository with a patch or a description is fine; it will just take longer.

## Getting changes back into your edition

Read `docs/UPDATING.md`. In short: the base rarely touches your edition's own files, files you and the base both changed stop the merge with a conflict that you resolve by hand, and the tests check that the ids of chapters and actions are still those your readers' ticks use.

## Versions

Maintainers of the base follow `docs/RELEASING.md`: every release has a number, a Git tag and an entry in `CHANGELOG.md`, written for the people who maintain an edition (what changed, what needs their attention).

## Where to talk

The issue tracker of the base repository. Mirrors on other forges, a mailing list or a chat for maintainers may come later; this file will say so.
