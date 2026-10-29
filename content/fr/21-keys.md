# Chapitre 6 : Des clés plutôt que des comptes

## En bref {#in-brief}

Un compte est une autorisation qu'une entreprise vous accorde et peut reprendre. Une clé est un secret que vous seul détenez, et elle fonctionne grâce aux mathématiques, qu'une entreprise soit d'accord ou non. Vous utilisez déjà des clés tous les jours sans les voir, dans votre messagerie et dans vos passkeys (clés d'accès). Le prix de cette liberté est que personne ne peut réinitialiser une clé à votre place, si bien que la plus grande partie de ce chapitre porte sur la manière de garder vos clés en sécurité.

## Un compte est une autorisation révocable

Un compte est une ligne dans la base de données de quelqu'un d'autre, et c'est l'entreprise qui décide de ce que cette ligne permet. Elle peut la verrouiller par erreur, par une décision automatisée, après un changement de règles, ou parce que le service ferme ou quitte votre pays. Des gens perdent ainsi des années d'e-mails et de photos, souvent sans aucun être humain à qui parler.

Un compte n'est aussi sûr que cette base de données. En novembre 2022, la Commission irlandaise de protection des données [a infligé à Meta une amende de 265 millions d'euros](https://www.dataprotection.ie/en/news-media/press-releases/data-protection-commission-announces-decision-in-facebook-data-scraping-inquiry) après la publication en ligne de données personnelles de plus de 500 millions d'utilisateurs de Facebook, numéros de téléphone compris.

Le bouton « mot de passe oublié » est une 2e porte d'entrée, ouverte à quiconque contrôle votre adresse e-mail ou votre numéro de téléphone. En mars 2020, Europol [a annoncé l'arrestation de 12 personnes en Espagne](https://www.europol.europa.eu/media-press/newsroom/news/sim-highjackers-how-criminals-are-stealing-millions-highjacking-phone-numbers), soupçonnées d'avoir volé plus de 3 millions d'euros en obtenant des doubles des cartes SIM de leurs victimes et en recevant à leur place les codes de confirmation des banques.

Les comptes sont pratiques et conviennent pour la plupart des services. Pour ce qui compte le plus (votre identité, vos conversations privées, votre argent), il vaut la peine de se demander si la chose pourrait fonctionner sans demander la permission à personne. Avec des clés, dans une large mesure, c'est possible.

## Un secret qui prouve qui vous êtes

Une **paire de clés** est composée de 2 très grands nombres créés ensemble sur votre appareil. La **clé privée** est un secret qui reste chez vous, et la **clé publique** est calculée à partir d'elle et peut être montrée à tout le monde. Passer de la clé privée à la clé publique est facile, alors que faire le chemin inverse est pratiquement impossible.

Une paire de clés fait 2 choses.

- **Recevoir des secrets.** Imaginez une boîte aux lettres avec une fente. Toute personne qui connaît l'adresse (votre clé publique) peut y glisser une lettre, et seul le détenteur de la clé de la boîte (votre clé privée) peut l'ouvrir.
- **Signer.** Votre clé privée produit une signature que n'importe qui peut vérifier avec votre clé publique, et qui ne peut pas être falsifiée en pratique sans la clé privée.

Aucun serveur central n'est nécessaire pour confirmer qui vous êtes, car la vérification est un calcul que n'importe qui peut effectuer.

Vous rencontrez déjà des clés sans le savoir. Votre messagerie chiffrée (chapitre 1) a créé une paire de clés sur votre téléphone. Une passkey (chapitre 2) est une paire de clés dont le site ne conserve que la moitié publique, et une identité Nostr (chapitre 7) est aussi une paire de clés. Beaucoup de wallets (portefeuilles) Bitcoin (partie 3) dérivent leurs clés d'une sauvegarde de 12 ou 24 mots, tandis que d'autres utilisent des formats différents (chapitre 14). Pour les curieux, les clés SSH connectent les administrateurs aux serveurs, et les clés PGP chiffrent les e-mails et signent des logiciels.

## Quelqu'un se porte toujours garant des clés des autres

Une clé supprime le tiers pour 1 propriété, le contrôle, car personne ne peut signer ni déchiffrer à votre place. L'authenticité reste ouverte dès qu'une clé appartenant à quelqu'un d'autre entre en jeu, puisque rien dans une clé publique n'indique à qui elle appartient. Cette information doit venir de quelque part, et il existe 4 réponses habituelles, un annuaire géré par une entreprise, comme dans la plupart des messageries (chapitre 1), une autorité de certification, qui est la manière dont votre navigateur reconnaît un site web, un réseau de confiance dans lequel les gens signent mutuellement leurs clés, comme le font les utilisateurs de PGP, ou une empreinte que vous comparez vous-même par un autre canal.

Seule la dernière réponse n'a pas de tiers de confiance. En 2011, l'autorité de certification néerlandaise DigiNotar a été piratée, [un faux certificat pour google.com a été émis](https://blog.mozilla.org/security/2011/08/29/fraudulent-google-com-certificate/) et les navigateurs ont retiré DigiNotar de leurs listes de confiance. Les journaux publics de [Certificate Transparency](https://certificate.transparency.dev/) permettent désormais à n'importe qui de voir quels certificats existent pour un domaine.

Les passkeys illustrent le même compromis pour le stockage. Synchronisées par Apple ou Google, elles sont [chiffrées de bout en bout](https://support.apple.com/en-us/102195), mais pour y accéder depuis un nouvel appareil il faut passer par votre compte chez cette entreprise, qui revient ainsi dans la boucle pour la disponibilité. Une passkey stockée sur une clé de sécurité ne dépend de personne, et elle ne peut pas être copiée.

## Choisissez où garder vos clés

Avec une clé, il n'y a pas de bouton « mot de passe oublié ». Aucune entreprise ne peut vous en bloquer l'accès, et aucune entreprise ne peut vous y redonner accès. Une clé perdue est perdue, et quiconque la copie peut agir à votre place. La responsabilité passe de l'entreprise à vous, et chaque clé a donc besoin d'un lieu de stockage proportionné à sa valeur.

| Où | Convient pour | Point faible | De qui vous dépendez encore |
|---|---|---|---|
| **Papier, écrit à la main, en 2 endroits** | Codes de récupération, une clé Nostr, une phrase de récupération pour de petits montants | Le feu, l'eau, et quiconque le trouve | De personne, sauf de quiconque peut entrer dans ces 2 endroits |
| **Gestionnaire de mots de passe** (chapitre 2) | Clés de faible valeur et codes de récupération de sites ordinaires | Il vit sur des appareils connectés. Ce n'est pas l'endroit pour une phrase de récupération Bitcoin, et il ne peut pas contenir ses propres codes de récupération | Le fournisseur, pour la synchronisation et les mises à jour de l'app. Le coffre est chiffré de bout en bout, et les gestionnaires open source peuvent être audités |
| **Appareil matériel** | Une clé de sécurité pour les connexions (YubiKey, Nitrokey, Token2, entre autres), un hardware wallet (appareil de signature) pour Bitcoin (chapitre 17) | Coûte de l'argent, peut casser ou être perdu. Il faut tout de même une sauvegarde, soit une 2e clé de sécurité, soit la phrase de récupération sur papier ou sur acier | Le fabricant de la puce et de son firmware. Le firmware de YubiKey est fermé, celui de Nitrokey est open source |
| **Sauvegarde sur acier** | Phrases de récupération qui doivent survivre au feu et à l'eau (chapitre 14) | Plus chère, et lisible par quiconque la trouve | De personne, sauf de quiconque peut atteindre la cachette |
| **Partage ou multisignature** | Valeur élevée, avec plusieurs clés à plusieurs endroits, pour qu'aucune perte ou aucun vol isolé ne soit fatal | Complexe. Une erreur de configuration peut vous verrouiller dehors. Apprenez d'abord | D'aucune partie unique. Du logiciel qui coordonne les clés, et des personnes ou des lieux qui les détiennent |

Une configuration raisonnable pour la plupart des gens associe **un gestionnaire de mots de passe pour les clés de faible valeur**, **du papier en 2 endroits pour les codes de récupération qui protègent tout le reste**, **2 clés de sécurité pour vos comptes principaux**, et un hardware wallet avec une sauvegarde sur acier dès que de réelles économies sont en jeu. Votre situation peut appeler un autre dosage.

## Pas à pas {#step-by-step}

L'exemple utilise les clés que la plupart des lecteurs possèdent déjà, et la logique est la même pour toutes les clés que vous créerez plus tard.

1. **Faites un inventaire.** Sur papier, listez les noms de vos clés et de vos codes de récupération, pas les secrets eux-mêmes. Il s'agit du mot de passe maître et du kit de récupération de votre gestionnaire de mots de passe, des codes de récupération de l'authentification à 2 facteurs de vos comptes principaux, du code PIN de votre messagerie, de la clé de récupération du chiffrement de disque de votre ordinateur, puis plus tard de votre clé Nostr et de votre phrase de récupération. Les passkeys ne peuvent pas être écrites, notez donc où chacune se trouve (quel téléphone, quel gestionnaire ou quelle clé de sécurité) et la 2e façon d'accéder à ce compte.
2. **Décidez d'un lieu pour chacune,** à l'aide du tableau ci-dessus, et écrivez-le à côté du nom.
3. **Écrivez les sauvegardes à la main.** Pas de photo, pas de capture d'écran, pas de note dans le cloud, pas d'imprimante de bureau. Écrivez lisiblement et vérifiez chaque caractère 2 fois.
4. **Rangez-les dans 2 endroits,** par exemple chez vous et chez un proche de confiance, ou dans un coffre bancaire si vous en acceptez les horaires d'ouverture et les règles. 1 seul incendie ou 1 seul cambriolage ne doit pas pouvoir emporter les 2 copies.
5. **Achetez 2 clés de sécurité, pas 1.** Une clé de sécurité ne peut pas être copiée, la 2e clé est donc un accès indépendant, et non une copie de la 1re. Enregistrez les 2 sur vos comptes principaux (e-mail, gestionnaire de mots de passe, stockage cloud) dans les paramètres de sécurité, sous « clé de sécurité » ou « passkey ». Gardez la 1re avec vous et la 2e avec vos sauvegardes papier, et conservez aussi les codes de récupération de ces comptes.
6. **Testez une récupération.** Connectez-vous à un compte avec un code de récupération, puis générez de nouveaux codes. Les anciens codes cessent de fonctionner, recopiez donc les nouveaux sur les 2 copies papier et détruisez les anciennes feuilles. Connectez-vous aussi 1 fois avec la 2e clé de sécurité, car une sauvegarde non testée peut échouer le jour où vous en avez besoin. C'est l'étape qui remplace la confiance dans une sauvegarde, et dans le processus de récupération d'une entreprise, par quelque chose que vous avez vérifié vous-même.
7. **Prévenez une personne de confiance** de l'endroit où se trouvent les choses et de ce qu'il faut faire, mais sans lui donner les secrets eux-mêmes. Une lettre scellée avec des instructions suffit. Aucune entreprise ne pourra aider votre famille à récupérer une clé après votre disparition.
8. **Révisez la liste 1 fois par an.**

## Erreurs à éviter {#mistakes-to-avoid}

- **Photographier une clé ou une phrase de récupération.** Les photos sont copiées vers des services cloud et peuvent être lues par d'autres apps, ce qui en fait une manière courante pour un secret de quitter vos mains.
- **Saisir une clé privée sur un site web, ou la donner au « support ».** Aucun service légitime ne la demande, et une demande de ce genre est la marque d'une arnaque.
- **Garder l'unique copie sur votre téléphone.** Des téléphones sont perdus, volés et cassés tous les jours.
- **Ranger la sauvegarde à côté de l'appareil.** Un voleur ou un incendie emporte alors les 2 en même temps.
- **La cacher si bien que personne ne la trouve.** Cela vous inclut dans 5 ans, et votre famille après vous.
- **Choisir trop tôt un schéma complexe.** Une sauvegarde fragmentée que vous ne comprenez pas entièrement est plus dangereuse que 2 feuilles de papier dans 2 endroits sûrs.

## Pour aller plus loin {#go-further}

- **Comprendre le chiffrement à clé publique :** Surveillance Self-Defense, « A Deep Dive on End-to-End Encryption », par l'Electronic Frontier Foundation (ssd.eff.org).
- **Comparer les clés de sécurité et les gestionnaires de mots de passe :** Privacy Guides (privacyguides.org).
- **Se renseigner sur les passkeys :** la FIDO Alliance (fidoalliance.org).
- **Chapitre suivant :** Nostr, des réseaux sociaux construits sur des clés plutôt que sur des comptes.

## Sources {#sources}

- [Data Protection Commission announces decision in Facebook "Data Scraping" Inquiry](https://www.dataprotection.ie/en/news-media/press-releases/data-protection-commission-announces-decision-in-facebook-data-scraping-inquiry), Data Protection Commission (Irlande), 28 novembre 2022.
- [Meta hit with ~$275M GDPR penalty for Facebook data-scraping breach](https://techcrunch.com/2022/11/28/facebook-gdpr-penalty/), TechCrunch, 28 novembre 2022.
- [The SIM highjackers: how criminals are stealing millions by highjacking phone numbers](https://www.europol.europa.eu/media-press/newsroom/news/sim-highjackers-how-criminals-are-stealing-millions-highjacking-phone-numbers), Europol, mars 2020.
- [Fraudulent *.google.com certificate](https://blog.mozilla.org/security/2011/08/29/fraudulent-google-com-certificate/), Mozilla Security Blog, 29 août 2011.
- [Certificate Transparency](https://certificate.transparency.dev/), site du projet, consulté en septembre 2026.
- [About the security of passkeys](https://support.apple.com/en-us/102195), Apple Support, consulté en septembre 2026.

## Votre checklist {#your-checklist}

- [ ] Listez toutes les clés et tous les codes de récupération que vous possédez déjà (1 h)
- [ ] Écrivez à la main les sauvegardes manquantes et rangez-les dans 2 endroits (1 h)
- [ ] Testez une récupération avec un vrai code de récupération (5 min)
- [ ] Prévenez une personne de confiance de l'endroit où se trouvent vos sauvegardes (5 min)
- [ ] Achetez 2 clés de sécurité et ajoutez-les à vos comptes principaux (1 week-end)
