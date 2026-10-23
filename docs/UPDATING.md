# Taking updates from the base

Your edition is a copy. The base keeps improving: a corrected fact, a new tool in a table, a clearer tutorial, an accessibility fix, a new option in the generator. Nothing reaches your edition unless you pull it. This page shows how to see what changed, take it, and keep your adaptations. No method can promise that every customisation survives every update untouched: where you and the base changed the same lines, you decide by hand.

## What usually changes on which side

| Usually only yours | Shared with the base, changes in updates |
|---|---|
| `edition.json`, `assets/`, `custom.css`, your `editions.json` entries, a folder edition under `examples/<slug>/`, any file you created (a new chapter, a language folder) | `build.py`, `release.py`, `theme/`, `tests/`, `docs/`, `README.md`, `AGENTS.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `.github/` |
| | `content/en/*.md`, `strings.json`, `actions.json`, `links.json`, `book.json` |
| | `LICENSE`, `LICENSE-CONTENT`, `NOTICE`, `THIRD-PARTY.md` |

The base avoids touching the files in the left column, but it may, for example to add a key to the root `edition.json` or an entry format to `editions.json`. If you edited a file of the right column (a chapter you localised, the stylesheet), a merge can stop on that file. That is normal: it is solved by hand, once per file.

## With a fork (recommended)

On GitHub, the button **Sync fork** of your repository merges the base when there is no conflict. With Git:

1. Add the base as a remote, once: `git remote add upstream <address of the base repository>`.
2. See what changed:

   ```bash
   git fetch upstream --tags
   git log --oneline HEAD..upstream/main
   git diff --stat HEAD...upstream/main
   ```

   Read the entries of [CHANGELOG.md](../CHANGELOG.md) between your version and theirs: they say what changed and whether something needs your attention (a renamed key, a reworded action).
3. Work on a branch, so that your published edition stays as it is until you are happy: `git switch -c update-1.1.0`, then `git merge upstream/main` (or the tag, `git merge v1.1.0`).
4. Resolve conflicts. `git status` lists the files. In each, keep your adaptation where it was deliberate, take the base's change where it is a fix, remove the markers, `git add` the file. `git diff upstream/main -- <file>` shows how your file differs from the base afterwards. If you get lost, `git merge --abort` returns to where you were.
5. Check:

   ```bash
   python3 -m unittest discover tests
   python3 build.py --check
   ```

   The tests compare the 18 chapter ids and 90 action ids with `tests/reference-ids.json`: readers' ticks are stored under them. If the base reworded an action, it kept the id and put the old wording in `previous_texts`; the build accepts both texts. If you reworded the same action yourself, the build lists it: put your text in `text` and keep the other wordings in `previous_texts`.
6. Preview (`python3 build.py --serve`), tick 1 action, reload: it stays ticked. Then merge your branch, publish, and note the version you are based on (`git describe --tags upstream/main`).

Only some files? `git checkout upstream/main -- content/en/14-email.md` takes 1 chapter. `git checkout HEAD -- build.py theme/` after a merge keeps your own generator and theme; you then maintain them yourself.

## With a repository made from the template

A repository made with "Use this template" starts with a fresh commit and shares no history with the base, so Git cannot tell which side changed what. 2 ways:

- **Compare and copy.** Download the new version of the base into another folder, compare it with yours (Meld, WinMerge, Kaleidoscope, `diff -r`), and copy the files you want: usually `build.py`, `release.py`, `theme/`, `tests/`, then chapters one by one. Then the checks of step 5 above.
- **Merge once with unrelated histories.** `git remote add upstream <address>`, `git fetch upstream --tags`, `git merge --allow-unrelated-histories v1.1.0`. Every file that exists on both sides with differences becomes a conflict, including files you never touched, because Git has no common starting point. After this first merge, later merges work like a fork's.

## Without Git (a downloaded copy)

Same as "compare and copy" above. Keep a note of the version you downloaded (it is in `CHANGELOG.md` and in the `generator` line of every page), so that you know what to compare against next time.

## Stable ids across updates

An action keeps its id when it is reworded, and an id is retired, never reused, when an action disappears. Chapter ids and part numbers are addresses: the base does not rename them lightly, and when it must, `CHANGELOG.md` says so in a section "Needs your attention". Your readers' ticks and bookmarks survive updates as long as the ids and your `storage_key` stay the same.

## What the base does not do

- It does not pull your changes. See `CONTRIBUTING.md` to send them.
- It does not notify you. Watch the repository on the forge (Releases only), or run `git fetch upstream` now and then.
- It does not check your edition. The directory in `editions.json` is a list, not a monitor.
