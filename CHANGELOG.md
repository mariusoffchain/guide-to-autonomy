# Changelog

What changed in each version of the base, for the people who maintain an edition. Versions follow `MAJOR.MINOR.PATCH`: a patch fixes, a minor version adds without breaking an edition, a major version may need changes in editions (always listed under "Needs your attention"). Each version has a Git tag `v<version>`. How to take an update: [docs/UPDATING.md](docs/UPDATING.md).

## 1.2.0, 2026-10-29

A full review of the text. Facts that had moved since September 2026 were checked again on 29 October 2026 and updated with their sources, beginners get the backup steps that were missing, and the base says openly that it is written for the European Union.

### Book

- **Updated facts.** Chat Control (Council position of November 2025, 6th trilogue on 29 September 2026, interim Regulation (EU) 2026/1881 until 3 April 2028). Session's protocol upgrade on hold and Threema's new owner. KeePassXC's certification version. Siri app in iOS 27, llama.cpp team at Hugging Face, Locally AI bought by LM Studio, Venice paid modes. StartOS 0.4.0 (Tor optional, old backups not restorable) and umbrelOS Tor access. Android developer verification in force since 30 September 2026. Mt. Gox repayments postponed again, without a deadline in the text. Boltz suspension and its effect on the Blockstream app. Digital euro mandate of the European Parliament. Bisq 1 and Bisq Easy told apart: Bisq Easy has no escrow.
- **Safety steps added.** Signal backups with their recovery key, and the Signal PIN kept in the password manager. The password manager's own recovery code never only inside it. Both paper copies replaced after regenerating recovery codes. Backup passwords and the Advanced Data Protection key on paper. What an Ark balance expiry means. A warning against Bitcoin ATM scams. An inheritance letter that never contains the words.
- **Chapter 17** adds COLDCARD to the table of devices, with the July 2026 seed-generation flaw and its licence.
- **A European base, said openly.** Part 3 states that its legal and banking examples are those of the EU and the euro area. The remaining Lithuanian and regional references are gone, and the introduction no longer assumes the reader comes from a talk. Chapter 15 uses a generic Lightning walkthrough.
- **Glossary.** 25 new terms (MiCA, DAC8, BIP39, SLIP39, passphrase, multisig, xpub and output descriptor, air-gapped, secure element, reproducible build, payment channel, Lightning invoice, Lightning address, LSP, swap, Liquid, Spark, Ark, UTXO, change, coin control, coinjoin, payjoin, pruned node, Electrum server) and a neutral CBDC definition.
- **Style.** Sentences patched with semicolons are rewritten as short sentences. Repeated formulas are gone. 1 unsourced sentence and the FreeAI Manifesto entry are removed.

### French

- **The book in French joins the base**: `content/fr/` (23 texts, interface, 90 actions with the same ids) and `languages/fr/edition.json`. It follows this version of the English text, with the same neutral identity. The base site publishes it under `/fr/`, and a language button links the 2 editions.

### Editions

- The base edition shows the "Other editions" page, with the PROOF edition, the original one, as its first entry. The README links to it under "See it live".
- `docs/CUSTOMIZING.md` lists the passages to adapt outside the European Union.
- Theme: the progress line of a checklist keeps its spaces, a long community name on the cover breaks between syllables instead of between letters, and the "Other editions" page no longer overflows on a phone.

### Building and publishing

- The GitHub Pages workflow also builds every `languages/<code>/edition.json` into `<code>/` of the same site (input `languages`, on by default), and the checks run `--check` on each of them. A test makes sure every language keeps the reference ids. See `docs/TRANSLATING.md` and `docs/HOSTING.md`.

### Needs your attention

- 4 actions are reworded, with the same ids, so readers' ticks are kept: `passwords-5`, `nostr-first-zap`, `seed-delete-digital-copies`, `seed-test-recovery`. Their former wording is in `previous_texts`. If you translated them, update your translation.
- The base `edition.json` now has `directory.enabled: true` and links to the French edition in `other_editions`. When you merge, keep your own values for these 2 keys.
- `languages/fr/` is built by the Pages workflow with the address of the base site in its `other_editions`. Adapt it to your own address, or remove the folder if your edition has no French version (`AGENTS.md`, step 4).

## 1.1.0, 2026-10-29

A neutral base: nothing in the pages of an edition names the original event any more, apart from the credit on the page "Licences, credits and source".

### Book

- The 3 parts are called **Privacy**, **Autonomy** and **Money**, instead of titles built on the word "proof". The introduction presents them as "3 parts", and the opening essay of part 3 no longer explains the double meaning of its former title. Chapter 11 announces "Part 3, Money".
- The address of the part 3 opening becomes `money/` (it was `work/`). Part ids (`part-1` to `part-3`), the 18 chapter ids and the 90 action ids do not change, so readers' ticks are kept.

### Editions

- The credit to the original work moves to the page "Licences, credits and source", which every footer and the colophon link to. It is no longer printed in the footer of every page nor on the cover. The credit, the licences and the source archive are unchanged.

### Needs your attention

- Links to `<your edition>/work/` from outside now land on the 404 page; point them to `money/`. To keep the former address, set `"slug": "work"` for part 3 in your `content/en/book.json`.
- If you kept the former part titles on purpose, for example an edition tied to the original event, keep your own `book.json` titles and the `#` lines of `10-part1-privacy.md`, `20-part2-autonomy.md` and `30-part3-work.md` when you merge: they must match each other.

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
