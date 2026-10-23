# Chapter 18: Running your own node

## In brief

Without your own node, your wallet asks someone else's server about your money. A node is your own copy of Bitcoin's rules and ledger, which checks every block and every transaction itself, so you no longer depend on somebody else's answer. It protects your privacy, and it strengthens the network. It needs a small always-on computer, a 2 TB SSD, a weekend of your time and then a few days of synchronisation during which the machine works alone. It is not a miner, and it earns nothing.

## Your wallet asks a stranger about your money

When you open a wallet app, it needs to know your balance. It does not have the ledger, so it asks a server what happened on your addresses. That server belongs to the wallet's maker, or to an unknown volunteer.

2 things follow. First, the server can learn which addresses are yours, all of them, together with your IP address. The separate wallets and fresh addresses from chapter 16 are grouped again, in somebody's logs. Second, you have to believe the answer, because if the server is wrong, offline or dishonest, your wallet shows you what it was told.

For small amounts this is a reasonable compromise, and most people start this way. It remains an odd arrangement for a system designed so that nobody has to be trusted. With your own node, the question stays inside your home network.

## A computer that checks every rule itself

A **node** is a computer running Bitcoin software, most often Bitcoin Core (other implementations exist, such as Bitcoin Knots). It downloads the whole ledger since the first block in 2009 and verifies every transaction against the rules, which means no coin spent twice, no coin created from nothing and never more than 21 million. It repeats this for every new block, about every 10 minutes, which is the meaning of "don't trust, verify".

Your node accepts only what follows the rules it runs. When thousands of people do the same, a company, a miner or a government that wanted different rules would first have to convince them to install different software.

A node is not a miner. It uses little electricity, earns nothing, and need not hold private keys. In the verification-only setup here, they stay in a separate wallet or signing device. Bitcoin Core can also run a wallet; if you use that feature, its wallet backups matter too.

It needs a small computer that stays on, a normal home connection and a 2 TB SSD. As of September 2026 the ledger weighs [about 770 GB](https://www.blockchain.com/explorer/charts/blocks-size) and [grows by 5 to 10 GB per month](https://bitcoincore.org/en/download/), and the index of an Electrum server adds from a few dozen to more than 100 GB, which would almost fill a 1 TB disk.

## What a node still asks you to trust

The question that runs through this book, who the trusted third party is and whether you can check, ends here. For the state of your money, a node brings the answer down to nobody. It believes neither a wallet maker's server nor the nodes it connects to, because every block they send is checked against the rules and rejected if invalid, whoever sent it. You gain authenticity (the balance you see is the real one) and control over the rules you accept.

2 things remain. The first is the software, because a node enforces the rules of the program you installed, and a falsified copy would enforce somebody else's. Bitcoin Core answers with reproducible builds, in which several developers compile each release independently, obtain identical files and [publish their signatures](https://github.com/bitcoin-core/guix.sigs). By checking a few of them, you stop depending on the honesty of a single person. A node platform adds its maker to the list, for the system, the app store and the updates. The second is your own hardware and operating system, which you cannot fully audit.

The price is a disk, a weekend and some maintenance, and for small amounts a public server stays a sensible choice.

## Choose your route

All routes run the same Bitcoin software underneath, and they differ in how much is done for you.

On an everyday computer, a **pruned node** is the lighter option. It verifies everything but keeps only the most recent blocks, so storage can be around 10 GB at a low pruning target, plus room for growth and other files. It still downloads and validates the full history; pruning does not remove that initial bandwidth requirement. However, most wallet server software needs the full ledger, which is why a dedicated node keeps it.

| Route | What it is | Strengths | Trade-offs | Who you still trust |
|---|---|---|---|---|
| **Bitcoin Core on your everyday computer** | The reference software, open source, from bitcoincore.org | Free, the simplest start, includes its own wallet, can run in pruned mode on a small disk | Not always on. Without pruned mode it fills most of a 1 TB disk | The Bitcoin Core developers, unless you check the signatures of several builders, and your everyday computer |
| **Umbrel** | A home server system with an app store. Runs on your own hardware, or on a device the company sells | The most polished interface, one-click apps | Made by a single company. Free for personal use, but its licence is not open source (no commercial reuse) | Umbrel as well, for the system, its app store and its updates. The code can be read |
| **Start9 (StartOS)** | An open source server system. Runs on your own hardware, or on a server the company sells | Strong focus on privacy and self-hosting, good documentation | Made by a single company. A little more to learn at the start | Start9 as well, for the system, its marketplace and its updates. The image comes with a checksum and a signature |
| **RaspiBlitz** | An open source community project for the Raspberry Pi | No company involved, strong Lightning tools | More technical, some work on the command line | Its volunteer maintainers. Build scripts are public, and the image carries the lead developer's PGP signature |
| **MyNode** | A node system for small computers, with a free community edition and a paid premium edition | Simple web interface, many Bitcoin apps | Made by a small company, some features reserved for the paid edition | MyNode as well, for the system, the apps it packages and its updates |
| **The manual route** | Debian or Ubuntu Linux, then Bitcoin Core, then an Electrum server (electrs or Fulcrum), by following a guide | You understand every part. Nothing hidden, fully open source | Slow, command line only. For learners who enjoy it | Only the software whose signatures you check yourself, the authors of your guide, and your hardware |

Umbrel and Start9 are also general home servers, which connects with chapter 10, since the same box can host your files and your passwords.

A reasonable setup for most people is to try Bitcoin Core on your computer, in pruned mode, to see what a node is, then to move to a dedicated small computer with the platform whose trade-offs suit you.

## A word on Lightning nodes

The same platforms let you install a Lightning node (LND or Core Lightning) in 1 click. Treat it as a later project. A Lightning node holds real funds in channels, on a machine that is always online. Channels need their own backups, regular attention and an understanding of what happens if the disk fails, and restoring an old backup the wrong way can even cost you the funds in a channel. A Bitcoin node alone can break without any loss, because you only have to synchronise again, which is not true of a Lightning node. Learn with small amounts, and only after the rest of this chapter has become routine.

## Step by step

The example uses a platform with an app store, such as Umbrel or StartOS. RaspiBlitz and MyNode follow the same order. Your own work fits in a weekend, and the machine then needs a few days on its own.

1. **Choose the hardware.** A used mini PC or a recent Raspberry Pi with 8 GB of memory, a 2 TB SSD from a known brand, and a network cable to your router.
2. **Install the platform** by following its official guide, from an image downloaded on its official website, and set a strong, unique password (chapter 2). Where the project publishes a checksum or a signature for that image, as [Start9](https://docs.start9.com/start-os/0.4.0.x/installing-startos.html) and [RaspiBlitz](https://docs.raspiblitz.org/docs/faq) do, check it before you write the image to the disk. This is the step that replaces trust in the download with verification.
3. **Install the Bitcoin app and let it synchronise.** It takes a few days, and up to a week on slow hardware such as a Raspberry Pi. Leave it running when practical. If you need to stop, shut it down cleanly from the interface and let synchronisation resume later; do not cut the power.
4. **Install an Electrum server app** (electrs or Fulcrum). It builds an index so that wallets can ask your node questions, which takes several more hours, sometimes a full day.
5. **Connect your wallet.** In Sparrow, BlueWallet or Nunchuk, open the server or network settings and enter the address of your own Electrum server instead of the public one. From this step on, your wallet shows what your own node verified, and no longer what a third party told it. Zeus works differently, because it connects to a Lightning node, which is for later.
6. **Reach it from outside your home** over Tor or a private VPN (see chapter 10). The platforms provide a Tor address for this.
7. **Keep it updated,** and keep your seed backups separate from the node. A verification-only node needs no seed and should never see one. If you enable Bitcoin Core's wallet or install Lightning, protect and back up those wallets separately.

## Mistakes to avoid

- **Using a cheap SD card or USB stick, or a disk that is too small.** A node writes constantly, and SD cards and USB sticks tend to fail within months and can corrupt the data. Use a real SSD of 2 TB, because 1 TB leaves almost no margin as of September 2026, and [the RaspiBolt guide now asks for 2 TB](https://raspibolt.org/) as well.
- **No power protection.** A sudden power cut can damage the database and cost you days of synchronisation. Always shut down from the interface, and consider a small battery backup (UPS).
- **Thinking the node holds your coins.** A verification-only node holds no spending keys. Bitcoin Core's optional wallet and a Lightning app do hold keys, and require their own backups. With keys kept separately, a failed verification node can be rebuilt without losing funds.
- **Exposing it to the internet.** Do not open ports on your router to reach the dashboard. Use Tor or a VPN.
- **Giving up during the first synchronisation.** It can look stuck for days while it verifies more than 15 years of transactions, which it only has to do once.
- **Downloading software from the wrong place, or without verifying it.** Get Bitcoin Core only from bitcoincore.org, and each platform from its official website. The [download page of Bitcoin Core](https://bitcoincore.org/en/download/) explains how to check the file against the published list of checksums, and how to check that this list carries the PGP signatures of several developers. On a platform, you rely on its maker to do this for the apps it installs, whereas on your own computer and on the manual route it is your job.

## Go further

- **The basics:** the download page of Bitcoin Core (bitcoincore.org), with the current requirements, pruned mode and the procedure to verify your download.
- **The manual route:** the RaspiBolt guide (raspibolt.org, version 4, updated in August 2026) and MiniBolt, a similar guide for ordinary PCs (minibolt.minibolt.info). Both are maintained as of September 2026.
- **Connecting a wallet to your node:** the Sparrow Wallet documentation (sparrowwallet.com/docs).
- **Next:** your checklist.

## Sources

- [Graceful shutdown, stop RPC](https://bitcoincore.org/en/doc/30.0.0/rpc/control/stop/), Bitcoin Core documentation, checked 22 October 2026.
- [Blockchain size chart](https://www.blockchain.com/explorer/charts/blocks-size), Blockchain.com, consulted on 20 September 2026 (about 770 GB).
- [Download Bitcoin Core, with requirements and verification of the download](https://bitcoincore.org/en/download/), Bitcoin Core project, consulted in September 2026.
- [Signatures of the Bitcoin Core builders (guix.sigs)](https://github.com/bitcoin-core/guix.sigs), Bitcoin Core project on GitHub, updated at every release.
- [Installing StartOS, with verification of the download](https://docs.start9.com/start-os/0.4.0.x/installing-startos.html), Start9 documentation, consulted in September 2026.
- [RaspiBlitz FAQ, how to verify the SD card image](https://docs.raspiblitz.org/docs/faq), RaspiBlitz project, consulted in September 2026.
- [RaspiBolt, version 4](https://raspibolt.org/), RaspiBolt community guide, updated in August 2026.
- [MiniBolt](https://minibolt.minibolt.info/), MiniBolt community guide, consulted in September 2026.

## Your checklist

- [ ] Look in your wallet's network settings and see which server it uses today (5 min)
- [ ] Verify the Bitcoin Core download, install it in pruned mode so it does not fill your disk, and watch it synchronise (1 hour)
- [ ] Choose a platform and the hardware for a dedicated node, with a 2 TB SSD (1 hour)
- [ ] Build the node, start the synchronisation (a few days, unattended) and add an Electrum server (weekend)
- [ ] Point your wallet to your own node and remove the public server (5 min)
