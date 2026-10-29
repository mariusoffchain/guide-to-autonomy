# Chapitre 9 : Reprendre le contrôle de votre téléphone

## En bref {#in-brief}

Votre téléphone en sait plus sur vous que n'importe quel autre objet que vous possédez. Vous pouvez réduire le partage inutile de données en 1 soirée, sur le téléphone que vous avez déjà, sans rien installer. Il s'agit des autorisations, de l'identifiant publicitaire, de la localisation, de l'écran de verrouillage, du code PIN de la carte SIM et des mises à jour. C'est le niveau 1, et il suffit à la plupart des gens. Le niveau 2 s'adresse aux curieux, avec des boutiques d'apps alternatives et des systèmes Android qui fonctionnent sans Google.

## Un capteur qui rend des comptes à de nombreuses entreprises

Votre téléphone est le capteur le plus complet que vous possédez. Il sait où vous dormez et où vous travaillez, il contient vos contacts, vos photos, vos paiements et souvent vos données de santé, et il transporte un micro et une caméra partout où vous allez.

Une app de lampe torche n'a pas besoin de vos contacts et un jeu n'a pas besoin de votre localisation précise, pourtant beaucoup les demandent quand même, car les données peuvent être vendues, et de nombreuses apps gratuites contiennent du code publicitaire qui rend compte aux mêmes quelques entreprises. En janvier 2025, le courtier en données de localisation Gravy Analytics a été piraté, et [les fichiers volés](https://www.theregister.com/2025/02/06/gravy_analytics_data_breach_suit/) contenaient les coordonnées de dizaines de millions de téléphones, dont certains en Europe, collectées par des apps populaires comme Tinder, Candy Crush et MyFitnessPal.

Pour relier ces signalements, votre téléphone porte un **identifiant publicitaire**, un numéro partagé avec chaque app afin que ce que vous faites dans une app puisse être relié à ce que vous faites dans une autre. En avril 2021, l'organisation noyb [a déposé une plainte en France](https://noyb.eu/en/buy-phone-get-tracker-unauthorized-tracking-code-illegally-installed-android-phones), en soutenant qu'Android crée cet identifiant sans demander de consentement.

Enfin, 2 entreprises, Google et Apple, contrôlent presque tous les téléphones, du système à la boutique d'apps et aux services par défaut.

## 4 leviers qui sont entre vos mains

Presque tout dans ce chapitre se ramène à 4 idées.

- **Les autorisations.** Une app ne peut pas accéder à votre localisation, à votre caméra, à votre micro, à vos contacts ou à vos photos si le système ne l'autorise pas. C'est vous qui l'accordez, et vous pouvez la reprendre à tout moment, ce qui en fait votre levier le plus fort.
- **L'identifiant publicitaire.** C'est un réglage. Vous pouvez le réinitialiser, et sur les téléphones actuels vous pouvez le supprimer ou refuser entièrement le suivi.
- **La boutique d'apps comme gardienne.** La boutique décide des apps qui existent pour vous, exige un compte, et sait tout ce que vous installez. Sur Android, vous pouvez installer des apps depuis d'autres sources, dans des conditions qui évoluent (voir le niveau 2). Sur iPhone, c'est beaucoup plus restreint, même dans l'Union européenne.
- **Le système face aux services.** Android lui-même est open source. Ce que la plupart des gens appellent « Android » est ce système plus les apps et les services de Google, qui s'exécutent avec des privilèges élevés. Les 2 peuvent être séparés, et c'est ce que font les systèmes alternatifs. iOS ne peut pas être séparé d'Apple, mais une bonne partie de ce qu'il envoie à iCloud peut être désactivée ou chiffrée.

## Niveau 1, durcir le téléphone que vous avez

Le niveau 1 fonctionne sur n'importe quel téléphone, Android ou iPhone, et peut commencer dès aujourd'hui. Il utilise des réglages que Google et Apple fournissent déjà, sans nouvelle app à installer. Restreindre les autorisations peut affecter certaines fonctions des apps, testez donc les changements et ne rétablissez que ce dont vous avez besoin. Ces réglages couvrent les 2 premiers leviers ci-dessus, les autorisations et l'identifiant publicitaire, ainsi que l'écran de verrouillage, la carte SIM et les mises à jour.

Comptez 1 soirée pour toute la liste. La revue des autorisations est la partie la plus longue, puisqu'il faut regarder chaque app une fois, et les autres étapes prennent quelques minutes chacune. Rien ici n'est permanent, donc une app qui cesse de fonctionner parce qu'elle avait vraiment besoin d'une autorisation la demandera à nouveau, et vous pourrez alors l'accorder.

Le niveau 1 a une limite qu'il vaut mieux connaître. Google ou Apple restent dans le tableau, avec leur boutique, leur compte et leurs services, et les apps que vous gardez voient toujours ce que vous leur permettez de voir. Pour la plupart des gens, c'est un endroit raisonnable pour s'arrêter. Les étapes suivent immédiatement, et le niveau 2 vient après pour les lecteurs qui veulent aller plus loin.

## Pas à pas {#step-by-step}

Ce sont les étapes du niveau 1, sur le téléphone que vous avez. Les noms de menus varient selon les marques et les versions, utilisez donc la barre de recherche des réglages si vous n'en trouvez pas un.

1. **Retirez ce que vous n'utilisez pas.** Parcourez vos apps et désinstallez toutes celles que vous n'avez pas ouvertes depuis des mois. Supprimer une app arrête son activité locale, mais n'efface pas les données que son fournisseur détient déjà.
2. **Faites l'audit des autorisations.** Sur Android, ouvrez Paramètres (Settings), Confidentialité (Privacy), Gestionnaire d'autorisations (Permission manager). Sur iPhone, ouvrez Réglages (Settings), Confidentialité et sécurité (Privacy & Security). Passez en revue Localisation (Location), Micro (Microphone), Appareil photo (Camera), Contacts et Photos, et demandez-vous pour chaque app si elle en a vraiment besoin. En cas de doute, refusez, car l'app le redemandera si c'est important. C'est l'étape qui remplace la confiance dans ce qu'une app dit d'elle-même par une vérification de ce à quoi elle peut accéder.
3. **Limitez la localisation.** Choisissez « Pendant l'utilisation de l'app » (While using the app) plutôt que « Toujours » (Always), et désactivez la localisation précise pour tout sauf les cartes et la navigation. Une app météo n'a besoin que de votre ville.
4. **Supprimez l'identifiant publicitaire.** Sur Android, dans les paramètres de confidentialité ou de Google, ouvrez Publicités (Ads) et choisissez « Supprimer l'identifiant publicitaire » (Delete advertising ID). Sur iPhone, ouvrez Réglages, Confidentialité et sécurité, Suivi (Tracking), et désactivez « Autoriser les demandes de suivi des apps » (Allow Apps to Request to Track).
5. **Renforcez le verrouillage.** Utilisez un code PIN d'au moins 6 chiffres, ou une passphrase. Gardez le déverrouillage par empreinte ou par visage pour le confort si vous le souhaitez, mais le PIN est la vraie clé. Masquez le contenu des notifications sur l'écran de verrouillage.
6. **Définissez un code PIN de carte SIM.** Il se trouve dans les paramètres de la carte SIM ou du réseau mobile. Une carte SIM volée et placée dans un autre téléphone ne peut alors recevoir ni vos appels ni vos SMS de codes sans ce PIN. Cherchez d'abord le PIN par défaut de votre opérateur et la procédure de récupération par code PUK, car 3 tentatives erronées de PIN bloquent la carte. Cela protège la carte SIM physique, mais pas contre un SIM swap autorisé par l'opérateur.
7. **Activez les mises à jour automatiques,** pour le système et pour les apps. La plupart des attaques utilisent des failles déjà corrigées.
8. **Sur iPhone, chiffrez iCloud.** Ouvrez Réglages, votre nom, iCloud, Protection avancée des données (Advanced Data Protection). Vos sauvegardes, vos photos et vos notes deviennent chiffrées de bout en bout. Vous devez définir un contact de récupération ou une clé de récupération, car Apple ne peut plus vous aider à reprendre l'accès. Écrivez la clé de récupération sur papier et gardez-la en 2 endroits, comme au chapitre 6. En octobre 2026, l'option est disponible dans l'Union européenne, mais pas au Royaume-Uni, où [Apple l'a retirée en février 2025](https://support.apple.com/en-us/122234). Si vous courez un risque réel d'attaques ciblées (journaliste, militant, personnalité publique), regardez aussi le mode de verrouillage renforcé (Lockdown Mode) dans Confidentialité et sécurité.

## Niveau 2, changer de boutique ou de système

Le niveau 2 agit sur les 2 derniers leviers, la boutique d'apps et la séparation entre le système et les services de Google. Il se présente en 2 étapes indépendantes l'une de l'autre. Sur Android, vous pouvez ajouter une autre source d'apps à côté de Google Play, ou à sa place, ce qui prend environ 1 heure et peut être annulé. Vous pouvez aussi remplacer tout le système par une version d'Android qui fonctionne sans Google, ce qui prend un week-end, efface le téléphone et ne fonctionne que sur certains modèles. Sur iPhone, le système ne peut pas être remplacé et les boutiques alternatives restent beaucoup plus restreintes, de sorte que le niveau 1 avec la Protection avancée des données est en pratique la limite.

Le prix est le confort, et parfois une app qui refuse de fonctionner. Les 3 parties ci-dessous traitent de la confiance que vous accordez une fois que vous quittez la voie officielle, du choix des systèmes et des sources d'apps, et de ce qui peut casser, en commençant par les apps bancaires. Les faits des 2 tableaux sont valables en septembre 2026 et évoluent vite.

### Quelqu'un signe chaque mise à jour que vous installez

Sur un téléphone, l'authenticité est une affaire de signatures. Le système ne démarre que s'il est signé avec une clé que le matériel accepte, un mécanisme qu'Android appelle le [démarrage vérifié](https://source.android.com/docs/security/features/verifiedboot) (verified boot), et une mise à jour d'app n'est installée que si elle porte la même signature de développeur que la version déjà présente sur le téléphone. Les tiers de confiance sont donc le fabricant du système, qui peut pousser une mise à jour vers chaque téléphone, et la boutique d'apps, qui décide de ce qui est listé et de ce qui est retiré, et qui sait ce que chaque compte a installé.

Quitter la boutique officielle déplace cette confiance sans la supprimer. F-Droid compile chaque app à partir de son code source public et signe la plupart d'entre elles avec sa propre clé, vous faites donc confiance à F-Droid à la place de chaque développeur. Pour une partie de son catalogue, il s'appuie sur des [compilations reproductibles](https://f-droid.org/docs/Reproducible_Builds/), où n'importe qui peut recompiler l'app et obtenir exactement le même fichier, et l'app conserve alors la signature de son développeur. Un fichier téléchargé depuis un site web n'a aucun relecteur, de sorte que l'adresse et la 1re installation portent tout le risque, et pour un débutant la boutique officielle est souvent plus sûre qu'un téléchargement fait sans précaution.

### Choisissez votre système et votre source d'apps

Le 1er tableau compare les systèmes, en commençant par celui que vous avez déjà après le niveau 1, et le 2e compare les sources d'apps sur Android. Dans les 2, la dernière colonne indique qui signe ce que vous installez.

| Système | Fonctionne sur | Point fort | Contrepartie | Qui signe vos mises à jour |
|---|---|---|---|---|
| **Android ou iOS d'origine, durci** | Votre téléphone actuel | Réglages familiers, restrictions réversibles | Google ou Apple restent dans le tableau | Apple, ou Google et le fabricant du téléphone. Le démarrage vérifié est activé |
| **GrapheneOS** | Les téléphones Google Pixel compatibles figurant sur la [liste de prise en charge tenue à jour](https://grapheneos.org/faq). Vérifiez la durée de prise en charge de sécurité restante avant d'acheter, car le plus ancien modèle pris en charge peut n'avoir plus beaucoup de temps devant lui. Un partenariat avec Motorola a été [annoncé en mars 2026](https://9to5google.com/2026/03/01/motorola-confirms-grapheneos-partnership-for-a-future-smartphone-porting-features/) pour de futurs modèles. GrapheneOS [attend les premiers en 2027](https://www.techrepublic.com/article/news-motorola-grapheneos-partnership-2027/), et aucun téléphone Motorola actuel n'est pris en charge | La sécurité la plus forte. Google Play est facultatif et fonctionne comme une app ordinaire, sans privilèges particuliers | Vous devez acheter un Pixel pour le moment. Certaines apps refusent de fonctionner | Le projet GrapheneOS. Le bootloader (chargeur de démarrage) est reverrouillé, et son [app Auditor](https://attestation.app/about) permet à un 2e téléphone de vérifier le système |
| **CalyxOS** | Pixels, certains modèles Fairphone et Motorola, SHIFTphone 8 | Un démarrage plus doux, utilise microG (un remplaçant open source des services Google) | Les mises à jour de sécurité se sont arrêtées en août 2025, et le projet a alors conseillé aux utilisateurs de partir. Les versions ont [repris le 1er juillet 2026](https://calyxos.org/news/2026/07/01/calyxos-official-release-is-back/). Vérifiez le rythme des versions sur calyxos.org avant de le choisir | Le Calyx Institute, une organisation à but non lucratif américaine. Le bootloader est reverrouillé, le démarrage vérifié reste donc activé |
| **LineageOS** | Des centaines de modèles, y compris des plus anciens | Offre une 2e vie aux vieux téléphones | La sécurité dépend de l'appareil et de son mainteneur bénévole. Pas de Google par défaut | Le projet et le mainteneur bénévole de votre modèle. Le bootloader [reste généralement déverrouillé](https://wiki.lineageos.org/faq), le démarrage vérifié est donc désactivé |
| **/e/OS (Murena)** | De nombreux modèles, vendus aussi préinstallés | Aucune installation nécessaire si vous en achetez un. Fabriqué par une entreprise européenne | Les mises à jour de sécurité peuvent arriver plus tard que sur les autres | Murena et la e Foundation. Le bootloader ne peut être reverrouillé que sur certains modèles |

| Source d'apps | Ce que c'est | Contrepartie | À qui vous devez faire confiance |
|---|---|---|---|
| **F-Droid** | Catalogue d'apps open source uniquement, sans compte | Les mises à jour peuvent être lentes. Choix plus restreint | F-Droid, qui compile et signe lui-même la plupart des apps. Les compilations reproductibles conservent la signature du développeur |
| **Aurora Store** | Client open source pour Google Play, utilisable sans votre propre compte Google | Apps gratuites uniquement en mode anonyme. Non approuvé par Google, peut cesser de fonctionner | Les serveurs de Google et la signature de chaque développeur, comme dans Google Play, plus les comptes partagés d'Aurora |
| **Obtainium** | Récupère les mises à jour directement depuis la page de publication du développeur | Vous décidez à qui faire confiance. Aucune vérification intermédiaire | Chaque développeur, et la page que vous avez ajoutée. Android vérifie seulement que les mises à jour correspondent à la 1re signature |
| **Accrescent** | Boutique axée sur la sécurité | Catalogue très restreint | Chaque développeur, qui signe ses propres apps. Des [métadonnées signées](https://accrescent.app/features) fixent la bonne clé dès la 1re installation |

Les règles d'installation d'apps hors de Google Play changent. Avec son [programme de vérification des développeurs](https://android-developers.googleblog.com/2026/06/android-developer-verification.html), Google exige que les apps installées sur des téléphones Android certifiés proviennent d'un développeur qui a enregistré une identité auprès de Google. Il a démarré le 30 septembre 2026 au Brésil, en Indonésie, à Singapour et en Thaïlande, et Google prévoit de l'étendre au monde entier en 2027, donc rien ne change en Europe pour le moment. Les apps de développeurs non enregistrés peuvent toujours être installées par un [« parcours avancé »](https://developer.android.com/developer-verification/guides) (advanced flow) comportant des étapes de confirmation supplémentaires, que Google a lancé en août 2026. F-Droid [considère le programme comme une menace](https://f-droid.org/2025/09/29/google-developer-registration-decree.html) pour son catalogue. Les systèmes alternatifs comme GrapheneOS ne sont pas des appareils certifiés et ne l'appliquent pas.

Un parcours raisonnable pour la plupart des gens consiste à faire le niveau 1 maintenant, à ajouter F-Droid si vous utilisez Android, et à envisager un autre système au prochain changement de téléphone.

### Les apps bancaires et les autres choses qui peuvent casser

Soyez lucide là-dessus avant de remplacer le système. Certaines apps vérifient si le téléphone est certifié par Google et refusent de fonctionner s'il ne l'est pas. Les apps bancaires, les apps de paiement, certaines apps administratives et d'identité, et quelques jeux sont les cas habituels. Le paiement sans contact avec Google Wallet ne fonctionne pas sur les systèmes alternatifs.

De nombreuses apps bancaires fonctionnent, surtout sur GrapheneOS avec Google Play installé comme app ordinaire. Cependant, personne ne peut le promettre pour votre banque, et une mise à jour peut changer la situation.

Les gens s'y prennent de plusieurs façons.

- Ils consultent les listes de compatibilité communautaires pour leur banque avant de changer.
- Ils utilisent le site web de la banque et une carte physique à la place de l'app.
- Ils gardent un 2e téléphone avec le système d'origine, à la maison et en Wi-Fi, uniquement pour la banque et les apps officielles. Il doit s'agir d'un modèle qui reçoit encore des mises à jour de sécurité, car un vieux téléphone qui n'en reçoit plus est un mauvais endroit pour une app bancaire.
- Ils choisissent une banque dont l'app fonctionne.

## Erreurs à éviter {#mistakes-to-avoid}

- **Tout accorder pendant l'installation.** C'est le moment où vous faites le moins attention. Refusez d'abord, autorisez plus tard si quelque chose ne fonctionne pas.
- **Ne compter que sur votre empreinte ou votre visage.** La biométrie est pratique, mais quelqu'un peut tenir le téléphone devant votre visage. Les 2 systèmes peuvent désactiver la biométrie jusqu'à la prochaine saisie du PIN. Sur iPhone, maintenez le bouton latéral et un bouton de volume pendant quelques secondes. Sur Android, utilisez l'option de verrouillage renforcé (Lockdown) du menu d'alimentation.
- **Installer un système alternatif sur votre unique téléphone la veille d'un voyage.** Testez d'abord, avec vos apps bancaires et de billets, idéalement sur un 2e appareil.
- **Garder un téléphone qui ne reçoit plus de mises à jour de sécurité.** Vérifiez combien de temps le fabricant prend en charge un modèle avant de l'acheter. Une fois la prise en charge terminée, les failles connues restent ouvertes quels que soient vos réglages, et cela vaut aussi pour un 2e téléphone gardé à la maison pour la banque.
- **Télécharger des fichiers d'apps depuis des sites web au hasard.** En dehors de Google Play, utilisez des sources connues comme F-Droid, le site du développeur lui-même, ou l'une des boutiques ci-dessus.
- **Croire qu'un nouveau système corrige vos habitudes.** Un téléphone durci rempli d'apps de suivi, connecté aux mêmes comptes, envoie une grande partie des mêmes données qu'avant.

## Pour aller plus loin {#go-further}

- **Comparer les systèmes et les boutiques :** Privacy Guides, les sections Android et téléphones mobiles (privacyguides.org).
- **Des guides pour iPhone et Android :** Surveillance Self-Defense, par l'Electronic Frontier Foundation (ssd.eff.org).
- **Sites des projets :** grapheneos.org, calyxos.org, lineageos.org, e.foundation, f-droid.org.
- **Chapitre suivant :** héberger vos propres services.

## Sources {#sources}

- [Supported devices and support lifetimes](https://grapheneos.org/faq), FAQ de GrapheneOS, consulté le 22 octobre 2026.
- [Coordinates of millions of smartphones feared stolen, sparking yet another lawsuit against data broker](https://www.theregister.com/2025/02/06/gravy_analytics_data_breach_suit/), The Register, 6 février 2025.
- [Buy a phone, get a tracker: unauthorized tracking code illegally installed on Android phones](https://noyb.eu/en/buy-phone-get-tracker-unauthorized-tracking-code-illegally-installed-android-phones), noyb, 7 avril 2021.
- [Android developer verification: Building a safer ecosystem together](https://android-developers.googleblog.com/2026/06/android-developer-verification.html), Android Developers Blog, 18 juin 2026.
- [Android developer verification guides](https://developer.android.com/developer-verification/guides), Android Developers, consulté le 29 octobre 2026.
- [Motorola plans GrapheneOS-compatible devices as early as 2027](https://www.techrepublic.com/article/news-motorola-grapheneos-partnership-2027/), TechRepublic, 2026, consulté le 29 octobre 2026.
- [F-Droid and Google's developer registration decree](https://f-droid.org/2025/09/29/google-developer-registration-decree.html), F-Droid, 29 septembre 2025.
- [Verified Boot](https://source.android.com/docs/security/features/verifiedboot), Android Open Source Project, consulté en septembre 2026.
- [Reproducible builds](https://f-droid.org/docs/Reproducible_Builds/), documentation de F-Droid, consulté en septembre 2026.
- [Frequently asked questions](https://wiki.lineageos.org/faq), wiki de LineageOS, consulté en septembre 2026.
- [Accrescent features](https://accrescent.app/features), Accrescent, consulté en septembre 2026.
- [CalyxOS is back: download release 7.2.2.0 with full maintenance support](https://calyxos.org/news/2026/07/01/calyxos-official-release-is-back/), CalyxOS, 1er juillet 2026.
- [Apple can no longer offer Advanced Data Protection in the United Kingdom to new users](https://support.apple.com/en-us/122234), Apple Support, 2025, consulté le 29 octobre 2026.

## Votre checklist {#your-checklist}

- [ ] Désinstallez les apps que vous n'utilisez plus (5 min)
- [ ] Passez en revue les autorisations de localisation, de micro, de caméra et de contacts (1 h)
- [ ] Supprimez l'identifiant publicitaire ou désactivez le suivi (5 min)
- [ ] Définissez un PIN de 6 chiffres ou plus, et un PIN de carte SIM (5 min)
- [ ] Sur iPhone, activez la Protection avancée des données. Sur Android, installez F-Droid et essayez 1 app (1 h)
