# Chapitre 16 : Confidentialité dans Bitcoin

## En bref {#in-brief}

Bitcoin ne masque pas le graphe de ses transactions à sa couche de base. Les transactions restent publiques, et l'identification de leurs propriétaires dépend d'informations extérieures et d'heuristiques. Une adresse, cependant, ne porte aucun nom. Elle se rattache à vous par le contrôle d'identité d'une plateforme d'échange, ou par les personnes avec qui vous faites des transactions et qui vous connaissent, et de là un observateur peut relier un wallet à une personne. Quelques habitudes réduisent considérablement cette exposition (des adresses neuves, des wallets séparés, des pièces étiquetées, votre propre nœud, Lightning pour les dépenses courantes), et des outils avancés comme le coinjoin et le payjoin vont plus loin. Aucun d'entre eux ne modifie vos obligations légales ou fiscales.

## Un registre public qui n'oublie jamais

Votre relevé bancaire est vu par vous et par votre banque, alors que le registre Bitcoin peut être lu par n'importe qui, et rien n'en est jamais effacé. Ceux qui disent que Bitcoin manque de confidentialité ont raison à propos de cette couche de base, parce que le graphe des transactions reste disponible pour l'analyse, même quand ses propriétaires ne peuvent pas être identifiés de façon fiable.

Ceux qui répondent qu'une adresse n'est pas une identité ont raison eux aussi, jusqu'à un certain point. Une adresse ne porte aucun nom, et elle n'en reçoit un que par un lien établi ailleurs. Une plateforme d'échange qui a vérifié votre identité sait où vous avez retiré vos pièces. Les personnes avec qui vous faites des transactions vous connaissent, comme une boutique en ligne qui a votre nom et voit l'adresse depuis laquelle vous avez payé. Des sociétés d'analyse en ont fait un commerce, en collectant ces liens, en regroupant les adresses par propriétaire et en vendant le résultat, ce qui permet à un observateur de relier un wallet à une personne physique.

À partir de ce moment, l'activité passée et future liée à cette adresse peut être suivie par un commerçant, un employeur, un propriétaire ou une connaissance curieuse.

L'enjeu est aussi physique. En janvier 2025, [David Balland, cofondateur de Ledger, a été enlevé à son domicile en France](https://www.coindesk.com/policy/2025/01/24/ledger-co-founder-s-kidnapping-sheds-light-on-soaring-crypto-robberies) et les agresseurs ont exigé une rançon en cryptomonnaie avant que la police ne libère David Balland ainsi que son ou sa partenaire. Le développeur Jameson Lopp tient [une liste publique des agressions physiques contre des détenteurs de bitcoins](https://github.com/jlopp/physical-bitcoin-attacks).

## Les gros mouvements se voient, les particuliers ont des outils

Avec la monnaie fiat, les plus grands acteurs peuvent placer de grosses transactions derrière des structures financières, comme des sociétés holding, des trusts et des comptes dans plusieurs juridictions, tandis que l'usage quotidien des services bancaires par la population est étroitement surveillé, paiement par paiement. Avec Bitcoin, c'est plutôt l'inverse. La confidentialité peut être plus difficile à obtenir pour de très gros montants, car un coinjoin a besoin d'autres participants et d'un ensemble utile de sorties plausibles, de sorte que lorsqu'un État ou une grande institution déplace des bitcoins, cela se voit généralement sur le registre public. À l'été 2024, le Land allemand de Saxe a [vendu environ 49 858 bitcoins saisis entre le 19 juin et le 12 juillet](https://www.medienservice.sachsen.de/medien/news/1077662), et la presse a [suivi les transferts depuis le wallet étiqueté vers les plateformes d'échange](https://cointelegraph.com/news/german-government-354m-btc-sell-off) jour après jour, à l'aide des données de la société d'analyse Arkham.

Un particulier, en revanche, dispose d'outils pour gagner en confidentialité et résister à la désanonymisation, que le reste de ce chapitre présente. Cela demande du soin et un peu d'apprentissage, mais quelqu'un qui les applique correctement peut, en pratique, utiliser Bitcoin de façon privée.

## 3 schémas qui vous trahissent

Vos bitcoins s'imaginent mieux comme des pièces séparées de tailles différentes, comme des billets dans un porte-monnaie, que comme un solde de compte. Chaque pièce que vous avez reçue figure sur le registre public avec son montant et son adresse.

3 schémas simples révèlent beaucoup.

- **Réutilisation d'adresse.** Si vous recevez 10 paiements sur la même adresse, n'importe qui peut voir les 10, les additionner, et observer quand ils bougent.
- **Entrées fusionnées.** Quand vous payez, votre wallet peut combiner plusieurs pièces en 1 transaction, comme payer avec 2 billets. Un observateur en conclut que les 2 pièces appartiennent à la même personne, si bien que 1 pièce portant votre nom identifie désormais l'autre.
- **La monnaie rendue (change).** Si vous payez 30 avec une pièce de 50, les 20 restants reviennent vers une nouvelle adresse à vous. Les observateurs peuvent souvent deviner quelle sortie est la monnaie rendue, et continuer à vous suivre.

Les analystes combinent ces suppositions, appelées heuristiques. Elles ne sont pas toujours exactes, mais elles suffisent à construire un profil, et de bonnes habitudes de confidentialité leur laissent moins de matière.

## Le KYC et ce qu'il implique

Le KYC signifie « know your customer » (« connaître son client »), la vérification d'identité que les plateformes d'échange régulées doivent effectuer. Vous envoyez une copie de votre pièce d'identité, souvent avec un selfie et un justificatif de domicile. C'est une obligation légale pour l'entreprise, et utiliser un tel service est légal et courant.

Il crée toutefois un lien durable entre votre identité et vos pièces, stocké dans la base de données d'une entreprise. Dans l'Union européenne, [le règlement MiCA](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica) s'applique aux prestataires de services sur crypto-actifs depuis le 30 décembre 2024, avec une période de transition qui s'est terminée le 1er juillet 2026. Depuis le 1er janvier 2026, [la directive DAC8](https://taxation-customs.ec.europa.eu/taxation/tax-transparency-cooperation/administrative-co-operation-and-mutual-assistance/directive-administrative-cooperation-dac/dac8_en) exige aussi de ces prestataires qu'ils collectent des données sur les transactions de leurs utilisateurs résidant dans l'UE et les déclarent aux administrations fiscales, qui les échangent entre États membres à partir de 2027. Des bases de données de ce type peuvent fuiter, et une liste de personnes qui détiennent des bitcoins, avec leur adresse personnelle, intéresse évidemment les criminels.

Bitcoin peut aussi être acquis sur des marchés de pair à pair, où vous échangez directement avec une autre personne et où aucune entreprise centrale ne collecte vos documents. C'est légal dans la plupart des endroits, mais les règles diffèrent, vérifiez donc les vôtres. Vos obligations fiscales restent exactement les mêmes quelle que soit la manière dont vous avez acquis vos pièces, conservez donc vos propres justificatifs.

## Qui apprend quelles pièces sont les vôtres

Le registre montre des adresses sans noms, votre confidentialité dépend donc des parties capables d'y rattacher votre nom.

La première est le serveur que votre wallet interroge. Un wallet qui ne détient pas le registre interroge un serveur sur chacune de ses adresses, et par défaut ce serveur appartient au fabricant du wallet ou à un bénévole. D'après [la documentation de Sparrow](https://sparrowwallet.com/docs/best-practices.html), un serveur public apprend votre solde et, via votre adresse IP, votre localisation. Il peut ne rien journaliser, mais vous ne pouvez pas le vérifier.

La seconde est la plateforme d'échange qui a vérifié votre identité, qui connaît votre nom, votre adresse personnelle et l'endroit où vous avez retiré, et qui peut être piratée ou contrainte de remettre ses dossiers. En mai 2025, Coinbase a révélé que des données de clients avaient été copiées depuis ses systèmes d'assistance, et [sa déclaration comptait 69 461 personnes](https://cointelegraph.com/news/70k-impacted-coinbase-data-breach-maine-attorneys). Les sociétés d'analyse sont des observateurs, qui travaillent à partir du registre public et des données qu'elles obtiennent.

Ni le serveur ni la plateforme d'échange ne peuvent être audités de l'extérieur, la voie pratique consiste donc à les supprimer là où c'est important, avec votre propre nœud, Tor en attendant et l'acquisition de pair à pair, chacun au prix de la commodité. Pour un débutant, une plateforme d'échange régulée reste souvent plus sûre face aux arnaques, au prix d'une perte durable de confidentialité.

## Choisir vos habitudes de confidentialité

La confidentialité dans Bitcoin vient d'un ensemble d'habitudes plutôt que d'1 outil. Chacune aide à elle seule, commencez donc par le haut du tableau.

| Habitude | Outils | Effort | Ce que vous gagnez | Qui apprend encore quelque chose |
|---|---|---|---|---|
| **Ne jamais réutiliser une adresse** | Tout wallet moderne donne une adresse neuve pour chaque paiement | Aucun | Évite le lien direct créé en recevant plusieurs fois sur 1 même adresse. Une dépense ultérieure peut encore relier des paiements | Le serveur que votre wallet interroge voit toujours toutes ces adresses ensemble |
| **Des wallets séparés pour des usages séparés** | N'importe quel wallet, pour l'épargne, les dépenses, les pièces KYC, les pièces non-KYC | Faible | Réduit les liens accidentels entre usages. Des serveurs partagés et des transactions ultérieures peuvent encore les relier | Le même serveur, si les 2 wallets l'interrogent depuis la même adresse IP |
| **Étiqueter vos pièces et utiliser le contrôle des pièces (coin control)** | Sparrow Wallet, Nunchuk, Electrum (tous open source) | Moyen | Vous décidez quelle pièce paie, et vous évitez de fusionner des pièces par accident | Personne de nouveau, puisque les étiquettes restent dans votre fichier de wallet. Sauvegardez ce fichier |
| **Vous connecter à votre propre nœud** | Voir le chapitre 18 | Élevé (un week-end de travail, puis quelques jours de synchronisation) | Aucun serveur extérieur n'apprend quelles adresses sont les vôtres | Personne pour votre solde. D'autres nœuds voient la transaction que vous diffusez, sauf si votre nœud utilise Tor |
| **Utiliser Lightning pour les dépenses courantes** | Voir le chapitre 15 | Faible | Les paiements individuels ne sont pas écrits sur le registre public | Un wallet custodial voit chaque paiement. Le fournisseur de service (LSP) d'une application en self-custody en voit encore une partie |
| **Utiliser Tor dans votre wallet** | Sparrow inclut Tor. Electrum et plusieurs autres ont un paramètre de proxy, qui demande que Tor soit installé séparément | Faible à moyen | Le serveur auquel vous vous connectez ne voit pas votre adresse IP | Le serveur voit toujours vos adresses. Les relais Tor sont gérés par des bénévoles et transportent du trafic chiffré |
| **Acquisition de pair à pair** | Bisq (ordinateur, open source, aucune entreprise au milieu), RoboSats (open source, via Tor et Lightning), Hodl Hodl (plateforme web gérée par une entreprise, entiercement multisignature) | Moyen | Aucun document d'identité stocké dans la base de données d'une plateforme d'échange | L'autre trader, qui voit votre nom sur un virement bancaire. La plateforme voit l'échange, pas votre pièce d'identité |
| **Coinjoin et payjoin** (avancé, voir ci-dessous) | Pour le coinjoin, Wasabi Wallet avec un coordinateur indépendant, JoinMarket (désormais joinmarket-ng, avec l'interface Jam), Ashigaru. Pour le payjoin, BTCPay Server, Bull Bitcoin, Cake Wallet | Élevé pour le coinjoin (frais, temps, discipline ensuite). Faible pour le payjoin, quand les 2 côtés le prennent en charge | Affaiblit les heuristiques de propriété commune ou de monnaie rendue, selon le protocole et la façon dont vous dépensez ensuite | Un coordinateur voit que vous participez, mais par conception pas quelle sortie est la vôtre. Certaines plateformes d'échange mettent en doute les pièces issues d'un coinjoin |
| **Convertir une petite somme en Monero pour la dépenser** (avancé, voir ci-dessous) | Logiciel de swap atomique (eigenwallet, open source, non-custodial) ou marchés de pair à pair qui listent Monero (Bisq) | Moyen à élevé | Un paiement beaucoup moins susceptible d'être relié à votre identité, puisque Monero masque par défaut les montants, les expéditeurs et les destinataires | La contrepartie du swap voit le côté bitcoin. Un outil pour dépenser, pas pour épargner |

Lightning protège mieux le payeur que le destinataire, et un wallet Lightning custodial voit tous vos paiements. Les plateformes de pair à pair ne fonctionnent pas dans tous les pays, vérifiez donc le vôtre.

Une configuration raisonnable pour la plupart des personnes est constituée d'adresses neuves, de 1 wallet par usage, d'étiquettes dès le premier jour et de Lightning pour les petits paiements, puis de votre propre nœud quand vous serez prêt. Les 2 dernières lignes sont avancées, et les 3 prochaines sections les expliquent.

## Coinjoin, payjoin et mixeurs

Les 3 schémas reposent sur des suppositions, et certains outils sont conçus pour les faire échouer. Dans un **coinjoin**, plusieurs personnes construisent ensemble 1 transaction, avec de nombreuses entrées et de nombreuses sorties de mêmes montants, de sorte que la propriété des pièces est plus difficile à déduire à partir de cette seule transaction. Les montants, le moment et les dépenses ultérieures peuvent encore fournir des indices. Personne ne cède la garde de ses pièces, car chaque participant ne signe que si sa propre sortie y figure. Dans un **payjoin**, l'expéditeur et le destinataire apportent tous les 2 des entrées à un paiement, ce qui brise l'hypothèse que toutes les entrées d'une transaction appartiennent à 1 personne, et masque le montant réellement payé. Les **mixeurs** sont l'approche plus ancienne, un service qui prend vos pièces et vous en renvoie d'autres. Il est custodial, l'opérateur peut donc garder l'argent ou les journaux.

En septembre 2026, le coinjoin est utilisable dans [Wasabi Wallet](https://docs.wasabiwallet.io/using-wasabi/CoinJoin.html), via des coordinateurs indépendants depuis que son fabricant a fermé le sien en juin 2024, dans JoinMarket, un marché de pair à pair sans coordinateur, [poursuivi sous le nom de joinmarket-ng depuis que le dépôt d'origine a été archivé en avril 2026](https://atlas21.com/coinjoin-comparison-of-tools-to-improve-privacy-on-bitcoin/), et dans Ashigaru, un fork de Samourai Wallet qui a [relancé le coinjoin Whirlpool en juin 2025](https://ashigaru.rs/news/announcement-whirlpool/). Le payjoin fonctionne dans BTCPay Server pour les commerçants, et [dans les applications Bull Bitcoin et Cake Wallet](https://bitcoinops.org/en/topics/payjoin/) depuis 2025.

## Légal à utiliser, poursuivi à exploiter

Utiliser ces outils pour protéger votre vie privée financière est légal dans la plupart des endroits, mais la loi diffère selon les pays et évolue, vérifiez donc la vôtre, et ce que vous devez déclarer reste identique. Les poursuites jusqu'ici ont visé les opérateurs. Aux États-Unis, les 2 fondateurs de Samourai Wallet, arrêtés en avril 2024, ont plaidé coupable de complot en vue d'exploiter une entreprise de transmission de fonds sans licence qui déplaçait sciemment le produit d'activités criminelles, et ont été [condamnés en novembre 2025 à 5 et 4 ans de prison](https://www.irs.gov/compliance/criminal-investigation/founders-of-samourai-wallet-cryptocurrency-mixing-service-sentenced-to-five-and-four-years-in-prison). Roman Storm, développeur de Tornado Cash, un mixeur sur Ethereum, a été [reconnu coupable d'une infraction similaire le 6 août 2025](https://www.irs.gov/compliance/criminal-investigation/founder-of-tornado-cash-crypto-mixing-service-convicted-of-knowingly-transmitting-criminal-proceeds). Le jury n'est pas parvenu à un verdict sur les chefs de blanchiment d'argent et de sanctions, ce qui laisse une partie de l'affaire ouverte en septembre 2026, bien que le Trésor américain ait [levé ses sanctions contre Tornado Cash le 21 mars 2025](https://home.treasury.gov/news/press-releases/sb0057).

Aux Pays-Bas, Alexey Pertsev, un autre développeur de Tornado Cash, a été [condamné à 64 mois de prison en mai 2024](https://www.coindesk.com/policy/2024/05/14/tornado-cash-developer-alexey-pertsev-found-guilty-of-money-laundering) et a fait appel. Aucun de ces développeurs n'est accusé d'avoir volé quoi que ce soit. Ce qu'on leur reproche, c'est d'avoir écrit et exploité un logiciel que des criminels ont aussi utilisé, tout comme des personnes qui cherchaient une confidentialité financière ordinaire. Ces sources n'établissent pas quelle part des utilisateurs appartenait à chacun de ces groupes. Pour de nombreux développeurs et organisations de défense des libertés civiles, c'est une atteinte grave à la liberté d'expression et à la liberté de créer, car publier du code est une forme d'expression et un outil de confidentialité ne choisit pas ses utilisateurs, pas plus que le chiffrement ou les espèces. Plusieurs de ces affaires sont encore devant les tribunaux en septembre 2026.

Ces affaires expliquent pourquoi des coordinateurs ferment ou refusent des utilisateurs de certains pays, et pourquoi certaines plateformes d'échange mettent en doute les pièces issues d'un coinjoin. Un débutant n'a pas besoin de commencer par là.

## Monero pour dépenser, pas pour épargner

Certains utilisateurs avancés gardent bitcoin comme l'actif qu'ils détiennent sur le long terme, et convertissent une petite somme en Monero quand ils veulent un paiement moins susceptible d'être relié à leur identité. Monero est une monnaie distincte, au but proche, de l'argent que vous pouvez détenir vous-même, où les montants, les expéditeurs et les destinataires sont masqués par défaut, ce qui est sa vraie force.

Il est cependant moins sûr comme lieu de conservation de valeur, parce qu'il est beaucoup moins liquide et beaucoup moins accepté, que son logiciel client est développé par un groupe plus petit et plus centralisé, et que son réseau, beaucoup plus petit, est plus facile à attaquer pour une entité extérieure. En septembre 2025, un petit pool de minage, Qubic, [a annulé 118 transactions confirmées](https://www.coindesk.com/web3/2025/09/15/monero-suffers-deepest-ever-blockchain-reorganization-invalidating-118-transactions) par une réorganisation de 18 blocs (chapitre 12).

Les swaps se font avec un logiciel de swap atomique non-custodial comme eigenwallet, ou sur des marchés de pair à pair comme Bisq, puisque les plateformes régulées en Europe retirent Monero. Le [règlement européen de lutte contre le blanchiment de 2024](https://eur-lex.europa.eu/eli/reg/2024/1624/oj) leur interdit, à partir du 10 juillet 2027, de tenir des comptes qui utilisent des « monnaies renforçant l'anonymat » (anonymity-enhancing coins). Des sites de swap instantané existent aussi, mais ils détiennent vos pièces pendant le swap. Les obligations légales et fiscales s'appliquent toujours, et dans de nombreux pays un swap est un fait générateur d'impôt. Le chapitre 12 compare Bitcoin et Monero comme lieux de conservation de valeur.

## Pas à pas {#step-by-step}

L'exemple utilise Sparrow Wallet sur un ordinateur. Nunchuk et Electrum offrent les mêmes fonctions sous des noms légèrement différents.

1. **Créez 1 wallet par usage.** Par exemple l'épargne, les dépenses, et un wallet séparé pour les pièces venues d'une plateforme d'échange avec vérification d'identité.
2. **Recevez sur une adresse neuve à chaque fois.** L'écran de réception (Receive) en propose automatiquement une nouvelle. Ne copiez jamais une ancienne adresse depuis votre historique.
3. **Étiquetez chaque paiement à son arrivée.** Écrivez d'où il vient, par exemple « plateforme d'échange, mars » ou « vendu mon vélo à un voisin ». Dans 6 mois, vous ne vous en souviendrez plus.
4. **Choisissez quelle pièce paie.** Avant d'envoyer, ouvrez la liste de vos pièces (Sparrow l'appelle UTXOs), sélectionnez celle qui convient, et envoyez depuis elle. Évitez de combiner des pièces de sources différentes.
5. **Étiquetez la monnaie rendue.** La pièce qui vous revient hérite de l'historique du paiement, notez-la donc.
6. **Payez les petites choses sur Lightning** (chapitre 15), et gardez les transactions on-chain pour les mouvements plus importants et plus rares.
7. **Activez Tor** dans les paramètres de serveur ou de réseau du wallet si vous utilisez encore un serveur public. Plus tard, remplacez le serveur public par votre propre nœud (chapitre 18). Tor ne cache votre adresse IP qu'à ce serveur, alors que le nœud est l'étape qui supprime le tiers, parce que les questions sur vos adresses ne quittent plus votre domicile.

## Erreurs à éviter {#mistakes-to-avoid}

- **Publier des adresses ou des soldes.** Une capture d'écran de votre wallet sur les réseaux sociaux relie votre nom à vos pièces, et supprimer la publication plus tard n'y change rien, car des copies circulent et le registre garde tout.
- **Fusionner des pièces KYC et non-KYC.** Une transaction qui les combine dit à tous les observateurs qu'elles appartiennent à la même personne, gardez-les donc dans des wallets séparés. Le but est d'éviter de montrer tout votre historique à un commerçant, et cela ne change rien à ce que vous devez déclarer.
- **Réutiliser une adresse de dons.** Une adresse statique unique montre à chaque donateur ce que tous les autres ont donné, et ce que vous en avez fait. Utilisez un outil qui génère une nouvelle adresse par donateur, ou Lightning.
- **Croire qu'un VPN rend Bitcoin privé.** Un VPN cache votre adresse IP à un serveur. Il ne fait rien pour le registre, qui est public pour tout le monde.
- **Parler de ce que vous possédez.** Les analystes travaillent à partir du registre, mais une conversation livre la même information plus vite. Personne n'a besoin de connaître le chiffre, en ligne ou lors d'un dîner.
- **Viser la perfection et ne rien faire.** Les étiquettes et les wallets séparés peuvent commencer aujourd'hui, alors que le nœud et les techniques avancées peuvent attendre.

## Pour aller plus loin {#go-further}

- **Le texte de référence.** La page « Privacy » du Bitcoin Wiki (en.bitcoin.it). Longue, mais complète.
- **Coinjoin et payjoin expliqués.** La documentation de Wasabi Wallet (docs.wasabiwallet.io) et le projet Payjoin (payjoin.org).
- **Guides pratiques.** Bitcoiner.Guide, par BitcoinQ+A (bitcoiner.guide), et la documentation de Sparrow Wallet (sparrowwallet.com/docs) pour les étiquettes et le contrôle des pièces.
- **Chapitre suivant.** Les hardware wallets.

## Sources {#sources}

- [Protect your privacy](https://bitcoin.org/en/protect-your-privacy), Bitcoin.org, consulté le 22 octobre 2026.
- [DAC8, the directive on the reporting of crypto-asset transactions](https://taxation-customs.ec.europa.eu/taxation/tax-transparency-cooperation/administrative-co-operation-and-mutual-assistance/directive-administrative-cooperation-dac/dac8_en), Commission européenne, applicable depuis le 1er janvier 2026.
- [Markets in Crypto-Assets Regulation (MiCA)](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica), Autorité européenne des marchés financiers, page consultée en septembre 2026.
- [Regulation (EU) 2024/1624 on the prevention of money laundering](https://eur-lex.europa.eu/eli/reg/2024/1624/oj), adopté le 31 mai 2024 et publié au Journal officiel de l'Union européenne le 19 juin 2024.
- [Monero Suffers Deepest-Ever Blockchain Reorganization, Invalidating 118 Transactions](https://www.coindesk.com/web3/2025/09/15/monero-suffers-deepest-ever-blockchain-reorganization-invalidating-118-transactions), CoinDesk, 15 septembre 2025.
- [Notveräußerung von fast 50.000 Bitcoins abgeschlossen](https://www.medienservice.sachsen.de/medien/news/1077662), Generalstaatsanwaltschaft Dresden, Land libre de Saxe, 16 juillet 2024 (en allemand).
- [German gov't $354M BTC sell-off](https://cointelegraph.com/news/german-government-354m-btc-sell-off), Cointelegraph, 10 juillet 2024.
- [Coinjoin](https://docs.wasabiwallet.io/using-wasabi/CoinJoin.html), documentation de Wasabi Wallet, consultée en septembre 2026.
- [CoinJoin in 2026: Wasabi, JoinMarket and Ashigaru compared](https://atlas21.com/coinjoin-comparison-of-tools-to-improve-privacy-on-bitcoin/), Atlas21, mis à jour le 10 juin 2026.
- [Announcement: new Zerolink coinjoin coordinator](https://ashigaru.rs/news/announcement-whirlpool/), Ashigaru, juin 2025.
- [Payjoin](https://bitcoinops.org/en/topics/payjoin/), Bitcoin Optech, consulté en septembre 2026.
- [Founders of Samourai Wallet cryptocurrency mixing service sentenced to five and four years in prison](https://www.irs.gov/compliance/criminal-investigation/founders-of-samourai-wallet-cryptocurrency-mixing-service-sentenced-to-five-and-four-years-in-prison), IRS Criminal Investigation, 19 novembre 2025.
- [Founder of Tornado Cash crypto mixing service convicted of knowingly transmitting criminal proceeds](https://www.irs.gov/compliance/criminal-investigation/founder-of-tornado-cash-crypto-mixing-service-convicted-of-knowingly-transmitting-criminal-proceeds), IRS Criminal Investigation, 6 août 2025.
- [Tornado Cash Developer Alexey Pertsev Found Guilty of Money Laundering](https://www.coindesk.com/policy/2024/05/14/tornado-cash-developer-alexey-pertsev-found-guilty-of-money-laundering), CoinDesk, 14 mai 2024.
- [Tornado Cash delisting](https://home.treasury.gov/news/press-releases/sb0057), Département du Trésor des États-Unis, 21 mars 2025.
- [Ledger Co-Founder's Kidnapping Highlights Threat of Crypto Robberies](https://www.coindesk.com/policy/2025/01/24/ledger-co-founder-s-kidnapping-sheds-light-on-soaring-crypto-robberies), CoinDesk, 24 janvier 2025.
- [Known physical bitcoin attacks](https://github.com/jlopp/physical-bitcoin-attacks), Jameson Lopp, liste mise à jour en continu.
- [Best practices](https://sparrowwallet.com/docs/best-practices.html), documentation de Sparrow Wallet, consultée en septembre 2026.
- [Coinbase breach hit almost 70k users](https://cointelegraph.com/news/70k-impacted-coinbase-data-breach-maine-attorneys), Cointelegraph, 21 mai 2025.

## Votre checklist {#your-checklist}

- [ ] Vérifiez que votre wallet affiche une adresse neuve pour chaque paiement (5 min)
- [ ] Retrouvez toute adresse ou tout solde que vous avez publié, et cessez de recevoir sur ces adresses (5 min)
- [ ] Créez des wallets séparés pour l'épargne, les dépenses et les retraits depuis les plateformes d'échange (1 h)
- [ ] Étiquetez chaque pièce que vous possédez avec son origine (1 h)
- [ ] Connectez votre wallet à votre propre nœud, après le chapitre 18 (1 week-end)
