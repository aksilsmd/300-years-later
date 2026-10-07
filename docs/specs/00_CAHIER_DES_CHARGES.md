# 00 — Cahier des charges général

> **EN —** The contractual brief: object, scope, stakeholders, measurable success criteria, constraints, deliverables per phase, gates, acceptance rules, risks, budget and schedule — all of it traced back to the design dossier.

Propriétaire : Product Owner · v1.0 · 7 octobre 2026 · Vue contractuelle, **non normative pour la
conception** (voir [`README.md`](README.md) §2).

---

## 1. Contexte et objet

### 1.1 Objet du marché
Concevoir, développer, tester, mettre en conformité et publier **un jeu vidéo coopératif en ligne 3D
réaliste** pour PC Windows, distribué sur Steam en Early Access : jusqu'à quatre joueurs occupent
simultanément quatre siècles (an 0, an 300, an 600, an 900) d'une même vallée fictive, et tout ce qu'un
joueur laisse dans son époque **vieillit de façon déterministe** et réapparaît transformé chez les autres.

Nom de code **CENTURY TEMPS**, titre public de travail **Afterloom** (à valider juridiquement).
*Source :* `docs/design/00_README_INDEX.md`, `GDD_CENTURY_TEMPS.md` §0.

### 1.2 Contexte de marché, en une ligne
Le marché PC 2026 est en surproduction (17 200 sorties, revenu médian ≈ 1 728 $, 84,6 % des revenus captés
par le top 1 %) ; le créneau retenu est l'intersection non occupée entre le **coop social** et la
**profondeur sandbox**. *Source :* `GDD_CENTURY_TEMPS.md` §1.1 à §1.4.

### 1.3 Écart stratégique assumé
Le dossier retient le coop social et la lisibilité en trois secondes, mais **contredit volontairement** deux
facteurs communs aux succès analysés (prix ≤ 10 €, graphismes modestes) en choisissant le photoréalisme
Unreal Engine 5.8 et un prix indicatif de 19,99 €. Ce choix est écrit, motivé et **réévalué à la porte G3**,
wishlists en main. *Source :* `GDD_CENTURY_TEMPS.md` §0 (encadré), ADR 0012, §7.3.

### 1.4 Nature particulière de ce marché
L'exécutant principal du code est une **IA de code supervisée** (Claude Code), encadrée par un contrat
d'agent écrit ([`AGENTS.md`](../../AGENTS.md)) et huit procédures (`.claude/skills/`). Les éléments
artistiques organiques et les décisions irréversibles restent humains (§3). Ce cahier des charges engage donc
autant la **méthode de preuve** (§8) que le résultat.

---

## 2. Périmètre

### 2.1 Inclus
| # | Inclus dans le périmètre Early Access | Source |
|---|---|---|
| I01 | Moteur de vieillissement déterministe : graine + journal d'actions + recettes, 1 à 3 sauts d'époque | `GDD` §3.3, `40_TECHNICAL_DESIGN.md` §1-§4 |
| I02 | Quatre époques d'une vallée unique de 400 × 400 m, grille de 2 m, terrain et eau modifiables | `20_GAME_DESIGN_PARAMETERS.md` §3, `21_WORLD_LEVEL_DESIGN.md` §2 |
| I03 | Multijoueur 1 à 4 joueurs, hôte autoritaire en listen server, sessions Steam | `40` §6 |
| I04 | 5 modes : Coop Contrat, Saboteur du Temps, Solo Relais, Capsule asynchrone, Défi du jour | `GDD` §3.1 |
| I05 | 30 recettes de vieillissement et 12 contrats de référence à l'Early Access | `GDD` §3.3, `12_SCENARIOS.md` §2 |
| I06 | Peuples (9 civilisations d'arrivée), Figures, Porte-Voix, Serments, météo, catastrophes, phénomènes | `13_PEUPLES_DIEUX_ET_PHENOMENES.md` |
| I07 | Paradoxes (non-conformités), Chronomites, Effondrement | `20` §5 |
| I08 | Machine à clips : statues de pose, Musée de l'an 900, Chronique par modèles de phrases, carte-récap | `GDD` §3.8 |
| I09 | Voix de proximité inter-époques, roue de pings, emotes, texte rapide | `20` §9 |
| I10 | Mode streamer « Spectateurs du Temps » (lecture anonyme du chat, votes, noms de statues) | `GDD` §3.9 |
| I11 | Progression, monnaie in-game Chronos, cosmétiques, 5 chapitres narratifs | `20` §10, `10_NARRATIVE_BIBLE.md` §7 |
| I12 | Accessibilité étendue (6 catégories d'options) et localisation FR, EN, ES, PT-BR, DE, RU, ZH-Hans, JA | `32_UX_UI_SPEC.md` §6, `70_MARKETING_GTM.md` §3 |
| I13 | Conformité : RGPD, mineurs, DSA, accessibilité, licences, transparence IA, classification d'âge | `60_LEGAL_COMPLIANCE.md`, [`legal/README.md`](../../legal/README.md) |
| I14 | Démo multijoueur (1 carte, 2 époques) pour un Steam Next Fest | `GDD` §7.1 |
| I15 | Médias produits **dans le moteur** (12 plans de `33_VISUAL_TARGETS.md` §5), trailers, page Steam, landing page sans traceur | `33` §5-§6, `70` §3-§4 |

### 2.2 Explicitement exclu
| # | Hors périmètre | Raison et source |
|---|---|---|
| E01 | Toute plateforme autre que PC Windows (consoles, mobile, Mac natif) | Cible Steam d'abord ; IARC seulement « si sortie consoles » — `GDD` §6.2, §7.1 |
| E02 | Free-to-play, publicité, microtransactions, loot box, pass payant | Interdit par le modèle et par l'éthique — `GDD` §7.1, §3.10, `71_LIVE_OPS.md` §5 |
| E03 | Serveur de jeu propriétaire, compte éditeur, base de joueurs hébergée | Le jeu reste jouable sans serveur propriétaire — `71` §6 |
| E04 | IA générative en temps réel dans le jeu ; tout asset livré généré par IA | `GDD` §6.5, `30_ART_BIBLE.md` §6 |
| E05 | Toute image du jeu produite hors Unreal Engine | `33` (encadré d'ouverture) |
| E06 | Toute culture, religion, marque, œuvre, personne ou période historique réelle | `10` §2, §10, `13` §0 |
| E07 | Contenu binaire sous licence Epic/Fab/Megascans/MetaHuman dans un dépôt public | `40` §12, `ARCHITECTURE.md` |
| E08 | Biome Côte, cinquième ancrage E-1, Steam Workshop, éditeur de contrats | Reportés en Saison 1 à 3 — `71` §2 |
| E09 | Analytics tiers, traceur publicitaire, cookie, CDN externe, police tierce hébergée | `GDD` §6.1, `ARCHITECTURE.md` |
| E10 | Enregistrement de la voix des joueurs, sous quelque forme que ce soit | `GDD` §6.1, `40` §7 |

### 2.3 Périmètre sacrifiable, dans l'ordre
En cas de retard, l'ordre de coupe est contractuel et **non négociable à la hausse** : biome Côte → mode
Saboteur → Défi du jour → mode Capsule → mode Streamer → voix inter-époques (les pings restent) → 2ᵉ biome de
recettes. **Jamais coupés :** moteur de vieillissement, rotation, musée, 4 joueurs en ligne, conformité.
*Source :* `50_PRODUCTION_PLAN.md` §6.

---

## 3. Parties prenantes et rôles

| Rôle | Tenu par | Responsabilité | Décide seul ? |
|---|---|---|---|
| Producteur / Product Owner | Porteur du projet (humain) | Backlog, priorités, portes, budget, planning | Oui |
| Game Director | Porteur du projet | Vision, fun, arbitrages de design | Oui |
| Lead Dev / Dev | **Claude Code, supervisé** | Code, tests, CI, ADR | Non — reversible seulement, journalisé dans `DECISIONS.md` |
| Tech Art | Claude Code (plugin MCP Unreal) | PCG, matériaux, Niagara, intégration, Python d'éditeur | Non |
| QA Lead | Porteur du projet | Plan de test, campagnes, playtests, go/no-go qualité | Oui |
| Artistes 3D / animation | Freelances | Créatures (Bouloche, chèvres, Chronomites), capture de jeu d'acteur, direction artistique finale | Non |
| Audio | Compositeur freelance (+ SFX procéduraux par l'IA) | Musique, design sonore | Non |
| Illustration | Illustrateur freelance | Capsule Steam, logo, panneaux de cinématique | Non |
| Localisation | Traducteurs freelances | Langues de l'Early Access | Non |
| Juridique / comptabilité | Professionnels externes | Validation des 22 textes, marque, structure, fiscalité | Avis liant avant G5 |
| Communauté | Porteur du projet | Discord/Stoat, réseaux, créateurs | Oui |

*Source :* `50_PRODUCTION_PLAN.md` §1, `33_VISUAL_TARGETS.md` §7, `AGENTS.md` §3.

### 3.1 Arrêts obligatoires — ce que l'IA ne fait jamais
À **tous** les niveaux d'autonomie : créer un compte, installer Unreal derrière l'identification Epic, tout
achat, toute signature, toute publication, publier un média non approuvé, fixer le prix. L'IA prépare le
dossier pour que l'humain n'ait qu'à cliquer, puis poursuit sur une autre piste.
*Source :* `AGENTS.md` §3, `ARCHITECTURE.md` (autonomie et arrêts obligatoires).

### 3.2 Contrat de sécurité (non négociable, prime sur tout le reste)
Aucune lecture hors du dépôt ; aucune donnée sortie de la machine ; aucun traceur ; aucun achat,
publication, signature ni création de compte sans l'humain ; aucun asset Epic/Fab/MetaHuman ni
`game/Content/` dans un dépôt public ; aucune image du jeu hors moteur ; aucun média publié avant
approbation humaine dans `media/APPROVALS.md` ; **aucune revendication de progrès non prouvée**.
*Source :* `AGENTS.md` §4.

---

## 4. Objectifs mesurables et critères de succès

### 4.1 Portes de décision produit (go / no-go) — seuils contractuels
| Étape | Seuil de « go » | Source |
|---|---|---|
| Prototype (M1) | 5 testeurs sur 5 rient ou s'exclament dans les 10 premières minutes | `GDD` §7.3 |
| Page Steam avant Next Fest | ≥ 7 000 wishlists | `GDD` §7.3 |
| Next Fest | ≥ 20 000 wishlists **et** temps médian de démo ≥ 20 min | `GDD` §7.3 |
| Lancement Early Access | évaluations ≥ 85 % positives | `GDD` §7.3 |

**Règle d'arrêt :** si G1 échoue deux fois après itération, la mécanique change ou le projet s'arrête, pour
un coût perdu ≤ 1 mois. *Source :* `50` §2.

### 4.2 Objectifs d'expérience, mesurables
| Objectif | Cible | Source |
|---|---|---|
| Temps jusqu'au « aha » (voir son arbre dans l'époque suivante) | < 60 s | `GDD` §3.11, `32` §2 |
| Temps jusqu'à la première graine plantée | < 30 s | `32` §9 |
| Abandon du tutoriel | < 10 % | `32` §9 |
| Durée d'une partie | 15-20 min | `20` §1 |
| Partage de la carte-récap | 15 % des parties | `32` §9 |
| Compréhension du lien entre époques (playtest, 1-5) | « je rejouerais » ≥ 4/5 à G3 | `50` §2 |
| Lisibilité des systèmes émergents | 4 testeurs sur 5 savent dire pourquoi leur Figure est née | `13` §10, `51_QA_TEST_PLAN.md` |

### 4.3 Objectifs de qualité technique
| Objectif | Cible | Source |
|---|---|---|
| Profil recommandé (RTX 3070 / RX 6800) | 1440p, 60 i/s, Lumen High | `40` §10 |
| Profil minimum (GTX 1660 Super / RX 5600 XT) | 1080p, 30-60 i/s, Lumen Medium, TSR | `40` §10 |
| Steam Deck | 800p, 30 i/s, « jouable » visé | `40` §10 |
| Tick logique hôte | 20 Hz, < 4 ms | `40` §10 |
| Propagation | p95 < 2 ms | `40` §10 |
| Bande passante | < 30 ko/s par joueur | `40` §10 |
| Couverture de tests du cœur temporel | ≥ 90 % | `50` §9 |
| Temps de CI | < 10 min | `50` §9 |
| Stabilité à G6 | 2 h de session à 4 joueurs sans plantage | `50` §2, `51` §2 |

### 4.4 Objectifs de pilotage
Vélocité stable ± 20 % ; 0 bug P0 ouvert en fin de sprint ; wishlists +100/semaine après ouverture de la
page Steam. *Source :* `50` §9.

---

## 5. Contraintes

### 5.1 Techniques
| Contrainte | Détail | Source |
|---|---|---|
| Moteur imposé | Unreal Engine 5.8, C++ `TemporalCore` pur, Blueprints pour l'assemblage, Python d'éditeur | ADR 0012, `40` §1, §13 |
| Event sourcing | Le monde est une graine + un journal d'actions + les recettes ; rien d'autre n'est autoritatif | ADR 0002, `AGENTS.md` §5.1 |
| Déterminisme strict | PCG32, entiers, conteneurs triés ; interdits : `FMath::Rand`, l'heure système, le `float`, la physique dans le cœur | `40` §4, `ARCHITECTURE.md` |
| Hôte autoritaire | Les requêtes client sont validées puis diffusées ; rien de ce qu'un client dit n'est cru | `40` §6 |
| Époque locale seule | Seul le décor et l'éclairage de l'époque du joueur sont chargés | `40` §5 |
| Zéro valeur de gameplay en dur | Tout nombre vit dans [`data/`](../../data/tuning.json) | `20` (en-tête), `AGENTS.md` §5.5 |
| Décision structurelle = ADR avant le code | `docs/adr/` ; ADR 0013 à 0020 restent à écrire en phase P0 | `40` §14, `AGENTS.md` §5.7 |
| Contenu binaire séparé | `game/Content/` en dépôt privé (Git LFS ou Perforce) | `40` §12 |
| CI | Runner **Windows auto-hébergé** avec VS 2022 et UE 5.8 installés | `40` §12 |

### 5.2 Budgétaires
Trois scénarios d'équipe, hors rémunération du porteur : **A solo + IA ≈ 40 000 – 80 000 €**,
**B studio réduit ≈ 150 000 – 300 000 €**, **C petite équipe ≈ 500 000 € – 1,2 M€**.
Ordre d'engagement des dépenses imposé : marque (avant annonce, G3) → illustrateur capsule (G3) →
compositeur (G4) → juriste (G5) → Steam Direct dès que la page est prête (G3).
Redevance Unreal Engine : 5 % au-delà de 1 M$ de revenus bruts cumulés.
*Source :* [`docs/guides/03_TEMPS_ET_COUTS.md`](../guides/03_TEMPS_ET_COUTS.md) §1-§2, `50` §7, `GDD` §7.1.

### 5.3 Calendaires
18 à 48 mois jusqu'à l'Early Access selon le scénario d'équipe. **Règle de pilotage :** un retard de plus de
25 % sur une porte déclenche une revue de périmètre (§2.3) **avant** toute rallonge budgétaire.
*Source :* `50` §3, `docs/guides/03_TEMPS_ET_COUTS.md` §1, §3.

### 5.4 Juridiques
Droit français et droit de l'Union européenne. Obligations structurantes : RGPD (minimisation, opt-in, voix
jamais enregistrée) ; art. 82 de la loi Informatique et Libertés (aucun traceur) ; RGPD art. 8 et protection
des mineurs (COPPA, Children's Code) ; DSA (signalement, point de contact — applicabilité à confirmer) ;
directive 2019/770 et principes CPC 2025 sur les monnaies virtuelles ; interdiction des loot box ;
European Accessibility Act (applicabilité aux jeux à confirmer) ; loi Toubon ; Règlement IA (UE 2024/1689)
et déclaration Steam ; CPI art. L131-3 pour les cessions de droits ; accord Steamworks, CLUF Unreal
Engine, licences Fab et MetaHuman. Les 22 textes sont des **brouillons** jusqu'à validation par un
professionnel. *Source :* [`legal/README.md`](../../legal/README.md) §2, §3, `60_LEGAL_COMPLIANCE.md`.

Deux obligations préalables à la commercialisation, à la charge du porteur : vérifier la clause
d'exclusivité et de propriété intellectuelle de son contrat de travail (G0) ; créer la structure et remplir
l'entretien fiscal Steam (G3). *Source :* `60` §1, `GDD` §6.7.

### 5.5 Ressources
Dépendance assumée à des prestataires pour ce que l'IA ne peut pas produire seule : sculpt/groom/rig des
créatures, capture faciale et corporelle, direction artistique et étalonnage, capsule Steam et logo,
musique. Chaque commande exige un contrat de cession de droits écrit. *Source :* `33` §7, `60` §7.

### 5.6 Ton, sensibilité et public
Comédie absurde bienveillante, cible PEGI 7-12 : pas d'horreur gore, aucun point de vie, les dangers
étourdissent ou confisquent mais ne tuent jamais ; les catastrophes ne sont jamais létales ; la satire vise
les institutions, jamais les croyants ni les joueurs ; vocabulaire de croyance entièrement inventé.
*Source :* `GDD` §2.1, `20` §2, `10` §2, `13` §0.

---

## 6. Livrables attendus par phase

Phases P0 à P8 du plan de production, chacune close par ses livrables. Les durées sont celles du scénario B.
*Source :* `50_PRODUCTION_PLAN.md`, `docs/guides/03_TEMPS_ET_COUTS.md` §3.

| Phase | Durée (scénario B) | Livrables attendus | Porte |
|---|---|---|---|
| **A-C** Diagnostic, installation, personnalisation | 1-2 semaines | Poste de travail conforme, titre public choisi, `studio.config.yaml` renseigné | — |
| **P0** Fondations | 2-3 semaines | Projet Unreal `TemporalValley` créé, modules C++ en place, CI sur runner Windows, ADR 0013 à 0020 écrits | — |
| **P1** Prototype du fun | 4-8 semaines | Graine → arbre jouable hors ligne, tutoriel, 5 testeurs mesurés | **G1** |
| **P2** Multijoueur | 6-10 semaines | 4 joueurs en ligne, hôte autoritaire, journal répliqué, hash de contrôle, 30 min sans désynchronisation | **G2** |
| **P3** Boucle de partie | 8-12 semaines | Partie complète 15-20 min (3 manches, pause café, rotation, évaluation), page Steam ouverte, premiers clips | **G3** |
| **P4** Monde réaliste et contenu | 6-12 mois | Vallée réaliste (Landscape, PCG, Nanite), prefabs des 30 recettes, MetaHumans, 12 contrats, dangers, peuples et Figures, météo et catastrophes | — |
| **P5** Machine à clips | 6-10 semaines | Musée généré, Chronique, carte-récap, capsules, Solo Relais | — |
| **P6** Voix, streamer, saboteur | 6-8 semaines | Voix de proximité inter-époques, mode Spectateurs du Temps, mode Saboteur, Défi du jour | **G4** |
| **P7** Conformité, accessibilité, localisation | 8-12 semaines | Toutes les options d'accessibilité, localisation FR/EN à 100 %, 22 textes juridiques relus par un professionnel, AIPD | **G5** |
| **P8** Démo et Early Access | 8-12 semaines | Démo multijoueur, build Shipping, questionnaire Steam rempli, trailers, presskit, lancement | **G6**, **G7** |

---

## 7. Jalons et portes de décision

| Porte | Objet | Critères de sortie — **tous** obligatoires | Décideur |
|---|---|---|---|
| **G0** Concept | Étude, pitch, audit | Dossier v2 validé ; contrat de travail vérifié (exclusivité / PI) | Porteur du projet |
| **G1** Prototype du fun | Graine → arbre hors ligne | 5/5 testeurs réagissent en < 10 min ; temps au « aha » < 60 s | Porteur + 5 testeurs |
| **G2** Pré-prod close | Phases P0-P2 | 4 joueurs en ligne sans désynchronisation sur 30 min ; ADR 0001-0010 écrits | Porteur du projet |
| **G3** Tranche verticale | Partie complète | Playtest 8 personnes, « je rejouerais » ≥ 4/5 ; 0 bloquant ; page Steam ouverte | Porteur du projet |
| **G4** Alpha | Toutes les fonctions | 30 recettes, 12 contrats, tous les modes ; taux de plantage < 1/heure ; voix et mode streamer fonctionnels | Porteur du projet |
| **G5** Beta | Contenu complet + conformité | Localisation FR/EN à 100 % ; checklist accessibilité verte ; textes juridiques validés par un professionnel ; 0 bloquant, ≤ 5 majeurs | Porteur + juriste |
| **G6** Release Candidate | Démo + build EA | 60 i/s sur Deck ; 2 h à 4 joueurs sans plantage ; questionnaire Steam rempli ; build approuvée par Valve | Porteur du projet |
| **G7** Gold / Lancement EA | Mise en vente | Next Fest passé ; seuils de wishlists (§4.1) atteints ; plan live ops prêt | Porteur du projet |

> **Écart relevé, non corrigé ici :** `50` §2 exige « 60 fps Deck » à G6 alors que `40` §10 fixe la cible
> Deck à « 800p 30 i/s, jouable visé », et `51` §6 écrit « 60 fps Deck » dans la scène de stress. Les trois
> chiffres ne peuvent pas être vrais ensemble. Signalé dans [`docs/backlog.md`](../backlog.md) ; la cible
> retenue par ce cahier des charges est celle de `40` §10, document normatif (§9.1 de `AGENTS.md`).

---

## 8. Modalités de recette

### 8.1 Le principe de preuve
La recette ne porte pas sur une déclaration mais sur un **fichier de preuve existant**.
[`STUDIO_STATE.md`](../../STUDIO_STATE.md) contient un bloc `yaml state` où chaque système porte un statut
(`planned` → `specified` → `implemented` → `built` → `tested` → `validated` → `released`) et un chemin
`evidence`. **Un statut ne peut pas être élevé sans que ce fichier existe** :
`python3 tools/validate_state.py` fait échouer le commit et la CI dans le cas contraire.
*Source :* `AGENTS.md` §6, `STUDIO_STATE.md`.

### 8.2 Qui valide quoi, sur quelles preuves
| Objet de la recette | Qui valide | Preuve exigée |
|---|---|---|
| Une PR de code | Product Owner | Tests verts, lint, audit de licences, clés `tr()` créées, doc ou ADR à jour, build jouée 5 min sans régression (Definition of Done, `50` §4) |
| Un système déclaré `built` | Claude Code → Product Owner | Journal de build ou fichier de run CI |
| Un système déclaré `tested` | QA Lead | Rapport de test |
| Un système déclaré `validated` | QA Lead + Product Owner | `docs/qa/<gate>.md` : périmètre, exécutés/réussis/échoués/bloqués, anomalies par sévérité, risques résiduels, recommandation go/no-go (`51` §10) |
| Une porte (G0-G7) | Porteur du projet (G5 : + juriste) | Les critères de sortie de §7, intégralement |
| Un média (image, vidéo) | Humain, nommément | Case cochée dans `media/APPROVALS.md` : identifiant, date, validateur, commentaire (`33` §8) |
| Un texte juridique | Avocat / expert-comptable | Version datée et archivée après intégration des corrections ([`legal/README.md`](../../legal/README.md) §3) |
| Le fun | 5 (G1) à 12 (G3) testeurs | Grille horodatée + questionnaire 1-5 + entretien (`51` §7) |

### 8.3 Portes automatiques avant tout commit
Sept scripts doivent passer, et chacun refuse une situation précise :
`repo_audit.py` (structure, liens internes, actions épinglées) · `validate_skills.py` ·
`validate_state.py` (preuve exigée) · `validate_data.py` (données contre schémas) ·
`privacy_scan.py` (donnée personnelle, secret, traceur) · `license_audit.py` ·
`check_media_approvals.py` (aucun média non approuvé référencé).
*Source :* `AGENTS.md` §6, `ARCHITECTURE.md` (les portes).

### 8.4 Critères de sortie des campagnes de test
- **Fin de phase :** 100 % des cas P0/P1 exécutés, 0 anomalie S1 ouverte, ≤ 3 S2 avec contournement, taux de
  réussite ≥ 95 %.
- **G6 :** 0 S1, 0 S2, ≤ 10 S3 ; 2 h de session à 4 joueurs sans plantage ; performance conforme.
*Source :* `51` §2.

### 8.5 Rapport de non-conformité
Un échec se rapporte comme un échec : la commande lancée est nommée et sa sortie est citée. Aucune
revendication de progrès sans preuve. *Source :* `AGENTS.md` §4.7, §6.

---

## 9. Hypothèses et risques majeurs

### 9.1 Hypothèses dont dépend le cahier des charges
| # | Hypothèse | Si elle tombe |
|---|---|---|
| H1 | Le contrat de travail du porteur n'interdit pas l'activité (clause d'exclusivité / PI) | Projet bloqué avant G3 — vérification exigée dès G0 (`60` §1) |
| H2 | Le titre public est disponible en classes 9 et 41 | Renommage avant annonce (`60` §7) |
| H3 | La lecture anonyme du chat Twitch reste autorisée | Repli EventSub OAuth opt-in, puis coupe du mode streamer (R16, `52_RISK_REGISTER.md`) |
| H4 | Le réalisme Unreal tient dans les budgets des trois profils | Scalabilité, Lumen Medium, coupe de périmètre (R05) |
| H5 | Une IA de code supervisée peut mener un projet Unreal C++ de cette taille | Plugin MCP officiel, petites PR, revue humaine (R04) |
| H6 | Les prestataires livrent dans les délais contractuels | Placeholders procéduraux, jalons contractuels (R17) |
| H7 | Les seuils de wishlists de §4.1 sont atteignables avec le plan marketing prévu | Réévaluation du projet à G3 (`GDD` §7.3) |

### 9.2 Risques majeurs (criticité ≥ 15)
| ID | Risque | C | Réponse |
|---|---|---|---|
| R14 | Visibilité insuffisante (wishlists) | 20 | Clips hebdomadaires dès G3, créateurs, Next Fest, capsule professionnelle |
| R19 | Budget du réalisme sous-estimé (assets, artistes, capture) | 20 | Budget par porte, achats après G3, coupe de périmètre |
| R06 | Dérive du périmètre | 16 | Ordre de coupe, Definition of Ready, phases verrouillées |
| R07 | Manque de temps (projet à temps partiel) | 16 | Calendrier avec 20 % de marge, sprints réalistes |
| R01 | Le cœur n'est pas assez drôle | 15 | Porte G1 stricte, 2 itérations maximum puis pivot |
| R03 | Désynchronisation réseau | 15 | Event sourcing, hash toutes les 5 s, golden tests, resynchronisation |

Registre complet, avec probabilité, impact, propriétaire et déclencheur : `52_RISK_REGISTER.md` (21 risques).

### 9.3 Faiblesses connues du produit, assumées et non masquées
Issues de [`docs/reviews/2026-10-07-revue-joueur.md`](../reviews/2026-10-07-revue-joueur.md) et suivies dans
[`docs/backlog.md`](../backlog.md). Trois restent **ouvertes** et conditionnent la valeur perçue :
- **M4** — l'aval (an 900) n'a presque aucune prise sur l'amont : un seul objet par manche via la cabine
  temporelle. Asymétrie d'agentivité dans un coop. *À trancher.*
- **M6** — la vallée est remise à zéro à chaque partie, alors que le thème du jeu est la trace.
  Proposition d'une vallée d'équipe persistante. *À trancher.*
- **M8** — la valeur solo d'un jeu à 19,99 € : soit l'assumer sur la page Steam, soit faire du Défi du jour
  une vraie colonne vertébrale solo. *À trancher.*

Quatre ont été traitées depuis (M1 recettes croisées, M2 variété par bifurcation des peuples, M3 carnet et
Panthéon, M5 enjeu de perte par les Figures et les catastrophes) et une partiellement (M7 progression).

---

## 10. Budget et délais

Ce cahier des charges **ne chiffre pas** : il renvoie aux trois scénarios de
[`docs/guides/03_TEMPS_ET_COUTS.md`](../guides/03_TEMPS_ET_COUTS.md), qui sont des ordres de grandeur au
7 octobre 2026 et doivent être remesurés à chaque porte.

| | A — Solo + IA | B — Studio réduit | C — Petite équipe |
|---|---|---|---|
| Composition | Porteur à temps partiel + IA + freelances ponctuels | Porteur à plein temps + 2-3 freelances réguliers | 5-8 personnes + IA |
| Durée jusqu'à l'Early Access | 30-48 mois | 18-30 mois | 15-24 mois |
| Budget hors rémunération du porteur | ≈ 40 000 – 80 000 € | ≈ 150 000 – 300 000 € | ≈ 500 000 € – 1,2 M€ |
| Risque principal | Durée et périmètre | Trésorerie | Coût fixe mensuel |

Postes détaillés (assets Fab, créatures, capture, musique, localisation ≈ 15 000 mots × 7 langues,
juridique, marque, Steam Direct ≈ 100 $, QA externe, marketing, abonnement à l'assistant IA) : même document
§2. Aides françaises à étudier : crédit d'impôt jeu vidéo, fonds d'aide du CNC, Bpifrance, aides régionales.

**Ce qui fait exploser les estimations**, et que ce cahier des charges verrouille donc par §2.3 et §5.3 : le
périmètre (une époque, un biome ou un mode en plus), la qualité des humains réalistes, la capture de
mouvement, une localisation tardive, l'absence de playtests tôt.

---

## 11. Ce que ce document ne fait pas

Il ne remplace ni le dossier de conception, ni un avis juridique, ni un devis. Il n'autorise aucune dépense
et ne fixe aucun prix de vente : le prix est un arrêt obligatoire humain (§3.1). Les exigences détaillées
sont dans [`10_SPEC_FONCTIONNELLE.md`](10_SPEC_FONCTIONNELLE.md) et
[`20_SPEC_TECHNIQUE_COMPLEMENTAIRE.md`](20_SPEC_TECHNIQUE_COMPLEMENTAIRE.md) ; leur vérification est dans
[`30_MATRICE_EXIGENCES.md`](30_MATRICE_EXIGENCES.md).
