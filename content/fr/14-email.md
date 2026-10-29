# Chapitre 4 : Votre email et vos alias

## En bref {#in-brief}

Votre adresse email est la clé de tous vos autres comptes, et l'étiquette qui relie vos profils entre eux sur internet. Déplacez votre messagerie email vers un fournisseur qui vit d'abonnements et non de publicité, et qui peut chiffrer votre boîte afin que l'entreprise elle-même ne soit pas en mesure de la lire. Cessez ensuite de donner votre vraie adresse à tout le monde et utilisez des alias, avec une adresse différente pour chaque service. Vous verrez qui laisse fuiter ou vend votre adresse, et vous pourrez désactiver 1 alias sans toucher au reste.

## L'adresse qui relie tous vos comptes

Presque tous vos comptes peuvent être réinitialisés par email, si bien que celui qui contrôle votre boîte peut cliquer sur « mot de passe oublié » pour votre banque, vos réseaux sociaux et votre stockage cloud. La boîte email est aussi une archive de votre vie, avec des factures, des billets, des rendez-vous médicaux et des années de conversations.

Les boîtes email les plus populaires sont gratuites parce que l'entreprise qui transporte votre courrier gère aussi une activité publicitaire. Google [a annoncé en juin 2017](https://blog.google/products/gmail/g-suite-gains-traction-in-the-enterprise-g-suites-gmail-and-consumer-gmail-to-more-closely-align/) qu'il cesserait d'analyser le contenu de Gmail grand public pour personnaliser les publicités, mais la boîte reste liée à un compte qui peut aussi contenir vos recherches, vos vidéos et votre historique de position.

Il y a ensuite l'adresse elle-même, que vous donnez aux boutiques, aux newsletters, aux applications et aux administrations. Comme elle ne change jamais, les courtiers en données peuvent s'en servir pour réunir des bases de données distinctes en 1 seul profil de vous. Quand l'un de ces services est piraté, l'adresse se retrouve sur des listes utilisées pour le spam et pour l'hameçonnage, c'est-à-dire de faux messages écrits pour voler vos mots de passe. En 2020, Ledger, fabricant de hardware wallets (des appareils physiques qui conservent vos clés et signent vos transactions), [a perdu environ 1 million d'adresses email de clients](https://www.ledger.com/message-ledgers-ceo-data-leak) dans sa base marketing, ainsi que les coordonnées postales d'environ 272 000 clients, et des campagnes d'hameçonnage par email et par SMS ont suivi.

## Une boîte chiffrée et une adresse différente partout

Un **fournisseur d'email chiffré** stocke votre boîte sous une forme que l'entreprise ne peut pas lire. Chez Proton Mail et Tuta, c'est toujours activé, et les messages entre 2 utilisateurs du même fournisseur sont chiffrés de bout en bout. Chez Mailbox.org et Posteo, vous l'activez vous-même.

Un message envoyé à une adresse Gmail ou Outlook ordinaire n'est pas chiffré de bout en bout et reste lisible là-bas. Le chiffrement protège le contenu, pas les métadonnées (qui écrit à qui, et quand), et un tribunal peut encore contraindre un fournisseur à remettre ce qu'il détient. En septembre 2021, Proton [a confirmé qu'une ordonnance suisse l'avait obligé à enregistrer l'adresse IP](https://proton.me/blog/climate-activist-arrest) d'un militant pour le climat (le numéro qui identifie une connexion internet), tandis que le contenu restait hors de portée. Pour les conversations privées, utilisez une messagerie du chapitre 1.

Un **alias** est une adresse de transfert, comme shop-name@alias-service, créée pour 1 seule boutique. Ses messages arrivent dans votre boîte et la boutique ne voit jamais votre vraie adresse. Si cet alias commence à recevoir du spam, vous savez qui l'a laissé fuiter ou l'a vendu, et vous le désactivez en 1 clic. Les courtiers ont plus de mal à relier vos comptes, car chaque service vous connaît sous une adresse différente.

## Qui peut lire, falsifier ou verrouiller votre courrier

L'email a été conçu sans chiffrement ni preuve de l'expéditeur, si bien que sa confidentialité, son authenticité et sa disponibilité dépendent toutes de votre fournisseur. Un message venant d'une boîte ordinaire arrive chez le fournisseur sous forme lisible avant d'être chiffré pour le stockage. Vous comptez donc sur l'entreprise pour ne pas en garder de copie, pour livrer des applications honnêtes et pour maintenir votre compte ouvert. L'opérateur d'alias est un second tiers du même genre, puisque chaque message transféré traverse ses serveurs.

Le chiffrement de bout en bout retire le fournisseur du contenu seulement lorsque les 2 extrémités détiennent des clés, à l'intérieur d'1 seul fournisseur ou avec PGP entre 2 fournisseurs. Le fournisseur fournit alors la clé de l'autre personne, comme l'annuaire d'une messagerie (chapitre 1). Proton vous permet de [marquer la clé d'un contact comme de confiance](https://proton.me/support/address-verification), et Tuta [a ajouté la vérification des clés par QR code en août 2025](https://tuta.com/blog/key-verification). Avec PGP, vous comparez l'empreinte de la clé par un autre canal.

La disponibilité est la propriété que l'on peut décentraliser à peu de frais. Avec un domaine qui vous appartient, le fournisseur devient remplaçable et le bureau d'enregistrement du domaine devient la partie à surveiller. Faire tourner votre propre serveur de messagerie est possible, mais le sécuriser et faire accepter ses messages ailleurs en font un mauvais premier projet.

## Choisir votre fournisseur d'email

Toutes les options ci-dessous sont financées par leurs utilisateurs et non par la publicité. Elles diffèrent par le prix, par la manière de chiffrer et par la possibilité d'utiliser une application de messagerie ordinaire.

| Fournisseur | Établi en | En qui vous devez avoir confiance | Prix | Compromis |
|---|---|---|---|---|
| **[Proton Mail](https://proton.me/mail)** | Suisse | Proton voit le courrier entrant ordinaire avant de le chiffrer, et fournit les clés de vos contacts. Les clés de confiance sont une vérification facultative. | Offre gratuite, offres payantes | Boîte toujours chiffrée. Applications open source, grand écosystème (agenda, stockage, VPN). Les objets des messages ne sont pas chiffrés de bout en bout. Les applications de messagerie ordinaires nécessitent un programme « bridge » supplémentaire, sur une offre payante. |
| **[Tuta](https://tuta.com/)** | Allemagne | Tuta voit le courrier entrant ordinaire avant de le chiffrer, et fournit les clés de vos contacts. La vérification des clés est facultative. | Offre gratuite, offres payantes | Boîte toujours chiffrée. Applications open source, chiffre aussi les objets des messages. Utilise son propre système de chiffrement, donc pas d'applications de messagerie ordinaires ni de PGP (l'ancien standard de chiffrement des emails). |
| **[Mailbox.org](https://mailbox.org/en/)** | Allemagne | Mailbox.org peut lire le courrier stocké tant que vous n'avez pas activé le chiffrement de la boîte de réception. Avec PGP, vous vérifiez les clés vous-même. | Payant, prix bas | Boîte classique qui fonctionne avec n'importe quelle application de messagerie. Le chiffrement de votre boîte de réception (avec PGP) est facultatif, et vous l'activez vous-même. Moins soigné sur mobile. |
| **[Posteo](https://posteo.de/en)** | Allemagne | Posteo peut lire le courrier stocké tant que vous n'avez pas activé le chiffrement. Avec PGP, vous vérifiez les clés vous-même. | Payant, prix bas | Fonctionne avec n'importe quelle application de messagerie, peut être payé de façon anonyme, y compris en espèces par courrier. Le chiffrement de votre courrier stocké est facultatif, et vous l'activez vous-même. Ne prend pas en charge votre propre domaine. |
| **Votre propre domaine** | Là où vous l'hébergez | Le même fournisseur pour le contenu, plus votre bureau d'enregistrement de domaine. Aucun fournisseur ne peut garder votre adresse. | Frais annuels de domaine plus une boîte payante | you@your-name.eu, hébergé chez l'un des fournisseurs ci-dessus. Vous pouvez changer de fournisseur plus tard sans changer d'adresse. Vous ne devez jamais oublier de renouveler le domaine. |

Une configuration raisonnable pour la plupart des gens est 1 boîte de cette liste, avec le chiffrement activé là où il est facultatif, plus un service d'alias. Si vous comptez garder la même adresse pendant les 20 prochaines années, envisagez votre propre domaine dès le départ.

## Choisir votre service d'alias

Un service d'alias se place entre le monde et votre boîte. Il transfère votre courrier et peut techniquement voir les messages qui passent, choisissez donc un opérateur en qui vous avez autant confiance qu'en votre fournisseur d'email.

| Service | Qui l'exploite | Prix | Compromis |
|---|---|---|---|
| **[SimpleLogin](https://simplelogin.io/)** | Proton (Suisse) | Offre gratuite avec un nombre limité d'alias, payant pour un nombre illimité | Open source. Vous pouvez aussi répondre et écrire depuis un alias. Fonctionne avec n'importe quelle boîte, pas seulement Proton. Inclus dans certaines offres payantes de Proton. |
| **[Alias intégrés de Proton](https://proton.me/pass/aliases)** (« hide-my-email ») | Proton (Suisse), avec la technologie de SimpleLogin | Un nombre limité sur les offres gratuite et Mail Plus (10 en septembre 2026), illimité avec Pass Plus ou Proton Unlimited | Créés directement dans Proton Mail ou dans le gestionnaire de mots de passe Proton Pass. Très pratique si votre boîte est chez Proton. Votre boîte et vos alias sont alors entre les mains de la même entreprise, donc si ce compte est perdu ou bloqué, les 2 disparaissent. |
| **[addy.io](https://addy.io/)** | Un petit opérateur indépendant | Offre gratuite généreuse, offres payantes | Open source, et vous pouvez l'héberger vous-même. Une petite équipe est aussi un point de défaillance unique. |
| **[DuckDuckGo Email Protection](https://duckduckgo.com/email/)** | DuckDuckGo (États-Unis) | Gratuit | Très facile, supprime les traceurs cachés dans les emails. Nécessite l'application ou l'extension de navigateur DuckDuckGo. |
| **[Firefox Relay](https://relay.firefox.com/)** | Mozilla (États-Unis) | Offre gratuite avec quelques alias, payant pour en avoir plus | Simple, intégré à Firefox. Peu d'alias sur l'offre gratuite. |
| **Adresses supplémentaires chez votre fournisseur d'email** | Votre fournisseur d'email | Généralement dans les offres payantes | Proton Mail, Tuta, Mailbox.org et Posteo permettent tous d'ajouter quelques adresses supplémentaires à la même boîte. Rien de nouveau à qui faire confiance, mais le nombre est limité. |
| **Adressage avec « + » (« plus addressing »)** | N'importe quel fournisseur | Gratuit | you+shop@domain.com. Utile pour trier le courrier, faible pour la confidentialité, car votre vraie adresse y est visible et la partie « +shop » est facile à retirer. |

Une configuration raisonnable pour la plupart des gens est un service d'alias dédié avec une extension de navigateur, de sorte que créer un alias prenne 1 clic quand vous vous inscrivez quelque part. Choisir un opérateur différent de votre fournisseur d'email évite de dépendre d'1 seule entreprise pour les 2.

## Boîtes jetables pour un usage unique

Certains sites, vous n'y retournerez jamais, comme un téléchargement ponctuel, un portail Wi-Fi ou un forum lu 1 fois, et pour ceux-là une boîte jetable suffit. Il n'y a pas d'inscription. Vous inventez une adresse sur le moment, vous la saisissez dans le formulaire, puis vous ouvrez la boîte sur le site du service pour lire le message.

Sur les services publics de ce genre, il n'y a pas de mot de passe, donc quiconque devine ou connaît l'adresse peut lire la boîte. Les messages sont supprimés rapidement, vous ne pouvez pas compter les retrouver plus tard, et de nombreux sites refusent ces domaines. Une boîte jetable convient donc pour un code de vérification qui ne protège rien d'important. C'est le mauvais outil pour un compte que vous voulez garder, pour tout ce qui contient des données personnelles, ou partout où une réinitialisation de mot de passe pourrait être envoyée plus tard, car quiconque saisirait la même adresse la recevrait. Pour tout le reste, un alias fait mieux l'affaire.

| Service | Comment obtenir une adresse | Durée de conservation du courrier | Compromis |
|---|---|---|---|
| **[Mailinator](https://www.mailinator.com/)** | Inventez n'importe quel nom sur son domaine public | Quelques heures | Entièrement public, donc quiconque saisit le même nom lit la même boîte. Réception uniquement. Conçu surtout pour les testeurs de logiciels, avec des offres privées payantes. Largement bloqué. |
| **[Guerrilla Mail](https://www.guerrillamail.com/)** | Une adresse aléatoire vous est attribuée, ou vous en choisissez une | 1 heure | Pas de mot de passe, donc la boîte n'est protégée que par la difficulté à deviner son nom. Propose une adresse « brouillée » pour rendre la devinette plus difficile. |
| **[Maildrop](https://maildrop.cc/)** | Inventez n'importe quel nom sur son domaine public | 10 messages au maximum, effacés après 24 heures sans nouveau courrier | Entièrement public, sans mot de passe. Les pièces jointes sont supprimées. |

## Quand un site exige un numéro de téléphone

Votre numéro de téléphone est un identifiant encore plus fort que votre adresse email. Vous le gardez des années, il relie vos comptes entre eux, il attire les appels indésirables, et il est la cible des attaques de SIM swap (chapitre 2). Vérifiez d'abord si le champ est vraiment obligatoire. Quand il l'est, vous avez plusieurs options, aucune n'étant parfaite.

| Option | Fonctionnement | Compromis |
|---|---|---|
| **Une seconde SIM ou eSIM, utilisée uniquement pour les inscriptions** | Un vrai numéro mobile d'un opérateur ordinaire, gardé à part de votre numéro personnel | Accepté partout. Les numéros prépayés expirent si vous ne les rechargez pas. En 2025, [19 des 28 pays européens étudiés par Cullen International](https://www.cullen-international.com/news/2025/10/19-EU-countries-mandate-the-registration-of-prepaid-customers.html) imposaient aux opérateurs d'enregistrer l'identité des clients prépayés. Les règles varient, et cette option sépare vos numéros sans vous rendre anonyme. |
| **Applications de numéros virtuels (VoIP)** [JMP.chat](https://jmp.chat/), [Hushed](https://hushed.com/), [MySudo](https://mysudo.com/) | Un numéro payant qui fonctionne par internet, dans une application | JMP.chat est open source mais ne propose que des numéros américains et canadiens. Hushed (code fermé) propose des numéros américains, canadiens et britanniques. MySudo (code fermé) ne peut être installé que dans quelques pays, vérifiez donc avant de compter dessus. De nombreux services refusent les numéros VoIP, et un site européen peut refuser un numéro étranger. |
| **Une eSIM de données payée en bitcoin,** par exemple [Silent.link](https://silent.link/) | Pas de compte. Certaines offres incluent un numéro mobile américain ou britannique capable de recevoir des SMS | Coûte plus cher qu'une SIM ordinaire. Le numéro est loué à l'année, et il disparaît si vous ne le renouvelez pas. 1 seul petit opérateur. |
| **Services payants de réception de SMS à usage unique** | Vous louez un numéro pour quelques minutes afin de recevoir 1 seul code | Le numéro passe ensuite à quelqu'un d'autre, qui pourrait s'en servir pour prendre le contrôle du compte. La qualité varie beaucoup, et de nombreux sites l'interdisent dans leurs conditions. |
| **Sites publics gratuits de « réception de SMS en ligne »** | Des numéros partagés dont les messages entrants sont affichés sur une page web | Tout le monde voit votre code. Les numéros sont recyclés et déjà bloqués pour la plupart. Seulement pour quelque chose qui n'a aucune importance. |

Ces options ont elles aussi leurs limites. Si vous perdez l'accès au numéro, vous pouvez perdre le compte, n'utilisez donc jamais un numéro que vous ne contrôlez pas pour votre banque, pour l'authentification à 2 facteurs ou pour tout compte important. Respectez les conditions d'utilisation du site et la loi de votre pays. L'objectif est simplement d'éviter de donner votre numéro personnel à chaque boutique et à chaque application.

## Pas à pas {#step-by-step}

L'exemple utilise Proton Mail pour la boîte et SimpleLogin pour les alias, car c'est un premier pas courant. Les 2 appartiennent à Proton, ce qui est pratique mais signifie que votre boîte et vos alias dépendent d'1 seule entreprise. Si vous préférez répartir le risque, gardez la boîte et choisissez addy.io pour les alias, ou gardez SimpleLogin et choisissez une autre boîte, car les étapes sont les mêmes.

1. **Ouvrez la nouvelle boîte.** Choisissez une adresse que vous pouvez garder pendant des années. Protégez-la avec un mot de passe long et unique issu de votre gestionnaire de mots de passe et avec un second facteur (chapitre 2). Activez la phrase de récupération et notez-la sur papier. Elle rétablit à la fois votre accès et votre courrier chiffré. Une réinitialisation par email ou par SMS ne rend que l'accès, et vos anciens messages peuvent rester illisibles. Consultez [les instructions de récupération du fournisseur](https://proton.me/support/set-account-recovery-methods) avant de vous y fier.
2. **Configurez le service d'alias.** Créez le compte, connectez-le à votre nouvelle boîte, et installez son extension de navigateur (et son application pour téléphone, s'il en a une).
3. **Déplacez d'abord vos comptes les plus importants.** Ce sont votre banque, les services publics, votre opérateur téléphonique, votre compte Apple ou Google et votre gestionnaire de mots de passe. Changez l'adresse email dans chacun d'eux. Utilisez votre vraie nouvelle adresse ou un alias dédié, comme vous préférez, mais notez votre choix dans votre gestionnaire de mots de passe.
4. **Transférez l'ancienne boîte.** Dans les paramètres de votre ancienne boîte, activez le transfert automatique vers la nouvelle. La plupart des fournisseurs chiffrés proposent aussi un outil d'import qui copie vos anciens messages et contacts.
5. **Déplacez le reste au fil de l'eau.** Chaque fois qu'un message transféré arrive d'un service que vous utilisez encore, changez l'adresse là-bas pour un nouvel alias. Supprimez les comptes que vous n'utilisez plus.
6. **Créez un nouvel alias pour chaque inscription.** Une boutique, une newsletter ou un portail Wi-Fi reçoivent chacun leur propre adresse. Nommez l'alias d'après le service, afin qu'une fuite soit facile à retracer.
7. **Gardez l'ancienne adresse pendant au moins 1 an.** Ne la supprimez pas, car des comptes oubliés, d'anciens contacts et des réinitialisations de mot de passe continueront d'y arriver pendant longtemps.

## Erreurs à éviter {#mistakes-to-avoid}

- **Penser qu'un fournisseur chiffré rend tout votre email privé.** Il protège votre boîte, alors qu'un message envoyé à une boîte ordinaire reste lisible à l'autre bout.
- **Supprimer trop tôt l'ancienne adresse.** Certains fournisseurs recyclent les adresses abandonnées, et un inconnu pourrait alors recevoir les réinitialisations de mot de passe de comptes que vous avez oubliés.
- **Perdre la phrase de récupération.** Sans elle, un mot de passe oublié peut vous coûter vos anciens messages (étape 1).
- **Laisser votre propre domaine expirer.** Celui qui l'enregistre après vous reçoit votre courrier et peut réinitialiser vos comptes. Activez le renouvellement automatique et gardez la carte de paiement à jour.
- **Utiliser le même alias pour tout.** Un alias partagé entre 10 services n'est qu'une seconde vraie adresse, puisque la valeur vient du fait d'avoir un alias différent pour chaque service.
- **Placer la banque derrière un service d'alias en qui vous n'avez pas pleinement confiance.** Pour les quelques comptes qui comptent le plus, votre vraie adresse chez votre propre fournisseur est un choix parfaitement valable.

## Pour aller plus loin {#go-further}

- **Comparer les fournisseurs en détail :** Privacy Guides, [« Email Services »](https://www.privacyguides.org/en/email/) et [« Email Aliasing »](https://www.privacyguides.org/en/email-aliasing/).
- **Vérifier si votre adresse a déjà fuité :** [Have I Been Pwned](https://haveibeenpwned.com/).
- **Chapitre suivant :** votre réseau.

## Sources {#sources}

- [Proton Account recovery explained](https://proton.me/support/set-account-recovery-methods), Proton Support, consulté le 22 octobre 2026.
- [As G Suite gains traction in the enterprise, G Suite's Gmail and consumer Gmail to more closely align](https://blog.google/products/gmail/g-suite-gains-traction-in-the-enterprise-g-suites-gmail-and-consumer-gmail-to-more-closely-align/), Google, 23 juin 2017.
- [Message by Ledger's CEO: update on the July data breach](https://www.ledger.com/message-ledgers-ceo-data-leak), Ledger, 21 décembre 2020.
- [Important clarifications regarding arrest of climate activist](https://proton.me/blog/climate-activist-arrest), Proton, 6 septembre 2021.
- [Address verification with trusted keys](https://proton.me/support/address-verification), Proton, consulté en septembre 2026.
- [Tuta introduces key verification](https://tuta.com/blog/key-verification), Tuta, 26 août 2025.
- [19 EU countries mandate the registration of prepaid customers](https://www.cullen-international.com/news/2025/10/19-EU-countries-mandate-the-registration-of-prepaid-customers.html), Cullen International, 8 octobre 2025, consulté le 29 octobre 2026.

## Votre checklist {#your-checklist}

- [ ] Ouvrez une boîte email chez un fournisseur financé par ses utilisateurs (1 h)
- [ ] Configurez un service d'alias et son extension de navigateur (1 h)
- [ ] Créez votre premier alias et utilisez-le pour votre prochaine inscription (5 min)
- [ ] Déplacez vos 5 comptes les plus importants vers la nouvelle adresse (1 h)
- [ ] Transférez l'ancienne boîte et déplacez les comptes restants (1 week-end)
