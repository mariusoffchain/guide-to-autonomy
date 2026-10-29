# Chapter 17: Hardware wallets

## In brief

A phone wallet suits pocket money, but savings call for something more solid. A hardware wallet is a small dedicated device that keeps your private keys offline and signs transactions inside itself, so that malware on your computer or phone does not get to see them. There are several good ones, with different trade-offs, and none of them is infallible. The device does not replace your seed backup (chapter 14), because it can break or be lost, and the backup is then what restores your funds.

## Keys on a machine that is always online

Your phone is online all day. It runs dozens of apps, receives links from strangers, connects to public wifi and installs updates from many companies, and your computer is no better. Each of these is a door, and a wallet app on the same machine keeps its keys behind those doors.

For the amount you would carry in a physical purse, that risk is acceptable, and the convenience is worth it. For savings, the calculation changes. Malware that reads a wallet file, replaces an address in the clipboard or records the screen exists and is sold as a ready-made product. A Bitcoin transaction cannot be reversed, and there is no support desk to call.

Nobody needs to become a security expert to deal with this. The practical answer is to move the keys off these machines, onto a device built to keep them out of reach of this kind of software.

## A small computer that only signs

A hardware wallet, more precisely called a **signing device**, is a tiny computer with a single job. It generates your seed, stores the private keys on its own chip, and is designed never to let them out.

When you want to send bitcoin, the work is split in 2:

1. An app on your computer or phone prepares the transaction. This app only knows your public information, so it can show your balance and build a payment, but it cannot spend.
2. The transaction goes to the device, by cable, Bluetooth, QR code or memory card. The device shows the amount and the destination address on its own screen. You check, you confirm on the device, and it signs internally. Only the signature comes back.

If your computer is infected, the malware sees a signed transaction and not a key. It can still show you a false address on the computer, which is why the screen of the device is the one you read.

The seed remains the real wallet, and the device is only a safer tool to use it. You still need the backup from chapter 14, and the seed is only as good as the randomness the device used to create it. In August 2023, the ["Milk Sad" disclosure](https://milksad.info/disclosure.html) showed that Libbitcoin Explorer, a software tool, had been creating seeds from only 32 bits of randomness instead of the 128 to 256 expected, and wallets made with it were emptied on 12 July 2023. No update could repair those seeds, and their owners had to create new ones and move their funds. The same kind of failure reached a hardware wallet in July 2026, when Coinkite [disclosed that COLDCARD firmware](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/) released since 2021 had created weak seeds (see the table).

## The maker you still have to trust

Moving the keys offline protects them from your computer and shifts your trust to the device's maker. The maker writes the firmware that creates your seed and signs your transactions, controls the supply chain, and usually runs the companion app, whose servers can see your addresses and your IP address. The Ledger leak (see the table) did not even come from the device, but from the customer list of the maker's shop.

Open source firmware can be read by outsiders, and a [reproducible build](https://github.com/BitBoxSwiss/bitbox02-firmware/blob/master/releases/README.md) lets anyone confirm that the published code is what you install. A signature check proves the firmware comes from the maker, not that it is sound, and air-gapped signing limits what a computer can send to the device. A secure element resists someone holding the device, but such chips often come with a confidentiality agreement, which is [why Ledger keeps part of its system closed](https://www.ledger.com/blog-ledger-is-95-opensource-why-not-100). Some devices accept dice rolls as a source of randomness, which lets you add your own to the chip's.

None of this removes the maker. Multi-signature across 2 makers (explained below) spreads that trust, whereas for a first device the maker's app and its automatic checks remain the safer path.

## Choose your device

The devices below differ in openness, price, comfort and isolation. "Air-gapped" means the device never needs a connection to a computer, because transactions travel by QR code or memory card. Ranges change quickly, and this table is valid as of September 2026.

| Device | Maker | Strengths | Trade-offs | Trust in the maker, and what you can check |
|---|---|---|---|---|
| **BitBox02** | BitBox (Shift Crypto), Switzerland | Open source, simple, a Bitcoin-only edition exists. [The BitBox02 Nova, announced in June 2025](https://bitcoinmagazine.com/news/bitbox-announces-bitbox02-nova-a-new-hardware-wallet-for-bitcoin), adds Bluetooth and iPhone support | Not air-gapped. It connects by USB-C, or by Bluetooth on the Nova | Open source firmware with reproducible builds, signature checked by the BitBoxApp. The secure chip is not trusted alone |
| **Trezor** | SatoshiLabs, Czech Republic | The open source pioneer, easy, widely supported | Older models connect by cable only, while [the Safe 7, released in late 2025](https://trezor.io/guides/trezor-devices/trezor-safe-7/trezor-safe-7-faqs), adds Bluetooth. Supports many other coins unless you choose Bitcoin-only firmware | Open source, reproducible firmware, checked by Trezor Suite. The Safe 7 adds an auditable secure element (TROPIC01) |
| **COLDCARD** (Mk and Q series) | Coinkite, Canada | Bitcoin-only, designed to sign without a cable, by memory card or, on the Q, by QR code. 2 secure chips from different makers. Many advanced options | More menus and options than a beginner needs. In July 2026 a firmware flaw that weakened seeds created since 2021 led to thefts from more than 5,200 addresses, [about 1,800 bitcoin in a preliminary count](https://www.trmlabs.com/resources/blog/the-largest-hardware-wallet-exploit-of-2026-inside-the-usd-116-million-coldcard-hack). [Updating does not repair an affected seed](https://coldcard.com/resources/security/coldcard-security-and-verification), which must be replaced | Source code published, with reproducible builds, but its [licence forbids selling the software](https://github.com/Coldcard/firmware/blob/master/COPYING-CC), so it is not open source in the strict sense. A numbered bag and a green light at start-up help check the device |
| **Blockstream Jade** | Blockstream | Affordable, open source, can work air-gapped with QR codes | Its PIN protection relies on a server (Blockstream's, or your own) | Open source firmware. No secure element, so the PIN server is part of the trust unless you host it |
| **Foundation Passport** | Foundation Devices, USA | Open source, comfortable to use, signs by QR code | Among the more expensive. The recent Passport Prime also uses Bluetooth and does more than Bitcoin (security keys, 2FA codes) | Open source firmware with reproducible builds, whose hash you can compare with the published one |
| **SeedSigner** | Community project | Build it yourself from standard parts, open source, stateless (it stores no seed at all) | You assemble it, and you load your seed at every use. Not a first device | No company. You verify the software signature yourself, builds are reproducible, randomness comes from dice or a photo |
| **Ledger** | Ledger, France | Popular, supports many coins, uses a secure chip | Firmware not fully open source. [A breach of its customer database in 2020](https://www.ledger.com/blog/update-efforts-to-protect-your-data-and-prosecute-the-scammers) exposed about 1 million email addresses, and the names, postal addresses and phone numbers of about 272,000 buyers | Part of the system on the secure chip is closed, so outsiders cannot fully verify what the firmware does |

You also need companion software, either the maker's own app or an independent open source wallet such as Sparrow Wallet, Electrum (computer), Nunchuk (computer and phone) or BlueWallet (phone, mainly with devices that sign by QR code). With an independent wallet, you do not depend on the maker's app staying available.

For larger amounts, the next level is **multi-signature**, a wallet that needs for example 2 devices out of 3 to sign. With devices from different makers, a flaw at 1 maker or the theft of 1 device is not enough to empty it. Back up the complete multisig configuration or output descriptor, including all cosigner xpubs, as well as enough signing keys (chapter 14). Those public keys cannot spend alone but reveal wallet activity. It is more work, so master 1 device first.

A reasonable setup for most people is an open source device with a Bitcoin-only firmware, bought new and updated before use, with Sparrow or the maker's app. The choice of maker stays yours.

## Step by step

The order is broadly the same for every device, but the verification in step 2 differs between makers, so keep the maker's official guide open.

1. **Buy directly from the maker or an official reseller.** Never second hand, never from a marketplace seller.
2. **Verify the device the way its maker describes.** Some makers ship in a sealed or numbered security bag. Ledger, on the other hand, [states that it uses no anti-tamper seals](https://donjon.ledger.com/threat-model/device-genuineness/), which it considers easy to copy, and relies on a cryptographic check in its app. The apps of BitBox, Trezor and Ledger check the device and install signed firmware. With SeedSigner, you download the software yourself and verify its signature. In every case, install the latest firmware before creating a seed. This is the step that replaces trust in the delivery chain with verification, although it still rests on the maker's own signature.
3. **Generate a new seed on the device.** The words must appear on the device screen, for the first time, in front of you. Never use words that came printed in the box.
4. **Back it up** on paper or metal, as explained in chapter 14. Set a PIN where the device supports one. Stateless devices such as SeedSigner work differently.
5. **Verify the receive address on the device screen, then send a tiny test amount.** Do this before moving savings, not afterwards.
6. **Check recovery with only the tiny test balance at stake.** Follow the maker's backup-check or wipe-and-restore procedure on the device, with compatible backup format and any passphrase recorded. Confirm the same addresses and test balance before adding savings. Keep the backup out of ordinary phone or computer wallets. A stateless device is reloaded rather than wiped.
7. **Move the rest,** in 1 or several transactions.
8. **Verify the receive address on the device screen, every time.** The computer screen can be manipulated, which is much harder to do with the screen of the device.

## Mistakes to avoid

- **Buying from marketplaces.** A device that passed through unknown hands may have been modified, and the small saving is not worth it.
- **Accepting a seed card that arrives filled in.** Treat it as a scam in every case, because the person who printed those words is waiting for your deposit.
- **Typing the seed into a computer "to update".** No real update, app or support agent needs your seed. For recovery, follow the maker's verified procedure and the device's instructions. Enter the words on the device itself when it allows it. Never enter them on a website, or because an update or a support agent asks for them.
- **Skipping the test restore.** A wrong or missing word is better discovered now, with a test amount, than in 5 years with your savings.
- **Using your home address for delivery without thinking.** Customer lists leak, as the Ledger case showed, and the list then tells strangers where a bitcoin holder lives. Consider a pickup point or a parcel locker.
- **Trusting emails that claim to be from the manufacturer.** After the Ledger leak, buyers received convincing phishing, with fake security alerts and fake updates, and in 2021 some even received [altered devices by post](https://www.bleepingcomputer.com/news/cryptocurrency/criminals-are-mailing-altered-ledger-devices-to-steal-cryptocurrency/), presented as replacements. Go to the official website yourself, never through a link.

## Go further

- **Independent checks of wallets and devices:** WalletScrutiny (walletscrutiny.com) tests whether the published code matches what you actually install.
- **Connecting a device to an independent wallet:** the Sparrow Wallet documentation (sparrowwallet.com/docs).
- **Step-by-step device guides:** Bitcoiner.Guide (bitcoiner.guide).
- **Next chapter:** running your own node.

## Sources

- [How to use a wallet backup](https://trezor.io/guides/backups-recovery/general-standards/how-to-use-a-wallet-backup), Trezor, checked 22 October 2026.
- [Multisig backup warning and descriptor export](https://github.com/sparrowwallet/sparrow/blob/master/src/main/java/com/sparrowwallet/sparrow/wallet/MultisigBackupDialog.java), Sparrow source code, checked 22 October 2026.
- [Update: efforts to protect your data and prosecute the scammers](https://www.ledger.com/blog/update-efforts-to-protect-your-data-and-prosecute-the-scammers), Ledger, 13 January 2021.
- [Threat model: device genuineness](https://donjon.ledger.com/threat-model/device-genuineness/), Ledger Donjon, page consulted in September 2026.
- [Criminals are mailing altered Ledger devices to steal cryptocurrency](https://www.bleepingcomputer.com/news/cryptocurrency/criminals-are-mailing-altered-ledger-devices-to-steal-cryptocurrency/), BleepingComputer, 16 June 2021.
- [Milk Sad: technical write-up of CVE-2023-39910](https://milksad.info/disclosure.html), Milk Sad research team, August 2023.
- [BitBox Announces BitBox02 Nova](https://bitcoinmagazine.com/news/bitbox-announces-bitbox02-nova-a-new-hardware-wallet-for-bitcoin), Bitcoin Magazine, 20 June 2025.
- [Reproducible builds of the BitBox02 firmware](https://github.com/BitBoxSwiss/bitbox02-firmware/blob/master/releases/README.md), BitBox on GitHub, consulted in September 2026.
- [Ledger is 95% open source, why not 100%?](https://www.ledger.com/blog-ledger-is-95-opensource-why-not-100), Ledger, consulted in September 2026.
- [Coldcard Security Advisory](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/), Coinkite, 30 July 2026, checked 29 October 2026.
- [COLDCARD security and verification](https://coldcard.com/resources/security/coldcard-security-and-verification) (dual secure elements, numbered bag, migration of affected seeds), Coinkite, checked 29 October 2026.
- [The Largest Hardware Wallet Exploit of 2026: Inside the USD 116 Million Coldcard Hack](https://www.trmlabs.com/resources/blog/the-largest-hardware-wallet-exploit-of-2026-inside-the-usd-116-million-coldcard-hack), TRM Labs, 5 August 2026, preliminary figures from Galaxy Research.
- [COLDCARD firmware licence, MIT with the Commons Clause](https://github.com/Coldcard/firmware/blob/master/COPYING-CC), Coinkite on GitHub, checked 29 October 2026.

## Your checklist

- [ ] Decide what amount is "savings" for you and no longer belongs on a phone (5 min)
- [ ] Choose a device from the table and order it from the maker, to a pickup point (1 hour)
- [ ] Check the device and its firmware the way the maker describes, create a new seed and a backup, then send a test amount (1 hour)
- [ ] With only a tiny test balance, follow the maker's hardware backup-check or restore procedure before adding savings (1 hour)
- [ ] Verify the address on the device screen at every receive (5 min)
