# Temps, coûts et consommation

> Estimations d'ordre de grandeur au 7 octobre 2026, pour un jeu coop **3D réaliste** sous Unreal Engine 5.8 tel que décrit dans `docs/design/`. Elles servent à décider, pas à promettre. Mesurez vos chiffres réels à chaque porte et ajustez.

## 1. Trois scénarios
| | A — Solo + IA | B — Studio réduit | C — Petite équipe |
|---|---|---|---|
| Composition | porteur du projet (temps partiel) + Claude Code + freelances ponctuels | porteur à plein temps + 2-3 freelances réguliers (art 3D, animation, son) | 5-8 personnes (prog. gameplay, tech art, 2 artistes, animateur, producteur/QA) + IA |
| Durée jusqu'à l'Early Access | 30-48 mois | 18-30 mois | 15-24 mois |
| Budget hors rémunération du porteur | **≈ 40 000 – 80 000 €** | **≈ 150 000 – 300 000 €** | **≈ 500 000 € – 1,2 M€** |
| Niveau visuel atteignable | réaliste grâce aux assets achetés, animations surtout issues des bibliothèques | réaliste cohérent, créatures et PNJ sur mesure | réaliste soigné, capture de jeu d'acteur, contenu plus riche |
| Risque principal | durée et périmètre | trésorerie | coût fixe mensuel |

## 2. Postes de dépense (fourchettes)
| Poste | Scénario A | Scénario C | Remarques |
|---|---|---|---|
| Poste de travail (si nécessaire) | 2 000 – 3 500 € | 2 500 € × personnes | GPU RTX 4070+, 64 Go conseillés |
| Unreal Engine | 0 € | 0 € | 5 % au-delà de 1 M$ de revenus bruts cumulés |
| Assets Fab / Megascans | 1 000 – 6 000 € | 8 000 – 30 000 € | Megascans payants depuis 2025 |
| Créatures (sculpt, groom, rig) | 3 000 – 10 000 € | 15 000 – 40 000 € | Bouloche, chèvres, Chronomites |
| Capture faciale / corporelle | 0 – 3 000 € | 15 000 – 60 000 € | MetaHuman Animator (vidéo) vs studio de mocap |
| Musique (6 pistes + stingers) | 3 000 – 8 000 € | 10 000 – 30 000 € | cession de droits incluse |
| Design sonore complémentaire | 1 000 – 4 000 € | 8 000 – 25 000 € | |
| Capsule Steam, logo, illustrations | 1 500 – 4 000 € | 5 000 – 15 000 € | |
| Montage et étalonnage du trailer | 1 000 – 3 000 € | 5 000 – 20 000 € | |
| Localisation (≈ 15 000 mots × 7 langues) | 8 000 – 16 000 € | 12 000 – 25 000 € | tarifs professionnels au mot ; relecture native |
| Juridique (CGU, confidentialité, contrats, AIPD) | 2 000 – 6 000 € | 8 000 – 20 000 € | |
| Marque (UE, 1-3 classes) | 850 – 1 500 € | 2 000 – 5 000 € | + international si besoin |
| Expert-comptable, assurance RC pro | 1 500 – 3 500 €/an | 4 000 – 10 000 €/an | |
| Steam Direct | ≈ 100 $ | ≈ 100 $ | par jeu |
| Playtests et QA externe | 500 – 3 000 € | 10 000 – 40 000 € | |
| Marketing (salons, relations presse, publicité) | 2 000 – 10 000 € | 30 000 – 150 000 € | |
| Abonnement à l'assistant IA | selon l'offre choisie | selon l'offre × personnes | voir les offres sur support.claude.com |
| Salaires de l'équipe | — | 400 000 € – 900 000 € | principal poste du scénario C |

Aides possibles en France à étudier : crédit d'impôt jeux vidéo (conditions strictes), fonds d'aide au jeu vidéo du CNC, Bpifrance, aides régionales (`legal/20_fiscalite-redevances.md`).

## 3. Calendrier par phase (scénario B)
| Phase | Durée | Porte | Ce qui se passe |
|---|---|---|---|
| A-C Diagnostic, installation, personnalisation | 1-2 semaines | — | poste prêt, titre choisi |
| P0 Fondations | 2-3 semaines | — | projet Unreal, CI, ADR |
| P1 Prototype du fun | 4-8 semaines | **G1** | graine → arbre jouable, 5 testeurs |
| P2 Multijoueur | 6-10 semaines | G2 | 4 joueurs en ligne sans désynchronisation |
| P3 Boucle de partie | 8-12 semaines | **G3** | partie complète, page Steam, premiers clips |
| P4 Monde réaliste et contenu | 6-12 mois | — | le plus long : assets, PCG, prefabs, MetaHumans |
| P5 Machine à clips | 6-10 semaines | — | musée, capsules, solo |
| P6 Voix, streamer, saboteur | 6-8 semaines | G4 | alpha |
| P7 Conformité, accessibilité, localisation | 8-12 semaines | **G5** | bêta, relecture juridique |
| P8 Démo et Early Access | 8-12 semaines | G6 | démo, Next Fest, lancement |

## 4. Consommation de l'IA (ordre de grandeur)
- **Temps d'agent** : une phase de code représente typiquement de 20 à 80 sessions de travail de Claude Code, de 30 minutes à quelques heures chacune ; la phase P4 est la plus gourmande (nombreuses opérations dans l'éditeur via MCP).
- **Jetons** : très variable selon la taille du projet, la mise en cache et le nombre d'opérations d'éditeur. Comptez plusieurs millions de jetons par journée de travail intensive. Mesurez votre consommation réelle (commande de coût/usage de votre outil) dès la phase P0 et reportez-la dans `STUDIO_STATE.md` pour extrapoler.
- **Leviers d'économie** : une phase par session, mode plan d'abord, petites PR, tests ciblés, éviter de relire tout le dépôt à chaque session (le skill `game-studio` lit `STUDIO_STATE.md` en premier).
- **Temps humain incompressible** : revues de PR (≈ 20-30 % du temps d'agent), playtests, achats d'assets, direction artistique, validation des médias et des textes, décisions de porte.

## 5. Ce qui fait exploser les estimations
Le périmètre (ajouter une époque, un biome, un mode), la qualité des humains réalistes, la capture de mouvement, la localisation tardive, et l'absence de playtests tôt. La règle de coupe de `docs/design/50_PRODUCTION_PLAN.md` §6 s'applique avant toute rallonge budgétaire.
