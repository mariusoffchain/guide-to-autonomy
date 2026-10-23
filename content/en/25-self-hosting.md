# Chapter 10: Hosting your own services

## In brief

"The cloud" is someone else's computer. Self-hosting means running some of your services, such as your files, your photos, your notes and later a Bitcoin node, on a small computer that you own and keep at home. Beginner-friendly platforms now make installing an app about as easy as on a phone, although backups, updates and remote access still ask for some reading and become your job. The sensible path is to start with 1 service, make it reliable, then grow.

## In someone else's cloud you are a tenant

When your files, photos and calendar live in a company's cloud, that company sets the rules. It can read what is not end-to-end encrypted, raise the price, close the product or lock your account through an automated decision, with a support form as your only recourse. It can also change the terms after you have moved in. Google Photos offered free unlimited storage for years, then announced in November 2020 that [every new photo would count toward a 15 GB limit](https://blog.google/products-and-platforms/products/photos/storage-changes/) from 1 June 2021.

Chapter 8 showed how to move to more respectful providers, which is already a big step, but you remain a tenant there too.

Self-hosting goes a step further, because the service runs on a machine in your home and the data sits on your disk. There is no account that a provider can suspend and no third party between you and your files.

It is not free, however. You pay for the hardware, the electricity and an off-site backup, you pay with your time, and you become the person responsible when something breaks.

## A server is a computer that stays on

A server is only a computer that stays on and answers requests from other devices, and a household does not need a data centre for that. An old laptop, a small mini PC or a Raspberry Pi is enough. A mini PC or a laptop with an SSD is usually the most comfortable start, and on a Raspberry Pi an SSD is preferable to a memory card, because cards tend to wear out quickly.

On that computer you install a **platform**, a system that gives you a web page with an app store. You open it from your browser, click "install" on Nextcloud or Immich, and the platform installs and manages the app. Some platforms use containers to isolate apps, but Linux containers share the host kernel and their security depends on configuration; they are not sealed security boxes.

Your phone and laptop then talk to this box instead of talking to a company. At home this happens over your own wifi, and from outside you need a safe way in, which has its own section below.

The technology is the smaller part of the change, since backups, updates and security are now yours.

## You become your own trusted third party

Self-hosting takes the company out of confidentiality, since nobody else holds the data, and it hands you the other properties. Availability now depends on your disk, your electricity and your backups, and the provider's engineers are replaced by whatever you remember to do. For a beginner, a well-run provider with end-to-end encryption can be the safer choice, and hosting a few services while renting the rest is a sound result.

Some third parties remain, and it helps to name them. The maker of the platform publishes the system updates and curates the app store, so a careless or malicious update would reach every server at once. Open source code, and the possibility to add another store or to install an app by hand, keep that party replaceable. For remote access, Tailscale's coordination server gives each of your devices the public keys of the others. Traffic contents remain encrypted between your devices, including when a relay carries them, but Tailscale's documentation [acknowledges](https://tailscale.com/kb/1226/tailnet-lock) that a malicious coordinator could insert a device into your network, and it offers Tailnet Lock, with which your own devices must sign any newcomer. Headscale or plain WireGuard remove that party, at the price of more configuration.

## Choose your platform

All of these are made for people who are not system administrators, and they differ in focus, licence and who stands behind them. The licence matters in a book that puts open source first. StartOS is published under the [MIT licence](https://github.com/Start9Labs/start-technologies/blob/master/LICENSE) and YunoHost is free software too, whereas umbrelOS uses the [PolyForm Noncommercial licence](https://github.com/getumbrel/umbrel/blob/master/LICENSE.md), which lets you read and modify the code for personal use but is not an open-source licence. Start9 and Umbrel both sell their own servers, and neither requires them, since both systems install free of charge on a computer you already own.

| Platform | Made by | Strength | Trade-off | Who controls apps and updates |
|---|---|---|---|---|
| **Start9 (StartOS)** | A single company, which also sells servers | Open source. Built around sovereignty, with Tor by default and encrypted backups built in | Smaller app catalogue, a little more to learn | Start9 for the system. 2 default registries, [others can be added](https://docs.start9.com/start-os/0.4.0.x/marketplace.html), and packages installed by hand |
| **YunoHost** | A volunteer community, non-profit | Open source, based on Debian, many apps, a single login for all of them | Designed for services reachable from the internet, so domains and email appear early. Plainer interface | Volunteers maintain the system and the catalogue. Any app can also be [installed from a URL](https://doc.yunohost.org/en/admin/apps/custom_apps/) |
| **Umbrel (umbrelOS)** | A single company, which also sells its own hardware | The most polished interface, large app store, strong Bitcoin and Lightning apps | The code is public, but the licence is not a true open-source licence (no commercial use) | Umbrel for the system and the official store. [Community app stores](https://umbrel.com/support/apps/how-to-add-a-community-app-store) can be added, without review by Umbrel |
| **CasaOS** | A single company (IceWhale) | Open source. A simple layer you add on top of an existing Linux system | In maintenance mode as of September 2026, because the company now focuses on its newer ZimaOS. No built-in backups | IceWhale for the layer and its store, which accepts other app sources. Your Linux distribution for the system |
| **Debian or Ubuntu with Docker** | You | Full control, you learn how everything really works, no platform to depend on | The command line, and nobody to blame. For the curious | Debian or Ubuntu for system packages, and the publisher of each container image you pull |

What to host first:

| App | Replaces | Note |
|---|---|---|
| **Nextcloud** | Cloud drive, calendar, contacts | The classic first app. Keep it simple, do not install every add-on |
| **Immich** | Cloud photo libraries | Automatic backup of phone photos. Moves fast, so read update notes |
| **Jellyfin** | Streaming your own films and music | Low risk, a good learning project |
| **Home Assistant** | Smart home clouds | Keeps your home devices local |
| **Vaultwarden** | The server side of a password manager | Works with the Bitwarden apps. Not a beginner's project, because a broken server without a tested backup can cost you every password. Wait until restores are routine |
| **A Bitcoin node** | Trusting someone else's node | Later. See chapter 18 |

A reasonable setup for most people is an open-source platform such as StartOS or YunoHost on a mini PC, with Nextcloud or Immich as the first app. umbrelOS is the most polished alternative if its licence suits you.

## Reaching it from outside, safely

A home router normally refuses connections that start from the internet, so a server behind it is not directly reachable from outside. That protection has known gaps, however. Many routers ship with UPnP turned on, a feature that allows any device or app on your network to open a port by itself, and with IPv6 each device can receive a public address that only the router's firewall keeps closed. It is worth opening the router settings to turn UPnP off and to confirm that the IPv6 firewall is on.

The classic mistake is to open a port on purpose so that your files are reachable from anywhere. It works, and it also shows your login page to every automated scanner on the internet.

Safer options, from most independent to most convenient:

- **A WireGuard VPN into your home.** Your phone opens an encrypted tunnel to your own network and behaves as if it were at home. Open source, nobody in the middle. It needs some router configuration, and CGNAT (a public address shared by several customers) can prevent a direct inbound connection unless you arrange another reachable endpoint or working IPv6. The 2 options below are often easier in that situation.
- **Tor onion services.** Umbrel and Start9 have this built in, so your server gets a private .onion address reachable through Tor, with no open port. Slower, but simple and private.
- **Tailscale.** Built on WireGuard and very easy to install on the server and on your phone. Your traffic stays encrypted between your devices, but a company coordinates the connections and the accounts. **Headscale** is an open-source replacement for that coordination part, which you host yourself.

Whatever you choose, change every default password first.

## Step by step

The example uses StartOS because it is open source and installs on ordinary hardware. The logic is the same on YunoHost and umbrelOS.

1. **Pick the hardware.** An unused laptop or a mini PC with 8 GB of memory and an SSD is plenty. Connect it to your router with a cable, not wifi.
2. **Install the platform.** Download the image from the project's website, write it to a USB stick, start the computer from it and follow the installer. When the project publishes a checksum (a fingerprint of the file), as Start9 does on its release page, compare it before you write the image, because this is the step that replaces trust in the download with verification. This erases the computer's disk.
3. **Create your account.** Open the address shown at the end of the installation from another device on the same network. Choose a long, unique password and store it in your password manager. If the platform offers two-factor authentication, as umbrelOS does in its settings, turn it on.
4. **Install 1 app.** Only 1. Nextcloud or Immich is a good start, so install the phone app, enter your server's address, and let it copy your photos.
5. **Set up backups.** Follow the 3-2-1 rule, which means 3 copies of your data, on 2 different devices, with 1 copy in another place. In practice that is the server, a second disk and an encrypted copy off-site (a disk at a relative's home, or an encrypted cloud backup). StartOS writes encrypted backups to an external disk or a network folder, and umbrelOS can [run them automatically every hour](https://umbrel.com/support/backups-and-recovery/backing-up-your-data). If your platform does not schedule them, add a recurring reminder to your calendar.
6. **Test a restore.** Recover 1 file from the backup, because a backup is only proven once something has come back from it.
7. **Keep it updated.** Review platform and app updates at least monthly, read release notes and keep backups current. Apply relevant security fixes promptly; do not wait for the monthly review when a known vulnerability affects your setup.
8. **Only then add a second app.** Live with the first one for a few weeks before you grow.

## Mistakes to avoid

- **Having no backups.** Disks fail without warning, and professional hosts are not immune. On 10 March 2021 a fire [destroyed the SBG2 datacentre of OVHcloud](https://corporate.ovhcloud.com/en/newsroom/news/informations-site-strasbourg/) in Strasbourg, about 120,000 services were affected, and customers without a copy elsewhere lost their data. At home the backup is your job, so set it up before you trust the server with anything you cannot lose.
- **Exposing services to the internet with default passwords.** Automated scanners find open services quickly. Use one of the safe routes above and unique passwords everywhere.
- **Hosting your email or your passwords as a first project.** Email is the hardest service to run, because large providers often reject mail from home servers and a mistake means lost messages. A password server that breaks without a tested backup locks you out of everything else. Use a good provider (chapters 2 and 4) and host other things first.
- **Making the family depend on it before it is stable.** Run it for yourself for 1 or 2 months. Move the family photos only when backups and updates have become routine.
- **Deleting the cloud copy too early.** Keep your old service in parallel until you have restored from your own backup at least once.
- **Installing 20 apps in the first week.** Each app is something more to update and to secure, and the ones you forget become the weak point of the server.

## Go further

- **Platforms:** start9.com, yunohost.org, umbrel.com, casaos.zimaspace.com.
- **A large catalogue of software you can host:** the awesome-selfhosted list (awesome-selfhosted.net).
- **Remote access:** wireguard.com, tailscale.com, and Headscale (headscale.net).
- **Next chapter:** AI without giving yourself away, where the same server can run a language model for the family. It comes back once more in chapter 18, as a Bitcoin node.

## Sources

- [Docker Engine security](https://docs.docker.com/engine/security/), Docker documentation, checked 22 October 2026.
- [Updating Google Photos' storage policy to build for the future](https://blog.google/products-and-platforms/products/photos/storage-changes/), Google, 11 November 2020.
- [Strasbourg datacentre: latest information](https://corporate.ovhcloud.com/en/newsroom/news/informations-site-strasbourg/), OVHcloud, 18 March 2021, updated until April 2021.
- [Umbrel licence (PolyForm Noncommercial 1.0.0)](https://github.com/getumbrel/umbrel/blob/master/LICENSE.md), Umbrel on GitHub, consulted in September 2026.
- [StartOS licence (MIT)](https://github.com/Start9Labs/start-technologies/blob/master/LICENSE), Start9 Labs on GitHub, consulted in September 2026.
- [Backing up your data](https://umbrel.com/support/backups-and-recovery/backing-up-your-data), umbrelOS Support, consulted in September 2026.
- [Tailnet Lock](https://tailscale.com/kb/1226/tailnet-lock), Tailscale documentation, consulted in September 2026.
- [Marketplace](https://docs.start9.com/start-os/0.4.0.x/marketplace.html), StartOS documentation, consulted in September 2026.
- [Adding a community app store](https://umbrel.com/support/apps/how-to-add-a-community-app-store), umbrelOS Support, consulted in September 2026.
- [Installing custom apps](https://doc.yunohost.org/en/admin/apps/custom_apps/), YunoHost documentation, consulted in September 2026.

## Your checklist

- [ ] Find a computer that can stay on, such as an old laptop, a mini PC or a Raspberry Pi (5 min)
- [ ] Install a platform and a first app (weekend)
- [ ] Set up automatic backups on a second disk, plus a copy off-site (1 hour)
- [ ] Restore a file from the backup to check that it works (5 min)
- [ ] Choose a safe way to reach it from outside, and change every default password (1 hour)
