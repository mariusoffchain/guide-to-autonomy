# Harbour Circle edition: notes from the test of the fork path

Date: 2026-10-22. Written by the AI assistant that created this edition by following `AGENTS.md`, `README.md` and `docs/CONFIGURATION.md` only (plus `content/en/book.json` for the chapter ids, as step 3 of `AGENTS.md` says). The generator, the theme and the chapters were not read. The organiser is fictional and not a developer.

Environment: macOS, Python 3.9.6 (the minimum version), Markdown 3.9 already installed, git present with 1 commit and no remote.

## What was built

- `examples/harbour-circle/edition.json`: light scheme, warm off-white `#faf6ef` on dark brown `#2b1d14`, part accents sea green `#2e8b74` / `#1f6b58`, deep blue `#1f4e8c` / `#173d6e`, rust `#b7472a` / `#94381f`, no logo, system fonts, normal-case headings, kicker "Read along with the Circle", big button on `messages`, default intro and reading paths, 3 search suggestions, English, "Other editions" page on, storage key `guide-autonomy.harbour-circle.v1`, no address, no offline copy.
- `examples/harbour-circle/editions.json`: empty directory, so the "Other editions" page exists and can be filled later.
- Build: `python3 build.py --edition examples/harbour-circle/edition.json --out dist-harbour`, 28 pages, 90 actions, 1327 internal links checked. `--check` passed on the first run, for this edition and for the untouched root edition.
- Preview: `--serve --port 8765` in the background, `/`, `/messages/`, `/editions/`, `/actions/` all answered 200, server stopped.

## Build errors

None. The JSON was valid on the first attempt and the build never stopped. This means the error messages of the build were not tested in this exercise.

## Where the instructions were unclear, wrong, missing, or made me guess

1. **The organiser's main constraint is not covered.** `AGENTS.md` assumes the edition is the root `edition.json` (ground rule 5, every step, the step 7 commit). The organiser wanted a separate folder and a separate output folder. Nothing in `AGENTS.md` says how to do that. I found the way in `README.md` ("Commands": `--edition … --out …`) and in `examples/README.md` ("Copy an example only if you want to keep several editions in 1 repository"), and confirmed it with `python3 build.py --help`. `AGENTS.md` should have 1 paragraph: "if the person wants to keep the base intact or several editions, create `examples/<slug>/edition.json` and pass `--edition` and `--out` to every build command below".

2. **Ground rule 6 checks the wrong file in that case.** "After every change: `python3 build.py --check`" verifies the root `edition.json`, not the edition being worked on. A person following `AGENTS.md` literally in a folder edition would see "0 files to write, all up to date" and believe their edition is fine. I had to guess that `--check` combines with `--edition` and `--out`; `--help` does not say so either, it just lists the flags. It does work.

3. **`examples/README.md` describes this folder before it existed.** It already lists `harbour-circle/` and "its `NOTES.md`" with a summary of what the notes say. Anyone who read the examples folder before this commit found a dangling reference. The entry should be written after the edition, or marked as planned.

4. **The `about` key is undocumented.** `docs/CONFIGURATION.md` says "An unknown key stops the build with its name", yet the root `edition.json` and the Riverside example both carry an `about` key that is in no table. I kept it and hoped; the build accepted it. Either document `about` as a free comment key or remove it from the shipped files.

5. **Edition name length.** Step 1 says to suggest "<Community> edition". For "Harbour Privacy Circle" that gives a 4-word header. I shortened it to "Harbour Circle edition" by judgement; nothing says whether long names break the header. The same applies to `wordmark` (step 1 says 1 or 2 words, the default is the community name, which here has 3).

6. **Colours: the organiser asked me for hex values and the docs give no help choosing them.** Only the 2 default pairs are given. For "warm off-white", "dark brown", "sea green", "deep blue", "rust" I invented values and estimated contrast by eye; `docs/CONFIGURATION.md` says "the build does not compute contrast" and sends a non-developer to the browser developer tools, which is the one thing a non-developer will not do. A small table of tested pairs per scheme, or a contrast warning in `--check`, would remove this guess.

7. **The `text` colour of a part: 2 descriptions that do not quite match.** `AGENTS.md` step 2 says "if they give only 1 colour per part, use it for both and warn"; `docs/CONFIGURATION.md` says `text` defaults to `accent`. So the key can simply be omitted, but `AGENTS.md` makes the assistant write it twice. Harmless, but 1 sentence should point to the other.

8. **Search suggestions: "4 to 6 words" versus 3 given.** Step 3 asks for 4 to 6; the organiser gave 3. `AGENTS.md` does not say whether this is a hard rule. I kept the 3 words and the build accepted them.

9. **The empty "Other editions" page.** Step 4 and `docs/CONFIGURATION.md` do not say what the page shows when `editions` is empty, nor whether an empty list is valid. It is: the page says "No other edition is listed in this copy of the book yet." That sentence should be in the docs, because the organiser's exact request was "show the page even if empty".

10. **Format of `editions.json`: 2 different shapes in the repository.** The root file has an `entry_format` key and `docs/CONFIGURATION.md` says "the format is described inside the file"; the Riverside copy has no `entry_format`. I did not know whether `entry_format` is read, required, or merely a comment. I left it out and put the format in `about`; the build did not complain. Document the file in `docs/CONFIGURATION.md` directly instead of pointing inside it.

11. **`language.locale` is never asked.** Step 4 does not mention it; the root uses `en_US`, Riverside `en_GB`. A port city gives no hint. I chose `en_GB` without asking. It only affects an Open Graph tag, but the assistant should either ask or `AGENTS.md` should say "keep the default".

12. **The step 7 commit command stages everything.** `git add -A && git commit` would also stage any unrelated file lying around. For a folder edition the right command is `git add examples/<slug>`. `AGENTS.md` should mention it, and should say that `dist/` and `dist-*/` are already in `.gitignore` (I had to read `.gitignore` to be sure `dist-harbour/` would not land in the commit).

13. **Step 0 fork-or-download test has a third case.** "remote present = fork, no remote = plain download" does not cover a local git repository with commits and no remote, which is exactly what a ZIP user who ran `git init`, or this test, looks like. Step 7 handles it (option "keep it local for now") but step 0 should name it.

14. **`--port` exists but is not in the docs.** `AGENTS.md` and `README.md` only mention port 8000. When 8000 is busy (common on a developer's machine, rare for an organiser) the fix is `--port`, visible only in `--help`.

15. **pip noise.** `python3 -m pip install -r requirements.txt` printed a 2-line warning about an old pip version. `AGENTS.md` does not say it can be ignored; a non-developer would stop and ask.

16. **The check output does not name the edition file.** `--check` prints "Would write 32 files … -> …/dist-harbour" but not which `edition.json` it read. Combined with point 2, it is easy to check the wrong edition without noticing. `build-report.json` does record the edition path, but only after a real build.

17. **Ground rule 3 "never delete files" and `--out`.** Nothing says whether building into an existing non-empty folder overwrites or merges. `README.md` says "the build never deletes anything and writes only inside the output folder", which answers it, but that sentence is in `README.md`, not in `AGENTS.md` where the assistant looks when it worries.

## Questions I could not answer from the docs

- Is `about` an accepted key of `edition.json`? (answered by trying: yes)
- Does `--check` honour `--edition` and `--out`? (answered by trying: yes)
- Is `entry_format` in `editions.json` read by the build, required, or a comment? (unknown; left out, build passed)
- What does the "Other editions" page show when the list is empty? (answered by building)
- Which `locale` for an English edition outside the US? (guessed `en_GB`)
- Are 3 search suggestions acceptable? (build passed; the UI effect was not seen)
- How to commit only 1 folder when `AGENTS.md` prescribes `git add -A`? (used `git add examples/harbour-circle`)
- Do the chosen colours meet 4.5:1 on body text? (not verifiable without a browser; estimated only)

## Verdict

A non-developer with an AI assistant and a shell can do the standard path (edit the root `edition.json`) in well under 1 hour: the keys are clear, the defaults are good, the build passed first time and its summary line is readable.
The moment they step off that path (keep the base intact, several editions in 1 repository, pick their own colours), `AGENTS.md` goes silent and the answer is scattered across `README.md`, `examples/README.md`, `--help` and `.gitignore`, which a non-developer will not assemble alone.
Without an assistant, the same person would get stuck on hex colours and on `--edition`/`--out`, and would not know whether an empty directory page or an undocumented `about` key is a mistake.
