# Chapter 16: Privacy in Bitcoin

## In brief

Bitcoin does not hide its transaction graph at the base layer. Transactions remain public; identifying their owners depends on outside information and heuristics. An address, however, carries no name. It becomes tied to you through the identity check of an exchange, or through the people you transact with who know you, and from there an observer can link a wallet to a person. A few habits reduce this exposure considerably (fresh addresses, separate wallets, labelled coins, your own node, Lightning for everyday spending), and advanced tools such as coinjoin and payjoin go further. None of them changes your legal or tax obligations.

## A public ledger that never forgets

Your bank statement is seen by you and your bank, whereas the Bitcoin ledger can be read by anyone, and nothing is ever erased from it. Those who say that Bitcoin lacks privacy are right about this base layer, because the transaction graph remains available for analysis, even when its owners cannot be identified reliably.

Those who answer that an address is not an identity are right too, up to a point. An address carries no name, and it only gets one through a link made elsewhere. An exchange that verified your identity knows where you withdrew your coins. The people you transact with know you, such as an online shop that has your name and sees the address you paid from. Analytics companies make a business of collecting these links, grouping addresses by owner and selling the result, which lets an observer link a wallet to a physical person.

From that moment, past and future activity connected to that address can be followed by a merchant, an employer, a landlord or a curious acquaintance.

The stake is also physical. In January 2025, [David Balland, a co-founder of Ledger, was kidnapped at his home in France](https://www.coindesk.com/policy/2025/01/24/ledger-co-founder-s-kidnapping-sheds-light-on-soaring-crypto-robberies) and the attackers demanded a ransom in cryptocurrency before the police freed him and his partner. The developer Jameson Lopp maintains [a public list of physical attacks on bitcoin holders](https://github.com/jlopp/physical-bitcoin-attacks).

## Large movements show, individuals have tools

With fiat money, the largest actors can place large transactions behind financial structures, such as holding companies, trusts and accounts in several jurisdictions, while the population's everyday use of banking services is closely monitored, payment by payment. With Bitcoin it tends to be the reverse. Privacy can be harder for very large amounts, because a coinjoin needs other participants and a useful set of plausible outputs, so when a state or a large institution moves bitcoin, it usually shows on the public ledger. In the summer of 2024, the German state of Saxony [sold about 49,858 seized bitcoin between 19 June and 12 July](https://www.medienservice.sachsen.de/medien/news/1077662), and the press [followed the transfers from the labelled wallet to exchanges](https://cointelegraph.com/news/german-government-354m-btc-sell-off) day by day, using the data of the analytics firm Arkham.

An individual, on the other hand, has tools to gain privacy and to resist deanonymisation, which the rest of this chapter presents. It takes care and some learning, but someone who applies them properly can, in practice, use Bitcoin privately.

## 3 patterns that give you away

Your bitcoin is better pictured as separate coins of different sizes, like banknotes in a purse, than as an account balance. Each coin you received sits on the public ledger with its amount and its address.

3 simple patterns reveal a lot:

- **Address reuse.** If you receive 10 payments on the same address, anyone can see all 10, add them up, and watch when they move.
- **Merged inputs.** When you pay, your wallet may combine several coins into 1 transaction, like paying with 2 banknotes. An observer concludes that both coins belong to the same person, so 1 coin with your name on it now identifies the other.
- **Change.** If you pay 30 with a coin of 50, the remaining 20 comes back to a new address of yours. Observers can often guess which output is the change, and keep following you.

Analysts combine these guesses, which are called heuristics. They are not always right, but they are good enough to build a profile, and good privacy habits give them less to work with.

## KYC and what it implies

KYC means "know your customer", the identity verification that regulated exchanges must perform. You send a copy of your ID, often with a selfie and a proof of address. This is a legal duty for the company, and using such a service is perfectly normal.

It does create a lasting link between your identity and your coins, stored in a company database. In the European Union, [the MiCA regulation](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica) has applied to crypto-asset service providers since 30 December 2024, with a transition period that ended on 1 July 2026. Since 1 January 2026, [the DAC8 directive](https://taxation-customs.ec.europa.eu/taxation/tax-transparency-cooperation/administrative-co-operation-and-mutual-assistance/directive-administrative-cooperation-dac/dac8_en) also requires these providers to collect data on the transactions of their EU-resident users and to report it to the tax authorities, which exchange it between member states from 2027. Databases of this kind can leak, and a list of people who hold bitcoin, with home addresses, is of obvious interest to criminals.

Bitcoin can also be acquired on peer-to-peer markets, where you trade directly with another person and no central company collects your documents. This is legal in most places, but rules differ, so check yours. Your tax obligations remain exactly the same however you acquired your coins, so keep your own records.

## Who learns which coins are yours

The ledger shows addresses without names, so your confidentiality depends on the parties able to attach your name to them.

The first is the server your wallet queries. A wallet that does not hold the ledger asks a server about each of its addresses, and by default that server belongs to the wallet's maker or to a volunteer. According to [the Sparrow documentation](https://sparrowwallet.com/docs/best-practices.html), a public server learns your balance and, through your IP address, your location. It may log nothing, but you cannot check.

The second is the exchange that verified your identity, which knows your name, your home address and where you withdrew, and can be breached or ordered to hand over its records. In May 2025, Coinbase disclosed that customer data had been copied from its support systems, and [its filing counted 69,461 people](https://cointelegraph.com/news/70k-impacted-coinbase-data-breach-maine-attorneys). Analytics firms are observers, working from the public ledger and the data they obtain.

Neither the server nor the exchange can be audited from outside, so the practical route is to remove them where it matters, with your own node, Tor in the meantime and peer-to-peer acquisition, each at the price of convenience. For a beginner, a regulated exchange often remains the safer choice.

## Choose your privacy habits

Privacy in Bitcoin comes from a set of habits rather than from 1 tool. Each helps on its own, so start at the top of the table.

| Habit | Tools | Effort | What you gain | Who still learns something |
|---|---|---|---|---|
| **Never reuse an address** | Any modern wallet gives a fresh address for every payment | None | Avoids the direct link created by receiving repeatedly on 1 address; later spending can still link payments | The server your wallet queries still sees all these addresses together |
| **Separate wallets for separate purposes** | Any wallet: savings, spending, KYC coins, non-KYC coins | Low | Reduces accidental links between purposes; shared servers and later transactions can still connect them | The same server, if both wallets query it from the same IP address |
| **Label your coins and use coin control** | Sparrow Wallet, Nunchuk, Electrum (all open source) | Medium | You decide which coin pays, and you avoid merging coins by accident | Nobody new, since labels stay in your wallet file. Back that file up |
| **Connect to your own node** | See chapter 18 | High (a weekend of work, then a few days of synchronisation) | No outside server learns which addresses are yours | Nobody for your balance. Other nodes see the transaction you broadcast, unless your node uses Tor |
| **Use Lightning for everyday spending** | See chapter 15 | Low | Individual payments are not written on the public ledger | A custodial wallet sees every payment. A self-custodial app's service provider (LSP) still sees part of them |
| **Use Tor in your wallet** | Sparrow includes Tor. Electrum and several others have a proxy setting, which needs Tor installed separately | Low to medium | The server you connect to does not see your IP address | The server still sees your addresses. Tor relays are run by volunteers and carry encrypted traffic |
| **Peer-to-peer acquisition** | Bisq (desktop, open source, no company in the middle), RoboSats (open source, over Tor and Lightning), Hodl Hodl (web platform run by a company, multi-signature escrow) | Medium | No identity documents stored in an exchange database | The other trader, who sees your name on a bank transfer. The platform sees the trade, not your ID |
| **Coinjoin and payjoin** (advanced, see below) | Coinjoin: Wasabi Wallet with an independent coordinator, JoinMarket (now joinmarket-ng, with the Jam interface), Ashigaru. Payjoin: BTCPay Server, Bull Bitcoin, Cake Wallet | High for coinjoin (fees, time, discipline afterwards). Low for payjoin, when both sides support it | Weakens common-ownership or change heuristics, depending on the protocol and how you spend afterwards | A coordinator sees that you take part, by design not which output is yours. Some exchanges question coinjoined coins |
| **Swap a small amount into Monero to spend it** (advanced, see below) | Atomic swap software (eigenwallet, open source, non-custodial) or peer-to-peer markets that list Monero (Bisq) | Medium to high | A payment much less likely to be linked to your identity, since Monero hides amounts, senders and receivers by default | The swap counterparty sees the bitcoin side. A tool for spending, not for savings |

Lightning protects the payer better than the receiver, and a custodial Lightning wallet sees all your payments. Peer-to-peer platforms do not operate in every country, so check yours.

A reasonable setup for most people is fresh addresses, 1 wallet per purpose, labels from the first day and Lightning for small payments, then your own node when you are ready. The last 2 rows are advanced, and the next 3 sections explain them.

## Coinjoin, payjoin and mixers

The 3 patterns rest on guesses, and some tools are built to make those guesses fail. In a **coinjoin**, several people build 1 transaction together, with many inputs and many outputs of the same amounts, so that ownership is harder to infer from that transaction alone. Amounts, timing and later spending can still provide clues. Nobody gives up custody, because each participant signs only if their own output is there. In a **payjoin**, the sender and the receiver both contribute inputs to a payment, which breaks the assumption that all the inputs of a transaction belong to 1 person, and hides the amount really paid. **Mixers** are the older approach, a service that takes your coins and sends back others. It is custodial, so the operator can keep the money or the logs.

As of September 2026, coinjoin is usable in [Wasabi Wallet](https://docs.wasabiwallet.io/using-wasabi/CoinJoin.html), through independent coordinators since its maker closed its own in June 2024, in JoinMarket, a peer-to-peer market without a coordinator, [continued as joinmarket-ng since the original repository was archived in April 2026](https://atlas21.com/coinjoin-comparison-of-tools-to-improve-privacy-on-bitcoin/), and in Ashigaru, a fork of Samourai Wallet that [relaunched the Whirlpool coinjoin in June 2025](https://ashigaru.rs/news/announcement-whirlpool/). Payjoin works in BTCPay Server for merchants, and [in the Bull Bitcoin and Cake Wallet apps](https://bitcoinops.org/en/topics/payjoin/) since 2025.

## Legal to use, prosecuted to operate

Using these tools to protect your financial privacy is legal in most places, but the law differs between countries and is moving, so check yours, and what you have to declare stays the same. The prosecutions so far have targeted operators. In the United States, the 2 founders of Samourai Wallet, arrested in April 2024, pleaded guilty to conspiring to operate an unlicensed money transmitting business that knowingly moved criminal proceeds, and were [sentenced in November 2025 to 5 and 4 years in prison](https://www.irs.gov/compliance/criminal-investigation/founders-of-samourai-wallet-cryptocurrency-mixing-service-sentenced-to-five-and-four-years-in-prison). Roman Storm, a developer of Tornado Cash, a mixer on Ethereum, was [convicted of a similar offence on 6 August 2025](https://www.irs.gov/compliance/criminal-investigation/founder-of-tornado-cash-crypto-mixing-service-convicted-of-knowingly-transmitting-criminal-proceeds). The jury reached no verdict on the money laundering and sanctions counts, which leaves part of the case open as of September 2026, although the US Treasury had [lifted its sanctions on Tornado Cash on 21 March 2025](https://home.treasury.gov/news/press-releases/sb0057).

In the Netherlands, Alexey Pertsev, another Tornado Cash developer, was [sentenced to 64 months in prison in May 2024](https://www.coindesk.com/policy/2024/05/14/tornado-cash-developer-alexey-pertsev-found-guilty-of-money-laundering) and has appealed. None of these developers is accused of having stolen anything. What they are blamed for is having written and run software that criminals also used, as well as people seeking ordinary financial privacy. These sources do not establish what share of users belonged to either group. For many developers and civil liberties groups, this is a serious attack on freedom of expression and on the freedom to build, because publishing code is a form of speech and a privacy tool does not choose its users, any more than encryption or cash does. Several of these cases are still before the courts as of September 2026.

These cases explain why coordinators close or refuse users from some countries, and why some exchanges question coins that come out of a coinjoin. A beginner does not need to start here.

## Monero for spending, not for saving

Some advanced users keep bitcoin as the asset they hold for the long term, and swap a small amount into Monero when they want a payment that is less likely to be linked to their identity. Monero is a separate currency with a similar purpose, money you can hold yourself, where amounts, senders and receivers are hidden by default, which is its real strength.

It is however less secure as a place to keep value, because it is much less liquid and much less accepted, its client software is developed by a smaller, more centralised group, and its much smaller network is easier for an outside entity to attack. In 2025 the Qubic mining pool claimed a majority of its mining power, and on 14 September a [reorganisation of 18 blocks cancelled 118 confirmed transactions](https://www.coindesk.com/web3/2025/09/15/monero-suffers-deepest-ever-blockchain-reorganization-invalidating-118-transactions). Qubic is a small project run by a small group of people, which leaves open the question of what a government, or any better organised and better funded group, could do to the same network.

Swaps are done with non-custodial atomic swap software such as eigenwallet, or on peer-to-peer markets such as Bisq, since regulated platforms in Europe are removing Monero. The [EU anti-money-laundering regulation of 2024](https://eur-lex.europa.eu/eli/reg/2024/1624/oj) bars them, from 10 July 2027, from keeping accounts that use "anonymity-enhancing coins". Instant swap websites also exist, but they hold your coins during the swap. Legal and tax obligations still apply, and in many countries a swap is a taxable event. Chapter 12 compares the 2.

## Step by step

The example uses Sparrow Wallet on a computer. Nunchuk and Electrum offer the same functions under slightly different names.

1. **Create 1 wallet per purpose.** For example savings, spending, and a separate wallet for coins that came from an exchange with identity verification.
2. **Receive on a fresh address every time.** The Receive screen offers a new one automatically. Never copy an old address from your history.
3. **Label every payment when it arrives.** Write where it came from, for example "exchange, March" or "sold my bike to Tomas". In 6 months you will not remember.
4. **Choose which coin pays.** Before sending, open the list of your coins (Sparrow calls it UTXOs), select the one that fits, and send from it. Avoid combining coins from different sources.
5. **Label the change.** The coin that comes back to you inherits the history of the payment, so note it.
6. **Pay small things over Lightning** (chapter 15), and keep on-chain transactions for larger, rarer movements.
7. **Turn on Tor** in the wallet's server or network settings if you still use a public server. Later, replace the public server with your own node (chapter 18). Tor only hides your IP address from that server, whereas the node is the step that removes the third party, because the questions about your addresses no longer leave your home.

## Mistakes to avoid

- **Posting addresses or balances publicly.** A screenshot of your wallet on social media links your name to your coins, and deleting the post later does not undo it, because copies circulate and the ledger keeps everything.
- **Merging KYC and non-KYC coins.** A transaction that combines them tells every observer they belong to the same person, so keep them in separate wallets. The aim is to avoid showing your whole history to a merchant, and it changes nothing in what you have to declare.
- **Reusing a donation address.** A single static address shows every donor what all the others gave, and what you did with it. Use a tool that generates a new address per donor, or Lightning.
- **Believing a VPN makes Bitcoin private.** A VPN hides your IP address from a server. It does nothing about the ledger, which is public for everyone.
- **Talking about how much you own.** Analysts work from the ledger, but a conversation gives away the same information faster. Nobody needs to know the number, online or at a dinner.
- **Aiming for perfection and doing nothing.** Labels and separate wallets can start today, whereas the node and the advanced techniques can wait.

## Go further

- **The reference text:** the "Privacy" page of the Bitcoin Wiki (en.bitcoin.it). Long, but complete.
- **Coinjoin and payjoin explained:** the Wasabi Wallet documentation (docs.wasabiwallet.io) and the Payjoin project (payjoin.org).
- **Practical guides:** Bitcoiner.Guide, by BitcoinQ+A (bitcoiner.guide), and the Sparrow Wallet documentation (sparrowwallet.com/docs) for labels and coin control.
- **Next chapter:** hardware wallets.

## Sources

- [Protect your privacy](https://bitcoin.org/en/protect-your-privacy), Bitcoin.org, checked 22 October 2026.
- [DAC8, the directive on the reporting of crypto-asset transactions](https://taxation-customs.ec.europa.eu/taxation/tax-transparency-cooperation/administrative-co-operation-and-mutual-assistance/directive-administrative-cooperation-dac/dac8_en), European Commission, applicable since 1 January 2026.
- [Markets in Crypto-Assets Regulation (MiCA)](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica), European Securities and Markets Authority, page consulted in September 2026.
- [Regulation (EU) 2024/1624 on the prevention of money laundering](https://eur-lex.europa.eu/eli/reg/2024/1624/oj), Official Journal of the European Union, 19 June 2024.
- [Monero Suffers Deepest-Ever Blockchain Reorganization, Invalidating 118 Transactions](https://www.coindesk.com/web3/2025/09/15/monero-suffers-deepest-ever-blockchain-reorganization-invalidating-118-transactions), CoinDesk, 15 September 2025.
- [Notveräußerung von fast 50.000 Bitcoins abgeschlossen](https://www.medienservice.sachsen.de/medien/news/1077662), Generalstaatsanwaltschaft Dresden, Free State of Saxony, 16 July 2024 (in German).
- [German gov't $354M BTC sell-off](https://cointelegraph.com/news/german-government-354m-btc-sell-off), Cointelegraph, 10 July 2024.
- [Coinjoin](https://docs.wasabiwallet.io/using-wasabi/CoinJoin.html), Wasabi Wallet documentation, consulted in September 2026.
- [CoinJoin in 2026: Wasabi, JoinMarket and Ashigaru compared](https://atlas21.com/coinjoin-comparison-of-tools-to-improve-privacy-on-bitcoin/), Atlas21, updated 10 June 2026.
- [Announcement: new Zerolink coinjoin coordinator](https://ashigaru.rs/news/announcement-whirlpool/), Ashigaru, June 2025.
- [Payjoin](https://bitcoinops.org/en/topics/payjoin/), Bitcoin Optech, consulted in September 2026.
- [Founders of Samourai Wallet cryptocurrency mixing service sentenced to five and four years in prison](https://www.irs.gov/compliance/criminal-investigation/founders-of-samourai-wallet-cryptocurrency-mixing-service-sentenced-to-five-and-four-years-in-prison), IRS Criminal Investigation, 19 November 2025.
- [Founder of Tornado Cash crypto mixing service convicted of knowingly transmitting criminal proceeds](https://www.irs.gov/compliance/criminal-investigation/founder-of-tornado-cash-crypto-mixing-service-convicted-of-knowingly-transmitting-criminal-proceeds), IRS Criminal Investigation, 6 August 2025.
- [Tornado Cash Developer Alexey Pertsev Found Guilty of Money Laundering](https://www.coindesk.com/policy/2024/05/14/tornado-cash-developer-alexey-pertsev-found-guilty-of-money-laundering), CoinDesk, 14 May 2024.
- [Tornado Cash delisting](https://home.treasury.gov/news/press-releases/sb0057), US Department of the Treasury, 21 March 2025.
- [Ledger Co-Founder's Kidnapping Highlights Threat of Crypto Robberies](https://www.coindesk.com/policy/2025/01/24/ledger-co-founder-s-kidnapping-sheds-light-on-soaring-crypto-robberies), CoinDesk, 24 January 2025.
- [Known physical bitcoin attacks](https://github.com/jlopp/physical-bitcoin-attacks), Jameson Lopp, list updated continuously.
- [Best practices](https://sparrowwallet.com/docs/best-practices.html), Sparrow Wallet documentation, consulted in September 2026.
- [Coinbase breach hit almost 70k users](https://cointelegraph.com/news/70k-impacted-coinbase-data-breach-maine-attorneys), Cointelegraph, 21 May 2025.

## Your checklist

- [ ] Check that your wallet shows a fresh address for every payment (5 min)
- [ ] Find any address or balance you have posted publicly, and stop receiving on those addresses (5 min)
- [ ] Create separate wallets for savings, spending and exchange withdrawals (1 hour)
- [ ] Label every coin you own with its origin (1 hour)
- [ ] Connect your wallet to your own node, after chapter 18 (weekend)
