# Chapter 3: Your browser and your searches

## In brief

Your browser and your search engine see more of your life than any other software, and the ones on your device were chosen for you by a business deal. Switch to a browser that blocks tracking, add a single good content blocker, and pick a search engine that does not build a profile of you. It takes less than an hour, and the difference shows at once in fewer ads and faster pages.

## A default that someone else paid for

You read the news, look up symptoms and compare loans in your browser, and most pages you open also load invisible code from dozens of other companies, such as advertising networks and analytics services. These **trackers** note what you are reading and add it to a profile built over years. Your searches reveal even more, since you ask a search engine things you would not ask your doctor or your partner.

Yet the defaults on your device were not chosen by you. A slide made public during the US antitrust trial against Google showed that the company [paid $26.3 billion in 2021](https://www.cnbc.com/2023/10/27/google-paid-26-billion-in-2021-to-become-a-default-search-engine.html) to be the default search engine, with Apple as the likely largest recipient and browser makers such as Mozilla among the others. In September 2025, a US federal judge [ended the exclusive contracts but let Google keep paying for placement](https://www.npr.org/2025/09/02/nx-s1-5478625/google-chrome-doj-antitrust-ruling), so as of September 2026 the default on your device is still, in most cases, the result of a payment.

Private or incognito mode does not solve this, because it only stops your own device from keeping the history and cookies. Websites, trackers, your internet provider and your employer's network see the same as before.

## 3 ways trackers recognise you

Trackers rely on 3 main techniques.

- **Third-party cookies.** A cookie is a small file a site stores in your browser. When the same advertising company is present on thousands of sites, its cookie follows you from one to the next. Safari, Firefox and Brave block or isolate these by default. Chrome, the most used browser, still allows them, and in April 2025 Google [confirmed that it was keeping this approach](https://privacysandbox.google.com/blog/privacy-sandbox-next-steps) after years of announcing their removal.
- **Fingerprinting.** Your browser reveals many small details, such as screen size, language, time zone, installed fonts and graphics hardware. Each one is ordinary, but combined they are often unique to you. Nothing is stored on your device, so deleting cookies changes nothing.
- **Your accounts.** If you stay logged in to Google or Facebook, every page that contains their code can be linked to your real name.

The defences follow the same logic.

- **Block.** A content blocker refuses to load known trackers at all.
- **Isolate.** The browser gives every site its own separate cookie storage, so that a cookie set on a given site is not readable on the next.
- **Look like everyone else.** Some browsers aim to make all their users appear identical, so that a fingerprint points to a crowd instead of a person.

Your IP address also identifies you, which is the subject of chapter 5.

## Who vouches for the padlock

The padlock promises that nobody on the way can read the page (confidentiality) and that the site really is the one named in the address (authenticity). The second promise comes from a **certificate authority**, an organisation that signs a certificate for the site, and your browser or system ships with a list of the authorities it accepts. Any of them can vouch for any site, which makes them the classic trusted third parties of the web. In 2011, an intruder at the Dutch authority DigiNotar [issued 531 false certificates](https://www.enisa.europa.eu/sites/default/files/all_files/Operation_Black_Tulip_v2.pdf), and the google.com one served to intercept about 300,000 users, almost all in Iran, before [browsers removed DigiNotar from their lists](https://blog.mozilla.org/security/2011/09/02/diginotar-removal-follow-up/).

**Certificate transparency** grew out of that failure. Certificates now have to appear in public logs that anyone can search, so a site's owner can spot a false one, and [Firefox has refused unlogged certificates on computers since version 135](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/OagRKpVirsA/m/Q4c89XG-EAAJ), in February 2025, as Chrome and Safari already did.

The browser maker is the other third party, because it chooses that list, the default search engine and the extension store, and its update channel can change the program you run. Open source and reproducible builds let outsiders check what it ships.

## Choose your browser

No browser is perfect, so look at who builds it, what it blocks without setup and what you give up.

| Browser | Who is behind it | Who you must trust | Strengths | Trade-offs |
|---|---|---|---|---|
| **Firefox** | Mozilla, owned by a non-profit foundation | Mozilla, for updates, its own list of certificate authorities and its add-ons store. Public code. | Its own engine, independent from Google's Chromium. Strong protection in Strict mode. Runs the full uBlock Origin on computers and on Android. | A few settings to change first. Sends usage data by default. Most of Mozilla's income comes from its search deal with Google. On iPhone it cannot install extensions. |
| **Brave** | Brave Software, a for-profit US company | Brave Software for updates, Google for the Chromium code underneath and the extension store. Public code. | Blocks ads and trackers with no setup, on iPhone too. Works with nearly every site. Computer and phone. | Promotes its own products, including a crypto wallet, reward ads and a paid VPN. You can turn them off. Built on Google's Chromium engine. |
| **Mullvad Browser** | Built by the Tor Project with Mullvad, a Swedish VPN company | The Tor Project and Mullvad, for updates. Public code, with reproducible builds that outsiders can check. | Strong anti-fingerprinting, designed so that all users look the same. No usage data sent. Free, no VPN required. | Computer only. Forgets everything when closed. Some sites break. |
| **LibreWolf** | A community of volunteers | A few volunteers, for the builds and for how fast Firefox security fixes arrive. Public code. | Firefox with strict settings already applied, usage data removed, uBlock Origin included. | Computer only. Small team. On some systems you handle updates yourself. |
| **Tor Browser** | The Tor Project, a non-profit | The Tor Project for updates (reproducible builds). No single relay sees both you and the site. | Hides your IP address by passing through 3 relays. The strongest anonymity in this table. | Slow. Many sites show extra checks or block it. Not made for your everyday logged-in accounts. |

For blocking, the reference is **uBlock Origin**, which is free, open source and has no paid exceptions for advertisers. It works fully in Firefox on computers and on Android. Chrome no longer runs it, because Google [switched off the older extension format in July 2025](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline) and removed the last extensions of that kind from the Chrome Web Store on 31 August 2026. What remains is a more limited version, uBlock Origin Lite, while Brave has its own blocker built in.

The iPhone is a separate case, because [Firefox for iOS cannot install extensions](https://support.mozilla.org/en-US/kb/add-ons-firefox-ios) so uBlock Origin is not available there. The options are Brave's built-in blocker, the simpler ad blocker that [Firefox offers on iOS](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) (off by default and rolling out progressively), or Safari with uBlock Origin Lite, available since August 2025.

Resist installing more, because every extension can read the pages you visit, and an unusual set makes your fingerprint more unique.

A reasonable setup for most people is **Firefox or Brave for everyday life**, plus **Mullvad Browser or Tor Browser** for the searches you prefer to keep apart from your accounts.

## Choose your search engine

Changing your search engine takes about a minute, which makes it one of the easiest steps in this book. According to their own policies, none of the options below builds an advertising profile of you, but they differ in where their results come from and how they earn money.

| Search engine | Where results come from | How it earns money | Good to know |
|---|---|---|---|
| **DuckDuckGo** | Mostly Bing, plus its own sources | Ads based on the words you type, not on a profile | US company. The easiest switch. |
| **Brave Search** | Its own independent index | Ads | Same company as the Brave browser. |
| **Startpage** | Google results, requested without your identity | Ads that are not personalised | Dutch company. Since 2019 its majority owner is System1, a US advertising group. |
| **Kagi** | Its own index plus several other sources | Paid subscription, no ads | US company. Needs an account. Funded by its users only. |
| **SearXNG** | Combines many engines at once | Nothing. It is free, open-source software | Host it yourself or use a public instance (list at searx.space). You then trust whoever runs that instance. |

Try one for 2 weeks before judging. Results for local Lithuanian searches can vary from one engine to another, and nothing stops you from using a second engine for the occasional difficult query.

## Step by step

The example uses Firefox on a computer, because it exists on every system and is independent from Google's engine. The same logic applies to the others, and the names of settings may move slightly between versions.

1. **Install it** from mozilla.org or your system's official store.
2. **Raise the protection.** In Settings, Privacy & Security, set Enhanced Tracking Protection to Strict.
3. **Force encrypted connections.** On the same page, turn on HTTPS-Only Mode in all windows. This is the step that replaces trust with verification, since the browser then checks a certificate on every connection instead of relying on the networks in between.
4. **Stop sending usage data.** Still on the same page, in the section about Firefox data collection, untick the boxes.
5. **Change the search engine.** In Settings, Search, choose your new default. If it is not in the list, visit the search engine's site and add it from the address bar.
6. **Install uBlock Origin** from the official add-ons site (addons.mozilla.org), and keep its default settings, which are good.
7. **Bring your bookmarks.** Use the import tool in the bookmarks menu to copy bookmarks from your old browser. Do not import saved passwords, because they belong in your password manager (chapter 2).
8. **Make it the default, on your phone too.** Set the new browser as default on your computer, then repeat the same choices on your phone. On Android, Firefox also accepts uBlock Origin. On iPhone it does not, so use one of the iPhone options described above.

## Mistakes to avoid

- **Believing incognito mode makes you invisible.** It hides your browsing from the people who share your device, and from nobody else.
- **Installing 10 privacy extensions.** Each one can read your pages, and together they make you stand out, so a single good content blocker is enough.
- **Staying logged in to Google or Facebook all day in your main browser.** Keeping those accounts in a second browser stops their cookies from following your everyday browsing, which weakens the link between your name and what you read. It does not remove that link, because your IP address and your fingerprint remain visible to the sites you visit.
- **Clicking "Accept all" out of habit.** Look for "Reject all". uBlock Origin can also hide most cookie banners if you turn on the cookie notices lists in its settings.
- **Pushing every setting to the maximum.** If half your sites break, you are likely to go back to the old browser within a week, so raise the settings gradually and keep the level you can live with.
- **Ignoring updates.** The browser is the program most exposed to the internet, so restart it when it asks.

## Go further

- **Test your browser:** Cover Your Tracks, by the Electronic Frontier Foundation (coveryourtracks.eff.org), shows how unique your fingerprint is.
- **Compare in detail:** Privacy Guides, "Desktop Browsers" and "Search Engines" (privacyguides.org).
- **Next chapter:** your email and your aliases.

## Sources

- [Operation Black Tulip: certificate authorities lose authority](https://www.enisa.europa.eu/sites/default/files/all_files/Operation_Black_Tulip_v2.pdf), ENISA (European Union Agency for Cybersecurity), December 2011.
- [DigiNotar removal follow up](https://blog.mozilla.org/security/2011/09/02/diginotar-removal-follow-up/), Mozilla Security Blog, 2 September 2011.
- [Certificate Transparency is now enforced in Firefox on desktop platforms starting with version 135](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/OagRKpVirsA/m/Q4c89XG-EAAJ), Mozilla dev-security-policy list, 4 February 2025.
- [Google paid $26 billion in 2021 to become a default search engine](https://www.cnbc.com/2023/10/27/google-paid-26-billion-in-2021-to-become-a-default-search-engine.html), CNBC, 27 October 2023.
- [In a major antitrust ruling, a judge lets Google keep Chrome but levies other penalties](https://www.npr.org/2025/09/02/nx-s1-5478625/google-chrome-doj-antitrust-ruling), NPR, 2 September 2025.
- [Next steps for Privacy Sandbox and tracking protections in Chrome](https://privacysandbox.google.com/blog/privacy-sandbox-next-steps), Google, 22 April 2025.
- [Manifest V2 support timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline), Chrome for Developers (Google), updated in September 2026.
- [Add-ons in Firefox for iOS](https://support.mozilla.org/en-US/kb/add-ons-firefox-ios), Mozilla Support, consulted in September 2026.
- [Block ads in Firefox for iOS](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios), Mozilla Support, checked 22 October 2026.

## Your checklist

- [ ] Change the default search engine on your computer and your phone (5 min)
- [ ] Install a browser that blocks tracking and make it your default (1 hour)
- [ ] Add uBlock Origin where supported, or use your browser's blocker, and remove unused extensions (5 min)
- [ ] Move your Google and Facebook sessions to a second browser (5 min)
- [ ] Test your browser on coveryourtracks.eff.org (5 min)
