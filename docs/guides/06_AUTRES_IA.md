# Utiliser le kit avec d'autres IA

🇬🇧 [English version](en/06_OTHER_AIS.md)

| Outil | Comment |
|---|---|
| **Claude Code** | natif : skills dans `.claude/skills/`, règles dans `CLAUDE.md`, permissions dans `.claude/settings.json`, plugin officiel Epic pour Unreal |
| Gemini CLI | lit `GEMINI.md`, qui importe `AGENTS.md` |
| GitHub Copilot | lit `.github/copilot-instructions.md`, qui renvoie à `AGENTS.md` |
| Kimi, Codex, Aider, Cursor, Windsurf, autres | lisent `AGENTS.md` (sinon : « Lis AGENTS.md » en premier message), qui pointe vers les skills comme procédures Markdown |
| Agent sans accès à l'éditeur Unreal | Python d'éditeur en ligne de commande : `UnrealEditor-Cmd.exe <projet> -run=pythonscript -script=game/Scripts/<script>.py` et compilation via `Build.bat` |

**Prompt universel :**
> Lis AGENTS.md puis applique le skill game-studio. Travaille en autonomie de A à Z selon studio.config.yaml ; ne me sollicite qu'aux arrêts obligatoires, en regroupant tes questions avec ta recommandation. Réponds-moi en français.
> *(facultatif)* Instructions en plus : …

Quel que soit l'outil : reproduisez les règles `deny` de `.claude/settings.json` dans sa configuration de permissions, et lancez `tools/privacy_scan.py` avant chaque commit.

Si l'outil n'a pas de skill `frontend-design`, la landing suit strictement `docs/design/34_LANDING_CINEMATIQUE.md` et `30_ART_BIBLE.md`. Si l'outil ne gère pas les plugins, l'installation du plugin Epic se fait côté Claude Code ou est remplacée par le Python d'éditeur.
