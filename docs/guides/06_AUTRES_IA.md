# Utiliser le kit avec d'autres IA

| Outil | Comment |
|---|---|
| **Claude Code** | natif : skills dans `.claude/skills/`, règles dans `CLAUDE.md`, permissions dans `.claude/settings.json`, plugin officiel Epic pour Unreal |
| Codex, Gemini CLI, Aider, Cursor, Copilot | lisent `AGENTS.md`, qui pointe vers les skills comme procédures Markdown |
| Agent sans accès à l'éditeur Unreal | Python d'éditeur en ligne de commande : `UnrealEditor-Cmd.exe <projet> -run=pythonscript -script=game/Scripts/<script>.py` et compilation via `Build.bat` |

**Prompt universel :**
> Lis AGENTS.md puis `.claude/skills/game-studio/SKILL.md`. Applique le contrat de sécurité. Fais l'étape A (diagnostic) et présente-moi le plan de l'étape B. N'installe rien avant mon accord.

Quel que soit l'outil : reproduisez les règles `deny` de `.claude/settings.json` dans sa configuration de permissions, et lancez `tools/privacy_scan.py` avant chaque commit.
