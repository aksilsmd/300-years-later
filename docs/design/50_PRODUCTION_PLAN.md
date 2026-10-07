# 50 — Plan de production
Propriétaire : Product Owner · v2.0 (Unreal Engine 5.8, réaliste) · Claude Code comme exécutant principal du code, des freelances pour l'art organique, l'humain pour les décisions.

## 1. Rôles (équipe d'un studio, version solo)
| Rôle studio | Qui | Responsabilités |
|---|---|---|
| Producteur / Product Owner | Porteur du projet | Backlog, priorités, gates, budget, planning |
| Game Director | Porteur du projet | Vision, fun, arbitrages de design |
| Lead Dev / Dev | Claude Code (supervisé) | Code, tests, CI, ADR |
| QA Lead | Porteur du projet | Plan de test, campagnes, playtests, go/no-go qualité |
| Tech Art | Claude Code (plugin MCP Unreal) | PCG, matériaux, Niagara, intégration des assets, Python d'éditeur |
| Artistes 3D / animation | Freelances | Créatures, capture de jeu d'acteur, retouches d'assets, direction artistique |
| Audio | Compositeur freelance + Claude Code (SFX procéduraux) | Musique, SFX |
| Illustration | Illustrateur freelance | Capsule, logo, panneaux de cinématique |
| Localisation | Traducteurs freelance (ou communauté encadrée) | Langues EA |
| Juridique / compta | Professionnels externes | Contrats, marque, structure |
| Community | Porteur du projet | Discord/Stoat, réseaux, créateurs |

## 2. Portes de décision (gates)
| Gate | Contenu | Critères de sortie (tous obligatoires) | Décideur |
|---|---|---|---|
| **G0 Concept** | Étude, pitch, audit | Dossier v2 validé ; contrat de travail vérifié (clause exclusivité/PI) | Porteur du projet |
| **G1 Prototype du fun** (phase 1) | Graine→arbre hors ligne | 5/5 testeurs réagissent (rire, « wow ») en < 10 min ; temps au « aha » < 60 s | Porteur du projet + 5 testeurs |
| **G2 Pré-prod close** | Phases 0-2 | 4 joueurs en ligne sans désync sur 30 min ; ADR 0001-0010 écrits | Porteur du projet |
| **G3 Tranche verticale** (phase 3) | Partie complète 15-20 min | Playtest 8 personnes : note moyenne « je rejouerais » ≥ 4/5 ; 0 bloquant ; page Steam ouverte | Porteur du projet |
| **G4 Alpha** (phases 4-6) | Toutes features | 30 recettes, 12 contrats, tous modes ; crash rate < 1/heure ; voix + streamer OK | Porteur du projet |
| **G5 Beta** (phase 7) | Contenu complet + conformité | Loc FR/EN 100 % ; checklist accessibilité verte ; textes juridiques validés par un pro ; 0 bloquant, ≤ 5 majeurs | Porteur du projet + juriste |
| **G6 Release Candidate** (phase 8) | Démo + build EA | 60 fps Deck ; 2 h à 4 sans crash ; questionnaire Steam rempli ; build approuvée par Valve | Porteur du projet |
| **G7 Gold / Lancement EA** | Mise en vente | Next Fest passé ; seuils wishlists (GDD §7.3) ; plan live ops prêt | Porteur du projet |

**Règle d'arrêt :** si G1 échoue deux fois après itération, on change de mécanique ou on abandonne le projet (coût perdu ≤ 1 mois).

## 3. Calendrier
Le calendrier dépend du scénario d'équipe (solo + IA, studio réduit, petite équipe) : voir **`docs/guides/03_TEMPS_ET_COUTS.md` §1 et §3** (18 à 48 mois jusqu'à l'Early Access). Règle : un retard de plus de 25 % sur une porte déclenche une revue de périmètre (§6) avant toute rallonge de budget.

## 4. Méthode : Scrum allégé
- **Sprint** : 2 semaines. **Planification** (30 min) : choisir les tickets « Prêts » du backlog. **Revue** (30 min) : jouer la build. **Rétro** (15 min) : 1 chose à garder, 1 à changer.
- **Backlog** : GitHub Issues + GitHub Projects (colonnes : Idée → Prêt → En cours → En revue → Fait). Labels : `phase-N`, `type:feature|bug|tech-debt|content|legal|qa`, `prio:P0..P3`, `gate:Gx`.
- **Definition of Ready (DoR)** : un ticket est « Prêt » s'il a : objectif joueur, référence au document de design (§), critères d'acceptation Gherkin, dépendances identifiées, taille ≤ 1 jour Claude Code.
- **Definition of Done (DoD)** : code + tests verts + lint + audit licences + clés `tr()` créées + doc à jour (`architecture.md` ou ADR) + PR relue par Product Owner + build jouée 5 min sans régression.
- **Priorités** : P0 bloquant (crash, désync, conformité), P1 cœur du fun, P2 confort, P3 idée.

## 5. Gestion de configuration
- Git (GitHub privé), branches `feat/*`, `fix/*`, PR obligatoire, `main` protégé, tags `phase-N` et `vX.Y.Z`.
- Versionnage sémantique ; changelog `CHANGELOG.md` (Keep a Changelog) mis à jour à chaque PR.
- Builds : artefacts CI conservés 30 jours ; builds de gate archivées.
- Branches Steam : `default` (public), `beta`, `demo`, `qa` (protégée par mot de passe).

## 6. Gestion du périmètre (scope)
Ordre de coupe si retard (du premier sacrifié au dernier) : biome Côte → mode Saboteur → Défi du jour → mode Capsule → mode Streamer → voix inter-époques (garder pings) → 2e biome de recettes. **Jamais coupés** : moteur de vieillissement, rotation, musée, 4 joueurs en ligne, conformité.

## 7. Budget et achats
Voir GDD §7.5. Ordre d'engagement des dépenses : marque (avant annonce, G3) → illustrateur capsule (G3) → compositeur (G4) → juriste (G5) → Steam Direct (dès que la page est prête, G3).

## 8. Rituels de communication
- Journal de dev hebdomadaire (`docs/devlog/AAAA-SS.md`) : fait / appris / prochain.
- Publication publique bimensuelle (clip + 3 lignes) dès G3.

## 9. Indicateurs de pilotage
| KPI | Cible |
|---|---|
| Vélocité (tickets/sprint) | stable ± 20 % |
| Bugs P0 ouverts | 0 en fin de sprint |
| Couverture de tests du cœur temporel | ≥ 90 % |
| Temps de CI | < 10 min |
| Wishlists (après page) | +100/semaine avant Next Fest, objectif 7 000 |
