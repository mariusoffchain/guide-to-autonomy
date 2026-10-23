# Chapter 6: Keys instead of accounts

## In brief

An account is a permission that a company gives you and can take back. A key is a secret that only you hold, and it works because of mathematics, whether or not a company agrees. You already use keys every day without seeing them, in your messenger and in your passkeys. The price of this freedom is that nobody can reset a key for you, so most of this chapter is about keeping your keys safe.

## An account is a revocable permission

An account is a row in the database of someone else, and the company decides what that row allows. It can lock it by mistake, by an automated decision, after a change of rules, or because the service closes or leaves your country. People lose years of email and photos this way, often with no human being to talk to.

An account is also only as safe as that database. In November 2022, the Irish Data Protection Commission [fined Meta 265 million euros](https://www.dataprotection.ie/en/news-media/press-releases/data-protection-commission-announces-decision-in-facebook-data-scraping-inquiry) after personal data of more than 500 million Facebook users, phone numbers included, had been posted online.

The "forgot my password" button is a second entrance, open to whoever controls your email address or your phone number. In March 2020, Europol [announced the arrest of 12 people in Spain](https://www.europol.europa.eu/media-press/newsroom/news/sim-highjackers-how-criminals-are-stealing-millions-highjacking-phone-numbers) suspected of stealing more than 3 million euros by obtaining duplicates of their victims' SIM cards and receiving the banks' confirmation codes in their place.

Accounts are convenient and fine for most services. For what matters most (your identity, your private conversations, your money), it is worth asking whether the thing could work without asking anyone for permission. With keys, to a large extent, it can.

## A secret that proves who you are

A **key pair** is 2 very large numbers created together on your device. The **private key** is a secret that stays with you, and the **public key** is calculated from it and can be shown to anyone. Going from private to public is easy, while going back is practically impossible.

A key pair does 2 things:

- **Receiving secrets.** Imagine a mailbox with a slot. Anyone who knows the address (your public key) can drop a letter in, and only the holder of the mailbox key (your private key) can open it.
- **Signing.** Your private key produces a signature that anyone can check with your public key, and that cannot be forged in practice without the private key.

No central server is needed to confirm who you are, because the verification is a calculation that anyone can run.

You already meet keys without knowing it. Your encrypted messenger (chapter 1) created a key pair on your phone. A passkey (chapter 2) is a key pair of which the website stores only the public half, and a Nostr identity (chapter 7) is a key pair too. Many Bitcoin wallets (Part 3) derive their keys from a backup of 12 or 24 words, while others use different formats (chapter 14). For the curious, SSH keys log administrators into servers, and PGP keys encrypt email and sign software.

## Someone still vouches for other people's keys

A key removes the third party for 1 property, control, because nobody can sign or decrypt in your place. Authenticity stays open as soon as someone else's key is involved, since nothing in a public key says whose it is. That information has to come from somewhere, and there are 4 usual answers: a directory run by a company, as in most messengers (chapter 1), a certificate authority, which is how your browser recognises a website, a web of trust in which people sign each other's keys, as PGP users do, or a fingerprint that you compare yourself through another channel.

Only the last answer has no trusted third party. In 2011 the Dutch certificate authority DigiNotar was breached, [a false certificate for google.com was issued](https://blog.mozilla.org/security/2011/08/29/fraudulent-google-com-certificate/) and browsers removed DigiNotar from their trusted lists. Public [Certificate Transparency](https://certificate.transparency.dev/) logs now allow anyone to see which certificates exist for a domain.

Passkeys show the same trade-off for storage. Synced by Apple or Google, they are [end-to-end encrypted](https://support.apple.com/en-us/102195), but reaching them from a new device goes through your account with that company, which is back in the loop for availability. A passkey on a security key depends on nobody, and it cannot be copied.

## Choose where to keep your keys

With a key there is no "forgot my password" button. No company can lock you out of it, and no company can let you back in. A lost key is gone, and whoever copies it can act as you. The responsibility moves from the company to you, so each key needs a home that matches its value.

| Where | Good for | Weak point | Who you still depend on |
|---|---|---|---|
| **Paper, written by hand, in 2 places** | Recovery codes, a Nostr key, a seed phrase for small amounts | Fire, water, and anyone who finds it | Nobody, apart from whoever can enter those 2 places |
| **Password manager** (chapter 2) | Low-value keys and recovery codes of ordinary sites | It lives on connected devices. Not the place for a Bitcoin seed, and it cannot hold its own recovery codes | The provider, for sync and app updates. The vault is end-to-end encrypted, and open source managers can be audited |
| **Hardware device** | A security key for logins (YubiKey, Nitrokey, Token2, among others), a hardware wallet or signing device for Bitcoin (chapter 17) | Costs money, can break or be lost. You still need a backup, either a second security key, or the seed on paper or steel | The maker of the chip and its firmware. YubiKey firmware is closed, Nitrokey firmware is open source |
| **Steel backup** | Seed phrases that must survive fire and water (chapter 14) | More expensive, and readable by whoever finds it | Nobody, apart from whoever can reach the hiding place |
| **Splitting or multi-signature** | Large value, with several keys in several places, so that no single loss or theft is fatal | Complex. A mistake in the setup can lock you out. Learn first | No single party. The software that coordinates the keys, and the people or places that hold them |

A reasonable setup for most people is **a password manager for low-value keys**, **paper in 2 places for the recovery codes that protect everything else**, **2 security keys for your main accounts**, and a hardware wallet with a steel backup once real savings are involved. Your situation may call for a different mix.

## Step by step

The example uses the keys most readers already have, and the logic is the same for every key you will create later.

1. **Make an inventory.** On paper, list the names of your keys and recovery codes, not the secrets themselves: the master password and recovery kit of your password manager, the two-factor recovery codes of your main accounts, your messenger PIN, the disk encryption recovery key of your computer, and later your Nostr key and your seed phrase. Passkeys cannot be written down, so note where each one lives (which phone, manager or security key) and the second way into that account.
2. **Decide a home for each one,** using the table above, and write it next to the name.
3. **Write the backups by hand.** No photo, no screenshot, no cloud note, no office printer. Write clearly and check every character twice.
4. **Store them in 2 locations,** for example your home and the home of a relative you trust, or a bank safe deposit box if you accept its opening hours and its rules. A single fire or burglary should not be able to take both copies.
5. **Buy 2 security keys, not 1.** A security key cannot be copied, so the second key is an independent way in, not a copy of the first. Register both on your main accounts (email, password manager, cloud storage) in the security settings, under "security key" or "passkey". Keep the first with you and the second with your paper backups, and keep the recovery codes of those accounts as well.
6. **Test a recovery.** Log in to an account with a recovery code, then generate fresh codes. Log in once with the second security key too, because an untested backup may fail on the day you need it. This is the step that replaces trust in a backup, and in a company's recovery process, with something you have checked yourself.
7. **Tell a trusted person** where things are and what to do, not the secrets themselves. A sealed letter with instructions is enough. No company can help your family recover a key after you are gone.
8. **Review the list once a year.**

## Mistakes to avoid

- **Photographing a key or a seed phrase.** Photos are copied to cloud services and can be read by other apps, which makes them a common way for a secret to leave your hands.
- **Typing a private key into a website, or giving it to "support".** No legitimate service asks for it, and a request of this kind is the mark of a scam.
- **Keeping the only copy on your phone.** Phones are lost, stolen and broken every day.
- **Storing the backup next to the device.** A thief or a fire then takes both at once.
- **Hiding it so well that nobody finds it.** That includes you in 5 years, and your family after you.
- **Choosing a complex scheme too early.** A split backup you do not fully understand is more dangerous than 2 sheets of paper in 2 safe places.

## Go further

- **Understand public key encryption:** Surveillance Self-Defense, "A Deep Dive on End-to-End Encryption", by the Electronic Frontier Foundation (ssd.eff.org).
- **Compare security keys and password managers:** Privacy Guides (privacyguides.org).
- **Learn about passkeys:** the FIDO Alliance (fidoalliance.org).
- **Next chapter:** Nostr, social media built on keys instead of accounts.

## Sources

- [Data Protection Commission announces decision in Facebook "Data Scraping" Inquiry](https://www.dataprotection.ie/en/news-media/press-releases/data-protection-commission-announces-decision-in-facebook-data-scraping-inquiry), Data Protection Commission (Ireland), 28 November 2022.
- [Meta hit with ~$275M GDPR penalty for Facebook data-scraping breach](https://techcrunch.com/2022/11/28/facebook-gdpr-penalty/), TechCrunch, 28 November 2022.
- [The SIM highjackers: how criminals are stealing millions by highjacking phone numbers](https://www.europol.europa.eu/media-press/newsroom/news/sim-highjackers-how-criminals-are-stealing-millions-highjacking-phone-numbers), Europol, March 2020.
- [Fraudulent *.google.com certificate](https://blog.mozilla.org/security/2011/08/29/fraudulent-google-com-certificate/), Mozilla Security Blog, 29 August 2011.
- [Certificate Transparency](https://certificate.transparency.dev/), project site, consulted in September 2026.
- [About the security of passkeys](https://support.apple.com/en-us/102195), Apple Support, consulted in September 2026.

## Your checklist

- [ ] List every key and recovery code you already have (1 hour)
- [ ] Write the missing backups by hand and store them in 2 places (1 hour)
- [ ] Test a recovery with a real recovery code (5 min)
- [ ] Tell a trusted person where your backups are (5 min)
- [ ] Buy 2 security keys and add them to your main accounts (weekend)
