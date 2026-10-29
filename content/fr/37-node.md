# Chapitre 18 : Faire tourner votre propre nœud

## En bref {#in-brief}

Sans votre propre nœud, votre wallet interroge le serveur de quelqu'un d'autre au sujet de votre argent. Un nœud est votre propre copie des règles et du registre de Bitcoin, qui vérifie lui-même chaque bloc et chaque transaction, de sorte que vous ne dépendez plus de la réponse d'autrui. Il protège votre confidentialité, et il renforce le réseau. Il demande un petit ordinateur toujours allumé, un SSD de 2 To, un week-end de votre temps, puis quelques jours de synchronisation pendant lesquels la machine travaille seule. Ce n'est pas un mineur, et il ne rapporte rien.

## Votre wallet interroge un inconnu au sujet de votre argent

Quand vous ouvrez une application de wallet, elle a besoin de connaître votre solde. Elle n'a pas le registre, elle demande donc à un serveur ce qui s'est passé sur vos adresses. Ce serveur appartient au fabricant du wallet, ou à un bénévole inconnu.

2 choses en découlent. D'abord, le serveur peut apprendre quelles adresses sont les vôtres, toutes, avec votre adresse IP. Les wallets séparés et les adresses neuves du chapitre 16 sont de nouveau regroupés, dans les journaux de quelqu'un. Ensuite, vous devez croire la réponse, car si le serveur se trompe, est hors ligne ou malhonnête, votre wallet vous montre ce qu'on lui a dit.

Pour de petits montants, c'est un compromis raisonnable, et la plupart des gens commencent ainsi. Cela reste un arrangement étrange pour un système conçu pour que personne n'ait à faire confiance. Avec votre propre nœud, la question reste à l'intérieur de votre réseau domestique.

## Un ordinateur qui vérifie lui-même chaque règle

Un **nœud** est un ordinateur qui fait tourner un logiciel Bitcoin, le plus souvent Bitcoin Core (d'autres implémentations existent, comme Bitcoin Knots). Il télécharge l'ensemble du registre depuis le premier bloc en 2009 et vérifie chaque transaction au regard des règles, c'est-à-dire aucune pièce dépensée 2 fois, aucune pièce créée à partir de rien et jamais plus de 21 millions. Il répète cela pour chaque nouveau bloc, environ toutes les 10 minutes, ce qui est le sens de « don't trust, verify » (« ne faites pas confiance, vérifiez »).

Votre nœud n'accepte que ce qui suit les règles qu'il applique. Quand des milliers de personnes font de même, une entreprise, un mineur ou un gouvernement qui voudrait d'autres règles devrait d'abord les convaincre d'installer un autre logiciel.

Un nœud n'est pas un mineur. Il consomme peu d'électricité, ne rapporte rien, et n'a pas besoin de détenir de clés privées. Dans la configuration de simple vérification décrite ici, elles restent dans un wallet ou un appareil de signature séparé. Bitcoin Core peut aussi faire tourner un wallet. Si vous utilisez cette fonction, sauvegardez aussi ce wallet.

Il lui faut un petit ordinateur qui reste allumé, une connexion domestique normale et un SSD de 2 To. En septembre 2026, le registre pèse [environ 770 Go](https://www.blockchain.com/explorer/charts/blocks-size) et [grandit de 5 à 10 Go par mois](https://bitcoincore.org/en/download/), et l'index d'un serveur Electrum ajoute de quelques dizaines à plus de 100 Go, ce qui remplirait presque un disque de 1 To.

## Ce qu'un nœud vous demande encore de croire

La question qui traverse ce livre, qui est le tiers de confiance et si vous pouvez le vérifier, s'arrête ici. Pour l'état de votre argent, un nœud ramène la réponse à personne. Il ne croit ni le serveur d'un fabricant de wallet ni les nœuds auxquels il se connecte, car chaque bloc qu'ils envoient est vérifié au regard des règles et rejeté s'il est invalide, quel qu'en soit l'expéditeur. Vous gagnez l'authenticité (le solde que vous voyez est le vrai) et le contrôle des règles que vous acceptez.

2 choses subsistent. La première est le logiciel, car un nœud applique les règles du programme que vous avez installé, et une copie falsifiée appliquerait celles de quelqu'un d'autre. Bitcoin Core répond avec des builds reproductibles, dans lesquels plusieurs développeurs compilent chaque version indépendamment, obtiennent des fichiers identiques et [publient leurs signatures](https://github.com/bitcoin-core/guix.sigs). En en vérifiant quelques-unes, vous cessez de dépendre de l'honnêteté d'1 personne. Une plateforme de nœud ajoute son fabricant à la liste, pour le système, la boutique d'applications et les mises à jour. La seconde est votre propre matériel et votre système d'exploitation, que vous ne pouvez pas auditer entièrement.

Le prix est un disque, un week-end et un peu de maintenance, et pour de petits montants un serveur public reste un choix raisonnable.

## Choisir votre route

Toutes les routes font tourner le même logiciel Bitcoin en dessous, et elles diffèrent par la quantité de travail faite pour vous.

Sur un ordinateur de tous les jours, un **nœud élagué** (pruned node) est l'option la plus légère. Il vérifie tout mais ne conserve que les blocs les plus récents, de sorte que le stockage peut tourner autour de 10 Go avec une cible d'élagage basse, plus de la place pour la croissance et d'autres fichiers. Il télécharge et vérifie tout de même l'historique complet, l'élagage ne raccourcit donc pas le premier téléchargement. Cependant, la plupart des logiciels de serveur pour wallets ont besoin du registre complet, c'est pourquoi un nœud dédié le conserve.

| Route | Ce que c'est | Points forts | Compromis | En qui vous avez encore confiance |
|---|---|---|---|---|
| **Bitcoin Core sur votre ordinateur de tous les jours** | Le logiciel de référence, open source, depuis bitcoincore.org | Gratuit, le départ le plus simple, inclut son propre wallet, peut fonctionner en mode élagué sur un petit disque | Pas toujours allumé. Sans le mode élagué, il remplit la majeure partie d'un disque de 1 To | Les développeurs de Bitcoin Core, sauf si vous vérifiez les signatures de plusieurs constructeurs (builders), et votre ordinateur de tous les jours |
| **Umbrel** | Un système de serveur domestique avec une boutique d'applications. Tourne sur votre propre matériel, ou sur un appareil que l'entreprise vend | L'interface la plus soignée, des applications en 1 clic | Fait par 1 entreprise. Gratuit pour un usage personnel, mais sa licence n'est pas open source (pas de réutilisation commerciale) | Umbrel aussi, pour le système, sa boutique d'applications et ses mises à jour. Le code peut être lu |
| **Start9 (StartOS)** | Un système de serveur open source. Tourne sur votre propre matériel, ou sur un serveur que l'entreprise vend | Fort accent sur la confidentialité et l'auto-hébergement, bonne documentation | Fait par 1 entreprise. Un peu plus à apprendre au départ | Start9 aussi, pour le système, sa place de marché et ses mises à jour. L'image est fournie avec une somme de contrôle et une signature |
| **RaspiBlitz** | Un projet communautaire open source pour le Raspberry Pi | Aucune entreprise impliquée, des outils Lightning solides | Plus technique, un peu de travail en ligne de commande | Ses mainteneurs bénévoles. Les scripts de build sont publics, et l'image porte la signature PGP du développeur principal |
| **MyNode** | Un système de nœud pour petits ordinateurs, avec une édition communautaire gratuite et une édition premium payante | Interface web simple, de nombreuses applications Bitcoin | Fait par une petite entreprise, certaines fonctions sont réservées à l'édition payante | MyNode aussi, pour le système, les applications qu'il empaquette et ses mises à jour |
| **La route manuelle** | Linux Debian ou Ubuntu, puis Bitcoin Core, puis un serveur Electrum (electrs ou Fulcrum), en suivant un guide | Vous comprenez chaque élément. Rien de caché, entièrement open source | Lente, ligne de commande uniquement. Pour ceux qui apprennent et y prennent plaisir | Seulement les logiciels dont vous vérifiez vous-même les signatures, les auteurs de votre guide, et votre matériel |

Umbrel et Start9 sont aussi des serveurs domestiques généraux, ce qui rejoint le chapitre 10, puisque la même boîte peut héberger vos fichiers et vos photos.

Une configuration raisonnable pour la plupart des personnes est d'essayer Bitcoin Core sur votre ordinateur, en mode élagué, pour voir ce qu'est un nœud, puis de passer à un petit ordinateur dédié avec la plateforme dont les compromis vous conviennent.

## Un mot sur les nœuds Lightning

Les mêmes plateformes permettent d'installer un nœud Lightning (LND ou Core Lightning) en 1 clic. Considérez-le comme un projet pour plus tard. Un nœud Lightning détient de vrais fonds dans des canaux, sur une machine toujours en ligne. Les canaux ont besoin de leurs propres sauvegardes, d'une attention régulière et d'une compréhension de ce qui se passe si le disque tombe en panne, et restaurer une ancienne sauvegarde de la mauvaise manière peut même vous coûter les fonds d'un canal. Un nœud Bitcoin seul peut tomber en panne sans aucune perte, car il suffit de se synchroniser à nouveau, ce qui n'est pas vrai d'un nœud Lightning. Apprenez avec de petites sommes, et seulement après que le reste de ce chapitre est devenu une routine.

## Pas à pas {#step-by-step}

L'exemple utilise une plateforme avec boutique d'applications, comme Umbrel ou StartOS. RaspiBlitz et MyNode suivent le même ordre. Votre propre travail tient dans un week-end, et la machine a ensuite besoin de quelques jours de son côté.

1. **Choisissez le matériel.** Un mini PC d'occasion ou un Raspberry Pi récent avec 8 Go de mémoire, un SSD de 2 To d'une marque connue, et un câble réseau vers votre routeur.
2. **Installez la plateforme** en suivant son guide officiel, à partir d'une image téléchargée sur son site officiel, et définissez un mot de passe fort et unique (chapitre 2). Quand le projet publie une somme de contrôle ou une signature pour cette image, comme le font [Start9](https://docs.start9.com/start-os/0.4.0.x/installing-startos.html) et [RaspiBlitz](https://docs.raspiblitz.org/docs/faq), vérifiez-la avant d'écrire l'image sur le disque. C'est l'étape qui remplace la confiance dans le téléchargement par la vérification.
3. **Installez l'application Bitcoin et laissez-la se synchroniser.** Cela prend quelques jours, et jusqu'à 1 semaine sur un matériel lent comme un Raspberry Pi. Laissez-la tourner quand c'est possible. Si vous devez l'arrêter, éteignez-la proprement depuis l'interface et laissez la synchronisation reprendre plus tard. Ne coupez pas le courant.
4. **Installez une application de serveur Electrum** (electrs ou Fulcrum). Elle construit un index pour que les wallets puissent poser des questions à votre nœud, ce qui prend encore plusieurs heures, parfois 1 journée entière.
5. **Connectez votre wallet.** Dans Sparrow, BlueWallet ou Nunchuk, ouvrez les paramètres de serveur ou de réseau et saisissez l'adresse de votre propre serveur Electrum à la place du serveur public. À partir de cette étape, votre wallet affiche ce que votre propre nœud a vérifié, et non plus ce qu'un tiers lui a dit. Zeus fonctionne différemment, car il se connecte à un nœud Lightning, ce qui est pour plus tard.
6. **Accédez-y depuis l'extérieur de chez vous** via Tor ou un VPN privé (voir le chapitre 10). umbrelOS et StartOS proposent un accès par Tor en option.
7. **Gardez-le à jour,** et conservez vos sauvegardes de seed séparément du nœud. Un nœud de simple vérification n'a besoin d'aucune seed et ne devrait jamais en voir une. Si vous activez le wallet de Bitcoin Core ou installez Lightning, protégez et sauvegardez ces wallets séparément.

## Erreurs à éviter {#mistakes-to-avoid}

- **Utiliser une carte SD ou une clé USB bon marché, ou un disque trop petit.** Un nœud écrit en permanence, et les cartes SD et les clés USB ont tendance à tomber en panne en quelques mois et peuvent corrompre les données. Utilisez un vrai SSD de 2 To, car 1 To ne laisse presque aucune marge en septembre 2026, et [le guide RaspiBolt demande désormais lui aussi 2 To](https://raspibolt.org/).
- **Aucune protection électrique.** Une coupure de courant soudaine peut endommager la base de données et vous coûter des jours de synchronisation. Éteignez toujours depuis l'interface, et envisagez un petit onduleur (UPS).
- **Penser que le nœud détient vos pièces.** Un nœud de simple vérification ne détient aucune clé de dépense. Le wallet facultatif de Bitcoin Core et une application Lightning, eux, détiennent des clés et demandent leurs propres sauvegardes. Avec des clés conservées à part, un nœud de vérification en panne peut être reconstruit sans perte de fonds.
- **L'exposer à internet.** N'ouvrez pas de ports sur votre routeur pour accéder au tableau de bord. Utilisez Tor ou un VPN.
- **Abandonner pendant la première synchronisation.** Elle peut sembler bloquée pendant des jours, le temps de vérifier plus de 15 ans de transactions, ce qu'elle n'a à faire qu'1 fois.
- **Télécharger un logiciel au mauvais endroit, ou sans le vérifier.** Obtenez Bitcoin Core uniquement sur bitcoincore.org, et chaque plateforme sur son site officiel. La [page de téléchargement de Bitcoin Core](https://bitcoincore.org/en/download/) explique comment vérifier le fichier par rapport à la liste publiée des sommes de contrôle, et comment vérifier que cette liste porte les signatures PGP de plusieurs développeurs. Sur une plateforme, vous comptez sur son fabricant pour le faire pour les applications qu'elle installe, alors que sur votre propre ordinateur et sur la route manuelle, c'est votre travail.

## Pour aller plus loin {#go-further}

- **Les bases.** La page de téléchargement de Bitcoin Core (bitcoincore.org), avec les prérequis actuels, le mode élagué et la procédure pour vérifier votre téléchargement.
- **La route manuelle.** Le guide RaspiBolt (raspibolt.org, version 4, mis à jour en août 2026) et MiniBolt, un guide similaire pour les PC ordinaires (minibolt.minibolt.info). Les 2 sont maintenus en septembre 2026.
- **Connecter un wallet à votre nœud.** La documentation de Sparrow Wallet (sparrowwallet.com/docs).
- **La suite.** Votre checklist.

## Sources {#sources}

- [Graceful shutdown, stop RPC](https://bitcoincore.org/en/doc/30.0.0/rpc/control/stop/), documentation de Bitcoin Core, consultée le 22 octobre 2026.
- [Blockchain size chart](https://www.blockchain.com/explorer/charts/blocks-size), Blockchain.com, consulté le 20 septembre 2026 (environ 770 Go).
- [Download Bitcoin Core, with requirements and verification of the download](https://bitcoincore.org/en/download/), projet Bitcoin Core, consulté en septembre 2026.
- [Signatures of the Bitcoin Core builders (guix.sigs)](https://github.com/bitcoin-core/guix.sigs), projet Bitcoin Core sur GitHub, mis à jour à chaque version.
- [Installing StartOS, with verification of the download](https://docs.start9.com/start-os/0.4.0.x/installing-startos.html), documentation de Start9, consultée en septembre 2026.
- [RaspiBlitz FAQ, how to verify the SD card image](https://docs.raspiblitz.org/docs/faq), projet RaspiBlitz, consultée en septembre 2026.
- [RaspiBolt, version 4](https://raspibolt.org/), guide communautaire RaspiBolt, mis à jour en août 2026.
- [MiniBolt](https://minibolt.minibolt.info/), guide communautaire MiniBolt, consulté en septembre 2026.

## Votre checklist {#your-checklist}

- [ ] Regardez dans les paramètres réseau de votre wallet quel serveur il utilise aujourd'hui (5 min)
- [ ] Vérifiez le téléchargement de Bitcoin Core, installez-le en mode élagué pour qu'il ne remplisse pas votre disque, et regardez-le se synchroniser (1 h)
- [ ] Choisissez une plateforme et le matériel pour un nœud dédié, avec un SSD de 2 To (1 h)
- [ ] Construisez le nœud, lancez la synchronisation (quelques jours, sans surveillance) et ajoutez un serveur Electrum (1 week-end)
- [ ] Pointez votre wallet vers votre propre nœud et retirez le serveur public (5 min)
