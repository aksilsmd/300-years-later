# 10 — Spécification fonctionnelle détaillée

> **EN —** What the system does, domain by domain, as numbered falsifiable requirements traced to the design dossier — never how it does it.

Propriétaire : Product Owner · v1.0 · 7 octobre 2026

**Ce document décrit *ce que* le système fait, jamais *comment*.** L'architecture, les modules, les
protocoles et les formats relèvent de [`40_TECHNICAL_DESIGN.md`](../design/40_TECHNICAL_DESIGN.md), qui reste
normatif. Aucune exigence ci-dessous n'ajoute de décision : chacune cite la section de `docs/design/` ou de
`data/` qui la porte.

**Conventions.** Les sources notées `NN_*.md §n` désignent `docs/design/NN_*.md` section *n* ;
`GDD §n` désigne `docs/design/GDD_CENTURY_TEMPS.md` ; `data/*` part de la racine du dépôt.
Priorités MoSCoW : **MUST** = non livrable sans ; **SHOULD** = prévu, sacrifiable selon l'ordre de coupe de
`50_PRODUCTION_PLAN.md` §6 ; **COULD** = confort ou après-lancement.
Une mention ***À trancher :*** signale un endroit où le dossier de conception est **réellement silencieux** :
l'exigence est alors un point ouvert renvoyé à [`docs/backlog.md`](../backlog.md), et n'est jamais complétée
par une invention.

Domaines : [LANCE](#1-lance--lancement-et-consentement) · [MENU](#2-menu--menus-lobby-et-agence) ·
[APPAR](#3-appar--appariement-et-invitation) · [PARTIE](#4-partie--déroulé-dune-partie-et-hud) ·
[ACTION](#5-action--actions-du-joueur-outils-caméra) ·
[VIEIL](#6-vieil--moteur-de-vieillissement-et-recettes) · [PARAD](#7-parad--paradoxes-non-conformités) ·
[CONTR](#8-contr--contrats-et-score) · [PEUPL](#9-peupl--peuples-figures-porte-voix-serments) ·
[CLIMA](#10-clima--météo-catastrophes-phénomènes) · [MUSEE](#11-musee--musée-chronique-carte-récap) ·
[MODES](#12-modes--modes-de-jeu) · [COMM](#13-comm--voix-pings-emotes-fantômes) ·
[STREAM](#14-stream--mode-streamer) · [PROGR](#15-progr--progression-et-boutique-chronos) ·
[OPT](#16-opt--options-et-accessibilité) · [SAUV](#17-sauv--sauvegarde-et-reprise) ·
[LIMIT](#18-limit--erreurs-et-cas-limites)

---

## 1. LANCE — lancement et consentement

**EF-LANCE-01** — Au premier lancement, l'écran de confidentialité et de consentement s'affiche **avant** le menu principal. *Source :* `32_UX_UI_SPEC.md §1`, `§2`. *Critère d'acceptation :* sur un profil vierge, aucun écran de menu n'est atteignable avant que le choix soit fait. *Priorité :* MUST.

**EF-LANCE-02** — L'écran de consentement propose deux boutons de **même poids visuel** (« Jouer sans rien partager » / « Aider avec des statistiques anonymes »), sans aucune case pré-cochée, et un lien vers la politique de confidentialité. *Source :* `60_LEGAL_COMPLIANCE.md §5`, `11_SCRIPTS_DIALOGUES.md §11` (PRIVACY_*). *Critère d'acceptation :* les deux boutons ont la même taille et le même style ; aucune case n'est cochée à l'ouverture. *Priorité :* MUST.

**EF-LANCE-03** — Télémétrie et rapports de plantage sont **désactivés par défaut**, n'émettent rien tant qu'aucun choix n'est fait, et ne s'activent que par consentement explicite. *Source :* `GDD §6.1`, `51_QA_TEST_PLAN.md §3`, `§9`. *Critère d'acceptation :* profil vierge : aucune requête vers un hôte de télémétrie pendant et après l'écran de consentement si « Jouer sans rien partager » est choisi. *Priorité :* MUST.

**EF-LANCE-04** — Le choix de consentement est modifiable à tout moment depuis Options › Confidentialité, retrait compris. *Source :* `60_LEGAL_COMPLIANCE.md §5`, `32_UX_UI_SPEC.md §1`. *Critère d'acceptation :* retirer le consentement en cours de session arrête immédiatement l'émission d'événements. *Priorité :* MUST.

**EF-LANCE-05** — Le jeu offre un bouton « Supprimer mes données locales ». *Source :* `GDD §6.1`, `51_QA_TEST_PLAN.md §9`. *Critère d'acceptation :* après usage, aucune donnée de progression ni de réglage ne subsiste dans le dossier utilisateur. *Priorité :* MUST.

**EF-LANCE-06** — La politique de confidentialité, les mentions légales, le CLUF et les licences tierces sont consultables depuis le menu (« Crédits & licences ») sans quitter le jeu. *Source :* `32_UX_UI_SPEC.md §1`, `60_LEGAL_COMPLIANCE.md §1`, `§7`. *Critère d'acceptation :* les quatre textes s'ouvrent en jeu et affichent leur date de mise à jour. *Priorité :* MUST.

**EF-LANCE-07** — Après le consentement, au premier lancement, le tutoriel Solo Relais se lance automatiquement et amène le joueur à planter une graine. *Source :* `32_UX_UI_SPEC.md §2`, `11_SCRIPTS_DIALOGUES.md §1`. *Critère d'acceptation :* la première graine est plantable en moins de 30 s, et le saut d'époque qui révèle l'arbre survient avant la 60ᵉ seconde. *Priorité :* MUST.

---

## 2. MENU — menus, lobby et Agence

**EF-MENU-01** — Le menu principal présente un seul bouton proéminent « JOUER », le reste des entrées restant discrètes, et il n'y a **jamais plus de deux clics** entre le menu principal et une partie avec des amis. *Source :* `32_UX_UI_SPEC.md §1`, `§2`. *Critère d'acceptation :* Jouer → Héberger → invitation par l'overlay : deux clics comptés. *Priorité :* MUST.

**EF-MENU-02** — L'entrée « Jouer » propose exactement : Héberger, Rejoindre (amis / code / public), Solo Relais, Capsule, Défi du jour. *Source :* `32_UX_UI_SPEC.md §1`. *Critère d'acceptation :* les cinq entrées sont présentes et fonctionnelles. *Priorité :* MUST.

**EF-MENU-03** — Le lobby affiche quatre cartes joueur portant chapeau, couleur et époque assignée, l'époque étant déplaçable d'une carte à l'autre. *Source :* `32_UX_UI_SPEC.md §4`. *Critère d'acceptation :* un déplacement d'époque est répercuté sur tous les clients. *Priorité :* MUST.

**EF-MENU-04** — Le lobby expose les modificateurs : durée de manche (180 / 300 / 420 s), multiplicateur de dangers (0,5 / 1 / 1,5), vitesse de paradoxe (lent / normal / rapide), rotation activée ou non. *Source :* `20_GAME_DESIGN_PARAMETERS.md §12`, `data/tuning.json` (`lobby_modifiers`, `match.rotation`). *Critère d'acceptation :* chaque modificateur agit sur la partie suivante avec la valeur lue dans `data/tuning.json`. *Priorité :* MUST.

**EF-MENU-05** — Un mode « Détente » désactive la jauge de paradoxe, applique 0,5× aux dangers et exclut la partie de tout classement. *Source :* `20_GAME_DESIGN_PARAMETERS.md §12`. *Critère d'acceptation :* la jauge est absente du HUD et la partie n'apparaît pas au classement du Défi du jour. *Priorité :* SHOULD.

**EF-MENU-06** — Le code d'invitation du lobby est masquable par un contrôle explicite. *Source :* `32_UX_UI_SPEC.md §4`, `GDD §3.9`. *Critère d'acceptation :* code masqué : aucun caractère lisible à l'écran ni dans une capture. *Priorité :* MUST.

**EF-MENU-07** — Le bouton « Lancer » n'est actif, pour l'hôte, que lorsque tous les joueurs sont prêts. *Source :* `32_UX_UI_SPEC.md §4`. *Critère d'acceptation :* un joueur non prêt rend le bouton inactif. *Priorité :* MUST.

**EF-MENU-08** — Avant la première manche, un écran de brief présente le contrat (portrait d'Odile, carte cartonnée, tampon « URGENT ») avec un compte à rebours de 15 s et un bouton « Compris ». *Source :* `32_UX_UI_SPEC.md §4`, `11_SCRIPTS_DIALOGUES.md §3`. *Critère d'acceptation :* le brief énonce objectif principal, deux bonus et exigence absurde, et se ferme au clic ou à l'expiration du compte à rebours. *Priorité :* MUST.

**EF-MENU-09** — Un écran « Agence » regroupe la progression, la boutique Chronos, les chapitres et le **Panthéon** (Figures rencontrées, leur domaine, leur Bienfait, leur Serment). *Source :* `32_UX_UI_SPEC.md §1`, `20_GAME_DESIGN_PARAMETERS.md §10`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8`. *Critère d'acceptation :* une Figure majeure née en partie apparaît au Panthéon avec ses quatre informations. *Priorité :* SHOULD.

**EF-MENU-10** — Le menu de pause en jeu propose Reprendre, Options, Confidentialité et Quitter la mission, y compris en ligne. *Source :* `32_UX_UI_SPEC.md §1`. *Critère d'acceptation :* les quatre entrées sont présentes et fonctionnelles en partie en ligne. *Priorité :* MUST.

**EF-MENU-11** — Tout texte affiché passe par la fonction de traduction ; aucun texte n'est codé en dur. *Source :* `32_UX_UI_SPEC.md` (en-tête), `50_PRODUCTION_PLAN.md §4` (Definition of Done). *Critère d'acceptation :* la pseudo-localisation de `51 §8` ne laisse apparaître aucune chaîne non traduite. *Priorité :* MUST.

---

## 3. APPAR — appariement et invitation

**EF-APPAR-01** — Les lobbies sont **« amis seulement » par défaut** ; l'ouverture au public est un choix explicite. *Source :* `GDD §6.2`, `32_UX_UI_SPEC.md §6`. *Critère d'acceptation :* profil vierge : le lobby créé n'est pas joignable par un non-ami. *Priorité :* MUST.

**EF-APPAR-02** — L'invitation d'un ami passe par l'overlay de la plateforme sans quitter le jeu, et une partie est aussi rejoignable par code d'invitation. *Source :* `32_UX_UI_SPEC.md §1`, `§2`, `40_TECHNICAL_DESIGN.md §6`. *Critère d'acceptation :* l'invitation aboutit sans reprise de main par le jeu ; un code invalide affiche un message non technique. *Priorité :* MUST.

**EF-APPAR-03** — L'allocation des époques suit le nombre de joueurs : 4 → E0 à E3 ; 3 → E0, E1, E2 (E3 simulée) ; 2 → E0 et E2 par défaut, E1 et E3 en option ; 1 → E0 puis E1, E2, E3 successivement. *Source :* `12_SCENARIOS.md §3`. *Critère d'acceptation :* pour chaque effectif, l'allocation correspond exactement au tableau de la source. *Priorité :* MUST.

**EF-APPAR-04** — Les époques sans joueur sont **simulées** à la pause café par des règles déterministes : Bouloche mange 30 % des pousses non protégées, Fiscalin confisque 50 % des objets brillants en zone publique, les Automates traitent les objets à moins de 4 m des rails, la Brigade recycle 100 % des anachronismes sans certificat. *Source :* `12_SCENARIOS.md §3`, `data/tuning.json` (`hazards.empty_era_sim`). *Critère d'acceptation :* même graine et même journal : même simulation des époques vides sur deux machines. *Priorité :* MUST.

**EF-APPAR-05** — À 3 joueurs, l'époque E3 est révélée à la pause café et visitée au musée, la Brigade n'y agissant qu'en simulation. *Source :* `12_SCENARIOS.md §3`. *Critère d'acceptation :* l'état de E3 est affiché à la pause café et visitable au musée. *Priorité :* MUST.

**EF-APPAR-06** — ***À trancher :*** le dossier ne décrit **aucun mécanisme d'appariement** pour un joueur qui n'a pas trois amis disponibles ; les lobbies publics sont une option, pas un appariement. *Source :* `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir avec la décision ; l'exigence n'est pas implémentable en l'état. *Priorité :* SHOULD.

**EF-APPAR-07** — ***À trancher :*** le comportement d'un joueur qui **rejoint en cours de partie** (ce qu'il voit, à quelle époque il entre, ce qui lui est rejoué) n'est pas spécifié. *Source :* `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir avec la décision. *Priorité :* SHOULD.

**EF-APPAR-08** — ***À trancher :*** le crossplay n'est ni exclu ni spécifié. *Source :* `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir avec la décision. *Priorité :* COULD.

**EF-APPAR-09** — ***À trancher :*** les joueurs de la démo peuvent rejoindre des amis, mais le dossier ne dit pas si cette possibilité est **permanente** après le Next Fest, ni si quatre joueurs peuvent jouer quand un seul possède le jeu. *Source :* `GDD §7.1`, `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir avec la décision. *Priorité :* SHOULD.

---

## 4. PARTIE — déroulé d'une partie et HUD

**EF-PARTIE-01** — Une partie compte 3 manches (4 en Solo Relais) de 300 s (240 s en Solo Relais), pour une durée cible de 15 à 20 minutes, et avertit les joueurs à 60 s et à 10 s de la fin de chaque manche. *Source :* `20_GAME_DESIGN_PARAMETERS.md §1`, `data/tuning.json` (`match`). *Critère d'acceptation :* toutes les durées sont lues dans `data/tuning.json` ; le chrono passe à l'orange à 60 s et au rouge à 10 s avec un signal sonore. *Priorité :* MUST.

**EF-PARTIE-02** — Entre deux manches, une pause café de 30 s enchaîne 10 s de cinématique des siècles, 15 s de vote et de rotation, puis 5 s de compte à rebours. *Source :* `20_GAME_DESIGN_PARAMETERS.md §1`. *Critère d'acceptation :* la somme des trois segments vaut `match.coffee_break_seconds`. *Priorité :* MUST.

**EF-PARTIE-03** — À chaque pause café, chaque joueur avance d'une époque (E3 → E0) et hérite de l'état laissé par son prédécesseur, sauf si la rotation est désactivée au lobby. *Source :* `20_GAME_DESIGN_PARAMETERS.md §1`, `11_SCRIPTS_DIALOGUES.md §5` (CAFE_ROTATE). *Critère d'acceptation :* après rotation, chaque joueur occupe l'époque suivante. *Priorité :* MUST. *Point à expliciter :* avec 3 manches, un joueur ne voit que 3 des 4 époques dans une partie (`docs/backlog.md`).

**EF-PARTIE-04** — La pause café affiche la frise des quatre époques en bandes horizontales qui se remplissent, l'annonce de rotation fléchée, et le vote des spectateurs s'il est actif. *Source :* `32_UX_UI_SPEC.md §4`. *Critère d'acceptation :* les trois éléments sont lisibles à 1280 × 800. *Priorité :* MUST.

**EF-PARTIE-05** — Les jauges des Peuples, les bifurcations, l'usure des chemins et le déclenchement des catastrophes sont résolus **à la pause café**, jamais pendant une manche. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §1.2`, `§5.1`, `21_WORLD_LEVEL_DESIGN.md §6`. *Critère d'acceptation :* pendant une manche, aucun sentier ne se dessine sous les pas et aucune jauge de Peuple ne change. *Priorité :* MUST.

**EF-PARTIE-06** — La visite du musée dure 120 s au maximum et ne peut être écourtée qu'à l'unanimité. *Source :* `20_GAME_DESIGN_PARAMETERS.md §1`. *Critère d'acceptation :* un seul refus empêche l'écourtement. *Priorité :* MUST.

**EF-PARTIE-07** — La séquence d'une partie est : brief → (manche → pause café) × 3 → évaluation → musée → carte-récap → lobby. *Source :* `32_UX_UI_SPEC.md §1`. *Critère d'acceptation :* l'enchaînement est respecté sans écran intermédiaire non spécifié. *Priorité :* MUST.

**EF-PARTIE-08** — Le HUD affiche en permanence le badge d'époque (icône + nom + couleur + motif d'accessibilité), le chrono et le numéro de manche, et la carte du contrat repliable dont les bonus se cochent en direct. *Source :* `32_UX_UI_SPEC.md §3`. *Critère d'acceptation :* le badge est identifiable sans la couleur seule ; valider un bonus en jeu coche l'entrée correspondante sans action du joueur. *Priorité :* MUST.

**EF-PARTIE-09** — Le HUD affiche la jauge de non-conformité (0-100, trois seuils marqués), l'inventaire (3 emplacements + 1 objet lourd), les indicateurs de voix des quatre joueurs avec l'état du micro, et un réticule contextuel nommant l'action disponible et sa touche. *Source :* `32_UX_UI_SPEC.md §3`. *Critère d'acceptation :* les quatre blocs sont présents et lisibles à 1280 × 800 ; l'intitulé du réticule change selon la cible visée. *Priorité :* MUST.

**EF-PARTIE-10** — Les notifications de recette (« Votre graine (an 0) est devenue un arbre (an 300) ») s'affichent 3 s, à raison d'une au maximum toutes les 2 s. *Source :* `32_UX_UI_SPEC.md §3`. *Critère d'acceptation :* dix propagations simultanées ne produisent pas plus d'une notification par 2 s. *Priorité :* MUST.

**EF-PARTIE-11** — Les fantômes des autres époques portent une icône d'époque en espace monde, et le nom des joueurs s'affiche en deçà de 15 m. *Source :* `32_UX_UI_SPEC.md §3`. *Critère d'acceptation :* au-delà de 15 m, aucun nom n'est affiché ; l'icône d'époque reste lisible. *Priorité :* SHOULD.

**EF-PARTIE-12** — La musique suit l'état de la partie : couche de base permanente, couche de tension en fondu de 1,5 s quand un danger est à moins de 15 m ou que la jauge atteint 50, couche de pause café au tempo accéléré, et la mélodie se poursuit **à la même mesure** lors d'un changement d'époque. *Source :* `31_AUDIO_DESIGN.md §1.2`. *Critère d'acceptation :* les trois couches et la continuité de mesure sont observables à l'écoute. *Priorité :* SHOULD.

---

## 5. ACTION — actions du joueur, outils, caméra

**EF-ACTION-01** — Le joueur marche à 4,5 m/s, court à 7,5 m/s avec 6 s d'endurance et 4 s de régénération, et saute 1,2 m sans double saut. *Source :* `20_GAME_DESIGN_PARAMETERS.md §2`, `data/tuning.json` (`player`). *Critère d'acceptation :* valeurs mesurées égales à celles de `data/tuning.json` ; une seconde pression en l'air n'a aucun effet. *Priorité :* MUST.

**EF-ACTION-02** — L'interaction porte à 2,5 m dans un cône de 90°. *Source :* `20_GAME_DESIGN_PARAMETERS.md §2`, `40_TECHNICAL_DESIGN.md §6`. *Critère d'acceptation :* une cible à 2,6 m ou hors du cône n'est pas interactive, et l'hôte rejette la requête correspondante. *Priorité :* MUST.

**EF-ACTION-03** — L'inventaire offre 3 emplacements pour petits objets et 1 objet lourd porté à deux mains (0,7× de vitesse) ; les objets lourds désignés (tronc, menhir, Bouloche bébé) sont portés à deux (0,5×) ou traînés par un seul (0,3×). *Source :* `20_GAME_DESIGN_PARAMETERS.md §2`. *Critère d'acceptation :* un quatrième petit objet est refusé ; les trois régimes de vitesse sont observables. *Priorité :* MUST.

**EF-ACTION-04** — Creuser prend 1,5 s par cellule de 2 m jusqu'à 3 cellules de profondeur ; planter prend 0,5 s. *Source :* `20_GAME_DESIGN_PARAMETERS.md §2`. *Critère d'acceptation :* la quatrième cellule de profondeur est refusée ; les durées correspondent à `data/tuning.json`. *Priorité :* MUST.

**EF-ACTION-05** — Il n'existe **aucun point de vie** : les dangers étourdissent 2 s ou confisquent, jamais ne tuent ; une chute ne blesse pas et étourdit 1,5 s au-delà de 6 m. *Source :* `20_GAME_DESIGN_PARAMETERS.md §2`, `GDD §2.1`. *Critère d'acceptation :* aucun état de mort n'est atteignable, quel que soit le danger ou la hauteur de chute. *Priorité :* MUST.

**EF-ACTION-06** — Les joueurs n'ont pas de collision entre eux, et les fantômes n'ont aucune physique. *Source :* `20_GAME_DESIGN_PARAMETERS.md §2`, `40_TECHNICAL_DESIGN.md §5`. *Critère d'acceptation :* aucun joueur ne peut bloquer physiquement un autre. *Priorité :* MUST.

**EF-ACTION-07** — Le joueur dispose des outils suivants avec leurs paramètres : pelle, pistolet à graines (portée 15 m, 1 graine / 0,8 s, 20 par manche), socle de statue (1 par joueur par manche, capture 2 s), pigments (3 couleurs, 10 applications), corne d'appel (20 m, cooldown 10 s), cabine temporelle (1 objet par manche), ancre temporelle (2 charges par partie), sablier de poche (aperçu du +1 saut pendant 5 s, cooldown 20 s), faux certificat. *Source :* `20_GAME_DESIGN_PARAMETERS.md §7`, `data/tuning.json` (`tools`). *Critère d'acceptation :* chaque paramètre est lu dans `data/tuning.json` ; aucun outil n'ignore sa limite d'usage. *Priorité :* MUST.

**EF-ACTION-08** — L'ancre temporelle rend l'objet ancré insensible aux recettes à tous les sauts ; le sablier de poche montre l'état du +1 saut **sans l'engager**. *Source :* `20_GAME_DESIGN_PARAMETERS.md §4.3` (`protected`), `§7`. *Critère d'acceptation :* un objet ancré est identique aux sauts +1, +2 et +3 ; l'aperçu disparaît après 5 s sans modifier l'état du monde. *Priorité :* MUST.

**EF-ACTION-09** — La capture de pose n'utilise que des **poses prédéfinies** (8 poses), jamais une pose libre. *Source :* `33_VISUAL_TARGETS.md §3`, `60_LEGAL_COMPLIANCE.md §6`. *Critère d'acceptation :* l'interface ne propose que les 8 poses listées ; aucune manipulation du squelette n'est offerte au joueur. *Priorité :* MUST.

**EF-ACTION-10** — La caméra est à la troisième personne, à 4,5 m (zoom 2,5 à 7 m), hauteur 1,8 m, champ de vision 70° réglable de 60 à 100°, avec collision ; un mode « épaule » s'active à la visée. *Source :* `20_GAME_DESIGN_PARAMETERS.md §11`, `data/tuning.json` (`camera`). *Critère d'acceptation :* les bornes sont celles de `data/tuning.json` ; la caméra ne traverse pas la géométrie. *Priorité :* MUST.

**EF-ACTION-11** — Les commandes sont intégralement remappables, l'agencement azerty / qwerty est détecté automatiquement, et les icônes de manette suivent le fabricant détecté. *Source :* `32_UX_UI_SPEC.md §5`. *Critère d'acceptation :* chaque action du tableau `32 §5` est remappable ; un clavier azerty affiche ZQSD sans réglage. *Priorité :* MUST.

**EF-ACTION-12** — Quatre cabines de téléportation fixes, une par repère, sont utilisables une fois par manche. *Source :* `21_WORLD_LEVEL_DESIGN.md §8`. *Critère d'acceptation :* un second usage dans la même manche est refusé. *Priorité :* SHOULD.

**EF-ACTION-13** — Le terrain est déformable sur la grille de 2 m (creuser, remblayer, tranchées) ; l'eau s'écoule vers la cellule voisine la plus basse à 4 Hz de façon déterministe ; la pente maximale marchable est de 35°. *Source :* `20_GAME_DESIGN_PARAMETERS.md §3`, `40_TECHNICAL_DESIGN.md §5`. *Critère d'acceptation :* une tranchée reliée à la rivière détourne l'eau de façon identique sur deux machines ; au-delà de 35°, le joueur ne progresse pas. *Priorité :* MUST.

**EF-ACTION-14** — Les dangers se comportent selon les machines à états et paramètres de `20 §8` : Bouloche (E0), Sire Fiscalin (E1), Automates et smog (E2), Brigade Propreté (E3), Chronomites et touristes ; chacun a une contre-mesure explicite. *Source :* `20_GAME_DESIGN_PARAMETERS.md §8`, `data/tuning.json` (`hazards`). *Critère d'acceptation :* chaque danger détecte, agit et se laisse contrer selon les valeurs de `data/tuning.json`. *Priorité :* MUST.

---

## 6. VIEIL — moteur de vieillissement et recettes

**EF-VIEIL-01** — Toute trace persistante porte une recette temporelle : une fonction pure de son état et de son environnement vers son état 300 ans plus tard. *Source :* `GDD §3.3`, `40_TECHNICAL_DESIGN.md §1`. *Critère d'acceptation :* deux appels de propagation sur le même état donnent le même résultat, sans effet de bord. *Priorité :* MUST.

**EF-VIEIL-02** — Pour une même graine et un même journal d'actions, le résultat du vieillissement est **identique sur tous les clients**. *Source :* `GDD §3.3`, `40_TECHNICAL_DESIGN.md §4`. *Critère d'acceptation :* les hachages des quatre époques sont identiques sur deux machines après rejeu d'un journal de 200 actions. *Priorité :* MUST.

**EF-VIEIL-03** — Une chaîne de recettes ne dépasse jamais 3 sauts d'époque. *Source :* `20_GAME_DESIGN_PARAMETERS.md §4.3`, `data/tuning.json` (`aging.max_hops`), `GDD §9`. *Critère d'acceptation :* aucune sortie n'est produite au-delà du saut 3. *Priorité :* MUST.

**EF-VIEIL-04** — Les traces portent les étiquettes de `20 §4.1` (`organic`, `mineral`, `metal`, `crafted`, `living`, `symbolic`, `liquid`, `fire`, `anachronism`, `protected`), et les conditions d'environnement évaluables sont exactement celles énumérées par le schéma de recette. *Source :* `20_GAME_DESIGN_PARAMETERS.md §4.1`, `§4.2`, `data/schemas/recipe.schema.json`. *Critère d'acceptation :* `python3 tools/validate_data.py` rejette toute étiquette ou condition hors liste. *Priorité :* MUST.

**EF-VIEIL-05** — Quand plusieurs recettes s'appliquent, la `priority` la plus haute gagne ; à égalité, l'identifiant alphabétique tranche. L'ordre du fichier **ne départage jamais**. *Source :* `20_GAME_DESIGN_PARAMETERS.md §4.3`, `data/schemas/recipe.schema.json` (`priority`). *Critère d'acceptation :* permuter l'ordre des recettes dans `data/recipes/` ne change aucun résultat de propagation. *Priorité :* MUST.

**EF-VIEIL-06** — Une sortie de recette peut proposer des variantes pondérées, tirées par un générateur à graine indexé par `(graine, identifiant d'entité, saut)`. *Source :* `20_GAME_DESIGN_PARAMETERS.md §4.3`, `40_TECHNICAL_DESIGN.md §4`. *Critère d'acceptation :* même triplet d'entrée, même variante, sur deux machines et deux exécutions. *Priorité :* MUST.

**EF-VIEIL-07** — Une recette peut être **croisée** : exiger une seconde trace dans un rayon donné, éventuellement consommée par le résultat. *Source :* `data/schemas/recipe.schema.json` (`input.with`), `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8`. *Critère d'acceptation :* la recette ne se déclenche pas si la compagne est hors du rayon ; avec `consumes`, la compagne disparaît. *Priorité :* MUST.

**EF-VIEIL-08** — L'Early Access comporte 30 recettes valides, l'objectif ultérieur étant d'au moins 60. *Source :* `GDD §3.3`, `71_LIVE_OPS.md §2`. *Critère d'acceptation :* `data/recipes/` contient 30 recettes conformes au schéma à la porte G4. *Priorité :* MUST. *État constaté le 7 octobre 2026 :* `data/recipes/` contient **35** recettes, dont **4** croisées (`input.with`) — l'objectif de 30 est donc dépassé en nombre, mais `docs/backlog.md` annonce « 10 recettes croisées » et la revue joueur « 25 écrites » : les deux mentions sont périmées.

**EF-VIEIL-09** — La propagation est calculée instantanément, mais l'apparition visuelle dans l'époque aval dure 0,4 s et porte un son dédié. *Source :* `20_GAME_DESIGN_PARAMETERS.md §4.4`, `31_AUDIO_DESIGN.md §2`. *Critère d'acceptation :* l'entité existe dans l'état aval avant la fin de l'animation, mesurée à 0,4 s. *Priorité :* MUST.

**EF-VIEIL-10** — Chaque trace vieillie change de silhouette à chaque saut. *Source :* `33_VISUAL_TARGETS.md §1`, `21_WORLD_LEVEL_DESIGN.md §10`. *Critère d'acceptation :* revue visuelle : graine, arbre, grand arbre et arbre millénaire sont distinguables en silhouette à contre-jour. *Priorité :* MUST.

**EF-VIEIL-11** — Une trace vieillie occupe les cellules correspondant à sa taille ; si l'emplacement aval est occupé par un bâtiment d'époque, la recette produit sa variante « contrariée », et un lac formé sur un quartier bâti ajoute +10 à la jauge de non-conformité. *Source :* `21_WORLD_LEVEL_DESIGN.md §5`, `data/schemas/recipe.schema.json` (`contrary`). *Critère d'acceptation :* planter sous un bâtiment produit la variante `contrary` ; le cas du lac ajoute exactement 10. *Priorité :* MUST.

**EF-VIEIL-12** — Le budget est de 2 000 entités persistantes par époque, et son approche ne provoque ni plantage ni perte de déterminisme. *Source :* `20_GAME_DESIGN_PARAMETERS.md §3`, `data/tuning.json` (`world.trace_budget_per_era`), `51_QA_TEST_PLAN.md §6`. *Critère d'acceptation :* la scène de stress de `51 §6` (2 000 traces par époque, 4 joueurs, smog, 6 Chronomites) tourne sans plantage. *Priorité :* MUST.

**EF-VIEIL-13** — L'usure des chemins produit un sentier à 40 passages, une route pavée à 120 et un tapis roulant à 300, en comptant les passages de toutes les époques. *Source :* `21_WORLD_LEVEL_DESIGN.md §6`, `data/tuning.json` (`aging.path_wear_thresholds`). *Critère d'acceptation :* les trois seuils déclenchent les trois résultats, lus dans `data/tuning.json`. *Priorité :* SHOULD.

**EF-VIEIL-14** — Les objets placés dans la Grotte Qui Ronfle sont protégés du vieillissement extérieur. *Source :* `10_NARRATIVE_BIBLE.md §3`, `20_GAME_DESIGN_PARAMETERS.md §4.3` (`seed_cave`, `metal_cave`). *Critère d'acceptation :* une graine en grotte reste une graine aux sauts +1 et +2 et devient « graine fossile » au saut +3. *Priorité :* MUST.

**EF-VIEIL-15** — Un objet d'une époque amené dans une époque antérieure est un **anachronisme** : fan-club, puis religion technologique, puis paradoxe latent (+10 à la jauge). *Source :* `20_GAME_DESIGN_PARAMETERS.md §4.3` (`anachronism`), `GDD §3.3`. *Critère d'acceptation :* la chaîne des trois sauts est observable et ajoute +10 au troisième. *Priorité :* MUST.

**EF-VIEIL-16** — Les recettes, les contrats, les phrases et les réglages sont chargés depuis `data/`, validés contre leur schéma, et un fichier non conforme est **rejeté explicitement** au démarrage. *Source :* `40_TECHNICAL_DESIGN.md §3`, `AGENTS.md §5.5`. *Critère d'acceptation :* un fichier de recette invalide empêche le démarrage avec un message nommant le fichier et l'erreur. *Priorité :* MUST.

---

## 7. PARAD — paradoxes (non-conformités)

**EF-PARAD-01** — Une jauge de non-conformité d'équipe va de 0 à 100 et décroît de 1 par seconde en l'absence de non-conformité active. *Source :* `20_GAME_DESIGN_PARAMETERS.md §5`, `data/tuning.json` (`paradox`). *Critère d'acceptation :* la jauge est commune aux quatre joueurs ; à 40 et sans non-conformité, elle atteint 30 en 10 s. *Priorité :* MUST.

**EF-PARAD-02** — Modifier une trace héritée depuis une époque aval la marque « revendiquée » ; la changer ensuite en amont ajoute +15 (modification mineure) ou +25 (destruction). *Source :* `20_GAME_DESIGN_PARAMETERS.md §5`, `51_QA_TEST_PLAN.md §3`. *Critère d'acceptation :* arracher la graine d'un arbre gravé en aval ajoute exactement 25. *Priorité :* MUST.

**EF-PARAD-03** — La trace contredite clignote 3 s puis se transforme (« glitch »), et les seuils 25, 50, 75 et 100 déclenchent les messages correspondants. *Source :* `GDD §3.4`, `51_QA_TEST_PLAN.md §3`, `11_SCRIPTS_DIALOGUES.md §5`. *Critère d'acceptation :* le clignotement dure 3 s, la variante sans flash est utilisée si l'option de photosensibilité est active, et les quatre messages se déclenchent à leur seuil. *Priorité :* MUST.

**EF-PARAD-04** — Un anachronisme sans certificat ajoute +5 à chaque pause café. *Source :* `20_GAME_DESIGN_PARAMETERS.md §5`. *Critère d'acceptation :* deux pauses café avec un anachronisme non certifié ajoutent 10. *Priorité :* MUST.

**EF-PARAD-05** — Des Chronomites apparaissent à 50 (3 créatures) et à 75 (6) ; chacune ronge une trace toutes les 20 s de façon déterministe, et se chasse à la corne (cooldown 10 s) ou en réparant la contradiction. *Source :* `20_GAME_DESIGN_PARAMETERS.md §5`, `§7`. *Critère d'acceptation :* même graine et même journal : les mêmes traces sont rongées dans le même ordre. *Priorité :* MUST.

**EF-PARAD-06** — Les Chronomites ciblent **en priorité les Figures**. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8`, `10_NARRATIVE_BIBLE.md §7` (chapitre 3). *Critère d'acceptation :* en présence d'une Figure et de traces ordinaires, la Figure est visée la première. *Priorité :* SHOULD.

**EF-PARAD-07** — Rompre un Serment ajoute +10 à la jauge. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.3`, `data/tuning.json` (`faith.oath_broken_paradox`). *Critère d'acceptation :* la rupture ajoute exactement 10. *Priorité :* MUST.

**EF-PARAD-08** — À 100, la partie se termine par un **Effondrement** : cinématique de 10 s, aile du musée fermée, 50 % des Chronos acquis, score plafonné à 40, et la partie compte comme jouée. *Source :* `20_GAME_DESIGN_PARAMETERS.md §5`, `§6`, `12_SCENARIOS.md §4`. *Critère d'acceptation :* les cinq conséquences sont observables. *Priorité :* MUST.

**EF-PARAD-09** — Le paradoxe est aussi un **outil** : certains contrats l'exigent volontairement. *Source :* `GDD §3.4`, `12_SCENARIOS.md §2` (C10). *Critère d'acceptation :* au moins un contrat de `data/contracts/` est validé par la création d'un anachronisme. *Priorité :* SHOULD.

**EF-PARAD-10** — En mode « Détente », la jauge de paradoxe est désactivée sans que le reste des règles change. *Source :* `20_GAME_DESIGN_PARAMETERS.md §12`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §11`. *Critère d'acceptation :* aucune non-conformité n'est comptée et aucune Chronomite n'apparaît en mode Détente. *Priorité :* SHOULD.

---

## 8. CONTR — contrats et score

**EF-CONTR-01** — Les contrats sont générés procéduralement à partir de modèles de la forme « le client de l'an 900 veut [RÉSULTAT] à [LIEU] », et comportent 1 objectif principal, 2 bonus et 1 exigence absurde. *Source :* `GDD §3.5`, `11_SCRIPTS_DIALOGUES.md §3`. *Critère d'acceptation :* chaque contrat généré porte les quatre éléments ; deux graines différentes produisent deux énoncés distincts. *Priorité :* MUST.

**EF-CONTR-02** — Un contrat est décrit **en données** par : résultat attendu (type d'entité + zone + époque), conditions de bonus, exigence absurde, seuils de score, outils requis et chapitre. *Source :* `12_SCENARIOS.md §2`. *Critère d'acceptation :* `python3 tools/validate_data.py` valide `data/contracts/` contre son schéma. *Priorité :* MUST.

**EF-CONTR-03** — L'Early Access propose les 12 contrats de référence C01 à C12, répartis sur les 5 chapitres. *Source :* `12_SCENARIOS.md §2`, `71_LIVE_OPS.md §2`. *Critère d'acceptation :* les 12 identifiants existent et sont jouables à la porte G4. *Priorité :* MUST. *État constaté le 7 octobre 2026 :* `data/contracts/` contient **16** contrats (C01 à C16) ; `13 §8` documente l'ajout de C13 et C14, mais C15 et C16 n'apparaissent dans aucun document de conception — seule une mention de passage dans `12 §4bis` (« bonus C16 manqué ») y renvoie. Le tableau de `12 §2` est à mettre à jour (`docs/backlog.md`).

**EF-CONTR-04** — Le score s'établit ainsi : objectif principal 60 ; solution alternative 36 ; chaque bonus 15 ; exigence absurde 10 ; richesse du musée +1 par trace distincte exposée, plafonnée à 20 ; pénalité de paradoxe −0,2 × valeur maximale atteinte ; plafond de 40 en cas d'Effondrement. *Source :* `20_GAME_DESIGN_PARAMETERS.md §6`, `data/tuning.json` (`score`). *Critère d'acceptation :* un jeu de cas de référence donne les scores attendus, toutes valeurs lues dans `data/tuning.json`. *Priorité :* MUST.

**EF-CONTR-05** — Les étoiles sont attribuées aux seuils 90, 75, 55 et 35 ; les Chronos valent 20 × étoiles + 2 × richesse, doublés à la première victoire 5 étoiles du jour. *Source :* `20_GAME_DESIGN_PARAMETERS.md §6`. *Critère d'acceptation :* un score de 90 donne 5 étoiles, 89 en donne 4 ; la formule des Chronos est vérifiable sur une partie notée. *Priorité :* MUST.

**EF-CONTR-06** — Si le chaos rend le contrat impossible, le Client accepte une **solution alternative** : tout résultat du même type dans un rayon de 30 m donne 60 % des points de l'objectif. *Source :* `12_SCENARIOS.md §4`, `20_GAME_DESIGN_PARAMETERS.md §6`. *Critère d'acceptation :* 36 points sont attribués dans ce cas, 0 au-delà du rayon. *Priorité :* MUST.

**EF-CONTR-07** — L'écran d'évaluation présente l'hologramme du Client, les étoiles qui tombent une par une (0,3 s) et le détail des points. *Source :* `32_UX_UI_SPEC.md §4`, `11_SCRIPTS_DIALOGUES.md §4`. *Critère d'acceptation :* le détail affiché reconstitue exactement le score final. *Priorité :* MUST.

**EF-CONTR-08** — Au chapitre 4, un contrat peut être **refusé ou saboté** sans perdre la partie : la note tombe à 1 étoile et un déblocage secret est accordé. *Source :* `10_NARRATIVE_BIBLE.md §7`. *Critère d'acceptation :* le refus termine la partie normalement, note 1 étoile, déblocage accordé. *Priorité :* SHOULD.

**EF-CONTR-09** — Au chapitre 5 (« Le Vernissage »), l'équipe choisit entre **Livrer** (5 étoiles, Figures archivées), **Garder** (1 étoile, déblocage de la Saison 1) et **Tricher** (4 étoiles, fin secrète, réservé à qui possède une Figure d'Ailleurs). *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §7`. *Critère d'acceptation :* les trois issues sont atteignables et distinctes ; aucune n'est présentée comme « la bonne ». *Priorité :* SHOULD.

**EF-CONTR-10** — La Ferveur ne doit récompenser qu'une petite minorité de contrats, afin qu'elle ne devienne pas la seule stratégie optimale ; `13 §11` chiffre cette minorité à 2 contrats sur 14. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §11`. *Critère d'acceptation :* le rapport entre les contrats citant la Ferveur et le total des contrats de `data/contracts/` reste au plus égal à celui de la source. *Priorité :* SHOULD. *État constaté le 7 octobre 2026 :* **4** des **16** contrats de `data/contracts/` citent la Ferveur ou une Figure (C13 à C16), soit un rapport de 1 sur 4 au lieu de 1 sur 7 : l'équilibre annoncé par `13 §11` n'est pas tenu par les données. À arbitrer (`docs/backlog.md`).

---

## 9. PEUPL — peuples, Figures, Porte-Voix, Serments

**EF-PEUPL-01** — Chaque Peuple porte cinq jauges entières bornées à 100 — Eau, Vivres, Abri, Ferveur, Rancune — calculées comme des sommes d'entiers sur la grille, sans dépendre de l'horloge ni d'un hasard hors graine. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §1.2`, `data/tuning.json` (`peoples`). *Critère d'acceptation :* même graine et même journal : mêmes jauges, valeurs entières, sur deux machines. *Priorité :* MUST.

**EF-PEUPL-02** — À chaque passage d'époque, le Peuple **bifurque** selon les règles chiffrées de `13 §1.3`, évaluées à la pause café ; en cas d'égalité, la branche par défaut gagne. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §1.3`, `data/tuning.json` (`peoples.branch`). *Critère d'acceptation :* un cas d'égalité construit produit la branche par défaut, de façon reproductible. *Priorité :* MUST.

**EF-PEUPL-03** — Neuf états de civilisation d'arrivée sont atteignables en l'an 900, et chacun change les dangers, les PNJ, la musique et le musée. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §1.3`. *Critère d'acceptation :* un harnais de graines atteint au moins 6 des 9 civilisations ; « Les Ateliers Libres » n'ont pas d'Automates sur rails, « La Commune du Jardin » n'a pas de Brigade, « Le Musée Vide » n'a aucun PNJ et double le score de richesse. *Priorité :* MUST.

**EF-PEUPL-04** — À la pause café, une **frise des peuples** affiche, par époque, le nom du Peuple, son icône et la jauge qui a fait basculer la bifurcation. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §1.4`. *Critère d'acceptation :* la frise nomme la jauge décisive et sa valeur (« Eau 28 → Nomades »), lisible en 3 s et sans dépendre de la couleur seule. *Priorité :* MUST.

**EF-PEUPL-05** — Toute trace porte une **Ferveur** entière, propagée par les recettes comme le reste de son état. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.1`, `data/schemas/recipe.schema.json` (`faith`). *Critère d'acceptation :* la Ferveur d'une trace survit au saut d'époque selon la recette appliquée. *Priorité :* MUST.

**EF-PEUPL-06** — Une trace devient **Figure locale** à 30 de Ferveur (plaque nommée, détour des PNJ, Fiscalin n'ose plus confisquer) et **Figure majeure** à 70. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.1`, `data/tuning.json` (`faith`). *Critère d'acceptation :* les trois statuts et leurs effets apparaissent aux seuils exacts. *Priorité :* MUST.

**EF-PEUPL-07** — Les gains de Ferveur par pause café sont +3 (PNJ passé à moins de 3 m), +5 (trace ayant survécu à une catastrophe), +8 (la plus haute ou la plus ancienne de sa zone), +10 (citée par un contrat) ; les pertes −5 (trace rivale du même domaine montant plus vite) et −15 (détruite puis reconstruite ailleurs). *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.1`, `data/tuning.json` (`peoples.gain`, `peoples.loss`). *Critère d'acceptation :* chaque source produit exactement sa valeur, lue dans `data/tuning.json`. *Priorité :* MUST.

**EF-PEUPL-08** — Le **domaine** d'une Figure n'est pas choisi : il est hérité des étiquettes de la trace d'origine, parmi Croissance, Eau, Geste, Éclat, Chaleur, Ailleurs, Mémoire. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.2`. *Critère d'acceptation :* une statue de pose donne toujours Geste ; un objet brillant confisqué donne Éclat. *Priorité :* MUST.

**EF-PEUPL-09** — Les noms de Figures sont assemblés par **modèles de phrases** depuis `data/phrases/`, jamais générés par une IA en jeu. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.2`, `GDD §3.8`, `§6.5`. *Critère d'acceptation :* aucun appel à un modèle génératif n'existe dans le chemin de nommage ; tous les fragments viennent de `data/phrases/`. *Priorité :* MUST.

**EF-PEUPL-10** — Chaque Figure majeure accorde un **Bienfait** et réclame un **Serment** selon les sept couples de `13 §2.3`, sans ajout ni substitution ; rompre le Serment inverse le Bienfait pendant exactement une manche et rend les PNJ boudeurs, sans autre punition. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.3`, `data/tuning.json` (`faith.sulk_rounds`). *Critère d'acceptation :* les sept domaines produisent les effets listés (Mémoire : traces insensibles aux catastrophes) ; la rupture n'enlève aucun point de vie ni aucun objet. *Priorité :* MUST.

**EF-PEUPL-11** — Deux Figures du même domaine à moins de 60 m déclenchent un **Procès en Authenticité** : à la pause café suivante, celle qui a le plus de Ferveur absorbe l'autre, qui garde 30 % de sa Ferveur en « site annexe ». Aucun affrontement. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.4`, `data/tuning.json` (`faith.conflict_radius_m`, `faith.absorb_keep_ratio`). *Critère d'acceptation :* le conflit se résout par absorption et affichage, sans aucune mécanique de combat. *Priorité :* SHOULD.

**EF-PEUPL-12** — Un **Porte-Voix** apparaît dès qu'une Figure dépasse 70 ; les quatre Porte-Voix (Petit Moss en E0, Dame Orielle en E1, Contremaître Bouilly en E2, Vé-7 en E3) produisent les effets de jeu de `13 §3`, dont la transmission faillible du domaine par Petit Moss une fois sur deux. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §3`, `10_NARRATIVE_BIBLE.md §6`. *Critère d'acceptation :* chaque Porte-Voix produit son effet (Orielle : +10 Ferveur garantis si on lui montre une trace) ; le tirage de Petit Moss est déterministe à graine donnée. *Priorité :* SHOULD.

**EF-PEUPL-13** — Toute la couche des Peuples et des Figures est **passive** : une partie 5 étoiles est atteignable sans qu'aucune Figure ne naisse. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §11`. *Critère d'acceptation :* une partie notée 5 étoiles sans Figure est jouable et reproductible. *Priorité :* MUST.

**EF-PEUPL-14** — Aucun nom, symbole, rite, fête ou formule ne renvoie à une religion, une divinité, une institution religieuse ou une culture réelles ; le vocabulaire est celui de la vallée (Figure, Ferveur, Porte-Voix, Serment, Veillée) ; aucune violence de croyance n'existe, les conflits de Figures restant bureaucratiques et comiques. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0`, `10_NARRATIVE_BIBLE.md §10`. *Critère d'acceptation :* revue humaine obligatoire avant publication, consignée (`13 §10`), sans aucune occurrence contrevenante. *Priorité :* MUST.

---

## 10. CLIMA — météo, catastrophes, phénomènes

**EF-CLIMA-01** — La météo d'une époque **découle** d'un Indice Climatique calculé sur la vallée (couvert forestier, surface d'eau, pollution, sol nu) et de la graine ; elle n'est jamais tirée au sort, et cet indice se transmet d'une époque à l'autre comme une trace. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §4.1`, `§4.2`. *Critère d'acceptation :* une vallée déboisée en E0 arrive en E3 avec un ciel de Canicule et une rivière maigre, de façon reproductible ; une vallée reboisée arrive verte. *Priorité :* MUST.

**EF-CLIMA-02** — Sept états de météo existent (Clair, Pluie, Brume, Vent du Plateau, Canicule, Gel, Pluie acide) avec les effets chiffrés de `13 §4.1` ; la météo change au maximum une fois par manche et est annoncée 15 s à l'avance par un signe visuel et sonore. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §4.1`, `data/tuning.json` (`weather`). *Critère d'acceptation :* chaque état produit son effet (pluie : pousse ×2 ; vent : érosion ×2 ; canicule : incendie ×3 ; pluie acide : 1 cran de rouille par manche) ; aucun changement sans annonce, aucun second changement dans la manche. *Priorité :* MUST.

**EF-CLIMA-03** — Les sept catastrophes (Crue, Sécheresse, Incendie, Glissement de terrain, Grand Gel, Chute de météore, Tempête de la Compagnie) sont **annoncées** par des signes pendant 45 s, **atténuables** par une action claire, **non létales** et **transformatrices**, et se déclenchent sur les seuils chiffrés de `13 §5.1`. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §5.1`, `data/tuning.json` (`disasters`). *Critère d'acceptation :* aucune catastrophe sans signes ; aucun PNJ blessé ; chaque seuil vaut la valeur de `data/tuning.json` (crue : 3 barrages ; sécheresse : forêt < 20 % ; glissement : 2 cellules creusées ; gel : abri < 30 ; météore : 1 sur 8 ; tempête : pollution ≥ 70). *Priorité :* MUST.

**EF-CLIMA-04** — Une catastrophe ne retire jamais plus de 20 % des traces d'une époque, et **jamais** une trace protégée par une Figure de Mémoire. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §5.1`, `§10`, `data/tuning.json` (`disasters.max_traces_removed_ratio`). *Critère d'acceptation :* sur un harnais de graines, le ratio n'est jamais dépassé et aucune trace protégée ne disparaît. *Priorité :* MUST.

**EF-CLIMA-05** — Aucune catastrophe ne fait perdre la partie. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §5.2`. *Critère d'acceptation :* la partie se poursuit après chacune des sept catastrophes. *Priorité :* MUST.

**EF-CLIMA-06** — Cinq phénomènes existent : la Résonance (20 s, une fois par partie, à la 2ᵉ pause café, les quatre époques superposées), la Brume Remontante (Brume + Ferveur ≥ 50), la Nuit Sans Ombre (Gel + ciel clair), l'Aurore des Traces (après une catastrophe survécue, +10 Ferveur aux survivantes) et le Silence (1 partie sur 50, 15 s sans aucun son). *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §6`, `data/tuning.json` (`phenomena`). *Critère d'acceptation :* chaque phénomène se déclenche à sa condition exacte et dure la durée annoncée. *Priorité :* SHOULD.

**EF-CLIMA-07** — Pendant un orage, une chute de météore et la Résonance, **aucun flash ne dépasse 3 Hz**, y compris en dehors du mode « réduire les clignotements ». *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6`, `§10`, `51_QA_TEST_PLAN.md` (tableau `13`). *Critère d'acceptation :* mesure image par image sur les trois séquences : fréquence de flash ≤ 3 Hz. *Priorité :* MUST.

**EF-CLIMA-08** — Toute météo et toute catastrophe est signalée par un **son, une icône et un texte** en plus de la couleur, et une option « intempéries douces » réduit les effets d'écran **sans changer les règles**. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6`. *Critère d'acceptation :* en mode daltonien et sans son, le joueur identifie la météo ; avec « intempéries douces », les effets de jeu restent identiques. *Priorité :* MUST.

**EF-CLIMA-09** — La chute de météore peut être déclenchée par un vote des spectateurs ou, à défaut, une fois sur huit à la graine ; elle creuse un cratère de 7 × 7 cellules devenant un lac au saut suivant, et ce qui s'y trouvait gagne +40 de Ferveur. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §5.1`, `12_SCENARIOS.md §5`, `data/tuning.json` (`disasters.meteor`). *Critère d'acceptation :* les trois conséquences sont observables et chiffrées comme dans `data/tuning.json`. *Priorité :* SHOULD.

---

## 11. MUSEE — musée, Chronique, carte-récap

**EF-MUSEE-01** — À la fin de la partie, l'équipe visite le Musée de l'an 900, **généré à partir du journal d'actions** : statues, artefacts, frise chronologique. *Source :* `GDD §3.8`. *Critère d'acceptation :* chaque pièce exposée est traçable à une entrée du journal. *Priorité :* MUST.

**EF-MUSEE-02** — Le guide ARCHIVE commente la visite avec des textes assemblés par **modèles de phrases** (25 modèles à l'Early Access, 60 visés, chacun en 2 variantes), sans aucune IA générative en jeu. *Source :* `GDD §3.8`, `§6.5`, `11_SCRIPTS_DIALOGUES.md §6`. *Critère d'acceptation :* tous les textes proviennent de `data/phrases/` ; la déclaration « contenu généré en direct » reste « Non ». *Priorité :* MUST.

**EF-MUSEE-03** — Le musée comporte une **salle des Figures**, et la Chronique raconte le Peuple, ses bifurcations et ses catastrophes. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8`, `12_SCENARIOS.md §4bis`. *Critère d'acceptation :* une partie avec une Figure majeure, une bifurcation et une catastrophe produit les trois récits correspondants. *Priorité :* SHOULD.

**EF-MUSEE-04** — Les ailes du musée apparaissent selon la richesse de la Chronique. *Source :* `21_WORLD_LEVEL_DESIGN.md §2`. *Critère d'acceptation :* une partie pauvre et une partie riche en traces n'ouvrent pas le même nombre d'ailes. *Priorité :* SHOULD.

**EF-MUSEE-05** — Les statues du musée reproduisent la pose réellement capturée par le joueur. *Source :* `40_TECHNICAL_DESIGN.md §8`, `33_VISUAL_TARGETS.md §5` (S10). *Critère d'acceptation :* la pose affichée est celle choisie au socle, et non une pose générique. *Priorité :* MUST.

**EF-MUSEE-06** — La visite se fait caméra sur rails, avec les sous-titres d'ARCHIVE, un bouton « Capturer » (mode photo) et un bouton « Marquer le moment ». *Source :* `32_UX_UI_SPEC.md §4`. *Critère d'acceptation :* les quatre éléments sont présents et fonctionnels. *Priorité :* MUST.

**EF-MUSEE-07** — Le jeu produit lui-même une **carte-récap** aux formats 1080 × 1350 et 16:9, portant le titre de la mission, les 4 avatars, la statue la plus drôle, 3 phrases de Chronique, la note et un code capsule optionnel, avec les boutons Enregistrer, Copier et Partager ; elle n'est jamais le produit d'un montage externe. *Source :* `32_UX_UI_SPEC.md §4`, `33_VISUAL_TARGETS.md §5` (S11). *Critère d'acceptation :* les deux formats sont écrits par le jeu en fin de partie et contiennent les six éléments. *Priorité :* MUST.

**EF-MUSEE-08** — Le jeu pose des marqueurs d'enregistrement aux moments forts pour l'outil d'enregistrement de la plateforme. *Source :* `GDD §3.8`, `32_UX_UI_SPEC.md §4`. *Critère d'acceptation :* au moins un marqueur est posé par partie contenant un moment fort identifié. *Priorité :* SHOULD.

**EF-MUSEE-09** — En cas d'Effondrement, le musée affiche « Cette aile est fermée pour cause d'Effondrement » et l'aile correspondante est inaccessible. *Source :* `51_QA_TEST_PLAN.md §3`, `11_SCRIPTS_DIALOGUES.md §6` (CHR_COLLAPSE_01). *Critère d'acceptation :* le message exact s'affiche et l'aile est fermée. *Priorité :* MUST.

**EF-MUSEE-10** — ***À trancher :*** le dossier ne dit pas si la caméra sur rails du musée peut provoquer du mal des transports, ni si le texte de la Chronique reste affiché assez longtemps pour une lecture lente. *Source :* `docs/reviews/2026-10-07-revue-joueur.md §5` (confort) ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir ; l'option « caméra stable » de `32 §6` est le candidat naturel. *Priorité :* SHOULD.

---

## 12. MODES — modes de jeu

**EF-MODES-01** — Le mode **Coop Contrat** accueille 1 à 4 joueurs, un par époque. *Source :* `GDD §3.1`. *Critère d'acceptation :* les quatre effectifs sont jouables selon l'allocation de EF-APPAR-03. *Priorité :* MUST.

**EF-MODES-02** — Le mode **Saboteur du Temps** se joue à 4 : un joueur reçoit secrètement pour mission de provoquer l'Effondrement sans être démasqué, et dispose de la Clé à paradoxe (+20, cooldown 60 s, 3 charges). *Source :* `GDD §3.1`, `12_SCENARIOS.md §8`, `data/tuning.json` (`paradox.saboteur_*`). *Critère d'acceptation :* le rôle n'est révélé à aucun autre client, y compris dans les paquets réseau ; les trois paramètres sont lus dans `data/tuning.json`. *Priorité :* SHOULD.

**EF-MODES-03** — En mode Saboteur, chaque pause café ouvre un vote de 20 s ; une accusation erronée fait perdre 10 points de paradoxe à l'équipe. Le Saboteur gagne sur un Effondrement ; l'équipe gagne avec un contrat à ≥ 3 étoiles ou si le Saboteur est rapatrié. *Source :* `12_SCENARIOS.md §8`, `20_GAME_DESIGN_PARAMETERS.md §5`. *Critère d'acceptation :* les trois conditions de victoire sont distinguées et appliquées. *Priorité :* SHOULD.

**EF-MODES-04** — Le mode **Solo Relais** enchaîne E0, E1, E2 puis E3 en 4 manches de 240 s, avec des dangers réduits de 30 %, le même barème de score, et sert de tutoriel. *Source :* `12_SCENARIOS.md §6`, `20_GAME_DESIGN_PARAMETERS.md §1`, `data/tuning.json` (`hazards.solo_hazard_mult`). *Critère d'acceptation :* le joueur hérite de ses propres traces à chaque manche ; le multiplicateur vaut 0,7. *Priorité :* MUST. *Incohérence relevée :* 4 × 240 s = 16 min de manches seules, alors que `12 §6` annonce 12-16 minutes au total, musée non compris (`docs/backlog.md`).

**EF-MODES-05** — Le mode **Capsule asynchrone** produit un code partageable contenant la graine et le journal, de 300 à 1 500 caractères environ, qu'un autre joueur charge pour jouer l'époque suivante ; une **Capsule mystère** hebdomadaire reprend le même mécanisme avec une graine mondiale. *Source :* `12_SCENARIOS.md §7`, `40_TECHNICAL_DESIGN.md §8`, `71_LIVE_OPS.md §1`. *Critère d'acceptation :* charger une capsule reconstitue exactement la vallée vieillie de son auteur ; la capsule de la semaine est identique pour tous. *Priorité :* SHOULD.

**EF-MODES-06** — Un code capsule ne contient **aucune donnée personnelle** : ni pseudonyme, ni identifiant de plateforme. *Source :* `GDD §6.1`, `51_QA_TEST_PLAN.md §3`. *Critère d'acceptation :* une capsule générée par des joueurs nommés, décodée, ne contient aucun de leurs noms ni identifiants. *Priorité :* MUST.

**EF-MODES-07** — Une capsule d'une version antérieure est migrée si possible, sinon refusée avec le message CAPSULE_INVALID, sans plantage. *Source :* `12_SCENARIOS.md §4`, `11_SCRIPTS_DIALOGUES.md §11`. *Critère d'acceptation :* une capsule migrable se charge ; une capsule non migrable affiche le message. *Priorité :* MUST.

**EF-MODES-08** — ***À trancher :*** le dossier ne décrit pas comment une capsule survit à un **changement de recettes** entre deux versions, au-delà du refus. *Source :* `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir avec la décision (stratégie de migration des recettes). *Priorité :* SHOULD.

**EF-MODES-09** — Le **Défi du jour** utilise une graine mondiale quotidienne (UTC) et un contrat identique pour tous, 1 à 4 joueurs, un essai par équipe et par jour, avec classement amis et mondial, un chapeau du jour en récompense, et un score égal aux points de contrat plus la richesse du musée moins les paradoxes. *Source :* `12_SCENARIOS.md §9`. *Critère d'acceptation :* deux équipes du même jour reçoivent la même graine et le même contrat ; un second essai est refusé ; la formule de score est vérifiable. *Priorité :* SHOULD.

**EF-MODES-10** — La démo publique propose une carte et deux époques en multijoueur, et ses joueurs peuvent rejoindre des amis. *Source :* `GDD §7.1`. *Critère d'acceptation :* la démo est jouable à plusieurs et accepte une invitation venue de la version complète. *Priorité :* MUST.

**EF-MODES-11** — ***À trancher :*** une **vallée d'équipe persistante** (chaque partie y dépose définitivement ses traces) est proposée comme réponse à la contradiction entre le thème du jeu et la remise à zéro de chaque partie. Non décidée. *Source :* `docs/reviews/2026-10-07-revue-joueur.md §2` (M6) ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir avec la décision. *Priorité :* COULD.

**EF-MODES-12** — ***À trancher :*** la valeur solo d'un jeu à 19,99 € n'est pas arbitrée : soit elle est assumée explicitement sur la page de vente, soit le Défi du jour devient une colonne vertébrale solo (progression, classement, objectifs hebdomadaires). *Source :* `docs/reviews/2026-10-07-revue-joueur.md §2` (M8) ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir avec la décision. *Priorité :* SHOULD.

---

## 13. COMM — voix, pings, emotes, fantômes

**EF-COMM-01** — Le micro n'est **jamais obligatoire** : la roue de pings, les emotes et le texte rapide permettent de jouer et de finir une partie sans parler. *Source :* `GDD §3.2`, `§6.3`, `20_GAME_DESIGN_PARAMETERS.md §9`. *Critère d'acceptation :* une partie complète est terminable sans aucun micro (`51 §9`). *Priorité :* MUST.

**EF-COMM-02** — La voix de proximité **inter-époques** est claire jusqu'à 8 m, filtrée en passe-bas 1,2 kHz et atténuée de 9 dB entre 8 et 25 m, puis passée en « radio ancienne » (passe-bande 400-2 500 Hz, −15 dB) au-delà ; dans la même époque, l'atténuation 3D standard porte sur 30 m. *Source :* `20_GAME_DESIGN_PARAMETERS.md §9`, `data/tuning.json` (`voice`), `31_AUDIO_DESIGN.md §4`. *Critère d'acceptation :* les quatre régimes sont mesurables au spectre et les seuils viennent de `data/tuning.json`. *Priorité :* SHOULD.

**EF-COMM-03** — La détection de voix se déclenche à −45 dBFS, l'appui pour parler est disponible en option, et la musique est atténuée de 6 dB pendant une prise de parole. *Source :* `20_GAME_DESIGN_PARAMETERS.md §9`, `31_AUDIO_DESIGN.md §4`. *Critère d'acceptation :* les trois valeurs sont lues dans `data/tuning.json` et mesurables. *Priorité :* SHOULD.

**EF-COMM-04** — Une roue de 6 pings (ici, danger, objet, eau, aide, bravo) est visible **dans toutes les époques** pendant 8 s, à raison de 2 pings par seconde au maximum. *Source :* `20_GAME_DESIGN_PARAMETERS.md §9`, `GDD §3.2`, `data/tuning.json` (`ping`). *Critère d'acceptation :* un ping posé en E0 est visible en E1, E2 et E3 pendant 8 s. *Priorité :* MUST.

**EF-COMM-05** — Le jeu propose 8 emotes et 12 phrases de texte rapide localisées. *Source :* `20_GAME_DESIGN_PARAMETERS.md §9`. *Critère d'acceptation :* les 20 éléments existent et sont traduits dans toutes les langues de l'Early Access. *Priorité :* MUST.

**EF-COMM-06** — Les joueurs des autres époques sont visibles en **silhouette fantôme** translucide, teintée de la couleur de leur époque, avec icône d'époque et motif d'accessibilité ; l'amplitude vocale anime la bouche sur trois états. *Source :* `GDD §3.2`, `32_UX_UI_SPEC.md §3`, `33_VISUAL_TARGETS.md §1`, `20_GAME_DESIGN_PARAMETERS.md §9`. *Critère d'acceptation :* un joueur identifie l'époque d'un fantôme sans la couleur ; les trois états de bouche sont observables. *Priorité :* MUST.

**EF-COMM-07** — Le mute et le blocage d'un joueur s'obtiennent en un clic depuis le HUD ou le menu de pause. *Source :* `32_UX_UI_SPEC.md §6`, `GDD §6.2`. *Critère d'acceptation :* un clic suffit ; l'effet est immédiat. *Priorité :* MUST.

**EF-COMM-08** — Le seul texte libre saisissable par un joueur est le nom d'une statue, limité à 16 caractères et filtré. *Source :* `40_TECHNICAL_DESIGN.md §6`, `12_SCENARIOS.md §5`. *Critère d'acceptation :* aucun autre champ de texte libre n'existe ; un nom de 17 caractères est refusé ; un terme filtré est rejeté. *Priorité :* MUST.

**EF-COMM-09** — Les PNJ parlent en charabia synthétique sous-titré, sans imiter aucune langue réelle. *Source :* `31_AUDIO_DESIGN.md §3`, `11_SCRIPTS_DIALOGUES.md` (en-tête). *Critère d'acceptation :* aucun doublage dans aucune langue ; chaque réplique a son sous-titre localisé. *Priorité :* MUST.

---

## 14. STREAM — mode streamer

**EF-STREAM-01** — Le mode « Spectateurs du Temps » est **désactivé par défaut**, activé explicitement par le streamer, et la lecture du chat est **anonyme et en lecture seule**, sans authentification obligatoire du spectateur. *Source :* `40_TECHNICAL_DESIGN.md §9`, `GDD §3.9`, `60_LEGAL_COMPLIANCE.md §10`. *Critère d'acceptation :* profil vierge : aucune connexion au service de chat ; aucun spectateur n'a besoin de se connecter pour voter. *Priorité :* SHOULD.

**EF-STREAM-02** — **Rien n'est stocké** : ni pseudonyme, ni message, ni historique de vote. *Source :* `GDD §3.9`, `12_SCENARIOS.md §5`, `60_LEGAL_COMPLIANCE.md §2`. *Critère d'acceptation :* après une session de streaming, aucun fichier du dossier utilisateur ne contient un pseudonyme ni un message de chat. *Priorité :* MUST.

**EF-STREAM-03** — Les spectateurs nomment la prochaine statue par commande de chat, avec filtre de mots et longueur limitée à 16 caractères ; le même filtre s'applique aux noms de Figures. *Source :* `12_SCENARIOS.md §5`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8`. *Critère d'acceptation :* un nom filtré ou trop long est ignoré sans affichage. *Priorité :* SHOULD.

**EF-STREAM-04** — À la pause café, les spectateurs votent entre trois événements (météore, pluie, mammouth) ou la météo, et le résultat est annoncé en jeu. *Source :* `12_SCENARIOS.md §5`, `GDD §3.9`, `11_SCRIPTS_DIALOGUES.md §11` (STREAM_VOTE_*). *Critère d'acceptation :* le vote tient dans le segment prévu de la pause café et l'événement élu s'applique. *Priorité :* SHOULD.

**EF-STREAM-05** — Une file « Prochains intérimaires » permet aux spectateurs possédant le jeu de rejoindre, avec rotation automatique entre parties et 4 joueurs au maximum ; un overlay optionnel « Chronique en direct » affiche les phrases d'ARCHIVE au fil de la partie. *Source :* `12_SCENARIOS.md §5`. *Critère d'acceptation :* la file tourne sans intervention du streamer et ne dépasse jamais 4 joueurs ; l'overlay s'active et se désactive sans quitter la partie. *Priorité :* COULD.

**EF-STREAM-06** — Le mode streamer masque les codes d'invitation à l'écran, filtre les pseudonymes, et n'utilise qu'une musique 100 % originale (ou CC0 auditée) déclarée sans risque de réclamation. *Source :* `GDD §3.9`, `31_AUDIO_DESIGN.md` (en-tête), `60_LEGAL_COMPLIANCE.md §10`. *Critère d'acceptation :* aucun code lisible dans une capture ; la bande sonore est intégralement originale ou CC0 auditée. *Priorité :* MUST.

**EF-STREAM-07** — ***À trancher :*** les noms votés par le chat sont du contenu créé par des tiers et affiché à tous les joueurs ; le dossier ne dit pas si le filtre de mots suffit, ni **qui modère un signalement en direct**. *Source :* `docs/reviews/2026-10-07-revue-joueur.md §5` (modération) ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir avec la décision, en cohérence avec le document de modération du corpus `legal/`. *Priorité :* MUST.

---

## 15. PROGR — progression et boutique Chronos

**EF-PROGR-01** — La monnaie Chronos s'obtient **uniquement** en jouant des contrats ; il n'existe aucune microtransaction, aucune loot box, aucun pass payant et aucun achat réel au lancement. *Source :* `GDD §3.10`, `§7.1`, `20_GAME_DESIGN_PARAMETERS.md §10`, `71_LIVE_OPS.md §5`. *Critère d'acceptation :* aucun point d'achat réel n'existe dans le jeu ; aucun contenu n'est obtenu par tirage aléatoire payant. *Priorité :* MUST.

**EF-PROGR-02** — Cinq rangs jalonnent la progression aux seuils 0, 200, 800, 2 000 et 5 000 Chronos cumulés, débloquant chapitres et cosmétiques, et l'Early Access propose 24 chapeaux, 12 couleurs, 8 emotes et 6 poses supplémentaires de 50 à 400 Chronos. *Source :* `20_GAME_DESIGN_PARAMETERS.md §10`, `data/tuning.json` (`progression.ranks`). *Critère d'acceptation :* les seuils sont lus dans `data/tuning.json` ; le compte des cosmétiques et leurs prix correspondent à la source. *Priorité :* MUST.

**EF-PROGR-03** — Les outils sont débloqués par chapitre puis achetés en Chronos aux prix de `20 §7` ; un outil d'un chapitre non atteint n'est pas achetable. *Source :* `20_GAME_DESIGN_PARAMETERS.md §7`, `data/tuning.json` (`tools`). *Critère d'acceptation :* l'achat est refusé tant que le chapitre n'est pas atteint. *Priorité :* MUST.

**EF-PROGR-04** — Les rangs débloquent aussi des **Serments d'agence**, c'est-à-dire des modificateurs de lobby, et pas seulement des cosmétiques. *Source :* `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8`. *Critère d'acceptation :* au moins un modificateur de lobby est verrouillé derrière un rang. *Priorité :* SHOULD.

**EF-PROGR-05** — L'arc narratif compte 5 chapitres, chacun formé de 3 à 4 contrats, d'un outil débloqué et d'une cinématique courte de 20 s au maximum, et il reste **optionnel** : le jeu est jouable sans le suivre. *Source :* `10_NARRATIVE_BIBLE.md §7`. *Critère d'acceptation :* les cinq chapitres existent avec leur contenu, aucune cinématique ne dépasse 20 s, et une partie libre est jouable sans progression de chapitre. *Priorité :* SHOULD.

**EF-PROGR-06** — ***À trancher :*** la progression n'a presque pas d'effet sur la façon de jouer après le rang « Chef d'équipe » ; la revue propose des outils mutuellement exclusifs (3 emportés sur 7) ou des variantes débloquées par l'usage. Non décidé. *Source :* `docs/reviews/2026-10-07-revue-joueur.md §2` (M7) ; point ouvert dans `docs/backlog.md` (statut « partiel »). *Critère d'acceptation :* à définir avec la décision. *Priorité :* SHOULD.

---

## 16. OPT — options et accessibilité

**EF-OPT-01** — Les six catégories d'options d'accessibilité de `32 §6` (Vision, Audio, Moteur, Cognitif, Photosensibilité, Social) sont **toutes présentes et fonctionnelles**. *Source :* `32_UX_UI_SPEC.md §6`, `51_QA_TEST_PLAN.md §9`. *Critère d'acceptation :* checklist d'accessibilité verte : chaque option du tableau existe et produit son effet. *Priorité :* MUST.

**EF-OPT-02** — Vision : taille de texte réglable de 100 à 200 %, contraste élevé, motifs de fantômes, indicateurs d'époque par forme, contour renforcé, désactivation du smog visuel (remplacé par une bordure d'écran), réduction du bloom et des néons. *Source :* `32_UX_UI_SPEC.md §6`. *Critère d'acceptation :* à 200 %, aucun écran ne tronque son texte (`51 §8`). *Priorité :* MUST.

**EF-OPT-03** — Audio : sous-titres de tous les dialogues (taille et fond réglables), sous-titres des sons importants, sortie mono, volumes par bus, visualisation des voix. *Source :* `32_UX_UI_SPEC.md §6`, `GDD §6.3`, `31_AUDIO_DESIGN.md §5`. *Critère d'acceptation :* la partie est terminable sans aucun son (`51 §9`). *Priorité :* MUST.

**EF-OPT-04** — Moteur et cognitif : caméra stable, assistance de visée, maintien converti en basculement, tempo réduit, vibrations activables, rappel permanent de l'objectif, flèche vers l'objectif, tutoriel rejouable, manche de 7 minutes. *Source :* `32_UX_UI_SPEC.md §6`, `20_GAME_DESIGN_PARAMETERS.md §12`. *Critère d'acceptation :* les neuf options sont présentes et effectives ; la durée de 420 s est sélectionnable au lobby. *Priorité :* MUST.

**EF-OPT-05** — Photosensibilité : une option « réduire les clignotements » rend le glitch et les Chronomites sans flash et adoucit les transitions. *Source :* `32_UX_UI_SPEC.md §6`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6`. *Critère d'acceptation :* avec l'option active, aucun flash n'est émis par le glitch, les Chronomites, l'orage, le météore ni la Résonance. *Priorité :* MUST.

**EF-OPT-06** — Social : micro jamais requis, texte rapide, blocage et mute en un clic, mode « amis seulement » par défaut. *Source :* `32_UX_UI_SPEC.md §6`, `GDD §6.2`. *Critère d'acceptation :* les quatre garanties sont vérifiables sur un profil vierge. *Priorité :* MUST.

**EF-OPT-07** — Les époques se distinguent **aussi** par les formes et les icônes, jamais par la couleur seule, frise des peuples comprise, et le smog ne masque jamais le HUD ni les pings. *Source :* `GDD §6.3`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6`, `21_WORLD_LEVEL_DESIGN.md §10`. *Critère d'acceptation :* la partie est terminable en mode daltonien (`51 §9`) ; smog au maximum, HUD et pings restent lisibles. *Priorité :* MUST.

**EF-OPT-08** — ***À trancher :*** le dossier ne dit pas si la cinématique de pause café (les siècles qui défilent) est couverte par le mode « réduire les clignotements ». *Source :* `docs/reviews/2026-10-07-revue-joueur.md §5` (confort) ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir ; par cohérence avec EF-CLIMA-07, la limite de 3 Hz devrait s'y appliquer. *Priorité :* MUST.

---

## 17. SAUV — sauvegarde et reprise

**EF-SAUV-01** — La progression (Chronos, déblocages, réglages) est sauvegardée et synchronisée par le nuage de la plateforme jusqu'à suppression par le joueur, et le jeu ne requiert **aucun compte propre** ni serveur propriétaire. *Source :* `60_LEGAL_COMPLIANCE.md §2`, `71_LIVE_OPS.md §6`. *Critère d'acceptation :* la progression est retrouvée sur une seconde machine liée au même compte ; une partie est lançable sans aucun service propre à l'éditeur. *Priorité :* MUST.

**EF-SAUV-02** — Un mode en réseau local est conservé, de sorte que le jeu reste jouable en fin de vie. *Source :* `71_LIVE_OPS.md §6`, `40_TECHNICAL_DESIGN.md §6`. *Critère d'acceptation :* une partie à plusieurs est jouable sur un réseau local sans service en ligne. *Priorité :* MUST.

**EF-SAUV-03** — Le journal d'actions porte un en-tête versionné (signature, version, graine, mode, nombre de joueurs) et ses migrations sont versionnées. *Source :* `40_TECHNICAL_DESIGN.md §3`. *Critère d'acceptation :* un journal d'une version antérieure est soit migré, soit refusé avec un message explicite. *Priorité :* MUST.

**EF-SAUV-04** — Lorsqu'un joueur se déconnecte, son époque devient « simulée » jusqu'à son retour, ses actions passées restant acquises ; la reconnexion est possible depuis la graine et le journal. *Source :* `12_SCENARIOS.md §4`, `51_QA_TEST_PLAN.md §5`. *Critère d'acceptation :* un client déconnecté puis reconnecté en pleine manche retrouve l'état exact de son époque. *Priorité :* MUST.

**EF-SAUV-05** — Si l'hôte quitte, la mission se termine, une prime partielle de 50 % des Chronos acquis est versée, et une **capsule de reprise** est générée et affichée à tous les joueurs. *Source :* `12_SCENARIOS.md §4`, `51_QA_TEST_PLAN.md §3`. *Critère d'acceptation :* chaque client affiche le message NET_HOST_LEFT et reçoit un code capsule valide. *Priorité :* MUST.

**EF-SAUV-06** — Les journaux techniques sont écrits dans le dossier utilisateur et ne contiennent **aucune donnée personnelle**. *Source :* `32_UX_UI_SPEC.md §7`, `GDD §6.1`. *Critère d'acceptation :* inspection après une session de 10 min : aucun pseudonyme, identifiant de plateforme, adresse IP ni fichier audio. *Priorité :* MUST.

---

## 18. LIMIT — erreurs et cas limites

Ce domaine reprend `12_SCENARIOS.md §4` et `32_UX_UI_SPEC.md §7`.

**EF-LIMIT-01** — Un joueur inactif plus de 90 s reçoit une icône « sieste », et les autres peuvent voter son rapatriement à l'unanimité ; le joueur rapatrié reçoit le message NET_KICKED. *Source :* `12_SCENARIOS.md §4`, `11_SCRIPTS_DIALOGUES.md §11`, `data/tuning.json` (`net.afk_seconds`). *Critère d'acceptation :* l'icône apparaît à 90 s ; un seul refus annule le vote ; la session se ferme proprement. *Priorité :* MUST.

**EF-LIMIT-02** — Le griefing est structurellement empêché : pas de collision entre joueurs, vote de rapatriement, et validation de **chaque** action par l'hôte (portée, cooldown, inventaire, époque). *Source :* `12_SCENARIOS.md §4`, `40_TECHNICAL_DESIGN.md §6`. *Critère d'acceptation :* aucun joueur ne peut bloquer, déplacer ni empêcher physiquement un autre. *Priorité :* MUST.

**EF-LIMIT-03** — Si deux joueurs agissent sur la même trace au même instant, l'hôte ordonne par tick puis par identifiant de joueur, et le second reçoit « Trop tard ! ». *Source :* `12_SCENARIOS.md §4`. *Critère d'acceptation :* le départage est reproductible et identique sur tous les clients. *Priorité :* MUST.

**EF-LIMIT-04** — Un objet atteignant le bord de la carte est arrêté par un mur invisible (« Lisière du Bail ») accompagné d'une réplique. *Source :* `12_SCENARIOS.md §4`, `10_NARRATIVE_BIBLE.md §3`. *Critère d'acceptation :* aucun objet ni joueur ne sort de la vallée de 400 × 400 m. *Priorité :* MUST.

**EF-LIMIT-05** — Lorsque aucun arbre n'est possible (sol minéral), la recette produit une « graine fossile » sans résultat visible, et le sablier de poche le montre à l'avance. *Source :* `12_SCENARIOS.md §4`, `51_QA_TEST_PLAN.md §3`. *Critère d'acceptation :* rien n'apparaît aux sauts +1 et +2, l'entité fossile apparaît au saut +3, et l'aperçu du sablier l'annonce. *Priorité :* MUST.

**EF-LIMIT-06** — Les incidents réseau produisent les messages dédiés : NET_RECONNECT avec roue d'attente de 10 s puis NET_HOST_LEFT en cas d'échec ; NET_VERSION avec bouton de mise à jour si la version diffère de celle de l'hôte ; NET_LOBBY_FULL au cinquième joueur. *Source :* `32_UX_UI_SPEC.md §7`, `11_SCRIPTS_DIALOGUES.md §11`. *Critère d'acceptation :* les quatre cas sont observables sur une coupure, une version divergente et un lobby plein, sans plantage. *Priorité :* MUST.

**EF-LIMIT-07** — Les messages d'erreur affichés au joueur sont rédigés sur le ton d'Odile et **jamais techniques** ; le détail technique part dans le journal du dossier utilisateur. *Source :* `32_UX_UI_SPEC.md §7`. *Critère d'acceptation :* aucun code d'erreur, pile d'appels ni chemin de fichier n'apparaît à l'écran. *Priorité :* MUST.

**EF-LIMIT-08** — L'hôte **rejette** toute action hors de portée ou non conforme, aucune entrée n'est alors ajoutée au journal, et un client atteignant 20 rejets par minute est exclu. *Source :* `51_QA_TEST_PLAN.md §3`, `40_TECHNICAL_DESIGN.md §6`, `data/tuning.json` (`net.kick_rejects_per_minute`). *Critère d'acceptation :* une requête de ramassage émise à 10 m d'une pierre est rejetée, le journal reste inchangé, et le seuil d'exclusion est celui de `data/tuning.json`. *Priorité :* MUST.

**EF-LIMIT-09** — ***À trancher :*** le dossier ne décrit pas ce que devient la vallée d'une partie dont l'hôte a une **connexion instable** sans quitter franchement. *Source :* `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md`. *Critère d'acceptation :* à définir avec la décision. *Priorité :* SHOULD.

---

## 19. Récapitulatif

| Domaine | Exigences | Dont points ouverts (*À trancher*) |
|---|---|---|
| LANCE — lancement et consentement | 7 | 0 |
| MENU — menus, lobby, Agence | 11 | 0 |
| APPAR — appariement et invitation | 9 | 4 |
| PARTIE — déroulé et HUD | 12 | 0 |
| ACTION — actions, outils, caméra | 14 | 0 |
| VIEIL — vieillissement et recettes | 16 | 0 |
| PARAD — paradoxes | 10 | 0 |
| CONTR — contrats et score | 10 | 0 |
| PEUPL — peuples et Figures | 14 | 0 |
| CLIMA — météo, catastrophes, phénomènes | 9 | 0 |
| MUSEE — musée, Chronique, carte-récap | 10 | 1 |
| MODES — modes de jeu | 12 | 3 |
| COMM — voix, pings, emotes | 9 | 0 |
| STREAM — mode streamer | 7 | 1 |
| PROGR — progression | 6 | 1 |
| OPT — options et accessibilité | 8 | 1 |
| SAUV — sauvegarde et reprise | 6 | 0 |
| LIMIT — erreurs et cas limites | 9 | 1 |
| **Total** | **179** | **12** |

Les exigences non fonctionnelles sont dans
[`20_SPEC_TECHNIQUE_COMPLEMENTAIRE.md`](20_SPEC_TECHNIQUE_COMPLEMENTAIRE.md) ; leur vérification dans
[`30_MATRICE_EXIGENCES.md`](30_MATRICE_EXIGENCES.md).
