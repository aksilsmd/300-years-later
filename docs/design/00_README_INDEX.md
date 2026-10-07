# CENTURY TEMPS — Dossier de production v2 (index)

> Nom de code : **CENTURY TEMPS**. Titre public à choisir et à déposer (voir `60_LEGAL_COMPLIANCE.md` §7 — candidats : *Temporis*, *Intérim Temporel*, *300 Ans Plus Tard*, *Chronotemps*, *Temporis Intérim*).
> Date : 7 octobre 2026 · **v3 : Unreal Engine 5.8, réalisme, aucune image hors moteur.** Auteur : étude Claude + Product Owner. Statut : **Pré-production — prêt pour Claude Code**.

## 1. Pourquoi ce dossier existe
Un grand studio ne « code pas un jeu » : il traverse des **portes de décision** (gates) avec des livrables précis à chaque étape. Ce dossier reproduit ce pipeline à l'échelle d'un développeur seul assisté par Claude Code.

| Étape studio | Question à laquelle elle répond | Livrables | Fichiers |
|---|---|---|---|
| **G0 Concept** | Quelle idée, pour qui, pourquoi maintenant ? | Pitch, étude de marché, originalité | `GDD_CENTURY_TEMPS.md` (v1) + audit `01_AUDIT_V1.md` |
| **G1 Greenlight** | Vaut-elle l'investissement ? | Critères de go/no-go, budget, risques | `GDD` §7, `52_RISK_REGISTER.md` |
| **G2 Pré-production** | Sait-on exactement quoi construire ? | Bible narrative, scripts, scénarios, design détaillé, monde, art réaliste, **cahier de rendu**, audio, UX, TDD Unreal, données, plan de prod, plan QA, cadre juridique | `10` à `60` (dont `33_VISUAL_TARGETS.md` et `34_LANDING_CINEMATIQUE.md`) + `data/` + `../../legal/` |
| **G3 Tranche verticale (First Playable)** | Est-ce amusant, en ligne, avec la qualité cible ? | Build jouable à 4, playtest mesuré | `50_PRODUCTION_PLAN.md` §4, `51_QA_TEST_PLAN.md` |
| **G4 Alpha** (features complètes) → **G5 Beta** (contenu complet) → **G6 Release Candidate** → **G7 Gold** | Le jeu est-il complet, stable, conforme ? | Builds, rapports de tests, checklists | `50`, `51`, `60` |
| **Lancement** | Comment être trouvé et acheté ? | Page Steam, trailer, créateurs, communauté | `70_MARKETING_GTM.md` |
| **Live ops** | Comment durer ? | Roadmap EA, cadence de patchs, événements | `71_LIVE_OPS.md` |
| **Exécution** | Que donner à Claude Code, dans quel ordre ? | Playbook, prompts, templates, backlog | `80_CLAUDE_CODE_PLAYBOOK.md`, `CLAUDE.md`, `.github/`, `docs/adr/` |

## 2. Ordre de lecture
**Pour l'humain (Product Owner)** : `01_AUDIT_V1.md` → `GDD` → `10_NARRATIVE_BIBLE.md` → `12_SCENARIOS.md` → `50_PRODUCTION_PLAN.md` → `60_LEGAL_COMPLIANCE.md` → `80_CLAUDE_CODE_PLAYBOOK.md`.

**Pour Claude Code** (ordre imposé dans `CLAUDE.md`) : `CLAUDE.md` → `GDD` → `40_TECHNICAL_DESIGN.md` → `20_GAME_DESIGN_PARAMETERS.md` → `21_WORLD_LEVEL_DESIGN.md` → `data/` → `10`/`11`/`12` → `30`/`33`/`34`/`31`/`32` → `50`/`51` → `80`.

**Guides humains :** `../guides/` · **Juridique :** `../../legal/` · **Décisions :** `../adr/` (dont ADR 0012 : Unreal Engine 5.8 et réalisme).

## 3. Règle d'or du dossier
Chaque document a un **propriétaire** (Product Owner), une **version**, et ne change que par décision écrite (ADR ou note de version en tête de fichier). Claude Code **ne modifie jamais** un document de design ; il propose une modification dans `docs/backlog.md` et l'humain tranche.

## 4. Vocabulaire (identique dans tous les documents)
| Terme | Définition |
|---|---|
| Époque (E0…E3) | L'Aube (an 0), Les Bannières (an 300), La Vapeur (an 600), Le Néon (an 900) |
| Trace | Tout objet/état persistant laissé dans une époque et soumis au vieillissement |
| Recette | Règle déterministe : état d'une trace + environnement → état 300 ans plus tard |
| Saut (hop) | Un passage d'époque (E0→E1 = 1 saut) |
| Propagation | Recalcul des époques aval après une action |
| Non-conformité | Paradoxe : conflit entre une modification aval et un changement amont |
| Chronomites | Créatures qui apparaissent quand la jauge de non-conformité monte |
| Contrat | Objectif de partie émis par le Client, noté sur 5 étoiles |
| Pause café | Intermède de 30 s entre deux manches : cinématique des siècles qui défilent |
| Rotation | Chaque joueur avance d'une époque entre deux manches |
| Capsule | Code partageable (graine + journal d'actions) pour jouer en différé |
| Chronique | Récit de la partie généré par modèles de phrases, affiché au Musée |
