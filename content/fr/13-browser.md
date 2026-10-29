# Chapitre 3 : Votre navigateur et vos recherches

## En bref {#in-brief}

Votre navigateur et votre moteur de recherche voient davantage de votre vie que n'importe quel autre logiciel, et ceux de votre appareil ont été choisis pour vous par un accord commercial. Passez à un navigateur qui bloque le pistage, ajoutez 1 seul bon bloqueur de contenu, et choisissez un moteur de recherche qui ne construit pas de profil sur vous. Cela prend moins d'1 heure, et la différence se voit tout de suite, avec moins de publicités et des pages plus rapides.

## Un réglage par défaut payé par quelqu'un d'autre

Vous lisez l'actualité, cherchez des symptômes et comparez des prêts dans votre navigateur, et la plupart des pages que vous ouvrez chargent aussi du code invisible provenant de dizaines d'autres entreprises, comme des régies publicitaires et des services d'analyse. Ces **traceurs** (trackers) notent ce que vous lisez et l'ajoutent à un profil construit sur des années. Vos recherches en révèlent encore plus, puisque vous demandez à un moteur de recherche des choses que vous ne demanderiez ni à votre médecin ni à votre partenaire.

Pourtant, les réglages par défaut de votre appareil n'ont pas été choisis par vous. Une diapositive rendue publique lors du procès antitrust américain contre Google a montré que l'entreprise [avait payé 26,3 milliards de dollars en 2021](https://www.cnbc.com/2023/10/27/google-paid-26-billion-in-2021-to-become-a-default-search-engine.html) pour être le moteur de recherche par défaut, Apple en étant probablement le principal bénéficiaire et des éditeurs de navigateurs comme Mozilla figurant parmi les autres. En septembre 2025, un juge fédéral américain [a mis fin aux contrats d'exclusivité mais a laissé Google continuer à payer pour son placement](https://www.npr.org/2025/09/02/nx-s1-5478625/google-chrome-doj-antitrust-ruling). En septembre 2026, le réglage par défaut de votre appareil reste donc, dans la plupart des cas, le résultat d'un paiement.

Le mode privé ou navigation privée ne résout pas ce problème, car il empêche seulement votre propre appareil de conserver l'historique et les cookies. Les sites web, les traceurs, votre fournisseur d'accès à internet et le réseau de votre employeur voient la même chose qu'avant.

## 3 façons dont les traceurs vous reconnaissent

Les traceurs s'appuient sur 3 techniques principales.

- **Cookies tiers.** Un cookie est un petit fichier qu'un site stocke dans votre navigateur. Quand la même entreprise publicitaire est présente sur des milliers de sites, son cookie vous suit de l'un à l'autre. Safari, Firefox et Brave bloquent ou isolent ces cookies par défaut. Chrome, le navigateur le plus utilisé, les autorise encore, et en avril 2025 Google [a confirmé qu'il conservait cette approche](https://privacysandbox.google.com/blog/privacy-sandbox-next-steps) après des années d'annonces de leur suppression.
- **Prise d'empreinte numérique (fingerprinting).** Votre navigateur révèle de nombreux petits détails, comme la taille de l'écran, la langue, le fuseau horaire, les polices installées et le matériel graphique. Chacun est banal, mais combinés ils sont souvent uniques à vous. Rien n'est stocké sur votre appareil, donc effacer les cookies ne change rien.
- **Vos comptes.** Si vous restez connecté à Google ou à Facebook, chaque page qui contient leur code peut être reliée à votre vrai nom.

Les défenses suivent la même logique.

- **Bloquer.** Un bloqueur de contenu refuse tout simplement de charger les traceurs connus.
- **Isoler.** Le navigateur donne à chaque site son propre stockage de cookies séparé, de sorte qu'un cookie déposé sur un site donné n'est pas lisible sur le suivant.
- **Ressembler à tout le monde.** Certains navigateurs cherchent à faire apparaître tous leurs utilisateurs de manière identique, de sorte qu'une empreinte désigne une foule plutôt qu'une personne.

Votre adresse IP vous identifie aussi, ce qui est le sujet du chapitre 5.

## Qui garantit le cadenas

Le cadenas promet que personne sur le chemin ne peut lire la page (confidentialité) et que le site est bien celui qui figure dans l'adresse (authenticité). La seconde promesse vient d'une **autorité de certification**, une organisation qui signe un certificat pour le site, et votre navigateur ou votre système est livré avec une liste des autorités qu'il accepte. N'importe laquelle d'entre elles peut se porter garante de n'importe quel site, ce qui en fait les tiers de confiance classiques du web. En 2011, un intrus au sein de l'autorité néerlandaise DigiNotar [a émis 531 faux certificats](https://www.enisa.europa.eu/sites/default/files/all_files/Operation_Black_Tulip_v2.pdf), et celui de google.com a servi à intercepter environ 300 000 utilisateurs, presque tous en Iran, avant que [les navigateurs retirent DigiNotar de leurs listes](https://blog.mozilla.org/security/2011/09/02/diginotar-removal-follow-up/).

La **transparence des certificats** est née de cet échec. Les certificats doivent désormais apparaître dans des journaux publics que tout le monde peut consulter, ce qui permet au propriétaire d'un site de repérer un faux, et [Firefox refuse les certificats non journalisés sur ordinateur depuis la version 135](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/OagRKpVirsA/m/Q4c89XG-EAAJ), en février 2025, comme le faisaient déjà Chrome et Safari.

L'éditeur du navigateur est l'autre tiers, car il choisit cette liste, le moteur de recherche par défaut et la boutique d'extensions, et son canal de mise à jour peut modifier le programme que vous exécutez. L'open source et les builds reproductibles permettent à des tiers de vérifier ce qu'il livre.

## Choisir votre navigateur

Aucun navigateur n'est parfait. Regardez donc qui le construit, ce qu'il bloque sans réglage et ce à quoi vous renoncez.

| Navigateur | Qui est derrière | En qui vous devez avoir confiance | Points forts | Compromis |
|---|---|---|---|---|
| **Firefox** | Mozilla, détenue par une fondation à but non lucratif | Mozilla, pour les mises à jour, sa propre liste d'autorités de certification et sa boutique de modules complémentaires. Code public. | Son propre moteur, indépendant de Chromium de Google. Forte protection en mode Strict. Exécute uBlock Origin complet sur ordinateur et sur Android. | Quelques réglages à modifier d'abord. Envoie des données d'utilisation par défaut. L'essentiel des revenus de Mozilla provient de son accord de recherche avec Google. Sur iPhone, il ne peut pas installer d'extensions. |
| **Brave** | Brave Software, une entreprise américaine à but lucratif | Brave Software pour les mises à jour, Google pour le code Chromium sous-jacent et la boutique d'extensions. Code public. | Bloque publicités et traceurs sans réglage, sur iPhone aussi. Fonctionne avec presque tous les sites. Ordinateur et téléphone. | Promeut ses propres produits, dont un wallet (portefeuille) crypto, des publicités avec récompenses et un VPN payant. Vous pouvez les désactiver. Construit sur le moteur Chromium de Google. |
| **Mullvad Browser** | Conçu par le Tor Project avec Mullvad, une entreprise suédoise de VPN | Le Tor Project et Mullvad, pour les mises à jour. Code public, avec des builds reproductibles que des tiers peuvent vérifier. | Forte protection contre la prise d'empreinte, conçue pour que tous les utilisateurs se ressemblent. Aucune donnée d'utilisation envoyée. Gratuit, aucun VPN requis. | Ordinateur uniquement. Oublie tout à la fermeture. Certains sites ne fonctionnent plus. |
| **LibreWolf** | Une communauté de bénévoles | Quelques bénévoles, pour les builds et pour la rapidité d'arrivée des correctifs de sécurité de Firefox. Code public. | Firefox avec des réglages stricts déjà appliqués, sans données d'utilisation, uBlock Origin inclus. | Ordinateur uniquement. Petite équipe. Sur certains systèmes, vous gérez vous-même les mises à jour. |
| **Tor Browser** | Le Tor Project, une organisation à but non lucratif | Le Tor Project pour les mises à jour (builds reproductibles). Aucun relais ne voit à la fois vous et le site. | Masque votre adresse IP en passant par 3 relais. L'anonymat le plus fort de ce tableau. | Lent. De nombreux sites affichent des vérifications supplémentaires ou le bloquent. Pas conçu pour vos comptes connectés du quotidien. |

Pour le blocage, la référence est **uBlock Origin**, gratuit, open source et sans exceptions payantes pour les annonceurs. Il fonctionne pleinement dans Firefox sur ordinateur et sur Android. Chrome ne l'exécute plus, car Google [a désactivé l'ancien format d'extensions en juillet 2025](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline) et a retiré les dernières extensions de ce type du Chrome Web Store le 31 août 2026. Il reste une version plus limitée, uBlock Origin Lite, tandis que Brave intègre son propre bloqueur.

L'iPhone est un cas à part, car [Firefox pour iOS ne peut pas installer d'extensions](https://support.mozilla.org/en-US/kb/add-ons-firefox-ios), donc uBlock Origin n'y est pas disponible. Les options sont le bloqueur intégré de Brave, le bloqueur de publicités plus simple que [Firefox propose sur iOS](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios) (désactivé par défaut et déployé progressivement), ou Safari avec uBlock Origin Lite, disponible depuis août 2025.

Résistez à l'envie d'en installer davantage, car chaque extension peut lire les pages que vous visitez, et un ensemble inhabituel rend votre empreinte plus unique.

Une configuration raisonnable pour la plupart des gens est **Firefox ou Brave pour le quotidien**, plus **Mullvad Browser ou Tor Browser** pour les recherches que vous préférez garder séparées de vos comptes.

## Choisir votre moteur de recherche

Changer de moteur de recherche prend environ 1 minute, ce qui en fait l'une des étapes les plus faciles de ce livre. D'après leurs propres politiques, aucune des options ci-dessous ne construit de profil publicitaire sur vous, mais elles diffèrent par l'origine de leurs résultats et par leur manière de gagner de l'argent.

| Moteur de recherche | Origine des résultats | Comment il gagne de l'argent | Bon à savoir |
|---|---|---|---|
| **DuckDuckGo** | Surtout Bing, plus ses propres sources | Publicités fondées sur les mots que vous saisissez, pas sur un profil | Entreprise américaine. Le changement le plus facile. |
| **Brave Search** | Son propre index indépendant | Publicités | Même entreprise que le navigateur Brave. |
| **Startpage** | Résultats de Google, demandés sans votre identité | Publicités non personnalisées | Entreprise néerlandaise. Depuis 2019, son actionnaire majoritaire est System1, un groupe publicitaire américain. |
| **Kagi** | Son propre index plus plusieurs autres sources | Abonnement payant, sans publicité | Entreprise américaine. Nécessite un compte. Financée uniquement par ses utilisateurs. |
| **SearXNG** | Combine de nombreux moteurs à la fois | Rien. C'est un logiciel libre gratuit | Hébergez-le vous-même ou utilisez une instance publique (liste sur searx.space). Vous faites alors confiance à celui qui exploite cette instance. |

Essayez-en un pendant 2 semaines avant de juger. Les résultats des recherches locales, dans votre pays et dans votre langue, peuvent varier d'un moteur à l'autre, et rien ne vous empêche d'utiliser un second moteur pour la requête difficile occasionnelle.

## Pas à pas {#step-by-step}

L'exemple utilise Firefox sur ordinateur, car il existe sur tous les systèmes et il est indépendant du moteur de Google. La même logique s'applique aux autres, et les noms des réglages peuvent légèrement changer d'une version à l'autre.

1. **Installez-le** depuis firefox.com ou depuis la boutique officielle de votre système.
2. **Renforcez la protection.** Dans Paramètres (Settings), Vie privée et sécurité (Privacy & Security), réglez la protection renforcée contre le pistage (Enhanced Tracking Protection) sur Stricte (Strict).
3. **Forcez les connexions chiffrées.** Sur la même page, activez le mode HTTPS uniquement (HTTPS-Only Mode) dans toutes les fenêtres. Le navigateur vous avertit alors avant toute page non chiffrée, si bien que les réseaux intermédiaires ne peuvent pas dégrader discrètement une connexion. Vous vous fiez toujours aux autorités de certification décrites plus haut.
4. **Cessez d'envoyer des données d'utilisation.** Toujours sur la même page, dans la section sur la collecte de données par Firefox, décochez les cases.
5. **Changez de moteur de recherche.** Dans Paramètres, Recherche (Search), choisissez votre nouveau moteur par défaut. S'il ne figure pas dans la liste, visitez le site du moteur de recherche et ajoutez-le depuis la barre d'adresse.
6. **Installez uBlock Origin** depuis le site officiel des modules complémentaires (addons.mozilla.org), et conservez ses réglages par défaut, qui sont bons.
7. **Récupérez vos marque-pages.** Utilisez l'outil d'import du menu des marque-pages pour copier les marque-pages de votre ancien navigateur. N'importez pas les mots de passe enregistrés, car ils ont leur place dans votre gestionnaire de mots de passe (chapitre 2).
8. **Faites-en le navigateur par défaut, sur votre téléphone aussi.** Définissez le nouveau navigateur par défaut sur votre ordinateur, puis répétez les mêmes choix sur votre téléphone. Sur Android, Firefox accepte aussi uBlock Origin. Sur iPhone, ce n'est pas le cas, utilisez donc l'une des options pour iPhone décrites plus haut.

## Erreurs à éviter {#mistakes-to-avoid}

- **Croire que le mode privé vous rend invisible.** Il cache votre navigation aux personnes qui partagent votre appareil, et à personne d'autre.
- **Installer 10 extensions de confidentialité.** Chacune peut lire vos pages, et ensemble elles vous font ressortir, donc 1 seul bon bloqueur de contenu suffit.
- **Rester connecté à Google ou à Facebook toute la journée dans votre navigateur principal.** Garder ces comptes dans un second navigateur empêche leurs cookies de suivre votre navigation quotidienne, ce qui affaiblit le lien entre votre nom et ce que vous lisez. Cela ne supprime pas ce lien, car votre adresse IP et votre empreinte restent visibles des sites que vous visitez.
- **Cliquer sur « Tout accepter » par habitude.** Cherchez « Tout refuser ». uBlock Origin peut aussi masquer la plupart des bandeaux de cookies si vous activez les listes de bandeaux de cookies dans ses réglages.
- **Pousser tous les réglages au maximum.** Si la moitié de vos sites ne fonctionnent plus, vous risquez de revenir à l'ancien navigateur en moins d'1 semaine. Montez donc les réglages progressivement et gardez le niveau avec lequel vous pouvez vivre.
- **Ignorer les mises à jour.** Le navigateur est le programme le plus exposé à internet, redémarrez-le donc quand il le demande.

## Pour aller plus loin {#go-further}

- **Tester votre navigateur :** Cover Your Tracks, par l'Electronic Frontier Foundation (coveryourtracks.eff.org), montre à quel point votre empreinte est unique.
- **Comparer en détail :** Privacy Guides, « Desktop Browsers » et « Search Engines » (privacyguides.org).
- **Chapitre suivant :** votre email et vos alias.

## Sources {#sources}

- [Operation Black Tulip: certificate authorities lose authority](https://www.enisa.europa.eu/sites/default/files/all_files/Operation_Black_Tulip_v2.pdf), ENISA (Agence de l'Union européenne pour la cybersécurité), décembre 2011.
- [DigiNotar removal follow up](https://blog.mozilla.org/security/2011/09/02/diginotar-removal-follow-up/), Mozilla Security Blog, 2 septembre 2011.
- [Certificate Transparency is now enforced in Firefox on desktop platforms starting with version 135](https://groups.google.com/a/mozilla.org/g/dev-security-policy/c/OagRKpVirsA/m/Q4c89XG-EAAJ), liste Mozilla dev-security-policy, 4 février 2025.
- [Google paid $26 billion in 2021 to become a default search engine](https://www.cnbc.com/2023/10/27/google-paid-26-billion-in-2021-to-become-a-default-search-engine.html), CNBC, 27 octobre 2023.
- [In a major antitrust ruling, a judge lets Google keep Chrome but levies other penalties](https://www.npr.org/2025/09/02/nx-s1-5478625/google-chrome-doj-antitrust-ruling), NPR, 2 septembre 2025.
- [Next steps for Privacy Sandbox and tracking protections in Chrome](https://privacysandbox.google.com/blog/privacy-sandbox-next-steps), Google, 22 avril 2025.
- [Manifest V2 support timeline](https://developer.chrome.com/docs/extensions/develop/migrate/mv2-deprecation-timeline), Chrome for Developers (Google), mis à jour en septembre 2026.
- [Add-ons in Firefox for iOS](https://support.mozilla.org/en-US/kb/add-ons-firefox-ios), Mozilla Support, consulté en septembre 2026.
- [Block ads in Firefox for iOS](https://support.mozilla.org/en-US/kb/block-ads-firefox-ios), Mozilla Support, consulté le 22 octobre 2026.

## Votre checklist {#your-checklist}

- [ ] Changez le moteur de recherche par défaut sur votre ordinateur et votre téléphone (5 min)
- [ ] Installez un navigateur qui bloque le pistage et faites-en votre navigateur par défaut (1 h)
- [ ] Ajoutez uBlock Origin là où c'est possible, ou utilisez le bloqueur de votre navigateur, et supprimez les extensions inutilisées (5 min)
- [ ] Déplacez vos sessions Google et Facebook vers un second navigateur (5 min)
- [ ] Testez votre navigateur sur coveryourtracks.eff.org (5 min)
