# Chapter 12: Where to keep the fruit of your work

## In brief

Every place where you can keep savings is a trade-off between convenience, protection against inflation, privacy and control. Cash, banks, shares, gold, Bitcoin and Monero fail and succeed in different ways. This chapter does not tell you what to buy. It gives you 5 questions to ask of anything you own, and a way to stop depending on a single institution. Nothing here is investment advice, and the tax rules of your country apply to everything below.

## When everything sits in the same place

A common arrangement is to keep everything inside a single system, often a single bank, with the salary, the savings and perhaps a fund or a pension sold by that same bank. It feels safe because it is normal.

In practice it means that savings lose purchasing power when their return after costs and tax falls below inflation, that every movement is recorded under your name, and that everything depends on the goodwill and the health of a few intermediaries. A frozen account, a bank in difficulty, a broker that stops serving your country or new capital controls are rare events, but they hit everything you own at the same moment when everything is in the same place. In March 2013 Cyprus closed its banks for about 10 days, and customers of its 2 largest banks [took losses on their deposits above 100,000 euros](https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/4/), while limits on withdrawals and transfers were only lifted in stages until 2015.

The opposite mistake exists too, which is to put everything into a single asset because someone online was convincing. Sovereignty, in this chapter, means having no single point of failure, on either side.

## 5 questions to ask of any asset

Forget returns for a moment, and ask 5 questions about anything you own.

1. **Who holds it?** You, or someone who owes it to you? A bank deposit is a loan to the bank. A share sits in a chain of brokers and depositories. A coin in your hand, or a key in your head, is held by you. The risk that the other side fails or refuses is called **counterparty risk**.
2. **Who can freeze or seize it?** Anything held by an intermediary can be blocked with a single decision.
3. **Who sees it?** Most assets are registered under your name and reported automatically.
4. **Who can create more of it?** If someone can, your share of the total shrinks.
5. **Can you move it?** Across a border, in an emergency, or to your children.

No asset gets 5 good answers, so the choice is about combining them, and about spreading not only what you own but also who holds it.

## A balance you cannot check yourself

The 5 questions are this book's recurring question, "who is the trusted third party?", applied to money. Earlier chapters asked who vouches for a key or who runs a server, and here the third party is whoever holds the asset, keeps the register or decides how much of it exists.

The grid adds a question about verification. A bank balance or a fund unit is a line in somebody else's database, which you read through their app and cannot audit yourself, so you rely on auditors, supervisors and the deposit guarantee. Physical gold can be tested, by weight, size, density or a dealer's spectrometer, provided someone does it. In June 2020, Caixin reported that at least part of the 83 tonnes of bars pledged by Wuhan Kingold Jewelry against about 16 billion yuan of outstanding loans [turned out to be gilded copper](https://www.caixinglobal.com/2020-06-29/cover-story-the-mystery-of-2-billion-of-loans-backed-by-fake-gold-101572911.html) when lenders finally had them tested. Bitcoin is designed so that an ordinary computer can do the audit, because a [full node](https://bitcoin.org/en/full-node) checks every transaction and every block against the rules, including the limit of 21 million (chapter 18). Until you run one, your wallet asks somebody else's server (chapter 13).

## Choose where value can live

The table applies the 5 questions to the main places where value can live. It describes trade-offs as of September 2026, it is not a ranking, and every line has serious weaknesses.

| Asset | Who holds it | Can it be frozen or seized? | Who sees it? | Can more be created? | Main weaknesses |
|---|---|---|---|---|---|
| **Cash** | You | Only physically | Nobody | Yes, by design | Loses purchasing power when prices rise. Theft, fire. Legal limits on large cash payments in many EU countries, and an EU-wide ceiling of 10,000 euros for payments to businesses from 10 July 2027. |
| **Bank deposit** | The bank. You hold a claim, guaranteed [up to 100,000 euros per depositor and per bank](https://eur-lex.europa.eu/EN/legal-content/summary/deposit-guarantee-schemes.html) in the EU. | Yes, with a single decision | The bank, the state | Yes, by design | Loses purchasing power if its net interest lags inflation. Fully surveilled. Depends on the bank and on the rules of the moment. |
| **Shares and funds** | A broker and a central depository, in your name | Yes. Centralised and easy to block, for example by sanctions or a broker leaving your country. | The broker, the tax office | Companies can issue new shares | You own part of real businesses, which is a genuine strength. But prices can fall for years, markets close, and you never hold anything yourself. |
| **Physical gold** | You, if it is at home or in a safe you control | Only physically. States have confiscated gold in the past (see the next section). | Dealers must identify buyers above a threshold that varies by country | Only by mining, slowly | Heavy, hard to move across borders, hard to spend, and verifying it takes tools or a dealer. Dealer margins. Storage and theft risk. |
| **"Paper" gold** (funds, unallocated accounts) | An intermediary | Yes | The intermediary, the tax office | Claims can exceed the metal | It is a promise of gold, not gold. Convenient, but with the same flaws as shares. |
| **Bitcoin, self-custody** | You, with your keys (chapters 13 and 14) | Not without your keys, although exchanges and payment services can still refuse to serve you | The ledger is public, under pseudonyms (chapter 16) | No. The limit of 21 million is enforced by every node | Young and volatile, so the price can fall hard. Mistakes are irreversible. Requires learning. |
| **Monero, self-custody** (advanced) | You, with your keys | Not without your keys, with the same limit as Bitcoin | Amounts, senders and receivers are hidden by default | Yes, slowly. Since 9 June 2022 a fixed [0.6 XMR per block](https://web.getmonero.org/get-started/faq/) is issued forever to pay miners (the "tail emission") | Much less liquid and much less accepted than Bitcoin. Regulated exchanges in Europe have been removing it (see the next section). A much smaller network, which an outside mining pool disrupted in 2025 (see below). More centralised development. Fewer wallets and devices. Volatile. |

Bitcoin left on an exchange, or gold left with a dealer, belongs in the "intermediary" rows, not in the self-custody ones.

Monero has a similar purpose to Bitcoin, money you can hold yourself, and privacy by default remains its real strength. Its network is however much smaller, which makes it easier for an outside entity to attack. In August 2025 the Qubic mining pool [claimed more than 51% of Monero's mining power](https://www.coindesk.com/business/2025/08/12/qubic-claims-majority-control-of-monero-hashrate-raising-51-attack-fears), and on 14 September 2025 a [reorganisation of 18 blocks cancelled 118 confirmed transactions](https://www.coindesk.com/web3/2025/09/15/monero-suffers-deepest-ever-blockchain-reorganization-invalidating-118-transactions). The [researchers who measured the campaign](https://arxiv.org/abs/2512.01437) observed deeper reorganisations, not a sustained majority. Qubic is a small project run by a small group of people, which leaves open the question of what a government, or any better organised and better funded group, could do to the same network. Its development is also more centralised, with a smaller group of developers and rule changes made through [upgrades that every participant must install](https://www.getmonero.org/2022/04/20/network-upgrade-july-2022.html).

A reasonable approach for most people is to keep what you need for the coming months where it is simple and stable, to make sure no single institution holds everything, and to learn, with small amounts, how to hold at least 1 asset that needs nobody's permission. Which asset, and how much, is your decision alone.

## The rules around an asset can change

The answers in the table are not fixed, because the rules around an asset can change with a single decision. On 5 April 1933, [Executive Order 6102](https://www.presidency.ucsb.edu/documents/executive-order-6102-forbidding-the-hoarding-gold-coin-gold-bullion-and-gold-certificates) required people in the United States to deliver their gold coins, bullion and certificates to the Federal Reserve by 1 May, above an exemption of 100 dollars per person. The penalty was a fine of up to 10,000 dollars, up to 10 years in prison, or both.

Monero is a current European example. Kraken [stopped trading it for clients in the European Economic Area on 31 October 2024](https://support.kraken.com/articles/support-for-monero-xmr-in-europe), citing regulatory changes. The EU's anti-money-laundering regulation of 31 May 2024 goes further, since [its Article 79](https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng) prohibits banks and crypto-asset service providers, from 10 July 2027, from keeping accounts that allow transactions to be anonymised, including through "anonymity-enhancing coins".

The prohibition is addressed to regulated intermediaries, and the regulation states that it does not apply to providers of self-hosted wallets. The practical effect, as of September 2026, is that Monero is becoming harder to buy and to sell through regulated platforms in Europe.

Some of its users see this exclusion as its strength. An asset that large marketplaces cannot list depends on none of them, and it is used by individuals, from person to person. Bitcoin has both faces, since it is held by large institutions and traded on regulated platforms while also circulating between individuals, peer to peer.

## Step by step

1. **Draw the map.** On paper, list where your savings are, including accounts, funds, pension, cash and anything else. Next to each, write who holds it.
2. **Ask the 5 questions** for each line. You are not looking for a perfect score, only for what you did not know.
3. **Find the single point of failure.** A single bank for everything, a single broker or a single country is the first thing to fix, and fixing it can be as simple as opening a second account elsewhere.
4. **Keep a reserve that needs nobody's permission.** A modest amount of cash at home covers a card outage or a frozen account for a few days.
5. **Learn 1 self-held asset with small amounts.** For Bitcoin, chapters 13 to 18 take you through it. For physical gold, the usual precautions are to choose common, recognisable coins from an established dealer, to compare the price with the metal price of the day, and to decide where the coins will be stored before anything else. Weighing and measuring a coin yourself, or later checking your bitcoin balance with your own node (chapter 18), is the step that replaces trust with verification.
6. **Keep records.** Dates, amounts and prices of what you buy and sell. Your tax return will need them.
7. **Plan for your absence.** An asset that only you can reach, and that only you know about, disappears with you. Chapter 6 explains how to leave instructions without handing over the keys.

## Mistakes to avoid

- **Confusing a claim with the thing.** A gold fund is not gold, and bitcoin on an exchange is not bitcoin in your wallet. Both are promises.
- **Putting everything in a single place,** whether that place is a bank or the asset you have just fallen in love with.
- **Investing money you will need soon, or money you borrowed,** in something volatile. Bitcoin, Monero, shares and even gold can lose a large part of their price for years, and a loan still has to be repaid after the price has fallen.
- **Following tips.** Anyone promising a return, a deadline or a secret is selling something. Be especially careful with strangers who contact you first.
- **Talking about what you hold.** Discretion is part of security, online and at dinner.
- **Forgetting taxes.** Selling at a profit is usually taxable, whatever the asset and however you acquired it.

## Go further

- **How the monetary system works, for general readers:** "Broken Money", by Lyn Alden.
- **How your deposits are protected:** the European Commission's page on deposit guarantee schemes (ec.europa.eu).
- **Monero, from the project itself:** getmonero.org. Common wallets include Monero GUI, Feather Wallet and Cake Wallet.
- **Next chapter:** your first Bitcoin wallet and your first sats.

## Sources

- [What are interest rates? Nominal and real returns](https://data.ecb.europa.eu/methodology/what-are-interest-rates), European Central Bank, checked 22 October 2026.
- [Deposit guarantee schemes, summary of Directive 2014/49/EU](https://eur-lex.europa.eu/EN/legal-content/summary/deposit-guarantee-schemes.html), EUR-Lex, consulted in September 2026.
- [Cyprus: National Bank Holiday, 2013](https://elischolar.library.yale.edu/journal-of-financial-crises/vol7/iss2/4/), Yale Program on Financial Stability, Journal of Financial Crises, 2025.
- [Executive Order 6102, Forbidding the Hoarding of Gold Coin, Gold Bullion and Gold Certificates](https://www.presidency.ucsb.edu/documents/executive-order-6102-forbidding-the-hoarding-gold-coin-gold-bullion-and-gold-certificates), The American Presidency Project, 5 April 1933.
- [Regulation (EU) 2024/1624, Articles 79 and 80](https://eur-lex.europa.eu/eli/reg/2024/1624/oj/eng), adopted on 31 May 2024 and published in the Official Journal of the European Union on 19 June 2024.
- [Support for Monero (XMR) in Europe](https://support.kraken.com/articles/support-for-monero-xmr-in-europe), Kraken, October 2024.
- [Cover Story: The Mystery of $2 Billion of Loans Backed by Fake Gold](https://www.caixinglobal.com/2020-06-29/cover-story-the-mystery-of-2-billion-of-loans-backed-by-fake-gold-101572911.html), Caixin Global, 29 June 2020.
- [Running a full node](https://bitcoin.org/en/full-node), Bitcoin.org, consulted in September 2026.
- [Qubic Claims Majority Control of Monero Hashrate, Raising 51% Attack Fears](https://www.coindesk.com/business/2025/08/12/qubic-claims-majority-control-of-monero-hashrate-raising-51-attack-fears), CoinDesk, 12 August 2025.
- [Monero Suffers Deepest-Ever Blockchain Reorganization, Invalidating 118 Transactions](https://www.coindesk.com/web3/2025/09/15/monero-suffers-deepest-ever-blockchain-reorganization-invalidating-118-transactions), CoinDesk, 15 September 2025.
- [Inside Qubic's Selfish Mining Campaign on Monero: Evidence, Tactics, and Limits](https://arxiv.org/abs/2512.01437), Suhyeon Lee and Hyeongyeong Kim, arXiv, December 2025, revised August 2026.
- [Monero will undergo a network upgrade on 13th August, 2022](https://www.getmonero.org/2022/04/20/network-upgrade-july-2022.html), getmonero.org, 20 April 2022.
- [FAQ, tail emission at block 2641623 on 9 June 2022](https://web.getmonero.org/get-started/faq/), Monero project, checked 22 October 2026. The current FAQ gives the actual start; the older Moneropedia page still carries an end-of-May estimate.

## Your checklist

- [ ] Draw the map of where your savings are and who holds each part (1 hour)
- [ ] Answer the 5 questions for your main account and your main investment (1 hour)
- [ ] Check that no single bank or broker holds everything you own (5 min)
- [ ] Set aside a small cash reserve at home (5 min)
- [ ] Decide which self-held asset you want to learn first, and with what small amount (5 min)
