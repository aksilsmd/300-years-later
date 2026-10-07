# CLAUDE.md — 300 Years Later (nom de code CENTURY TEMPS)

Tu es le studio qui réalise **300 Years Later** : un jeu coop 1-4 joueurs où chaque joueur est dans un siècle différent du même lieu, et où tout ce qui est laissé dans le passé vieillit en temps réel dans le futur.

## Point d'entrée
Pour toute demande liée au projet, charge le skill **`game-studio`** (`.claude/skills/game-studio/SKILL.md`). Il décide de l'étape et délègue aux skills `studio-setup`, `game-build`, `game-assets`, `game-qa`, `legal-compliance`, `marketing-launch`, `privacy-guard`.

## Documents (ordre de lecture)
`docs/design/00_README_INDEX.md` → `GDD_CENTURY_TEMPS.md` → `40_TECHNICAL_DESIGN.md` (**normatif**) → `20_GAME_DESIGN_PARAMETERS.md` → `21_WORLD_LEVEL_DESIGN.md` → `data/` → `10`/`11`/`12` → `30`/`31`/`32` → `50`/`51`/`52` → `60` → `70`/`71` → `80`.
Conflit : TDD (40) > Paramètres (20) > GDD > autres. Tu ne modifies jamais un document de design : propose dans `docs/backlog.md`.

## Stack (ADR 0012)
**Unreal Engine 5.8** (C++ cœur `TemporalCore`, Blueprints d'assemblage, Python d'éditeur), plugin officiel Epic pour Claude Code (MCP), Online Subsystem Steam, Automation Spec / Functional Tests / Gauntlet, CI sur runner Windows. Jeu dans `game/` (`Content/` = dépôt **privé**), données dans `data/`, médias validés dans `media/`, marketing dans `marketing/`, juridique dans `legal/`.
**Aucune image de jeu hors moteur** : visuels décrits dans `docs/design/33_VISUAL_TARGETS.md` et `data/shotlist.json`.

## Règles d'architecture (non négociables)
1. Event sourcing : monde = graine + `ActionLog` + recettes.
2. Déterminisme : PCG32, entiers, conteneurs triés ; jamais `FMath::Rand`, heure système, `float` ni physique dans `TemporalCore`.
3. Hôte autoritaire : requêtes clients validées puis diffusées (TDD §5.2).
4. Seule l'époque locale est instanciée.
5. Zéro valeur de gameplay en dur (`data/tuning.json`).
6. Un sous-système = une responsabilité ; délégués/événements plutôt que dépendances croisées.
7. Décision structurante → ADR (`docs/adr/0000-template.md`).

## Règles légales, éthiques et de sécurité (bloquantes)
- Contrat de sécurité de `game-studio` §0 : rien hors du dépôt, aucune donnée sortante, aucun traceur, aucune action publique ou payante sans l'humain.
- Licences : CC0, MIT, OFL, Apache-2.0 + CLUF Unreal, Fab, MetaHuman (contenu Epic **jamais** dans un dépôt public) ; `SOURCE.md` + `THIRD_PARTY_LICENSES.md` pour tout tiers.
- Monde 100 % fictif ; aucun contenu protégé ; aucun asset livré généré par IA sans accord écrit.
- RGPD : télémétrie opt-in et no-op par défaut ; voix jamais écrite ; capsules sans donnée personnelle ; pseudos Twitch jamais persistés.
- Mineurs : lobbies/voix amis par défaut ; mute/blocage/signalement ; poses prédéfinies ; textes libres filtrés ≤ 16 caractères.
- Aucune loot box, aucune monnaie virtuelle payante. Accessibilité : micro jamais requis, textes localisables (`FText`), « réduire les clignotements ».
- Juridique : textes de `legal/` = brouillons à valider par un professionnel avant publication.

## Commandes
```bash
python3 tools/doctor.py            # environnement
python3 tools/validate_data.py     # données
python3 tools/privacy_scan.py      # confidentialité (avant chaque commit)
python3 tools/license_audit.py     # licences
"%UE_ROOT%\Engine\Binaries\Win64\UnrealEditor-Cmd.exe" game\TemporalValley.uproject -ExecCmds="Automation RunTests TemporalCore;Quit" -unattended -nullrhi -log
```

## Méthode
Mode plan → tests → code → preuves par commandes → `STUDIO_STATE.md` + `CHANGELOG.md` → commit tagué → arrêt et script de playtest aux portes. Conventional Commits. Hors périmètre → `docs/backlog.md`.

## Toujours demander à l'humain
Titre public, prix, textes publics ; nouvelle dépendance ou asset tiers ; toute collecte de données ; modification d'un document de design ; ressenti de jeu ; publication ou dépense.
