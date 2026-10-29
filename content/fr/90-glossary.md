# Glossaire

Les mots qui reviennent tout au long de ce livre, en langage simple.

## Vie privée

**Chiffrement.** Brouiller l'information pour que seule une personne détenant la bonne clé puisse la lire.

**Chiffrement de bout en bout.** Chiffrement où seuls vous et la personne à qui vous parlez détenez les clés. Le service au milieu transporte le message mais ne peut pas le lire.

**Confidentialité.** Personne, hormis les 2 personnes qui se parlent, ne peut lire le message.

**Authenticité.** La garantie que la personne à l'autre bout est bien celle que vous croyez, et que le message n'a pas été modifié en chemin. Le chiffrement seul ne la donne pas.

**Tiers de confiance.** Un intermédiaire dont l'honnêteté conditionne tout le système. Une messagerie qui distribue les clés de ses utilisateurs depuis son propre annuaire en est un, même lorsqu'elle chiffre de bout en bout.

**Confidentialité persistante (forward secrecy).** Une conception où une clé volée un jour ne peut pas déverrouiller les messages échangés avant.

**Métadonnées.** Pas ce que vous dites, mais à qui vous parlez, quand, d'où et à quelle fréquence. Souvent plus révélatrices que le contenu lui-même.

**Open source.** Logiciel dont le code source est public, avec une licence qui permet de l'utiliser, de le modifier et de le redistribuer. Un code public ne suffit pas à lui seul, comme l'expliquent les chapitres 10 et 11.

**Traqueur (tracker).** Un morceau de code dans un site ou une application qui signale ce que vous faites à un tiers, généralement une société de publicité.

**Empreinte numérique (fingerprinting).** Reconnaître votre navigateur ou votre appareil à partir de ses détails techniques (écran, polices, paramètres), même sans cookies.

**Gestionnaire de mots de passe.** Un coffre chiffré qui crée et mémorise un mot de passe fort différent pour chaque site. Vous ne retenez que le mot de passe du coffre.

**Authentification à 2 facteurs (2FA).** Une seconde preuve en plus de votre mot de passe, comme un code issu d'une application, ou une clé physique.

**SIM swap (échange de carte SIM).** Une fraude où quelqu'un convainc votre opérateur de transférer votre numéro de téléphone vers sa carte SIM, puis reçoit vos codes SMS.

**Alias (e-mail).** Une adresse jetable qui redirige vers votre vraie boîte. 1 par service, pour qu'une fuite puisse être tracée et coupée.

**VPN.** Un service qui fait passer votre trafic par son propre serveur. Il cache votre activité à votre fournisseur d'accès à internet et votre adresse aux sites que vous visitez, mais il faut faire confiance à l'entreprise du VPN elle-même.

**Tor.** Un réseau qui fait passer votre trafic par plusieurs bénévoles indépendants, de sorte qu'aucun d'eux ne sache à la fois qui vous êtes et ce que vous visitez.

**Mixnet.** Un réseau qui, en plus d'acheminer le trafic par plusieurs sauts, le mélange et le retarde pour masquer les schémas temporels.

**Modèle de menace (threat model).** La réponse honnête à la question « de qui est-ce que je veux me protéger ? ». Il détermine jusqu'où vous devez aller.

## Autonomie

**Clé privée.** Un long nombre secret que vous seul détenez. Elle prouve que vous êtes vous, et celui qui la détient contrôle l'identité ou l'argent qui est derrière.

**Clé publique.** Le nombre correspondant que vous pouvez partager librement. Les autres l'utilisent pour vérifier votre signature ou pour vous écrire.

**Passkey.** Une paire de clés utilisée pour se connecter à un site web ou à une application. Le service conserve la moitié publique. La moitié privée reste dans un appareil, ou peut être synchronisée sous forme chiffrée par un fournisseur de passkeys. Une clé de sécurité matérielle la garde sur la clé elle-même.

**Décentralisé.** Géré par de nombreuses parties indépendantes, sans que personne puisse l'éteindre, le censurer ou changer les règles seul.

**Auto-hébergement (self-hosting).** Faire tourner un service sur une machine que vous contrôlez au lieu de le louer à une entreprise.

**Nostr.** Un protocole ouvert pour les réseaux sociaux. Votre identité est une paire de clés, et vos messages transitent par des relais que n'importe qui peut gérer.

**npub et nsec.** Votre clé publique (npub, votre identité publique) et votre clé secrète (nsec, ne la partagez jamais) sur Nostr.

**Relais (relay).** Un serveur simple qui stocke et retransmet les messages Nostr. Vous pouvez en utiliser plusieurs, et en changer à tout moment.

**Zap.** Un petit paiement Lightning envoyé à quelqu'un sur Nostr, comme pourboire ou comme remerciement.

## Argent et épargne

**Inflation.** La hausse des prix dans le temps, ce qui revient à une perte de pouvoir d'achat de la monnaie. Les monnaies nationales sont conçues pour perdre un peu de valeur chaque année.

**Risque de contrepartie.** Le risque que celui qui détient un actif pour vous (une banque, un courtier, une plateforme d'échange) fasse défaut, ou refuse de vous le rendre.

**Self-custody (garde de vos propres clés).** Détenir un actif vous-même, sans intermédiaire, avec des pièces dans votre main ou des clés en votre possession. Aucune entreprise ne peut le geler, le prêter ou le perdre à votre place.

**Custodial.** Une entreprise détient l'actif pour vous. Pratique, mais ce que vous possédez est une promesse.

**Monero.** Une monnaie numérique au but proche de celui de Bitcoin, de l'argent que vous pouvez détenir vous-même, où les montants, les expéditeurs et les destinataires sont masqués par défaut. Utilisée par certains utilisateurs avancés comme complément privé de Bitcoin. Elle est beaucoup moins liquide et beaucoup moins acceptée, son réseau, beaucoup plus petit, est plus facile à attaquer pour une entité extérieure, comme l'ont montré les réorganisations de blocs de 2025, et son développement est plus centralisé (chapitre 12).

**KYC (« know your customer », connaître son client).** Contrôles d'identité obligatoires effectués par les sociétés financières. Ils relient votre nom à ce que vous possédez dans une base de données.

**MiCA.** Le règlement européen sur les services sur crypto-actifs, appliqué depuis le 30 décembre 2024. Les plateformes d'échange, les courtiers et les wallets custodial ont besoin d'une licence et doivent identifier leurs utilisateurs (chapitre 16).

**DAC8.** Une directive fiscale européenne, appliquée depuis le 1er janvier 2026. Les prestataires de services sur crypto-actifs déclarent aux autorités fiscales les transactions de leurs utilisateurs résidant dans l'UE (chapitre 16).

**CBDC.** Monnaie numérique de banque centrale (central bank digital currency), de la monnaie émise sous forme numérique par une banque centrale à destination du public. L'émetteur se trouve sur le chemin du paiement, de sorte que ce qu'il peut voir, limiter ou bloquer dépend de la conception du système et de la loi. L'euro numérique est une CBDC en projet (partie 3).

## Bitcoin

**Bitcoin.** Une monnaie numérique sans émetteur et à offre fixe de 21 millions. Les règles sont appliquées par des milliers d'ordinateurs indépendants.

**Sat (satoshi).** La plus petite unité de bitcoin. 1 bitcoin vaut 100 millions de sats.

**Wallet (portefeuille).** Une application ou un appareil qui détient vos clés et signe vos transactions. Il ne détient pas de pièces, car les pièces sont des entrées du registre partagé.

**Phrase de récupération (seed phrase).** Les mots de récupération des clés d'un wallet, généralement 12 ou 24 avec BIP39, mais il existe d'autres formats comme SLIP39 en 20 mots et les seeds natives d'Electrum. La récupération exige un logiciel compatible et toute passphrase supplémentaire. Les étiquettes, la configuration multisignature et l'état Lightning peuvent demander des sauvegardes séparées (chapitre 14).

**BIP39.** Le standard le plus courant pour les phrases de récupération, avec 12 ou 24 mots tirés d'une liste fixe de 2 048 mots anglais (chapitre 14).

**SLIP39.** Un standard de sauvegarde pris en charge par Trezor, généralement en 20 mots, qui peut aussi diviser une seed en parts, par exemple n'importe lesquelles 2 sur 3. Il n'est pas compatible avec BIP39 (chapitre 14).

**Passphrase.** Un mot ou une phrase supplémentaire facultatif ajouté à une phrase de récupération. Chaque passphrase ouvre un wallet différent, et une passphrase oubliée signifie des pièces perdues (chapitre 14).

**Multisignature (multisig).** Un wallet qui exige plusieurs clés indépendantes pour dépenser, par exemple 2 sur 3, conservées dans des lieux différents (chapitres 14 et 17).

**xpub et descripteur de sortie (output descriptor).** La description publique d'un wallet. La clé publique étendue (xpub) permet à un logiciel de trouver ses adresses, et le descripteur y ajoute les règles et, pour une multisignature, la xpub de chaque cosignataire. Ils ne permettent pas de dépenser, mais ils révèlent l'activité du wallet, et un wallet multisignature ne peut pas être restauré sans eux (chapitre 14).

**Hardware wallet (appareil de signature).** Un petit appareil dédié qui garde vos clés hors ligne et signe les transactions sans les exposer à votre ordinateur ou à votre téléphone.

**Air-gapped.** Se dit d'un appareil de signature qui ne se connecte jamais à un ordinateur. Les transactions voyagent par QR code ou carte mémoire (chapitre 17).

**Élément sécurisé (secure element).** Une puce conçue pour résister aux attaques physiques, utilisée dans de nombreux hardware wallets pour protéger les clés (chapitre 17).

**Build reproductible (reproducible build).** Un logiciel publié de sorte que n'importe qui puisse le reconstruire à partir du code source et obtenir exactement le même fichier. Il montre que ce que vous installez correspond au code publié (chapitres 13, 17 et 18).

**Lightning.** Un réseau de paiement construit au-dessus de Bitcoin, fait pour les montants du quotidien. Les paiements sont généralement instantanés et peu chers, même si certains wallets facturent des frais pour ouvrir le premier canal (chapitre 13).

**Canal de paiement.** 2 personnes verrouillent ensemble des bitcoins dans une transaction on-chain, puis déplacent le solde entre elles aussi souvent qu'elles le veulent sans toucher la blockchain. Lightning est un réseau de tels canaux (chapitre 15).

**Facture Lightning (invoice).** Une demande de paiement à usage unique, affichée sous la forme d'un QR code ou d'un texte, généralement pour un montant fixe et avec une date d'expiration (chapitre 15).

**Adresse Lightning.** Une adresse réutilisable qui ressemble à une adresse e-mail (you@provider.com), pratique pour les pourboires et pour être payé. La plupart reposent sur le serveur web d'un fournisseur (chapitre 15).

**Fournisseur de service Lightning (LSP).** Une entreprise qui ouvre des canaux pour un wallet Lightning en self-custody et relaie ses paiements, comme ACINQ pour Phoenix ou Blocktank pour Bitkit. Elle voit une partie de vos paiements et peut refuser de les relayer (chapitres 13 et 15).

**Swap.** Un échange entre 2 formes de bitcoin, par exemple on-chain et Lightning, ou Lightning et Liquid, généralement par un service extérieur (chapitre 13).

**Liquid.** Une sidechain (chaîne latérale) de Bitcoin gérée par une fédération d'entreprises, qui détiennent les bitcoins verrouillés sur la chaîne principale (chapitre 13).

**Spark.** Un système de paiements bitcoin off-chain rapides, dans lequel un petit groupe d'opérateurs cosigne chaque transfert. Les utilisateurs gardent leurs clés et une sortie vers la blockchain (chapitre 13).

**Ark.** Une manière de faire des paiements off-chain rapides et peu chers, dans laquelle de nombreux utilisateurs partagent des transactions on-chain via un serveur Ark. Un solde expire si le wallet ne le renouvelle pas à temps, et jusque-là vous pouvez sortir vers la blockchain sans le serveur (chapitre 13).

**On-chain.** Une transaction enregistrée directement dans le registre Bitcoin. Le délai de confirmation et les frais varient. Chaque nouvelle confirmation rend une annulation moins probable, mais il n'existe pas de caractère définitif absolu. Souvent adaptée aux montants plus importants.

**UTXO (pièce).** Un montant de bitcoin que vous avez reçu et pas encore dépensé. Un wallet en détient généralement plusieurs, comme des billets de valeurs différentes (chapitre 16).

**Monnaie rendue (change).** Ce qui vous revient, sur une nouvelle adresse à vous, quand vous payez avec une pièce plus grosse que le montant dû (chapitre 16).

**Contrôle des pièces (coin control).** Choisir vous-même quelles pièces paient une transaction, pour que des pièces de sources différentes ne soient pas reliées entre elles (chapitre 16).

**Coinjoin.** Une transaction construite ensemble par plusieurs personnes, avec de nombreuses entrées et sorties de mêmes montants, de sorte que la propriété des pièces est plus difficile à retracer (chapitre 16).

**Payjoin.** Un paiement dans lequel l'expéditeur et le destinataire ajoutent tous les 2 des pièces, ce qui brise l'hypothèse que toutes les entrées d'une transaction appartiennent à 1 personne (chapitre 16).

**Nœud.** Un ordinateur qui conserve sa propre copie du registre Bitcoin et vérifie chaque transaction au regard des règles.

**Nœud élagué (pruned node).** Un nœud qui vérifie tout l'historique mais ne conserve que les blocs récents, de sorte qu'il tient sur un petit disque (chapitre 18).

**Serveur Electrum.** Un logiciel qui indexe les données de votre nœud pour que des wallets comme Sparrow ou BlueWallet puissent l'interroger sur vos adresses (chapitre 18).

**Preuve de travail (proof of work).** L'énergie que les mineurs doivent dépenser pour ajouter un bloc. Elle rend l'historique des transactions extrêmement coûteux à réécrire.

**Pair à pair (peer-to-peer, P2P).** Directement entre 2 personnes, sans qu'aucune entreprise ne détienne les fonds au milieu.
