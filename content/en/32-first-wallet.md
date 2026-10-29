# Chapter 13: Your first wallet and your first sats

## In brief

Bitcoin left on an exchange is a promise from a company, whereas bitcoin in a wallet where you hold the keys is under your own control. A wallet is a free app that takes about 10 minutes to set up, and you can learn with an amount close to the price of a lunch. Install one, write down the recovery words, receive a first payment, send part of it back, then try a second wallet from another team to compare.

## An exchange balance is an IOU

When you buy bitcoin on an exchange and leave it there, what you hold is a line in the company's database saying that it owes you some. As long as the company stays honest, solvent, secure and allowed to serve you, the difference with real bitcoin is invisible.

Mt. Gox, which was the largest bitcoin exchange in the world, filed for bankruptcy in February 2014 and announced that [about 850,000 bitcoin were missing](https://www.wired.com/2014/03/bitcoin-exchange/). Its trustee made the first repayments to creditors in July 2024, and in October 2026, more than 12 years after the collapse, he [postponed the end of the repayments once more](https://www.mtgox.com/img/pdf/20261016_b3a13e0f-55f6-4653-913b-be80762390e8_announcement_en.pdf).

FTX, one of the largest exchanges of its time, filed for bankruptcy in November 2022, a few days after withdrawals were suspended. Its founder was convicted of fraud in November 2023 and [sentenced to 25 years in prison](https://www.justice.gov/archives/opa/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes) in March 2024. Between events of that size there are more ordinary ones, such as frozen accounts, suspended withdrawals and hacked platforms, which Bitcoin users sum up with the saying "Not your keys, not your coins."

## A wallet holds keys, not coins

Every bitcoin exists only as an entry in the blockchain, the public ledger that thousands of computers keep in sync. What your wallet holds is **keys**, secret numbers that prove to the network that you are allowed to move a given entry. Spending means signing a message with your key, so whoever holds the key controls the coins, without a name, an account or a permission being involved.

The app is therefore a window and a pen. It shows you what your keys control and it signs when you decide to pay. Many wallets back up their keys as 12 or 24 words. Other formats exist, and recovery requires compatible software (chapter 14). Lightning may also need wallet-specific recovery data.

You do not need a whole bitcoin either. 1 bitcoin divides into 100 million units called **satoshis**, or **sats**, and a wallet works the same way with 20,000 sats as with 2 bitcoin, which allows you to learn with small amounts.

## 2 choices you will meet

**On-chain or Lightning.** On-chain transactions are written directly into the blockchain. They take from minutes to hours and cost a fee that depends on demand, which suits larger amounts and savings. Lightning is a payment network built on top of Bitcoin, in practice instant and very cheap, which suits small everyday amounts (chapter 15).

**Custodial or self-custodial.** A custodial wallet works like a small exchange, because a company holds the keys and shows you a balance. A self-custodial wallet keeps the keys on your phone.

A custodial wallet is the easiest possible start, with nothing to back up and nothing to understand, and it is acceptable for an amount you could lose without pain, like the coins in your pocket. In the EU the option is shrinking, however, because custodial providers now need a licence and must identify their users (chapter 16). Self-custody asks a little more of you, mainly a serious backup. In return no company can freeze or lose your balance on your behalf, although exchanges and brokers can still refuse to serve you.

## Holding the keys is not the whole story

With a custodial wallet the trusted third party is obvious, because the company holds the keys and can freeze or lose your balance. Holding your own keys removes that party and leaves 3 quieter ones in place.

The first is the server your wallet asks. A phone wallet does not check the blockchain itself, it queries a server, usually the wallet team's, which learns your addresses and your IP address and could show a wrong balance, although it cannot spend your coins. The second is the delivery channel, because Apple's or Google's store and the developer's signing key decide which code runs on your phone. The third, on Lightning, is the service provider. Phoenix opens its channels only with ACINQ's node, which usually sees where your payments go and could decline to relay them, while wallets built on Spark depend on [a small group of operators](https://docs.spark.money/spark/trust-model). Both designs keep an exit to the blockchain, at a cost.

Each of these can be partly checked. Open source code can be read, [WalletScrutiny](https://walletscrutiny.com/methodology/) tests whether the app in the store can be rebuilt from that code (a reproducible build), and several wallets let you connect to your own node (chapter 18).

## Choose your wallet

All the wallets below are free, and it helps to try 2 of them from different teams, so that a problem with one app or one service never leaves you unable to pay.

The first row, [Bitkit](https://bitkit.to/), is this book's editorial choice for a first wallet. The app, published by Synonym for iPhone and Android, shows 2 balances on one screen, savings held on-chain and spending held on Lightning, behind a single list of 12 words. You can receive over Lightning from the first minute, because Synonym's service provider, Blocktank, opens a channel when the first payment arrives and deducts its fee, [about 1,800 sats in a case documented in mid-September 2026](https://github.com/synonymdev/bitkit-android/issues/1265). Bitkit depends on Blocktank for that channel, and its Lightning connections are [not offered to residents of the United States or Canada](https://help.bitkit.to/hc/help-center/articles/1702656162-how-do-i-manage-my-spending-balance).

The last 2 rows are built on Ark, a way to make fast, cheap off-chain bitcoin payments in which many users share the same on-chain transactions through an Ark server. You keep pre-signed transactions that allow you to exit to the blockchain by yourself if that server disappears. Ark is young, since it opened on Bitcoin's main network in [October 2025 with Arkade](https://arklabs.xyz/insights/press-start-arkade-goes-live) and in [June 2026 with Second's Bark](https://second.tech/blog/introducing-noah-and-arke/), and on Second's server a balance [expires after 28 days unless the wallet refreshes it](https://second.tech/docs/learn/intro). Open an Ark wallet regularly so that it can refresh your balance. After expiry the server can sweep the funds, and getting them back depends on its cooperation. The table is valid as of September 2026, so check each project's website before you install.

| Wallet | Who holds the keys | Who it still depends on | Networks | Open source | Honest trade-off |
|---|---|---|---|---|---|
| **[Bitkit](https://bitkit.to/)** | You | Synonym's provider, Blocktank, for Lightning channels by default. Synonym's Electrum server for blockchain data, replaceable by your own. | On-chain and Lightning, as 2 balances in one app | Yes | A Lightning node on your phone next to an on-chain savings balance, behind 1 backup. The first Lightning payment pays for the channel (about 1,800 sats in mid-September 2026, depending on mining fees), total Lightning capacity is capped near 999 dollars, and Lightning is not offered to residents of the United States or Canada. |
| **Phoenix** | You | ACINQ's node for every Lightning payment. Electrum servers for blockchain data, replaceable by your own. | Lightning (on-chain in and out through swaps) | Yes | A real Lightning node on your phone, simple to use. Depends on a single company (ACINQ) for its channels. Opening the first channel [costs 1,000 sats plus 1% plus the mining fee](https://phoenix.acinq.co/faq), so a very small first payment is refused. |
| **Breez** (Glow, the successor to Misty Breez) | You | The Spark operators, who co-sign each transfer, and Breez's software. | Lightning, through the Spark network | Yes | Misty Breez [lost its Lightning and on-chain payments](https://breez.technology/misty/) in August 2026. Breez now points to Glow, launched the same month. No channels to manage, but very new, and Spark relies on a small group of operators. |
| **BlueWallet** | You | BlueWallet's Electrum servers for balances and broadcasting, replaceable by your own in the settings. | On-chain | Yes | Clear and good for learning on-chain. Its hosted Lightning service closed in 2023. |
| **Blockstream app** (formerly Green) | You | Blockstream's servers by default, or your own Electrum server. The Liquid federation, and a swap service for Lightning. | On-chain and Liquid. Lightning through swaps, or in beta on the desktop app | Yes | Many options, works with hardware wallets. More menus for a beginner. Its Lightning payments went through swaps to Liquid, run by Boltz, which [suspended its service on 3 August 2026](https://www.tftc.io/boltz-bitcoin-swaps-suspended-ai-attacks). The desktop app [paused new swaps and added Lightning in beta](https://blog.blockstream.com/blockstream-app-desktop-3-5-0/) on 24 August 2026, so check what works in your version. |
| **Zeus** | You | Zeus's own service provider (Olympus) for channels, by default. Other Bitcoin nodes for blockchain data, or your own. | Lightning and on-chain | Yes | A real Lightning node in your phone, or a remote control for your own node (chapter 18). Powerful, more to learn. In August 2026 an attack on Zeus's servers [closed many users' channels](https://zeusln.com/blog/post-mortem-security-update-august-5th-2026/), without loss of customer funds. |
| **Wallet of Satoshi** | You in the EU, where its custodial mode [has been unavailable since January 2026](https://www.therage.co/wallet-of-satoshi-eu-mica/). The company elsewhere. | The company for a custodial balance. In self-custodial mode, the Spark operators and the company's servers. | Lightning | No | The easiest of all. Its self-custodial mode runs on Spark, a recent system that relies on a small group of operators. Pocket money only. |
| **Bringin** | You | Bringin for the optional euro account, which it can block like any payment company. The bitcoin wallet is self-custodial, so Bringin does not hold those funds. | Lightning and on-chain | Not stated on its website | Wallet linked to an optional euro account, which requires identity verification (chapter 15). |
| **[Arkade wallet](https://arkade.money/)** | You | The Arkade server run by Ark Labs, which co-signs each Ark payment. The exit to the blockchain works without it. | Ark and on-chain | Yes | A web app installed from the browser, without an app store. Public beta since October 2025, and Ark Labs wrote at launch that it is not ready for savings. |
| **[Noah](https://beta.noahwallet.io/)** | You | The Ark server run by Second, which co-signs payments and connects the wallet to Lightning. The exit to the blockchain works without it. | Ark, Lightning and on-chain | Yes | From the team behind the Blixt wallet. Beta for Android, and for iPhone through TestFlight. Its developers ask you to deposit only what you can afford to lose. |

A reasonable setup for most people is a self-custodial Lightning wallet for small amounts and an on-chain wallet to understand the base layer, either in one app such as Bitkit or in 2 separate apps, with BlueWallet or the Blockstream app for the on-chain side. Wallets that run their own channels (Bitkit, Phoenix, Zeus) cost more on the first day and depend on fewer outside services, while those built on swaps or on Spark are the other way round. Try 2 and keep the one you find clear.

## Step by step

The example uses Bitkit. The logic is the same for the others.

1. **Install it** from the official store. Before you tap, check the developer name (Synonym Software for Bitkit) and follow the link from the project's official website, bitkit.to, rather than a store search. This check, completed by a look at the app's page on walletscrutiny.com, is the step that replaces trust with verification, as far as a phone allows.
2. **Create a new wallet.** The app asks for no email, no name and no account, which is normal.
3. **Write down the recovery words before receiving anything.** Find the 12 words in the backup settings, copy them by hand on paper, and read chapter 14 before adding more than pocket money.
4. **Receive a first payment larger than the channel fee.** Tap Receive, choose to receive on the spending balance and show the QR code, keeping the app open until the payment appears. Blocktank opens your channel at that moment and takes its fee out of the amount, 1,835 sats in [a case reported on 15 September 2026](https://github.com/synonymdev/bitkit-android/issues/1265), more when mining fees rise. The same report, still open on 20 September, shows that the suggested minimum of 2,000 sats can leave a balance too small to spend. Ask for a realistic amount, for example 20,000 sats, and read the fee the app displays before you accept. To test with a few hundred sats only, use a wallet without channels (Wallet of Satoshi or Glow) and accept its trade-off.
5. **Send a small amount back.** Scan the other person's QR code, check the amount, confirm. It usually arrives in 1 or 2 seconds.
6. **Check the fee** in the payment details, so that you know what a normal fee looks like.
7. **Try a second wallet**, send sats from one to the other, and compare.

## Mistakes to avoid

- **Leaving savings on an exchange.** An exchange is useful for the time of a purchase. Afterwards, withdraw to a wallet you control.
- **Taking a screenshot of your recovery words.** Photos are often synced to the cloud and can be read by other apps. Use paper and a pen (chapter 14).
- **Installing a fake wallet.** App stores contain copies built to steal. Check the developer name and start from the project's official site.
- **Sending to the wrong network.** A Lightning invoice, an on-chain address and a Liquid address are 3 different things. A good wallet refuses the wrong one, and if something looks odd, stop and ask.
- **Starting with a large amount.** Beginner mistakes happen in the first weeks, so make them with a small sum.
- **Trusting anyone who offers to "help" with your wallet online.** No wallet team, exchange or authority needs your recovery words.

## Go further

- **Step-by-step wallet tutorials:** Plan B Academy (planb.academy).
- **Check whether a wallet is really open source:** WalletScrutiny (walletscrutiny.com).
- **Plain guides for beginners:** Bitcoiner.Guide (bitcoiner.guide).
- **Next chapter:** backing up your seed phrase.

## Sources

- [The Inside Story of Mt. Gox, Bitcoin's $460 Million Disaster](https://www.wired.com/2014/03/bitcoin-exchange/), Wired, 3 March 2014.
- [Notice Concerning Change of Repayment Deadlines](https://www.mtgox.com/img/pdf/20261016_b3a13e0f-55f6-4653-913b-be80762390e8_announcement_en.pdf), MtGox Co., Ltd. Rehabilitation Trustee, 16 October 2026, checked 29 October 2026.
- [Samuel Bankman-Fried Sentenced to 25 Years for His Orchestration of Multiple Fraudulent Schemes](https://www.justice.gov/archives/opa/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes), U.S. Department of Justice, 28 March 2024.
- [Methodology](https://walletscrutiny.com/methodology/), WalletScrutiny, consulted in September 2026.
- [Spark trust model](https://docs.spark.money/spark/trust-model), Spark documentation, consulted in September 2026.
- [Phoenix FAQ: fees, restoring a wallet](https://phoenix.acinq.co/faq), ACINQ, consulted in September 2026.
- [How do I manage my spending balance?](https://help.bitkit.to/hc/help-center/articles/1702656162-how-do-i-manage-my-spending-balance) (Blocktank, the 999 dollar cap, United States and Canada), Bitkit Help Center, Synonym, consulted in September 2026.
- [CJIT at suggested minimum yields unspendable channel](https://github.com/synonymdev/bitkit-android/issues/1265) (Blocktank fee of 1,835 sats on a first payment), Bitkit issue tracker on GitHub, 15 September 2026.
- [Press Start: Arkade Goes Live](https://arklabs.xyz/insights/press-start-arkade-goes-live), Ark Labs, 20 October 2025.
- [Introducing Noah and Arké: Two new Bark-based wallets](https://second.tech/blog/introducing-noah-and-arke/), Second, 10 June 2026.
- [Intro to the Ark protocol](https://second.tech/docs/learn/intro) (expiry after 28 days, sweep by the server), Second documentation, checked 29 October 2026.
- [Boltz Suspends Bitcoin Swaps Indefinitely as AI Attacks Outpace Patching](https://www.tftc.io/boltz-bitcoin-swaps-suspended-ai-attacks), TFTC, 4 August 2026, checked 29 October 2026.
- [The Blockstream App 3.5.0 for Desktop: Lightning in Beta and Air-Gapped Jade Signing](https://blog.blockstream.com/blockstream-app-desktop-3-5-0/), Blockstream, 24 August 2026, checked 29 October 2026.

## Your checklist

- [ ] Install a self-custodial wallet from its official source, after checking the developer name and its page on walletscrutiny.com (5 min)
- [ ] Write the recovery words on paper before receiving anything (5 min)
- [ ] Receive a first payment larger than the setup fee and send some back (5 min)
- [ ] Install a second wallet from another team and compare (1 hour)
- [ ] Move anything you left on an exchange to a wallet you control (1 hour)
