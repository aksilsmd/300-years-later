---
name: studio-setup
description: Diagnostique et installe le poste de studio pour un jeu Unreal Engine 5.8 réaliste — Epic Games Launcher, Visual Studio 2022, .NET 8, Git LFS, plugin officiel Epic pour Claude Code (MCP), Node, ffmpeg, Blender, Robot Framework, k6, gitleaks, semgrep — depuis les sources officielles, avec vérification matérielle. Utiliser au premier lancement, quand un outil manque ou pour changer de version.
---

# Skill : studio-setup

## Règles
- Versions épinglées dans `tools/versions.env`. Sources officielles uniquement (winget/Homebrew/apt, sites des éditeurs). Jamais `curl | sh`.
- **L'humain** crée les comptes (Epic, GitHub, Steamworks), accepte les licences (CLUF Unreal, Visual Studio) et se connecte au launcher. Tu ne saisis jamais d'identifiants.
- `sudo`/administrateur seulement après avoir montré la commande et obtenu l'accord.

## Procédure
1. `python3 tools/doctor.py` (ou `py tools\doctor.py`) → ce qui manque.
2. Vérifie le matériel (le script Windows l'affiche) : GPU RTX 3070/4070+ recommandé, 32-64 Go de RAM, 300 Go libres. S'il est insuffisant, **préviens** : le développement Unreal réaliste sera lent ou impossible ; propose de ne faire que les volets conception/marketing/landing.
3. Windows : `powershell -ExecutionPolicy Bypass -File .claude/skills/studio-setup/scripts/install_windows.ps1 -Plan`, montre le plan, puis exécute sans `-Plan` après accord.
   macOS/Linux (outils annexes) : `bash .claude/skills/studio-setup/scripts/install_tools_unix.sh --plan`.
4. Guide l'humain pour les étapes manuelles affichées (installation d'UE 5.8 dans le launcher, plugin Claude Code, activation du serveur MCP dans l'éditeur, variable `UE_ROOT`).
5. Vérifie la connexion MCP : demande la liste des acteurs de la carte ouverte via le plugin ; si elle échoue, consulte la documentation du plugin et corrige la configuration.
6. Relance `doctor.py` ; écris `docs/DEPENDENCIES.md` (outil, version exacte, licence, source, date).

## Plugins et outils utilisés par les autres skills
| Élément | Rôle | Licence / coût |
|---|---|---|
| Unreal Engine 5.8 | moteur | gratuit < 1 M$ de revenus cumulés, puis 5 % (Epic Games Store exonéré) |
| Plugin Epic « Unreal Engine skills for Claude Code » + plugins éditeur Model Context Protocol / AllToolsets | piloter l'éditeur (acteurs, Blueprints, matériaux, Niagara, Sequencer, tests) | MIT (plugin Claude) |
| Visual Studio 2022 ou Rider | compilation C++ | Community gratuit sous conditions Microsoft / Rider payant |
| Fab (Megascans, kits) | assets photoréalistes | **payant** depuis 2025 (Standard/Professional) — l'humain achète |
| MetaHuman (Creator intégré à l'éditeur) | humains réalistes | gratuit < 1 M$ de revenus annuels |
| Online Subsystem Steam | sessions, voix, succès | inclus dans UE ; Steamworks : frais Steam Direct |
| Git LFS ou Perforce | contenu binaire (privé) | gratuit/payant selon l'hébergeur |
| Node, Remotion, Vite, React, Framer Motion | landing page, motion design | MIT ; **Remotion : licence d'entreprise payante au-delà d'un seuil** — vérifier |
| Robot Framework, k6, gitleaks, semgrep | tests et sécurité | Apache/AGPL/MIT/LGPL (outils) |

## Dépannage
- MCP ne répond pas : l'éditeur doit être ouvert, plugins activés, serveur démarré ; sous Windows le plugin Claude a besoin de Git Bash ou WSL sur le PATH.
- Compilation lente : activer le cache DDC partagé, exclure les dossiers du projet de l'antivirus (avec accord de l'humain).
- Proxy d'entreprise : configurer les certificats de l'entreprise ; ne jamais désactiver TLS.
