# Chapter 9: Taking back control of your phone

## In brief

Your phone knows more about you than any other object you own. You can reduce unnecessary data sharing in 1 evening, on the phone you already have, without installing anything: permissions, advertising ID, location, lock screen, SIM PIN, updates. That is level 1, and it is enough for most people. Level 2 is for the curious, with alternative app stores and Android systems that run without Google.

## A sensor that reports to many companies

Your phone is the most complete sensor you own. It knows where you sleep and where you work, it holds your contacts, your photos, your payments and often your health data, and it carries a microphone and a camera everywhere you go.

A flashlight app has no use for your contacts and a game has no use for your precise location, yet many ask anyway because data can be sold, and many free apps contain advertising code that reports to the same few companies. In January 2025 the location broker Gravy Analytics was hacked, and [the stolen files](https://www.theregister.com/2025/02/06/gravy_analytics_data_breach_suit/) contained the coordinates of tens of millions of phones, some of them in Europe, collected through popular apps such as Tinder, Candy Crush and MyFitnessPal.

To connect those reports, your phone carries an **advertising ID**, a number shared with every app so that what you do in one app can be linked to what you do in another. In April 2021 the organisation noyb [filed a complaint in France](https://noyb.eu/en/buy-phone-get-tracker-unauthorized-tracking-code-illegally-installed-android-phones), arguing that Android creates this identifier without asking for consent.

Finally, 2 companies, Google and Apple, control almost every phone, from the system to the app store and the default services.

## 4 levers that are in your hands

Almost everything in this chapter comes down to 4 ideas.

- **Permissions.** An app cannot reach your location, camera, microphone, contacts or photos unless the system allows it. You are the one who grants it, and you can take it back at any time, which makes it your strongest lever.
- **The advertising ID.** It is a setting. You can reset it, and on current phones you can delete it or refuse tracking entirely.
- **The app store as gatekeeper.** The store decides which apps exist for you, requires an account, and knows everything you install. On Android you may install apps from other sources, under conditions that are changing (see level 2). On iPhone this is far more restricted, even in the European Union.
- **System versus services.** Android itself is open source. What most people call "Android" is that system plus Google's apps and services, which run with deep privileges. The 2 can be separated, and that is what alternative systems do. iOS cannot be separated from Apple, but much of what it sends to iCloud can be switched off or encrypted.

## Level 1: harden the phone you have

Level 1 works on any phone, Android or iPhone, and it can start today. It uses settings that Google and Apple already provide, with no new app to install. Restricting permissions can affect app features; test the changes and restore only what you need. They cover the first 2 levers above, permissions and the advertising ID, together with the lock screen, the SIM card and updates.

Count 1 evening for the whole list. The review of permissions is the longest part, since every app has to be looked at once, and the other steps take a few minutes each. Nothing here is permanent, so an app that stops working because it really needed a permission will ask again, and you can grant it then.

Level 1 has a limit that is worth knowing. Google or Apple stay in the picture, with their store, their account and their services, and the apps you keep still see whatever you allow them to see. For most people this is a reasonable place to stop. The steps follow immediately, and level 2 comes after them for readers who want to go further.

## Step by step

These are the level 1 steps, on the phone you have. Menu names vary between brands and versions, so use the search bar in Settings if you cannot find one.

1. **Remove what you do not use.** Go through your apps and uninstall every one you have not opened in months. Removing an app stops its local activity, but does not delete data already held by its provider.
2. **Audit permissions.** On Android, open Settings, Privacy, Permission manager. On iPhone, open Settings, Privacy & Security. Go through Location, Microphone, Camera, Contacts and Photos, and ask for each app whether it really needs this. If in doubt, refuse, because the app will ask again if it matters. This is the step that replaces trust in what an app says about itself with a check of what it can reach.
3. **Limit location.** Choose "While using the app" instead of "Always", and turn off precise location for everything except maps and navigation. A weather app only needs your city.
4. **Remove the advertising ID.** On Android, in the privacy or Google settings, open Ads and choose "Delete advertising ID". On iPhone, open Settings, Privacy & Security, Tracking, and turn off "Allow Apps to Request to Track".
5. **Strengthen the lock.** Use a PIN of at least 6 digits, or a passphrase. Keep fingerprint or face unlock for convenience if you like, but the PIN is the real key. Hide the content of notifications on the lock screen.
6. **Set a SIM PIN.** It is in the SIM or mobile network settings. A stolen SIM placed in another phone then cannot receive your calls or SMS codes without that PIN. Find your operator's default PIN and PUK recovery procedure first, because 3 wrong PIN attempts block the card. This protects the physical SIM, not a SIM swap authorised by the operator.
7. **Turn on automatic updates,** for the system and for apps. Most attacks use holes that were already fixed.
8. **On iPhone, encrypt iCloud.** Open Settings, your name, iCloud, Advanced Data Protection. Your backups, photos and notes become end-to-end encrypted. You must set a recovery contact or a recovery key, because Apple can no longer help you get back in. As of September 2026 the option is available in the European Union, but not in the United Kingdom, where [Apple withdrew it in February 2025](https://support.apple.com/en-us/122234). If you are at real risk of targeted attacks (journalist, activist, public figure), also look at Lockdown Mode in Privacy & Security.

## Level 2: change the store or the system

Level 2 acts on the last 2 levers, the app store and the separation between the system and Google's services. It comes in 2 stages that do not depend on each other. On Android you can add another source of apps next to Google Play, or in place of it, which takes about 1 hour and can be undone. You can also replace the whole system with a version of Android that runs without Google, which takes a weekend, erases the phone and only works on certain models. On iPhone the system cannot be replaced and alternative stores remain far more restricted, so level 1 with Advanced Data Protection is in practice as far as it goes.

The price is convenience, and sometimes an app that refuses to run. The 3 parts below cover who you trust once you leave the official path, the choice of systems and app sources, and what may break, starting with banking apps. The facts in both tables are valid as of September 2026 and move fast.

### Someone signs every update you install

On a phone, authenticity is a matter of signatures. The system only starts if it is signed with a key that the hardware accepts, a mechanism Android calls [verified boot](https://source.android.com/docs/security/features/verifiedboot), and an app update is only installed if it carries the same developer signature as the version already on the phone. The trusted third parties are therefore the maker of the system, which can push an update to every phone, and the app store, which decides what is listed and what is removed, and which knows what each account has installed.

Leaving the official store moves that trust without removing it. F-Droid builds each app from its public source code and signs most of them with its own key, so you trust F-Droid in place of each developer. For part of its catalogue it relies on [reproducible builds](https://f-droid.org/docs/Reproducible_Builds/), where anyone can rebuild the app and obtain exactly the same file, and the app then keeps its developer's signature. A file downloaded from a website has no reviewer at all, so the address and the first installation carry the whole risk, and for a beginner the official store is often safer than a careless download.

### Choose your system and your app source

The first table compares the systems, starting with the one you already have after level 1, and the second compares the sources of apps on Android. In both, the last column names who signs what you install.

| System | Runs on | Strength | Trade-off | Who signs your updates |
|---|---|---|---|---|
| **Stock Android or iOS, hardened** | Your current phone | Familiar settings, reversible restrictions | Google or Apple remain in the picture | Apple, or Google and the phone's manufacturer. Verified boot is on |
| **GrapheneOS** | Compatible Google Pixel phones on the [maintained support list](https://grapheneos.org/faq). Check the remaining security support before buying; the oldest supported model may have little time left. A partnership with Motorola was [announced in March 2026](https://9to5google.com/2026/03/01/motorola-confirms-grapheneos-partnership-for-a-future-smartphone-porting-features/) for future models, and no current Motorola phone is supported | Strongest security. Google Play is optional and runs as an ordinary app without special privileges | You must buy a Pixel for the moment. Some apps refuse to run | The GrapheneOS project. The bootloader is locked again, and its [Auditor app](https://attestation.app/about) lets a second phone check the system |
| **CalyxOS** | Pixels, some Fairphone and Motorola models, SHIFTphone 8 | Gentler start, uses microG (an open-source replacement for Google services) | Security updates stopped in August 2025, and the project then advised users to leave. Releases [resumed on 1 July 2026](https://calyxos.org/news/2026/07/01/calyxos-official-release-is-back/). Check the pace of releases on calyxos.org before you choose it | The Calyx Institute, a US non-profit. The bootloader is locked again, so verified boot stays on |
| **LineageOS** | Hundreds of models, including older ones | Gives old phones a second life | Security depends on the device and its volunteer maintainer. No Google by default | The project and the volunteer maintainer of your model. The bootloader [usually stays unlocked](https://wiki.lineageos.org/faq), so verified boot is off |
| **/e/OS (Murena)** | Many models, also sold preinstalled | No installation needed if you buy one. Made by a European company | Security updates can arrive later than on the others | Murena and the e Foundation. The bootloader can be locked again on some models only |

| App source | What it is | Trade-off | Who you must trust |
|---|---|---|---|
| **F-Droid** | Catalogue of open-source apps only, no account | Updates can be slow. Smaller choice | F-Droid, which builds and signs most apps itself. Reproducible builds keep the developer's signature |
| **Aurora Store** | Open-source client for Google Play, usable without your own Google account | Free apps only in anonymous mode. Not endorsed by Google, can break | Google's servers and each developer's signature, as in Google Play, plus Aurora's shared accounts |
| **Obtainium** | Fetches updates directly from the developer's release page | You decide whom to trust. No review in between | Each developer, and the page you added. Android only checks that updates match the first signature |
| **Accrescent** | Security-focused store | Very small catalogue | Each developer, who signs their own apps. [Signed metadata](https://accrescent.app/features) pins the right key from the first install |

The rules for installing apps outside Google Play are changing. With its [developer verification programme](https://android-developers.googleblog.com/2026/06/android-developer-verification.html), Google requires that apps installed on certified Android phones come from a developer who has registered an identity with Google. It starts on 30 September 2026 in Brazil, Indonesia, Singapore and Thailand, and Google plans to extend it worldwide in 2027, so nothing changes in Europe for the moment. Apps from unregistered developers should remain installable through an "advanced flow" with extra confirmation steps. F-Droid [considers the programme a threat](https://f-droid.org/2025/09/29/google-developer-registration-decree.html) to its catalogue. Alternative systems such as GrapheneOS are not certified devices and do not apply it.

A reasonable path for most people is to do level 1 now, add F-Droid if you use Android, and consider a different system when you next change phones.

### Banking apps and other things that may break

Be clear about this before you replace the system. Some apps check whether the phone is certified by Google and refuse to run if it is not. Banking apps, payment apps, some government and identity apps, and a few games are the usual cases. Contactless payment with Google Wallet does not work on alternative systems.

Many banking apps do work, especially on GrapheneOS with Google Play installed as an ordinary app. However, nobody can promise it for your bank, and an update can change it.

People handle it in a few ways:

- They check community compatibility lists for their bank before switching.
- They use the bank's website and a physical card instead of the app.
- They keep a second phone with the stock system, at home and on wifi, only for banking and official apps. It has to be a model that still receives security updates, because an old phone that no longer gets them is a poor place for a banking app.
- They choose a bank whose app works.

## Mistakes to avoid

- **Granting everything during installation.** That is the moment you pay the least attention. Refuse first, allow later if something does not work.
- **Relying only on your fingerprint or face.** Biometrics are convenient, but someone can hold the phone to your face. Both systems can switch biometrics off until the next PIN entry. On iPhone, hold the side button and a volume button for a few seconds. On Android, use the Lockdown option in the power menu.
- **Installing an alternative system on your only phone the night before a trip.** Test first, with your banking and ticket apps, ideally on a second device.
- **Keeping a phone that no longer receives security updates.** Check how long the manufacturer supports a model before you buy it. Once support ends, known holes stay open whatever your settings, and this also applies to a second phone kept at home for banking.
- **Downloading app files from random websites.** Outside Google Play, use known sources such as F-Droid, the developer's own site, or one of the stores above.
- **Thinking a new system fixes your habits.** A hardened phone full of tracking apps, logged in to the same accounts, sends much of the same data as before.

## Go further

- **Compare systems and stores:** Privacy Guides, the Android and mobile phone sections (privacyguides.org).
- **Guides for both iPhone and Android:** Surveillance Self-Defense, by the Electronic Frontier Foundation (ssd.eff.org).
- **Project sites:** grapheneos.org, calyxos.org, lineageos.org, e.foundation, f-droid.org.
- **Next chapter:** hosting your own services.

## Sources

- [Supported devices and support lifetimes](https://grapheneos.org/faq), GrapheneOS FAQ, checked 22 October 2026.
- [Coordinates of millions of smartphones feared stolen, sparking yet another lawsuit against data broker](https://www.theregister.com/2025/02/06/gravy_analytics_data_breach_suit/), The Register, 6 February 2025.
- [Buy a phone, get a tracker: unauthorized tracking code illegally installed on Android phones](https://noyb.eu/en/buy-phone-get-tracker-unauthorized-tracking-code-illegally-installed-android-phones), noyb, 7 April 2021.
- [Android developer verification: Building a safer ecosystem together](https://android-developers.googleblog.com/2026/06/android-developer-verification.html), Android Developers Blog, 18 June 2026.
- [F-Droid and Google's developer registration decree](https://f-droid.org/2025/09/29/google-developer-registration-decree.html), F-Droid, 29 September 2025.
- [Verified Boot](https://source.android.com/docs/security/features/verifiedboot), Android Open Source Project, consulted in September 2026.
- [Reproducible builds](https://f-droid.org/docs/Reproducible_Builds/), F-Droid documentation, consulted in September 2026.
- [Frequently asked questions](https://wiki.lineageos.org/faq), LineageOS Wiki, consulted in September 2026.
- [Accrescent features](https://accrescent.app/features), Accrescent, consulted in September 2026.
- [CalyxOS is back: download release 7.2.2.0 with full maintenance support](https://calyxos.org/news/2026/07/01/calyxos-official-release-is-back/), CalyxOS, 1 July 2026.
- [Apple can no longer offer Advanced Data Protection in the United Kingdom to new users](https://support.apple.com/en-us/122234), Apple Support, 2025.

## Your checklist

- [ ] Uninstall the apps you no longer use (5 min)
- [ ] Review location, microphone, camera and contacts permissions (1 hour)
- [ ] Delete the advertising ID or turn off tracking (5 min)
- [ ] Set a PIN of 6 digits or more, and a SIM PIN (5 min)
- [ ] On iPhone, turn on Advanced Data Protection. On Android, install F-Droid and try 1 app (1 hour)
