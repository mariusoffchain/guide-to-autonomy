# Chapter 14: Backing up your seed phrase

## In brief

Your recovery words back up the keys to your wallet, and the phone is a tool for using them. Many wallets use 12 or 24 words; some use a different format. Whoever reads the words can take the coins, and if you lose both the phone and the words, the coins can no longer be recovered. Write them by hand, keep 2 copies in 2 places you control, never make a digital copy, and test the backup with the method appropriate to your wallet while the amount is still small (step 6).

## No support desk, no reset button

With a bank, losing access is an inconvenience, because you prove who you are and someone resets it. Self-custody removes that someone. There is no support desk, no "forgot my words" button and no court that can order the network to give your coins back. It is what makes your bitcoin very hard to freeze or seize from a distance, and it also leaves you as the only person responsible.

2 things go wrong in real life, and they pull in opposite directions. The first is **loss**, when a phone falls into a lake, the paper is thrown out during a move, or a fire destroys the single copy. The second is **theft**, when the words were saved in a photo, an email draft, a cloud note or a password manager, and someone found them. In March 2025, US federal investigators [linked a theft of about 150 million dollars](https://krebsonsecurity.com/2025/03/feds-link-150m-cyberheist-to-2022-lastpass-hacks/), committed in January 2024, to secrets stored in the LastPass password manager, which had been breached in 2022. Coins stolen this way move within minutes and cannot be recalled, so a good backup has to protect against loss and theft at once.

## A single random number, written as words

When you create a wallet, the app generates a single very large random number, and everything else comes from it, meaning every key and every address for every coin you will ever receive in that wallet. A common standard called [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) writes this number, most often, as 12 or 24 words taken from a fixed list of 2,048 simple English words, because people copy words more reliably than long strings of digits. The last word includes a checksum, which detects most copying errors.

For keys derived from that seed, the words do not change after each payment. Recovery still needs a compatible backup format, the right address type or derivation path, and any passphrase you used. Trezor also supports SLIP39 backups, commonly 20 words; native Electrum seeds use a different scheme from BIP39. Do not assume that any wallet accepts any words.

Keep the wallet name and backup format with your recovery instructions. The seed alone does not restore labels, separately imported keys or every wallet setting; back up those according to the wallet's documentation.

Lightning is the exception. Funds in channels depend on the wallet that opened them, and some Lightning wallets need an extra backup file in addition to the words. If so, the app says it clearly, and its instructions come first.

## Nobody to trust, nobody to call

An on-chain seed backup in an open format can be recovered without the original company or an account, using compatible software and blockchain data. You still depend on the recovery software and device, and on a server unless you use your own node. Keeping only the words is not enough for every wallet design, especially Lightning and multisig. The backup's availability and confidentiality rest on you.

Every convenience that softens this brings a third party back. A steel plate ordered online puts your name and address in a maker's customer file, the kind that leaked at Ledger in 2020 (see "Mistakes to avoid"). Shamir shares and multi-signature spread the risk, but each person holding a share or a key can lose it or collude, and the software that splits and rebuilds the secret has to be trusted too. Any service that offers to recover your seed for you goes further. To return a backup after an identity check, a company has to hold it outside your home, where it can be breached, compelled or closed. It can suit someone who fears loss above all, knowing that trusted third parties are then back in the picture.

Verification means checking that the backup works with the recovery procedure appropriate to your wallet (step 6).

## Choose how to store it

The right support depends on the amount and on what threatens your home, whether water, fire, burglars or curious visitors. All of the options below keep the words offline, and they can be combined.

| Method | Cost | Who you must trust | Strength | Weakness |
|---|---|---|---|---|
| **Paper**, pencil or permanent ink | Almost nothing | Nobody, apart from the people who can reach the place where it is kept | Immediate, no tool needed | Water, fire, fading, easily thrown away by mistake |
| **Laminated paper** | A few euros | Nobody, as long as the laminator is yours. A copy shop would be a third party. | Resists water and wear | Still burns. Use your own laminator, not a copy shop. |
| **Steel product**: Cryptosteel, Seedor and others | Tens of euros, up to about a hundred | The maker and the shop, which learn your name and address, but never the words | Resists fire, water and time | The price. A visible object that says "bitcoin" to whoever finds it. |
| **DIY steel**: letters stamped into steel washers held on a bolt | A few euros of hardware, plus a set of letter stamps | Nobody. A hardware shop has no idea what the washers are for. | Same resistance, discreet, no brand to trust | An hour of work, and care when stamping |
| **Passphrase** (the optional "25th word") | Free | Nobody else, provided it is written down and kept apart from the words | The words alone are no longer enough for a thief, if the passphrase is long and random | A short or guessable one adds almost nothing. An extra secret to back up and to pass on. Forgotten passphrase, lost coins. |

There are also 2 advanced options, for larger amounts:

- **Splitting across locations.** Standard schemes such as Shamir backup ([SLIP39](https://github.com/satoshilabs/slips/blob/master/slip-0039.md)), supported by some hardware wallets, divide the secret into shares, for example any 2 of 3. SLIP39 uses its own word list and is not compatible with BIP39, so only wallets that support it can restore it. Do not invent your own scheme by cutting the word list in half (the next section explains why).
- **Multi-signature.** A wallet that requires several independent keys, for example 2 of 3, kept in different places, so that a single theft or loss is not fatal. Keep enough signing-key backups and the complete wallet configuration or output descriptor, including every cosigner's extended public key (xpub). Enough seeds alone may be insufficient. The descriptor cannot spend on its own but exposes wallet information, so protect its privacy. Chapter 17 introduces the devices that make this practical.

A reasonable starting point for most people is paper on the first day, then a steel copy once the amount would hurt to lose, without a passphrase until you fully understand it. Beyond that, setups legitimately differ, as the next section shows.

## No single right setup

There is no single right setup, because amounts, homes, families and threats differ, and 2 careful people can reasonably choose differently. The 3 main approaches can be combined.

| Approach | What you gain | The price |
|---|---|---|
| **Several independent keys**, or several hardware wallets, for different purposes such as spending and savings | A theft or a mistake touches 1 wallet, not everything | More backups to store, label and test |
| **1 key whose backup is split into fragments** kept in different places, with a copy of each fragment in 2 places | Losing 1 place does not lose the money, and finding 1 fragment does not reveal it | More places and people involved, and a restore that needs compatible software |
| **1 key plus a passphrase** (the optional extra word or sentence) | The words alone no longer open the wallet | 1 more secret to back up and to pass on |

Shamir secret sharing and multi-signature are different. In a proper threshold secret-sharing scheme, fewer than the required shares reveal no secret. Multisig uses independent keys; 1 key does not authorise spending when the threshold is higher, but may reveal wallet information. Preserve the full multisig configuration as well as the keys. Cutting the word list yourself gives each finder part of the secret, and in June 2020 John Cantrell [found the 4 missing words of a 12-word phrase in about 30 hours](https://bitcoinwords.github.io/how-i-checked-over-1-trillion-mnemonics) with rented graphics cards.

An attacker who holds the words can also try passphrases very fast, so a short or guessable one adds almost no security, and it has to be long and random. Each different passphrase opens a different wallet, which allows separate or hidden sub-accounts. It must itself be backed up, separately from the words, where your heirs can find it.

The practical criterion is to choose the simplest setup you will still understand, and be able to restore, in 10 years.

## Step by step

The example uses paper and a pen. The logic is the same on steel.

1. **Choose the moment.** Alone, at a table, no camera behind you, not in a café or on a train.
2. **Write the words by hand**, numbered, in order, in clear capital letters. Note the wallet's name and the date, not the amount.
3. **Check them twice.** Read them back against the screen, word by word. Most wallets then ask you to confirm some of them.
4. **Never make a digital version.** Do not type, photograph, print, dictate or email the words, and do not store them in the cloud or in a password manager. For a signing device, keep its backup out of ordinary software wallets. Follow its official backup-check and recovery procedure; do not type the words into an online device merely to test them.
5. **Make 2 copies** and store them in 2 places you control, for example your home and the home of a close relative, each in a sealed envelope. The second place is a trade-off, because without a passphrase whoever opens the envelope controls the coins. Choose someone you would trust with the same amount in cash, and consider one of the approaches above once the amount grows. If you use fragments or a passphrase, the rule of 2 copies applies to each of them, and a passphrase is never stored with the words.
6. **Test the backup in the right environment.** For a small on-chain **software wallet**, restore on a second device you control with compatible software, compare its addresses and balance, then remove the test copy. Keep the original app throughout; this protects against a copying mistake, not against malware on the second device. For a **hardware wallet**, use the maker's backup-check feature or restore on compatible hardware through its official procedure. Never import a hardware-wallet seed into a phone or computer just for this test. A wipe-and-restore exercise is for a tiny test balance before savings are added (chapter 17).
7. **Treat a Lightning wallet differently.** Deleting an app that holds open channels can cost you the funds if the restore fails, and Phoenix, for example, [warns against running 2 apps on the same seed](https://phoenix.acinq.co/faq). Read your wallet's restore instructions first. The real test usually comes when you change phones, with a small balance, the old phone switched off, and the old app kept until the balance shows on the new one.
8. **Plan the inheritance.** Add a sealed letter explaining in plain words what this is, that it has value, that the words must never be typed into a website, who can be trusted to help, and how many pieces your setup has (words, fragments, passphrase) and where each is kept.

## Mistakes to avoid

- **Keeping a digital copy.** Photos, notes, email drafts and cloud drives are exposed to malware and intruders. Deleting a file does not undo exposure or remove every synced copy. If the words may have leaked, follow the maker's instructions to create a fresh wallet and move the funds safely; never wipe your only working wallet first.
- **Keeping a single copy.** A fire, a flood or a house move is enough to lose it, which is why you keep 2 copies in 2 places.
- **Telling people how much you own.** In December 2020, the names, postal addresses and phone numbers of [about 272,000 Ledger customers](https://www.ledger.com/message-ledgers-ceo-data-leak) were published on a hacking forum after a breach of the company's shop database, and these customers were then targeted by phishing campaigns. Talk about Bitcoin as much as you like, not about your balance.
- **Entering your words into a website or giving them to "support".** No wallet team, exchange or authority will ever ask for them, so whoever asks is attempting a theft.
- **Building a scheme you will not remember in 5 years.** Words hidden in a book, split in 4, with an improvised code, have locked many people out of their own coins. Keep the scheme simple, documented and tested.
- **Never testing, or testing by deleting the app.** An untested backup may contain a wrong word, and if you delete the app first you discover it after the only working copy is gone. Use the software or hardware procedure appropriate to your wallet (step 6).

## Go further

- **Steel backups tested against fire, acid and a press:** Jameson Lopp's metal storage reviews (jlopp.github.io/metal-bitcoin-storage-reviews).
- **Backup and recovery tutorials:** Plan B Academy (planb.academy).
- **The standard itself and its word list:** BIP39, in the Bitcoin improvement proposals (github.com/bitcoin/bips).
- **Which wallet can restore which seed:** Wallets Recovery (walletsrecovery.org).
- **Next chapter:** Lightning and euros in everyday life.

## Sources

- [Understanding Trezor backups, 12, 20 or 24 words](https://trezor.io/learn/security-privacy/personal-security-standards/understanding-trezor-wallet-backups-12-20-or-24-words), Trezor, checked 22 October 2026.
- [Seed version system](https://electrum.readthedocs.io/en/latest/seedphrase.html), Electrum documentation, checked 22 October 2026.
- [How to use a wallet backup](https://trezor.io/guides/backups-recovery/general-standards/how-to-use-a-wallet-backup), Trezor, checked 22 October 2026.
- [Move crypto to a wallet with a new backup](https://trezor.io/guides/backups-recovery/general-standards/move-crypto-to-a-wallet-with-a-new-wallet-backup), Trezor, checked 22 October 2026.
- [Multisig backup warning and descriptor export](https://github.com/sparrowwallet/sparrow/blob/master/src/main/java/com/sparrowwallet/sparrow/wallet/MultisigBackupDialog.java), Sparrow source code, checked 22 October 2026.
- [Feds Link $150M Cyberheist to 2022 LastPass Hacks](https://krebsonsecurity.com/2025/03/feds-link-150m-cyberheist-to-2022-lastpass-hacks/), Krebs on Security, 6 March 2025.
- [Message from Ledger's CEO on the data leak](https://www.ledger.com/message-ledgers-ceo-data-leak), Ledger, 21 December 2020.
- [BIP39: Mnemonic code for generating deterministic keys](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), Bitcoin Improvement Proposals, 2013.
- [SLIP39: Shamir's Secret-Sharing for Mnemonic Codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md), SatoshiLabs, consulted in September 2026.
- [How I checked over 1 trillion mnemonics in 30 hours to win a bitcoin](https://bitcoinwords.github.io/how-i-checked-over-1-trillion-mnemonics), John Cantrell, republished by WORDS Bitcoin Journal, 18 June 2020.
- [Phoenix FAQ: restoring a wallet, limitations](https://phoenix.acinq.co/faq), ACINQ, consulted in September 2026.

## Your checklist

- [ ] Write your words by hand and check them twice (5 min)
- [ ] Remove digital seed copies; if exposure is possible, move funds safely to a fresh wallet, since deletion does not undo a leak (1 hour)
- [ ] Make a second copy and store it in a second place (1 hour)
- [ ] Test a tiny software wallet on a second device without deleting the original; check hardware backups only with the maker's hardware procedure (1 hour)
- [ ] Write the sealed letter for your family and make a steel copy (weekend)
