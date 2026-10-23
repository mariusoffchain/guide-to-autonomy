# Chapter 5: Your network

## In brief

Every connection you make passes through equipment that belongs to someone else, whether it is your internet provider, the wifi of a cafe or the network at work. HTTPS already hides what you read and type, while networks can often still identify the sites you visit. A VPN hides that list from your provider and hides your IP address from websites, by moving your trust to the VPN company, and it does not make you anonymous. Tor and mixnets go further, at the cost of speed.

## Every network on the way can watch

Between your device and a website, your traffic crosses several networks, and each of them can observe it without any hacker being involved, because this is how networks work by default.

- **Your internet provider** sees every connection you make from home or from your phone, and in many countries the law makes it keep records of them.
- **Public wifi** in a cafe, a hotel or an airport is run by someone you do not know, and so is any network with the same name set up by a stranger.
- **The network at work or at school** is often monitored as a matter of policy.
- **Every site you visit** sees your IP address, the number that identifies your connection. It reveals your provider and your approximate location, and it lets sites and advertisers recognise you from one visit to the next, even without cookies.

In the European Union, a 2006 directive obliged providers to keep traffic and location data for 6 months to 2 years. The Court of Justice [declared it invalid on 8 April 2014](https://curia.europa.eu/site/upload/docs/application/pdf/2014-04/cp140054en.pdf), noting that such data "may provide very precise information on the private lives" of the people concerned. National retention rules still exist in several member states.

## The padlock hides pages, not destinations

**HTTPS**, the padlock in your browser, encrypts the link between you and the site, and almost all sites use it today. The networks in between can no longer see the pages you read, what you type or your passwords. They still see destination IP addresses, timing and data volumes, and often the domain name (the site, not the exact page). Encrypted DNS combined with Encrypted Client Hello, where supported, can hide that name too, though IP addresses and traffic patterns can still reveal destinations.

**DNS** is the phone book of the internet. Before your device can reach signal.org, it has to ask a DNS server which IP address is behind that name. By default the server belongs to your internet provider and the question often travels unencrypted, so your provider holds the list of every name you looked up even before the page loads.

**Encrypted DNS** sends those questions through an encrypted channel to a server you choose. Good free options are Quad9 (a Swiss non-profit that also blocks known malicious sites), Mullvad DNS (no account needed, optional ad blocking) and NextDNS (a company, very configurable, free up to a monthly limit). It is a small and useful step, although the network still sees the IP addresses you connect to.

## What a VPN does, and what it does not

A **VPN** builds an encrypted tunnel from your device to a server run by the VPN company, and all your traffic goes through it, DNS included. Your provider or the cafe's wifi only sees that you use a VPN, and websites see the address of the VPN server.

The VPN company now sees what your provider used to see, so a VPN moves your trust from a company you did not choose to one you did. It does not make you anonymous either, since cookies and browser fingerprinting (chapter 3) still work, and Google or Facebook know who you are as soon as you log in.

**Tor** removes the single trusted company by sending your traffic through 3 relays run by independent volunteers. The first knows who you are but not where you go, the last knows the opposite, and no single relay sees both ends. A **mixnet** also uses several hops, mixes your packets with those of other users, delays them and adds fake "cover" traffic. The design aims to make it much harder, even for an observer of the whole network, to match what enters with what leaves. It is slower and less tested in practice than Tor.

## A no-logs promise needs evidence

With a VPN, the confidentiality of your destinations rests on 1 company, which could log your connections, be ordered to do so, or be breached. A no-logs policy is a promise, and 2 kinds of evidence support it. Audits are the first, such as the [no-logs audit that Securitum has carried out at Proton VPN every year since 2022](https://protonvpn.com/blog/no-logs-audit), or the [security audit that IVPN orders from Cure53 each year](https://www.ivpn.net/blog/annual-security-audit-scheduled-2026). Legal cases are the second. On 18 April 2023, Swedish police [came to Mullvad's office in Gothenburg with a search warrant](https://mullvad.net/en/blog/2023/4/20/mullvad-vpn-was-subject-to-a-search-warrant-customer-data-not-compromised) and, according to the company, left without customer data because none existed. Both are snapshots, and neither shows what a server records today.

**Multi-hop**, offered by several VPNs, chains 2 servers so that a compromised server learns less, but when both belong to the same company the trust has not moved. Decentralising it takes independent operators, as with the 3 volunteer relays of Tor or the independently run servers of NymVPN. Decentralised does not mean verified, however, since nobody audits each relay or operator, and the protection rests on the low chance that they cooperate. You still trust the publisher of the software, and you pay in speed.

## Choose your network protection

The apps of every option below are open source, and each of the 4 VPN companies has published at least 1 independent security audit. They differ in who you have to trust, in speed and in how you can pay. Prices and payment methods were checked on the official sites in September 2026.

| Tool | Who runs it | Who sees your traffic | Payment | Trade-offs |
|---|---|---|---|---|
| **Mullvad VPN** | A single company, Sweden | Mullvad sees your IP address and your destinations. Its evidence is a series of audits and a 2023 police search that seized nothing. | Flat price of 5 euros a month. Card, PayPal, bank transfer, cash by post, bitcoin (Lightning included), monero | No email needed, the account is a random number. Fast, audited. No free tier. |
| **IVPN** | A single company, Gibraltar | IVPN sees your IP address and your destinations. Its evidence is a no-logs audit in 2019, then yearly security audits. | Paid. Card, PayPal, cash, bitcoin (Lightning included), monero | No email needed. Audited every year, very transparent about its limits. Smaller server network. |
| **Proton VPN** | A single company, Switzerland | Proton sees your IP address and your destinations. Its evidence is a yearly no-logs audit by Securitum since 2022. | Free tier without data limit on 1 device, paid plans. Card, PayPal, bank transfer, cash, bitcoin (only from an existing account) | Audited. The free tier is honest but slower, with few countries. The account needs an email address. |
| **NymVPN** | Nym, Switzerland. Servers run by independent operators | The entry operator sees your IP address, the exit operator your destinations. Nym publishes the app. Operators are not audited. | Paid. Card, cash by post, bitcoin (Lightning included), monero and other cryptocurrencies | No email needed, the account is a 24-word phrase. Audited in 2024. A fast 2-hop mode and a much slower 5-hop mixnet mode. A younger product with a shorter track record. |
| **Tor Browser / Orbot** | A non-profit and thousands of volunteer relays | The entry relay sees your IP address, the exit relay your destinations. No single relay sees both. Relays are not audited. | Free | The strongest protection of your IP address for browsing. Slow, and some sites block it or show endless verification puzzles. Orbot sends the traffic of phone apps through Tor. |

If you need a VPN, choose an operator from this list whose trade-offs suit you, including a reputable free tier where it meets your needs. Keep **Tor Browser** for browsing you want to separate from your usual connection and accounts; it cannot guarantee anonymity.

"Free VPN" apps deserve caution, because running servers costs money and the traffic of users who do not pay often becomes the product through advertising, tracking or resale of data. "Best VPN" ranking sites deserve the same caution. Most are paid a commission for each subscription they sell, and some belong to the same groups as the VPNs they rank. In March 2021, Kape Technologies [bought Webselenese, the publisher of the review sites vpnMentor and Wizcase, for 149.1 million dollars](https://en.globes.co.il/en/article-kape-acquires-israeli-co-webselenese-for-149m-1001363243), and vpnMentor [states on its own site](https://www.vpnmentor.com/about-us/) that Kape also owns ExpressVPN, CyberGhost and Private Internet Access.

## Step by step

The example uses Mullvad, and the same logic applies to the others.

1. **Install the app** from the official website of the provider or from the official store, never from a link in an advertisement.
2. **Create the account.** Mullvad gives you an account number and asks for nothing else. Store it in your password manager, then add time with the payment method you prefer.
3. **Connect.** Choose a server in your own country or a neighbouring one for the best speed. A distant country is only useful if you need to appear there.
4. **Turn on the kill switch.** This setting blocks all traffic if the tunnel drops, so that nothing goes out beside it. In Mullvad it is always active, and on computers an extra "lockdown mode" also blocks the internet when you disconnect on purpose. In other apps, look for "kill switch" in the settings. On Android, the system VPN settings also offer "Always-on VPN" and "Block connections without VPN".
5. **Connect automatically.** In the settings, turn on launch at start-up and auto-connect. Some apps, such as IVPN and Proton VPN, let you mark your home wifi as trusted and connect automatically on every other network.
6. **Set encrypted DNS for the moments without VPN.** On Android, in the network settings, find "Private DNS" and enter the host name of the service you chose, for example dns.quad9.net. On iPhone and on computers, the chosen service gives you a profile or an app to install. In your browser, turn on "secure DNS" in the privacy settings.
7. **Check for leaks.** With the VPN on, open mullvad.net/check or dnsleaktest.com. The IP address shown must belong to the VPN. The DNS servers shown belong either to the VPN or, if step 6 is active on that device or browser, to the encrypted DNS service you chose (Quad9, for example), whose questions then travel inside the tunnel. Both results are fine. A leak is when the name of your internet provider appears. This is the step that replaces trust with verification for what leaves your device, although no test of this kind shows what the VPN's own servers record.

## Mistakes to avoid

- **Believing a VPN makes you anonymous.** It hides your IP address from sites and your traffic from your provider, while cookies, fingerprinting and your own logins still identify you.
- **Choosing a VPN because it is free or because a ranking site said so.** Look for open-source apps, independent audits, a clear owner and a simple paid business model.
- **Leaving the kill switch off.** Tunnels drop, especially when your phone moves between wifi and mobile data, and without a kill switch your traffic silently goes back to the normal route.
- **Logging in to personal accounts inside Tor Browser.** Once you sign in, the site knows who you are and the extra hops no longer hide you from it.
- **Thinking the padlock means the site is honest.** HTTPS protects the connection, and a phishing site can have a padlock too.
- **Forgetting that the rules still apply.** A VPN is a legal privacy tool in the European Union, and what is illegal without it is still illegal with it. Some countries outside the EU restrict VPNs, so check the local rules before you travel.

## Go further

- **Compare VPNs without paid rankings:** Privacy Guides, "VPN Services" and "DNS Resolvers" (privacyguides.org).
- **Understand and download Tor:** the Tor Project (torproject.org). There is no official Tor Browser for iPhone, where the Tor Project [recommends Onion Browser](https://support.torproject.org/tor-browser/getting-started/installing/#ios), with weaker protections than on a computer.
- **Choosing a VPN that fits your situation:** Surveillance Self-Defense (ssd.eff.org).
- **Next chapter:** Part 2 begins, with keys instead of accounts.

## Sources

- [Firefox DNS over HTTPS, including ECH](https://support.mozilla.org/en-US/kb/firefox-dns-over-https), Mozilla Support, checked 22 October 2026.
- [Press release No 54/14: The Court of Justice declares the Data Retention Directive to be invalid](https://curia.europa.eu/site/upload/docs/application/pdf/2014-04/cp140054en.pdf), Court of Justice of the European Union, 8 April 2014.
- [Kape acquires Israeli co Webselenese for $149m](https://en.globes.co.il/en/article-kape-acquires-israeli-co-webselenese-for-149m-1001363243), Globes, 8 March 2021.
- [About us (ownership disclosure)](https://www.vpnmentor.com/about-us/), vpnMentor, consulted in September 2026.
- [Proton VPN passes 5th annual external audit of no-logs policy](https://protonvpn.com/blog/no-logs-audit), Proton VPN, updated 16 June 2026.
- [Mullvad VPN was subject to a search warrant. Customer data not compromised](https://mullvad.net/en/blog/2023/4/20/mullvad-vpn-was-subject-to-a-search-warrant-customer-data-not-compromised), Mullvad VPN, 20 April 2023.
- [Annual security audit scheduled for 2026](https://www.ivpn.net/blog/annual-security-audit-scheduled-2026), IVPN, 19 June 2026.
- [Nym response to Cure53 security audit](https://nym.com/trust-center/Cure53-security-audit-2024), Nym, July 2024.
- [Lightning payments](https://mullvad.net/en/blog/2025/8/5/lightning-payments), Mullvad VPN, 5 August 2025.
- [Installing Tor Browser (iOS section)](https://support.torproject.org/tor-browser/getting-started/installing/#ios), Tor Project, consulted in September 2026.

## Your checklist

- [ ] Turn on encrypted DNS on your phone and in your browser (5 min)
- [ ] Choose and install a VPN from a trustworthy operator (1 hour)
- [ ] Turn on the kill switch and auto-connect, then check for leaks (5 min)
- [ ] Install Tor Browser and try it once (5 min)
- [ ] Remove VPN apps whose operator or privacy practices you cannot trust (5 min)
