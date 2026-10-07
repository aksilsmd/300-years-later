# Installation du poste de studio

## 1. Matériel
| | Minimum pratique | Recommandé |
|---|---|---|
| Système | Windows 10 64 bits | Windows 11 64 bits |
| Processeur | 8 cœurs | 12-16 cœurs (compilation C++ et shaders) |
| Mémoire | 16 Go (lent) | 32-64 Go |
| Carte graphique | 8 Go de VRAM (RTX 2070 / RX 6600 XT) | RTX 3070/4070 ou mieux, 12 Go+ |
| Stockage | 300 Go SSD | 1 To NVMe |
| Réseau | fibre conseillée | moteur + assets = 100-200 Go à télécharger |
macOS est possible pour Unreal (Epic Games Launcher + Xcode) mais le projet cible d'abord Windows. Linux sert pour les outils annexes (landing, tests).

## 2. Logiciels
Le skill `studio-setup` installe tout via `winget` après votre accord :
```powershell
powershell -ExecutionPolicy Bypass -File .claude/skills/studio-setup/scripts/install_windows.ps1 -Plan   # voir le plan
powershell -ExecutionPolicy Bypass -File .claude/skills/studio-setup/scripts/install_windows.ps1         # installer
```
| Outil | Pourquoi |
|---|---|
| Epic Games Launcher + **Unreal Engine 5.8** | moteur (installation dans le launcher, par vous) |
| Visual Studio 2022 (jeux C++ + bureau C++) ou Rider | compilation |
| .NET 8, Git, Git LFS, GitHub CLI, Python 3.12 | outils de build et du kit |
| Node LTS, ffmpeg | landing page, vidéo |
| Blender LTS | retouches d'assets |
| Robot Framework, k6, gitleaks, semgrep | tests et sécurité |

## 3. Brancher Claude Code sur Unreal (plugin officiel Epic)
1. Dans Claude Code : `/plugin install unreal-engine-skills-for-claude-code@claude-plugins-official`
2. Dans l'éditeur Unreal : *Edit › Plugins*, activer **Model Context Protocol** et **AllToolsets**, redémarrer.
3. Console de l'éditeur : `ModelContextProtocol.StartServer`
4. Sous Windows, Git Bash (installé avec Git) doit être sur le `PATH`.
5. Test : demandez à Claude « liste les acteurs de la carte ouverte ».
> ⚠️ Ce plugin donne à l'IA un accès large à l'éditeur, y compris l'exécution de Python. Travaillez toujours sur une branche Git et validez (commit) avant chaque série d'opérations.

## 4. Variables et dossiers
```powershell
setx UE_ROOT "C:\Program Files\Epic Games\UE_5.8"
```
Créez un dépôt **privé** pour `game/Content/` (Git LFS ou Perforce). Ne publiez jamais ce dossier.

## 5. Vérifier
```powershell
py tools\doctor.py
```
Toutes les lignes utiles doivent être ✓.
