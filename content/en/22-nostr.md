# Chapter 7: Nostr: an open network without a company in charge

## In brief

On a platform, your profile, your posts and your audience belong to the company that runs it. Nostr is an open protocol for signed data, where your identity is a key pair that you hold and where many independent relays and apps carry what you publish, so you can change app or relay at any time and keep your name and your followers. Today it is mostly used to build alternatives to social platforms, from short posts to photos, long articles, live video, music and marketplaces. It is smaller and rougher than the big platforms, and creating an account in an app such as Primal, Damus or Amethyst takes a few minutes.

## A public square owned by someone else

A social network looks like a public square, but it works like a private building whose owner sets the rules and can change them overnight. On 18 December 2022, Twitter [announced that it would remove links to Facebook, Instagram, Mastodon and Nostr](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/) and suspend accounts that promoted them, then withdrew the policy within a day after a wave of protest.

The same owner can remove an account, with or without a stated reason, and years of posts and contacts go with it. It can also reduce how many people see you without telling you, a practice often called a shadow ban. In ordinary times, an algorithm tuned for time spent and for advertising decides what you see, and your reach changes whenever it does.

Your audience is not yours either, because you cannot take your followers to another service, which is a large part of why leaving is so hard. What you read, like and write also feeds an advertising profile. In April 2025 the European Commission [fined Meta 200 million euros](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1085) under the Digital Markets Act, because users of Facebook and Instagram had to either accept the combination of their personal data for advertising or pay a subscription.

## Relays keep the record, clients are windows

Nostr is a protocol, like email or the web, which means that no company owns it and no single app defines it. It carries signed data of any kind, and a short post is only 1 case among others. It starts from 3 parts:

- **Your identity is a key pair** (chapter 6). The public key, which starts with **npub**, is your address, and you can share it freely. The private key, which starts with **nsec**, is your secret, because it proves that you are you.
- **Everything you publish is a signed event.** A post, a photo, a long article, a product listing or the announcement of a live stream carries a signature made with your nsec, so anyone can check that it is really yours and was not modified.
- **Zaps** are small Lightning payments (Part 3) sent directly to a person or a post. They allow you to support someone without advertising and without a platform taking a share.

To see where relays and clients fit, think of everything people publish as what happens outside, in nature. **Relays** are what records and keeps what happens out there. They are simple servers that anyone can run, and you publish to several at once. A **client** is a window onto it, and windows differ. Some show almost everything, others filter or hide part of the view, and a window can be shut or even boarded up while others stay open. You can always walk to another window, because the landscape does not belong to any of them, and a new client can retrieve your signed profile, posts and contact lists from the relays that still hold them. Keep local exports of important content; relays and media hosts do not promise permanent storage.

In February 2023, Apple [pulled the Damus client from its App Store in China](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) 2 days after its launch, at the request of the Chinese internet regulator. That window was boarded up for 1 country, while the relays and the other clients kept working.

## Relays cannot forge, but they can hide

A client is only a window, so it can filter spam or hide an account, which is often a service to you, but it cannot erase every copy from the network. Relays may remove events, including in response to a signed deletion request, and another client can show only the copies it can still retrieve. A relay keeps the record, so it can refuse your events, drop them later or never serve them to a given reader. It cannot write in your name or alter what you wrote, because the signature would no longer match your npub, and any client can run that check. Availability therefore depends on publishing to several relays run by different operators, and your [relay list](https://github.com/nostr-protocol/nips/blob/master/65.md) tells other clients where to find you.

2 trusted third parties remain. The first is whatever tells you that an npub belongs to the person you think. A NIP-05 address only shows that the key is listed on a domain, and [its specification](https://github.com/nostr-protocol/nips/blob/master/05.md) says that it identifies a user without verifying them, so for someone who matters, take the npub from that person directly. The second is any software that holds your nsec, because it could sign anything as you, a risk that signers, described below, reduce by keeping the key out of clients. A client can still misuse signing permissions you grant.

## Choose your client

Nostr is often presented as an alternative to X, which is only 1 of its uses. Some clients work like Instagram, others like Medium, Twitch, a podcast or music app, a marketplace, a group chat or an app store, and all of them accept the same key.

Be clear about what you get. The network is much smaller than the big platforms, spam exists, and some apps feel unfinished. There is no password reset, and no real deletion either, because you can ask relays to delete an event but they are free to ignore you. Treat every post as permanent and public.

Apart from Fountain, whose code is not published, and part of Wavlake, the clients below publish their source code under a free licence (checked on their public repositories in September 2026). Open source does not guarantee that the version in the app store matches the public code, but it allows anyone to check.

| Client | What it resembles | Type of content | Platforms | Where the trust sits |
|---|---|---|---|---|
| [**Primal**](https://primal.net/) | X, with the smoothest start and a built-in wallet. | Short posts, articles, media feeds | iOS, Android, web | Primal's caching server chooses what reaches you. It is [open source](https://github.com/PrimalHQ/primal-server), and the settings accept another one. |
| [**Damus**](https://damus.io/) | X, close to what Twitter looked like. Simple. | Short posts | iOS | Talks to your relays directly. The app itself holds your nsec on the phone. |
| [**Amethyst**](https://amethyst.social/) | X, with the most features, which can feel overwhelming at first. | Short posts, and most other kinds of events | Android | Talks to your relays directly. With the Amber signer, the app never holds your nsec. |
| [**Yakihonne**](https://yakihonne.com/) | Medium. | Long articles, curated content, short posts | iOS, Android, web | A single company builds the apps and runs its own relays. Accepts a remote signer. |
| [**Olas**](https://olas.app/) | Instagram. Slow release pace: the iPhone version in the store dates from March 2025, and a rewrite is in progress. | Photos and short videos | iOS, Android | Talks to your relays directly. The image files sit on media servers, which can remove them. |
| [**zap.stream**](https://zap.stream/) | Twitch. | Live video, with chat and zaps | Web, iOS, Android | Chat and announcements are signed events. The video passes through a streaming server, zap.stream's by default. |
| [**Fountain**](https://fountain.fm/) | A podcast app with comments and payments to the shows. | Podcasts, music | iOS, Android | A single company. The code is not published, and the built-in wallet is custodial. |
| [**Wavlake**](https://wavlake.com/) | Spotify or Bandcamp, for independent artists. | Music, paid directly to artists | Web, iOS, Android | A single company hosts the music and handles the payments to artists. The iPhone app dates from November 2025. |
| [**Shopstr**](https://shopstr.store/) | A classified-ads marketplace. | Product listings, paid in bitcoin | Web | Listings are signed events. Payment goes straight to the seller, without escrow, so check who you buy from. |
| [**0xchat**](https://www.0xchat.com/) | Telegram or WhatsApp. | Private and group chat | iOS, Android, desktop | Relays carry the encrypted messages. A young project, without the track record of the messengers of chapter 1. |
| [**Zapstore**](https://zapstore.dev/) | Google Play or F-Droid. | Android apps | Android | Each release is signed with the developer's Nostr key and checked before install. You choose which catalogs and developers to trust. |
| [**Iris**](https://iris.to/), [**Coracle**](https://coracle.social/), [**noStrudel**](https://nostrudel.ninja/) | X, in a browser. Coracle gives fine control over relays, noStrudel explores everything the protocol can do. | Short posts, and more in noStrudel | Web (Iris also on mobile) | The site that serves the code at each visit. Log in through an extension or a remote signer, not with the nsec. noStrudel can be self-hosted. |

A reasonable setup for most people is **a mobile client** for everyday use (Primal, Damus or Amethyst), **a web client** on your computer, used through a signer, and then 1 or 2 specialised clients that fit what you read, watch or listen to.

## Protect your nsec

Your nsec is your whole identity. If it leaks, someone can post as you for as long as they like, and you cannot change it the way you change a password. The rule that follows is to **never paste your nsec into a website you do not know**, and to paste it in as few places as possible.

The clean solution is a **signer**, a small app that keeps the key and signs on behalf of your clients. The client asks, the signer signs, and the client never sees the key. Check the requested permissions, avoid blanket approval for unknown clients, and revoke connections you no longer use. Several options exist:

- **Amber** on Android, an open source signer app that other Nostr apps call when they need a signature.
- **A browser extension** such as nos2x or Alby, for web clients on your computer.
- **A remote signer**, often called an nsec bunker, where the key stays on a single device or server and your apps connect to it over Nostr. It works on every platform.

On iPhone there is no exact equivalent of Amber for the moment, because iOS gives apps fewer ways to call each other. A few signer apps and Safari extensions exist, and the directory nostrapps.com lists the current ones. Otherwise, a remote signer is the usual route.

Then back up the nsec like any key in chapter 6, on paper in 2 places, or in your password manager while the account has little value.

## Step by step

The example uses a mobile client, and the logic is the same in all of them.

1. **Create your keys in a client.** Install it and choose "create account". No email and no phone number are needed, because the app generates the key pair on your phone.
2. **Back up the nsec immediately.** You find it in the settings, under keys or account. Do this before you post anything.
3. **Fill the profile** with a name, a picture and a short description, and remember that it is public.
4. **Optional: add a human-readable address** (called NIP-05). It looks like an email address, name@domain, and shows that your key is listed on that domain, and nothing more. Some services offer one, or you can use your own domain. It is not a login.
5. **Follow people.** Search by name for people you already know, add a few starter accounts that your client suggests, and follow some hashtags. An empty feed on day 1 is normal. For the accounts that matter to you, compare the npub with the one the person gives on their own website or in person, which is the step that replaces trust in a search result with verification.
6. **Add a second client with a signer.** On Android, install Amber. On a computer, install a browser extension such as nos2x or Alby. On iPhone, pick a signer app or a Safari extension from nostrapps.com, or set up a remote signer. Import your nsec into the signer once, then open a web client and choose the option to log in with an extension or a signer. Check that the second client finds your profile and contact lists, and that you publish to several independent relays. Portability depends on those records remaining available.
7. **Connect a Lightning wallet for zaps.** Add a Lightning address to your profile to receive, and link a wallet to send. Part 3 explains the wallets.

## Mistakes to avoid

- **Pasting your nsec into every new app you try.** Each copy is a risk. Use a signer, or test new apps with a second, throwaway key.
- **Thinking Nostr is private.** Notes are public by design. Direct messages vary from app to app, and may reveal who writes to whom. For private conversations, use a messenger from chapter 1.
- **Posting what you may want to delete.** Relays receive a deletion request and are free to ignore it, and copies may already exist elsewhere.
- **Depending on a single relay.** Publish to several, run by different operators, because the resistance to censorship comes from there.
- **Expecting the big platforms on day 1.** The network is smaller, and it becomes interesting once you follow 30 or 40 active people.
- **Keeping money in a wallet built for zaps.** A zap wallet is for small amounts, even when it is self-custodial. Primal's built-in wallet, for example, was custodial until 2026. Since version 3.0 (March 2026) it is [self-custodial](https://breez.technology/case-studies/primal), so you hold the recovery words, and it runs on Spark, a recent Bitcoin layer compatible with Lightning, whose guarantees depend in part on Spark's operators. Older reviews still describe the custodial version, and the built-in wallet of Fountain is custodial. Savings belong elsewhere (Part 3).

## Go further

- **A beginner guide:** nostr.how.
- **A directory of clients, signers and tools:** nostrapps.com.
- **The protocol itself,** for the curious: the NIPs repository (github.com/nostr-protocol/nips).
- **Next chapter:** replacing Big Tech services, one at a time.

## Sources

- [NIP-09, event deletion requests](https://github.com/nostr-protocol/nips/blob/master/09.md), Nostr protocol repository, checked 22 October 2026.
- [NIP-46, remote signing and permissions](https://github.com/nostr-protocol/nips/blob/master/46.md), Nostr protocol repository, checked 22 October 2026.
- [Twitter won't let you post your Facebook, Instagram and Mastodon handles](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/), TechCrunch, 18 December 2022.
- [Commission finds Apple and Meta in breach of the Digital Markets Act](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1085), European Commission, 23 April 2025.
- [Damus pulled from Apple's App Store in China after two days](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/), TechCrunch, 2 February 2023.
- [NIP-05: mapping Nostr keys to DNS-based internet identifiers](https://github.com/nostr-protocol/nips/blob/master/05.md), Nostr protocol repository, consulted in September 2026.
- [NIP-65: relay list metadata](https://github.com/nostr-protocol/nips/blob/master/65.md), Nostr protocol repository, consulted in September 2026.
- [Zapstore, an open app store](https://zapstore.dev/), Zapstore, consulted in September 2026.
- [Shopstr, a marketplace built on Nostr](https://shopstr.store/), Shopstr, consulted in September 2026.
- [Olas on the App Store](https://apps.apple.com/us/app/olas/id6738208592), Apple, version 0.4.0 published 11 March 2025, consulted in September 2026.
- [Primal Server](https://github.com/PrimalHQ/primal-server), PrimalHQ on GitHub, consulted in September 2026.
- [Primal case study](https://breez.technology/case-studies/primal), Breez, 2026.
- [Primal for Android, release notes](https://github.com/PrimalHQ/primal-android-app/releases), PrimalHQ on GitHub, version 3.0.7 published 17 March 2026.

## Your checklist

- [ ] Install a client and create your keys (5 min)
- [ ] Back up your nsec on paper or in your password manager (5 min)
- [ ] Fill your profile and follow a few people you already know (5 min)
- [ ] Install a signer and log in to a second client through it (5 min)
- [ ] Add a Lightning address to your profile and send your first zap (1 hour)
