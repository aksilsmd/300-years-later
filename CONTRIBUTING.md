# Contribuer

Merci ! Ce projet est un **kit de studio de jeu piloté par IA**. Les contributions les plus utiles :
- nouvelles **recettes de vieillissement** dans `data/recipes/` (validées par `tools/validate_data.py`) ;
- nouveaux **modèles de Chronique** FR/EN dans `data/phrases/` ;
- traductions ;
- améliorations des **skills** (`.claude/skills/`) testées sur un vrai run ;
- retours de run complets (« j'ai lancé la phase 3, voici ce qui a coincé »).

## Règles
1. `python3 tools/validate_data.py && python3 tools/privacy_scan.py` doivent passer.
2. Aucun contenu protégé (personnage, marque, musique, police non libre).
3. Aucun asset généré par IA sans le déclarer dans la PR.
4. Commits au format Conventional Commits (`feat:`, `fix:`, `docs:`…).
5. Respectez le [code de conduite](CODE_OF_CONDUCT.md).

## Workflow
Fork → branche `feat/ma-recette` → PR avec le modèle fourni → revue → fusion.
