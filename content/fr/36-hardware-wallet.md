# Chapitre 17 : Hardware wallets

## En bref {#in-brief}

Un wallet de téléphone convient à l'argent de poche, mais l'épargne demande quelque chose de plus solide. Un hardware wallet est un petit appareil dédié (un appareil de signature) qui garde vos clés privées hors ligne et signe les transactions à l'intérieur de lui-même, de sorte que les logiciels malveillants de votre ordinateur ou de votre téléphone ne puissent pas les voir. Il en existe plusieurs bons, avec des compromis différents, et aucun n'est infaillible. L'appareil ne remplace pas la sauvegarde de votre seed (chapitre 14), car il peut casser ou être perdu, et c'est alors la sauvegarde qui restaure vos fonds.

## Des clés sur une machine toujours en ligne

Votre téléphone est en ligne toute la journée. Il fait tourner des dizaines d'applications, reçoit des liens d'inconnus, se connecte à des wifi publics et installe des mises à jour de nombreuses entreprises, et votre ordinateur ne vaut pas mieux. Chacun de ces éléments est une porte, et une application de wallet sur la même machine garde ses clés derrière ces portes.

Pour la somme que vous porteriez dans un porte-monnaie physique, ce risque est acceptable, et la commodité en vaut la peine. Pour l'épargne, le calcul change. Des logiciels malveillants qui lisent un fichier de wallet, remplacent une adresse dans le presse-papiers ou enregistrent l'écran existent et se vendent comme des produits prêts à l'emploi. Une transaction Bitcoin ne peut pas être annulée, et il n'y a pas de service d'assistance à appeler.

Personne n'a besoin de devenir expert en sécurité pour y faire face. La réponse pratique consiste à sortir les clés de ces machines, vers un appareil conçu pour les garder hors de portée de ce type de logiciel.

## Un petit ordinateur qui ne fait que signer

Un hardware wallet, plus précisément appelé **appareil de signature**, est un minuscule ordinateur qui n'a qu'1 tâche. Il génère votre seed, stocke les clés privées sur sa propre puce, et est conçu pour ne jamais les laisser sortir.

Quand vous voulez envoyer des bitcoins, le travail est réparti en 2 étapes.

1. Une application sur votre ordinateur ou votre téléphone prépare la transaction. Cette application ne connaît que vos informations publiques, elle peut donc afficher votre solde et construire un paiement, mais pas dépenser.
2. La transaction va vers l'appareil, par câble, Bluetooth, QR code ou carte mémoire. L'appareil affiche le montant et l'adresse de destination sur son propre écran. Vous vérifiez, vous confirmez sur l'appareil, et il signe en interne. Seule la signature revient.

Si votre ordinateur est infecté, le logiciel malveillant voit une transaction signée et non une clé. Il peut encore vous afficher une fausse adresse sur l'ordinateur, c'est pourquoi l'écran de l'appareil est celui que vous lisez.

La seed reste le vrai wallet, et l'appareil n'est qu'un outil plus sûr pour s'en servir. Vous avez toujours besoin de la sauvegarde du chapitre 14, et la seed ne vaut que ce que vaut l'aléa que l'appareil a utilisé pour la créer. En août 2023, la [divulgation « Milk Sad »](https://milksad.info/disclosure.html) a montré que Libbitcoin Explorer, un outil logiciel, créait des seeds à partir de seulement 32 bits d'aléa au lieu des 128 à 256 attendus, et que des wallets créés avec lui avaient été vidés le 12 juillet 2023. Aucune mise à jour ne pouvait réparer ces seeds, et leurs propriétaires ont dû en créer de nouvelles et y déplacer leurs fonds. Le même type de défaillance a touché un hardware wallet en juillet 2026, quand Coinkite [a révélé que le firmware des COLDCARD](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/) publié depuis 2021 avait créé des seeds faibles (voir le tableau).

## Le fabricant auquel vous devez encore faire confiance

Mettre les clés hors ligne les protège de votre ordinateur et déplace votre confiance vers le fabricant de l'appareil. Le fabricant écrit le firmware qui crée votre seed et signe vos transactions, contrôle la chaîne d'approvisionnement, et gère généralement l'application compagnon, dont les serveurs peuvent voir vos adresses et votre adresse IP. La fuite de Ledger (voir le tableau) ne venait même pas de l'appareil, mais de la liste clients de la boutique du fabricant.

Le firmware open source peut être lu par des tiers, et un [build reproductible](https://github.com/BitBoxSwiss/bitbox02-firmware/blob/master/releases/README.md) permet à n'importe qui de confirmer que le code publié est celui que vous installez. Une vérification de signature prouve que le firmware vient du fabricant, pas qu'il est sain, et la signature isolée de tout réseau (air-gapped) limite ce qu'un ordinateur peut envoyer à l'appareil. Un élément sécurisé résiste à quelqu'un qui tient l'appareil en main, mais de telles puces s'accompagnent souvent d'un accord de confidentialité, ce qui est [la raison pour laquelle Ledger garde une partie de son système fermée](https://www.ledger.com/blog-ledger-is-95-opensource-why-not-100). Certains appareils acceptent des lancers de dés comme source d'aléa, ce qui permet d'ajouter le vôtre à celui de la puce.

Rien de tout cela ne supprime le fabricant. La multisignature entre 2 fabricants (expliquée plus bas) répartit cette confiance, alors que pour un premier appareil, l'application du fabricant et ses vérifications automatiques restent la voie la plus sûre.

## Choisir votre appareil

Les appareils ci-dessous diffèrent par leur ouverture, leur prix, leur confort et leur isolation. « Air-gapped » signifie que l'appareil n'a jamais besoin d'être connecté à un ordinateur, car les transactions voyagent par QR code ou carte mémoire. Les gammes changent vite, et ce tableau est valable en septembre 2026.

| Appareil | Fabricant | Points forts | Compromis | Confiance envers le fabricant, et ce que vous pouvez vérifier |
|---|---|---|---|---|
| **BitBox02** | BitBox (Shift Crypto), Suisse | Open source, simple, une édition Bitcoin-only existe. [Le BitBox02 Nova, annoncé en juin 2025](https://bitcoinmagazine.com/news/bitbox-announces-bitbox02-nova-a-new-hardware-wallet-for-bitcoin), ajoute le Bluetooth et la prise en charge de l'iPhone | Pas air-gapped. Il se connecte par USB-C, ou par Bluetooth sur le Nova | Firmware open source avec builds reproductibles, signature vérifiée par la BitBoxApp. On ne se fie pas à la puce sécurisée seule |
| **Trezor** | SatoshiLabs, République tchèque | Le pionnier open source, facile, largement pris en charge | Les modèles plus anciens se connectent uniquement par câble, tandis que [le Safe 7, sorti fin 2025](https://trezor.io/guides/trezor-devices/trezor-safe-7/trezor-safe-7-faqs), ajoute le Bluetooth. Prend en charge beaucoup d'autres cryptomonnaies sauf si vous choisissez le firmware Bitcoin-only | Open source, firmware reproductible, vérifié par Trezor Suite. Le Safe 7 ajoute un élément sécurisé auditable (TROPIC01) |
| **COLDCARD** (séries Mk et Q) | Coinkite, Canada | Bitcoin-only, conçu pour signer sans câble, par carte mémoire ou, sur le Q, par QR code. 2 puces sécurisées de fabricants différents. De nombreuses options avancées | Plus de menus et d'options qu'il n'en faut à un débutant. En juillet 2026, une faille du firmware qui affaiblissait les seeds créées depuis 2021 a conduit à des vols sur plus de 5 200 adresses, [environ 1 800 bitcoins selon un décompte provisoire](https://www.trmlabs.com/resources/blog/the-largest-hardware-wallet-exploit-of-2026-inside-the-usd-116-million-coldcard-hack). [Une mise à jour ne répare pas une seed concernée](https://coldcard.com/resources/security/coldcard-security-and-verification), qui doit être remplacée | Code source publié, avec des builds reproductibles, mais sa [licence interdit de vendre le logiciel](https://github.com/Coldcard/firmware/blob/master/COPYING-CC), il n'est donc pas open source au sens strict. Un sachet numéroté et un voyant vert au démarrage aident à vérifier l'appareil |
| **Blockstream Jade** | Blockstream | Abordable, open source, peut fonctionner air-gapped avec des QR codes | Sa protection par PIN repose sur un serveur (celui de Blockstream, ou le vôtre) | Firmware open source. Pas d'élément sécurisé, donc le serveur de PIN fait partie de la confiance, sauf si vous l'hébergez |
| **Foundation Passport** | Foundation Devices, États-Unis | Open source, confortable à utiliser, signe par QR code | Parmi les plus chers. Le récent Passport Prime utilise aussi le Bluetooth et fait plus que Bitcoin (clés de sécurité, codes 2FA) | Firmware open source avec builds reproductibles, dont vous pouvez comparer le hash avec celui publié |
| **SeedSigner** | Projet communautaire | À construire soi-même avec des composants standard, open source, sans état (il ne stocke aucune seed) | Vous l'assemblez, et vous chargez votre seed à chaque utilisation. Pas un premier appareil | Aucune entreprise. Vous vérifiez vous-même la signature du logiciel, les builds sont reproductibles, l'aléa vient de dés ou d'une photo |
| **Ledger** | Ledger, France | Populaire, prend en charge beaucoup de cryptomonnaies, utilise une puce sécurisée | Firmware pas entièrement open source. [Une fuite de sa base de données clients en 2020](https://www.ledger.com/blog/update-efforts-to-protect-your-data-and-prosecute-the-scammers) a exposé environ 1 million d'adresses e-mail, ainsi que les noms, adresses postales et numéros de téléphone d'environ 272 000 acheteurs | Une partie du système sur la puce sécurisée est fermée, de sorte que des tiers ne peuvent pas vérifier pleinement ce que fait le firmware |

Vous avez aussi besoin d'un logiciel compagnon, soit l'application propre du fabricant, soit un wallet open source indépendant comme Sparrow Wallet, Electrum (ordinateur), Nunchuk (ordinateur et téléphone) ou BlueWallet (téléphone, surtout avec des appareils qui signent par QR code). Avec un wallet indépendant, vous ne dépendez pas du maintien en service de l'application du fabricant.

Pour des montants plus importants, le niveau suivant est la **multisignature**, un wallet qui exige par exemple 2 appareils sur 3 pour signer. Avec des appareils de fabricants différents, une faille chez 1 fabricant ou le vol d'1 appareil ne suffit pas à le vider. Sauvegardez la configuration multisignature complète ou son descripteur de sortie (output descriptor), y compris les xpubs de tous les cosignataires, ainsi que suffisamment de clés de signature (chapitre 14). Ces clés publiques ne permettent pas de dépenser à elles seules, mais elles révèlent l'activité du wallet. C'est plus de travail, maîtrisez donc d'abord 1 appareil.

Une configuration raisonnable pour la plupart des personnes est un appareil open source avec un firmware Bitcoin-only, acheté neuf et mis à jour avant usage, avec Sparrow ou l'application du fabricant. Le choix du fabricant reste le vôtre.

## Pas à pas {#step-by-step}

L'ordre est globalement le même pour chaque appareil, mais la vérification de l'étape 2 diffère selon les fabricants, gardez donc le guide officiel du fabricant ouvert.

1. **Achetez directement chez le fabricant ou chez un revendeur officiel.** Jamais d'occasion, jamais auprès d'un vendeur de marketplace.
2. **Vérifiez l'appareil comme le décrit son fabricant.** Certains fabricants expédient dans un sachet de sécurité scellé ou numéroté. Ledger, en revanche, [déclare n'utiliser aucun scellé anti-effraction](https://donjon.ledger.com/threat-model/device-genuineness/), qu'il juge faciles à copier, et s'appuie sur une vérification cryptographique dans son application. Les applications de BitBox, Trezor et Ledger vérifient l'appareil et installent un firmware signé. Avec SeedSigner, vous téléchargez le logiciel vous-même et vérifiez sa signature. Dans tous les cas, installez le dernier firmware avant de créer une seed. C'est l'étape qui remplace la confiance dans la chaîne de livraison par la vérification, bien qu'elle repose encore sur la signature du fabricant lui-même.
3. **Générez une nouvelle seed sur l'appareil.** Les mots doivent apparaître sur l'écran de l'appareil, pour la première fois, devant vous. N'utilisez jamais des mots livrés imprimés dans la boîte.
4. **Sauvegardez-la** sur papier ou sur métal, comme expliqué au chapitre 14. Définissez un PIN si l'appareil le permet. Les appareils sans état comme SeedSigner fonctionnent autrement.
5. **Vérifiez l'adresse de réception sur l'écran de l'appareil, puis envoyez un montant de test minuscule.** Faites-le avant de déplacer votre épargne, pas après.
6. **Vérifiez la récupération avec, pour seul enjeu, le minuscule solde de test.** Suivez sur l'appareil la procédure du fabricant pour vérifier la sauvegarde, ou pour effacer puis restaurer l'appareil, avec un format de sauvegarde compatible et toute passphrase notée. Vérifiez que vous retrouvez les mêmes adresses et le même solde de test avant d'ajouter votre épargne. Gardez la sauvegarde hors des wallets ordinaires de téléphone ou d'ordinateur. Un appareil sans état est rechargé plutôt qu'effacé.
7. **Déplacez le reste,** en 1 ou plusieurs transactions.
8. **Vérifiez l'adresse de réception sur l'écran de l'appareil, à chaque fois.** L'écran de l'ordinateur peut être manipulé, ce qui est bien plus difficile à faire avec l'écran de l'appareil.

## Erreurs à éviter {#mistakes-to-avoid}

- **Acheter sur des marketplaces.** Un appareil passé entre des mains inconnues peut avoir été modifié, et la petite économie ne vaut pas le risque.
- **Accepter une carte de seed qui arrive déjà remplie.** Considérez-la dans tous les cas comme une arnaque, car la personne qui a imprimé ces mots attend votre dépôt.
- **Taper la seed sur un ordinateur « pour mettre à jour ».** Aucune vraie mise à jour, aucune application ni aucun agent de support n'a besoin de votre seed. Pour une récupération, suivez la procédure vérifiée du fabricant et les instructions de l'appareil. Saisissez les mots sur l'appareil lui-même quand il le permet. Ne les saisissez jamais sur un site web, ni parce qu'une mise à jour ou un agent de support vous les demande.
- **Sauter la restauration de test.** Un mot erroné ou manquant vaut mieux être découvert maintenant, avec un montant de test, que dans 5 ans avec votre épargne.
- **Utiliser votre adresse personnelle pour la livraison sans y réfléchir.** Les listes de clients fuitent, comme l'a montré le cas de Ledger, et la liste dit alors à des inconnus où habite un détenteur de bitcoins. Envisagez un point de retrait ou une consigne à colis.
- **Faire confiance aux e-mails qui prétendent venir du fabricant.** Après la fuite de Ledger, des acheteurs ont reçu de l'hameçonnage convaincant, avec de fausses alertes de sécurité et de fausses mises à jour, et en 2021 certains ont même reçu par la poste des [appareils modifiés](https://www.bleepingcomputer.com/news/cryptocurrency/criminals-are-mailing-altered-ledger-devices-to-steal-cryptocurrency/), présentés comme des remplacements. Allez vous-même sur le site officiel, jamais par un lien.

## Pour aller plus loin {#go-further}

- **Des vérifications indépendantes de wallets et d'appareils.** WalletScrutiny (walletscrutiny.com) teste si le code publié correspond à ce que vous installez réellement.
- **Connecter un appareil à un wallet indépendant.** La documentation de Sparrow Wallet (sparrowwallet.com/docs).
- **Guides pas à pas pour les appareils.** Bitcoiner.Guide (bitcoiner.guide).
- **Chapitre suivant.** Faire tourner votre propre nœud.

## Sources {#sources}

- [How to use a wallet backup](https://trezor.io/guides/backups-recovery/general-standards/how-to-use-a-wallet-backup), Trezor, consulté le 22 octobre 2026.
- [Multisig backup warning and descriptor export](https://github.com/sparrowwallet/sparrow/blob/master/src/main/java/com/sparrowwallet/sparrow/wallet/MultisigBackupDialog.java), code source de Sparrow, consulté le 22 octobre 2026.
- [Update: efforts to protect your data and prosecute the scammers](https://www.ledger.com/blog/update-efforts-to-protect-your-data-and-prosecute-the-scammers), Ledger, 13 janvier 2021.
- [Threat model: device genuineness](https://donjon.ledger.com/threat-model/device-genuineness/), Ledger Donjon, page consultée en septembre 2026.
- [Criminals are mailing altered Ledger devices to steal cryptocurrency](https://www.bleepingcomputer.com/news/cryptocurrency/criminals-are-mailing-altered-ledger-devices-to-steal-cryptocurrency/), BleepingComputer, 16 juin 2021.
- [Milk Sad: technical write-up of CVE-2023-39910](https://milksad.info/disclosure.html), équipe de recherche Milk Sad, août 2023.
- [BitBox Announces BitBox02 Nova](https://bitcoinmagazine.com/news/bitbox-announces-bitbox02-nova-a-new-hardware-wallet-for-bitcoin), Bitcoin Magazine, 20 juin 2025.
- [Reproducible builds of the BitBox02 firmware](https://github.com/BitBoxSwiss/bitbox02-firmware/blob/master/releases/README.md), BitBox sur GitHub, consulté en septembre 2026.
- [Ledger is 95% open source, why not 100%?](https://www.ledger.com/blog-ledger-is-95-opensource-why-not-100), Ledger, consulté en septembre 2026.
- [Coldcard Security Advisory](https://blog.coinkite.com/coldcard-mk3-seed-generation-warning/), Coinkite, 30 juillet 2026, consulté le 29 octobre 2026.
- [COLDCARD security and verification](https://coldcard.com/resources/security/coldcard-security-and-verification) (2 éléments sécurisés, sachet numéroté, migration des seeds concernées), Coinkite, consulté le 29 octobre 2026.
- [The Largest Hardware Wallet Exploit of 2026: Inside the USD 116 Million Coldcard Hack](https://www.trmlabs.com/resources/blog/the-largest-hardware-wallet-exploit-of-2026-inside-the-usd-116-million-coldcard-hack), TRM Labs, 5 août 2026, chiffres provisoires de Galaxy Research.
- [COLDCARD firmware licence, MIT with the Commons Clause](https://github.com/Coldcard/firmware/blob/master/COPYING-CC), Coinkite sur GitHub, consulté le 29 octobre 2026.

## Votre checklist {#your-checklist}

- [ ] Décidez quel montant est de l'« épargne » pour vous et n'a plus sa place sur un téléphone (5 min)
- [ ] Choisissez un appareil dans le tableau et commandez-le chez le fabricant, vers un point de retrait (1 h)
- [ ] Vérifiez l'appareil et son firmware comme le décrit le fabricant, créez une nouvelle seed et une sauvegarde, puis envoyez un montant de test (1 h)
- [ ] Avec seulement un minuscule solde de test, suivez la procédure du fabricant pour vérifier la sauvegarde de l'appareil ou le restaurer, avant d'ajouter votre épargne (1 h)
- [ ] Vérifiez l'adresse sur l'écran de l'appareil à chaque réception (5 min)
