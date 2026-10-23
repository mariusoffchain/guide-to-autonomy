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

**Open source.** Software with public source code and a licence allowing use, modification and redistribution. Public code alone is not enough; see the licence distinctions in chapters 10 and 11.

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

**Passkey.** A key pair used to log in to a website or app. The service keeps the public half. The private half stays in a device or may sync in encrypted form through a passkey provider; a hardware security key keeps it on that key.

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

**CBDC.** Central bank digital currency, money issued digitally by a central bank. Who can see or control payments depends on its design and laws. For the proposed digital euro, the [ECB describes](https://www.ecb.europa.eu/euro/digital_euro/features/privacy/html/index.en.html) offline privacy and limits on its own access to identifiable payment data; these are design commitments, not a deployed system.

## Bitcoin

**Bitcoin.** Digital money with no issuer and a fixed supply of 21 million. The rules are enforced by thousands of independent computers.

**Sat (satoshi).** The smallest unit of bitcoin. One bitcoin is 100 million sats.

**Wallet.** An app or a device that holds your keys and signs your transactions. It does not hold coins: the coins are entries in the shared ledger.

**Seed phrase.** Recovery words for a wallet's keys, commonly 12 or 24 in BIP39, with other formats such as 20-word SLIP39 and native Electrum seeds. Recovery requires compatible software and any extra passphrase; labels, multisig configuration and Lightning state can need separate backups (chapter 14).

**Hardware wallet.** A small dedicated device that keeps your keys offline and signs transactions without exposing them to your computer or phone.

**Lightning.** A payment network built on top of Bitcoin: instant, nearly free, made for everyday amounts.

**On-chain.** A transaction recorded directly in the Bitcoin ledger. Confirmation time and fees vary. Additional confirmations reduce reversal risk; there is no absolute finality. Often suited to larger amounts.

**Node.** A computer that keeps its own copy of the Bitcoin ledger and checks every transaction against the rules.

**Proof of work.** The energy miners must spend to add a block. It makes the history of transactions extremely costly to rewrite.

**Peer-to-peer (P2P).** Directly between 2 people, with no company holding the funds in the middle.
