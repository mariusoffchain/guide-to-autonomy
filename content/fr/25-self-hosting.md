# Chapitre 10 : Héberger vos propres services

## En bref {#in-brief}

« Le cloud », c'est l'ordinateur de quelqu'un d'autre. L'auto-hébergement consiste à exécuter certains de vos services, comme vos fichiers, vos photos, vos notes et plus tard un nœud Bitcoin, sur un petit ordinateur que vous possédez et gardez chez vous. Des plateformes adaptées aux débutants rendent désormais l'installation d'une app à peu près aussi simple que sur un téléphone, même si les sauvegardes, les mises à jour et l'accès à distance demandent encore un peu de lecture et deviennent votre travail. Le chemin raisonnable est de commencer par 1 service, de le rendre fiable, puis de grandir.

## Dans le cloud de quelqu'un d'autre, vous êtes locataire

Quand vos fichiers, vos photos et votre agenda vivent dans le cloud d'une entreprise, c'est cette entreprise qui fixe les règles. Elle peut lire ce qui n'est pas chiffré de bout en bout, augmenter le prix, fermer le produit ou bloquer votre compte par une décision automatisée, avec pour seul recours un formulaire d'assistance. Elle peut aussi changer les conditions après votre arrivée. Google Photos a proposé pendant des années un stockage illimité gratuit, puis a annoncé en novembre 2020 que [chaque nouvelle photo compterait dans une limite de 15 Go](https://blog.google/products-and-platforms/products/photos/storage-changes/) à partir du 1er juin 2021.

Le chapitre 8 a montré comment passer à des fournisseurs plus respectueux, ce qui est déjà un grand pas, mais vous y restez locataire aussi.

L'auto-hébergement va un cran plus loin, car le service s'exécute sur une machine chez vous et les données se trouvent sur votre disque. Il n'y a pas de compte qu'un fournisseur puisse suspendre et pas de tiers entre vous et vos fichiers.

Ce n'est cependant pas gratuit. Vous payez le matériel, l'électricité et une sauvegarde hors site, vous payez avec votre temps, et vous devenez la personne responsable quand quelque chose tombe en panne.

## Un serveur est un ordinateur qui reste allumé

Un serveur n'est qu'un ordinateur qui reste allumé et répond aux demandes d'autres appareils, et un foyer n'a pas besoin d'un centre de données pour cela. Un vieux portable, un petit mini PC ou un Raspberry Pi suffit. Un mini PC ou un portable avec un SSD est généralement le départ le plus confortable, et sur un Raspberry Pi un SSD est préférable à une carte mémoire, car les cartes ont tendance à s'user vite.

Sur cet ordinateur, vous installez une **plateforme**, un système qui vous donne une page web avec une boutique d'apps. Vous l'ouvrez depuis votre navigateur, cliquez sur « installer » pour Nextcloud ou Immich, et la plateforme installe et gère l'app. Certaines plateformes utilisent des conteneurs, qui gardent les apps séparées les unes des autres. La séparation est plus faible qu'entre 2 ordinateurs, car tous les conteneurs partagent le même noyau du système, si bien qu'un conteneur n'est pas une boîte de sécurité scellée.

Votre téléphone et votre portable parlent ensuite à cette boîte au lieu de parler à une entreprise. À la maison, cela passe par votre propre Wi-Fi, et depuis l'extérieur il vous faut une entrée sûre, qui a sa propre section plus bas.

La technologie est la plus petite partie du changement, car les sauvegardes, les mises à jour et la sécurité sont désormais les vôtres.

## Vous devenez votre propre tiers de confiance

L'auto-hébergement retire l'entreprise de la confidentialité, puisque personne d'autre ne détient les données, et il vous confie les autres propriétés. La disponibilité dépend désormais de votre disque, de votre électricité et de vos sauvegardes, et les ingénieurs du fournisseur sont remplacés par ce que vous pensez à faire. Pour un débutant, un fournisseur bien géré avec chiffrement de bout en bout peut être le choix le plus sûr, et héberger quelques services tout en louant le reste est un résultat solide.

Certains tiers subsistent, et il est utile de les nommer. Le fabricant de la plateforme publie les mises à jour du système et organise la boutique d'apps, si bien qu'une mise à jour négligente ou malveillante atteindrait tous les serveurs à la fois. Le code open source, et la possibilité d'ajouter une autre boutique ou d'installer une app à la main, gardent cette partie remplaçable. Pour l'accès à distance, le serveur de coordination de Tailscale donne à chacun de vos appareils les clés publiques des autres. Le contenu du trafic reste chiffré entre vos appareils, y compris lorsqu'un relais le transporte, mais la documentation de Tailscale [reconnaît](https://tailscale.com/kb/1226/tailnet-lock) qu'un coordinateur malveillant pourrait insérer un appareil dans votre réseau, et elle propose Tailnet Lock, avec lequel vos propres appareils doivent signer tout nouvel arrivant. Headscale ou WireGuard seul suppriment cette partie, au prix de plus de configuration.

## Choisissez votre plateforme

Toutes sont faites pour des personnes qui ne sont pas administrateurs système, et elles diffèrent par leur orientation, leur licence et leurs soutiens. La licence compte dans un livre qui place l'open source en premier. StartOS est publié sous [licence MIT](https://github.com/Start9Labs/start-technologies/blob/master/LICENSE) et YunoHost est lui aussi un logiciel libre, alors qu'umbrelOS utilise la [licence PolyForm Noncommercial](https://github.com/getumbrel/umbrel/blob/master/LICENSE.md), qui vous permet de lire et de modifier le code pour un usage personnel mais n'est pas une licence open source. Start9 et Umbrel vendent chacun leurs propres serveurs, et aucun ne les exige, puisque les 2 systèmes s'installent gratuitement sur un ordinateur que vous possédez déjà.

| Plateforme | Créée par | Point fort | Contrepartie | Qui contrôle les apps et les mises à jour |
|---|---|---|---|---|
| **Start9 (StartOS)** | 1 seule entreprise, qui vend aussi des serveurs | Open source. Construit autour de la souveraineté. Les sauvegardes chiffrées et l'accès WireGuard sont intégrés, et Tor est un [plugin facultatif](https://github.com/Start9Labs/start-technologies/releases/tag/start-os%2Fv0.4.0) | Catalogue d'apps plus petit, un peu plus à apprendre | Start9 pour le système. 2 registres par défaut, [d'autres peuvent être ajoutés](https://docs.start9.com/start-os/0.4.0.x/marketplace.html), et des paquets installés à la main |
| **YunoHost** | Une communauté de bénévoles, à but non lucratif | Open source, basé sur Debian, de nombreuses apps, 1 seule connexion pour toutes | Conçu pour des services accessibles depuis internet, donc les noms de domaine et l'e-mail apparaissent tôt. Interface plus sobre | Des bénévoles maintiennent le système et le catalogue. Toute app peut aussi être [installée depuis une URL](https://doc.yunohost.org/en/admin/apps/custom_apps/) |
| **Umbrel (umbrelOS)** | 1 seule entreprise, qui vend aussi son propre matériel | L'interface la plus soignée, une grande boutique d'apps, de solides apps Bitcoin et Lightning | Le code est public, mais la licence n'est pas une vraie licence open source (pas d'usage commercial) | Umbrel pour le système et la boutique officielle. Des [boutiques d'apps communautaires](https://umbrel.com/support/apps/how-to-add-a-community-app-store) peuvent être ajoutées, sans validation par Umbrel |
| **CasaOS** | 1 seule entreprise (IceWhale) | Open source. Une couche simple à ajouter par-dessus un système Linux existant | En mode maintenance en septembre 2026, car l'entreprise se concentre désormais sur son nouveau ZimaOS. Pas de sauvegardes intégrées | IceWhale pour la couche et sa boutique, qui accepte d'autres sources d'apps. Votre distribution Linux pour le système |
| **Debian ou Ubuntu avec Docker** | Vous | Contrôle total, vous apprenez comment tout fonctionne réellement, aucune plateforme dont dépendre | La ligne de commande, et personne à blâmer. Pour les curieux | Debian ou Ubuntu pour les paquets système, et l'éditeur de chaque image de conteneur que vous récupérez |

Ce qu'il faut héberger en premier.

| App | Remplace | Note |
|---|---|---|
| **Nextcloud** | Stockage cloud, agenda, contacts | La 1re app classique. Restez simple, n'installez pas tous les modules complémentaires |
| **Immich** | Bibliothèques de photos dans le cloud | Sauvegarde automatique des photos du téléphone. Évolue vite, lisez donc les notes de mise à jour |
| **Jellyfin** | Le streaming de vos propres films et de votre musique | Faible risque, un bon projet pour apprendre |
| **Home Assistant** | Les clouds de domotique | Garde vos appareils domestiques en local |
| **Vaultwarden** | La partie serveur d'un gestionnaire de mots de passe | Fonctionne avec les apps Bitwarden. Pas un projet de débutant, car un serveur en panne sans sauvegarde testée peut vous coûter tous vos mots de passe. Attendez que les restaurations soient une routine |
| **Un nœud Bitcoin** | Faire confiance au nœud de quelqu'un d'autre | Plus tard. Voir le chapitre 18 |

Une configuration raisonnable pour la plupart des gens est une plateforme open source comme StartOS ou YunoHost sur un mini PC, avec Nextcloud ou Immich comme 1re app. umbrelOS est l'alternative la plus soignée si sa licence vous convient.

## L'atteindre de l'extérieur, en sécurité

Un routeur domestique refuse normalement les connexions qui partent d'internet, de sorte qu'un serveur derrière lui n'est pas directement accessible de l'extérieur. Cette protection a toutefois des failles connues. De nombreux routeurs sont livrés avec UPnP activé, une fonction qui permet à n'importe quel appareil ou app de votre réseau d'ouvrir un port tout seul, et avec IPv6 chaque appareil peut recevoir une adresse publique que seul le pare-feu du routeur garde fermée. Il vaut la peine d'ouvrir les réglages du routeur pour désactiver UPnP et pour confirmer que le pare-feu IPv6 est activé.

L'erreur classique est d'ouvrir volontairement un port pour que vos fichiers soient accessibles de partout. Cela fonctionne, et cela montre aussi votre page de connexion à tous les scanners automatisés d'internet.

Des options plus sûres, de la plus indépendante à la plus pratique.

- **Un VPN WireGuard vers votre domicile.** Votre téléphone ouvre un tunnel chiffré vers votre propre réseau et se comporte comme s'il était chez vous. Open source, personne au milieu. Il demande un peu de configuration du routeur, et le CGNAT (une adresse publique partagée par plusieurs clients) peut empêcher une connexion entrante directe, sauf si vous mettez en place un autre point d'accès joignable ou un IPv6 qui fonctionne. Les 2 options ci-dessous sont souvent plus simples dans cette situation.
- **Les services onion de Tor.** umbrelOS les propose en option dans ses paramètres, et StartOS sous forme de plugin facultatif, votre serveur obtient donc une adresse .onion privée accessible via Tor, sans port ouvert. Plus lent, mais simple et privé.
- **Tailscale.** Construit sur WireGuard et très facile à installer sur le serveur et sur votre téléphone. Votre trafic reste chiffré entre vos appareils, mais une entreprise coordonne les connexions et les comptes. **Headscale** est un remplaçant open source de cette partie de coordination, que vous hébergez vous-même.

Quel que soit votre choix, changez d'abord tous les mots de passe par défaut.

## Pas à pas {#step-by-step}

L'exemple utilise StartOS parce qu'il est open source et s'installe sur du matériel ordinaire. La logique est la même sur YunoHost et umbrelOS.

1. **Choisissez le matériel.** Un portable inutilisé ou un mini PC avec 8 Go de mémoire et un SSD est largement suffisant pour les fichiers et les photos. Un nœud Bitcoin demande un SSD de 2 To (chapitre 18), et un modèle d'IA local pour la famille demande plus de mémoire (chapitre 11). Branchez-le à votre routeur avec un câble, pas en Wi-Fi.
2. **Installez la plateforme.** Téléchargez l'image depuis le site du projet, écrivez-la sur une clé USB, démarrez l'ordinateur dessus et suivez l'installateur. Quand le projet publie une somme de contrôle (une empreinte du fichier), comme le fait Start9 sur sa page de publication, comparez-la avant d'écrire l'image, car c'est l'étape qui remplace la confiance dans le téléchargement par une vérification. Cela efface le disque de l'ordinateur.
3. **Créez votre compte.** Ouvrez l'adresse affichée à la fin de l'installation depuis un autre appareil du même réseau. Choisissez un mot de passe long et unique et conservez-le dans votre gestionnaire de mots de passe. Si la plateforme propose l'authentification à 2 facteurs, comme umbrelOS dans ses paramètres, activez-la.
4. **Installez 1 app.** Seulement 1. Nextcloud ou Immich est un bon départ, installez donc l'app du téléphone, saisissez l'adresse de votre serveur et laissez-la copier vos photos.
5. **Mettez en place les sauvegardes.** Suivez la règle 3-2-1, qui signifie 3 copies de vos données, sur 2 appareils différents, avec 1 copie dans un autre lieu. En pratique, cela donne le serveur, un 2e disque et une copie chiffrée hors site (un disque chez un proche, ou une sauvegarde cloud chiffrée). Conservez le mot de passe de sauvegarde comme n'importe quelle clé du chapitre 6, sur papier en 2 endroits, car une sauvegarde chiffrée ne peut pas être ouverte sans lui. StartOS écrit des sauvegardes chiffrées sur un disque externe ou un dossier réseau, et umbrelOS peut [les exécuter automatiquement toutes les heures](https://umbrel.com/support/backups-and-recovery/backing-up-your-data). Si votre plateforme ne les planifie pas, ajoutez un rappel récurrent à votre agenda.
6. **Testez une restauration.** Récupérez 1 fichier depuis la sauvegarde, car une sauvegarde n'est prouvée que lorsque quelque chose en est revenu.
7. **Gardez-le à jour.** Examinez les mises à jour de la plateforme et des apps au moins 1 fois par mois, lisez les notes de version et gardez vos sauvegardes à jour. Appliquez rapidement les correctifs de sécurité pertinents, sans attendre la revue mensuelle quand une vulnérabilité connue touche votre installation. Après une mise à niveau majeure, faites une nouvelle sauvegarde. StartOS 0.4.0, par exemple, ne peut pas restaurer les sauvegardes faites avec des versions antérieures.
8. **Ajoutez seulement ensuite une 2e app.** Vivez avec la 1re pendant quelques semaines avant de grandir.

## Erreurs à éviter {#mistakes-to-avoid}

- **Ne pas avoir de sauvegardes.** Les disques tombent en panne sans prévenir, et les hébergeurs professionnels n'y échappent pas. Le 10 mars 2021, un incendie [a détruit le datacentre SBG2 d'OVHcloud](https://corporate.ovhcloud.com/en/newsroom/news/informations-site-strasbourg/) à Strasbourg, environ 120 000 services ont été touchés, et les clients sans copie ailleurs ont perdu leurs données. À la maison, la sauvegarde est votre travail, mettez-la donc en place avant de confier au serveur quoi que ce soit que vous ne pouvez pas perdre.
- **Exposer des services à internet avec des mots de passe par défaut.** Les scanners automatisés trouvent rapidement les services ouverts. Utilisez l'une des voies sûres ci-dessus et des mots de passe uniques partout.
- **Héberger votre e-mail ou vos mots de passe comme premier projet.** L'e-mail est le service le plus difficile à exploiter, car les grands fournisseurs rejettent souvent le courrier venant de serveurs domestiques et une erreur signifie des messages perdus. Un serveur de mots de passe qui tombe en panne sans sauvegarde testée vous enferme hors de tout le reste. Utilisez un bon fournisseur (chapitres 2 et 4) et hébergez d'abord autre chose.
- **Faire dépendre la famille du serveur avant qu'il soit stable.** Faites-le tourner pour vous seul pendant 1 ou 2 mois. Ne déplacez les photos de la famille que lorsque les sauvegardes et les mises à jour sont devenues une routine.
- **Supprimer trop tôt la copie du cloud.** Gardez votre ancien service en parallèle tant que vous n'avez pas restauré au moins 1 fois depuis votre propre sauvegarde.
- **Installer 20 apps la 1re semaine.** Chaque app est une chose de plus à mettre à jour et à sécuriser, et celles que vous oubliez deviennent le point faible du serveur.

## Pour aller plus loin {#go-further}

- **Plateformes :** start9.com, yunohost.org, umbrel.com, casaos.zimaspace.com.
- **Un grand catalogue de logiciels que vous pouvez héberger :** la liste awesome-selfhosted (awesome-selfhosted.net).
- **Accès à distance :** wireguard.com, tailscale.com, et Headscale (headscale.net).
- **Chapitre suivant :** l'IA sans vous livrer, où le même serveur peut faire tourner un modèle de langage pour la famille. Il revient encore 1 fois au chapitre 18, comme nœud Bitcoin.

## Sources {#sources}

- [Docker Engine security](https://docs.docker.com/engine/security/), documentation de Docker, consulté le 22 octobre 2026.
- [Updating Google Photos' storage policy to build for the future](https://blog.google/products-and-platforms/products/photos/storage-changes/), Google, 11 novembre 2020.
- [Strasbourg datacentre: latest information](https://corporate.ovhcloud.com/en/newsroom/news/informations-site-strasbourg/), OVHcloud, 18 mars 2021, mis à jour jusqu'en avril 2021.
- [Umbrel licence (PolyForm Noncommercial 1.0.0)](https://github.com/getumbrel/umbrel/blob/master/LICENSE.md), Umbrel sur GitHub, consulté en septembre 2026.
- [StartOS v0.4.0 release notes](https://github.com/Start9Labs/start-technologies/releases/tag/start-os%2Fv0.4.0), Start9 Labs sur GitHub, 24 juillet 2026, consulté le 29 octobre 2026.
- [StartOS licence (MIT)](https://github.com/Start9Labs/start-technologies/blob/master/LICENSE), Start9 Labs sur GitHub, consulté en septembre 2026.
- [Backing up your data](https://umbrel.com/support/backups-and-recovery/backing-up-your-data), assistance umbrelOS, consulté en septembre 2026.
- [Tailnet Lock](https://tailscale.com/kb/1226/tailnet-lock), documentation de Tailscale, consulté en septembre 2026.
- [Marketplace](https://docs.start9.com/start-os/0.4.0.x/marketplace.html), documentation de StartOS, consulté en septembre 2026.
- [Adding a community app store](https://umbrel.com/support/apps/how-to-add-a-community-app-store), assistance umbrelOS, consulté en septembre 2026.
- [Installing custom apps](https://doc.yunohost.org/en/admin/apps/custom_apps/), documentation de YunoHost, consulté en septembre 2026.

## Votre checklist {#your-checklist}

- [ ] Trouvez un ordinateur qui peut rester allumé, comme un vieux portable, un mini PC ou un Raspberry Pi (5 min)
- [ ] Installez une plateforme et une première app (1 week-end)
- [ ] Mettez en place des sauvegardes automatiques sur un 2e disque, plus une copie hors site (1 h)
- [ ] Restaurez un fichier depuis la sauvegarde pour vérifier que cela fonctionne (5 min)
- [ ] Choisissez une façon sûre de l'atteindre de l'extérieur, et changez tous les mots de passe par défaut (1 h)
