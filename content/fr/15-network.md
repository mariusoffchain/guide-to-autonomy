# Chapitre 5 : Votre réseau

## En bref {#in-brief}

Chaque connexion que vous établissez passe par des équipements qui appartiennent à quelqu'un d'autre, qu'il s'agisse de votre fournisseur d'accès à internet, du Wi-Fi d'un café ou du réseau du travail. HTTPS cache déjà ce que vous lisez et ce que vous saisissez, alors que les réseaux peuvent souvent encore identifier les sites que vous visitez. Un VPN cache cette liste à votre fournisseur et cache votre adresse IP aux sites web, en déplaçant votre confiance vers l'entreprise du VPN, et il ne vous rend pas anonyme. Tor et les mixnets vont plus loin, au prix de la vitesse.

## Chaque réseau sur le chemin peut observer

Entre votre appareil et un site web, votre trafic traverse plusieurs réseaux, et chacun d'eux peut l'observer sans qu'aucun pirate n'intervienne, car c'est le fonctionnement par défaut des réseaux.

- **Votre fournisseur d'accès à internet** voit chaque connexion que vous établissez depuis chez vous ou depuis votre téléphone, et dans de nombreux pays la loi lui impose d'en conserver des traces.
- **Le Wi-Fi public** d'un café, d'un hôtel ou d'un aéroport est géré par quelqu'un que vous ne connaissez pas, tout comme n'importe quel réseau portant le même nom monté par un inconnu.
- **Le réseau du travail ou de l'école** est souvent surveillé par principe.
- **Chaque site que vous visitez** voit votre adresse IP, le numéro qui identifie votre connexion. Elle révèle votre fournisseur et votre position approximative, et elle permet aux sites et aux annonceurs de vous reconnaître d'une visite à l'autre, même sans cookies.

Dans l'Union européenne, une directive de 2006 obligeait les fournisseurs à conserver les données de trafic et de localisation pendant une durée de 6 mois à 2 ans. La Cour de justice [l'a déclarée invalide le 8 avril 2014](https://curia.europa.eu/site/upload/docs/application/pdf/2014-04/cp140054en.pdf), en relevant que ces données « peuvent fournir des informations très précises sur la vie privée » des personnes concernées. Des règles nationales de conservation existent toujours dans plusieurs États membres.

## Le cadenas cache les pages, pas les destinations

**HTTPS**, le cadenas de votre navigateur, chiffre la liaison entre vous et le site, et presque tous les sites l'utilisent aujourd'hui. Les réseaux intermédiaires ne peuvent plus voir les pages que vous lisez, ce que vous saisissez ni vos mots de passe. Ils voient encore les adresses IP de destination, les horaires et les volumes de données, et souvent le nom de domaine (le site, pas la page exacte). Là où les 2 sont pris en charge, le DNS chiffré (voir plus bas) et Encrypted Client Hello, une fonction plus récente qui cache le nom du site à l'ouverture de la connexion, peuvent aussi cacher ce nom. Les adresses IP et les schémas de trafic peuvent tout de même révéler les destinations.

Le **DNS** est l'annuaire téléphonique d'internet. Avant que votre appareil puisse joindre signal.org, il doit demander à un serveur DNS quelle adresse IP se cache derrière ce nom. Par défaut, le serveur appartient à votre fournisseur d'accès à internet et la question circule souvent sans chiffrement, si bien que votre fournisseur détient la liste de tous les noms que vous avez demandés avant même que la page ne se charge.

Le **DNS chiffré** envoie ces questions par un canal chiffré vers un serveur que vous choisissez. Parmi les bonnes options gratuites figurent Quad9 (une organisation suisse à but non lucratif qui bloque aussi les sites malveillants connus), Mullvad DNS (aucun compte nécessaire, blocage de publicités facultatif) et NextDNS (une entreprise, très configurable, gratuite jusqu'à une limite mensuelle). C'est une petite étape utile, bien que le réseau voie toujours les adresses IP auxquelles vous vous connectez.

## Ce que fait un VPN, et ce qu'il ne fait pas

Un **VPN** construit un tunnel chiffré entre votre appareil et un serveur géré par l'entreprise du VPN, et tout votre trafic y passe, DNS compris. Votre fournisseur ou le Wi-Fi du café voit seulement que vous utilisez un VPN, et les sites web voient l'adresse du serveur du VPN.

L'entreprise du VPN voit désormais ce que voyait votre fournisseur, si bien qu'un VPN déplace votre confiance d'une entreprise que vous n'avez pas choisie vers une entreprise que vous avez choisie. Il ne vous rend pas non plus anonyme, puisque les cookies et la prise d'empreinte du navigateur (chapitre 3) fonctionnent toujours, et que Google ou Facebook savent qui vous êtes dès que vous vous connectez.

**Tor** supprime l'entreprise de confiance unique en faisant passer votre trafic par 3 relais gérés par des bénévoles indépendants. Le premier sait qui vous êtes mais pas où vous allez, le dernier sait l'inverse, et aucun relais ne voit les 2 extrémités. Un **mixnet** utilise aussi plusieurs sauts, mélange vos paquets à ceux d'autres utilisateurs, les retarde et ajoute de faux trafic de « couverture ». Cette conception vise à rendre beaucoup plus difficile, même pour un observateur de l'ensemble du réseau, d'associer ce qui entre à ce qui sort. Il est plus lent et moins éprouvé en pratique que Tor.

## Une promesse de non-conservation des journaux a besoin de preuves

Avec un VPN, la confidentialité de vos destinations repose sur 1 entreprise, qui pourrait enregistrer vos connexions, recevoir l'ordre de le faire ou être piratée. Une politique d'absence de journaux (no-logs) est une promesse, et 2 types de preuves l'appuient. Les audits sont le premier, comme l'[audit no-logs que Securitum réalise chaque année chez Proton VPN depuis 2022](https://protonvpn.com/blog/no-logs-audit), ou l'[audit de sécurité qu'IVPN commande chaque année à Cure53](https://www.ivpn.net/blog/annual-security-audit-scheduled-2026). Les affaires judiciaires sont le second. Le 18 avril 2023, la police suédoise [s'est présentée au bureau de Mullvad à Göteborg avec un mandat de perquisition](https://mullvad.net/en/blog/2023/4/20/mullvad-vpn-was-subject-to-a-search-warrant-customer-data-not-compromised) et, selon l'entreprise, est repartie sans données de clients, car il n'en existait pas. Ce sont 2 instantanés, et aucun ne montre ce qu'un serveur enregistre aujourd'hui.

Le **multi-hop**, proposé par plusieurs VPN, enchaîne 2 serveurs afin qu'un serveur compromis en apprenne moins, mais lorsque les 2 appartiennent à la même entreprise, la confiance n'a pas bougé. La décentraliser demande des opérateurs indépendants, comme avec les 3 relais bénévoles de Tor ou les serveurs exploités de façon indépendante de NymVPN. Décentralisé ne veut cependant pas dire vérifié, puisque personne n'audite chaque relais ou chaque opérateur, et la protection repose sur la faible probabilité qu'ils coopèrent. Vous faites toujours confiance à l'éditeur du logiciel, et vous payez en vitesse.

## Choisir votre protection réseau

Les applications de chacune des options ci-dessous sont open source, et chacune des 4 entreprises de VPN a publié au moins 1 audit de sécurité indépendant. Elles diffèrent par la personne en qui vous devez avoir confiance, par la vitesse et par les moyens de paiement. Les prix et les moyens de paiement ont été vérifiés sur les sites officiels en septembre 2026.

| Outil | Qui l'exploite | Qui voit votre trafic | Paiement | Compromis |
|---|---|---|---|---|
| **Mullvad VPN** | 1 seule entreprise, Suède | Mullvad voit votre adresse IP et vos destinations. Ses preuves sont une série d'audits et une perquisition policière en 2023 qui n'a rien saisi. | Prix forfaitaire de 5 euros par mois. Carte, PayPal, virement bancaire, espèces par courrier, bitcoin (Lightning inclus), monero | Aucun email nécessaire, le compte est un numéro aléatoire. Rapide, audité. Pas d'offre gratuite. |
| **IVPN** | 1 seule entreprise, Gibraltar | IVPN voit votre adresse IP et vos destinations. Ses preuves sont un audit no-logs en 2019, puis des audits de sécurité annuels. | Payant. Carte, PayPal, espèces, bitcoin (Lightning inclus), monero | Aucun email nécessaire. Audité chaque année, très transparent sur ses limites. Réseau de serveurs plus petit. |
| **Proton VPN** | 1 seule entreprise, Suisse | Proton voit votre adresse IP et vos destinations. Ses preuves sont un audit no-logs annuel par Securitum depuis 2022. | Offre gratuite sans limite de données sur 1 appareil, offres payantes. Carte, PayPal, virement bancaire, espèces, bitcoin (uniquement depuis un compte existant) | Audité. L'offre gratuite est honnête mais plus lente, avec peu de pays. Le compte nécessite une adresse email. |
| **NymVPN** | Nym, Suisse. Serveurs exploités par des opérateurs indépendants | L'opérateur d'entrée voit votre adresse IP, l'opérateur de sortie vos destinations. Nym publie l'application. Les opérateurs ne sont pas audités. | Payant. Carte, espèces par courrier, bitcoin (Lightning inclus), monero et d'autres cryptomonnaies | Aucun email nécessaire, le compte est une phrase de 24 mots. Audité en 2024. Un mode rapide à 2 sauts et un mode mixnet à 5 sauts beaucoup plus lent. Un produit plus jeune, avec moins d'historique. |
| **Tor Browser / Orbot** | Une organisation à but non lucratif et des milliers de relais bénévoles | Le relais d'entrée voit votre adresse IP, le relais de sortie vos destinations. Aucun relais ne voit les 2. Les relais ne sont pas audités. | Gratuit | La protection la plus forte de votre adresse IP pour la navigation. Lent, et certains sites le bloquent ou affichent d'interminables énigmes de vérification. Orbot envoie le trafic des applications du téléphone par Tor. |

Une configuration raisonnable pour la plupart des gens est **Mullvad, IVPN ou Proton VPN**, plus **Tor Browser** pour la navigation que vous voulez garder à l'écart de votre connexion et de vos comptes habituels. Tor cache votre adresse IP, mais il ne peut pas garantir l'anonymat. L'offre gratuite de Proton VPN est la seule offre gratuite qui échappe à l'avertissement ci-dessous.

Les applications de « VPN gratuit » méritent de la prudence, car faire tourner des serveurs coûte de l'argent et le trafic des utilisateurs qui ne paient pas devient souvent le produit, par la publicité, le pistage ou la revente de données. Les sites de classement des « meilleurs VPN » méritent la même prudence. La plupart touchent une commission pour chaque abonnement vendu, et certains appartiennent aux mêmes groupes que les VPN qu'ils classent. En mars 2021, Kape Technologies [a racheté Webselenese, l'éditeur des sites d'avis vpnMentor et Wizcase, pour 149,1 millions de dollars](https://en.globes.co.il/en/article-kape-acquires-israeli-co-webselenese-for-149m-1001363243), et vpnMentor [indique sur son propre site](https://www.vpnmentor.com/about-us/) que Kape possède aussi ExpressVPN, CyberGhost et Private Internet Access.

## Pas à pas {#step-by-step}

L'exemple utilise Mullvad, et la même logique s'applique aux autres.

1. **Installez l'application** depuis le site officiel du fournisseur ou depuis la boutique officielle, jamais depuis un lien dans une publicité.
2. **Créez le compte.** Mullvad vous donne un numéro de compte et ne demande rien d'autre. Rangez-le dans votre gestionnaire de mots de passe, puis ajoutez du temps avec le moyen de paiement que vous préférez.
3. **Connectez-vous.** Choisissez un serveur dans votre pays ou dans un pays voisin pour la meilleure vitesse. Un pays éloigné n'est utile que si vous avez besoin d'apparaître dans ce pays.
4. **Activez le kill switch (coupe-circuit).** Ce réglage bloque tout le trafic si le tunnel tombe, de sorte que rien ne sorte à côté. Dans Mullvad, il est toujours actif, et sur ordinateur un « mode verrouillage » (lockdown mode) supplémentaire bloque aussi internet quand vous vous déconnectez volontairement. Dans les autres applications, cherchez « kill switch » dans les paramètres. Sur Android, les paramètres VPN du système proposent aussi « VPN permanent » (Always-on VPN) et « Bloquer les connexions sans VPN » (Block connections without VPN).
5. **Connectez-vous automatiquement.** Dans les paramètres, activez le lancement au démarrage et la connexion automatique. Certaines applications, comme IVPN et Proton VPN, vous permettent de marquer votre Wi-Fi domestique comme de confiance et de vous connecter automatiquement sur tous les autres réseaux. Votre fournisseur d'accès à internet voit alors de nouveau vos destinations quand vous êtes chez vous. N'utilisez donc cette option que si les réseaux publics sont votre principale préoccupation.
6. **Réglez le DNS chiffré pour les moments sans VPN.** Sur Android, dans les paramètres réseau, trouvez « DNS privé » (Private DNS) et saisissez le nom d'hôte du service que vous avez choisi, par exemple dns.quad9.net. Sur iPhone et sur ordinateur, le service choisi vous fournit un profil ou une application à installer. Dans votre navigateur, activez le « DNS sécurisé » (secure DNS) dans les paramètres de confidentialité.
7. **Vérifiez l'absence de fuites.** Avec le VPN activé, ouvrez mullvad.net/check ou dnsleaktest.com. L'adresse IP affichée doit appartenir au VPN. Les serveurs DNS affichés appartiennent soit au VPN, soit, si l'étape 6 est active sur cet appareil ou ce navigateur, au service de DNS chiffré que vous avez choisi (Quad9, par exemple), dont les questions circulent alors à l'intérieur du tunnel. Les 2 résultats sont corrects. Il y a une fuite quand le nom de votre fournisseur d'accès à internet apparaît. Ce test vérifie ce qui sort de votre appareil. Aucun test de ce type ne montre ce qu'enregistrent les serveurs du VPN eux-mêmes.

## Erreurs à éviter {#mistakes-to-avoid}

- **Croire qu'un VPN vous rend anonyme.** Il cache votre adresse IP aux sites et votre trafic à votre fournisseur, tandis que les cookies, la prise d'empreinte et vos propres connexions continuent de vous identifier.
- **Choisir un VPN parce qu'il est gratuit ou parce qu'un site de classement l'a dit.** Cherchez des applications open source, des audits indépendants, un propriétaire clair et un modèle économique payant simple.
- **Laisser le kill switch désactivé.** Les tunnels tombent, surtout quand votre téléphone passe du Wi-Fi aux données mobiles, et sans kill switch votre trafic retourne silencieusement par la route normale.
- **Se connecter à des comptes personnels dans Tor Browser.** Dès que vous vous identifiez, le site sait qui vous êtes et les sauts supplémentaires ne vous cachent plus de lui.
- **Penser que le cadenas signifie que le site est honnête.** HTTPS protège la connexion, et un site d'hameçonnage peut avoir un cadenas lui aussi.
- **Oublier que les règles s'appliquent toujours.** Un VPN est un outil légal de protection de la vie privée dans l'Union européenne, et ce qui est illégal sans lui reste illégal avec lui. Certains pays hors de l'UE restreignent les VPN, vérifiez donc les règles locales avant de voyager.

## Pour aller plus loin {#go-further}

- **Comparer les VPN sans classements payants :** Privacy Guides, « VPN Services » et « DNS Resolvers » (privacyguides.org).
- **Comprendre et télécharger Tor :** le Tor Project (torproject.org). Il n'existe pas de Tor Browser officiel pour iPhone, où le Tor Project [recommande Onion Browser](https://support.torproject.org/tor-browser/getting-started/installing/#ios), avec des protections plus faibles que sur ordinateur.
- **Choisir un VPN adapté à votre situation :** Surveillance Self-Defense (ssd.eff.org).
- **Chapitre suivant :** la partie 2 commence, avec les clés à la place des comptes.

## Sources {#sources}

- [Firefox DNS over HTTPS, including ECH](https://support.mozilla.org/en-US/kb/firefox-dns-over-https), Mozilla Support, consulté le 22 octobre 2026.
- [Press release No 54/14: The Court of Justice declares the Data Retention Directive to be invalid](https://curia.europa.eu/site/upload/docs/application/pdf/2014-04/cp140054en.pdf), Cour de justice de l'Union européenne, 8 avril 2014.
- [Kape acquires Israeli co Webselenese for $149m](https://en.globes.co.il/en/article-kape-acquires-israeli-co-webselenese-for-149m-1001363243), Globes, 8 mars 2021.
- [About us (ownership disclosure)](https://www.vpnmentor.com/about-us/), vpnMentor, consulté en septembre 2026.
- [Proton VPN passes 5th annual external audit of no-logs policy](https://protonvpn.com/blog/no-logs-audit), Proton VPN, mis à jour le 16 juin 2026.
- [Mullvad VPN was subject to a search warrant. Customer data not compromised](https://mullvad.net/en/blog/2023/4/20/mullvad-vpn-was-subject-to-a-search-warrant-customer-data-not-compromised), Mullvad VPN, 20 avril 2023.
- [Annual security audit scheduled for 2026](https://www.ivpn.net/blog/annual-security-audit-scheduled-2026), IVPN, 19 juin 2026.
- [Nym response to Cure53 security audit](https://nym.com/trust-center/Cure53-security-audit-2024), Nym, juillet 2024.
- [Lightning payments](https://mullvad.net/en/blog/2025/8/5/lightning-payments), Mullvad VPN, 5 août 2025.
- [Installing Tor Browser (iOS section)](https://support.torproject.org/tor-browser/getting-started/installing/#ios), Tor Project, consulté en septembre 2026.

## Votre checklist {#your-checklist}

- [ ] Activez le DNS chiffré sur votre téléphone et dans votre navigateur (5 min)
- [ ] Choisissez et installez un VPN auprès d'un opérateur digne de confiance (1 h)
- [ ] Activez le kill switch et la connexion automatique, puis vérifiez l'absence de fuites (5 min)
- [ ] Installez Tor Browser et essayez-le 1 fois (5 min)
- [ ] Supprimez les applications de VPN dont l'opérateur ou les pratiques de confidentialité ne vous inspirent pas confiance (5 min)
