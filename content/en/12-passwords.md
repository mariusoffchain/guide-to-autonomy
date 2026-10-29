# Chapter 2: Your passwords and your accounts

## In brief

Reused passwords remain one of the most common ways ordinary accounts get taken over, next to phishing. A password manager creates and remembers a different password for every site, and you protect it with a single strong passphrase. A second factor then goes on the accounts that matter, starting with your email, because whoever holds your email can reset almost everything else.

## A leaked password opens many doors

In January 2019, the security researcher Troy Hunt found a set of files circulating on a hacking forum under the name [Collection #1](https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/). It contained 773 million unique email addresses and more than 21 million unique passwords, assembled from thousands of older breaches. Attackers feed lists like this one to programs that try each pair of address and password on other services, such as your email, your shops and your social networks, a technique called **credential stuffing**.

Nobody is targeting you in particular, and the door simply opens wherever you reused a leaked password. Between April and September 2023, the genetic testing company 23andMe was hit in exactly this way. The British regulator [fined it £2.31 million in June 2025](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/06/23andme-fined-for-failing-to-protect-uk-users-genetic-data/), after the data of 155,592 UK residents was exposed, and noted that the company did not require a second factor at login.

You can check whether your own address appears in known breaches at [Have I Been Pwned](https://haveibeenpwned.com/), the free service that Troy Hunt runs. People who have been online for 10 years tend to find several. The account that matters most is your email, since whoever controls it can click "forgot my password" on almost everything else you own.

## A single passphrase, then a second factor

A **password manager** is an encrypted vault that creates a long random password for every site, remembers it and fills it in for you. The vault is encrypted on your own device before it is synchronised, so a well-designed provider is not able to read it, and you remember 1 secret instead of 100. That secret should be a **passphrase** of 6 random words, chosen for example by rolling dice against a word list (a method called diceware), which is hard to guess and far easier to remember than "xK9#qL2v".

**Two-factor authentication** (2FA) adds a step after the password, when the site asks for something you have. A code sent by SMS is the weak form, because a criminal can persuade your operator to move your number to their SIM card, an attack called a SIM swap. In March 2020, [Europol announced the arrest of 12 people in Spain](https://www.europol.europa.eu/media-press/newsroom/news/sim-highjackers-how-criminals-are-stealing-millions-highjacking-phone-numbers) who had used duplicate SIM cards to empty bank accounts more than 100 times, for a total above €3 million.

An authenticator app is much better, and a hardware security key is the strongest option. **Passkeys** use the same technology as these keys to replace the password itself.

## Zero knowledge still leaves a vault keeper

Encryption keeps a synchronised vault confidential, but the company that stores it and ships your updates remains a trusted third party. Providers call their design zero knowledge, meaning they hold the vault without the passphrase that opens it. In December 2022, LastPass [confirmed that an attacker had copied a backup of customer vaults](https://blog.lastpass.com/posts/notice-of-recent-security-incident). Passwords and notes were encrypted, the website addresses were not, and each stolen vault became only as strong as its owner's master password. The British regulator, which [fined the company £1.2 million in December 2025](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/12/password-manager-provider-fined/) for up to 1.6 million UK users affected, found no evidence that passwords had been decrypted.

Open-source apps let experts compare that claim with the code, and published audits add evidence, such as the [security certification that the French agency ANSSI gave KeePassXC](https://keepassxc.org/audits/) in November 2025, for its version 2.7.9. A local file or a server you host removes the vault keeper, and backups, updates and sync then become your job.

Second factors have third parties too. The site stores the same secret as your authenticator app and a sync service may hold a copy, whereas a hardware key also verifies authenticity in the other direction, by checking which website is asking.

## Choose your password manager

All the options below are far better than reusing passwords, and they differ on who holds your encrypted vault, whether the code is public, and how much work you accept.

| Manager | Open source | Where the vault lives | Who you must trust, and what you can check | Cost | Trade-offs |
|---|---|---|---|---|---|
| **[Bitwarden](https://bitwarden.com/)** | Yes | Bitwarden's cloud, or a server you host | Bitwarden, for storage and app updates. Public code, third-party audits published every year. Self-hosting removes the company. | Free, optional paid plan | The easiest open-source choice, on every device. The default service is run by a single US company. |
| **[KeePassXC](https://keepassxc.org/)** | Yes | A file on your own computer | No vault keeper. You rely on the app's public code, certified by ANSSI in 2025 (version 2.7.9), and on your own backups. | Free | No company, no cloud, no account. You handle sync and backups yourself. On phones, use compatible apps such as [KeePassDX](https://www.keepassdx.com/) (Android) or [KeePassium](https://keepassium.com/) (iPhone). |
| **[Proton Pass](https://proton.me/pass)** | Yes | Proton's cloud (Swiss company) | Proton, for storage and app updates. Public app code, audited by Cure53 in 2023. No self-hosting. | Free, optional paid plan | Includes email aliases. Practical if you already use Proton, but it concentrates more of your life in a single company. |
| **[1Password](https://1password.com/)** | No, closed source | 1Password's cloud (Canadian company) | 1Password, for storage, updates and the code itself. It publishes audit reports, not the source. | Paid subscription only | Polished, good for families, regularly audited. The public cannot inspect the code. |
| **Built into your browser or system** ([Google](https://passwords.google.com/), [Apple](https://support.apple.com/en-us/120758), [Firefox](https://www.firefox.com/en-US/features/password-manager/)) | Varies | Your Google, Apple or Mozilla account | Google, Apple or Mozilla, for storage, updates and account recovery. Only Firefox's code is fully public. | Free | Already there, and much better than nothing. Ties you to a single browser or ecosystem, and is only as safe as that main account. |

A reasonable setup for most people is **Bitwarden or Proton Pass** if you want sync without effort, or **KeePassXC** if you prefer that no company holds your vault, even encrypted.

## Choose your authenticator app

An authenticator app shows a 6-digit code that changes every 30 seconds. The site and your phone share a secret (the QR code you scan once), and both calculate the same code from it, even without a network, which makes it the right second factor for most of your accounts. Prefer an open-source app that lets you take your codes out again, because if the secrets live on 1 phone only, a lost or broken phone locks you out everywhere at once. Your password manager can often store these codes too, which is convenient but puts both factors in the same place.

| App | Platforms | Open source | Backup and sync | Trade-offs |
|---|---|---|---|---|
| **[Aegis](https://getaegis.app/)** | Android only | Yes | Encrypted vault on the phone. You export encrypted backups yourself. | No cloud and no account, so no sync service to trust. Backups are your job, and there is no iPhone version. |
| **[Ente Auth](https://ente.com/auth/)** | Android, iPhone, Windows, Mac, Linux, web | Yes | Optional end-to-end encrypted sync, which needs an Ente account. Also works offline without an account. | Your codes on all your devices. The sync depends on a single small company. |
| **[2FAS](https://2fas.com/)** | Android, iPhone, plus a browser extension | Yes | Backup through your Google Drive or iCloud account. | Simple. The backup is only as safe as that Google or Apple account. |
| **[Proton Authenticator](https://proton.me/authenticator)** | Android, iPhone, Windows, Mac, Linux | Yes | Works without an account. Optional end-to-end encrypted sync with a Proton account, plus local export and import. | Free, launched in July 2025, so younger than the others. Another part of your life at Proton if you already use it. |

A reasonable setup for most people is **Aegis** on Android if you accept handling backups yourself, or **Ente Auth or Proton Authenticator** if you want your codes on several devices. Whatever you choose, test the export or the backup once.

## Hardware security keys

A hardware security key is a different kind of tool. This small physical device, plugged into a USB port or held against your phone (NFC), holds a private key that is designed never to leave it, and it relies on open standards called FIDO2 and WebAuthn. When you log in, the key checks the real address of the website before it answers, and you touch it to confirm. A fake login page gets nothing from it, whereas a code from an app can still be typed into the wrong page by a tricked user. The same keys can also store **passkeys**.

Buy 2 and register both on every account, 1 for your keyring and 1 for a safe place. Not every site supports keys, so keep an authenticator app for the sites that do not, and use the keys first for the accounts that matter most, which are your email, your password manager and your main Apple or Google account.

| Key | Maker | Connection | Open source | Trade-offs |
|---|---|---|---|---|
| **[YubiKey](https://www.yubico.com/)** | Yubico (Sweden and United States) | USB-A or USB-C, NFC on most models | No, closed firmware | The most widely supported and documented. The firmware cannot be inspected or updated. The cheaper "Security Key" series is enough for logins. |
| **[Nitrokey](https://www.nitrokey.com/)** | Nitrokey (Germany) | USB-A or USB-C, NFC on some models | Yes, firmware and hardware | Firmware can be updated. Fewer models, less polished documentation. |
| **[Token2](https://www.token2.com/)** | Token2 (Switzerland) | USB-A or USB-C, NFC on most models | Partly. The FIDO2 part of the firmware is public and was independently reviewed in 2024, the rest is closed | Lower-priced keys. Less well known. |
| **[OnlyKey](https://onlykey.io/)** | CryptoTrust (United States) | USB only, no NFC | Yes, firmware | Has its own PIN buttons and can also type stored passwords. Bulkier, and more complex than a beginner needs. |

A reasonable setup for most people is 2 keys from any maker above, plus an authenticator app for the sites that do not accept keys.

## Step by step

The example uses Bitwarden because it is free, open source and works on every system, and the same logic applies to the others.

1. **Create your passphrase.** Roll dice against [the EFF word list](https://www.eff.org/dice), or use the manager's passphrase generator, until you have 6 words (the EFF recommends 6 as a minimum). Write it on paper and keep that paper somewhere safe at home.
2. **Install the manager** on your computer (as a browser extension) and on your phone, and create your account with that passphrase. If you forget it, you can lose your vault. Bitwarden cannot recover a forgotten master password. Emergency access, set up in advance, is a separate route (step 8).
3. **Start with your email.** Log in to your email account, change the password to one generated by the manager, and save it in the vault.
4. **Move 4 more accounts:** your main Apple or Google account, your bank or payment app, your main social network, and any shop that stores your card. The rest can follow over the next weeks, each time you log in somewhere.
5. **Turn on 2FA with your authenticator app** on those 5 accounts, email first, and on the password manager itself. In each account's security settings, look for "two-step verification" or "two-factor authentication", then scan the QR code with the app and type the code it shows. Where the site allows it, remove SMS as a method.
6. **Register your hardware keys, if you chose them.** In the same security settings, choose "security key" (sometimes "passkey"). Plug in or tap the first key, touch it, and give it a name, then repeat at once with the second key. From then on, the key checks the website's address at every login, instead of your eyes. Carry one and store the other in a safe place. Once both keys work, your way back in is the spare key plus the recovery codes (step 7). An authenticator app left on the same account is a weaker door, because its codes can still be phished. Remove it only after you have logged in once with the spare key.
7. **Save the recovery codes, away from the passphrase.** Most sites give you one-time codes for the day you lose your phone or your keys. Your password manager has one too, and it must never be stored only inside the vault it opens. Print them and keep them in a different place from your passphrase paper, for example the passphrase at home and the codes in a sealed envelope with a trusted relative, so that someone who finds 1 paper does not get everything.
8. **Plan emergency access.** Some managers have an emergency access feature for a trusted person (in Bitwarden it is part of the paid plan). Written instructions for your family, telling them where the 2 papers are, also work.

## Mistakes to avoid

- **Keeping the passphrase only in your head.** Memory can fail after an illness, an accident or a long holiday. A paper copy in a safe place is not a weakness, as long as your recovery codes are kept somewhere else.
- **Leaving SMS as a fallback.** If the site still accepts a code by SMS, a SIM swap still works, so remove it wherever the site lets you.
- **Having 1 authenticator or 1 hardware key, and no backup.** A lost phone or a lost key should cost you an afternoon and not your accounts, which is why you export your codes and register 2 keys.
- **Storing passwords in notes, spreadsheets or emails.** These are not encrypted vaults, and they are among the first places an intruder looks.
- **Typing a code into a page you reached from a message.** Authenticator codes can be phished too. If your manager does not offer to fill in the password, check the address, because you may be on a fake site.
- **Trying to change everything in a single evening.** Start with the 5 accounts above, then move the others over the following weeks, each time you log in somewhere.

## Go further

- **Check your exposure:** [Have I Been Pwned](https://haveibeenpwned.com/).
- **Make a dice passphrase:** [the word lists of the Electronic Frontier Foundation](https://www.eff.org/dice).
- **Compare tools in detail:** Privacy Guides, ["Password Managers"](https://www.privacyguides.org/en/passwords/), ["Multifactor Authentication"](https://www.privacyguides.org/en/multi-factor-authentication/) and ["Security Keys"](https://www.privacyguides.org/en/security-keys/).
- **Next chapter:** your browser and your searches.

## Sources

- [Implementing phishing-resistant MFA](https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf), CISA, checked 22 October 2026.
- [Emergency access](https://bitwarden.com/help/emergency-access/), Bitwarden Help, checked 22 October 2026.
- [The 773 Million Record "Collection #1" Data Breach](https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/), Troy Hunt, 17 January 2019.
- [23andMe fined £2.31 million for failing to protect UK users' genetic data](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/06/23andme-fined-for-failing-to-protect-uk-users-genetic-data/), Information Commissioner's Office (United Kingdom), 17 June 2025.
- [The SIM highjackers: how criminals are stealing millions by highjacking phone numbers](https://www.europol.europa.eu/media-press/newsroom/news/sim-highjackers-how-criminals-are-stealing-millions-highjacking-phone-numbers), Europol, 13 March 2020.
- [Notice of recent security incident](https://blog.lastpass.com/posts/notice-of-recent-security-incident), LastPass, 22 December 2022.
- [Password manager provider fined £1.2m by ICO for data breach](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/12/password-manager-provider-fined/), Information Commissioner's Office (United Kingdom), 11 December 2025.
- [KeePassXC security audits and certifications](https://keepassxc.org/audits/), KeePassXC, checked 29 October 2026.
- [EFF Dice-Generated Passphrases](https://www.eff.org/dice), Electronic Frontier Foundation, consulted in September 2026.

## Your checklist

- [ ] Check your email address on [Have I Been Pwned](https://haveibeenpwned.com/) (5 min)
- [ ] Install a password manager and create a passphrase of 6 random words (1 hour)
- [ ] Give your email a new unique password and turn on 2FA with an authenticator app, plus your 2 hardware keys if you bought them (1 hour)
- [ ] Move your 4 next most important accounts and remove SMS codes where possible (1 hour)
- [ ] Put your passphrase on paper in 1 safe place and your recovery codes in another, and tell 1 trusted person where (5 min)
