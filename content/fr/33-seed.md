# Chapitre 14 : Sauvegarder votre phrase de récupération

## En bref {#in-brief}

Vos mots de récupération sauvegardent les clés de votre wallet, et le téléphone est un outil pour les utiliser. De nombreux wallets utilisent 12 ou 24 mots, et certains utilisent un autre format. Celui qui lit les mots peut prendre les pièces, et si vous perdez à la fois le téléphone et les mots, les pièces ne peuvent plus être récupérées. Écrivez-les à la main, conservez 2 copies dans 2 endroits distincts, idéalement tous les 2 sous votre contrôle, ne faites jamais de copie numérique, et testez la sauvegarde avec la méthode adaptée à votre wallet tant que la somme est encore petite (étape 6).

## Pas de support, pas de bouton de réinitialisation

Avec une banque, perdre l'accès est un désagrément, car vous prouvez qui vous êtes et quelqu'un le réinitialise. La self-custody supprime ce quelqu'un. Il n'y a pas de service d'assistance, pas de bouton « j'ai oublié mes mots » et pas de tribunal qui puisse ordonner au réseau de vous rendre vos pièces. C'est ce qui rend vos bitcoins très difficiles à geler ou à saisir à distance, et cela fait aussi de vous la seule personne responsable.

2 choses tournent mal dans la vraie vie, et elles tirent dans des directions opposées. La première est la **perte**, quand un téléphone tombe dans un lac, que le papier est jeté pendant un déménagement ou qu'un incendie détruit l'exemplaire unique. La seconde est le **vol**, quand les mots ont été enregistrés dans une photo, un brouillon d'e-mail, une note dans le cloud ou un gestionnaire de mots de passe, et que quelqu'un les a trouvés. En mars 2025, des enquêteurs fédéraux américains ont [relié un vol d'environ 150 millions de dollars](https://krebsonsecurity.com/2025/03/feds-link-150m-cyberheist-to-2022-lastpass-hacks/), commis en janvier 2024, à des secrets stockés dans le gestionnaire de mots de passe LastPass, qui avait été piraté en 2022. Les pièces volées de cette manière bougent en quelques minutes et ne peuvent pas être rappelées, une bonne sauvegarde doit donc protéger à la fois contre la perte et contre le vol.

## Un nombre aléatoire unique, écrit en mots

Quand vous créez un wallet, l'application génère un unique très grand nombre aléatoire, et tout le reste en découle, c'est-à-dire chaque clé et chaque adresse pour chaque pièce que vous recevrez un jour dans ce wallet. Un standard répandu appelé [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) écrit ce nombre, le plus souvent, sous la forme de 12 ou 24 mots tirés d'une liste fixe de 2 048 mots anglais simples, parce que les gens recopient les mots plus fiablement que de longues suites de chiffres. Le dernier mot inclut une somme de contrôle (checksum), qui détecte la plupart des erreurs de copie.

Pour les clés dérivées de cette seed, les mots ne changent pas après chaque paiement. La récupération exige tout de même un format de sauvegarde compatible, le bon type d'adresse ou le bon chemin de dérivation (derivation path), et toute passphrase que vous avez utilisée. Trezor prend aussi en charge les sauvegardes SLIP39, généralement de 20 mots. Les seeds natives d'Electrum utilisent un schéma différent de BIP39. Ne supposez pas que n'importe quel wallet accepte n'importe quels mots.

Conservez le nom du wallet et le format de sauvegarde avec vos instructions de récupération. La seed seule ne restaure pas les étiquettes, les clés importées séparément ni tous les réglages du wallet. Sauvegardez-les comme l'explique la documentation du wallet.

Lightning est l'exception. Les fonds dans les canaux dépendent du wallet qui les a ouverts, et certains wallets Lightning demandent un fichier de sauvegarde supplémentaire en plus des mots. Si c'est le cas, l'application le dit clairement, et ses instructions passent en premier.

## Personne à qui faire confiance, personne à appeler

Une sauvegarde de seed on-chain dans un format ouvert peut être récupérée sans l'entreprise d'origine et sans compte, à l'aide d'un logiciel compatible et des données de la blockchain. Vous dépendez tout de même du logiciel et de l'appareil de récupération, ainsi que d'un serveur, sauf si vous utilisez votre propre nœud. Conserver uniquement les mots ne suffit pas pour toutes les conceptions de wallet, en particulier Lightning et la multisignature. La disponibilité et la confidentialité de la sauvegarde reposent sur vous.

Chaque commodité qui adoucit cela ramène un tiers. Une plaque d'acier commandée en ligne place votre nom et votre adresse dans le fichier clients d'un fabricant, du genre de celui qui a fuité chez Ledger en 2020 (voir « Erreurs à éviter »). Les parts Shamir et la multisignature répartissent le risque, mais chaque personne qui détient une part ou une clé peut la perdre ou s'entendre avec d'autres, et le logiciel qui découpe et reconstruit le secret doit lui aussi être digne de confiance. Tout service qui propose de récupérer votre seed à votre place va plus loin. Pour rendre une sauvegarde après un contrôle d'identité, une entreprise doit la détenir hors de chez vous, où elle peut être piratée, contrainte ou fermée. Cela peut convenir à quelqu'un qui craint la perte avant tout, en sachant que les tiers de confiance reviennent alors dans le tableau.

La vérification consiste à contrôler que la sauvegarde fonctionne avec la procédure de récupération adaptée à votre wallet (étape 6).

## Choisir comment la conserver

Le bon support dépend du montant et de ce qui menace votre domicile, qu'il s'agisse d'eau, de feu, de cambrioleurs ou de visiteurs curieux. Toutes les options ci-dessous gardent les mots hors ligne, et elles peuvent être combinées.

| Méthode | Coût | En qui vous devez avoir confiance | Force | Faiblesse |
|---|---|---|---|---|
| **Papier**, crayon ou encre permanente | Presque rien | Personne, hormis les gens qui peuvent accéder à l'endroit où il est conservé | Immédiat, aucun outil nécessaire | Eau, feu, décoloration, facile à jeter par erreur |
| **Papier plastifié** | Quelques euros | Personne, tant que la plastifieuse est la vôtre. Une boutique de photocopie serait un tiers. | Résiste à l'eau et à l'usure | Brûle toujours. Utilisez votre propre plastifieuse, pas une boutique de photocopie. |
| **Produit en acier** (Cryptosteel, Seedor et autres) | Des dizaines d'euros, jusqu'à environ 100 | Le fabricant et la boutique, qui apprennent votre nom et votre adresse, mais jamais les mots | Résiste au feu, à l'eau et au temps | Le prix. Un objet visible qui dit « bitcoin » à celui qui le trouve. |
| **Acier fait maison** (lettres frappées dans des rondelles d'acier tenues sur un boulon) | Quelques euros de quincaillerie, plus un jeu de poinçons de lettres | Personne. Une quincaillerie ignore à quoi servent les rondelles. | Même résistance, discret, aucune marque à croire | 1 heure de travail, et du soin au moment de frapper |

Il existe aussi 2 options avancées, pour des montants plus élevés.

- **Répartition sur plusieurs lieux.** Des schémas standard comme la sauvegarde Shamir ([SLIP39](https://github.com/satoshilabs/slips/blob/master/slip-0039.md)), prise en charge par certains hardware wallets, divisent le secret en parts, par exemple n'importe lesquelles 2 sur 3. SLIP39 utilise sa propre liste de mots et n'est pas compatible avec BIP39, donc seuls les wallets qui le prennent en charge peuvent le restaurer. N'inventez pas votre propre schéma en coupant la liste de mots en 2 (la section suivante explique pourquoi).
- **Multisignature.** Un wallet qui exige plusieurs clés indépendantes, par exemple 2 sur 3, conservées dans des lieux différents, de sorte qu'un vol ou une perte unique ne soit pas fatal. Conservez suffisamment de sauvegardes de clés de signature, ainsi que la configuration complète du wallet ou son descripteur de sortie (output descriptor), y compris la clé publique étendue (xpub) de chaque cosignataire. Avoir assez de seeds peut ne pas suffire. Le descripteur ne permet pas de dépenser à lui seul, mais il expose des informations sur le wallet, protégez donc sa confidentialité. Le chapitre 17 présente les appareils qui rendent cela praticable.

Un point de départ raisonnable pour la plupart des personnes est le papier le premier jour, puis une copie en acier quand le montant serait douloureux à perdre, sans passphrase tant que vous ne la comprenez pas pleinement. Au-delà, les configurations diffèrent légitimement, comme le montre la section suivante.

## Pas de bonne configuration unique

Il n'existe pas de bonne configuration unique, car les montants, les domiciles, les familles et les menaces diffèrent, et 2 personnes prudentes peuvent raisonnablement choisir différemment. Les 3 approches principales peuvent être combinées.

| Approche | Ce que vous gagnez | Le prix |
|---|---|---|
| **Plusieurs clés indépendantes**, ou plusieurs hardware wallets, pour des usages différents comme les dépenses et l'épargne | Un vol ou une erreur touche 1 wallet, pas tout | Davantage de sauvegardes à stocker, étiqueter et tester |
| **1 clé dont la sauvegarde est répartie en fragments** conservés dans des lieux différents, avec une copie de chaque fragment dans 2 lieux | Perdre 1 lieu ne fait pas perdre l'argent, et trouver 1 fragment ne le révèle pas | Davantage de lieux et de personnes impliqués, et une restauration qui demande un logiciel compatible |
| **1 clé plus une passphrase** (le mot ou la phrase supplémentaire facultatif) | Les mots seuls n'ouvrent plus le wallet | 1 secret de plus à sauvegarder et à transmettre |

Le partage de secret de Shamir et la multisignature sont 2 choses différentes. Dans un schéma de partage de secret à seuil bien conçu, un nombre de parts inférieur au seuil requis ne révèle rien du secret. La multisignature utilise des clés indépendantes. 1 clé seule ne permet pas de dépenser quand le seuil est plus élevé, mais elle peut révéler des informations sur le wallet. Conservez la configuration multisignature complète en plus des clés. Couper vous-même la liste de mots donne à chaque personne qui la trouve une partie du secret, et en juin 2020 John Cantrell a [retrouvé les 4 mots manquants d'une phrase de 12 mots en environ 30 heures](https://bitcoinwords.github.io/how-i-checked-over-1-trillion-mnemonics) avec des cartes graphiques louées.

Un attaquant qui détient les mots peut aussi essayer des passphrases très vite, de sorte qu'une passphrase courte ou devinable n'ajoute presque aucune sécurité, et elle doit être longue et aléatoire. Chaque passphrase différente ouvre un wallet différent, ce qui permet des sous-comptes séparés ou cachés. Elle doit elle-même être sauvegardée, séparément des mots, là où vos héritiers pourront la trouver. Une passphrase oubliée signifie des pièces perdues.

Le critère pratique est de choisir la configuration la plus simple que vous comprendrez encore, et saurez restaurer, dans 10 ans.

## Pas à pas {#step-by-step}

L'exemple utilise du papier et un stylo. La logique est la même sur de l'acier.

1. **Choisissez le moment.** Seul, à une table, sans caméra derrière vous, ni dans un café ni dans un train.
2. **Écrivez les mots à la main**, numérotés, dans l'ordre, en lettres capitales lisibles. Notez le nom du wallet et la date, pas le montant.
3. **Vérifiez-les 2 fois.** Relisez-les face à l'écran, mot par mot. La plupart des wallets vous demandent ensuite d'en confirmer certains.
4. **Ne faites jamais de version numérique.** Ne les tapez pas, ne les photographiez pas, ne les imprimez pas, ne les dictez pas, ne les envoyez pas par e-mail, et ne les stockez ni dans le cloud ni dans un gestionnaire de mots de passe. Pour un appareil de signature, gardez sa sauvegarde hors des wallets logiciels ordinaires. Suivez sa procédure officielle de vérification de la sauvegarde et de récupération. Ne tapez pas les mots dans un appareil connecté à internet simplement pour les tester.
5. **Faites 2 copies** et conservez-les dans 2 endroits distincts, par exemple chez vous et chez un proche, chacune dans une enveloppe scellée. Le second endroit est un compromis, car sans passphrase, celui qui ouvre l'enveloppe contrôle les pièces. Choisissez quelqu'un à qui vous confieriez le même montant en espèces, et envisagez l'une des approches ci-dessus quand le montant grandit. Si vous utilisez des fragments ou une passphrase, la règle des 2 copies s'applique à chacun d'eux, et une passphrase n'est jamais conservée avec les mots.
6. **Testez la sauvegarde dans le bon environnement.** Pour un petit **wallet logiciel** on-chain, restaurez-le sur un second appareil que vous contrôlez, avec un logiciel compatible, comparez ses adresses et son solde, puis supprimez la copie de test. Gardez l'application d'origine du début à la fin. Cela protège contre une erreur de copie, pas contre un logiciel malveillant présent sur le second appareil. Pour un **hardware wallet**, utilisez la fonction de vérification de la sauvegarde proposée par le fabricant, ou restaurez sur un matériel compatible en suivant sa procédure officielle. N'importez jamais la seed d'un hardware wallet dans un téléphone ou un ordinateur juste pour ce test. Un exercice d'effacement puis de restauration se fait avec un solde de test minuscule, avant d'y ajouter de l'épargne (chapitre 17).
7. **Traitez un wallet Lightning différemment.** Supprimer une application qui détient des canaux ouverts peut vous coûter les fonds si la restauration échoue, et Phoenix, par exemple, [déconseille de faire tourner 2 applications sur la même seed](https://phoenix.acinq.co/faq). Lisez d'abord les instructions de restauration de votre wallet. Le vrai test arrive généralement quand vous changez de téléphone, avec un petit solde, l'ancien téléphone éteint, et l'ancienne application conservée jusqu'à ce que le solde apparaisse sur le nouveau.
8. **Préparez la transmission.** Ajoutez une lettre scellée expliquant en termes simples ce dont il s'agit, que cela a de la valeur, que les mots ne doivent jamais être saisis sur un site web, à qui l'on peut faire confiance pour aider, et de combien d'éléments se compose votre configuration (mots, fragments, passphrase) et où chacun est conservé. La lettre ne contient jamais les mots eux-mêmes. Prévenez votre famille que les inconnus qui proposent de « récupérer » les pièces sont des escrocs.

## Erreurs à éviter {#mistakes-to-avoid}

- **Garder une copie numérique.** Les photos, les notes, les brouillons d'e-mail et les disques cloud sont exposés aux logiciels malveillants et aux intrus. Supprimer un fichier n'annule pas cette exposition et n'efface pas toutes les copies synchronisées. Si les mots ont pu fuiter, suivez les instructions du fabricant pour créer un nouveau wallet et y transférer les fonds en sécurité. N'effacez jamais en premier votre seul wallet fonctionnel.
- **Ne garder qu'1 copie.** Un incendie, une inondation ou un déménagement suffit à la perdre, c'est pourquoi vous gardez 2 copies dans 2 endroits.
- **Dire aux gens combien vous possédez.** En décembre 2020, les noms, adresses postales et numéros de téléphone d'[environ 272 000 clients de Ledger](https://www.ledger.com/message-ledgers-ceo-data-leak) ont été publiés sur un forum de pirates après une fuite de la base de données de la boutique de l'entreprise, et ces clients ont ensuite été visés par des campagnes d'hameçonnage. Parlez de Bitcoin autant que vous le voulez, mais pas de votre solde.
- **Saisir vos mots sur un site web ou les donner au « support ».** Aucune équipe de wallet, aucune plateforme d'échange et aucune autorité ne les demandera jamais, donc quiconque les demande tente un vol.
- **Bâtir un schéma dont vous ne vous souviendrez pas dans 5 ans.** Des mots cachés dans un livre, coupés en 4, avec un code improvisé, ont empêché de nombreuses personnes d'accéder à leurs propres pièces. Gardez un schéma simple, documenté et testé.
- **Ne jamais tester, ou tester en supprimant l'application.** Une sauvegarde non testée peut contenir un mot erroné, et si vous supprimez d'abord l'application, vous le découvrez après la perte de la seule copie fonctionnelle. Utilisez la procédure logicielle ou matérielle adaptée à votre wallet (étape 6).

## Pour aller plus loin {#go-further}

- **Des sauvegardes en acier testées au feu, à l'acide et à la presse.** Les évaluations de stockage métallique de Jameson Lopp (jlopp.github.io/metal-bitcoin-storage-reviews).
- **Tutoriels de sauvegarde et de récupération.** Plan B Academy (planb.academy).
- **Le standard lui-même et sa liste de mots.** BIP39, dans les propositions d'amélioration de Bitcoin (github.com/bitcoin/bips).
- **Quel wallet peut restaurer quelle seed.** Wallets Recovery (walletsrecovery.org).
- **Chapitre suivant.** Lightning et euros au quotidien.

## Sources {#sources}

- [Understanding Trezor backups, 12, 20 or 24 words](https://trezor.io/learn/security-privacy/personal-security-standards/understanding-trezor-wallet-backups-12-20-or-24-words), Trezor, consulté le 22 octobre 2026.
- [Seed version system](https://electrum.readthedocs.io/en/latest/seedphrase.html), documentation d'Electrum, consultée le 22 octobre 2026.
- [How to use a wallet backup](https://trezor.io/guides/backups-recovery/general-standards/how-to-use-a-wallet-backup), Trezor, consulté le 22 octobre 2026.
- [Move crypto to a wallet with a new backup](https://trezor.io/guides/backups-recovery/general-standards/move-crypto-to-a-wallet-with-a-new-wallet-backup), Trezor, consulté le 22 octobre 2026.
- [Multisig backup warning and descriptor export](https://github.com/sparrowwallet/sparrow/blob/master/src/main/java/com/sparrowwallet/sparrow/wallet/MultisigBackupDialog.java), code source de Sparrow, consulté le 22 octobre 2026.
- [Feds Link $150M Cyberheist to 2022 LastPass Hacks](https://krebsonsecurity.com/2025/03/feds-link-150m-cyberheist-to-2022-lastpass-hacks/), Krebs on Security, 6 mars 2025.
- [Message from Ledger's CEO on the data leak](https://www.ledger.com/message-ledgers-ceo-data-leak), Ledger, 21 décembre 2020.
- [BIP39: Mnemonic code for generating deterministic keys](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki), Bitcoin Improvement Proposals, 2013.
- [SLIP39: Shamir's Secret-Sharing for Mnemonic Codes](https://github.com/satoshilabs/slips/blob/master/slip-0039.md), SatoshiLabs, consulté en septembre 2026.
- [How I checked over 1 trillion mnemonics in 30 hours to win a bitcoin](https://bitcoinwords.github.io/how-i-checked-over-1-trillion-mnemonics), John Cantrell, republié par WORDS Bitcoin Journal, 18 juin 2020.
- [Phoenix FAQ: restoring a wallet, limitations](https://phoenix.acinq.co/faq), ACINQ, consultée en septembre 2026.

## Votre checklist {#your-checklist}

- [ ] Écrivez vos mots à la main et vérifiez-les 2 fois (5 min)
- [ ] Supprimez toute copie numérique de vos mots, et transférez les fonds vers un nouveau wallet si les mots ont pu fuiter (1 h)
- [ ] Faites une seconde copie et conservez-la dans un second endroit (1 h)
- [ ] Testez votre sauvegarde avec un petit solde, sans supprimer le wallet d'origine, et avec la procédure du fabricant pour un hardware wallet (1 h)
- [ ] Rédigez la lettre scellée pour votre famille et faites une copie en acier (1 week-end)
