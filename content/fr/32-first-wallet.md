# Chapitre 13 : Votre premier wallet et vos premiers sats

## En bref {#in-brief}

Des bitcoins laissés sur une plateforme d'échange sont une promesse d'une entreprise, alors que des bitcoins dans un wallet (portefeuille) dont vous détenez les clés sont sous votre propre contrôle. Un wallet est une application gratuite qui demande environ 10 minutes d'installation, et vous pouvez apprendre avec une somme proche du prix d'un déjeuner. Installez-en un, notez les mots de récupération, recevez un premier paiement, renvoyez-en une partie, puis essayez un second wallet d'une autre équipe pour comparer.

## Un solde sur une plateforme d'échange est une reconnaissance de dette

Quand vous achetez des bitcoins sur une plateforme d'échange et que vous les y laissez, ce que vous détenez est une ligne dans la base de données de l'entreprise, qui indique qu'elle vous en doit. Tant que l'entreprise reste honnête, solvable, sécurisée et autorisée à vous servir, la différence avec de vrais bitcoins est invisible.

Mt. Gox, qui était la plus grande plateforme d'échange de bitcoins au monde, a déposé son bilan en février 2014 et a annoncé que [environ 850 000 bitcoins avaient disparu](https://www.wired.com/2014/03/bitcoin-exchange/). Son administrateur a effectué les premiers remboursements aux créanciers en juillet 2024 et, en octobre 2026, plus de 12 ans après l'effondrement, il a [repoussé une nouvelle fois la fin des remboursements](https://www.mtgox.com/img/pdf/20261016_b3a13e0f-55f6-4653-913b-be80762390e8_announcement_en.pdf).

FTX, l'une des plus grandes plateformes de son époque, a déposé son bilan en novembre 2022, quelques jours après la suspension des retraits. Son fondateur a été reconnu coupable de fraude en novembre 2023 et [condamné à 25 ans de prison](https://www.justice.gov/archives/opa/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes) en mars 2024. Entre des événements de cette ampleur, il y en a de plus ordinaires, comme des comptes gelés, des retraits suspendus et des plateformes piratées, que les utilisateurs de Bitcoin résument par la formule « Not your keys, not your coins » (« pas vos clés, pas vos pièces »).

## Un wallet détient des clés, pas des pièces

Chaque bitcoin n'existe que comme une entrée dans la blockchain, le registre public que des milliers d'ordinateurs maintiennent synchronisé. Ce que votre wallet détient, ce sont des **clés**, des nombres secrets qui prouvent au réseau que vous avez le droit de déplacer une entrée donnée. Dépenser revient à signer un message avec votre clé, si bien que celui qui détient la clé contrôle les pièces, sans qu'un nom, un compte ou une autorisation n'intervienne.

L'application est donc une fenêtre et un stylo. Elle vous montre ce que vos clés contrôlent et elle signe quand vous décidez de payer. De nombreux wallets sauvegardent leurs clés sous la forme de 12 ou 24 mots. D'autres formats existent, et la récupération exige un logiciel compatible (chapitre 14). Lightning peut aussi demander des données de récupération propres au wallet.

Il ne vous faut pas non plus un bitcoin entier. 1 bitcoin se divise en 100 millions d'unités appelées **satoshis**, ou **sats**, et un wallet fonctionne de la même façon avec 20 000 sats qu'avec 2 bitcoins, ce qui vous permet d'apprendre avec de petites sommes.

## 2 choix que vous rencontrerez

**On-chain ou Lightning.** Les transactions on-chain sont écrites directement dans la blockchain. Elles prennent de quelques minutes à quelques heures et coûtent des frais qui dépendent de la demande, ce qui convient aux montants plus importants et à l'épargne. Lightning est un réseau de paiement construit au-dessus de Bitcoin, en pratique instantané et très peu cher, qui convient aux petits montants du quotidien (chapitre 15).

**Custodial ou en self-custody.** Un wallet custodial fonctionne comme une petite plateforme d'échange, car une entreprise détient les clés et vous affiche un solde. Un wallet en self-custody garde les clés sur votre téléphone.

Un wallet custodial est le départ le plus facile possible, sans rien à sauvegarder ni à comprendre, et il est acceptable pour une somme que vous pourriez perdre sans douleur, comme les pièces dans votre poche. Dans l'UE, l'option se réduit toutefois, car les prestataires custodial ont désormais besoin d'une licence et doivent identifier leurs utilisateurs (chapitre 16). La self-custody exige un peu plus de vous, principalement une sauvegarde sérieuse. En contrepartie, aucune entreprise ne peut geler ou perdre votre solde à votre place, même si les plateformes d'échange et les courtiers peuvent encore refuser de vous servir.

## Détenir les clés ne règle pas tout

Avec un wallet custodial, le tiers de confiance est évident, car l'entreprise détient les clés et peut geler ou perdre votre solde. Détenir vos propres clés supprime ce tiers et en laisse 3 plus discrets.

Le premier est le serveur que votre wallet interroge. Un wallet de téléphone ne vérifie pas lui-même la blockchain, il interroge un serveur, généralement celui de l'équipe du wallet, qui apprend vos adresses et votre adresse IP et pourrait afficher un solde erroné, même s'il ne peut pas dépenser vos pièces. Le second est le canal de distribution, car la boutique d'Apple ou de Google et la clé de signature du développeur décident du code qui s'exécute sur votre téléphone. Le 3e, sur Lightning, est le fournisseur de service. Phoenix n'ouvre ses canaux qu'avec le nœud d'ACINQ, qui voit généralement où vont vos paiements et pourrait refuser de les relayer, tandis que les wallets construits sur Spark dépendent d'[un petit groupe d'opérateurs](https://docs.spark.money/spark/trust-model). Les 2 conceptions conservent une sortie vers la blockchain, moyennant un coût.

Chacun de ces points peut être en partie vérifié. Le code open source peut être lu, [WalletScrutiny](https://walletscrutiny.com/methodology/) teste si l'application de la boutique peut être reconstruite à partir de ce code (un build reproductible), et plusieurs wallets permettent de se connecter à votre propre nœud (chapitre 18).

## Choisir votre wallet

Tous les wallets ci-dessous sont gratuits, et il est utile d'en essayer 2 d'équipes différentes, afin qu'un problème avec une application ou un service ne vous empêche jamais de payer.

La première ligne, [Bitkit](https://bitkit.to/), est le choix éditorial de ce livre pour un premier wallet. L'application, publiée par Synonym pour iPhone et Android, affiche 2 soldes sur 1 écran, l'épargne détenue on-chain et les dépenses détenues sur Lightning, derrière 1 liste de 12 mots. Vous pouvez recevoir sur Lightning dès la première minute, car le fournisseur de service de Synonym, Blocktank, ouvre un canal à l'arrivée du premier paiement et en déduit ses frais, [environ 1 800 sats dans un cas documenté à la mi-septembre 2026](https://github.com/synonymdev/bitkit-android/issues/1265). Bitkit dépend de Blocktank pour ce canal, et ses connexions Lightning ne sont [pas proposées aux résidents des États-Unis ou du Canada](https://help.bitkit.to/hc/help-center/articles/1702656162-how-do-i-manage-my-spending-balance).

Les 2 dernières lignes reposent sur Ark, une manière de faire des paiements bitcoin off-chain rapides et peu chers, dans laquelle de nombreux utilisateurs partagent les mêmes transactions on-chain via un serveur Ark. Vous conservez des transactions pré-signées qui vous permettent de sortir vers la blockchain par vous-même si ce serveur disparaît. Ark est jeune, puisqu'il a ouvert sur le réseau principal de Bitcoin en [octobre 2025 avec Arkade](https://arklabs.xyz/insights/press-start-arkade-goes-live) et en [juin 2026 avec Bark de Second](https://second.tech/blog/introducing-noah-and-arke/), et sur le serveur de Second un solde [expire après 28 jours sauf si le wallet le renouvelle](https://second.tech/docs/learn/intro). Ouvrez régulièrement un wallet Ark pour qu'il puisse renouveler votre solde. Après l'expiration, le serveur peut récupérer les fonds, et vous ne pouvez les retrouver qu'avec sa coopération. Le tableau est valable en septembre 2026, vérifiez donc le site de chaque projet avant d'installer.

| Wallet | Qui détient les clés | De qui il dépend encore | Réseaux | Open source | Compromis honnête |
|---|---|---|---|---|---|
| **[Bitkit](https://bitkit.to/)** | Vous | Le fournisseur de Synonym, Blocktank, pour les canaux Lightning par défaut. Le serveur Electrum de Synonym pour les données de la blockchain, remplaçable par le vôtre. | On-chain et Lightning, sous forme de 2 soldes dans 1 application | Oui | Un nœud Lightning sur votre téléphone à côté d'un solde d'épargne on-chain, derrière 1 sauvegarde. Le premier paiement Lightning paie le canal (environ 1 800 sats à la mi-septembre 2026, selon les frais de minage), la capacité Lightning totale est plafonnée autour de 999 dollars, et Lightning n'est pas proposé aux résidents des États-Unis ou du Canada. |
| **Phoenix** | Vous | Le nœud d'ACINQ pour chaque paiement Lightning. Des serveurs Electrum pour les données de la blockchain, remplaçables par les vôtres. | Lightning (on-chain en entrée et en sortie via des swaps) | Oui | Un vrai nœud Lightning sur votre téléphone, simple à utiliser. Dépend d'1 entreprise (ACINQ) pour ses canaux. L'ouverture du premier canal [coûte 1 000 sats plus 1 % plus les frais de minage](https://phoenix.acinq.co/faq), donc un très petit premier paiement est refusé. |
| **Breez** (Glow, le successeur de Misty Breez) | Vous | Les opérateurs Spark, qui cosignent chaque transfert, et le logiciel de Breez. | Lightning, via le réseau Spark | Oui | Misty Breez a [perdu ses paiements Lightning et on-chain](https://breez.technology/misty/) en août 2026. Breez renvoie désormais vers Glow, lancé le même mois. Pas de canaux à gérer, mais très récent, et Spark repose sur un petit groupe d'opérateurs. |
| **BlueWallet** | Vous | Les serveurs Electrum de BlueWallet pour les soldes et la diffusion des transactions, remplaçables par les vôtres dans les paramètres. | On-chain | Oui | Clair et bon pour apprendre l'on-chain. Son service Lightning hébergé a fermé en 2023. |
| **Application Blockstream** (anciennement Green) | Vous | Les serveurs de Blockstream par défaut, ou votre propre serveur Electrum. La fédération Liquid, et un service de swap pour Lightning. | On-chain et Liquid. Lightning via des swaps, ou en bêta dans l'application pour ordinateur | Oui | De nombreuses options, fonctionne avec les hardware wallets. Plus de menus pour un débutant. Ses paiements Lightning passaient par des swaps vers Liquid, gérés par Boltz, qui a [suspendu son service le 3 août 2026](https://www.tftc.io/boltz-bitcoin-swaps-suspended-ai-attacks). L'application pour ordinateur a [mis en pause les nouveaux swaps et ajouté Lightning en bêta](https://blog.blockstream.com/blockstream-app-desktop-3-5-0/) le 24 août 2026, vérifiez donc ce qui fonctionne dans votre version. |
| **Zeus** | Vous | Le propre fournisseur de service de Zeus (Olympus) pour les canaux, par défaut. D'autres nœuds Bitcoin pour les données de la blockchain, ou le vôtre. | Lightning et on-chain | Oui | Un vrai nœud Lightning dans votre téléphone, ou une télécommande pour votre propre nœud (chapitre 18). Puissant, mais plus à apprendre. En août 2026, une attaque contre les serveurs de Zeus a [fermé les canaux de nombreux utilisateurs](https://zeusln.com/blog/post-mortem-security-update-august-5th-2026/), sans perte de fonds des clients. |
| **Wallet of Satoshi** | Vous dans l'UE, où son mode custodial [n'est plus disponible depuis janvier 2026](https://www.therage.co/wallet-of-satoshi-eu-mica/). L'entreprise ailleurs. | L'entreprise pour un solde custodial. En mode self-custody, les opérateurs Spark et les serveurs de l'entreprise. | Lightning | Non | Le plus facile de tous. Son mode self-custody repose sur Spark, un système récent qui s'appuie sur un petit groupe d'opérateurs. Argent de poche uniquement. |
| **Bringin** | Vous | Bringin pour le compte en euros optionnel, qu'il peut bloquer comme n'importe quelle entreprise de paiement. Le wallet bitcoin est en self-custody, donc Bringin ne détient pas ces fonds. | Lightning et on-chain | Non précisé sur son site | Wallet lié à un compte en euros optionnel, qui exige une vérification d'identité (chapitre 15). |
| **[Wallet Arkade](https://arkade.money/)** | Vous | Le serveur Arkade géré par Ark Labs, qui cosigne chaque paiement Ark. La sortie vers la blockchain fonctionne sans lui. | Ark et on-chain | Oui | Une application web installée depuis le navigateur, sans boutique d'applications. Bêta publique depuis octobre 2025, et Ark Labs a écrit lors du lancement qu'elle n'est pas prête pour l'épargne. |
| **[Noah](https://beta.noahwallet.io/)** | Vous | Le serveur Ark géré par Second, qui cosigne les paiements et relie le wallet à Lightning. La sortie vers la blockchain fonctionne sans lui. | Ark, Lightning et on-chain | Oui | De l'équipe derrière le wallet Blixt. Bêta pour Android, et pour iPhone via TestFlight. Ses développeurs demandent de ne déposer que ce que vous pouvez vous permettre de perdre. |

Une configuration raisonnable pour la plupart des personnes est un wallet Lightning en self-custody pour les petits montants et un wallet on-chain pour comprendre la couche de base, soit dans 1 application comme Bitkit, soit dans 2 applications distinctes, avec BlueWallet ou l'application Blockstream pour le côté on-chain. Les wallets qui gèrent leurs propres canaux (Bitkit, Phoenix, Zeus) coûtent plus cher le premier jour et dépendent de moins de services extérieurs, tandis que ceux construits sur des swaps ou sur Spark font l'inverse. Essayez-en 2 et gardez celui que vous trouvez clair.

## Pas à pas {#step-by-step}

L'exemple utilise Bitkit. La logique est la même pour les autres.

1. **Installez-le** depuis la boutique officielle. Avant de toucher le bouton d'installation, vérifiez le nom du développeur (Synonym Software pour Bitkit) et suivez le lien depuis le site officiel du projet, bitkit.to, plutôt qu'une recherche dans la boutique. Cette vérification, complétée par un coup d'œil à la page de l'application sur walletscrutiny.com, est l'étape qui remplace la confiance par la vérification, autant qu'un téléphone le permet.
2. **Créez un nouveau wallet.** L'application ne demande ni e-mail, ni nom, ni compte, ce qui est normal.
3. **Notez les mots de récupération avant de recevoir quoi que ce soit.** Trouvez les 12 mots dans les paramètres de sauvegarde, recopiez-les à la main sur papier, et lisez le chapitre 14 avant d'ajouter plus que de l'argent de poche.
4. **Recevez un premier paiement supérieur aux frais de canal.** Touchez Recevoir (Receive), choisissez de recevoir sur le solde de dépenses (spending balance) et affichez le QR code, en gardant l'application ouverte jusqu'à l'apparition du paiement. Blocktank ouvre votre canal à ce moment-là et prélève ses frais sur le montant, 1 835 sats dans [un cas signalé le 15 septembre 2026](https://github.com/synonymdev/bitkit-android/issues/1265), davantage quand les frais de minage augmentent. Le même signalement, encore ouvert le 20 septembre, montre que le minimum suggéré de 2 000 sats peut laisser un solde trop petit pour être dépensé. Demandez un montant réaliste, par exemple 20 000 sats, et lisez les frais affichés par l'application avant d'accepter. Pour tester avec quelques centaines de sats seulement, utilisez un wallet sans canaux (Wallet of Satoshi ou Glow) et acceptez son compromis.
5. **Renvoyez un petit montant.** Scannez le QR code de l'autre personne, vérifiez le montant, confirmez. Il arrive généralement en 1 ou 2 secondes.
6. **Vérifiez les frais** dans le détail du paiement, afin de savoir à quoi ressemblent des frais normaux.
7. **Essayez un second wallet**, envoyez des sats de l'un à l'autre, et comparez.

## Erreurs à éviter {#mistakes-to-avoid}

- **Laisser son épargne sur une plateforme d'échange.** Une plateforme d'échange est utile le temps d'un achat. Ensuite, retirez vers un wallet que vous contrôlez.
- **Prendre une capture d'écran de vos mots de récupération.** Les photos sont souvent synchronisées dans le cloud et peuvent être lues par d'autres applications. Utilisez du papier et un stylo (chapitre 14).
- **Installer un faux wallet.** Les boutiques d'applications contiennent des copies conçues pour voler. Vérifiez le nom du développeur et partez du site officiel du projet.
- **Envoyer vers le mauvais réseau.** Une facture Lightning, une adresse on-chain et une adresse Liquid sont 3 choses différentes. Un bon wallet refuse la mauvaise, et si quelque chose paraît étrange, arrêtez-vous et demandez.
- **Commencer avec une grosse somme.** Les erreurs de débutant arrivent dans les premières semaines, faites-les donc avec une petite somme.
- **Faire confiance à quiconque propose de vous « aider » avec votre wallet en ligne.** Aucune équipe de wallet, aucune plateforme d'échange et aucune autorité n'a besoin de vos mots de récupération.

## Pour aller plus loin {#go-further}

- **Tutoriels pas à pas sur les wallets.** Plan B Academy (planb.academy).
- **Vérifier si un wallet est vraiment open source.** WalletScrutiny (walletscrutiny.com).
- **Guides simples pour débutants.** Bitcoiner.Guide (bitcoiner.guide).
- **Chapitre suivant.** Sauvegarder votre phrase de récupération (seed phrase).

## Sources {#sources}

- [The Inside Story of Mt. Gox, Bitcoin's $460 Million Disaster](https://www.wired.com/2014/03/bitcoin-exchange/), Wired, 3 mars 2014.
- [Notice Concerning Change of Repayment Deadlines](https://www.mtgox.com/img/pdf/20261016_b3a13e0f-55f6-4653-913b-be80762390e8_announcement_en.pdf), MtGox Co., Ltd., administrateur de la réhabilitation, 16 octobre 2026, consulté le 29 octobre 2026.
- [Samuel Bankman-Fried Sentenced to 25 Years for His Orchestration of Multiple Fraudulent Schemes](https://www.justice.gov/archives/opa/pr/samuel-bankman-fried-sentenced-25-years-his-orchestration-multiple-fraudulent-schemes), U.S. Department of Justice, 28 mars 2024.
- [Methodology](https://walletscrutiny.com/methodology/), WalletScrutiny, consulté en septembre 2026.
- [Spark trust model](https://docs.spark.money/spark/trust-model), documentation de Spark, consultée en septembre 2026.
- [Phoenix FAQ: fees, restoring a wallet](https://phoenix.acinq.co/faq), ACINQ, consultée en septembre 2026.
- [How do I manage my spending balance?](https://help.bitkit.to/hc/help-center/articles/1702656162-how-do-i-manage-my-spending-balance) (Blocktank, plafond de 999 dollars, États-Unis et Canada), centre d'aide de Bitkit, Synonym, consulté en septembre 2026.
- [CJIT at suggested minimum yields unspendable channel](https://github.com/synonymdev/bitkit-android/issues/1265) (frais de Blocktank de 1 835 sats sur un premier paiement), suivi des problèmes de Bitkit sur GitHub, 15 septembre 2026.
- [Press Start: Arkade Goes Live](https://arklabs.xyz/insights/press-start-arkade-goes-live), Ark Labs, 20 octobre 2025.
- [Introducing Noah and Arké: Two new Bark-based wallets](https://second.tech/blog/introducing-noah-and-arke/), Second, 10 juin 2026.
- [Intro to the Ark protocol](https://second.tech/docs/learn/intro) (expiration après 28 jours, récupération par le serveur), documentation de Second, consultée le 29 octobre 2026.
- [Boltz Suspends Bitcoin Swaps Indefinitely as AI Attacks Outpace Patching](https://www.tftc.io/boltz-bitcoin-swaps-suspended-ai-attacks), TFTC, 4 août 2026, consulté le 29 octobre 2026.
- [The Blockstream App 3.5.0 for Desktop: Lightning in Beta and Air-Gapped Jade Signing](https://blog.blockstream.com/blockstream-app-desktop-3-5-0/), Blockstream, 24 août 2026, consulté le 29 octobre 2026.

## Votre checklist {#your-checklist}

- [ ] Installez un wallet en self-custody depuis sa source officielle, après avoir vérifié le nom du développeur et sa page sur walletscrutiny.com (5 min)
- [ ] Notez les mots de récupération sur papier avant de recevoir quoi que ce soit (5 min)
- [ ] Recevez un premier paiement supérieur aux frais de mise en place et renvoyez-en une partie (5 min)
- [ ] Installez un second wallet d'une autre équipe et comparez (1 h)
- [ ] Déplacez vers un wallet que vous contrôlez tout ce que vous aviez laissé sur une plateforme d'échange (1 h)
