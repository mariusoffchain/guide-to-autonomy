# Chapitre 7 : Nostr, un réseau ouvert sans entreprise aux commandes

## En bref {#in-brief}

Sur une plateforme, votre profil, vos publications et votre audience appartiennent à l'entreprise qui l'exploite. Nostr est un protocole ouvert pour des données signées, où votre identité est une paire de clés que vous détenez et où de nombreux relais et apps indépendants transportent ce que vous publiez, de sorte que vous pouvez changer d'app ou de relais à tout moment et garder votre nom et vos abonnés. Il sert aujourd'hui surtout à construire des alternatives aux plateformes sociales, des messages courts aux photos, aux articles longs, à la vidéo en direct, à la musique et aux places de marché. Il est plus petit et plus brut que les grandes plateformes, et créer un compte dans une app comme Primal, Damus ou Amethyst prend quelques minutes.

## Une place publique qui appartient à quelqu'un d'autre

Un réseau social ressemble à une place publique, mais il fonctionne comme un bâtiment privé dont le propriétaire fixe les règles et peut les changer du jour au lendemain. Le 18 décembre 2022, Twitter [a annoncé qu'il retirerait les liens vers Facebook, Instagram, Mastodon et Nostr](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/) et suspendrait les comptes qui en faisaient la promotion, puis a retiré cette politique en moins d'une journée après une vague de protestations.

Le même propriétaire peut supprimer un compte, avec ou sans motif annoncé, et des années de publications et de contacts disparaissent avec lui. Il peut aussi réduire le nombre de personnes qui vous voient sans vous le dire, une pratique souvent appelée shadow ban. En temps ordinaire, un algorithme réglé pour le temps passé et pour la publicité décide de ce que vous voyez, et votre portée change chaque fois qu'il change.

Votre audience n'est pas non plus à vous, car vous ne pouvez pas emmener vos abonnés vers un autre service, ce qui explique en grande partie pourquoi partir est si difficile. Ce que vous lisez, aimez et écrivez alimente aussi un profil publicitaire. En avril 2025, la Commission européenne [a infligé à Meta une amende de 200 millions d'euros](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1085) au titre du Digital Markets Act, parce que les utilisateurs de Facebook et d'Instagram devaient soit accepter la combinaison de leurs données personnelles pour la publicité, soit payer un abonnement.

## Les relais gardent la trace, les clients sont des fenêtres

Nostr est un protocole, comme le courrier électronique ou le web, ce qui signifie qu'aucune entreprise ne le possède et qu'aucune app ne le définit à elle seule. Il transporte des données signées de toute nature, et un message court n'est qu'un cas parmi d'autres. Il repose sur 3 éléments.

- **Votre identité est une paire de clés** (chapitre 6). La clé publique, qui commence par **npub**, est votre adresse, et vous pouvez la partager librement. La clé privée, qui commence par **nsec**, est votre secret, car elle prouve que vous êtes vous.
- **Tout ce que vous publiez est un événement signé.** Un message, une photo, un article long, une fiche produit ou l'annonce d'une diffusion en direct porte une signature faite avec votre nsec, de sorte que n'importe qui peut vérifier qu'elle est bien de vous et n'a pas été modifiée.
- **Les zaps** sont de petits paiements Lightning (partie 3) envoyés directement à une personne ou à une publication. Ils permettent de soutenir quelqu'un sans publicité et sans qu'une plateforme prélève sa part.

Pour situer les relais et les clients, imaginez que tout ce que les gens publient correspond à ce qui se passe dehors, dans la nature. Les **relais** enregistrent et conservent ce qui s'y passe. Ce sont de simples serveurs que n'importe qui peut exploiter, et vous publiez sur plusieurs à la fois. Un **client** est une fenêtre ouverte sur ce paysage, et les fenêtres diffèrent. Certaines montrent presque tout, d'autres filtrent ou masquent une partie de la vue, et une fenêtre peut être fermée, voire condamnée par des planches, pendant que les autres restent ouvertes. Vous pouvez toujours aller à une autre fenêtre, car le paysage n'appartient à aucune d'elles, et un nouveau client peut récupérer votre profil, vos publications et vos listes de contacts signés auprès des relais qui les conservent encore. Gardez des exports locaux de vos contenus importants, car les relais et les hébergeurs de médias ne promettent pas un stockage permanent.

En février 2023, Apple [a retiré le client Damus de son App Store en Chine](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/) 2 jours après son lancement, à la demande du régulateur chinois de l'internet. Cette fenêtre a été condamnée pour 1 pays, tandis que les relais et les autres clients continuaient de fonctionner.

## Les relais ne peuvent pas falsifier, mais ils peuvent masquer

Un client n'est qu'une fenêtre, il peut donc filtrer le spam ou masquer un compte, ce qui est souvent un service rendu, mais il ne peut pas effacer toutes les copies du réseau. Les relais peuvent supprimer des événements, y compris en réponse à une demande de suppression signée, et un autre client ne peut montrer que les copies qu'il peut encore récupérer. Un relais conserve la trace, il peut donc refuser vos événements, les abandonner plus tard ou ne jamais les servir à un lecteur donné. Il ne peut pas écrire en votre nom ni modifier ce que vous avez écrit, car la signature ne correspondrait plus à votre npub, et n'importe quel client peut faire cette vérification. La disponibilité dépend donc du fait de publier sur plusieurs relais exploités par des opérateurs différents, et votre [liste de relais](https://github.com/nostr-protocol/nips/blob/master/65.md) indique aux autres clients où vous trouver.

2 tiers de confiance subsistent. Le 1er est ce qui vous dit qu'un npub appartient bien à la personne que vous croyez. Une adresse NIP-05 montre seulement que la clé est listée sur un domaine, et [sa spécification](https://github.com/nostr-protocol/nips/blob/master/05.md) précise qu'elle identifie un utilisateur sans vérifier de qui il s'agit. Pour quelqu'un qui compte, prenez donc le npub directement auprès de cette personne. Le 2e est tout logiciel qui détient votre nsec, car il pourrait signer n'importe quoi en votre nom, un risque que les signers, décrits plus bas, réduisent en gardant la clé hors des clients. Un client peut tout de même abuser des autorisations de signature que vous lui accordez.

## Choisissez votre client

Nostr est souvent présenté comme une alternative à X, qui n'est que 1 de ses usages. Certains clients fonctionnent comme Instagram, d'autres comme Medium, Twitch, une app de podcasts ou de musique, une place de marché, une messagerie de groupe ou une boutique d'apps, et tous acceptent la même clé.

Soyez lucide sur ce que vous obtenez. Le réseau est beaucoup plus petit que les grandes plateformes, le spam existe, et certaines apps paraissent inachevées. Il n'y a pas de réinitialisation de mot de passe, ni de véritable suppression non plus, car vous pouvez demander aux relais de supprimer un événement mais ils sont libres de vous ignorer. Considérez chaque publication comme permanente et publique.

À l'exception de Fountain, dont le code n'est pas publié, et d'une partie de Wavlake, les clients ci-dessous publient leur code source sous licence libre (vérifié sur leurs dépôts publics en septembre 2026). L'open source ne garantit pas que la version disponible dans la boutique d'apps correspond au code public, mais il permet à n'importe qui de le vérifier.

| Client | Ce à quoi il ressemble | Type de contenu | Plateformes | Où se situe la confiance |
|---|---|---|---|---|
| [**Primal**](https://primal.net/) | X, avec le démarrage le plus fluide et un wallet (portefeuille) intégré. | Messages courts, articles, flux de médias | iOS, Android, web | Le serveur de cache de Primal choisit ce qui vous parvient. Il est [open source](https://github.com/PrimalHQ/primal-server), et les paramètres en acceptent un autre. |
| [**Damus**](https://damus.io/) | X, proche de ce à quoi ressemblait Twitter. Simple. | Messages courts | iOS | Parle directement à vos relais. L'app elle-même garde votre nsec sur le téléphone. |
| [**Amethyst**](https://amethyst.social/) | X, avec le plus de fonctionnalités, ce qui peut déconcerter au début. | Messages courts, et la plupart des autres types d'événements | Android | Parle directement à vos relais. Avec le signer Amber, l'app ne détient jamais votre nsec. |
| [**Yakihonne**](https://yakihonne.com/) | Medium. | Articles longs, contenus sélectionnés, messages courts | iOS, Android, web | 1 seule entreprise développe les apps et exploite ses propres relais. Accepte un signer distant. |
| [**Olas**](https://olas.app/) | Instagram. Les versions sortent lentement. La version iPhone présente dans la boutique date de mars 2025, et une réécriture est en cours. | Photos et courtes vidéos | iOS, Android | Parle directement à vos relais. Les fichiers d'images se trouvent sur des serveurs de médias, qui peuvent les supprimer. |
| [**zap.stream**](https://zap.stream/) | Twitch. | Vidéo en direct, avec chat et zaps | Web, iOS, Android | Le chat et les annonces sont des événements signés. La vidéo passe par un serveur de streaming, celui de zap.stream par défaut. |
| [**Fountain**](https://fountain.fm/) | Une app de podcasts avec commentaires et paiements aux émissions. | Podcasts, musique | iOS, Android | 1 seule entreprise. Le code n'est pas publié, et le wallet intégré est custodial, c'est-à-dire que l'entreprise garde les clés à votre place. |
| [**Wavlake**](https://wavlake.com/) | Spotify ou Bandcamp, pour les artistes indépendants. | Musique, payée directement aux artistes | Web, iOS, Android | 1 seule entreprise héberge la musique et gère les paiements aux artistes. L'app iPhone date de novembre 2025. |
| [**Shopstr**](https://shopstr.store/) | Une place de petites annonces. | Fiches produits, payées en bitcoin | Web | Les annonces sont des événements signés. Le paiement va directement au vendeur, sans séquestre, donc vérifiez à qui vous achetez. |
| [**0xchat**](https://www.0xchat.com/) | Telegram ou WhatsApp. | Discussions privées et de groupe | iOS, Android, ordinateur | Les relais transportent les messages chiffrés. Un projet jeune, sans l'historique des messageries du chapitre 1. |
| [**Zapstore**](https://zapstore.dev/) | Google Play ou F-Droid. | Apps Android | Android | Chaque version est signée avec la clé Nostr du développeur et vérifiée avant l'installation. Vous choisissez les catalogues et les développeurs auxquels vous faites confiance. |
| [**Iris**](https://iris.to/), [**Coracle**](https://coracle.social/), [**noStrudel**](https://nostrudel.ninja/) | X, dans un navigateur. Coracle offre un contrôle fin des relais, noStrudel explore tout ce que le protocole permet. | Messages courts, et davantage dans noStrudel | Web (Iris aussi sur mobile) | Le site qui sert le code à chaque visite. Connectez-vous via une extension ou un signer distant, pas avec le nsec. noStrudel peut être auto-hébergé. |

Une configuration raisonnable pour la plupart des gens associe **un client mobile** pour l'usage quotidien (Primal, Damus ou Amethyst), **un client web** sur votre ordinateur, utilisé avec un signer, puis 1 ou 2 clients spécialisés qui correspondent à ce que vous lisez, regardez ou écoutez.

## Protégez votre nsec

Votre nsec est toute votre identité. S'il fuit, quelqu'un peut publier à votre place aussi longtemps qu'il le souhaite, et vous ne pouvez pas le changer comme on change un mot de passe. La règle qui en découle est de **ne jamais coller votre nsec dans un site web que vous ne connaissez pas**, et de le coller dans le moins d'endroits possible.

La solution propre est un **signer**, une petite app qui garde la clé et signe au nom de vos clients. Le client demande, le signer signe, et le client ne voit jamais la clé. Vérifiez les autorisations demandées, évitez d'accorder une approbation générale à des clients inconnus, et révoquez les connexions que vous n'utilisez plus. Plusieurs options existent.

- **Amber** sur Android, une app de signer open source que les autres apps Nostr appellent lorsqu'elles ont besoin d'une signature.
- **Une extension de navigateur** comme nos2x ou Alby, pour les clients web sur votre ordinateur.
- **Un signer distant**, souvent appelé nsec bunker, où la clé reste sur 1 seul appareil ou serveur et où vos apps s'y connectent via Nostr. Il fonctionne sur toutes les plateformes.

Sur iPhone, il n'existe pas pour le moment d'équivalent exact d'Amber, car iOS laisse moins de moyens aux apps de s'appeler entre elles. Quelques apps de signer et des extensions Safari existent, et l'annuaire nostrapps.com liste celles qui sont actuelles. À défaut, un signer distant est la voie habituelle.

Sauvegardez ensuite le nsec comme n'importe quelle clé du chapitre 6, sur papier en 2 endroits, ou dans votre gestionnaire de mots de passe tant que le compte a peu de valeur.

## Pas à pas {#step-by-step}

L'exemple utilise un client mobile, et la logique est la même dans tous.

1. **Créez vos clés dans un client.** Installez-le et choisissez « créer un compte ». Aucun e-mail ni numéro de téléphone n'est nécessaire, car l'app génère la paire de clés sur votre téléphone.
2. **Sauvegardez le nsec immédiatement.** Vous le trouvez dans les paramètres, sous clés ou compte. Faites-le avant de publier quoi que ce soit.
3. **Remplissez le profil** avec un nom, une photo et une courte description, et n'oubliez pas qu'il est public.
4. **Facultatif, ajoutez une adresse lisible** (appelée NIP-05). Elle ressemble à une adresse e-mail, nom@domaine, et montre que votre clé est listée sur ce domaine, et rien de plus. Certains services en proposent une, ou vous pouvez utiliser votre propre domaine. Ce n'est pas un identifiant de connexion.
5. **Suivez des gens.** Cherchez par leur nom des personnes que vous connaissez déjà, ajoutez quelques comptes de départ que votre client suggère, et suivez quelques hashtags. Un fil vide le jour 1 est normal. Pour les comptes qui comptent pour vous, comparez le npub avec celui que la personne indique sur son propre site web ou en personne, c'est l'étape qui remplace la confiance dans un résultat de recherche par une vérification.
6. **Ajoutez un 2e client avec un signer.** Sur Android, installez Amber. Sur un ordinateur, installez une extension de navigateur comme nos2x ou Alby. Sur iPhone, choisissez une app de signer ou une extension Safari sur nostrapps.com, ou mettez en place un signer distant. Importez une fois votre nsec dans le signer, puis ouvrez un client web et choisissez l'option pour se connecter avec une extension ou un signer. Vérifiez que le 2e client retrouve votre profil et vos listes de contacts, et que vous publiez sur plusieurs relais indépendants. La portabilité dépend de la disponibilité durable de ces enregistrements.
7. **Connectez un wallet Lightning pour les zaps.** Ajoutez une adresse Lightning à votre profil pour recevoir, et reliez un wallet pour envoyer. La partie 3 explique les wallets.

## Erreurs à éviter {#mistakes-to-avoid}

- **Coller votre nsec dans chaque nouvelle app que vous essayez.** Chaque copie est un risque. Utilisez un signer, ou testez les nouvelles apps avec une 2e clé jetable.
- **Croire que Nostr est privé.** Les notes sont publiques par conception. Les messages directs varient d'une app à l'autre, et peuvent révéler qui écrit à qui. Pour les conversations privées, utilisez une messagerie du chapitre 1.
- **Publier ce que vous pourriez vouloir supprimer.** Les relais reçoivent une demande de suppression et sont libres de l'ignorer, et des copies peuvent déjà exister ailleurs.
- **Dépendre d'1 seul relais.** Publiez sur plusieurs, exploités par des opérateurs différents, car la résistance à la censure vient de là.
- **Attendre les grandes plateformes dès le jour 1.** Le réseau est plus petit, et il devient intéressant lorsque vous suivez 30 ou 40 personnes actives.
- **Garder de l'argent dans un wallet conçu pour les zaps.** Un wallet de zaps est fait pour de petits montants, même lorsqu'il est en self-custody (vous gardez vous-même les clés). Le wallet intégré de Primal, par exemple, était custodial jusqu'en 2026. Depuis la version 3.0 (mars 2026), il est [en self-custody](https://breez.technology/case-studies/primal), ce qui signifie que vous détenez les mots de récupération, et il fonctionne sur Spark, une couche Bitcoin récente compatible avec Lightning, dont les garanties dépendent en partie des opérateurs de Spark. D'anciens tests décrivent encore la version custodial, et le wallet intégré de Fountain est custodial. L'épargne a sa place ailleurs (partie 3).

## Pour aller plus loin {#go-further}

- **Un guide pour débutants :** nostr.how.
- **Un annuaire de clients, de signers et d'outils :** nostrapps.com.
- **Le protocole lui-même,** pour les curieux : le dépôt des NIP (github.com/nostr-protocol/nips).
- **Chapitre suivant :** remplacer les services des Big Tech, 1 à la fois.

## Sources {#sources}

- [NIP-09, event deletion requests](https://github.com/nostr-protocol/nips/blob/master/09.md), dépôt du protocole Nostr, consulté le 22 octobre 2026.
- [NIP-46, remote signing and permissions](https://github.com/nostr-protocol/nips/blob/master/46.md), dépôt du protocole Nostr, consulté le 22 octobre 2026.
- [Twitter won't let you post your Facebook, Instagram and Mastodon handles](https://techcrunch.com/2022/12/18/twitter-wont-let-you-post-your-facebook-instagram-and-mastodon-handles/), TechCrunch, 18 décembre 2022.
- [Commission finds Apple and Meta in breach of the Digital Markets Act](https://ec.europa.eu/commission/presscorner/detail/en/ip_25_1085), Commission européenne, 23 avril 2025.
- [Damus pulled from Apple's App Store in China after two days](https://techcrunch.com/2023/02/02/damus-pulled-from-apples-app-store-in-china-after-two-days/), TechCrunch, 2 février 2023.
- [NIP-05: mapping Nostr keys to DNS-based internet identifiers](https://github.com/nostr-protocol/nips/blob/master/05.md), dépôt du protocole Nostr, consulté en septembre 2026.
- [NIP-65: relay list metadata](https://github.com/nostr-protocol/nips/blob/master/65.md), dépôt du protocole Nostr, consulté en septembre 2026.
- [Zapstore, an open app store](https://zapstore.dev/), Zapstore, consulté en septembre 2026.
- [Shopstr, a marketplace built on Nostr](https://shopstr.store/), Shopstr, consulté en septembre 2026.
- [Olas on the App Store](https://apps.apple.com/us/app/olas/id6738208592), Apple, version 0.4.0 publiée le 11 mars 2025, consulté en septembre 2026.
- [Primal Server](https://github.com/PrimalHQ/primal-server), PrimalHQ sur GitHub, consulté en septembre 2026.
- [Primal case study](https://breez.technology/case-studies/primal), Breez, 2026.
- [Primal for Android, release notes](https://github.com/PrimalHQ/primal-android-app/releases), PrimalHQ sur GitHub, version 3.0.7 publiée le 17 mars 2026.

## Votre checklist {#your-checklist}

- [ ] Installez un client et créez vos clés (5 min)
- [ ] Sauvegardez votre nsec sur papier ou dans votre gestionnaire de mots de passe (5 min)
- [ ] Remplissez votre profil et suivez quelques personnes que vous connaissez déjà (5 min)
- [ ] Installez un signer et connectez-vous à un 2e client grâce à lui (5 min)
- [ ] Une fois que vous avez un wallet Lightning (chapitres 13 et 15), ajoutez une adresse Lightning à votre profil et envoyez votre premier zap (1 h)
