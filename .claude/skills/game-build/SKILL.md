---
name: game-build
description: Développe le jeu « 300 Years Later » dans Unreal Engine 5.8 (C++ + Blueprints + Python d'éditeur, piloté via le plugin MCP officiel d'Epic) phase par phase (P0 → P8), en TDD, selon le TDD normatif docs/design/40 et data/tuning.json. Utiliser pour toute tâche de développement du jeu dans game/.
---

# Skill : game-build

## Avant de coder
1. Lis `CLAUDE.md`, `docs/design/40_TECHNICAL_DESIGN.md` (v2), `docs/adr/0012`, `docs/design/20_GAME_DESIGN_PARAMETERS.md`, puis le prompt de la phase dans `docs/design/80_CLAUDE_CODE_PLAYBOOK.md` §4.
2. `python3 tools/doctor.py` : Unreal 5.8, dotnet, git-lfs requis ; éditeur ouvert avec le serveur MCP démarré pour les tâches d'éditeur.
3. **Mode plan** : fichiers C++/assets touchés, tests écrits d'abord, critères d'acceptation, risques.
4. Commit propre avant toute série d'actions MCP (l'IA a un accès large à l'éditeur).

## Répartition des outils
| Besoin | Outil |
|---|---|
| Cœur temporel déterministe | C++ pur dans `Source/TemporalCore` + Automation Spec |
| Gameplay, réseau, UI | C++ (`Source/TemporalValley`) + Blueprints minces pour l'assemblage |
| Placement d'acteurs, PCG, matériaux, Niagara, Sequencer | plugin MCP (toolsets d'Epic) ou Python d'éditeur (`game/Scripts/`) |
| Données de jeu | `data/` (JSON validés) — jamais de valeurs en dur |

## Phases et preuves exigées
| Phase | Preuves (commandes ou artefacts) |
|---|---|
| P0 | compilation Development Editor OK ; Automation Spec vides verts en `-nullrhi` ; CI Windows verte ; ADR 0013-0020 |
| P1 | Automation Spec TemporalCore verts + golden ; vidéo de capture 30 s graine → arbre (pour l'humain, pas pour publication) |
| P2 | Gauntlet 1+3 clients : hash identiques après 200 actions ; Functional Test de rejet |
| P3 | un test par cas limite (`docs/design/12` §4) ; partie complète jouée par bots |
| P4 | `validate_data.py` ; 10 graines sans échec PCG ; rapport Insights sur 3 profils |
| P5 | test aller-retour capsule ; test « aucune donnée personnelle » |
| P6 | test statique + exécution « aucun audio sur disque » |
| P7 | rapports `legal-compliance` et `game-qa` verts |
| P8 | BuildCookRun Shipping ; rapport G6 |

## Commandes de référence (Windows)
```bat
"%UE_ROOT%\Engine\Build\BatchFiles\Build.bat" TemporalValleyEditor Win64 Development -Project="%CD%\game\TemporalValley.uproject"
"%UE_ROOT%\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" "%CD%\game\TemporalValley.uproject" -ExecCmds="Automation RunTests TemporalCore;Quit" -unattended -nullrhi -nosplash -log
"%UE_ROOT%\Engine\Build\BatchFiles\RunUAT.bat" BuildCookRun -project="%CD%\game\TemporalValley.uproject" -platform=Win64 -clientconfig=Shipping -build -cook -stage -pak -archive -archivedirectory="%CD%\build"
```

## Règles spécifiques Unreal
- `Content/` vit dans le dépôt **privé** ; ne jamais l'ajouter au dépôt public ; vérifier `git status` avant chaque commit.
- Pas d'asset Fab/Megascans/MetaHuman ajouté sans que l'humain l'ait acquis et sans ligne dans `THIRD_PARTY_LICENSES.md`.
- Pas de `FMath::Rand`, `FPlatformTime`, `float` dans `TemporalCore` (revue + test).
- Toute chaîne joueur via `FText` / tables de chaînes localisables.

## Fin de phase
Preuves dans `docs/qa/phase-N.md`, `STUDIO_STATE.md` et `CHANGELOG.md` à jour, tag `phase-N`, **arrêt** et script de playtest.
