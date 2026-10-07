# 80 — Playbook Claude Code (Unreal Engine 5.8)
Propriétaire : Product Owner · v2.0 (remplace la v1 Godot — ADR 0012)

## 1. Préparation (une fois, par l'humain)
1. **Matériel :** PC Windows 10/11 64 bits, GPU RTX 3070/4070 ou mieux (8 Go+ de VRAM), 32-64 Go de RAM, SSD NVMe 1 To libre, connexion fibre (téléchargements de 50-150 Go).
2. **Comptes (créés par l'humain, jamais par l'IA) :** Epic Games (moteur, Fab, MetaHuman), GitHub, Steamworks quand le jeu approche de G3.
3. **Installer :** Epic Games Launcher → Unreal Engine **5.8** (composants : *Editor symbols for debugging*, cibles Windows) ; Visual Studio 2022 (charges « Développement Desktop en C++ » et « Développement de jeux en C++ ») ou Rider ; Git + Git LFS ; Python 3.11+ ; Claude Code.
4. **Plugin officiel Epic pour Claude Code :** dans Claude Code, `/plugin install unreal-engine-skills-for-claude-code@claude-plugins-official`. Dans l'éditeur : activer les plugins **Model Context Protocol** et **AllToolsets**, puis démarrer le serveur (`ModelContextProtocol.StartServer` dans la console).
5. **Dépôts :** ce dépôt (public : conception, code, données) + un dépôt **privé** pour `game/Content/` (Git LFS ou Perforce).
6. Ouvrir un terminal à la racine et lancer `claude`, puis : « Lis AGENTS.md et lance le skill game-studio ».

## 2. Règles de pilotage
- Une phase = une ou plusieurs sessions ; toujours **mode plan** d'abord.
- **Sécurité éditeur :** le plugin MCP donne à l'IA un accès large à l'éditeur (y compris l'exécution de Python). Toujours travailler sur une branche, valider (commit) avant chaque série d'actions MCP, relire le diff.
- Revue humaine de chaque PR ; ouvrir l'éditeur et jouer 5 minutes.
- Agents parallèles seulement sur des zones indépendantes (ex. PCG de végétation ‖ UI ‖ landing page), jamais deux agents dans `TemporalCore` ou le réseau.
- Bug réseau ou de déterminisme : d'abord un test qui reproduit (graine + journal), puis la correction.

## 3. Séquence
| Phase | Prompt | Sortie | Porte |
|---|---|---|---|
| P0 | §4 P0 | projet UE 5.8, modules, CI Windows, ADR 0013-0020 | — |
| P1 | §4 P1 | prototype graine → arbre (blockout réaliste simple) | **G1** |
| P2 | §4 P2 | 4 joueurs en ligne (Steam) | G2 |
| P3 | §4 P3 | partie complète | **G3** |
| P4 | §4 P4 | monde réaliste, 30 recettes, prefabs | — |
| P5 | §4 P5 | musée, capsules, solo | — |
| P6 | §4 P6 | voix, streamer, saboteur | G4 |
| P7 | §4 P7 | conformité, accessibilité, localisation | **G5** |
| P8 | §4 P8 | démo, Steam, perf | G6 |
| M | §4 M | médias et trailer depuis le moteur | — |

## 4. Prompts (à coller tels quels)

**P0 — Fondations**
```
Lis CLAUDE.md, docs/design/40_TECHNICAL_DESIGN.md (v2) et docs/adr/0012. Mode plan.
Crée dans game/ un projet Unreal Engine 5.8 C++ "TemporalValley" avec les modules TemporalCore
(C++ pur, sans dépendance Engine dans le cœur), TemporalValley et TemporalValleyEditor ; active les
plugins listés au TDD §13 ; configure le staging de ../data ; .gitignore Unreal (Binaries, Intermediate,
Saved, DerivedDataCache) et exclusion de Content/ du dépôt public (sous-module privé). Ajoute la CI
(workflow pour runner Windows auto-hébergé : compilation Development Editor, tests Automation Spec en
-nullrhi, validate_data, privacy_scan) et les ADR 0013 à 0020. Vérifie avec le plugin MCP que l'éditeur
répond. Termine par la liste de ce que je dois faire moi-même.
```

**P1 — Prototype du fun**
```
Phase P1. TDD strict : écris d'abord les Automation Spec de SeededRng (vecteurs PCG32), ActionLog
(aller-retour, CRC), RecipeDB (chargement JSON, rejet d'une recette invalide), Propagator (seed,
seed_water, seed_cave, stones, trench, pose, chaînage 3 sauts, golden seed=42). Implémente-les.
Puis, via le plugin MCP : carte de test 100 × 100 m (Landscape simple, rivière Water plugin, grotte),
personnage troisième personne (template), interactions creuser/planter/empiler/poser, 2 époques
(Level Instances + éclairage), bascule F1, apparition 0,4 s, notification cause → effet.
Utilise des assets gratuits fournis par Epic pour le blockout. Aucune valeur en dur (data/tuning.json).
Arrête-toi aux critères de la phase et donne-moi un script de playtest de 10 minutes.
```

**P2 — Multijoueur**
```
Phase P2. TDD §6. Écris d'abord un test Gauntlet 1 hôte + 3 clients (200 actions aléatoires, hash
identique) et un Functional Test de rejet d'action hors portée. Implémente : sessions Online Subsystem
Steam (amis par défaut, AppID de test 480), RPC du journal, validation hôte, 4 époques, canaux de
collision par époque, fantômes, contrôle de hash 5 s + resync, reconnexion, capsule de reprise si
l'hôte part. Arrête-toi pour un playtest à 4.
```

**P3 — Boucle de partie**
```
Phase P3. docs/design/12 et 20 §1, §5-8. Machine à états de partie, contrats (data/contracts),
ContractEvaluator, ParadoxResolver, Chronomites, simulation des époques vides, Bouloche/Fiscalin/
Brigade en StateTree, allocation 2/3/4 joueurs, HUD Common UI (docs/32 §3), textes localisables
(clés de docs/11). Un test par cas limite de docs/12 §4. Arrête-toi pour le playtest G3 (8 personnes).
```

**P4 — Monde réaliste et contenu**
```
Phase P4. docs/design/21, 30, 33. Liste-moi d'abord les assets Fab/Megascans et MetaHuman nécessaires
(avec type de licence et coût estimé) : je les achète/télécharge moi-même. Ensuite : Landscape final de
la Vallée, 4 Level Instances d'époque, préréglages d'éclairage (33 §2), graphes PCG déterministes
pilotés par FEraState, 30 recettes (propose d'abord les 10 croisées), prefabs Packed Level Actor par
saut, matériaux fantôme/glitch/apparition, Niagara, MetaSounds. Mesure les perfs (Insights) sur les
profils du TDD §10.
```

**P5 — Machine à clips**
```
Phase P5. Chronique (data/phrases), Musée (LI_Museum, statues = pose figée MetaHuman), carte-récap
1080×1350 générée par le jeu, capsules CT1 (test aller-retour + test sans donnée personnelle),
Solo Relais + tutoriel (docs/11 §1), mode photo.
```

**P6 — Voix, streamer, social**
```
Phase P6. Steam VoIP + submix inter-époques (data/tuning.json voice), PTT/VAD, mute/blocage/
signalement, test « aucun audio sur disque », mode streamer opt-in (TDD §9), noms de statues filtrés,
masquage du code d'invitation, mode Saboteur, roue de pings et emotes.
```

**P7 — Conformité**
```
Phase P7. Délègue à legal-compliance et game-qa : écran de consentement, menu Confidentialité,
télémétrie no-op sans consentement, crédits et licences, toutes les options de docs/32 §6,
localisation FR/EN complète, pseudo-loc, intégration des textes de legal/ (après validation juridique).
```

**P8 — Démo et Early Access**
```
Phase P8. Build démo (chapitre 1, 2 époques) sur la branche Steam demo, succès, classement du Défi du
jour, Steam Cloud, Rich Presence, profilage sur les 3 profils du TDD §10, BuildCookRun Shipping,
CHANGELOG, presskit (brouillon). Rapport G6 par game-qa.
```

**M — Médias depuis le moteur**
```
Applique marketing-launch : rends les plans de data/shotlist.json avec Movie Render Graph et la
capture haute résolution, produis le trailer d'annonce (Sequencer) et la version verticale, puis
les titrages avec Remotion. Aucune image hors moteur. Liste les images à faire valider dans
media/APPROVALS.md.
```

## 5. Ce que l'IA ne fait jamais seule
Achats (Fab, Steam Direct, freelances), création de comptes, choix du nom et du prix, textes publics, publication (GitHub public, Steam, réseaux), signature de contrats, ajout d'un asset tiers sans vérification de licence, poussée de `Content/` vers un dépôt public.
