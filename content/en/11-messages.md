# Chapter 1: Your messages

## In brief

Your conversations are among the most intimate data you produce. Move them to a messenger that is end-to-end encrypted by default, that is open source, and that collects as little metadata as possible. Several good ones exist, and none wins on every point. Pick one, move your 5 closest contacts first, and keep your old app for everyone else.

## Encrypted does not mean private

Many everyday chat apps belong to advertising companies. WhatsApp and Messenger, both owned by Meta, do encrypt the content of your messages, but they still record who you talk to, when, how often, from which device and which location, and they connect it to the rest of what the group knows about you.

Others do not encrypt by default at all. On Telegram, ordinary chats and all group chats are stored in a form the company can read. SMS is weaker still, because your operator can read it and it crosses the telephone network unencrypted. After the group known as Salt Typhoon broke into several American telecom operators, the US cybersecurity agency CISA [advised in December 2024](https://www.cisa.gov/resources-tools/resources/mobile-communications-best-practice-guidance) that highly targeted people use only end-to-end encrypted messaging and stop relying on SMS for login codes.

Then come the backups. A conversation can be encrypted in transit and still end up readable in a cloud backup, yours or that of the person you are talking to.

The consequences are concrete: leaked conversations, accounts taken over by scammers who then write to your family, and messages handed over on a legal request, years after you forgot you wrote them.

## A sealed envelope the carrier cannot open

With **end-to-end encryption**, a message is locked on your phone and can only be unlocked on the phone of the person you write to. The company in the middle carries a sealed envelope it cannot open, so if it is hacked or receives a legal request, it has no message content to give. Depending on how the app was designed, it may still hold metadata, such as an IP address, a contact list or the date of your last connection.

That envelope is also a political subject in Europe. The regulation that the European Commission [proposed on 11 May 2022](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52022PC0209), known to its critics as "Chat Control", would allow authorities to order messaging services to scan private communications. As of September 2026 it is still being negotiated between the Parliament and the Council, and [the round of 29 June 2026](https://www.europarl.europa.eu/legislative-train/theme-promoting-our-european-way-of-life/file-combating-child-sexual-abuse-online) ended without agreement. The temporary rule that lets providers scan voluntarily was [reinstated on 23 July 2026](https://www.consilium.europa.eu/en/press/press-releases/2026/07/23/fighting-child-sexual-abuse-online-interim-measure-protecting-children-now-reinstated/) until 3 April 2028, and at the Parliament's request it [excludes end-to-end encrypted communications](https://www.europarl.europa.eu/news/en/press-room/20260706IPR46318/combating-child-sexual-abuse-support-for-a-more-limited-eprivacy-derogation).

Encryption is necessary, but 3 more things matter:

- **Open source.** The code is public, so independent experts can check that the app does what it claims, instead of taking the company's word for it.
- **Metadata.** The most careful messengers are designed to know very little about you, which can mean no contact list, no group membership and sometimes no identifier at all.
- **Who runs it.** A non-profit or a community has no advertising business to feed, and a network without a central company has no single door to knock on.

## Confidential does not mean authentic

Encryption answers 1 question, whether someone else can read the message, and leaves another open, which is whether the person at the other end is really who you think. Cryptographers call the first property confidentiality and the second authenticity. An SMS or an email offers neither, a familiar voice on a phone call can help recognise someone without making the call confidential, but is not proof of identity, since voices can be cloned, and a secure channel has to offer both.

Authenticity depends on how your app obtained the other person's key. In Signal, WhatsApp, iMessage and most encrypted messengers, that key comes from a directory run by the company, which makes the company a trusted third party, however well it encrypts. If the directory were compromised, or compelled to hand out a false key, the envelope would still be sealed, but for the wrong reader. Safeguards exist, with [safety numbers in Signal](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed) (60 digits to compare), [key transparency in WhatsApp](https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/) and [contact key verification in iMessage](https://security.apple.com/blog/imessage-contact-key-verification/), but they are optional and rarely used.

Other designs remove the directory and decentralise that trust. Olvid [requires 2 codes of 4 digits](https://olvid.io/faq/olvid-secure-channels/) to be exchanged before the first message, while SimpleX and Briar start from a link or a QR code that you hand over yourself. Security then rests on the 2 people involved, and the price is convenience, since the app cannot find your contacts for you.

## Choose your messenger

Start with an honest look at what you probably use today. None of these apps is useless, but each has a clear weak point. The table reflects the situation in September 2026.

| Messenger | Owner | End-to-end encrypted? | What it still collects or exposes | Verdict |
|---|---|---|---|---|
| [**WhatsApp**](https://www.whatsapp.com/) | Meta | Yes, by default (Signal protocol) | Extensive metadata: your contacts, who you write to, when, from which device. Closed source. Cloud backups are only end-to-end encrypted if you turn it on. | Content protected, metadata feeds an advertising group. |
| [**Facebook Messenger**](https://www.messenger.com/) | Meta | Yes, by default for personal chats and calls since December 2023. Not for chats with businesses or Marketplace. | The same metadata, tied to your Facebook identity. Closed source. | Better than before, still a Meta product. |
| [**Instagram direct messages**](https://www.instagram.com/) | Meta | No. The optional encrypted chats were removed on 8 May 2026. | Meta can read the content of every message, plus the metadata. | Not for anything private. |
| [**Telegram**](https://telegram.org/) | Telegram, a private company | Only in "secret chats", which you start by hand, between 2 people. Ordinary chats, all groups and channels are not. | Ordinary messages are stored on Telegram's servers, which the company can read. The server code is closed. | A social network more than a private messenger. |
| **SMS** | Your mobile operator | No | Content and metadata are readable by operators, can be intercepted, and can be redirected by a SIM swap (a scammer moving your number to their SIM card). | Avoid for anything sensitive, including login codes when you have the choice. |
| [**iMessage (Apple Messages)**](https://support.apple.com/messages) | Apple | Yes, between Apple devices (blue bubbles) | Apple devices only. Closed source. iCloud backups are readable by Apple unless you turn on Advanced Data Protection. | Good inside the Apple world, and nowhere else. |
| [**Google Messages (RCS)**](https://www.android.com/google-messages/) | Google, with the mobile operators | Yes, by default between Google Messages users. With iPhones, encryption started rolling out in May 2026, in beta, and depends on your operator. | Tied to your phone number. Metadata is still collected. Closed source. Falls back to plain SMS when RCS is not available. | Better than SMS. Check for the lock icon. |

Here are better options. There is no single right answer, which is healthy, because a world where everyone depends on a single app is fragile. All 7 encrypt your private conversations end to end by default, and their apps are open source.

| Messenger | Needs a phone number | Who runs the network | Who vouches for the keys | Best for |
|---|---|---|---|---|
| [**Signal**](https://signal.org/) | Yes (can be hidden from others) | A single non-profit foundation | A directory run by Signal. Optional check with a 60-digit safety number. | Replacing WhatsApp with family and friends. The easiest switch. |
| [**SimpleX Chat**](https://simplex.chat/) | No identifier at all | Relays anyone can run | Nobody. You hand over a link or a QR code yourself, with an optional security code to compare. | Strong metadata protection. No account, no username, no identifier to link. |
| [**Session**](https://getsession.org/) | No | A decentralised network of community-run nodes | No directory, since your Session ID is your public key. You must obtain that ID through a channel you trust. | Anonymous accounts, messages routed through several nodes. Slower, fewer features. Its current protocol lacks forward secrecy (a key stolen one day could unlock older messages). An upgrade has been announced. |
| [**Threema**](https://threema.com/) | No | A single Swiss company, paid app | A directory run by Threema. Scanning a contact's QR code in person raises them to the highest trust level. | People who want no phone number and a polished, paid product. |
| [**Olvid**](https://olvid.io/) | No, and no email or other personal data | A single French company, with servers hosted on Amazon Web Services | Nobody. The 2 people exchange 2 codes of 4 digits before the first message, and this step is mandatory. | A European app whose security is certified by ANSSI, the French cybersecurity agency. Messages and receiving calls are free. Making calls and using several devices need a subscription (about 5 euros a month). |
| [**Element (Matrix)**](https://element.io/) | No | Federated: many servers, or your own | Your server's directory. Optional verification by comparing emoji or scanning a QR code. | Communities, teams, people who want to host their own server. The servers involved see metadata (who is in which room, and when), so the choice of server matters. |
| [**Briar**](https://briarproject.org/) | No | Nobody: device to device | Nobody. Contacts are added by QR code in person, or by exchanging links. | Extreme situations. Works over Tor, and even over Bluetooth or wifi without internet. Android, plus a desktop version in beta (Windows, macOS, Linux). No iPhone app. |

A reasonable setup for most people is **Signal for everyday life**, plus **a messenger without a phone number** (SimpleX, Session or Olvid, for example) for contacts you do not want linked to your identity.

If part of your circle stays on WhatsApp, help them at least turn on encrypted backups (Settings, Chats, Chat backup, End-to-end encrypted backup). WhatsApp explains it in its help centre, under [About end-to-end encrypted backup](https://faq.whatsapp.com/490592613091019).

## Step by step

The example uses Signal because it is the most common first step, and the same logic applies to the others. Menu names are those of September 2026.

1. **Install it** from the official store or from the project website, and register.
2. **Lock your account.** In Settings, Account, set a PIN and turn on Registration Lock, so that re-registering your number requires that PIN.
3. **Hide your number.** Create a username, then in Settings, Privacy, Phone Number set "Who can see my number" to Nobody. You can now give your username instead of your number. The separate setting "Who can find me by number" decides whether someone who already has your number can find you on Signal. Set it to Nobody too if you prefer that, knowing that friends will then need your username.
4. **Make messages disappear by default.** In Settings, Privacy, Disappearing messages, choose a default timer, for example 4 weeks. This reduces the history left on your phone. It cannot remove screenshots, exports or copies made by the recipient.
5. **Lock the app** with Settings, Privacy, Screen lock.
6. **Verify your important contacts.** Open the conversation, tap the name, then View safety number, and compare it in person or by another channel you already trust, such as calling a number you already know is theirs. A familiar voice alone is not enough. This is the step that gives you authenticity and stops you depending on Signal's directory, so do it once with the few people who matter most.
7. **Move your people** without announcing a revolution. Write to your 5 closest contacts from the new app, create the family group there, and let the old app fade out.

## Mistakes to avoid

- **Thinking "encrypted" means "private".** Encryption protects the content, but it does not hide who you talk to unless the messenger was designed for that.
- **Forgetting the phone itself.** Anyone holding your unlocked phone can read everything, which makes a strong screen lock part of your messenger's security.
- **Leaving cloud backups on.** An unencrypted backup keeps a readable copy of conversations that were encrypted in transit. Check your settings, and remember that the other person's backup matters too.
- **Waiting for everyone to move.** Part of your circle will stay where it is, and 2 apps side by side is a perfectly fine result.
- **Confusing privacy with anonymity.** A messenger tied to your phone number protects what you say, not who you are. If you need to stay unidentified, use a messenger without a phone number.
- **Trusting the app more than the person.** Screenshots exist, and the weakest point of a conversation is often the other end.

## Go further

- **Compare messengers in detail:** Privacy Guides, "Real-Time Communication" (privacyguides.org).
- **Understand your own risks:** Surveillance Self-Defense, by the Electronic Frontier Foundation (ssd.eff.org).
- **Next chapter:** your passwords and your accounts.

## Sources

- [Set and manage disappearing messages](https://support.signal.org/hc/en-us/articles/360007320771-Set-and-manage-disappearing-messages), Signal Support, checked 22 October 2026.
- [Scammers use fake emergencies to steal your money](https://consumer.ftc.gov/articles/scammers-use-fake-emergencies-steal-your-money), Federal Trade Commission, checked 22 October 2026.
- [Proposal for a regulation laying down rules to prevent and combat child sexual abuse, COM(2022) 209](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52022PC0209), European Commission, 11 May 2022.
- [Legislative train: combating child sexual abuse online](https://www.europarl.europa.eu/legislative-train/theme-promoting-our-european-way-of-life/file-combating-child-sexual-abuse-online), European Parliament, updated 1 August 2026.
- [Combating child sexual abuse online: support for more limited ePrivacy derogation](https://www.europarl.europa.eu/news/en/press-room/20260706IPR46318/combating-child-sexual-abuse-support-for-a-more-limited-eprivacy-derogation), European Parliament, 9 July 2026.
- [Fighting child sexual abuse online: interim measure protecting children now reinstated](https://www.consilium.europa.eu/en/press/press-releases/2026/07/23/fighting-child-sexual-abuse-online-interim-measure-protecting-children-now-reinstated/), Council of the EU, 23 July 2026.
- [Mobile Communications Best Practice Guidance](https://www.cisa.gov/resources-tools/resources/mobile-communications-best-practice-guidance), CISA, 18 December 2024.
- [What is a safety number and why do I see that it changed?](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed), Signal Support, consulted in September 2026.
- [Deploying key transparency at WhatsApp](https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/), Engineering at Meta, 13 April 2023.
- [Advancing iMessage security: iMessage Contact Key Verification](https://security.apple.com/blog/imessage-contact-key-verification/), Apple Security Research, 2023.
- [Olvid secure channels](https://olvid.io/faq/olvid-secure-channels/), Olvid, consulted in September 2026.

## Your checklist

- [ ] Install a private messenger, lock it with a PIN, hide your number and set disappearing messages (5 min)
- [ ] Move your 5 closest contacts and your family group (1 hour)
- [ ] Verify the safety number of your 3 most important contacts (5 min)
- [ ] Install a second messenger that needs no phone number (5 min)
- [ ] Turn on encrypted backups in the apps you keep (5 min)
