# 30 — Matrice de traçabilité des exigences

> **EN —** One traceability table: every requirement, its source in the design dossier, the real test family or tool that verifies it, and its status — plus an honest list of what nothing verifies yet.

Propriétaire : QA Lead · v1.0 · 7 octobre 2026

Cette matrice relie chacune des **272 exigences** de [`10_SPEC_FONCTIONNELLE.md`](10_SPEC_FONCTIONNELLE.md)
(179 exigences fonctionnelles) et de
[`20_SPEC_TECHNIQUE_COMPLEMENTAIRE.md`](20_SPEC_TECHNIQUE_COMPLEMENTAIRE.md) (93 exigences non
fonctionnelles) à sa source et à son **moyen de vérification réel**.

## 1. Règles de lecture

- **Source** — la section de `docs/design/` ou de `data/` qui porte la décision. Les noms `NN_*.md`
  désignent `docs/design/NN_*.md` ; `GDD` désigne `docs/design/GDD_CENTURY_TEMPS.md`.
- **Vérifiée par** — une **famille de test existante** de [`51_QA_TEST_PLAN.md`](../design/51_QA_TEST_PLAN.md)
  (§1 pour la stratégie, §3 pour les cas Gherkin, §4 pour la matrice de configuration, §5 pour le réseau,
  §6 pour la performance, §7 pour le playtest, §8 pour la localisation, §9 pour les checklists de
  conformité, et le tableau final consacré à `13_PEUPLES_DIEUX_ET_PHENOMENES.md`) **ou** un script réel de
  `tools/`. Aucun nom de test n'est inventé. Un tiret (**—**) signifie qu'**aucun** moyen de vérification
  existant ne couvre l'exigence : ces 37 cas sont listés en §4.
- **Statut** — `spécifié` pour **toutes** les exigences, sans exception. Le jeu n'existe pas : `game/` est
  créé en phase P0, et [`STUDIO_STATE.md`](../../STUDIO_STATE.md) ne connaît aujourd'hui aucun système
  au-delà de `specified`. Un statut ne pourra être élevé qu'avec un fichier de preuve, ce que
  `python3 tools/validate_state.py` impose.

## 2. Répartition des moyens de vérification

| Moyen de vérification | Exigences |
|---|---|
| Conformité — checklists (`51 §1`, `§9`) | 44 |
| Functional Tests (`51 §1`) | 39 |
| **Aucun (voir §4)** | **37** |
| Gherkin système (`51 §1`, `§3`) | 36 |
| Automation Spec (`51 §1`) | 29 |
| Réseau (`51 §1`, `§5`) | 14 |
| Rendu / visuel (`51 §1`) | 11 |
| `tools/validate_data.py` | 9 |
| Localisation (`51 §1`, `§8`) | 8 |
| Performance (`51 §1`, `§6`) | 7 |
| Golden (`51 §1`) | 6 |
| Tableau `13` — photosensibilité (`51`) | 4 |
| Tableau `13` — déterminisme étendu (`51`) | 3 |
| Tableau `13` — catastrophes (`51`) | 3 |
| Tableau `13` — sensibilité, revue humaine (`51`) | 3 |
| Tableau `13` — bifurcations, serments, lisibilité (`51`) | 3 |
| Matrice de configuration (`51 §4`) | 3 |
| Gauntlet (`51 §1`) | 3 |
| `tools/license_audit.py` | 3 |
| `tools/privacy_scan.py` | 2 |
| Playtest (`51 §1`, `§7`) | 1 |
| Exploratoire (`51 §1`) | 1 |
| `tools/validate_state.py`, `tools/repo_audit.py`, `tools/check_media_approvals.py` | 3 |
| **Total** | **272** |

## 3. La matrice

| Exigence | Énoncé court | Source | Vérifiée par | Statut |
|---|---|---|---|---|
| **EF-LANCE-01** | Écran de consentement avant le menu | `32_UX_UI_SPEC.md §1`, `§2` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-LANCE-02** | Deux boutons égaux, aucune case pré-cochée | `60_LEGAL_COMPLIANCE.md §5`, `11_SCRIPTS_DIALOGUES.md §11` (PRIVACY_*) | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-LANCE-03** | Télémétrie désactivée par défaut, opt-in | `GDD §6.1`, `51_QA_TEST_PLAN.md §3`, `§9` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-LANCE-04** | Consentement modifiable et révocable | `60_LEGAL_COMPLIANCE.md §5`, `32_UX_UI_SPEC.md §1` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-LANCE-05** | Bouton « Supprimer mes données locales » | `GDD §6.1`, `51_QA_TEST_PLAN.md §9` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-LANCE-06** | Textes juridiques consultables en jeu | `32_UX_UI_SPEC.md §1`, `60_LEGAL_COMPLIANCE.md §1`, `§7` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-LANCE-07** | Tutoriel auto-lancé, « aha » avant 60 s | `32_UX_UI_SPEC.md §2`, `11_SCRIPTS_DIALOGUES.md §1` | Playtest (`51 §1`, `§7`) | spécifié |
| **EF-MENU-01** | Un bouton « JOUER », deux clics jusqu'à la partie | `32_UX_UI_SPEC.md §1`, `§2` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MENU-02** | Cinq entrées de jeu | `32_UX_UI_SPEC.md §1` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MENU-03** | Lobby : 4 cartes, époques déplaçables | `32_UX_UI_SPEC.md §4` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MENU-04** | Modificateurs de lobby lus dans `data/` | `20_GAME_DESIGN_PARAMETERS.md §12`, `data/tuning.json` (`lobby_modifiers`, `match.rotation`) | Functional Tests (`51 §1`) | spécifié |
| **EF-MENU-05** | Mode Détente | `20_GAME_DESIGN_PARAMETERS.md §12` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MENU-06** | Code d'invitation masquable | `32_UX_UI_SPEC.md §4`, `GDD §3.9` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MENU-07** | « Lancer » actif quand tous sont prêts | `32_UX_UI_SPEC.md §4` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MENU-08** | Brief de contrat, compte à rebours 15 s | `32_UX_UI_SPEC.md §4`, `11_SCRIPTS_DIALOGUES.md §3` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MENU-09** | Agence : progression, boutique, Panthéon | `32_UX_UI_SPEC.md §1`, `20_GAME_DESIGN_PARAMETERS.md §10`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MENU-10** | Menu de pause complet en ligne | `32_UX_UI_SPEC.md §1` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MENU-11** | Aucun texte codé en dur | `32_UX_UI_SPEC.md` (en-tête), `50_PRODUCTION_PLAN.md §4` (Definition of Done) | Localisation (`51 §1`, `§8`) | spécifié |
| **EF-APPAR-01** | Lobbies amis seulement par défaut | `GDD §6.2`, `32_UX_UI_SPEC.md §6` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-APPAR-02** | Invitation par overlay et par code | `32_UX_UI_SPEC.md §1`, `§2`, `40_TECHNICAL_DESIGN.md §6` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-APPAR-03** | Allocation des époques par effectif | `12_SCENARIOS.md §3` | Functional Tests (`51 §1`) | spécifié |
| **EF-APPAR-04** | Simulation déterministe des époques vides | `12_SCENARIOS.md §3`, `data/tuning.json` (`hazards.empty_era_sim`) | Golden (`51 §1`) | spécifié |
| **EF-APPAR-05** | E3 révélée et visitée à 3 joueurs | `12_SCENARIOS.md §3` | Functional Tests (`51 §1`) | spécifié |
| **EF-APPAR-06** | *Ouvert :* appariement sans amis | `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **EF-APPAR-07** | *Ouvert :* rejoindre en cours de partie | `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **EF-APPAR-08** | *Ouvert :* crossplay | `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **EF-APPAR-09** | *Ouvert :* démo multijoueur permanente | `GDD §7.1`, `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **EF-PARTIE-01** | 3 manches de 300 s, avertissements 60 s / 10 s | `20_GAME_DESIGN_PARAMETERS.md §1`, `data/tuning.json` (`match`) | Functional Tests (`51 §1`) | spécifié |
| **EF-PARTIE-02** | Pause café de 30 s en trois segments | `20_GAME_DESIGN_PARAMETERS.md §1` | Functional Tests (`51 §1`) | spécifié |
| **EF-PARTIE-03** | Rotation +1 époque par pause | `20_GAME_DESIGN_PARAMETERS.md §1`, `11_SCRIPTS_DIALOGUES.md §5` (CAFE_ROTATE) | Functional Tests (`51 §1`) | spécifié |
| **EF-PARTIE-04** | Frise des époques et annonce de rotation | `32_UX_UI_SPEC.md §4` | Rendu/visuel (`51 §1`) | spécifié |
| **EF-PARTIE-05** | Résolutions à la pause café uniquement | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §1.2`, `§5.1`, `21_WORLD_LEVEL_DESIGN.md §6` | Functional Tests (`51 §1`) | spécifié |
| **EF-PARTIE-06** | Musée 120 s, écourtable à l'unanimité | `20_GAME_DESIGN_PARAMETERS.md §1` | Functional Tests (`51 §1`) | spécifié |
| **EF-PARTIE-07** | Enchaînement des écrans d'une partie | `32_UX_UI_SPEC.md §1` | Functional Tests (`51 §1`) | spécifié |
| **EF-PARTIE-08** | HUD : époque, chrono, carte de contrat | `32_UX_UI_SPEC.md §3` | Rendu/visuel (`51 §1`) | spécifié |
| **EF-PARTIE-09** | HUD : jauge, inventaire, voix, réticule | `32_UX_UI_SPEC.md §3` | Rendu/visuel (`51 §1`) | spécifié |
| **EF-PARTIE-10** | Notifications de recette, une par 2 s | `32_UX_UI_SPEC.md §3` | Rendu/visuel (`51 §1`) | spécifié |
| **EF-PARTIE-11** | Icône d'époque des fantômes, noms sous 15 m | `32_UX_UI_SPEC.md §3` | Rendu/visuel (`51 §1`) | spécifié |
| **EF-PARTIE-12** | Musique adaptative par couches | `31_AUDIO_DESIGN.md §1.2` | — | spécifié |
| **EF-ACTION-01** | Vitesses, endurance et saut | `20_GAME_DESIGN_PARAMETERS.md §2`, `data/tuning.json` (`player`) | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-02** | Interaction 2,5 m, cône 90° | `20_GAME_DESIGN_PARAMETERS.md §2`, `40_TECHNICAL_DESIGN.md §6` | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-03** | Inventaire et objets lourds | `20_GAME_DESIGN_PARAMETERS.md §2` | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-04** | Creuser 1,5 s par cellule, planter 0,5 s | `20_GAME_DESIGN_PARAMETERS.md §2` | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-05** | Aucun point de vie, dangers non létaux | `20_GAME_DESIGN_PARAMETERS.md §2`, `GDD §2.1` | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-06** | Aucune collision entre joueurs | `20_GAME_DESIGN_PARAMETERS.md §2`, `40_TECHNICAL_DESIGN.md §5` | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-07** | Neuf outils et leurs paramètres | `20_GAME_DESIGN_PARAMETERS.md §7`, `data/tuning.json` (`tools`) | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-08** | Ancre temporelle et sablier de poche | `20_GAME_DESIGN_PARAMETERS.md §4.3` (`protected`), `§7` | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-09** | Poses prédéfinies uniquement | `33_VISUAL_TARGETS.md §3`, `60_LEGAL_COMPLIANCE.md §6` | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-10** | Caméra 3ᵉ personne et bornes de zoom | `20_GAME_DESIGN_PARAMETERS.md §11`, `data/tuning.json` (`camera`) | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-11** | Remappage complet et détection azerty | `32_UX_UI_SPEC.md §5` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-ACTION-12** | Quatre cabines, une fois par manche | `21_WORLD_LEVEL_DESIGN.md §8` | Functional Tests (`51 §1`) | spécifié |
| **EF-ACTION-13** | Terrain déformable et eau déterministe | `20_GAME_DESIGN_PARAMETERS.md §3`, `40_TECHNICAL_DESIGN.md §5` | Golden (`51 §1`) | spécifié |
| **EF-ACTION-14** | Dangers : machines à états de `20 §8` | `20_GAME_DESIGN_PARAMETERS.md §8`, `data/tuning.json` (`hazards`) | Functional Tests (`51 §1`) | spécifié |
| **EF-VIEIL-01** | Recette = fonction pure état + environnement | `GDD §3.3`, `40_TECHNICAL_DESIGN.md §1` | Automation Spec (`51 §1`) | spécifié |
| **EF-VIEIL-02** | Même graine, même monde sur tous les clients | `GDD §3.3`, `40_TECHNICAL_DESIGN.md §4` | Golden (`51 §1`) | spécifié |
| **EF-VIEIL-03** | Jamais plus de 3 sauts | `20_GAME_DESIGN_PARAMETERS.md §4.3`, `data/tuning.json` (`aging.max_hops`), `GDD §9` | Automation Spec (`51 §1`) | spécifié |
| **EF-VIEIL-04** | Étiquettes et conditions fermées | `20_GAME_DESIGN_PARAMETERS.md §4.1`, `§4.2`, `data/schemas/recipe.schema.json` | `tools/validate_data.py` | spécifié |
| **EF-VIEIL-05** | Départage par `priority`, jamais l'ordre du fichier | `20_GAME_DESIGN_PARAMETERS.md §4.3`, `data/schemas/recipe.schema.json` (`priority`) | Automation Spec (`51 §1`) | spécifié |
| **EF-VIEIL-06** | Variantes pondérées à graine indexée | `20_GAME_DESIGN_PARAMETERS.md §4.3`, `40_TECHNICAL_DESIGN.md §4` | Automation Spec (`51 §1`) | spécifié |
| **EF-VIEIL-07** | Recettes croisées (`input.with`) | `data/schemas/recipe.schema.json` (`input.with`), `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8` | Automation Spec (`51 §1`) | spécifié |
| **EF-VIEIL-08** | 30 recettes à l'Early Access | `GDD §3.3`, `71_LIVE_OPS.md §2` | `tools/validate_data.py` | spécifié |
| **EF-VIEIL-09** | Propagation instantanée, apparition 0,4 s | `20_GAME_DESIGN_PARAMETERS.md §4.4`, `31_AUDIO_DESIGN.md §2` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-VIEIL-10** | Changement de silhouette à chaque saut | `33_VISUAL_TARGETS.md §1`, `21_WORLD_LEVEL_DESIGN.md §10` | Rendu/visuel (`51 §1`) | spécifié |
| **EF-VIEIL-11** | Emplacements et variante contrariée | `21_WORLD_LEVEL_DESIGN.md §5`, `data/schemas/recipe.schema.json` (`contrary`) | Automation Spec (`51 §1`) | spécifié |
| **EF-VIEIL-12** | Budget de 2 000 traces par époque | `20_GAME_DESIGN_PARAMETERS.md §3`, `data/tuning.json` (`world.trace_budget_per_era`), `51_QA_TEST_PLAN.md §6` | Perf (`51 §1`, `§6`) | spécifié |
| **EF-VIEIL-13** | Usure des chemins : 40 / 120 / 300 | `21_WORLD_LEVEL_DESIGN.md §6`, `data/tuning.json` (`aging.path_wear_thresholds`) | Functional Tests (`51 §1`) | spécifié |
| **EF-VIEIL-14** | Grotte : protection du vieillissement | `10_NARRATIVE_BIBLE.md §3`, `20_GAME_DESIGN_PARAMETERS.md §4.3` (`seed_cave`, `metal_cave`) | Automation Spec (`51 §1`) | spécifié |
| **EF-VIEIL-15** | Anachronisme : fan-club puis paradoxe | `20_GAME_DESIGN_PARAMETERS.md §4.3` (`anachronism`), `GDD §3.3` | Automation Spec (`51 §1`) | spécifié |
| **EF-VIEIL-16** | Données validées, fichier non conforme rejeté | `40_TECHNICAL_DESIGN.md §3`, `AGENTS.md §5.5` | `tools/validate_data.py` | spécifié |
| **EF-PARAD-01** | Jauge 0-100 et décroissance −1/s | `20_GAME_DESIGN_PARAMETERS.md §5`, `data/tuning.json` (`paradox`) | Automation Spec (`51 §1`) | spécifié |
| **EF-PARAD-02** | Revendication aval, +15 / +25 en amont | `20_GAME_DESIGN_PARAMETERS.md §5`, `51_QA_TEST_PLAN.md §3` | Automation Spec (`51 §1`) | spécifié |
| **EF-PARAD-03** | Glitch de 3 s et messages de seuil | `GDD §3.4`, `51_QA_TEST_PLAN.md §3`, `11_SCRIPTS_DIALOGUES.md §5` | Photosensibilité (`51`, tableau `13`) | spécifié |
| **EF-PARAD-04** | Anachronisme non certifié : +5 par pause | `20_GAME_DESIGN_PARAMETERS.md §5` | Automation Spec (`51 §1`) | spécifié |
| **EF-PARAD-05** | Chronomites à 50 et 75, rongement déterministe | `20_GAME_DESIGN_PARAMETERS.md §5`, `§7` | Golden (`51 §1`) | spécifié |
| **EF-PARAD-06** | Chronomites visant les Figures d'abord | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8`, `10_NARRATIVE_BIBLE.md §7` (chapitre 3) | Functional Tests (`51 §1`) | spécifié |
| **EF-PARAD-07** | Serment rompu : +10 | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.3`, `data/tuning.json` (`faith.oath_broken_paradox`) | Automation Spec (`51 §1`) | spécifié |
| **EF-PARAD-08** | Effondrement à 100 | `20_GAME_DESIGN_PARAMETERS.md §5`, `§6`, `12_SCENARIOS.md §4` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-PARAD-09** | Paradoxe exigé par certains contrats | `GDD §3.4`, `12_SCENARIOS.md §2` (C10) | Automation Spec (`51 §1`) | spécifié |
| **EF-PARAD-10** | Jauge désactivée en mode Détente | `20_GAME_DESIGN_PARAMETERS.md §12`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §11` | Functional Tests (`51 §1`) | spécifié |
| **EF-CONTR-01** | Génération procédurale, 1 + 2 + 1 éléments | `GDD §3.5`, `11_SCRIPTS_DIALOGUES.md §3` | Automation Spec (`51 §1`) | spécifié |
| **EF-CONTR-02** | Contrat entièrement décrit en données | `12_SCENARIOS.md §2` | `tools/validate_data.py` | spécifié |
| **EF-CONTR-03** | Douze contrats de référence | `12_SCENARIOS.md §2`, `71_LIVE_OPS.md §2` | `tools/validate_data.py` | spécifié |
| **EF-CONTR-04** | Barème de score complet | `20_GAME_DESIGN_PARAMETERS.md §6`, `data/tuning.json` (`score`) | Automation Spec (`51 §1`) | spécifié |
| **EF-CONTR-05** | Seuils d'étoiles et formule des Chronos | `20_GAME_DESIGN_PARAMETERS.md §6` | Automation Spec (`51 §1`) | spécifié |
| **EF-CONTR-06** | Solution alternative dans 30 m | `12_SCENARIOS.md §4`, `20_GAME_DESIGN_PARAMETERS.md §6` | Automation Spec (`51 §1`) | spécifié |
| **EF-CONTR-07** | Écran d'évaluation détaillé | `32_UX_UI_SPEC.md §4`, `11_SCRIPTS_DIALOGUES.md §4` | Rendu/visuel (`51 §1`) | spécifié |
| **EF-CONTR-08** | Contrat refusable au chapitre 4 | `10_NARRATIVE_BIBLE.md §7` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-CONTR-09** | Trois issues du Vernissage | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §7` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-CONTR-10** | Ferveur récompensée dans 2 contrats sur 14 | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §11` | `tools/validate_data.py` | spécifié |
| **EF-PEUPL-01** | Cinq jauges entières par Peuple | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §1.2`, `data/tuning.json` (`peoples`) | Déterminisme étendu (`51`, tableau `13`) | spécifié |
| **EF-PEUPL-02** | Bifurcation à la pause café, défaut si égalité | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §1.3`, `data/tuning.json` (`peoples.branch`) | Automation Spec (`51 §1`) | spécifié |
| **EF-PEUPL-03** | Neuf civilisations d'arrivée | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §1.3` | Couverture des bifurcations (`51`, tableau `13`) | spécifié |
| **EF-PEUPL-04** | Frise des peuples lisible en 3 s | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §1.4` | Lisibilité (`51`, tableau `13`) | spécifié |
| **EF-PEUPL-05** | Ferveur portée et propagée par la trace | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.1`, `data/schemas/recipe.schema.json` (`faith`) | Automation Spec (`51 §1`) | spécifié |
| **EF-PEUPL-06** | Figure locale à 30, majeure à 70 | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.1`, `data/tuning.json` (`faith`) | Functional Tests (`51 §1`) | spécifié |
| **EF-PEUPL-07** | Gains et pertes de Ferveur chiffrés | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.1`, `data/tuning.json` (`peoples.gain`, `peoples.loss`) | Automation Spec (`51 §1`) | spécifié |
| **EF-PEUPL-08** | Domaine hérité de la trace d'origine | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.2` | Functional Tests (`51 §1`) | spécifié |
| **EF-PEUPL-09** | Noms par modèles de phrases, jamais par IA | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.2`, `GDD §3.8`, `§6.5` | Functional Tests (`51 §1`) | spécifié |
| **EF-PEUPL-10** | Bienfait, Serment et bouderie | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.3`, `data/tuning.json` (`faith.sulk_rounds`) | Serments (`51`, tableau `13`) | spécifié |
| **EF-PEUPL-11** | Procès en Authenticité, sans affrontement | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §2.4`, `data/tuning.json` (`faith.conflict_radius_m`, `faith.absorb_keep_ratio`) | Functional Tests (`51 §1`) | spécifié |
| **EF-PEUPL-12** | Quatre Porte-Voix et leurs effets | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §3`, `10_NARRATIVE_BIBLE.md §6` | Functional Tests (`51 §1`) | spécifié |
| **EF-PEUPL-13** | Couche passive : gagner sans Figure | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §11` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-PEUPL-14** | Aucune référence religieuse réelle | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0`, `10_NARRATIVE_BIBLE.md §10` | Sensibilité — revue humaine (`51`, tableau `13`) | spécifié |
| **EF-CLIMA-01** | Météo issue de l'Indice Climatique, transmise | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §4.1`, `§4.2` | Déterminisme étendu (`51`, tableau `13`) | spécifié |
| **EF-CLIMA-02** | Sept états, un changement par manche, annonce 15 s | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §4.1`, `data/tuning.json` (`weather`) | Functional Tests (`51 §1`) | spécifié |
| **EF-CLIMA-03** | Sept catastrophes annoncées et non létales | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §5.1`, `data/tuning.json` (`disasters`) | Catastrophes (`51`, tableau `13`) | spécifié |
| **EF-CLIMA-04** | ≤ 20 % des traces, Figures de Mémoire épargnées | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §5.1`, `§10`, `data/tuning.json` (`disasters.max_traces_removed_ratio`) | Catastrophes (`51`, tableau `13`) | spécifié |
| **EF-CLIMA-05** | Aucune catastrophe ne fait perdre la partie | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §5.2` | Catastrophes (`51`, tableau `13`) | spécifié |
| **EF-CLIMA-06** | Cinq phénomènes dont la Résonance | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §6`, `data/tuning.json` (`phenomena`) | Functional Tests (`51 §1`) | spécifié |
| **EF-CLIMA-07** | Aucun flash au-delà de 3 Hz | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6`, `§10`, `51_QA_TEST_PLAN.md` (tableau `13`) | Photosensibilité (`51`, tableau `13`) | spécifié |
| **EF-CLIMA-08** | Signalement sonore, iconique et textuel | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-CLIMA-09** | Météore : cratère, lac, +40 Ferveur | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §5.1`, `12_SCENARIOS.md §5`, `data/tuning.json` (`disasters.meteor`) | Functional Tests (`51 §1`) | spécifié |
| **EF-MUSEE-01** | Musée généré depuis le journal d'actions | `GDD §3.8` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MUSEE-02** | Chronique par modèles de phrases | `GDD §3.8`, `§6.5`, `11_SCRIPTS_DIALOGUES.md §6` | `tools/validate_data.py` | spécifié |
| **EF-MUSEE-03** | Salle des Figures et récit du Peuple | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8`, `12_SCENARIOS.md §4bis` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MUSEE-04** | Ailes selon la richesse de la Chronique | `21_WORLD_LEVEL_DESIGN.md §2` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MUSEE-05** | Statues à la pose réellement capturée | `40_TECHNICAL_DESIGN.md §8`, `33_VISUAL_TARGETS.md §5` (S10) | Rendu/visuel (`51 §1`) | spécifié |
| **EF-MUSEE-06** | Caméra sur rails, mode photo, marqueur | `32_UX_UI_SPEC.md §4` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MUSEE-07** | Carte-récap produite par le jeu | `32_UX_UI_SPEC.md §4`, `33_VISUAL_TARGETS.md §5` (S11) | Rendu/visuel (`51 §1`) | spécifié |
| **EF-MUSEE-08** | Marqueurs d'enregistrement aux moments forts | `GDD §3.8`, `32_UX_UI_SPEC.md §4` | — | spécifié |
| **EF-MUSEE-09** | Aile fermée en cas d'Effondrement | `51_QA_TEST_PLAN.md §3`, `11_SCRIPTS_DIALOGUES.md §6` (CHR_COLLAPSE_01) | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MUSEE-10** | *Ouvert :* confort du musée (caméra, lecture) | `docs/reviews/2026-10-07-revue-joueur.md §5` (confort) ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **EF-MODES-01** | Coop Contrat de 1 à 4 joueurs | `GDD §3.1` | Gauntlet (`51 §1`) | spécifié |
| **EF-MODES-02** | Saboteur : rôle secret et Clé à paradoxe | `GDD §3.1`, `12_SCENARIOS.md §8`, `data/tuning.json` (`paradox.saboteur_*`) | Réseau (`51 §1`, `§5`) | spécifié |
| **EF-MODES-03** | Vote de 20 s et conditions de victoire | `12_SCENARIOS.md §8`, `20_GAME_DESIGN_PARAMETERS.md §5` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MODES-04** | Solo Relais : 4 manches, dangers ×0,7 | `12_SCENARIOS.md §6`, `20_GAME_DESIGN_PARAMETERS.md §1`, `data/tuning.json` (`hazards.solo_hazard_mult`) | Functional Tests (`51 §1`) | spécifié |
| **EF-MODES-05** | Capsule asynchrone et Capsule mystère | `12_SCENARIOS.md §7`, `40_TECHNICAL_DESIGN.md §8`, `71_LIVE_OPS.md §1` | Automation Spec (`51 §1`) | spécifié |
| **EF-MODES-06** | Capsule sans aucune donnée personnelle | `GDD §6.1`, `51_QA_TEST_PLAN.md §3` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MODES-07** | Migration ou refus d'une capsule ancienne | `12_SCENARIOS.md §4`, `11_SCRIPTS_DIALOGUES.md §11` | Automation Spec (`51 §1`) | spécifié |
| **EF-MODES-08** | *Ouvert :* capsule et changement de recettes | `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **EF-MODES-09** | Défi du jour : graine UTC, un essai | `12_SCENARIOS.md §9` | Functional Tests (`51 §1`) | spécifié |
| **EF-MODES-10** | Démo : une carte, deux époques, multijoueur | `GDD §7.1` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-MODES-11** | *Ouvert :* vallée d'équipe persistante | `docs/reviews/2026-10-07-revue-joueur.md §2` (M6) ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **EF-MODES-12** | *Ouvert :* valeur solo du prix de 19,99 € | `docs/reviews/2026-10-07-revue-joueur.md §2` (M8) ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **EF-COMM-01** | Micro jamais obligatoire | `GDD §3.2`, `§6.3`, `20_GAME_DESIGN_PARAMETERS.md §9` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-COMM-02** | Voix inter-époques : quatre régimes de filtre | `20_GAME_DESIGN_PARAMETERS.md §9`, `data/tuning.json` (`voice`), `31_AUDIO_DESIGN.md §4` | — | spécifié |
| **EF-COMM-03** | Seuil de voix, appui pour parler, ducking | `20_GAME_DESIGN_PARAMETERS.md §9`, `31_AUDIO_DESIGN.md §4` | — | spécifié |
| **EF-COMM-04** | Six pings visibles dans toutes les époques | `20_GAME_DESIGN_PARAMETERS.md §9`, `GDD §3.2`, `data/tuning.json` (`ping`) | Functional Tests (`51 §1`) | spécifié |
| **EF-COMM-05** | Huit emotes et douze phrases localisées | `20_GAME_DESIGN_PARAMETERS.md §9` | Localisation (`51 §1`, `§8`) | spécifié |
| **EF-COMM-06** | Fantômes teintés, icône, bouche à 3 états | `GDD §3.2`, `32_UX_UI_SPEC.md §3`, `33_VISUAL_TARGETS.md §1`, `20_GAME_DESIGN_PARAMETERS.md §9` | Rendu/visuel (`51 §1`) | spécifié |
| **EF-COMM-07** | Mute et blocage en un clic | `32_UX_UI_SPEC.md §6`, `GDD §6.2` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-COMM-08** | Seul texte libre : nom de statue ≤ 16 | `40_TECHNICAL_DESIGN.md §6`, `12_SCENARIOS.md §5` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-COMM-09** | Charabia sous-titré, aucune langue réelle | `31_AUDIO_DESIGN.md §3`, `11_SCRIPTS_DIALOGUES.md` (en-tête) | — | spécifié |
| **EF-STREAM-01** | Désactivé par défaut, lecture anonyme | `40_TECHNICAL_DESIGN.md §9`, `GDD §3.9`, `60_LEGAL_COMPLIANCE.md §10` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-STREAM-02** | Rien n'est stocké du chat | `GDD §3.9`, `12_SCENARIOS.md §5`, `60_LEGAL_COMPLIANCE.md §2` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-STREAM-03** | Noms votés filtrés, 16 caractères au plus | `12_SCENARIOS.md §5`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-STREAM-04** | Vote d'événement ou de météo à la pause | `12_SCENARIOS.md §5`, `GDD §3.9`, `11_SCRIPTS_DIALOGUES.md §11` (STREAM_VOTE_*) | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-STREAM-05** | File des spectateurs et overlay Chronique | `12_SCENARIOS.md §5` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-STREAM-06** | Codes masqués, musique sans réclamation | `GDD §3.9`, `31_AUDIO_DESIGN.md` (en-tête), `60_LEGAL_COMPLIANCE.md §10` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-STREAM-07** | *Ouvert :* modération des noms votés | `docs/reviews/2026-10-07-revue-joueur.md §5` (modération) ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **EF-PROGR-01** | Chronos gagnés en jeu, aucun achat réel | `GDD §3.10`, `§7.1`, `20_GAME_DESIGN_PARAMETERS.md §10`, `71_LIVE_OPS.md §5` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-PROGR-02** | Cinq rangs et catalogue de cosmétiques | `20_GAME_DESIGN_PARAMETERS.md §10`, `data/tuning.json` (`progression.ranks`) | `tools/validate_data.py` | spécifié |
| **EF-PROGR-03** | Outils par chapitre, achat en Chronos | `20_GAME_DESIGN_PARAMETERS.md §7`, `data/tuning.json` (`tools`) | Functional Tests (`51 §1`) | spécifié |
| **EF-PROGR-04** | Serments d'agence débloqués par rang | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §8` | Functional Tests (`51 §1`) | spécifié |
| **EF-PROGR-05** | Cinq chapitres, arc optionnel | `10_NARRATIVE_BIBLE.md §7` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-PROGR-06** | *Ouvert :* progression sans effet de jeu | `docs/reviews/2026-10-07-revue-joueur.md §2` (M7) ; point ouvert dans `docs/backlog.md` (statut « partiel ») | — | spécifié |
| **EF-OPT-01** | Les six catégories présentes et effectives | `32_UX_UI_SPEC.md §6`, `51_QA_TEST_PLAN.md §9` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-OPT-02** | Vision : texte 100-200 %, contraste, motifs | `32_UX_UI_SPEC.md §6` | Localisation (`51 §1`, `§8`) | spécifié |
| **EF-OPT-03** | Audio : sous-titres, mono, volumes par bus | `32_UX_UI_SPEC.md §6`, `GDD §6.3`, `31_AUDIO_DESIGN.md §5` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-OPT-04** | Moteur et cognitif : neuf options | `32_UX_UI_SPEC.md §6`, `20_GAME_DESIGN_PARAMETERS.md §12` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-OPT-05** | Réduction des clignotements | `32_UX_UI_SPEC.md §6`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6` | Photosensibilité (`51`, tableau `13`) | spécifié |
| **EF-OPT-06** | Social : micro optionnel, blocage, amis | `32_UX_UI_SPEC.md §6`, `GDD §6.2` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-OPT-07** | Jamais la couleur seule ; HUD visible sous smog | `GDD §6.3`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6`, `21_WORLD_LEVEL_DESIGN.md §10` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-OPT-08** | *Ouvert :* cinématique café et clignotements | `docs/reviews/2026-10-07-revue-joueur.md §5` (confort) ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **EF-SAUV-01** | Progression en nuage, aucun compte propre | `60_LEGAL_COMPLIANCE.md §2`, `71_LIVE_OPS.md §6` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-SAUV-02** | Mode réseau local conservé | `71_LIVE_OPS.md §6`, `40_TECHNICAL_DESIGN.md §6` | Réseau (`51 §1`, `§5`) | spécifié |
| **EF-SAUV-03** | Journal versionné et migrable | `40_TECHNICAL_DESIGN.md §3` | Automation Spec (`51 §1`) | spécifié |
| **EF-SAUV-04** | Époque simulée et reconnexion | `12_SCENARIOS.md §4`, `51_QA_TEST_PLAN.md §5` | Réseau (`51 §1`, `§5`) | spécifié |
| **EF-SAUV-05** | Départ de l'hôte : prime et capsule | `12_SCENARIOS.md §4`, `51_QA_TEST_PLAN.md §3` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-SAUV-06** | Journaux sans donnée personnelle | `32_UX_UI_SPEC.md §7`, `GDD §6.1` | Conformité (`51 §1`, `§9`) | spécifié |
| **EF-LIMIT-01** | Inactivité 90 s et rapatriement unanime | `12_SCENARIOS.md §4`, `11_SCRIPTS_DIALOGUES.md §11`, `data/tuning.json` (`net.afk_seconds`) | Functional Tests (`51 §1`) | spécifié |
| **EF-LIMIT-02** | Griefing empêché par construction | `12_SCENARIOS.md §4`, `40_TECHNICAL_DESIGN.md §6` | Réseau (`51 §1`, `§5`) | spécifié |
| **EF-LIMIT-03** | Départage par tick puis identifiant | `12_SCENARIOS.md §4` | Réseau (`51 §1`, `§5`) | spécifié |
| **EF-LIMIT-04** | Lisière du Bail au bord de la carte | `12_SCENARIOS.md §4`, `10_NARRATIVE_BIBLE.md §3` | Functional Tests (`51 §1`) | spécifié |
| **EF-LIMIT-05** | Graine fossile en terrain impossible | `12_SCENARIOS.md §4`, `51_QA_TEST_PLAN.md §3` | Automation Spec (`51 §1`) | spécifié |
| **EF-LIMIT-06** | Messages réseau dédiés | `32_UX_UI_SPEC.md §7`, `11_SCRIPTS_DIALOGUES.md §11` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **EF-LIMIT-07** | Messages non techniques à l'écran | `32_UX_UI_SPEC.md §7` | Exploratoire (`51 §1`) | spécifié |
| **EF-LIMIT-08** | Rejet hors portée, exclusion à 20/min | `51_QA_TEST_PLAN.md §3`, `40_TECHNICAL_DESIGN.md §6`, `data/tuning.json` (`net.kick_rejects_per_minute`) | Réseau (`51 §1`, `§5`) | spécifié |
| **EF-LIMIT-09** | *Ouvert :* hôte à connexion instable | `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **ENF-PERF-01** | 1440p 60 i/s, 16,6 ms (recommandé) | `40_TECHNICAL_DESIGN.md §10`, `30_ART_BIBLE.md §4` | Perf (`51 §1`, `§6`) | spécifié |
| **ENF-PERF-02** | 1080p 30-60 i/s, 33 ms (minimum) | `40_TECHNICAL_DESIGN.md §10`, `30_ART_BIBLE.md §4` | Perf (`51 §1`, `§6`) | spécifié |
| **ENF-PERF-03** | 800p 30 i/s sur Steam Deck | `40_TECHNICAL_DESIGN.md §10` | Perf (`51 §1`, `§6`) | spécifié |
| **ENF-PERF-04** | Tick 20 Hz < 4 ms, propagation p95 < 2 ms | `40_TECHNICAL_DESIGN.md §10`, `51_QA_TEST_PLAN.md §6`, `data/tuning.json` (`net.tick_hz`) | Perf (`51 §1`, `§6`) | spécifié |
| **ENF-PERF-05** | Stress, mémoire sur 2 h, chargement < 8 s | `51_QA_TEST_PLAN.md §6` | Gauntlet (`51 §1`) | spécifié |
| **ENF-PERF-06** | Budgets de contenu et d'audio | `30_ART_BIBLE.md §4`, `31_AUDIO_DESIGN.md §6` | Perf (`51 §1`, `§6`) | spécifié |
| **ENF-DET-01** | Entiers, PCG32, conteneurs triés | `40_TECHNICAL_DESIGN.md §4`, `ARCHITECTURE.md` (invariant `TemporalCore`) | Automation Spec (`51 §1`) | spécifié |
| **ENF-DET-02** | Ni physique, ni heure, ni hasard global | `40_TECHNICAL_DESIGN.md §4`, `AGENTS.md §5.2` | Automation Spec (`51 §1`) | spécifié |
| **ENF-DET-03** | Gel des corps dynamiques en fin de manche | `40_TECHNICAL_DESIGN.md §4` | Golden (`51 §1`) | spécifié |
| **ENF-DET-04** | Test golden à chaque demande de fusion | `40_TECHNICAL_DESIGN.md §4`, `51_QA_TEST_PLAN.md §1` | Golden (`51 §1`) | spécifié |
| **ENF-DET-05** | Systèmes émergents dans le hachage de monde | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §10`, `51_QA_TEST_PLAN.md` (tableau `13`) | Déterminisme étendu (`51`, tableau `13`) | spécifié |
| **ENF-DET-06** | Génération du monde déterministe | `21_WORLD_LEVEL_DESIGN.md §4`, `40_TECHNICAL_DESIGN.md §5` | Automation Spec (`51 §1`) | spécifié |
| **ENF-RES-01** | Moins de 30 ko/s par joueur | `40_TECHNICAL_DESIGN.md §10`, `51_QA_TEST_PLAN.md §5` | Réseau (`51 §1`, `§5`) | spécifié |
| **ENF-RES-02** | Hachage toutes les 5 s et resynchronisation | `40_TECHNICAL_DESIGN.md §6`, `data/tuning.json` (`net.hash_check_seconds`) | Réseau (`51 §1`, `§5`) | spécifié |
| **ENF-RES-03** | Latence, perte et gigue sans désynchronisation | `51_QA_TEST_PLAN.md §5` | Réseau (`51 §1`, `§5`) | spécifié |
| **ENF-RES-04** | Déconnexion, départ d'hôte, même tick | `51_QA_TEST_PLAN.md §5`, `12_SCENARIOS.md §4` | Gauntlet (`51 §1`) | spécifié |
| **ENF-RES-05** | Pas de migration d'hôte, capsule de reprise | `40_TECHNICAL_DESIGN.md §6` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **ENF-RES-06** | Aucune adresse IP exposée | `40_TECHNICAL_DESIGN.md §6`, `51_QA_TEST_PLAN.md §9` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-SEC-01** | Validation hôte : portée, débit, taille | `40_TECHNICAL_DESIGN.md §6`, `data/tuning.json` (`net`) | Réseau (`51 §1`, `§5`) | spécifié |
| **ENF-SEC-02** | Exclusion à 20 rejets par minute | `40_TECHNICAL_DESIGN.md §6` | Réseau (`51 §1`, `§5`) | spécifié |
| **ENF-SEC-03** | Fuzzing de 10 000 appels sans plantage | `51_QA_TEST_PLAN.md §5` | Réseau (`51 §1`, `§5`) | spécifié |
| **ENF-SEC-04** | Aucun texte libre non filtré | `40_TECHNICAL_DESIGN.md §6`, `51_QA_TEST_PLAN.md §9` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-SEC-05** | Aucun secret dans le dépôt | `40_TECHNICAL_DESIGN.md §11`, `AGENTS.md §6` | `tools/privacy_scan.py` | spécifié |
| **ENF-SEC-06** | Politique de divulgation responsable | `legal/README.md` (document 16), `60_LEGAL_COMPLIANCE.md §1` | — | spécifié |
| **ENF-SEC-07** | *Ouvert :* anti-triche (ADR 0020) | `40_TECHNICAL_DESIGN.md §6`, `§14` (ADR 0020), `docs/reviews/2026-10-07-revue-joueur.md §5` | — | spécifié |
| **ENF-RGPD-01** | Minimisation conforme au registre | `60_LEGAL_COMPLIANCE.md §2`, `GDD §6.1` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-RGPD-02** | Voix jamais enregistrée | `GDD §6.1`, `40_TECHNICAL_DESIGN.md §7` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **ENF-RGPD-03** | Opt-in, hébergement UE, durées bornées | `GDD §6.1`, `60_LEGAL_COMPLIANCE.md §2` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-RGPD-04** | Événements sans identifiant ni texte libre | `20_GAME_DESIGN_PARAMETERS.md §13` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-RGPD-05** | Télémétrie inopérante sans consentement | `51_QA_TEST_PLAN.md §9` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-RGPD-06** | Droits des personnes exerçables | `60_LEGAL_COMPLIANCE.md §3`, `GDD §6.1` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-RGPD-07** | Aucun traceur, cookie ni CDN externe | `GDD §6.1`, `AGENTS.md §4.3`, `ARCHITECTURE.md` (invariant de la landing) | `tools/privacy_scan.py` | spécifié |
| **ENF-RGPD-08** | Chat streamer traité en mémoire seule | `GDD §6.1`, `40_TECHNICAL_DESIGN.md §9` | Gherkin système (`51 §1`, `§3`) | spécifié |
| **ENF-RGPD-09** | Consentement écrit aux playtests | `51_QA_TEST_PLAN.md §7`, `60_LEGAL_COMPLIANCE.md §2` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-RGPD-10** | Registre des traitements et analyse d'impact | `60_LEGAL_COMPLIANCE.md §1`, `legal/README.md` (documents 06 et 07) | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-RGPD-11** | Mineurs protégés par défaut | `GDD §6.2`, `60_LEGAL_COMPLIANCE.md §6`, `legal/README.md §2` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-ACC-01** | Référentiel d'accessibilité suivi | `GDD §6.3`, `51_QA_TEST_PLAN.md` (en-tête) | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-ACC-02** | Options présentes et fonctionnelles | `32_UX_UI_SPEC.md §6`, `51_QA_TEST_PLAN.md §9` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-ACC-03** | Jouable sans micro, sans son, en daltonien | `51_QA_TEST_PLAN.md §9`, `GDD §6.3` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-ACC-04** | Jamais la couleur seule | `GDD §6.3`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6`, `21_WORLD_LEVEL_DESIGN.md §10` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-ACC-05** | Aucun flash au-delà de 3 Hz | `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0.6`, `§10`, `32_UX_UI_SPEC.md §6` | Photosensibilité (`51`, tableau `13`) | spécifié |
| **ENF-ACC-06** | Texte de 100 à 200 % et au moins 9 px | `32_UX_UI_SPEC.md §6`, `§8`, `51_QA_TEST_PLAN.md §9` | Localisation (`51 §1`, `§8`) | spécifié |
| **ENF-ACC-07** | Remappage complet, maintien convertible | `32_UX_UI_SPEC.md §5`, `§6`, `GDD §6.3` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-ACC-08** | Déclaration d'accessibilité publiée | `GDD §6.3`, `legal/README.md` (document 11, matrice §2) | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-LOC-01** | Huit langues, FR et EN à 100 % à G5 | `70_MARKETING_GTM.md §3`, `11_SCRIPTS_DIALOGUES.md §12`, `50_PRODUCTION_PLAN.md §2` | Localisation (`51 §1`, `§8`) | spécifié |
| **ENF-LOC-02** | +30 % d'expansion, aucune image textuelle | `32_UX_UI_SPEC.md §8` | Localisation (`51 §1`, `§8`) | spécifié |
| **ENF-LOC-03** | Repli de police CJK | `32_UX_UI_SPEC.md §8`, `51_QA_TEST_PLAN.md §8` | Localisation (`51 §1`, `§8`) | spécifié |
| **ENF-LOC-04** | Marqueurs identiques dans toutes les langues | `51_QA_TEST_PLAN.md §8`, `11_SCRIPTS_DIALOGUES.md` (en-tête) | Localisation (`51 §1`, `§8`) | spécifié |
| **ENF-LOC-05** | Aucun doublage nécessaire | `31_AUDIO_DESIGN.md §3` | — | spécifié |
| **ENF-LOC-06** | Textes juridiques disponibles en français | `legal/README.md §2` (ligne « Langue ») | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-COMPAT-01** | Matrice de configuration couverte | `51_QA_TEST_PLAN.md §4` | Matrice de configuration (`51 §4`) | spécifié |
| **ENF-COMPAT-02** | Clavier-souris et manette | `32_UX_UI_SPEC.md §5`, `51_QA_TEST_PLAN.md §4` | Matrice de configuration (`51 §4`) | spécifié |
| **ENF-COMPAT-03** | Deck : contrôles natifs, texte ≥ 9 px | `51_QA_TEST_PLAN.md §9` | Matrice de configuration (`51 §4`) | spécifié |
| **ENF-COMPAT-04** | Quatre conditions de réseau testées | `51_QA_TEST_PLAN.md §4` | Réseau (`51 §1`, `§5`) | spécifié |
| **ENF-COMPAT-05** | *Ouvert :* niveau Deck visé, macOS et Linux | `40_TECHNICAL_DESIGN.md §10`, `docs/reviews/2026-10-07-revue-joueur.md §5` ; point ouvert dans `docs/backlog.md` | — | spécifié |
| **ENF-OBS-01** | Mesures sans donnée personnelle | `20_GAME_DESIGN_PARAMETERS.md §13`, `60_LEGAL_COMPLIANCE.md §2` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-OBS-02** | Quatre métriques d'expérience | `32_UX_UI_SPEC.md §9` | — | spécifié |
| **ENF-OBS-03** | Traces de profilage archivées par build | `40_TECHNICAL_DESIGN.md §10`, `51_QA_TEST_PLAN.md §1` | Perf (`51 §1`, `§6`) | spécifié |
| **ENF-OBS-04** | Journaux locaux sans donnée personnelle | `32_UX_UI_SPEC.md §7`, `GDD §6.1` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-OBS-05** | Tableau de bord qualité par porte | `51_QA_TEST_PLAN.md §10`, `STUDIO_STATE.md` | `tools/validate_state.py` | spécifié |
| **ENF-MAINT-01** | Aucune valeur de gameplay en dur | `20_GAME_DESIGN_PARAMETERS.md` (en-tête), `AGENTS.md §5.5`, `ARCHITECTURE.md` (invariant `data/`) | — | spécifié |
| **ENF-MAINT-02** | Données validées par schéma en intégration | `40_TECHNICAL_DESIGN.md §11`, `ARCHITECTURE.md` (les portes) | `tools/validate_data.py` | spécifié |
| **ENF-MAINT-03** | ADR écrit avant le code | `40_TECHNICAL_DESIGN.md §14`, `AGENTS.md §5.7` | — | spécifié |
| **ENF-MAINT-04** | Une responsabilité par sous-système | `AGENTS.md §5.6` | — | spécifié |
| **ENF-MAINT-05** | Couverture ≥ 90 %, intégration < 10 min | `50_PRODUCTION_PLAN.md §9` | — | spécifié |
| **ENF-MAINT-06** | Test de non-régression par S1 et S2 | `51_QA_TEST_PLAN.md §1` | — | spécifié |
| **ENF-MAINT-07** | Definition of Done respectée | `50_PRODUCTION_PLAN.md §4` | — | spécifié |
| **ENF-PORT-01** | Cœur temporel sans dépendance au moteur | `40_TECHNICAL_DESIGN.md §1`, `§2` | Automation Spec (`51 §1`) | spécifié |
| **ENF-PORT-02** | `data/` embarqué sans duplication | `40_TECHNICAL_DESIGN.md §2` | — | spécifié |
| **ENF-PORT-03** | Contenu binaire en dépôt privé | `40_TECHNICAL_DESIGN.md §12`, `AGENTS.md §4.5`, `ARCHITECTURE.md` | `tools/license_audit.py` | spécifié |
| **ENF-PORT-04** | Dépendances épinglées et versionnées | `40_TECHNICAL_DESIGN.md §13`, `tools/versions.env` | `tools/repo_audit.py` | spécifié |
| **ENF-PLAT-01** | Règles de la plateforme respectées | `51_QA_TEST_PLAN.md §9`, `60_LEGAL_COMPLIANCE.md §1` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-PLAT-02** | Déclaration sur l'IA honnête | `GDD §6.5`, `60_LEGAL_COMPLIANCE.md §8`, `legal/README.md` (document 17) | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-PLAT-03** | Classification d'âge cohérente | `GDD §6.2`, `60_LEGAL_COMPLIANCE.md §6`, `legal/README.md` (document 19) | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-PLAT-04** | Gameplay réellement capturé en jeu | `33_VISUAL_TARGETS.md §6` | Rendu/visuel (`51 §1`) | spécifié |
| **ENF-PLAT-05** | Conditions du chat tiers vérifiées avant P6 | `60_LEGAL_COMPLIANCE.md §10`, `40_TECHNICAL_DESIGN.md §9` | — | spécifié |
| **ENF-PLAT-06** | Redistribution limitée aux fichiers autorisés | `GDD §6.4` | `tools/license_audit.py` | spécifié |
| **ENF-LIC-01** | Source et licence par asset tiers | `GDD §6.4` | `tools/license_audit.py` | spécifié |
| **ENF-LIC-02** | Licences affichées dans les Crédits | `GDD §6.4`, `60_LEGAL_COMPLIANCE.md §7` | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-LIC-03** | Cession de droits écrite par commande | `60_LEGAL_COMPLIANCE.md §7`, `legal/README.md` (document 15) | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-LIC-04** | Aucune œuvre ni marque réelle reproduite | `30_ART_BIBLE.md §6`, `10_NARRATIVE_BIBLE.md §2` | Sensibilité — revue humaine (`51`, tableau `13`) | spécifié |
| **ENF-LIC-05** | Médias du moteur, approuvés avant publication | `33_VISUAL_TARGETS.md` (en-tête), `§8`, `AGENTS.md §4.6` | `tools/check_media_approvals.py` | spécifié |
| **ENF-LIC-06** | Redevance du moteur suivie et provisionnée | `GDD §7.1`, `legal/README.md` (document 20) | — | spécifié |
| **ENF-ETH-01** | Aucune loot box ni jeu d'argent | `GDD §6.2`, `§7.1`, `71_LIVE_OPS.md §5`, `legal/README.md §2` | — | spécifié |
| **ENF-ETH-02** | Aucun FOMO, saisons cosmétiques | `71_LIVE_OPS.md §3`, `§5` | — | spécifié |
| **ENF-ETH-03** | Contenus additionnels à prix fixe | `GDD §3.10`, `71_LIVE_OPS.md §5`, `legal/README.md` (document 10) | — | spécifié |
| **ENF-ETH-04** | Satire des institutions, jamais des personnes | `10_NARRATIVE_BIBLE.md §2`, `13_PEUPLES_DIEUX_ET_PHENOMENES.md §0` | Sensibilité — revue humaine (`51`, tableau `13`) | spécifié |
| **ENF-ETH-05** | Charte, code de conduite, modération publiés | `legal/README.md` (documents 08, 13, 18), `60_LEGAL_COMPLIANCE.md §6` | — | spécifié |
| **ENF-ETH-06** | Usage de l'IA documenté publiquement | `GDD §6.5`, `legal/README.md` (document 17) | Conformité (`51 §1`, `§9`) | spécifié |
| **ENF-DUR-01** | Aucun serveur propriétaire requis | `71_LIVE_OPS.md §6`, `GDD §6.1` | — | spécifié |
| **ENF-DUR-02** | Réseau local conservé | `71_LIVE_OPS.md §6`, `40_TECHNICAL_DESIGN.md §6` | Réseau (`51 §1`, `§5`) | spécifié |
| **ENF-DUR-03** | Procédure de fin de vie écrite | `71_LIVE_OPS.md §6` | — | spécifié |
| **ENF-DUR-04** | Monde reconstituable depuis graine et journal | ADR 0002, `40_TECHNICAL_DESIGN.md §1`, `§8` | Automation Spec (`51 §1`) | spécifié |
---

## 4. Exigences sans vérification — liste honnête

37 exigences sur 272 n'ont **aucun** moyen de vérification parmi les familles de test de `51` et les
scripts de `tools/`. Elles se répartissent en quatre causes distinctes, qui n'appellent pas les mêmes
réponses.

### 4.1 Points ouverts du dossier de conception — 14 exigences
Elles ne sont pas vérifiables parce qu'elles ne sont **pas encore décidées**. Chacune renvoie à
[`docs/backlog.md`](../backlog.md) et attend une décision humaine, non un test.

| Exigence | Décision attendue |
|---|---|
| EF-APPAR-06 | Appariement d'un joueur sans amis disponibles |
| EF-APPAR-07 | Comportement d'un joueur qui rejoint en cours de partie |
| EF-APPAR-08 | Crossplay : exclu ou prévu |
| EF-APPAR-09 | Démo multijoueur permanente ; jouer à 4 avec un seul exemplaire |
| EF-MUSEE-10 | Confort du musée : mal des transports, durée d'affichage de la Chronique |
| EF-MODES-08 | Survie d'une capsule à un changement de recettes |
| EF-MODES-11 | Vallée d'équipe persistante (revue M6) |
| EF-MODES-12 | Valeur solo assumée ou Défi du jour comme colonne vertébrale (revue M8) |
| EF-STREAM-07 | Qui modère un nom voté par le chat, et avec quels moyens |
| EF-PROGR-06 | Progression ayant un effet sur le jeu (revue M7) |
| EF-OPT-08 | Cinématique de pause café et mode « réduire les clignotements » |
| EF-LIMIT-09 | Hôte à connexion instable sans départ franc |
| ENF-SEC-07 | Anti-triche (ADR 0020) face au classement quotidien |
| ENF-COMPAT-05 | Niveau Steam Deck visé ; macOS et Linux |

> Douze de ces exigences sont fonctionnelles (`10`), deux sont non fonctionnelles (`20`).

### 4.2 Aucune famille de test audio dans `51` — 5 exigences
`31_AUDIO_DESIGN.md` §7 énonce de vrais tests audio (aucun son au-delà de 0 dBTP, aucune boucle avec clic,
latence de voix < 250 ms en réseau local, aucun fichier audio dans le dossier utilisateur) et renvoie à
`51_QA_TEST_PLAN.md` — mais **`51` ne contient aucune ligne audio** dans sa stratégie §1. Les exigences
suivantes n'ont donc pas de famille de test à nommer :

- **EF-PARTIE-12** — musique adaptative par couches et continuité de mesure au changement d'époque.
- **EF-COMM-02** — les quatre régimes de filtre de la voix inter-époques.
- **EF-COMM-03** — seuil de détection de voix, appui pour parler, atténuation de la musique.
- **ENF-LOC-05** et **EF-COMM-09** — charabia sous-titré, absence de doublage (couvert pour la partie
  « sous-titres » par `51 §8`, pas pour la partie audio).

**Recommandation (à instruire par l'humain) :** ajouter une ligne « Audio » à la stratégie de `51 §1`, qui
reprenne `31 §7`. Proposition consignée dans [`docs/backlog.md`](../backlog.md).

### 4.3 Engagements de gouvernance, d'éthique et de cycle de vie — 10 exigences
Elles sont vérifiables par un humain, mais aucune checklist de `51 §9` ni aucun script de `tools/` ne les
couvre aujourd'hui. `51 §9` contient cinq checklists — RGPD, Licences, Accessibilité, Steam, Sécurité — et
aucune ne porte sur les engagements éthiques ni sur la pérennité.

| Exigence | Ce qui manque |
|---|---|
| ENF-ETH-01 | Aucune checklist ne vérifie l'absence de loot box et de mécanique de jeu d'argent |
| ENF-ETH-02 | Aucune ne vérifie l'absence de pression temporelle (« FOMO ») |
| ENF-ETH-03 | Aucune ne vérifie l'absence de monnaie payante intermédiaire |
| ENF-ETH-05 | Aucune ne vérifie la publication de la charte, du code de conduite et du dispositif de modération |
| ENF-SEC-06 | Aucune ne vérifie l'existence de la politique de divulgation responsable et de son contact |
| ENF-PLAT-05 | Aucune ne vérifie que les conditions du service de chat tiers ont été relues avant la phase P6 |
| ENF-LIC-06 | Aucun suivi de la redevance du moteur n'est outillé |
| ENF-DUR-01 | Aucune ne vérifie l'absence de dépendance à un serveur propriétaire |
| ENF-DUR-03 | Aucune ne vérifie l'existence de la procédure de fin de vie |
| EF-MUSEE-08 | Les marqueurs d'enregistrement de la plateforme ne figurent pas dans la checklist Steam de `51 §9` |

**Recommandation :** étendre `51 §9` de deux checklists — « Éthique et monétisation » et « Pérennité et
divulgation » — plutôt que d'écrire du code de test. Proposition consignée dans
[`docs/backlog.md`](../backlog.md).

### 4.4 Exigences tenues par le processus, non par un test — 8 exigences
`ENF-MAINT-01` à `ENF-MAINT-07` (sauf `ENF-MAINT-02`, couverte par `tools/validate_data.py`) et
`ENF-PORT-02` et `ENF-OBS-02` sont garanties par la **Definition of Done** (`50_PRODUCTION_PLAN.md` §4) et
par les indicateurs de pilotage (`50 §9`), c'est-à-dire par des contrôles humains de revue, pas par une
famille de test. C'est défendable, mais cela veut dire qu'un relâchement de la revue ne déclenche aucune
alarme automatique.

Les trois plus exposées :
- **ENF-MAINT-01** — « aucune valeur de gameplay en dur » est l'invariant le plus structurant du dépôt
  (`ARCHITECTURE.md`) et **rien ne le vérifie**. Un script d'analyse statique cherchant des littéraux
  numériques dans le code de gameplay serait l'outil manquant le plus rentable.
- **ENF-MAINT-03** — « un ADR avant le code » : `tools/repo_audit.py` vérifie les liens et les fichiers
  requis, pas la présence des ADR 0013 à 0020 attendus en sortie de P0.
- **ENF-MAINT-05** — couverture ≥ 90 % et intégration continue < 10 min sont des indicateurs relevés à la
  main en fin de sprint.

## 5. Défaut relevé dans le plan de test lui-même

`51_QA_TEST_PLAN.md` §1 nomme, pour la famille **Réseau**, le script `tools/run_local_4p.sh --bot`.
**Ce script n'existe pas dans le dépôt.** Quatorze exigences de cette matrice s'appuient sur cette famille
(EF-LIMIT-02, EF-LIMIT-03, EF-LIMIT-08, EF-MODES-02, EF-SAUV-02, EF-SAUV-04, ENF-RES-01 à ENF-RES-03,
ENF-SEC-01 à ENF-SEC-03, ENF-COMPAT-04, ENF-DUR-02). Rien n'est faux : le script relève de la phase P2,
comme le reste du code. Mais la matrice ne peut pas le présenter comme un moyen de vérification **disponible**,
et c'est consigné ici plutôt que corrigé dans `51`, qu'aucun agent ne modifie
([`ARCHITECTURE.md`](../../ARCHITECTURE.md)).

## 6. Ce que cette matrice ne dit pas

Elle ne mesure ni le fun, ni la valeur commerciale. Le protocole de playtest (`51 §7`) et les seuils
go/no-go du [`00_CAHIER_DES_CHARGES.md`](00_CAHIER_DES_CHARGES.md) §4 vérifient cela, au niveau des portes
et non des exigences — c'est pourquoi une seule exigence de cette matrice renvoie au playtest. Elle ne
remplace pas non plus le tableau de bord qualité par porte (`51 §10`, `docs/qa/`), qui porte les résultats
réels d'exécution.
