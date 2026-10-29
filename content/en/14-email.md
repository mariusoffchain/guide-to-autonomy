# Chapter 4: Your email and your aliases

## In brief

Your email address is the key to all your other accounts, and the label that links your profiles together across the internet. Move your mail to a provider that lives from subscriptions and not from advertising, and that can encrypt your mailbox so that the company itself is not able to read it. Then stop giving your real address to everyone and use aliases instead, with a different address for each service. You will see who leaks or sells your address, and you can switch off 1 alias without touching the rest.

## The address that links all your accounts

Almost every account you own can be reset by email, so whoever controls your mailbox can click "forgot password" on your bank, your social networks and your cloud storage. The mailbox is also an archive of your life, with invoices, tickets, medical appointments and years of conversations.

The most popular mailboxes are free because the company that carries your mail also runs an advertising business. Google [announced in June 2017](https://blog.google/products/gmail/g-suite-gains-traction-in-the-enterprise-g-suites-gmail-and-consumer-gmail-to-more-closely-align/) that it would stop scanning the content of consumer Gmail to personalise ads, but the mailbox remains tied to an account that can also hold your searches, your videos and your location history.

Then there is the address itself, which you give to shops, newsletters, apps and public offices. Because it never changes, data brokers can use it to join separate databases into a single profile of you. When one of those services is breached, the address ends up on lists used for spam and for phishing, meaning fake messages written to steal your passwords. In 2020, the hardware wallet maker Ledger [lost about 1 million customer email addresses](https://www.ledger.com/message-ledgers-ceo-data-leak) from its marketing database, along with the postal details of roughly 272,000 customers, and phishing campaigns by email and SMS followed.

## An encrypted mailbox and a different address everywhere

An **encrypted mail provider** stores your mailbox in a form the company cannot read. With Proton Mail and Tuta this is always on, and messages between 2 users of the same provider are end-to-end encrypted. With Mailbox.org and Posteo, you switch it on yourself.

A message sent to an ordinary Gmail or Outlook address is not end-to-end encrypted and stays readable there. Encryption protects the content, not the metadata (who writes to whom, and when), and a court can still compel a provider to hand over what it holds. In September 2021, Proton [confirmed that a Swiss order had obliged it to log the IP address](https://proton.me/blog/climate-activist-arrest) of a climate activist (the number that identifies an internet connection), while the content stayed out of reach. For private conversations, use a messenger from chapter 1.

An **alias** is a forwarding address such as shop-name@alias-service, created for a single shop. Its messages arrive in your mailbox and the shop never sees your real address. If that alias starts receiving spam, you know who leaked or sold it and you switch it off with 1 click. Brokers find it harder to join your accounts, because every service knows you under a different address.

## Who can read, forge or lock your mail

Email was designed without encryption or proof of the sender, so its confidentiality, authenticity and availability all depend on your provider. A message coming from an ordinary mailbox reaches the provider in readable form before it is encrypted for storage, so you rely on the company not to keep a copy, to ship honest apps and to keep your account open. An alias operator is a second third party of the same kind, since every forwarded message crosses its servers.

End-to-end encryption takes the provider out of the content only when both ends hold keys, inside 1 provider or with PGP between 2 of them. The provider then supplies the other person's key, as a messenger's directory does (chapter 1). Proton lets you [mark a contact's key as trusted](https://proton.me/support/address-verification), and Tuta [added key verification by QR code in August 2025](https://tuta.com/blog/key-verification). With PGP, you compare the key's fingerprint through another channel.

Availability is the property you can decentralise cheaply. With a domain you own, the provider becomes replaceable and the domain registrar becomes the party to watch. Running your own mail server is possible, but securing it and getting its messages accepted elsewhere make it a poor first project.

## Choose your mail provider

All the options below are funded by their users and not by advertising. They differ in price, in how they encrypt, and in whether you can use an ordinary mail app.

| Provider | Based in | Who you must trust | Price | Trade-offs |
|---|---|---|---|---|
| **[Proton Mail](https://proton.me/mail)** | Switzerland | Proton sees ordinary incoming mail before encrypting it, and supplies your contacts' keys. Trusted keys are an optional check. | Free tier, paid plans | Mailbox always encrypted. Open-source apps, large ecosystem (calendar, drive, VPN). Subject lines are not end-to-end encrypted. Ordinary mail apps need an extra "bridge" program on a paid plan. |
| **[Tuta](https://tuta.com/)** | Germany | Tuta sees ordinary incoming mail before encrypting it, and supplies your contacts' keys. Key verification is optional. | Free tier, paid plans | Mailbox always encrypted. Open-source apps, encrypts subject lines too. Uses its own encryption system, so no ordinary mail apps and no PGP (the older standard for encrypting email). |
| **[Mailbox.org](https://mailbox.org/en/)** | Germany | Mailbox.org can read stored mail until you turn on inbox encryption. With PGP, you verify keys yourself. | Paid, low price | Classic mailbox that works with any mail app. Encryption of your inbox (with PGP) is optional, and you switch it on yourself. Less polished on mobile. |
| **[Posteo](https://posteo.de/en)** | Germany | Posteo can read stored mail until you turn on encryption. With PGP, you verify keys yourself. | Paid, low price | Works with any mail app, can be paid anonymously, including cash by post. Encryption of your stored mail is optional, and you switch it on yourself. Does not support your own domain. |
| **Your own domain** | Wherever you host it | The same provider for content, plus your domain registrar. No provider can keep your address. | Yearly domain fee plus a paid mailbox | you@your-name.eu, hosted at one of the providers above. You can change provider later without changing address. You must never forget to renew the domain. |

A reasonable setup for most people is 1 mailbox from this list, with encryption switched on where it is optional, plus an alias service. If you plan to keep the same address for the next 20 years, consider your own domain from the start.

## Choose your alias service

An alias service sits between the world and your mailbox. It forwards your mail and can technically see the messages passing through, so pick an operator you trust as much as your mail provider.

| Service | Who runs it | Price | Trade-offs |
|---|---|---|---|
| **[SimpleLogin](https://simplelogin.io/)** | Proton (Switzerland) | Free tier with a limited number of aliases, paid for unlimited | Open source. You can also reply and send from an alias. Works with any mailbox, not only Proton. Included in some paid Proton plans. |
| **[Proton's built-in aliases](https://proton.me/pass/aliases)** ("hide-my-email") | Proton (Switzerland), using SimpleLogin technology | A limited number on the free and Mail Plus plans (10 as of September 2026), unlimited with Pass Plus or Proton Unlimited | Created directly inside Proton Mail or the Proton Pass password manager. Very convenient if your mailbox is at Proton. Your mailbox and your aliases are then in the hands of the same company, so if that account is lost or blocked, both go. |
| **[addy.io](https://addy.io/)** | A small independent operator | Generous free tier, paid plans | Open source, and you can host it yourself. A small team is also a single point of failure. |
| **[DuckDuckGo Email Protection](https://duckduckgo.com/email/)** | DuckDuckGo (United States) | Free | Very easy, removes trackers hidden in emails. Needs the DuckDuckGo app or browser extension. |
| **[Firefox Relay](https://relay.firefox.com/)** | Mozilla (United States) | Free tier with a few aliases, paid for more | Simple, integrated into Firefox. Few aliases on the free tier. |
| **Extra addresses at your mail provider** | Your mail provider | Usually in paid plans | Proton Mail, Tuta, Mailbox.org and Posteo all let you add a few more addresses to the same mailbox. Nothing new to trust, but the number is limited. |
| **"Plus addressing"** | Any provider | Free | you+shop@domain.com. Useful for sorting mail, weak for privacy, because your real address is visible inside it and the "+shop" part is easy to remove. |

A reasonable setup for most people is a dedicated alias service with a browser extension, so that creating an alias takes 1 click when you sign up somewhere. Choosing an operator different from your mail provider avoids depending on a single company for both.

## Disposable inboxes for one-time use

Some sites you will never visit again, such as a one-time download, a wifi portal or a forum you read once, and for these a disposable inbox is enough. There is no sign-up. You invent an address on the spot, type it into the form, then open the inbox on the service's website to read the message.

On public services of this kind there is no password, so anyone who guesses or knows the address can read the inbox. Messages are deleted quickly, you cannot count on finding them later, and many websites refuse these domains. A disposable inbox is therefore fine for a verification code that protects nothing important. It is the wrong tool for an account you want to keep, for anything that contains personal data, or wherever a password reset could be sent later, because whoever types the same address would receive it. For everything else, an alias does the job better.

| Service | How you get an address | How long mail is kept | Trade-offs |
|---|---|---|---|
| **[Mailinator](https://www.mailinator.com/)** | Invent any name at its public domain | A few hours | Fully public, so anyone who types the same name reads the same inbox. Receive only. Built mainly for software testers, with paid private plans. Widely blocked. |
| **[Guerrilla Mail](https://www.guerrillamail.com/)** | A random address is given to you, or you choose one | 1 hour | No password, so the inbox is protected only by how hard its name is to guess. Offers a "scrambled" address to make guessing harder. |
| **[Maildrop](https://maildrop.cc/)** | Invent any name at its public domain | At most 10 messages, cleared after 24 hours without new mail | Fully public, no password. Attachments are removed. |

## When a site demands a phone number

Your phone number is an even stronger identifier than your email address. You keep it for years, it links your accounts together, it attracts spam calls, and it is the target of SIM-swap attacks (chapter 2). First check whether the field is truly mandatory. When it is, you have several options, none of them perfect.

| Option | How it works | Trade-offs |
|---|---|---|
| **A second SIM or eSIM, used only for sign-ups** | A real mobile number from an ordinary operator, kept apart from your personal one | Accepted everywhere. Prepaid numbers expire if you do not top them up. In 2025, [19 of the 28 European countries studied by Cullen International](https://www.cullen-international.com/news/2025/10/19-EU-countries-mandate-the-registration-of-prepaid-customers.html) required operators to register the identity of prepaid customers. The rules vary, and this option separates your numbers without making you anonymous. |
| **Virtual (VoIP) number apps:** [JMP.chat](https://jmp.chat/), [Hushed](https://hushed.com/), [MySudo](https://mysudo.com/) | A paid number that works over the internet, inside an app | JMP.chat is open source but offers only US and Canadian numbers. Hushed (closed source) offers US, Canadian and UK numbers. MySudo (closed source) can be installed in only a few countries, so check before you count on it. Many services refuse VoIP numbers, and a European site may refuse a foreign one. |
| **A data eSIM paid in bitcoin,** for example [Silent.link](https://silent.link/) | No account. Some plans include a US or UK mobile number that can receive SMS | Costs more than an ordinary SIM. The number is leased by the year, and it is gone if you do not renew it. A single small operator. |
| **Paid one-time SMS reception services** | You rent a number for a few minutes to receive a single code | The number then goes to someone else, who could use it to take over the account. Quality varies widely, and many sites forbid this in their terms. |
| **Free public "receive SMS online" websites** | Shared numbers whose incoming messages are displayed on a web page | Everyone sees your code. The numbers are recycled and mostly blocked already. Only for something that does not matter at all. |

These options have limits too. If you lose access to the number, you can lose the account, so never use a number you do not control for your bank, for two-factor authentication or for any important account. Respect the terms of service of the site and the law of your country. The goal is simply to avoid handing your personal number to every shop and app.

## Step by step

The example uses Proton Mail for the mailbox and SimpleLogin for the aliases, because they are a common first step. Both belong to Proton, which is convenient but means your mailbox and your aliases depend on a single company. If you prefer to spread the risk, keep the mailbox and choose addy.io for the aliases, or keep SimpleLogin and choose another mailbox, since the steps are the same.

1. **Open the new mailbox.** Choose an address you can keep for years. Protect it with a long, unique password from your password manager and a second factor (chapter 2). Enable the recovery phrase and write it on paper. It restores both your access and your encrypted mail. A reset by email or SMS only gives back access, and your old messages may stay unreadable. Check [the provider's recovery instructions](https://proton.me/support/set-account-recovery-methods) before you rely on it.
2. **Set up the alias service.** Create the account, connect it to your new mailbox, and install its browser extension (and its phone app, if it has one).
3. **Move your most important accounts first.** These are your bank, government services, your phone operator, your Apple or Google account and your password manager. Change the email address in each of them. Use your real new address or a dedicated alias, as you prefer, but note your choice in your password manager.
4. **Forward the old mailbox.** In the settings of your old mailbox, turn on automatic forwarding to the new one. Most encrypted providers also offer an import tool that copies your old messages and contacts.
5. **Move the rest as it comes.** Each time a forwarded message arrives from a service you still use, change the address there to a new alias. Delete accounts you no longer use.
6. **Create a new alias for every signup.** A shop, a newsletter or a wifi portal each gets its own address. Name the alias after the service, so that a leak is easy to trace.
7. **Keep the old address for at least a year.** Do not delete it, because forgotten accounts, old contacts and password resets will keep arriving there for a long time.

## Mistakes to avoid

- **Thinking an encrypted provider makes all your email private.** It protects your mailbox, while a message sent to an ordinary mailbox stays readable at the other end.
- **Deleting the old address too early.** Some providers recycle abandoned addresses, and a stranger could then receive the password resets of accounts you forgot.
- **Losing the recovery phrase.** Without it, a forgotten password can cost you your old messages (step 1).
- **Letting your own domain expire.** Whoever registers it after you receives your mail and can reset your accounts. Turn on automatic renewal and keep the payment card up to date.
- **Using the same alias for everything.** An alias shared between 10 services is just a second real address, since the value comes from having a different alias for each service.
- **Putting the bank behind an alias service you do not fully trust.** For the few accounts that matter most, your real address at your own provider is a perfectly good choice.

## Go further

- **Compare providers in detail:** Privacy Guides, ["Email Services"](https://www.privacyguides.org/en/email/) and ["Email Aliasing"](https://www.privacyguides.org/en/email-aliasing/).
- **Check whether your address has already leaked:** [Have I Been Pwned](https://haveibeenpwned.com/).
- **Next chapter:** your network.

## Sources

- [Proton Account recovery explained](https://proton.me/support/set-account-recovery-methods), Proton Support, checked 22 October 2026.
- [As G Suite gains traction in the enterprise, G Suite's Gmail and consumer Gmail to more closely align](https://blog.google/products/gmail/g-suite-gains-traction-in-the-enterprise-g-suites-gmail-and-consumer-gmail-to-more-closely-align/), Google, 23 June 2017.
- [Message by Ledger's CEO: update on the July data breach](https://www.ledger.com/message-ledgers-ceo-data-leak), Ledger, 21 December 2020.
- [Important clarifications regarding arrest of climate activist](https://proton.me/blog/climate-activist-arrest), Proton, 6 September 2021.
- [Address verification with trusted keys](https://proton.me/support/address-verification), Proton, consulted in September 2026.
- [Tuta introduces key verification](https://tuta.com/blog/key-verification), Tuta, 26 August 2025.
- [19 EU countries mandate the registration of prepaid customers](https://www.cullen-international.com/news/2025/10/19-EU-countries-mandate-the-registration-of-prepaid-customers.html), Cullen International, 8 October 2025, checked 29 October 2026.

## Your checklist

- [ ] Open a mailbox at a provider funded by its users (1 hour)
- [ ] Set up an alias service and its browser extension (1 hour)
- [ ] Create your first alias and use it for your next signup (5 min)
- [ ] Move your 5 most important accounts to the new address (1 hour)
- [ ] Forward the old mailbox and move the remaining accounts (weekend)
