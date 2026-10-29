# Chapter 8: Replacing Big Tech services, one at a time

## In brief

You do not leave Google, Apple, Meta or Microsoft in 1 day, and you do not have to. Export your data first, then replace 1 service, live with it for 2 weeks, and only then move to the next. For every need there are several credible alternatives, most of them open source and run by different operators. Each service you move reduces what a single company knows about you, and what you lose if that account is locked.

## A single account holds your whole digital life

Most digital lives run inside 1 or 2 companies, with mail, calendar, photos, documents, maps and videos under a single account. It is comfortable, and it creates 2 risks.

The first is the profile, because a company that sees your searches, your movements, your inbox and your photos knows more about you than any person does. The second is dependency, because if that account is locked (chapter 6), everything goes at the same moment.

In May 2025 the Associated Press reported that the chief prosecutor of the International Criminal Court had lost access to his Microsoft email account after US sanctions, although Microsoft says it never suspended its services to the court. In October 2025 the court [confirmed that it is replacing Microsoft Office with openDesk](https://www.theregister.com/2025/10/31/international_criminal_court_ditches_office/), an open source suite developed for the German state.

The usual reaction is a burst of motivation, "I delete everything today", and it almost always fails. Too many habits break at once, the family calendar stops working, a document cannot be found before a deadline, and 2 weeks later everything is back where it was, and the conclusion drawn is that alternatives do not work, when what failed was the attempt to change 10 habits at once.

## Export first, then 1 service at a time

The method rests on 3 ideas.

**Export first.** Article 20 of the [General Data Protection Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj), which applies since 25 May 2018, gives a right to portability for certain personal data you provided, when it is processed automatically on the basis of consent or a contract. It does not cover every record a provider holds. Covered data must be supplied in a structured, commonly used, machine-readable format. The big companies provide a tool for it: Google Takeout (takeout.google.com), Apple's "Data and Privacy" page (privacy.apple.com), and the "download your information" option in the account settings of Facebook and Instagram. The export takes hours or days to arrive. You keep your history whatever happens next, and you see how much they hold, which for many people is the moment the motivation becomes real.

**Pick 1 service.** There are 2 good ways to choose, either the one that knows the most about you (often mail, photos or search) or the easiest one (often maps, notes or search). If you hesitate, take the easiest, because an early success makes the next one simpler.

**Run both in parallel.** Use the new tool for 2 weeks while the old one still exists, and move the data and delete it there only once you have stopped opening the old one.

Then repeat. 1 new service every 1 or 2 months is a very good pace.

## A privacy brand is still 1 company

Moving from Google to a provider with "privacy" in its slogan changes the landlord and leaves the question intact, namely who can read your data, and what happens if that company fails, is sold or changes its terms. 3 tests help to answer it.

- **Can the provider read it?** With end-to-end encryption, the data is locked on your device and the provider stores something it cannot open. Without it, the content is protected only by the provider's promise and by the law of its country. Even with it, the provider sees some metadata and delivers the app that does the encrypting, which is why open source apps and published audits matter.
- **Can you leave?** An export in a standard format keeps any company replaceable.
- **Can someone else run it?** Software that you or an association can host (Nextcloud, CryptPad, Immich, PeerTube) does not depend on the survival of 1 operator, and local tools (Syncthing, Joplin, Obsidian, LibreOffice) keep the data on your own devices.

A well-run company with end-to-end encryption remains a reasonable choice for most readers, and often a safer one than a server that nobody maintains.

## Choose your replacements

The table is organised by need. "Open source" means the code is public and can be checked. "Self-hosted" means you, or someone you trust, must run a server (chapter 10). Everything else is ready to use.

No alternative is an exact copy of what it replaces. Some are better, some ask for a small compromise, and the notes say which. Try 2 options for the same need before you decide, since most are free or cheap to test.

Some names, Proton in particular, appear in several rows. Taking everything from a single provider is convenient, but it rebuilds the dependency you are leaving, so consider mixing operators.

| Need | Alternatives | Notes | Who can read your data |
|---|---|---|---|
| **Search** | See chapter 3 | The easiest first step, a single setting in your browser. | See chapter 3. |
| **Email and calendar** | See chapter 4 for email. Calendars: Proton Calendar, Tuta Calendar, Nextcloud | Proton and Tuta encrypt your calendar and publish the code of their apps. Each is a single company. Nextcloud is open source, self-hosted or rented from a provider of your choice. | Not Proton or Tuta, which [encrypt events end to end](https://proton.me/blog/protoncalendar-security-model). On Nextcloud, whoever runs the server can. |
| **Maps** | Organic Maps, CoMaps, OsmAnd, Magic Earth | All use OpenStreetMap data. Organic Maps, its community fork CoMaps, and OsmAnd (more detailed, more complex) are open source and work offline for free, without live traffic. Magic Earth is closed source and does offer live traffic, but as of September 2026 traffic and offline maps are part of its [paid Premium plan](https://www.magicearth.com/pricing). None has the shop reviews of Google Maps. | Offline search and routing run on the phone, without an account. Magic Earth's code cannot be checked. |
| **Cloud storage and sync** | Nextcloud, Proton Drive, Filen, Syncthing | Proton Drive and Filen are end-to-end encrypted, with open source apps, each run by a single company. For Nextcloud, see above. Syncthing is open source and has no cloud at all, because it syncs your own devices directly. It works best between computers. On Android, the official app was [discontinued in December 2024](https://forum.syncthing.net/t/discontinuing-syncthing-android/23002). A community version, Syncthing-Fork, continues on F-Droid and changed maintainer in 2025, so check its current state before you rely on it. On iPhone, only third-party apps exist. | Not Proton or Filen. A Nextcloud host can, unless you use client-side [end-to-end encrypted folders](https://nextcloud.com/encryption/). Server-side encryption alone does not hide files from the administrator. Syncthing [relays carry encrypted data](https://docs.syncthing.net/users/relaying.html). |
| **Documents** | CryptPad, LibreOffice, OnlyOffice | CryptPad offers encrypted online collaboration, is open source, and can be used on a public instance or hosted yourself. LibreOffice is open source and runs offline on your computer. OnlyOffice is open source, good with Microsoft formats, and often used inside Nextcloud. | Not a CryptPad host (documents are encrypted in your browser). LibreOffice files stay local. OnlyOffice depends on its host. |
| **Notes** | Standard Notes, Joplin, Notesnook, Obsidian | Standard Notes and Notesnook are open source and end-to-end encrypted by default. Standard Notes belongs to Proton. Joplin is open source and syncs through storage you choose, but its end-to-end encryption [is optional](https://joplinapp.org/help/apps/sync/e2ee/), so turn it on in the settings before the first sync. Obsidian is closed source, but your notes are plain text files on your own disk. | Not Standard Notes or Notesnook. Joplin's storage provider can, until encryption is on. Obsidian files stay local. |
| **Photos** | Ente Photos, Immich | Ente is end-to-end encrypted, open source, paid above a small free plan, and can be self-hosted. Immich is open source, self-hosted only, and the closest to the Google Photos experience. | Not Ente, whose [design is published](https://ente.io/architecture/). With Immich, whoever runs the server, which is normally you. |
| **Video** | NewPipe, FreeTube, Invidious, PeerTube | NewPipe (Android) and FreeTube (computer) play YouTube without an account or ads. Invidious does the same in a browser through public instances that often break. All 3 are open source and can stop working when YouTube changes something. PeerTube is different, an open source, federated network with its own videos. | YouTube still sees your IP address. An Invidious or PeerTube instance sees what you watch there. |
| **Translation** | LibreTranslate, the built-in translation of Firefox | LibreTranslate is open source and can be self-hosted. Firefox translates pages on your device. DeepL gives better quality but is closed source and receives your text, which is fine for a menu and not for a contract. | A LibreTranslate instance sees your text unless you host it. Firefox sends nothing. DeepL receives everything you type. |
| **App store on Android** | F-Droid, Obtainium, Aurora Store | F-Droid is a catalogue of open source apps only. See chapter 9. | Nobody reads data here. The question is who builds and signs the apps (chapter 9). |

A reasonable start for most people is **search, then maps, then notes**, because they need almost no migration. Mail and photos matter the most, and each deserves a calm weekend.

## Step by step

The example moves your photos, and the logic is the same for every row of the table.

1. **Export.** Request your full archive from the old service and store it on a disk you own. Check that the files open.
2. **Choose 1 service** from the table. Read its website, check who runs it, whether the code is open, whether the provider can read your data, and what it costs. This is the step that replaces trust in a brand with verification.
3. **Run both in parallel for 2 weeks.** Turn on the new photo backup on your phone and leave the old one on. Use the new app every time you want to look at a photo.
4. **Move the data.** Import your export into the new service. Most alternatives have an import tool or a guide for the big platforms.
5. **Change the default on every device,** meaning phone, tablet, computer, and the devices of anyone who shares the service with you. Turn off the old backup or sync.
6. **Delete the data from the old service,** once you have checked that the new copy is complete and that you have a backup of it. Be careful with photos. According to [Google's own help page](https://support.google.com/photos/answer/6128858/delete-or-restore-your-photos-amp-videos-android?co=GENIE.Platform%3DAndroid), deleting a backed-up photo in the Google Photos app also deletes the copy on your phone. To keep the phone copies, turn off backup on every device first and then delete from photos.google.com on a computer, or use "Undo backup" in the backup settings of the app, which removes the cloud copies and leaves the files on the device. With iCloud Photos, first [download the originals](https://support.apple.com/en-ie/102179), wait for the download to finish and verify the files, then turn off sync on the devices whose copies you want to keep before deleting cloud items. Deleted items stay in the trash for 30 days, which you can empty once you are sure.
7. **Pick the next one,** but not in the same week.

## Mistakes to avoid

- **Purism.** Replacing 7 services out of 10 is a large gain, and keeping YouTube or a work tool does not cancel the rest.
- **Moving everything at once.** It is the main reason people go back. Move 1 service, live with it for 2 weeks, then pick the next.
- **Forgetting the people you share with.** Shared albums, the family calendar and a shared shopping list all involve other people, so talk to them before you move, or keep that item where it is for now.
- **Trusting the word "privacy" in an advertisement.** Check the facts: is the code open, is the data encrypted so that the company cannot read it, is that encryption on by default, who owns the company, how does it earn money?
- **Deleting before verifying.** Open the new copy, count the albums, check the oldest and the newest files, and only then delete the original, in the way described in step 6.
- **Replacing a dependency with another.** If everything moves to a single new company, the dependency is the same with a better landlord. Spread your services across several operators.

## Go further

- **Detailed, independent recommendations:** Privacy Guides (privacyguides.org).
- **Alternatives listed by the service you want to replace:** switching.software.
- **Services based in Europe:** european-alternatives.eu.
- **Next chapter:** taking back control of your phone.

## Sources

- [Respect individuals' rights, including portability](https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_en), European Data Protection Board, checked 22 October 2026.
- [Server-side encryption and its limits](https://docs.nextcloud.com/server/32/admin_manual/configuration_files/encryption_configuration.html), Nextcloud Administration Manual, checked 22 October 2026.
- [Turn off iCloud Photos](https://support.apple.com/en-ie/102179), Apple Support, checked 22 October 2026.
- [International Criminal Court dumps Microsoft Office](https://www.theregister.com/2025/10/31/international_criminal_court_ditches_office/), The Register, 31 October 2025.
- [Regulation (EU) 2016/679, General Data Protection Regulation, Article 20](https://eur-lex.europa.eu/eli/reg/2016/679/oj), Official Journal of the European Union, 27 April 2016.
- [Discontinuing syncthing-android](https://forum.syncthing.net/t/discontinuing-syncthing-android/23002), Syncthing community forum, 20 October 2024.
- [Delete photos and videos](https://support.google.com/photos/answer/6128858/delete-or-restore-your-photos-amp-videos-android?co=GENIE.Platform%3DAndroid), Google Photos Help, checked 22 October 2026.
- [Magic Earth pricing](https://www.magicearth.com/pricing), Magic Earth, consulted in September 2026.
- [End-to-end encryption](https://joplinapp.org/help/apps/sync/e2ee/), Joplin documentation, consulted in September 2026.
- [The Proton Calendar security model](https://proton.me/blog/protoncalendar-security-model), Proton, consulted in September 2026.
- [Nextcloud encryption](https://nextcloud.com/encryption/), Nextcloud, consulted in September 2026.
- [Relaying](https://docs.syncthing.net/users/relaying.html), Syncthing documentation, consulted in September 2026.
- [Ente architecture](https://ente.io/architecture/), Ente, consulted in September 2026.

## Your checklist

- [ ] Request your data export from Google, Apple or Meta (5 min)
- [ ] Replace 1 easy service: search, maps or notes (5 min)
- [ ] Choose your first important service and run it in parallel for 2 weeks (1 hour)
- [ ] Move the data and change defaults; delete the old cloud copy only after verifying an independent backup and disabling sync on devices you want to keep (weekend)
- [ ] Write the next service to replace in your calendar, 1 month from now (5 min)
