# Chapter 15: Lightning and euros in everyday life

## In brief

Bitcoin's base layer is built to be secure, not to sell coffee. Lightning is a payment network on top of it, in practice instant and very cheap, made for everyday amounts. This chapter shows how to pay and get paid over Lightning, where to spend sats, and the several routes between bitcoin and euros, each with its cost in fees, convenience and privacy. Nothing here is investment advice, and the tax rules of your country still apply.

## A ledger too slow for a coffee

The Bitcoin blockchain adds a new block about every 10 minutes, and each block has limited space. The limit is deliberate, because it keeps the ledger small enough for ordinary people to verify on their own computer (chapter 18). The price of that choice is that an on-chain payment usually takes minutes to hours to gain confirmations, with no absolute finality, and that its fee rises when many people want space at the same time, which is acceptable for moving savings and unreasonable for a coffee.

The second difficulty is the bridge. Salaries, rent and taxes are in euros, so using bitcoin at all requires a way in and a way out. The best-known one is a large exchange that holds your coins, your identity documents and the full history of what you do. There are other routes, described further down, and they differ a lot from each other in fees, convenience and privacy.

## Channels that touch the blockchain twice

Lightning rests on **payment channels**. 2 participants lock some bitcoin together in an on-chain transaction, and from then on they can move the balance between them as often as they like, in practice instantly, by exchanging signed updates that never touch the blockchain. Only the opening and the closing of the channel are written on-chain. Channels connect into a network, so you can pay someone you share no channel with, and the payment hops through intermediaries who are not able to keep it and who usually earn a fraction of a cent.

In practice you see 2 things:

- **An invoice**, a payment request shown as a QR code or long text. Common BOLT11 invoices start with "lnbc", and newer BOLT12 requests use a different format. It is usually for a fixed amount, used once, and it expires.
- **A Lightning address**, which looks like an email address (you@provider.com) and can be reused, which is convenient for tips and for getting paid. Most of them rely on a provider's web server. Phoenix's address relies on BOLT12, a newer standard that, for the moment, only some wallets can pay.

Modern wallets either manage the channels for you or avoid them by swapping through an outside service (chapter 13).

## Where to spend sats

- **In person.** [BTC Map](https://btcmap.org/) (btcmap.org) is the tool to find places, a free, community-run map of the cafés, shops, hotels and freelancers that accept bitcoin. A listing can be out of date, so look at its last verification date, ask before you order, and add the places you discover.
- **Tips and zaps.** On Nostr (chapter 7), you can send a few sats to the author of a post you liked, directly, with no platform taking a share. Many podcasts and independent writers publish a Lightning address too.
- **People.** Splitting a bill or repaying a friend is often the first real use.
- **Online.** Several companies sell gift cards, phone top-ups, eSIMs or travel against bitcoin, an indirect way to live on sats where merchants do not accept them yet. Each one in the table below (valid as of September 2026) is a shop, not a wallet, so pay for what you need and leave no balance there.

| Service | What you can buy | Lightning? | Identity check |
|---|---|---|---|
| **[Bitrefill](https://www.bitrefill.com/)** | Gift cards, phone refills, eSIMs | Yes | No account required for ordinary purchases. Verification raises its purchase limits. |
| **[CoinsBee](https://www.coinsbee.com/en/)** (Coinsbee GmbH) | Gift cards, payment cards, phone top-ups | Yes | [None up to 1,000 euros per order and 10,000 euros in total](https://www.coinsbee.com/en/kyc-aml/), verification beyond. |
| **[Cryptorefills](https://www.cryptorefills.com/)** (Big Dream Ventures B.V., Amsterdam) | Gift cards, top-ups, eSIMs, flights, stays | Yes | None, according to its site |
| **[CoinGate gift cards](https://coingate.com/gift-cards)** | Gift cards from about 6,000 brands | Yes | No sign-up needed, according to its site |
| **[Travala](https://www.travala.com/)** | Hotels, flights, activities | Yes | Traveller details for the booking, and the airline or hotel checks your ID as usual |

## Who holds the funds, who can block

For every route, the grid asks who holds the funds while the payment is in progress, and who can stop it.

With a custodial app, the company holds the bitcoin until you withdraw, and it can freeze the balance or refuse a payment. With a self-custodial Lightning wallet the keys are yours, but payments pass through a Lightning service provider (ACINQ for Phoenix, Blocktank for Bitkit) or, in a different design, a small group of operators (Spark). These services can refuse transfers. Lightning wallets need correct channel handling and backups. Spark also relies on [a threshold of honest operators during transfers](https://docs.spark.money/learn/trust-model). An exit to the blockchain has its own conditions, fees and delays, so holding the keys does not protect you against every failure.

A broker under KYC holds your euros during the purchase, and it can refuse an order, ask where the money comes from or close your account, as can the bank sending the transfer. Peer-to-peer platforms try to remove the holder. Bisq 1 locks the coins in a [2-of-2 multi-signature address](https://bisq.wiki/Security_deposit) shared by the 2 traders, and Hodl Hodl in [a 2-of-3 address](https://hodlhodl.com/blog/en/escrow-explained) where the platform has 1 key, so no single party can move them. RoboSats uses a [Lightning payment held](https://learn.robosats.org/docs/escrow/) towards the coordinator hosting the order. Bisq Easy, the simpler trade mode of Bisq 2, has [no escrow and no security deposit](https://bisq.wiki/Bisq_Easy). The buyer relies on the seller's reputation, and each trade is capped at the equivalent of 600 dollars. The trust that remains goes to the other trader and to whoever settles a dispute.

## Choose your bridge to euros

No route is best on every count, because each one trades simplicity against fees and privacy. **KYC** ("know your customer") means the service verifies your identity with an ID document, which regulated companies in Europe now have to do, and chapter 16 explains what that implies for your privacy. This market moves fast. The Swiss broker Pocket Bitcoin, for example, [ended its lighter verification in December 2025](https://pocketbitcoin.com/blog/posts/full-verification-coming-to-pocket). On the peer-to-peer side, [Hodl Hodl](https://hodlhodl.com/), [Bisq](https://bisq.network/) and [RoboSats](https://learn.robosats.org/) let you trade with another person without handing your coins to a company, under the designs described in the previous section. The table is valid as of September 2026, and you should check in each case that the service accepts residents of your country.

| Route | Examples | Identity check (KYC) | Who holds the coins | Who can block it | Honest trade-off |
|---|---|---|---|---|---|
| **Earn sats** | Be paid or tipped in bitcoin for work, sales or content | None | You | Only a Lightning provider on either side, by declining to relay the payment | No intermediary at all. You need someone willing to pay this way, and income remains taxable. |
| **Peer-to-peer exchange** | Hodl Hodl (web), Bisq (desktop), RoboSats (Lightning, over Tor) | Generally none by the platform. Hodl Hodl may ask in a dispute. | You. Coins are locked in escrow only during the trade, where the platform offers one. | The other trader, by not paying, and the banks on both sides. A mediator or arbitrator settles disputes. | You trade with a person by bank transfer. More private, usually more expensive, slower, more to learn. |
| **European broker, recurring purchases** | Relai, Pocket Bitcoin (both Swiss) | Yes | You. They deliver to your own wallet. | The broker, which can refuse an order or close your account, and your bank, which can block the transfer | Very simple, automatic. A fee on each purchase, and the company knows who you are and what you bought. |
| **Euro account plus bitcoin wallet** | Bringin (euro IBAN and optional Visa card next to a self-custodial wallet), Strike (SEPA deposits, fully custodial) | Yes | Bringin: you, for the bitcoin. Strike: the company, for everything, until you withdraw to your own wallet. | Bringin for the euro account and the card, which it can block like any regulated payment company, but not the bitcoin, which sits in a self-custodial wallet. Strike is custodial, so the company holds the keys to both your euros and your bitcoin and has every right over them: it can freeze the balance, refuse a payment or close the account. | Convenient for moving between sats and euros. A single company sees both sides, each conversion carries a fee, and the euro side is a regulated account like any other. |
| **Bitcoin ATM** | Machines listed on coinatmradar.com | Usually yes in the EU, depending on operator and amount | You | The operator, which sets limits and can refuse a transaction | Cash in, coins out in minutes. Fees are typically the highest of all routes. Scammers often tell their victims to deposit cash into a Bitcoin ATM, and [older people lose the most](https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2024/08/bitcoin-atms-payment-portal-scammers). No bank, police force or support desk ever asks you to do this. |

A reasonable setup for most people who decide to exchange euros is a regulated route they find clear, used only to deliver coins to their own wallet, and a peer-to-peer route learned with small amounts, so that they do not depend on a single door. Whatever the route, selling or spending bitcoin can create a tax obligation, so keep records and check the rules of your country.

## Step by step

The steps are the same in most Lightning wallets, including the one you installed in chapter 13.

1. **Pay an invoice.** At a merchant or a meetup, tap Send and scan the QR code. Check the amount and the fee shown, then confirm. The merchant usually sees the payment within 1 or 2 seconds.
2. **Receive with an invoice.** Tap Receive, enter an amount if you wish, and show the QR code. Remember that it expires. In a wallet that opens its own channels, such as Bitkit or Phoenix, the first payment has to exceed the channel fee (chapter 13).
3. **Receive with a Lightning address.** If your wallet offers one, find it in the settings or on the receive screen, and test it from a second wallet before you publish it. Phoenix's address uses BOLT12, which many wallets cannot pay yet. An address from a custodial or Spark-based wallet works with almost every sender, with the trade-offs described in chapter 13.
4. **Withdraw from a broker or app to your OWN wallet.** Choose "withdraw" or "send", paste an address or an invoice generated by your wallet, and start with a small test. Seeing the coins arrive in a wallet whose keys you hold is the step that replaces trust in a displayed balance with verification. For larger amounts, withdraw on-chain to your savings wallet (chapters 14 and 17).
5. **Keep only spending money on the phone.** Think of the Lightning wallet as the wallet in your pocket. When it holds more than you would carry in cash, move the surplus on-chain.
6. **Keep records.** Export or note your purchases and sales with dates and amounts, because you will need them for the tax return.

## Mistakes to avoid

- **Keeping savings in a Lightning phone wallet.** It lives on a device you can lose or break, connected to the internet all day, so it suits spending money.
- **Confusing an invoice with an on-chain address.** A BOLT11 invoice starts with "lnbc" and expires, and BOLT12 uses other formats. An on-chain address starts with "bc1", "1" or "3" and does not. When you withdraw from a service, select the matching network.
- **Making large payments over Lightning.** Channels have limited capacity, and large payments fail more often. Lightning is for everyday amounts, and on-chain handles the rest.
- **Leaving coins with the broker.** A purchase is finished when the coins are in your wallet, not when the app shows a balance (chapter 13).
- **Ignoring the total cost.** Compare the final amount of sats you receive, not the advertised fee, because the exchange rate often hides a margin.
- **Forgetting the tax side.** Paying with bitcoin can count as selling it, and the rules differ by country.

## Go further

- **Find places to spend:** BTC Map (btcmap.org).
- **Tutorials for the wallets and exchanges above:** Plan B Academy (planb.academy).
- **Understand Lightning in depth:** "Mastering the Lightning Network", free to read online (github.com/lnbook/lnbook).
- **Next chapter:** privacy in Bitcoin.

## Sources

- [Spark trust model](https://docs.spark.money/learn/trust-model), Spark documentation, checked 22 October 2026.
- [Important Update: Full Verification Coming to Pocket](https://pocketbitcoin.com/blog/posts/full-verification-coming-to-pocket), Pocket Bitcoin, 16 October 2025.
- [Security deposit](https://bisq.wiki/Security_deposit), Bisq Wiki, consulted in September 2026.
- [What is multisig escrow and how it works](https://hodlhodl.com/blog/en/escrow-explained), Hodl Hodl, consulted in September 2026.
- [Trade escrow](https://learn.robosats.org/docs/escrow/), Learn RoboSats, consulted in September 2026.
- [Bisq Easy](https://bisq.wiki/Bisq_Easy) (no security deposit, seller reputation, trades from 6 to 600 dollars), Bisq Wiki, checked 29 October 2026.
- [Bitcoin ATMs: A payment portal for scammers](https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2024/08/bitcoin-atms-payment-portal-scammers), US Federal Trade Commission, September 2024.
- [Bringin: wallet, euro account and fees](https://bringin.app/), Bringin, consulted in September 2026.
- [KYC and AML: purchase limits](https://www.coinsbee.com/en/kyc-aml/), CoinsBee, consulted in September 2026.

## Your checklist

- [ ] Pay a Lightning invoice, at a merchant or a meetup (5 min)
- [ ] Get a Lightning address and test it from a second wallet (5 min)
- [ ] Find 3 places near you on btcmap.org (5 min)
- [ ] Withdraw any balance from a broker or exchange to your own wallet (1 hour)
- [ ] Read how a peer-to-peer exchange works, before you need it (1 hour)
