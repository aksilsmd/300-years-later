# Démarrage rapide (10 minutes)

## Ce que vous obtenez
Un **studio de jeu vidéo piloté par IA** : la conception complète d'un jeu coop 3D réaliste (*300 Years Later*), un corpus juridique, une landing page, des tests, et surtout des **skills** qui permettent à Claude Code (ou à une autre IA) de construire le jeu dans Unreal Engine 5.8, étape par étape, en s'arrêtant à chaque décision qui vous revient.

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
> Lis AGENTS.md puis lance le skill game-studio. Fais l'étape A (diagnostic) et présente-moi le plan de l'étape B. N'installe rien avant mon accord.

## Ensuite
Suivez le [guide de A à Z](01_GUIDE_A_Z.md). À chaque porte (G1, G3, G5…), l'IA s'arrête et vous demande un playtest ou une décision : c'est voulu.
