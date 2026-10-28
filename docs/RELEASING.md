# Releasing a version of the base

For the maintainers of the base repository. Editions do not need this page; they follow `UPDATING.md`.

## Before a release

1. Everything merged into `main` passes:

   ```bash
   python3 -m unittest discover tests
   python3 build.py --check
   python3 build.py --edition examples/riverside-meetup/edition.json --out dist-riverside --check
   python3 build.py --edition examples/harbour-circle/edition.json --out dist-harbour --check
   ```

2. Choose the number. Patch (`1.0.1`): fixes of text, theme or generator that change nothing for an edition's configuration. Minor (`1.1.0`): new options or content, existing editions build unchanged. Major (`2.0.0`): an edition must change something (a renamed key, a removed option, a chapter id that changes).
3. Set `VERSION` at the top of `build.py`.
4. Add the entry to `CHANGELOG.md`, newest first, with the date. Write for the maintainer of an edition: what changed, and under "Needs your attention" anything they must do. Name every reworded or retired action id and every renamed chapter id there.
5. If chapter or action ids changed on purpose, update `tests/reference-ids.json` in the same commit, and say why in the changelog.
6. Look at what will be public: `git status`, `git diff`, and the files of the source archive (`python3 -m zipfile -l dist/source/guide-to-autonomy-source.zip`). No local path, no private note, no report about other people, no secret. `build.py` stops on common local paths; it cannot judge the rest.

## Actions of the workflows

Once a year, or when GitHub warns about them in a run, check the major versions used in `.github/workflows/` against the latest releases of each action (`gh api repos/actions/<name>/releases/latest`), read their breaking changes, and keep the checks job on a runner image that still provides Python 3.9 as long as the kit supports it.

## Tag and publish

```bash
git commit -m "Release 1.1.0"
git tag -a v1.1.0 -m "A Guide to Autonomy 1.1.0"
git push origin main v1.1.0
```

Then, on the forge, create a release from the tag with the changelog entry as its text. Attaching a ZIP is optional: the forge offers the source of every tag.

A pushed tag is not moved or deleted afterwards. A mistake is fixed with a new version.

## Directory requests

Requests from the issue form "List my edition" are added by hand to `editions.json`:

1. Open the address. It must be an edition of this book with its page "Licences, credits and source".
2. Add the entry with `consent`: `{"public_listing": true, "date": "<date of the request>", "reference": "<address of the issue>"}`.
3. `python3 -m unittest discover tests` checks the file format. Close the issue with a link to the commit.

Removal requests are applied the same way, without discussion.
