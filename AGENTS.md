# AGENTS.md — instructions pour toute IA de code

Ce dépôt est un **studio de jeu vidéo piloté par IA** pour un jeu coop **3D réaliste sous Unreal Engine 5.8**. Il fonctionne nativement avec Claude Code (skills dans `.claude/skills/`) et avec d'autres agents (Codex, Gemini CLI, Cursor, Copilot, Aider…) qui lisent ce fichier.

## Si votre outil ne charge pas les « skills »
Les skills sont de simples fichiers Markdown. Lisez-les comme des procédures, dans cet ordre :
1. `.claude/skills/game-studio/SKILL.md` — **point d'entrée** (parcours A → Z, contrat de sécurité).
2. `.claude/skills/studio-setup/SKILL.md` — installation des outils.
3. `.claude/skills/game-build/SKILL.md` — code du jeu par phases.
4. `.claude/skills/game-assets/SKILL.md` — modèles 3D, shaders, sons.
5. `.claude/skills/game-qa/SKILL.md` — tests, charge, sécurité, conformité.
6. `.claude/skills/legal-compliance/SKILL.md` — RGPD, licences, Steam.
7. `.claude/skills/marketing-launch/SKILL.md` — médias, trailer, landing page, lancement.
8. `.claude/skills/privacy-guard/SKILL.md` — avant tout commit ou publication.

Puis appliquez les règles de `CLAUDE.md` (elles valent pour tous les agents). Si votre agent ne peut pas piloter l'éditeur Unreal via MCP, utilisez le Python d'éditeur (`UnrealEditor-Cmd.exe -run=pythonscript -script=...`) et la compilation en ligne de commande.

## Règles absolues (résumé)
- Ne lisez aucun fichier hors du dépôt ; aucun secret ; aucune donnée envoyée hors de la machine.
- Aucun traceur, cookie ou CDN externe.
- Aucun achat, compte, publication ou signature sans l'humain.
- Aucune image de jeu produite hors du moteur ; aucun asset Epic/Fab/MetaHuman dans un dépôt public.
- `python3 tools/privacy_scan.py && python3 tools/validate_data.py` avant chaque commit.

## Prompt de démarrage universel
> Lis AGENTS.md puis `.claude/skills/game-studio/SKILL.md`. Applique le contrat de sécurité. Fais l'étape A (diagnostic) et présente-moi le plan de l'étape B. N'installe rien avant mon accord.
