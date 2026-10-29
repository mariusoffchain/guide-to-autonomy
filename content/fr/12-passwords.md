# Chapitre 2 : Vos mots de passe et vos comptes

## En bref {#in-brief}

La réutilisation des mots de passe reste l'une des façons les plus courantes de prendre le contrôle de comptes ordinaires, avec l'hameçonnage (phishing). Un gestionnaire de mots de passe crée et retient un mot de passe différent pour chaque site, et vous le protégez avec 1 seule passphrase solide. Un second facteur vient ensuite sur les comptes qui comptent, en commençant par votre email, car celui qui détient votre email peut réinitialiser presque tout le reste.

## Un mot de passe divulgué ouvre de nombreuses portes

En janvier 2019, le chercheur en sécurité Troy Hunt a trouvé un ensemble de fichiers qui circulaient sur un forum de pirates sous le nom de [Collection #1](https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/). Il contenait 773 millions d'adresses email uniques et plus de 21 millions de mots de passe uniques, assemblés à partir de milliers de fuites plus anciennes. Des attaquants donnent des listes comme celle-ci à des programmes qui essaient chaque couple adresse et mot de passe sur d'autres services, comme votre email, vos boutiques et vos réseaux sociaux, une technique appelée **credential stuffing** (bourrage d'identifiants).

Personne ne vous vise en particulier, la porte s'ouvre simplement partout où vous avez réutilisé un mot de passe divulgué. D'avril à septembre 2023, l'entreprise de tests génétiques 23andMe a été touchée exactement de cette manière. Le régulateur britannique [lui a infligé une amende de 2,31 millions de £ en juin 2025](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/06/23andme-fined-for-failing-to-protect-uk-users-genetic-data/), après l'exposition des données de 155 592 résidents du Royaume-Uni, et a relevé que l'entreprise n'exigeait pas de second facteur à la connexion.

Vous pouvez vérifier si votre propre adresse apparaît dans des fuites connues sur [Have I Been Pwned](https://haveibeenpwned.com/), le service gratuit que gère Troy Hunt. Les personnes en ligne depuis 10 ans en trouvent en général plusieurs. Le compte le plus important est votre email, puisque celui qui le contrôle peut cliquer sur « mot de passe oublié » sur presque tout ce que vous possédez d'autre.

## 1 seule passphrase, puis un second facteur

Un **gestionnaire de mots de passe** est un coffre chiffré qui crée un long mot de passe aléatoire pour chaque site, le retient et le saisit à votre place. Le coffre est chiffré sur votre propre appareil avant d'être synchronisé, de sorte qu'un fournisseur bien conçu n'est pas en mesure de le lire, et vous retenez 1 secret au lieu de 100. Ce secret doit être une **passphrase** de 6 mots aléatoires, choisis par exemple en lançant des dés sur une liste de mots (une méthode appelée diceware), difficile à deviner et bien plus facile à retenir que « xK9#qL2v ».

L'**authentification à 2 facteurs** (2FA) ajoute une étape après le mot de passe, quand le site demande quelque chose que vous possédez. Un code envoyé par SMS en est la forme faible, car un criminel peut convaincre votre opérateur de transférer votre numéro vers sa carte SIM, une attaque appelée SIM swap. En mars 2020, [Europol a annoncé l'arrestation de 12 personnes en Espagne](https://www.europol.europa.eu/media-press/newsroom/news/sim-highjackers-how-criminals-are-stealing-millions-highjacking-phone-numbers) qui avaient utilisé des cartes SIM dupliquées pour vider des comptes bancaires plus de 100 fois, pour un total supérieur à 3 millions d'euros.

Une application d'authentification est bien meilleure, et une clé de sécurité matérielle est l'option la plus solide. Les **passkeys** (clés d'accès) utilisent la même technologie que ces clés pour remplacer le mot de passe lui-même.

## Même à connaissance nulle, il reste un gardien du coffre

Le chiffrement garde confidentiel un coffre synchronisé, mais l'entreprise qui le stocke et qui diffuse vos mises à jour reste un tiers de confiance. Les fournisseurs disent que leur conception est à connaissance nulle, c'est-à-dire qu'ils détiennent le coffre sans la passphrase qui l'ouvre. En décembre 2022, LastPass [a confirmé qu'un attaquant avait copié une sauvegarde de coffres de clients](https://blog.lastpass.com/posts/notice-of-recent-security-incident). Les mots de passe et les notes étaient chiffrés, les adresses des sites ne l'étaient pas, et chaque coffre volé n'était aussi solide que le mot de passe principal de son propriétaire. Le régulateur britannique, qui [a infligé à l'entreprise une amende de 1,2 million de £ en décembre 2025](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/12/password-manager-provider-fined/) pour jusqu'à 1,6 million d'utilisateurs britanniques touchés, n'a trouvé aucune preuve que des mots de passe avaient été déchiffrés.

Les applications open source permettent à des experts de confronter cette affirmation au code, et les audits publiés apportent des éléments supplémentaires, comme la [certification de sécurité que l'agence française ANSSI a délivrée à KeePassXC](https://keepassxc.org/audits/) en novembre 2025, pour sa version 2.7.9. Un fichier local ou un serveur que vous hébergez supprime le gardien du coffre, et les sauvegardes, les mises à jour et la synchronisation deviennent alors votre affaire.

Les seconds facteurs ont eux aussi des tiers. Le site conserve le même secret que votre application d'authentification et un service de synchronisation peut en détenir une copie, alors qu'une clé matérielle vérifie aussi l'authenticité dans l'autre sens, en contrôlant quel site fait la demande.

## Choisir votre gestionnaire de mots de passe

Toutes les options ci-dessous valent bien mieux que la réutilisation des mots de passe, et elles diffèrent sur la personne qui détient votre coffre chiffré, sur le caractère public du code et sur la quantité de travail que vous acceptez.

| Gestionnaire | Open source | Où se trouve le coffre | En qui vous devez avoir confiance, et ce que vous pouvez vérifier | Coût | Compromis |
|---|---|---|---|---|---|
| **[Bitwarden](https://bitwarden.com/)** | Oui | Le cloud de Bitwarden, ou un serveur que vous hébergez | Bitwarden, pour le stockage et les mises à jour de l'application. Code public, audits tiers publiés chaque année. L'auto-hébergement supprime l'entreprise. | Gratuit, offre payante facultative | Le choix open source le plus simple, sur tous les appareils. Le service par défaut est exploité par 1 seule entreprise américaine. |
| **[KeePassXC](https://keepassxc.org/)** | Oui | Un fichier sur votre propre ordinateur | Aucun gardien du coffre. Vous vous fiez au code public de l'application, certifié par l'ANSSI en 2025 (version 2.7.9), et à vos propres sauvegardes. | Gratuit | Pas d'entreprise, pas de cloud, pas de compte. Vous gérez vous-même la synchronisation et les sauvegardes. Sur téléphone, utilisez des applications compatibles comme [KeePassDX](https://www.keepassdx.com/) (Android) ou [KeePassium](https://keepassium.com/) (iPhone). |
| **[Proton Pass](https://proton.me/pass)** | Oui | Le cloud de Proton (entreprise suisse) | Proton, pour le stockage et les mises à jour de l'application. Code de l'application public, audité par Cure53 en 2023. Pas d'auto-hébergement. | Gratuit, offre payante facultative | Inclut des alias d'email. Pratique si vous utilisez déjà Proton, mais concentre davantage de votre vie dans 1 seule entreprise. |
| **[1Password](https://1password.com/)** | Non, code fermé | Le cloud de 1Password (entreprise canadienne) | 1Password, pour le stockage, les mises à jour et le code lui-même. Elle publie des rapports d'audit, pas le code source. | Abonnement payant uniquement | Soigné, bon pour les familles, audité régulièrement. Le public ne peut pas inspecter le code. |
| **Intégré à votre navigateur ou à votre système** ([Google](https://passwords.google.com/), [Apple](https://support.apple.com/en-us/120758), [Firefox](https://www.firefox.com/en-US/features/password-manager/)) | Variable | Votre compte Google, Apple ou Mozilla | Google, Apple ou Mozilla, pour le stockage, les mises à jour et la récupération du compte. Seul le code de Firefox est entièrement public. | Gratuit | Déjà là, et bien mieux que rien. Vous lie à 1 seul navigateur ou écosystème, et n'est aussi sûr que ce compte principal. |

Une configuration raisonnable pour la plupart des gens est **Bitwarden ou Proton Pass** si vous voulez la synchronisation sans effort, ou **KeePassXC** si vous préférez qu'aucune entreprise ne détienne votre coffre, même chiffré.

## Choisir votre application d'authentification

Une application d'authentification affiche un code à 6 chiffres qui change toutes les 30 secondes. Le site et votre téléphone partagent un secret (le QR code que vous scannez 1 fois), et les 2 calculent le même code à partir de ce secret, même sans réseau, ce qui en fait le bon second facteur pour la plupart de vos comptes. Privilégiez une application open source qui vous permet de ressortir vos codes, car si les secrets ne se trouvent que sur 1 téléphone, un téléphone perdu ou cassé vous bloque partout à la fois. Votre gestionnaire de mots de passe peut souvent stocker aussi ces codes, ce qui est pratique mais place les 2 facteurs au même endroit.

| Application | Plateformes | Open source | Sauvegarde et synchronisation | Compromis |
|---|---|---|---|---|
| **[Aegis](https://getaegis.app/)** | Android uniquement | Oui | Coffre chiffré sur le téléphone. Vous exportez vous-même des sauvegardes chiffrées. | Pas de cloud ni de compte, donc aucun service de synchronisation à qui faire confiance. Les sauvegardes sont votre affaire, et il n'existe pas de version iPhone. |
| **[Ente Auth](https://ente.com/auth/)** | Android, iPhone, Windows, Mac, Linux, web | Oui | Synchronisation chiffrée de bout en bout facultative, qui nécessite un compte Ente. Fonctionne aussi hors ligne sans compte. | Vos codes sur tous vos appareils. La synchronisation dépend d'1 seule petite entreprise. |
| **[2FAS](https://2fas.com/)** | Android, iPhone, plus une extension de navigateur | Oui | Sauvegarde via votre compte Google Drive ou iCloud. | Simple. La sauvegarde n'est aussi sûre que ce compte Google ou Apple. |
| **[Proton Authenticator](https://proton.me/authenticator)** | Android, iPhone, Windows, Mac, Linux | Oui | Fonctionne sans compte. Synchronisation chiffrée de bout en bout facultative avec un compte Proton, plus export et import locaux. | Gratuit, lancé en juillet 2025, donc plus récent que les autres. Une autre partie de votre vie chez Proton si vous l'utilisez déjà. |

Une configuration raisonnable pour la plupart des gens est **Aegis** sur Android si vous acceptez de gérer les sauvegardes vous-même, ou **Ente Auth ou Proton Authenticator** si vous voulez vos codes sur plusieurs appareils. Quel que soit votre choix, testez l'export ou la sauvegarde 1 fois.

## Clés de sécurité matérielles

Une clé de sécurité matérielle est un outil d'une autre nature. Ce petit appareil physique, branché sur un port USB ou approché de votre téléphone (NFC), contient une clé privée conçue pour ne jamais en sortir, et s'appuie sur des standards ouverts appelés FIDO2 et WebAuthn. Lorsque vous vous connectez, la clé vérifie l'adresse réelle du site avant de répondre, et vous la touchez pour confirmer. Une fausse page de connexion n'en obtient rien, alors qu'un code d'application peut encore être saisi sur la mauvaise page par un utilisateur trompé. Les mêmes clés peuvent aussi stocker des **passkeys**.

Achetez-en 2 et enregistrez les 2 sur chaque compte, 1 pour votre porte-clés et 1 pour un endroit sûr. Tous les sites ne prennent pas en charge les clés, gardez donc une application d'authentification pour les sites qui ne les acceptent pas, et utilisez d'abord les clés pour les comptes qui comptent le plus, c'est-à-dire votre email, votre gestionnaire de mots de passe et votre compte principal Apple ou Google.

| Clé | Fabricant | Connexion | Open source | Compromis |
|---|---|---|---|---|
| **[YubiKey](https://www.yubico.com/)** | Yubico (Suède et États-Unis) | USB-A ou USB-C, NFC sur la plupart des modèles | Non, firmware fermé | La plus largement prise en charge et documentée. Le firmware ne peut être ni inspecté ni mis à jour. La série « Security Key », moins chère, suffit pour les connexions. |
| **[Nitrokey](https://www.nitrokey.com/)** | Nitrokey (Allemagne) | USB-A ou USB-C, NFC sur certains modèles | Oui, firmware et matériel | Le firmware peut être mis à jour. Moins de modèles, documentation moins soignée. |
| **[Token2](https://www.token2.com/)** | Token2 (Suisse) | USB-A ou USB-C, NFC sur la plupart des modèles | Partiellement. La partie FIDO2 du firmware est publique et a été examinée de façon indépendante en 2024, le reste est fermé | Clés moins chères. Moins connue. |
| **[OnlyKey](https://onlykey.io/)** | CryptoTrust (États-Unis) | USB uniquement, pas de NFC | Oui, firmware | Dispose de ses propres boutons de PIN et peut aussi saisir des mots de passe stockés. Plus encombrante, et plus complexe que ce dont un débutant a besoin. |

Une configuration raisonnable pour la plupart des gens est de 2 clés d'un des fabricants ci-dessus, plus une application d'authentification pour les sites qui n'acceptent pas les clés.

## Pas à pas {#step-by-step}

L'exemple utilise Bitwarden, car il est gratuit, open source et fonctionne sur tous les systèmes, et la même logique s'applique aux autres.

1. **Créez votre passphrase.** Lancez des dés sur [la liste de mots de l'EFF](https://www.eff.org/dice), ou utilisez le générateur de passphrases du gestionnaire, jusqu'à obtenir 6 mots (l'EFF recommande 6 au minimum). Écrivez-la sur papier et gardez ce papier en lieu sûr chez vous.
2. **Installez le gestionnaire** sur votre ordinateur (sous forme d'extension de navigateur) et sur votre téléphone, et créez votre compte avec cette passphrase. Si vous l'oubliez, vous pouvez perdre votre coffre. Bitwarden ne peut pas récupérer un mot de passe maître oublié. L'accès d'urgence, configuré à l'avance, est une voie distincte (étape 8).
3. **Commencez par votre email.** Connectez-vous à votre compte email, changez le mot de passe pour un mot de passe généré par le gestionnaire, et enregistrez-le dans le coffre.
4. **Déplacez 4 autres comptes :** votre compte principal Apple ou Google, votre banque ou application de paiement, votre principal réseau social, et toute boutique qui conserve votre carte. Le reste peut suivre au cours des semaines suivantes, à chaque fois que vous vous connectez quelque part.
5. **Activez le 2FA avec votre application d'authentification** sur ces 5 comptes, email en premier, et sur le gestionnaire de mots de passe lui-même. Dans les paramètres de sécurité de chaque compte, cherchez « validation en 2 étapes » ou « authentification à 2 facteurs » (two-step verification, two-factor authentication), puis scannez le QR code avec l'application et saisissez le code qu'elle affiche. Là où le site le permet, supprimez le SMS comme méthode.
6. **Enregistrez vos clés matérielles, si vous en avez choisi.** Dans les mêmes paramètres de sécurité, choisissez « clé de sécurité » (parfois « passkey »). Branchez ou approchez la première clé, touchez-la et donnez-lui un nom, puis recommencez aussitôt avec la seconde clé. Dès lors, la clé contrôle l'adresse du site à chaque connexion, à la place de vos yeux. Portez-en une sur vous et rangez l'autre en lieu sûr. Une fois que les 2 clés fonctionnent, votre moyen de reprendre l'accès est la clé de secours plus les codes de récupération (étape 7). Une application d'authentification laissée sur le même compte est une porte plus faible, car ses codes peuvent encore être volés par hameçonnage. Ne la retirez qu'après vous être connecté 1 fois avec la clé de secours.
7. **Enregistrez les codes de récupération, loin de la passphrase.** La plupart des sites vous donnent des codes à usage unique pour le jour où vous perdez votre téléphone ou vos clés. Votre gestionnaire de mots de passe en a un aussi, et il ne doit jamais être conservé uniquement dans le coffre qu'il ouvre. Imprimez-les et gardez-les dans un autre endroit que le papier de votre passphrase, par exemple la passphrase chez vous et les codes dans une enveloppe scellée chez un proche de confiance, afin que celui qui trouve 1 papier n'obtienne pas tout.
8. **Prévoyez un accès d'urgence.** Certains gestionnaires proposent une fonction d'accès d'urgence pour une personne de confiance (chez Bitwarden, elle fait partie de l'offre payante). Des instructions écrites pour votre famille, qui lui indiquent où se trouvent les 2 papiers, fonctionnent aussi.

## Erreurs à éviter {#mistakes-to-avoid}

- **Garder la passphrase uniquement dans votre tête.** La mémoire peut défaillir après une maladie, un accident ou de longues vacances. Une copie papier en lieu sûr n'est pas une faiblesse, tant que vos codes de récupération sont conservés ailleurs.
- **Laisser le SMS comme solution de repli.** Si le site accepte encore un code par SMS, un SIM swap fonctionne toujours. Supprimez-le donc partout où le site vous le permet.
- **N'avoir qu'1 application d'authentification ou qu'1 clé matérielle, sans sauvegarde.** Un téléphone perdu ou une clé perdue doit vous coûter un après-midi et non vos comptes, c'est pourquoi vous exportez vos codes et enregistrez 2 clés.
- **Stocker des mots de passe dans des notes, des tableurs ou des emails.** Ce ne sont pas des coffres chiffrés, et ce sont parmi les premiers endroits que regarde un intrus.
- **Saisir un code sur une page atteinte depuis un message.** Les codes d'application d'authentification peuvent aussi être hameçonnés. Si votre gestionnaire ne propose pas de remplir le mot de passe, vérifiez l'adresse, car vous êtes peut-être sur un faux site.
- **Essayer de tout changer en 1 seule soirée.** Commencez par les 5 comptes ci-dessus, puis déplacez les autres au cours des semaines suivantes, à chaque fois que vous vous connectez quelque part.

## Pour aller plus loin {#go-further}

- **Vérifier votre exposition :** [Have I Been Pwned](https://haveibeenpwned.com/).
- **Créer une passphrase avec des dés :** [les listes de mots de l'Electronic Frontier Foundation](https://www.eff.org/dice).
- **Comparer les outils en détail :** Privacy Guides, [« Password Managers »](https://www.privacyguides.org/en/passwords/), [« Multifactor Authentication »](https://www.privacyguides.org/en/multi-factor-authentication/) et [« Security Keys »](https://www.privacyguides.org/en/security-keys/).
- **Chapitre suivant :** votre navigateur et vos recherches.

## Sources {#sources}

- [Implementing phishing-resistant MFA](https://www.cisa.gov/sites/default/files/2023-01/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf), CISA, consulté le 22 octobre 2026.
- [Emergency access](https://bitwarden.com/help/emergency-access/), Bitwarden Help, consulté le 22 octobre 2026.
- [The 773 Million Record "Collection #1" Data Breach](https://www.troyhunt.com/the-773-million-record-collection-1-data-reach/), Troy Hunt, 17 janvier 2019.
- [23andMe fined £2.31 million for failing to protect UK users' genetic data](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/06/23andme-fined-for-failing-to-protect-uk-users-genetic-data/), Information Commissioner's Office (Royaume-Uni), 17 juin 2025.
- [The SIM highjackers: how criminals are stealing millions by highjacking phone numbers](https://www.europol.europa.eu/media-press/newsroom/news/sim-highjackers-how-criminals-are-stealing-millions-highjacking-phone-numbers), Europol, 13 mars 2020.
- [Notice of recent security incident](https://blog.lastpass.com/posts/notice-of-recent-security-incident), LastPass, 22 décembre 2022.
- [Password manager provider fined £1.2m by ICO for data breach](https://ico.org.uk/about-the-ico/media-centre/news-and-blogs/2025/12/password-manager-provider-fined/), Information Commissioner's Office (Royaume-Uni), 11 décembre 2025.
- [KeePassXC security audits and certifications](https://keepassxc.org/audits/), KeePassXC, consulté le 29 octobre 2026.
- [EFF Dice-Generated Passphrases](https://www.eff.org/dice), Electronic Frontier Foundation, consulté en septembre 2026.

## Votre checklist {#your-checklist}

- [ ] Vérifiez votre adresse email sur [Have I Been Pwned](https://haveibeenpwned.com/) (5 min)
- [ ] Installez un gestionnaire de mots de passe et créez une passphrase de 6 mots aléatoires (1 h)
- [ ] Donnez à votre email un nouveau mot de passe unique et activez le 2FA avec une application d'authentification, plus vos 2 clés matérielles si vous en avez acheté (1 h)
- [ ] Déplacez vos 4 comptes suivants les plus importants et supprimez les codes par SMS quand c'est possible (1 h)
- [ ] Mettez votre passphrase sur papier à 1 endroit sûr et vos codes de récupération à un autre, et dites à 1 personne de confiance où ils se trouvent (5 min)
