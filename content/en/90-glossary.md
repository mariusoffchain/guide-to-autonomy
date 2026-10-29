# Glossary

The words that come back throughout this book, in plain language.

## Privacy

**Encryption.** Scrambling information so that only someone holding the right key can read it.

**End-to-end encryption.** Encryption where only you and the person you talk to hold the keys. The service in the middle carries the message but cannot read it.

**Confidentiality.** Nobody except the 2 people talking can read the message.

**Authenticity.** The guarantee that the person at the other end is really who you think, and that the message was not altered on the way. Encryption alone does not give it.

**Trusted third party.** An intermediary whose honesty the whole system depends on. A messenger that hands out its users' keys from its own directory is one, even when it encrypts end to end.

**Forward secrecy.** A design where a key stolen one day cannot unlock the messages exchanged before.

**Metadata.** Not what you say, but who you talk to, when, from where and how often. Often more revealing than the content itself.

**Open source.** Software with public source code and a licence allowing use, modification and redistribution. Public code alone is not enough, as chapters 10 and 11 explain.

**Tracker.** A piece of code inside a site or an app that reports what you do to a third party, usually an advertising company.

**Fingerprinting.** Recognising your browser or device from its technical details (screen, fonts, settings), even without cookies.

**Password manager.** An encrypted vault that creates and remembers a different strong password for every site. You remember only one.

**Two-factor authentication (2FA).** A second proof on top of your password: a code from an app, or a physical key.

**SIM swap.** A fraud where someone convinces your operator to move your phone number to their SIM card, and then receives your SMS codes.

**Alias (email).** A disposable address that forwards to your real mailbox. One per service, so a leak can be traced and switched off.

**VPN.** A service that carries your traffic through its own server. It hides your activity from your internet provider and your address from the sites you visit, but the VPN company itself must be trusted.

**Tor.** A network that routes your traffic through several independent volunteers, so that none of them knows both who you are and what you visit.

**Mixnet.** A network that, in addition to routing through several hops, mixes and delays traffic to hide timing patterns.

**Threat model.** The honest answer to the question "who do I want to protect myself from?". It decides how far you need to go.

## Autonomy

**Private key.** A long secret number that only you hold. It proves you are you, and whoever holds it controls the identity or the money behind it.

**Public key.** The matching number you can share freely. Others use it to check your signature or to write to you.

**Passkey.** A key pair used to log in to a website or app. The service keeps the public half. The private half stays in a device or may sync in encrypted form through a passkey provider. A hardware security key keeps it on the key itself.

**Decentralised.** Run by many independent parties, with nobody able to switch it off, censor it or change the rules alone.

**Self-hosting.** Running a service on a machine you control instead of renting it from a company.

**Nostr.** An open protocol for social media. Your identity is a key pair, and your posts travel through relays that anyone can run.

**npub and nsec.** Your public key (npub, your public identity) and your secret key (nsec, never share it) on Nostr.

**Relay.** A simple server that stores and forwards Nostr posts. You can use several, and change at any time.

**Zap.** A small Lightning payment sent to someone on Nostr, as a tip or a thank you.

## Money and savings

**Inflation.** The rise of prices over time, which is the same thing as money losing purchasing power. National currencies are designed to lose a little value every year.

**Counterparty risk.** The risk that whoever holds an asset for you (a bank, a broker, an exchange) fails, or refuses to give it back.

**Self-custody.** Holding an asset yourself, with no intermediary: coins in your hand, keys in your possession. No company can freeze it, lend it or lose it for you.

**Custodial.** A company holds the asset for you. Convenient, but what you own is a promise.

**Monero.** A digital currency with a purpose similar to Bitcoin's, money you can hold yourself, where amounts, senders and receivers are hidden by default. Used by some advanced users as a private complement to Bitcoin. It is much less liquid and much less accepted, its much smaller network is easier for an outside entity to attack, as the block reorganisations of 2025 showed, and its development is more centralised (chapter 12).

**KYC (know your customer).** Mandatory identity checks by financial companies. They link your name to what you own in a database.

**MiCA.** The EU regulation on crypto-asset services, applied since 30 December 2024. Exchanges, brokers and custodial wallets need a licence and must identify their users (chapter 16).

**DAC8.** An EU tax directive, applied since 1 January 2026. Crypto-asset service providers report the transactions of their EU-resident users to the tax authorities (chapter 16).

**CBDC.** Central bank digital currency, money issued in digital form by a central bank for the public. The issuer sits in the payment path, so what it can see, limit or block depends on the design of the system and on the law. The digital euro is a proposed CBDC (Part 3).

## Bitcoin

**Bitcoin.** Digital money with no issuer and a fixed supply of 21 million. The rules are enforced by thousands of independent computers.

**Sat (satoshi).** The smallest unit of bitcoin. One bitcoin is 100 million sats.

**Wallet.** An app or a device that holds your keys and signs your transactions. It does not hold coins: the coins are entries in the shared ledger.

**Seed phrase.** Recovery words for a wallet's keys, commonly 12 or 24 in BIP39, with other formats such as 20-word SLIP39 and native Electrum seeds. Recovery requires compatible software and any extra passphrase. Labels, multisig configuration and Lightning state can need separate backups (chapter 14).

**BIP39.** The most common standard for seed phrases, with 12 or 24 words taken from a fixed list of 2,048 English words (chapter 14).

**SLIP39.** A backup standard supported by Trezor, commonly 20 words, which can also split a seed into shares, for example any 2 of 3. It is not compatible with BIP39 (chapter 14).

**Passphrase.** An optional extra word or sentence added to a seed phrase. Each passphrase opens a different wallet, and a forgotten one means lost coins (chapter 14).

**Multi-signature (multisig).** A wallet that needs several independent keys to spend, for example 2 out of 3, kept in different places (chapters 14 and 17).

**xpub and output descriptor.** The public description of a wallet. The extended public key (xpub) lets software find its addresses, and the descriptor adds the rules and, for multisig, every cosigner's xpub. They cannot spend, but they reveal the wallet's activity, and a multisig wallet cannot be restored without them (chapter 14).

**Hardware wallet.** A small dedicated device that keeps your keys offline and signs transactions without exposing them to your computer or phone.

**Air-gapped.** A signing device that never connects to a computer. Transactions travel by QR code or memory card (chapter 17).

**Secure element.** A chip built to resist physical attacks, used in many hardware wallets to protect the keys (chapter 17).

**Reproducible build.** Software published so that anyone can rebuild it from the source code and get exactly the same file. It shows that what you install matches the published code (chapters 13, 17 and 18).

**Lightning.** A payment network built on top of Bitcoin, made for everyday amounts. Payments are usually instant and cheap, although some wallets charge a fee to open the first channel (chapter 13).

**Payment channel.** 2 people lock bitcoin together in an on-chain transaction, then move the balance between them as often as they like without touching the blockchain. Lightning is a network of such channels (chapter 15).

**Lightning invoice.** A one-time payment request, shown as a QR code or text, usually for a fixed amount and with an expiry (chapter 15).

**Lightning address.** A reusable address that looks like an email address (you@provider.com), convenient for tips and for getting paid. Most of them rely on a provider's web server (chapter 15).

**Lightning service provider (LSP).** A company that opens channels for a self-custodial Lightning wallet and relays its payments, such as ACINQ for Phoenix or Blocktank for Bitkit. It sees part of your payments and can refuse to relay them (chapters 13 and 15).

**Swap.** An exchange between 2 forms of bitcoin, for example on-chain and Lightning, or Lightning and Liquid, usually through an outside service (chapter 13).

**Liquid.** A sidechain of Bitcoin run by a federation of companies, which hold the bitcoin locked on the main chain (chapter 13).

**Spark.** A system for fast off-chain bitcoin payments in which a small group of operators co-sign each transfer. Users keep their keys and an exit to the blockchain (chapter 13).

**Ark.** A way to make fast, cheap off-chain payments in which many users share on-chain transactions through an Ark server. A balance expires unless the wallet refreshes it in time, and until then you can exit to the blockchain without the server (chapter 13).

**On-chain.** A transaction recorded directly in the Bitcoin ledger. Confirmation time and fees vary. Each new confirmation makes a reversal less likely, but there is no absolute finality. Often suited to larger amounts.

**UTXO (coin).** An amount of bitcoin you received and have not spent yet. A wallet usually holds several, like banknotes of different sizes (chapter 16).

**Change.** What comes back to you, on a new address of yours, when you pay with a coin larger than the amount due (chapter 16).

**Coin control.** Choosing yourself which coins pay a transaction, so that coins from different sources are not linked (chapter 16).

**Coinjoin.** A transaction built together by several people, with many inputs and outputs of the same amounts, so that ownership is harder to trace (chapter 16).

**Payjoin.** A payment in which the sender and the receiver both add coins, which breaks the assumption that all the inputs of a transaction belong to 1 person (chapter 16).

**Node.** A computer that keeps its own copy of the Bitcoin ledger and checks every transaction against the rules.

**Pruned node.** A node that checks the whole history but keeps only the recent blocks, so that it fits on a small disk (chapter 18).

**Electrum server.** Software that indexes your node's data so that wallets such as Sparrow or BlueWallet can ask it about your addresses (chapter 18).

**Proof of work.** The energy miners must spend to add a block. It makes the history of transactions extremely costly to rewrite.

**Peer-to-peer (P2P).** Directly between 2 people, with no company holding the funds in the middle.
