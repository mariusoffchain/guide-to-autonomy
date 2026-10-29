# Chapitre 1 : Vos messages

## En bref {#in-brief}

Vos conversations comptent parmi les données les plus intimes que vous produisez. Déplacez-les vers une messagerie chiffrée de bout en bout par défaut, open source, et qui collecte le moins de métadonnées possible. Il en existe plusieurs bonnes, et aucune ne l'emporte sur tous les points. Choisissez-en une, migrez d'abord vos 5 contacts les plus proches, et gardez votre ancienne application pour tous les autres.

## Chiffré ne veut pas dire privé

Beaucoup d'applications de messagerie courantes appartiennent à des entreprises publicitaires. WhatsApp et Messenger, détenus par Meta (les 2), chiffrent bien le contenu de vos messages, mais elles enregistrent tout de même avec qui vous parlez, quand, à quelle fréquence, depuis quel appareil et quel lieu, et elles relient ces informations au reste de ce que le groupe sait de vous.

D'autres ne chiffrent pas du tout par défaut. Sur Telegram, les conversations ordinaires et toutes les conversations de groupe sont stockées sous une forme que l'entreprise peut lire. Le SMS est plus faible encore, car votre opérateur peut le lire et il traverse le réseau téléphonique sans chiffrement. Après l'intrusion du groupe connu sous le nom de Salt Typhoon dans plusieurs opérateurs télécoms américains, l'agence américaine de cybersécurité CISA [a recommandé en décembre 2024](https://www.cisa.gov/resources-tools/resources/mobile-communications-best-practice-guidance) que les personnes très ciblées utilisent uniquement des messageries chiffrées de bout en bout et cessent de s'appuyer sur le SMS pour les codes de connexion.

Viennent ensuite les sauvegardes. Une conversation peut être chiffrée pendant son transport et se retrouver lisible dans une sauvegarde cloud, la vôtre ou celle de la personne avec qui vous parlez.

Les conséquences sont concrètes. Des conversations fuitent, des comptes sont pris en main par des escrocs qui écrivent ensuite à votre famille, et des messages sont transmis sur demande judiciaire, des années après que vous avez oublié les avoir écrits.

## Une enveloppe scellée que le facteur ne peut pas ouvrir

Avec le **chiffrement de bout en bout**, un message est verrouillé sur votre téléphone et ne peut être déverrouillé que sur celui de la personne à qui vous écrivez. L'entreprise au milieu transporte une enveloppe scellée qu'elle ne peut pas ouvrir. Si elle est piratée ou reçoit une demande judiciaire, elle n'a donc aucun contenu de message à fournir. Selon la conception de l'application, elle peut tout de même conserver des métadonnées, comme une adresse IP, une liste de contacts ou la date de votre dernière connexion.

Cette enveloppe est aussi un sujet politique en Europe. Le règlement que la Commission européenne [a proposé le 11 mai 2022](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52022PC0209), connu de ses détracteurs sous le nom de « Chat Control », permettrait aux autorités d'ordonner aux services de messagerie d'analyser les communications privées. En octobre 2026, il est [toujours en cours de négociation](https://www.europarl.europa.eu/legislative-train/theme-promoting-our-european-way-of-life/file-combating-child-sexual-abuse-online) entre le Parlement et le Conseil. Le 6e cycle de négociations, le 29 septembre 2026, [s'est terminé sans accord sur l'analyse des messages privés](https://data.consilium.europa.eu/doc/document/WK-15082-2026-INIT/en/pdf), et un nouveau cycle est attendu avant la fin de 2026. En attendant, la règle temporaire qui permet aux fournisseurs d'analyser volontairement, le règlement (UE) 2026/1881, a été [de nouveau approuvée en juillet 2026](https://www.consilium.europa.eu/en/press/press-releases/2026/07/23/fighting-child-sexual-abuse-online-interim-measure-protecting-children-now-reinstated/) et s'applique jusqu'au 3 avril 2028. À la demande du Parlement, elle [exclut les communications chiffrées de bout en bout](https://www.europarl.europa.eu/news/en/press-room/20260706IPR46318/combating-child-sexual-abuse-support-for-a-more-limited-eprivacy-derogation).

Le chiffrement est nécessaire, mais 3 autres éléments comptent aussi.

- **Open source.** Le code est public, si bien que des experts indépendants peuvent vérifier que l'application fait ce qu'elle annonce, au lieu de croire l'entreprise sur parole.
- **Métadonnées.** Les messageries les plus soigneuses sont conçues pour savoir très peu de choses sur vous, ce qui peut signifier aucune liste de contacts, aucune appartenance à des groupes et parfois aucun identifiant du tout.
- **Qui l'exploite.** Une organisation à but non lucratif ou une communauté n'a pas d'activité publicitaire à nourrir, et un réseau sans entreprise centrale n'a pas de porte unique à laquelle frapper.

## Confidentiel ne veut pas dire authentique

Le chiffrement répond à 1 question, celle de savoir si quelqu'un d'autre peut lire le message, et en laisse une autre ouverte, celle de savoir si la personne à l'autre bout est bien celle que vous croyez. Les cryptographes appellent la première propriété la confidentialité et la seconde l'authenticité. Un SMS ou un email n'offre ni l'une ni l'autre. Une voix familière au téléphone peut vous aider à reconnaître quelqu'un, mais elle ne rend pas l'appel confidentiel et ne prouve pas l'identité, puisque [les voix peuvent être clonées](https://consumer.ftc.gov/articles/scammers-use-fake-emergencies-steal-your-money). Un canal sûr doit offrir les 2.

L'authenticité dépend de la manière dont votre application a obtenu la clé de l'autre personne. Dans Signal, WhatsApp, iMessage et la plupart des messageries chiffrées, cette clé provient d'un annuaire géré par l'entreprise, ce qui fait de celle-ci un tiers de confiance, aussi bien qu'elle chiffre. Si l'annuaire était compromis, ou contraint de distribuer une fausse clé, l'enveloppe resterait scellée, mais pour le mauvais destinataire. Des garde-fous existent, avec les [numéros de sécurité de Signal](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed) (60 chiffres à comparer), la [transparence des clés de WhatsApp](https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/) et la [vérification des clés de contact d'iMessage](https://security.apple.com/blog/imessage-contact-key-verification/), mais ils sont facultatifs et rarement utilisés.

D'autres conceptions suppriment l'annuaire et décentralisent cette confiance. Olvid [exige l'échange de 2 codes de 4 chiffres](https://olvid.io/faq/olvid-secure-channels/) avant le premier message, tandis que SimpleX et Briar partent d'un lien ou d'un QR code que vous remettez vous-même. La sécurité repose alors sur les 2 personnes concernées, et le prix à payer est la commodité, puisque l'application ne peut pas retrouver vos contacts à votre place.

## Choisir votre messagerie

Commencez par regarder honnêtement ce que vous utilisez probablement aujourd'hui. Aucune de ces applications n'est inutile, mais chacune a un point faible évident. Le tableau reflète la situation en septembre 2026.

| Messagerie | Propriétaire | Chiffrée de bout en bout ? | Ce qu'elle collecte ou expose encore | Verdict |
|---|---|---|---|---|
| [**WhatsApp**](https://www.whatsapp.com/) | Meta | Oui, par défaut (protocole Signal) | Métadonnées étendues (vos contacts, les personnes à qui vous écrivez, quand, depuis quel appareil). Code fermé. Les sauvegardes cloud ne sont chiffrées de bout en bout que si vous l'activez. | Contenu protégé, métadonnées au service d'un groupe publicitaire. |
| [**Facebook Messenger**](https://www.messenger.com/) | Meta | Oui, par défaut pour les conversations et appels personnels depuis décembre 2023. Pas pour les conversations avec des entreprises ni pour Marketplace. | Les mêmes métadonnées, liées à votre identité Facebook. Code fermé. | Mieux qu'avant, mais toujours un produit Meta. |
| [**Messages privés Instagram**](https://www.instagram.com/) | Meta | Non. Les conversations chiffrées facultatives ont été supprimées le 8 mai 2026. | Meta peut lire le contenu de chaque message, en plus des métadonnées. | Pas pour quoi que ce soit de privé. |
| [**Telegram**](https://telegram.org/) | Telegram, une entreprise privée | Seulement dans les « conversations secrètes », que vous démarrez à la main, entre 2 personnes. Pas les conversations ordinaires, ni tous les groupes et canaux. | Les messages ordinaires sont stockés sur les serveurs de Telegram, que l'entreprise peut lire. Le code du serveur est fermé. | Un réseau social plus qu'une messagerie privée. |
| **SMS** | Votre opérateur mobile | Non | Contenu et métadonnées lisibles par les opérateurs, interceptables, et détournables par un SIM swap (un escroc fait transférer votre numéro vers sa carte SIM). | À éviter pour tout ce qui est sensible, y compris les codes de connexion quand vous avez le choix. |
| [**iMessage (Apple Messages)**](https://support.apple.com/messages) | Apple | Oui, entre appareils Apple (bulles bleues) | Appareils Apple uniquement. Code fermé. Les sauvegardes iCloud sont lisibles par Apple, sauf si vous activez la Protection avancée des données (Advanced Data Protection). | Bon dans l'univers Apple, et nulle part ailleurs. |
| [**Google Messages (RCS)**](https://www.android.com/google-messages/) | Google, avec les opérateurs mobiles | Oui, par défaut entre utilisateurs de Google Messages. Avec les iPhone, le chiffrement a commencé à être déployé en mai 2026, en bêta, et dépend de votre opérateur. | Lié à votre numéro de téléphone. Les métadonnées sont toujours collectées. Code fermé. Retombe sur du SMS ordinaire quand le RCS n'est pas disponible. | Mieux que le SMS. Vérifiez la présence de l'icône de cadenas. |

Voici de meilleures options. Il n'existe pas de bonne réponse unique, ce qui est sain, car un monde où tout le monde dépend d'1 seule application est fragile. Les 7 chiffrent vos conversations privées de bout en bout par défaut, et leurs applications sont open source.

| Messagerie | Numéro de téléphone requis | Qui exploite le réseau | Qui garantit les clés | Idéal pour |
|---|---|---|---|---|
| [**Signal**](https://signal.org/) | Oui (peut être masqué aux autres) | 1 seule fondation à but non lucratif | Un annuaire géré par Signal. Vérification facultative avec un numéro de sécurité de 60 chiffres. | Remplacer WhatsApp avec la famille et les amis. Le changement le plus facile. |
| [**SimpleX Chat**](https://simplex.chat/) | Aucun identifiant du tout | Des relais que n'importe qui peut exploiter | Personne. Vous remettez vous-même un lien ou un QR code, avec un code de sécurité facultatif à comparer. | Forte protection des métadonnées. Pas de compte, pas de nom d'utilisateur, aucun identifiant à relier. |
| [**Session**](https://getsession.org/) | Non | Un réseau décentralisé de nœuds gérés par la communauté | Aucun annuaire, puisque votre identifiant Session est votre clé publique. Vous devez obtenir cet identifiant par un canal en lequel vous avez confiance. | Comptes anonymes, messages acheminés par plusieurs nœuds. Plus lent, moins de fonctions. Son protocole actuel n'offre pas la confidentialité persistante (forward secrecy), c'est-à-dire qu'une clé volée un jour pourrait déverrouiller d'anciens messages. Une mise à niveau annoncée en décembre 2025 était [en suspens en août 2026](https://getsession.org/session-development-update-pro-beta-protocol-v2). |
| [**Threema**](https://threema.com/) | Non | 1 seule entreprise suisse, [détenue depuis janvier 2026](https://www.privacyguides.org/news/2026/01/16/another-private-equity-firm-acquires-threema/) par la société d'investissement allemande Comitis Capital. Application payante | Un annuaire géré par Threema. Scanner en personne le QR code d'un contact le fait passer au niveau de confiance le plus élevé. | Les personnes qui ne veulent pas de numéro de téléphone et souhaitent un produit soigné et payant. |
| [**Olvid**](https://olvid.io/) | Non, et ni email ni autre donnée personnelle | 1 seule entreprise française, avec des serveurs hébergés sur Amazon Web Services | Personne. Les 2 personnes échangent 2 codes de 4 chiffres avant le premier message, et cette étape est obligatoire. | Une application européenne dont la sécurité est certifiée par l'ANSSI, l'agence française de cybersécurité. Les messages et la réception d'appels sont gratuits. Passer des appels et utiliser plusieurs appareils nécessitent un abonnement (environ 5 euros par mois). |
| [**Element (Matrix)**](https://element.io/) | Non | Fédéré, avec de nombreux serveurs, ou le vôtre | L'annuaire de votre serveur. Vérification facultative par comparaison d'émojis ou scan d'un QR code. | Communautés, équipes, personnes qui veulent héberger leur propre serveur. Les serveurs concernés voient des métadonnées (qui se trouve dans quel salon, et quand), donc le choix du serveur compte. |
| [**Briar**](https://briarproject.org/) | Non | Personne, d'appareil à appareil | Personne. Les contacts sont ajoutés par QR code en personne, ou par échange de liens. | Situations extrêmes. Fonctionne via Tor, et même par Bluetooth ou Wi-Fi sans internet. Android, plus une version pour ordinateur en bêta (Windows, macOS, Linux). Pas d'application iPhone. |

Une configuration raisonnable pour la plupart des gens est **Signal pour le quotidien**, plus **une messagerie sans numéro de téléphone** (SimpleX ou Olvid, par exemple) pour les contacts que vous ne voulez pas relier à votre identité.

Si une partie de votre entourage reste sur WhatsApp, aidez-la au moins à activer les sauvegardes chiffrées (Paramètres (Settings), Discussions (Chats), Sauvegarde des discussions (Chat backup), Sauvegarde chiffrée de bout en bout (End-to-end encrypted backup)). WhatsApp l'explique dans son centre d'aide, sous [About end-to-end encrypted backup](https://faq.whatsapp.com/490592613091019).

## Pas à pas {#step-by-step}

L'exemple utilise Signal, car c'est le premier pas le plus courant, et la même logique s'applique aux autres. Les noms de menus sont ceux de septembre 2026.

1. **Installez-la** depuis la boutique officielle ou depuis le site du projet, puis inscrivez-vous.
2. **Verrouillez votre compte.** Dans Paramètres (Settings), Compte (Account), définissez un code PIN et activez le verrouillage de l'inscription (Registration Lock), afin que la réinscription de votre numéro exige ce PIN. Enregistrez ce PIN dans votre gestionnaire de mots de passe (chapitre 2).
3. **Masquez votre numéro.** Créez un nom d'utilisateur, puis dans Paramètres, Confidentialité (Privacy), Numéro de téléphone (Phone Number), réglez « Qui peut voir mon numéro » (Who can see my number) sur Personne (Nobody). Vous pouvez désormais donner votre nom d'utilisateur à la place de votre numéro. Le réglage distinct « Qui peut me trouver grâce à mon numéro » (Who can find me by number) détermine si une personne qui possède déjà votre numéro peut vous trouver sur Signal. Réglez-le aussi sur Personne si vous le préférez, en sachant que vos amis auront alors besoin de votre nom d'utilisateur.
4. **Faites disparaître les messages par défaut.** Dans Paramètres, Confidentialité, Messages éphémères (Disappearing messages), choisissez une durée par défaut, par exemple 4 semaines. Cela réduit l'historique conservé sur votre téléphone. Cela ne peut pas supprimer les captures d'écran, les exports ou les copies faites par le destinataire.
5. **Verrouillez l'application** avec Paramètres, Confidentialité, Verrouillage de l'écran (Screen lock).
6. **Activez les sauvegardes.** Sans sauvegarde, un téléphone perdu ou cassé signifie un historique perdu. Dans Paramètres, ouvrez Sauvegardes (Backups) et activez la [sauvegarde chiffrée de bout en bout](https://support.signal.org/hc/en-us/articles/9708267671322-Signal-Secure-Backup) de Signal. Elle est gratuite pour vos messages texte et les médias des 45 derniers jours. Signal affiche ensuite une clé de récupération de 64 caractères. Notez-la sur papier ou enregistrez-la dans votre gestionnaire de mots de passe, car Signal ne peut pas la récupérer, et sans elle la sauvegarde ne peut pas être restaurée.
7. **Vérifiez vos contacts importants.** Ouvrez la conversation, touchez le nom, puis Afficher le numéro de sécurité (View safety number), et comparez-le en personne ou par un autre canal en lequel vous avez déjà confiance, comme un appel vers un numéro dont vous savez déjà qu'il est le sien. Une voix familière ne suffit pas à elle seule. C'est l'étape qui vous apporte l'authenticité et qui vous évite de dépendre de l'annuaire de Signal. Faites-la donc 1 fois avec les quelques personnes qui comptent le plus.
8. **Déplacez vos proches** sans annoncer une révolution. Écrivez à vos 5 contacts les plus proches depuis la nouvelle application, créez-y le groupe familial, et laissez l'ancienne application s'éteindre peu à peu.

## Erreurs à éviter {#mistakes-to-avoid}

- **Croire que « chiffré » veut dire « privé ».** Le chiffrement protège le contenu, mais il ne cache pas avec qui vous parlez, sauf si la messagerie a été conçue pour cela.
- **Oublier le téléphone lui-même.** Quiconque tient votre téléphone déverrouillé peut tout lire, ce qui fait d'un verrouillage d'écran solide une partie de la sécurité de votre messagerie.
- **Laisser activées des sauvegardes cloud non chiffrées.** Une sauvegarde non chiffrée conserve une copie lisible de conversations qui étaient chiffrées pendant leur transport. Vérifiez vos réglages, et rappelez-vous que la sauvegarde de l'autre personne compte aussi.
- **Attendre que tout le monde change.** Une partie de votre entourage restera où elle est, et avoir 2 applications côte à côte est un résultat parfaitement correct.
- **Confondre vie privée et anonymat.** Une messagerie liée à votre numéro de téléphone protège ce que vous dites, pas qui vous êtes. Si vous devez rester non identifié, utilisez une messagerie sans numéro de téléphone.
- **Faire plus confiance à l'application qu'à la personne.** Les captures d'écran existent, et le point le plus faible d'une conversation est souvent l'autre extrémité.

## Pour aller plus loin {#go-further}

- **Comparer les messageries en détail :** Privacy Guides, « Real-Time Communication » (privacyguides.org).
- **Comprendre vos propres risques :** Surveillance Self-Defense, par l'Electronic Frontier Foundation (ssd.eff.org).
- **Chapitre suivant :** vos mots de passe et vos comptes.

## Sources {#sources}

- [Set and manage disappearing messages](https://support.signal.org/hc/en-us/articles/360007320771-Set-and-manage-disappearing-messages), Signal Support, consulté le 22 octobre 2026.
- [Scammers use fake emergencies to steal your money](https://consumer.ftc.gov/articles/scammers-use-fake-emergencies-steal-your-money), Federal Trade Commission, consulté le 22 octobre 2026.
- [Proposal for a regulation laying down rules to prevent and combat child sexual abuse, COM(2022) 209](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:52022PC0209), Commission européenne, 11 mai 2022.
- [Legislative train: combating child sexual abuse online](https://www.europarl.europa.eu/legislative-train/theme-promoting-our-european-way-of-life/file-combating-child-sexual-abuse-online), Parlement européen, mis à jour le 20 septembre 2026, consulté le 29 octobre 2026.
- [Outcome of the 6th trilogue on 29 September 2026 and way forward (WK 15082/2026)](https://data.consilium.europa.eu/doc/document/WK-15082-2026-INIT/en/pdf), Conseil de l'UE, 30 septembre 2026.
- [Combating child sexual abuse online: support for more limited ePrivacy derogation](https://www.europarl.europa.eu/news/en/press-room/20260706IPR46318/combating-child-sexual-abuse-support-for-a-more-limited-eprivacy-derogation), Parlement européen, 9 juillet 2026.
- [Fighting child sexual abuse online: interim measure protecting children now reinstated](https://www.consilium.europa.eu/en/press/press-releases/2026/07/23/fighting-child-sexual-abuse-online-interim-measure-protecting-children-now-reinstated/), Conseil de l'UE, 23 juillet 2026.
- [Mobile Communications Best Practice Guidance](https://www.cisa.gov/resources-tools/resources/mobile-communications-best-practice-guidance), CISA, 18 décembre 2024.
- [What is a safety number and why do I see that it changed?](https://support.signal.org/hc/en-us/articles/360007060632-What-is-a-safety-number-and-why-do-I-see-that-it-changed), Signal Support, consulté en septembre 2026.
- [Deploying key transparency at WhatsApp](https://engineering.fb.com/2023/04/13/security/whatsapp-key-transparency/), Engineering at Meta, 13 avril 2023.
- [Advancing iMessage security: iMessage Contact Key Verification](https://security.apple.com/blog/imessage-contact-key-verification/), Apple Security Research, 2023.
- [Olvid secure channels](https://olvid.io/faq/olvid-secure-channels/), Olvid, consulté en septembre 2026.
- [What are Signal Secure Backups?](https://support.signal.org/hc/en-us/articles/9708267671322-Signal-Secure-Backup), Signal Support, consulté le 29 octobre 2026.
- [Session Development Update: Pro Beta and Protocol v2](https://getsession.org/session-development-update-pro-beta-protocol-v2), Session, 2 août 2026, consulté le 29 octobre 2026.
- [Another private equity firm acquires Threema](https://www.privacyguides.org/news/2026/01/16/another-private-equity-firm-acquires-threema/), Privacy Guides, janvier 2026, consulté le 29 octobre 2026.

## Votre checklist {#your-checklist}

- [ ] Installez une messagerie privée, verrouillez-la avec un PIN, masquez votre numéro et activez les messages éphémères (5 min)
- [ ] Déplacez vos 5 contacts les plus proches et votre groupe familial (1 h)
- [ ] Vérifiez le numéro de sécurité de vos 3 contacts les plus importants (5 min)
- [ ] Installez une seconde messagerie qui ne nécessite aucun numéro de téléphone (5 min)
- [ ] Activez les sauvegardes chiffrées dans les applications que vous conservez (5 min)
