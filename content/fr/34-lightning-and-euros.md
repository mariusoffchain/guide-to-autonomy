# Chapitre 15 : Lightning et euros au quotidien

## En bref {#in-brief}

La couche de base de Bitcoin est conçue pour être sûre, pas pour vendre du café. Lightning est un réseau de paiement construit au-dessus, en pratique instantané et très peu cher, fait pour les montants du quotidien. Ce chapitre montre comment payer et être payé sur Lightning, où dépenser des sats, et les différentes routes entre bitcoin et euros, chacune avec son coût en frais, en commodité et en confidentialité. Rien ici n'est un conseil en investissement, et les règles fiscales de votre pays s'appliquent toujours.

## Un registre trop lent pour un café

La blockchain Bitcoin ajoute un nouveau bloc environ toutes les 10 minutes, et chaque bloc a un espace limité. La limite est délibérée, car elle garde le registre assez petit pour que des gens ordinaires le vérifient sur leur propre ordinateur (chapitre 18). Le prix de ce choix est qu'un paiement on-chain met généralement de quelques minutes à quelques heures à obtenir des confirmations, sans caractère définitif absolu, et que ses frais augmentent quand beaucoup de gens veulent de la place en même temps, ce qui est acceptable pour déplacer de l'épargne et déraisonnable pour un café.

La seconde difficulté est la passerelle. Les salaires, les loyers et les impôts sont en euros, utiliser bitcoin suppose donc une porte d'entrée et une porte de sortie. La plus connue est une grande plateforme d'échange qui détient vos pièces, vos pièces d'identité et l'historique complet de ce que vous faites. Il existe d'autres routes, décrites plus bas, et elles diffèrent beaucoup entre elles par les frais, la commodité et la confidentialité.

## Des canaux qui touchent la blockchain 2 fois

Lightning repose sur des **canaux de paiement**. 2 participants verrouillent ensemble des bitcoins dans une transaction on-chain, et dès lors ils peuvent déplacer le solde entre eux aussi souvent qu'ils le veulent, en pratique instantanément, en échangeant des mises à jour signées qui ne touchent jamais la blockchain. Seules l'ouverture et la fermeture du canal sont écrites on-chain. Les canaux se connectent en réseau, ce qui permet de payer quelqu'un avec qui vous ne partagez aucun canal, et le paiement transite par des intermédiaires qui ne peuvent pas le garder et qui gagnent généralement une fraction de centime.

En pratique, vous voyez 2 choses.

- **Une facture (invoice)**, une demande de paiement affichée sous la forme d'un QR code ou d'un long texte. Les factures BOLT11 courantes commencent par « lnbc », et les demandes BOLT12, plus récentes, utilisent un autre format. Elle porte généralement sur un montant fixe, sert 1 fois, et expire.
- **Une adresse Lightning**, qui ressemble à une adresse e-mail (you@provider.com) et peut être réutilisée, ce qui est pratique pour les pourboires et pour être payé. La plupart reposent sur le serveur web d'un fournisseur. L'adresse de Phoenix repose sur BOLT12, un standard plus récent que, pour le moment, seuls certains wallets peuvent payer.

Les wallets modernes gèrent les canaux à votre place ou les évitent en passant par un service extérieur via des swaps (chapitre 13).

## Où dépenser ses sats

- **En personne.** [BTC Map](https://btcmap.org/) (btcmap.org) est l'outil pour trouver des lieux, une carte gratuite, tenue par la communauté, des cafés, boutiques, hôtels et freelances qui acceptent bitcoin. Une fiche peut être périmée, regardez donc sa date de dernière vérification, demandez avant de commander, et ajoutez les lieux que vous découvrez.
- **Pourboires et zaps.** Sur Nostr (chapitre 7), vous pouvez envoyer quelques sats à l'auteur d'un message que vous avez aimé, directement, sans plateforme qui prélève une part. De nombreux podcasts et auteurs indépendants publient aussi une adresse Lightning.
- **Entre personnes.** Partager une addition ou rembourser un ami est souvent le premier usage réel.
- **En ligne.** Plusieurs entreprises vendent des cartes cadeaux, des recharges téléphoniques, des eSIM ou des voyages contre des bitcoins, un moyen indirect de vivre de sats là où les commerçants ne les acceptent pas encore. Chaque service du tableau ci-dessous (valable en septembre 2026) est une boutique, pas un wallet, payez donc ce dont vous avez besoin et n'y laissez aucun solde.

| Service | Ce que vous pouvez acheter | Lightning ? | Contrôle d'identité |
|---|---|---|---|
| **[Bitrefill](https://www.bitrefill.com/)** | Cartes cadeaux, recharges téléphoniques, eSIM | Oui | Aucun compte requis pour les achats ordinaires. La vérification relève ses limites d'achat. |
| **[CoinsBee](https://www.coinsbee.com/en/)** (Coinsbee GmbH) | Cartes cadeaux, cartes de paiement, recharges téléphoniques | Oui | [Aucun jusqu'à 1 000 euros par commande et 10 000 euros au total](https://www.coinsbee.com/en/kyc-aml/), vérification au-delà. |
| **[Cryptorefills](https://www.cryptorefills.com/)** (Big Dream Ventures B.V., Amsterdam) | Cartes cadeaux, recharges, eSIM, vols, séjours | Oui | Aucun, selon son site |
| **[Cartes cadeaux CoinGate](https://coingate.com/gift-cards)** | Cartes cadeaux d'environ 6 000 marques | Oui | Aucune inscription nécessaire, selon son site |
| **[Travala](https://www.travala.com/)** | Hôtels, vols, activités | Oui | Coordonnées du voyageur pour la réservation, et la compagnie aérienne ou l'hôtel vérifie votre pièce d'identité comme d'habitude |

## Qui détient les fonds, qui peut bloquer

Pour chaque route, la grille demande qui détient les fonds pendant que le paiement est en cours, et qui peut l'arrêter.

Avec une application custodial, l'entreprise détient les bitcoins jusqu'à votre retrait, et elle peut geler le solde ou refuser un paiement. Avec un wallet Lightning en self-custody, les clés sont les vôtres, mais les paiements passent par un fournisseur de service Lightning (ACINQ pour Phoenix, Blocktank pour Bitkit) ou, dans une conception différente, par un petit groupe d'opérateurs (Spark). Ces services peuvent refuser des transferts. Les wallets Lightning exigent une gestion correcte des canaux et des sauvegardes. Spark repose aussi sur [un seuil d'opérateurs honnêtes pendant les transferts](https://docs.spark.money/learn/trust-model). Une sortie vers la blockchain a ses propres conditions, frais et délais, et détenir les clés ne vous protège donc pas contre toutes les défaillances.

Un courtier soumis au KYC détient vos euros pendant l'achat, et il peut refuser un ordre, demander d'où vient l'argent ou fermer votre compte, tout comme la banque qui envoie le virement. Les plateformes de pair à pair essaient de supprimer le détenteur. Bisq 1 verrouille les pièces dans une [adresse multisignature 2-sur-2](https://bisq.wiki/Security_deposit) partagée par les 2 traders, et Hodl Hodl dans [une adresse 2-sur-3](https://hodlhodl.com/blog/en/escrow-explained) dont la plateforme détient 1 clé, de sorte qu'aucune partie seule ne puisse les déplacer. RoboSats utilise un [paiement Lightning retenu](https://learn.robosats.org/docs/escrow/) (held) envers le coordinateur qui héberge l'ordre. Bisq Easy, le mode d'échange simplifié de Bisq 2, n'a [ni entiercement ni dépôt de garantie](https://bisq.wiki/Bisq_Easy). L'acheteur se fie à la réputation du vendeur, et chaque échange est plafonné à l'équivalent de 600 dollars. La confiance qui subsiste va à l'autre trader et à celui qui tranche un litige.

## Choisir votre passerelle vers les euros

Aucune route n'est la meilleure sur tous les points, car chacune échange la simplicité contre des frais et de la confidentialité. Le **KYC** (« know your customer », « connaître son client ») signifie que le service vérifie votre identité avec une pièce d'identité, ce que les entreprises régulées en Europe doivent désormais faire, et le chapitre 16 explique ce que cela implique pour votre confidentialité. Ce marché évolue vite. Le courtier suisse Pocket Bitcoin, par exemple, a [mis fin à sa vérification allégée en décembre 2025](https://pocketbitcoin.com/blog/posts/full-verification-coming-to-pocket). Du côté pair à pair, [Hodl Hodl](https://hodlhodl.com/), [Bisq](https://bisq.network/) et [RoboSats](https://learn.robosats.org/) vous permettent d'échanger avec une autre personne sans confier vos pièces à une entreprise, selon les modèles décrits dans la section précédente. Le tableau est valable en septembre 2026, et vous devez vérifier dans chaque cas que le service accepte les résidents de votre pays.

| Route | Exemples | Contrôle d'identité (KYC) | Qui détient les pièces | Qui peut la bloquer | Compromis honnête |
|---|---|---|---|---|---|
| **Gagner des sats** | Être payé ou recevoir des pourboires en bitcoin pour du travail, des ventes ou du contenu | Aucun | Vous | Seulement un fournisseur Lightning de l'un ou l'autre côté, en refusant de relayer le paiement | Aucun intermédiaire du tout. Il vous faut quelqu'un prêt à payer ainsi, et le revenu reste imposable. |
| **Échange de pair à pair** | Hodl Hodl (web), Bisq (ordinateur), RoboSats (Lightning, via Tor) | Généralement aucun de la part de la plateforme. Hodl Hodl peut en demander en cas de litige. | Vous. Les pièces ne sont bloquées en entiercement que pendant l'échange, là où la plateforme en propose un. | L'autre trader, en ne payant pas, et les banques des 2 côtés. Un médiateur ou un arbitre tranche les litiges. | Vous échangez avec une personne par virement bancaire. Plus confidentiel, généralement plus cher, plus lent, plus à apprendre. |
| **Courtier européen, achats récurrents** | Relai, Pocket Bitcoin (tous les 2 suisses) | Oui | Vous. Ils livrent vers votre propre wallet. | Le courtier, qui peut refuser un ordre ou fermer votre compte, et votre banque, qui peut bloquer le virement | Très simple, automatique. Des frais sur chaque achat, et l'entreprise sait qui vous êtes et ce que vous avez acheté. |
| **Compte en euros plus wallet bitcoin** | Bringin (IBAN en euros et carte Visa facultative à côté d'un wallet en self-custody), Strike (dépôts SEPA, entièrement custodial) | Oui | Chez Bringin, vous, pour les bitcoins. Chez Strike, l'entreprise, pour tout, jusqu'à ce que vous retiriez vers votre propre wallet. | Bringin pour le compte en euros et la carte, qu'il peut bloquer comme n'importe quelle entreprise de paiement régulée, mais pas les bitcoins, qui se trouvent dans un wallet en self-custody. Strike est custodial, donc l'entreprise détient les clés de vos euros comme de vos bitcoins et a tous les droits sur eux, elle peut geler le solde, refuser un paiement ou fermer le compte. | Pratique pour passer des sats aux euros. 1 entreprise voit les 2 côtés, chaque conversion comporte des frais, et le côté euros est un compte régulé comme un autre. |
| **Distributeur de bitcoins** | Machines répertoriées sur coinatmradar.com | Généralement oui dans l'UE, selon l'opérateur et le montant | Vous | L'opérateur, qui fixe des limites et peut refuser une transaction | Espèces en entrée, pièces en sortie en quelques minutes. Les frais sont généralement les plus élevés de toutes les routes. Les escrocs demandent souvent à leurs victimes de déposer des espèces dans un distributeur de bitcoins, et [les personnes âgées sont celles qui perdent le plus](https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2024/08/bitcoin-atms-payment-portal-scammers). Aucune banque, aucune police et aucun service d'assistance ne vous demandera jamais de le faire. |

Une configuration raisonnable pour la plupart des personnes qui décident d'échanger des euros est une route régulée qu'elles trouvent claire, utilisée uniquement pour livrer des pièces à leur propre wallet, et une route de pair à pair apprise avec de petites sommes, afin de ne pas dépendre d'une porte unique. Quelle que soit la route, vendre ou dépenser des bitcoins peut créer une obligation fiscale, conservez donc des justificatifs et vérifiez les règles de votre pays.

## Pas à pas {#step-by-step}

Les étapes sont les mêmes dans la plupart des wallets Lightning, y compris celui que vous avez installé au chapitre 13.

1. **Payez une facture.** Chez un commerçant ou lors d'un meetup, touchez Envoyer (Send) et scannez le QR code. Vérifiez le montant et les frais affichés, puis confirmez. Le commerçant voit généralement le paiement en 1 ou 2 secondes.
2. **Recevez avec une facture.** Touchez Recevoir (Receive), saisissez un montant si vous le souhaitez, et affichez le QR code. Rappelez-vous qu'il expire. Dans un wallet qui ouvre ses propres canaux, comme Bitkit ou Phoenix, le premier paiement doit dépasser les frais de canal (chapitre 13).
3. **Recevez avec une adresse Lightning.** Si votre wallet en propose une, trouvez-la dans les paramètres ou sur l'écran de réception, et testez-la depuis un second wallet avant de la publier. L'adresse de Phoenix utilise BOLT12, que de nombreux wallets ne savent pas encore payer. Une adresse issue d'un wallet custodial ou basé sur Spark fonctionne avec presque tous les expéditeurs, avec les compromis décrits au chapitre 13.
4. **Retirez depuis un courtier ou une application vers votre PROPRE wallet.** Choisissez « retirer » (withdraw) ou « envoyer » (send), collez une adresse ou une facture générée par votre wallet, et commencez par un petit test. Voir les pièces arriver dans un wallet dont vous détenez les clés est l'étape qui remplace la confiance dans un solde affiché par la vérification. Pour des montants plus importants, retirez on-chain vers votre wallet d'épargne (chapitres 14 et 17).
5. **Ne gardez que de l'argent à dépenser sur le téléphone.** Voyez le wallet Lightning comme le portefeuille que vous avez en poche. Quand il contient plus que ce que vous porteriez en espèces, déplacez le surplus on-chain.
6. **Conservez des justificatifs.** Exportez ou notez vos achats et vos ventes avec les dates et les montants, car vous en aurez besoin pour la déclaration d'impôts.

## Erreurs à éviter {#mistakes-to-avoid}

- **Garder son épargne dans un wallet Lightning de téléphone.** Il vit sur un appareil que vous pouvez perdre ou casser, connecté à internet toute la journée, il convient donc à l'argent à dépenser.
- **Confondre une facture avec une adresse on-chain.** Une facture BOLT11 commence par « lnbc » et expire, et BOLT12 utilise d'autres formats. Une adresse on-chain commence par « bc1 », « 1 » ou « 3 » et n'expire pas. Quand vous retirez depuis un service, sélectionnez le réseau correspondant.
- **Faire de gros paiements sur Lightning.** Les canaux ont une capacité limitée, et les gros paiements échouent plus souvent. Lightning sert aux montants du quotidien, et l'on-chain gère le reste.
- **Laisser les pièces chez le courtier.** Un achat est terminé quand les pièces sont dans votre wallet, pas quand l'application affiche un solde (chapitre 13).
- **Ignorer le coût total.** Comparez le montant final de sats que vous recevez, pas les frais annoncés, car le taux de change cache souvent une marge.
- **Oublier le volet fiscal.** Payer en bitcoin peut compter comme le vendre, et les règles diffèrent selon les pays.

## Pour aller plus loin {#go-further}

- **Trouver des lieux où dépenser.** BTC Map (btcmap.org).
- **Tutoriels pour les wallets et plateformes d'échange ci-dessus.** Plan B Academy (planb.academy).
- **Comprendre Lightning en profondeur.** « Mastering the Lightning Network », à lire gratuitement en ligne (github.com/lnbook/lnbook).
- **Chapitre suivant.** La confidentialité dans Bitcoin.

## Sources {#sources}

- [Spark trust model](https://docs.spark.money/learn/trust-model), documentation de Spark, consultée le 22 octobre 2026.
- [Important Update: Full Verification Coming to Pocket](https://pocketbitcoin.com/blog/posts/full-verification-coming-to-pocket), Pocket Bitcoin, 16 octobre 2025.
- [Security deposit](https://bisq.wiki/Security_deposit), Bisq Wiki, consulté en septembre 2026.
- [What is multisig escrow and how it works](https://hodlhodl.com/blog/en/escrow-explained), Hodl Hodl, consulté en septembre 2026.
- [Trade escrow](https://learn.robosats.org/docs/escrow/), Learn RoboSats, consulté en septembre 2026.
- [Bisq Easy](https://bisq.wiki/Bisq_Easy) (pas de dépôt de garantie, réputation du vendeur, échanges de 6 à 600 dollars), Bisq Wiki, consulté le 29 octobre 2026.
- [Bitcoin ATMs: A payment portal for scammers](https://www.ftc.gov/news-events/data-visualizations/data-spotlight/2024/08/bitcoin-atms-payment-portal-scammers), Federal Trade Commission des États-Unis, septembre 2024.
- [Bringin: wallet, euro account and fees](https://bringin.app/), Bringin, consulté en septembre 2026.
- [KYC and AML: purchase limits](https://www.coinsbee.com/en/kyc-aml/), CoinsBee, consulté en septembre 2026.

## Votre checklist {#your-checklist}

- [ ] Payez une facture Lightning, chez un commerçant ou lors d'un meetup (5 min)
- [ ] Obtenez une adresse Lightning et testez-la depuis un second wallet (5 min)
- [ ] Trouvez 3 lieux près de chez vous sur btcmap.org (5 min)
- [ ] Retirez tout solde d'un courtier ou d'une plateforme d'échange vers votre propre wallet (1 h)
- [ ] Lisez comment fonctionne une plateforme d'échange de pair à pair, avant d'en avoir besoin (1 h)
