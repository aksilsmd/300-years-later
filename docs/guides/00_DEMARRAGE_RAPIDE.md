# Démarrage rapide (10 minutes)

🇬🇧 [English version](en/00_QUICK_START.md)

## Ce que vous obtenez
Un **studio de jeu vidéo piloté par IA** : la conception complète d'un jeu coop 3D réaliste (*300 Years Later*), un corpus juridique, une landing page cinématique, des tests, et surtout des **skills** qui permettent à Claude Code (ou à une autre IA) de construire le jeu dans Unreal Engine 5.8, en autonomie de A à Z, en ne vous sollicitant qu'aux décisions qui vous reviennent.

## Ce dont vous avez besoin
- Un PC Windows 10/11 avec une carte graphique récente (RTX 3070/4070 ou mieux), 32 Go de RAM, 300 Go libres — détails dans [02_INSTALLATION.md](02_INSTALLATION.md).
- Claude Code (ou un autre agent de code) et un compte Epic Games.
- Du temps et un budget réalistes : lisez [03_TEMPS_ET_COUTS.md](03_TEMPS_ET_COUTS.md) avant de vous lancer.

## Les 5 premières commandes
```bash
git clone <URL-DE-CE-DÉPÔT> 300-years-later && cd 300-years-later
python3 tools/doctor.py          # ce qui est installé / ce qui manque
python3 tools/validate_data.py   # les données du jeu sont cohérentes
python3 tools/privacy_scan.py    # aucune donnée personnelle ni secret
claude                            # lance Claude Code dans le dossier
```
Puis tapez dans Claude Code :
> Lis AGENTS.md puis applique le skill game-studio. Travaille en autonomie de A à Z selon studio.config.yaml ; ne me sollicite qu'aux arrêts obligatoires, en regroupant tes questions avec ta recommandation. Réponds-moi en français.
> *(facultatif)* Instructions en plus : …

Vous préférez garder la main ? Mettez `autonomy.level: guided` dans `studio.config.yaml` (l'IA demande avant chaque étape). Vous voulez qu'elle installe aussi sans demander ? `full`.

## Régler l'IA une fois pour toutes : `studio.config.yaml`
| Clé | Effet |
|---|---|
| `autonomy.level` | `guided` · `autonomous` (défaut) · `full` |
| `autonomy.max_questions_per_session` | nombre maximal de questions par session (défaut 3) |
| `project.languages` | langues du jeu et des textes publics (défaut fr, en) |
| `defaults.*` | scénario d'équipe, budget assets mensuel, direction artistique, mode de la landing… |
| `extra_instructions` | vos consignes libres, appliquées à chaque session |

Votre message l'emporte toujours sur ce fichier.

## Ensuite
L'IA avance seule et tient trois fichiers à jour : `STUDIO_STATE.md` (où on en est), `DECISIONS.md` (ce qu'elle a décidé seule, réversible), `QUESTIONS.md` (ce qu'elle attend de vous, avec sa recommandation — répondez « ok » pour l'accepter). Les arrêts obligatoires (comptes, installation d'Unreal, achats, publication…) sont décrits dans le [guide de A à Z](01_GUIDE_A_Z.md).
