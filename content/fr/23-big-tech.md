# Chapitre 8 : Remplacer les services des Big Tech, 1 à la fois

## En bref {#in-brief}

Vous ne quittez pas Google, Apple, Meta ou Microsoft en 1 jour, et vous n'avez pas à le faire. Exportez d'abord vos données, puis remplacez 1 service, vivez avec pendant 2 semaines, et seulement ensuite passez au suivant. Pour chaque besoin, il existe plusieurs alternatives crédibles, la plupart open source et exploitées par des opérateurs différents. Chaque service que vous déplacez réduit ce qu'1 seule entreprise sait de vous, et ce que vous perdez si ce compte est bloqué.

## 1 seul compte contient toute votre vie numérique

La plupart des vies numériques tournent à l'intérieur de 1 ou 2 entreprises, avec le courrier, l'agenda, les photos, les documents, les cartes et les vidéos sous 1 seul compte. C'est confortable, et cela crée 2 risques.

Le profil d'abord, car une entreprise qui voit vos recherches, vos déplacements, votre boîte de réception et vos photos en sait plus sur vous que n'importe quelle personne. La dépendance ensuite, car si ce compte est bloqué (chapitre 6), tout disparaît au même moment.

En mai 2025, l'Associated Press a rapporté que le procureur en chef de la Cour pénale internationale avait perdu l'accès à son compte e-mail Microsoft après des sanctions américaines, bien que Microsoft affirme n'avoir jamais suspendu ses services auprès de la Cour. En octobre 2025, la Cour [a confirmé qu'elle remplaçait Microsoft Office par openDesk](https://www.theregister.com/2025/10/31/international_criminal_court_ditches_office/), une suite open source développée pour l'État allemand.

La réaction habituelle est un élan de motivation, « je supprime tout aujourd'hui », et elle échoue presque toujours. Trop d'habitudes cassent en même temps, l'agenda de la famille cesse de fonctionner, un document reste introuvable avant une échéance, et 2 semaines plus tard tout est revenu en place. On en conclut que les alternatives ne marchent pas, alors que c'est la tentative de changer 10 habitudes d'un coup qui a échoué.

## Exporter d'abord, puis 1 service à la fois

La méthode repose sur 3 idées.

**Exporter d'abord.** L'article 20 du [Règlement général sur la protection des données](https://eur-lex.europa.eu/eli/reg/2016/679/oj), applicable depuis le 25 mai 2018, donne un droit à la portabilité pour certaines données personnelles que vous avez fournies, lorsqu'elles sont traitées de manière automatisée sur la base de votre consentement ou d'un contrat. Il ne couvre pas tout ce qu'un fournisseur détient. Les données couvertes doivent être fournies dans un format structuré, couramment utilisé et lisible par machine. Les grandes entreprises fournissent un outil pour cela, Google Takeout (takeout.google.com), la page « Données et confidentialité » d'Apple (Data and Privacy, privacy.apple.com), et l'option « télécharger vos informations » (download your information) dans les paramètres du compte de Facebook et d'Instagram. L'export met des heures ou des jours à arriver. Vous gardez votre historique quoi qu'il arrive ensuite, et vous voyez combien elles en détiennent, ce qui, pour beaucoup de gens, est le moment où la motivation devient réelle.

**Choisir 1 service.** Il y a 2 bonnes façons de choisir, soit celui qui en sait le plus sur vous (souvent le courrier, les photos ou la recherche), soit le plus facile (souvent les cartes, les notes ou la recherche). Si vous hésitez, prenez le plus facile, car un succès rapide rend le suivant plus simple.

**Faire tourner l'ancien et le nouveau en parallèle.** Utilisez le nouvel outil pendant 2 semaines pendant que l'ancien existe encore, et ne déplacez les données et ne les supprimez de l'ancien qu'une fois que vous avez cessé de l'ouvrir.

Recommencez ensuite. 1 nouveau service tous les mois ou tous les 2 mois est un très bon rythme.

## Une marque axée sur la confidentialité reste 1 entreprise

Passer de Google à un fournisseur qui a « confidentialité » dans son slogan change de propriétaire et laisse la question intacte, à savoir qui peut lire vos données, et ce qui se passe si cette entreprise fait faillite, est vendue ou change ses conditions. 3 tests aident à y répondre.

- **Le fournisseur peut-il le lire ?** Avec le chiffrement de bout en bout, les données sont verrouillées sur votre appareil et le fournisseur stocke quelque chose qu'il ne peut pas ouvrir. Sans lui, le contenu n'est protégé que par la promesse du fournisseur et par le droit de son pays. Même avec lui, le fournisseur voit certaines métadonnées et livre l'app qui effectue le chiffrement, c'est pourquoi les apps open source et les audits publiés comptent.
- **Pouvez-vous partir ?** Un export dans un format standard garde toute entreprise remplaçable.
- **Quelqu'un d'autre peut-il l'exploiter ?** Un logiciel que vous ou une association pouvez héberger (Nextcloud, CryptPad, Immich, PeerTube) ne dépend pas de la survie de 1 opérateur, et les outils locaux (Syncthing, Joplin, Obsidian, LibreOffice) gardent les données sur vos propres appareils.

Une entreprise bien gérée qui propose le chiffrement de bout en bout reste un choix raisonnable pour la plupart des lecteurs, et souvent plus sûr qu'un serveur que personne ne maintient.

## Choisissez vos remplacements

Le tableau est organisé par besoin. « Open source » signifie que le code est public et peut être vérifié. « Auto-hébergé » (self-hosted) signifie que vous, ou quelqu'un de confiance, devez exploiter un serveur (chapitre 10). Tout le reste est prêt à l'emploi.

Aucune alternative n'est une copie exacte de ce qu'elle remplace. Certaines sont meilleures, d'autres demandent un petit compromis, et les notes indiquent lesquelles. Essayez 2 options pour le même besoin avant de décider, car la plupart sont gratuites ou peu chères à tester.

Certains noms, Proton en particulier, apparaissent dans plusieurs lignes. Tout prendre chez 1 seul fournisseur est pratique, mais cela reconstruit la dépendance que vous quittez, pensez donc à mélanger les opérateurs.

| Besoin | Alternatives | Notes | Qui peut lire vos données |
|---|---|---|---|
| **Recherche** | Voir le chapitre 3 | Le premier pas le plus facile, 1 seul réglage dans votre navigateur. | Voir le chapitre 3. |
| **E-mail et agenda** | Voir le chapitre 4 pour l'e-mail. Agendas : Proton Calendar, Tuta Calendar, Nextcloud | Proton et Tuta chiffrent votre agenda et publient le code de leurs apps. Chacun est 1 seule entreprise. Nextcloud est open source, auto-hébergé ou loué auprès d'un fournisseur de votre choix. | Ni Proton ni Tuta, qui [chiffrent les événements de bout en bout](https://proton.me/blog/protoncalendar-security-model). Sur Nextcloud, celui qui exploite le serveur le peut. |
| **Cartes** | Organic Maps, CoMaps, OsmAnd, Magic Earth | Toutes utilisent les données d'OpenStreetMap. Organic Maps, son fork communautaire CoMaps, et OsmAnd (plus détaillé, plus complexe) sont open source et fonctionnent hors ligne gratuitement, sans trafic en direct. Magic Earth est à code fermé et propose bien le trafic en direct, mais en septembre 2026 le trafic et les cartes hors ligne font partie de son [abonnement Premium payant](https://www.magicearth.com/pricing). Aucune n'a les avis sur les commerces de Google Maps. | La recherche et le calcul d'itinéraire hors ligne s'exécutent sur le téléphone, sans compte. Le code de Magic Earth ne peut pas être vérifié. |
| **Stockage cloud et synchronisation** | Nextcloud, Proton Drive, Filen, Syncthing | Proton Drive et Filen sont chiffrés de bout en bout, avec des apps open source, chacun exploité par 1 seule entreprise. Pour Nextcloud, voir ci-dessus. Syncthing est open source et n'a aucun cloud, car il synchronise directement vos propres appareils. Il fonctionne mieux entre ordinateurs. Sur Android, l'app officielle a été [abandonnée en décembre 2024](https://forum.syncthing.net/t/discontinuing-syncthing-android/23002). Une version communautaire, Syncthing-Fork, continue sur F-Droid et a changé de mainteneur en 2025, vérifiez donc son état actuel avant de vous y fier. Sur iPhone, il n'existe que des apps tierces. | Ni Proton ni Filen. Un hébergeur Nextcloud le peut, sauf si vous utilisez des [dossiers chiffrés de bout en bout](https://nextcloud.com/encryption/) côté client. Le chiffrement côté serveur seul ne cache pas les fichiers à l'administrateur. Les [relais Syncthing transportent des données chiffrées](https://docs.syncthing.net/users/relaying.html). |
| **Documents** | CryptPad, LibreOffice, OnlyOffice | CryptPad propose une collaboration en ligne chiffrée, est open source, et peut être utilisé sur une instance publique ou hébergé par vous. LibreOffice est open source et fonctionne hors ligne sur votre ordinateur. OnlyOffice est open source, bon avec les formats Microsoft, et souvent utilisé dans Nextcloud. | Pas un hébergeur CryptPad (les documents sont chiffrés dans votre navigateur). Les fichiers LibreOffice restent en local. OnlyOffice dépend de son hébergeur. |
| **Notes** | Standard Notes, Joplin, Notesnook, Obsidian | Standard Notes et Notesnook sont open source et chiffrés de bout en bout par défaut. Standard Notes appartient à Proton. Joplin est open source et se synchronise via le stockage que vous choisissez, mais son chiffrement de bout en bout [est facultatif](https://joplinapp.org/help/apps/sync/e2ee/), activez-le donc dans les paramètres avant la 1re synchronisation. Obsidian est à code fermé, mais vos notes sont des fichiers texte simples sur votre propre disque. | Ni Standard Notes ni Notesnook. Le fournisseur de stockage de Joplin le peut, tant que le chiffrement n'est pas activé. Les fichiers Obsidian restent en local. |
| **Photos** | Ente Photos, Immich | Ente est chiffré de bout en bout, open source, payant au-delà d'un petit forfait gratuit, et peut être auto-hébergé. Immich est open source, uniquement auto-hébergé, et le plus proche de l'expérience Google Photos. | Pas Ente, dont la [conception est publiée](https://ente.io/architecture/). Avec Immich, celui qui exploite le serveur, qui est normalement vous. |
| **Vidéo** | NewPipe, FreeTube, Invidious, PeerTube | NewPipe (Android) et FreeTube (ordinateur) lisent YouTube sans compte ni publicités. Invidious fait la même chose dans un navigateur via des instances publiques qui tombent souvent en panne. Ces 3 outils sont open source et peuvent cesser de fonctionner quand YouTube change quelque chose. PeerTube est différent, un réseau open source et fédéré avec ses propres vidéos. | YouTube voit toujours votre adresse IP. Une instance Invidious ou PeerTube voit ce que vous y regardez. |
| **Traduction** | LibreTranslate, la traduction intégrée de Firefox | LibreTranslate est open source et peut être auto-hébergé. Firefox traduit les pages sur votre appareil. DeepL offre une meilleure qualité mais est à code fermé et reçoit votre texte, ce qui convient pour un menu et pas pour un contrat. | Une instance LibreTranslate voit votre texte, sauf si vous l'hébergez. Firefox n'envoie rien. DeepL reçoit tout ce que vous saisissez. |
| **Boutique d'apps sur Android** | F-Droid, Obtainium, Aurora Store | F-Droid est un catalogue d'apps open source uniquement. Voir le chapitre 9. | Personne ne lit de données ici. La question est de savoir qui compile et signe les apps (chapitre 9). |

Un départ raisonnable pour la plupart des gens est **la recherche, puis les cartes, puis les notes**, car elles ne demandent presque aucune migration. Le courrier et les photos comptent le plus, et chacun mérite un week-end tranquille.

## Pas à pas {#step-by-step}

L'exemple déplace vos photos, et la logique est la même pour chaque ligne du tableau.

1. **Exportez.** Demandez votre archive complète à l'ancien service et stockez-la sur un disque qui vous appartient. Vérifiez que les fichiers s'ouvrent.
2. **Choisissez 1 service** dans le tableau. Lisez son site web, vérifiez qui l'exploite, si le code est ouvert, si le fournisseur peut lire vos données, et combien il coûte. C'est l'étape qui remplace la confiance dans une marque par une vérification.
3. **Faites tourner l'ancien et le nouveau en parallèle pendant 2 semaines.** Activez la nouvelle sauvegarde de photos sur votre téléphone et laissez l'ancienne en place. Utilisez la nouvelle app chaque fois que vous voulez regarder une photo.
4. **Déplacez les données.** Importez votre export dans le nouveau service. La plupart des alternatives ont un outil d'import ou un guide pour les grandes plateformes.
5. **Changez le service par défaut sur chaque appareil,** c'est-à-dire téléphone, tablette, ordinateur, et les appareils de toute personne qui partage le service avec vous. Désactivez l'ancienne sauvegarde ou synchronisation.
6. **Supprimez les données de l'ancien service,** une fois que vous avez vérifié que la nouvelle copie est complète et que vous en avez une sauvegarde. Soyez prudent avec les photos. Selon la [page d'aide de Google elle-même](https://support.google.com/photos/answer/6128858/delete-or-restore-your-photos-amp-videos-android?co=GENIE.Platform%3DAndroid), supprimer une photo sauvegardée dans l'app Google Photos supprime aussi la copie présente sur votre téléphone. Pour conserver les copies du téléphone, désactivez d'abord la sauvegarde sur chaque appareil, puis supprimez depuis photos.google.com sur un ordinateur, ou utilisez « Annuler la sauvegarde » (Undo backup) dans les paramètres de sauvegarde de l'app, qui supprime les copies dans le cloud et laisse les fichiers sur l'appareil. Avec iCloud Photos, [téléchargez d'abord les originaux](https://support.apple.com/en-ie/102179), attendez la fin du téléchargement et vérifiez les fichiers, puis désactivez la synchronisation sur les appareils dont vous voulez garder les copies avant de supprimer les éléments du cloud. Les éléments supprimés restent dans la corbeille pendant 30 jours, que vous pouvez vider une fois que vous êtes sûr.
7. **Choisissez le suivant,** mais pas la même semaine.

## Erreurs à éviter {#mistakes-to-avoid}

- **Le purisme.** Remplacer 7 services sur 10 est un gain important, et garder YouTube ou un outil de travail n'annule pas le reste.
- **Tout déplacer d'un coup.** C'est la principale raison pour laquelle les gens reviennent en arrière. Déplacez 1 service, vivez avec pendant 2 semaines, puis choisissez le suivant.
- **Oublier les personnes avec qui vous partagez.** Les albums partagés, l'agenda de la famille et une liste de courses commune impliquent d'autres personnes, parlez-leur donc avant de déplacer, ou laissez cet élément où il est pour l'instant.
- **Faire confiance au mot « confidentialité » dans une publicité.** Vérifiez les faits. Le code est-il ouvert, les données sont-elles chiffrées de sorte que l'entreprise ne puisse pas les lire, ce chiffrement est-il activé par défaut, à qui appartient l'entreprise, comment gagne-t-elle de l'argent ?
- **Supprimer avant de vérifier.** Ouvrez la nouvelle copie, comptez les albums, vérifiez les fichiers les plus anciens et les plus récents, et seulement ensuite supprimez l'original, de la manière décrite à l'étape 6.
- **Remplacer une dépendance par une autre.** Si tout passe chez 1 seule nouvelle entreprise, la dépendance reste la même avec un meilleur propriétaire. Répartissez vos services entre plusieurs opérateurs.

## Pour aller plus loin {#go-further}

- **Des recommandations détaillées et indépendantes :** Privacy Guides (privacyguides.org).
- **Des alternatives classées par service à remplacer :** switching.software.
- **Des services basés en Europe :** european-alternatives.eu.
- **Chapitre suivant :** reprendre le contrôle de votre téléphone.

## Sources {#sources}

- [Respect individuals' rights, including portability](https://www.edpb.europa.eu/sme/be-compliant/respect-individuals-rights_en), Comité européen de la protection des données, consulté le 22 octobre 2026.
- [Server-side encryption and its limits](https://docs.nextcloud.com/server/32/admin_manual/configuration_files/encryption_configuration.html), manuel d'administration de Nextcloud, consulté le 22 octobre 2026.
- [Turn off iCloud Photos](https://support.apple.com/en-ie/102179), Apple Support, consulté le 22 octobre 2026.
- [International Criminal Court dumps Microsoft Office](https://www.theregister.com/2025/10/31/international_criminal_court_ditches_office/), The Register, 31 octobre 2025.
- [Regulation (EU) 2016/679, General Data Protection Regulation, Article 20](https://eur-lex.europa.eu/eli/reg/2016/679/oj), Journal officiel de l'Union européenne, 27 avril 2016.
- [Discontinuing syncthing-android](https://forum.syncthing.net/t/discontinuing-syncthing-android/23002), forum de la communauté Syncthing, 20 octobre 2024.
- [Delete photos and videos](https://support.google.com/photos/answer/6128858/delete-or-restore-your-photos-amp-videos-android?co=GENIE.Platform%3DAndroid), Aide Google Photos, consulté le 22 octobre 2026.
- [Magic Earth pricing](https://www.magicearth.com/pricing), Magic Earth, consulté en septembre 2026.
- [End-to-end encryption](https://joplinapp.org/help/apps/sync/e2ee/), documentation de Joplin, consulté en septembre 2026.
- [The Proton Calendar security model](https://proton.me/blog/protoncalendar-security-model), Proton, consulté en septembre 2026.
- [Nextcloud encryption](https://nextcloud.com/encryption/), Nextcloud, consulté en septembre 2026.
- [Relaying](https://docs.syncthing.net/users/relaying.html), documentation de Syncthing, consulté en septembre 2026.
- [Ente architecture](https://ente.io/architecture/), Ente, consulté en septembre 2026.

## Votre checklist {#your-checklist}

- [ ] Demandez votre export de données à Google, Apple ou Meta (5 min)
- [ ] Remplacez 1 service facile, recherche, cartes ou notes (5 min)
- [ ] Choisissez votre premier service important et faites-le tourner en parallèle pendant 2 semaines (1 h)
- [ ] Déplacez les données et changez les services par défaut, et ne supprimez l'ancienne copie dans le cloud qu'après avoir vérifié une sauvegarde indépendante et désactivé la synchronisation sur les appareils dont vous voulez garder les copies (1 week-end)
- [ ] Notez dans votre agenda le prochain service à remplacer, dans 1 mois (5 min)
