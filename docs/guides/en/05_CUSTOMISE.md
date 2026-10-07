# Customise the project (or make it your own game)

🇫🇷 [Version française](../05_PERSONNALISER.md)

Everything is designed to be changed. Licence: MIT code, CC BY 4.0 content (credit "The 300 Years Later contributors"). The title and trademark are not covered by the licence.

## 1. Tell the AI what you want
- **Once:** `extra_instructions` in `studio.config.yaml` (e.g. "English first, Steam Deck verified is a priority, no voice chat").
- **Per session:** add your instructions after the start prompt. They override the config; only the safety contract cannot be lifted.

## 2. Change the title
1. Choose a title and run a trademark search (`legal/21_marque-pi.md`).
2. Ask the AI: "Replace the public title "300 Years Later" with "<NEW TITLE>" everywhere it is public (READMEs, landing, Remotion, docs/design/70), without touching the codename CENTURY TEMPS or technical identifiers."
3. Check: `python3 tools/privacy_scan.py` and the landing tests.

## 3. Change the game without coding
| You want to… | Edit | Check |
|---|---|---|
| add a transformation over time | `data/recipes/*.json` (format: `data/schemas/recipe.schema.json`) + a Chronicle template in `data/phrases/` | `python3 tools/validate_data.py` |
| add a contract | `data/contracts/*.json` | same |
| tune round length, speeds, scoring | `data/tuning.json` | playtest |
| change an era's look | `docs/design/33_VISUAL_TARGETS.md` §2 then ask the AI to apply it | visual review |
| add a trailer or landing shot | `data/shotlist.json` | render + approval |

## 4. Reuse the studio for another game
The skills (`.claude/skills/`) are 80 % generic: replace `docs/design/` with your own design (keeping the same file structure), adapt `CLAUDE.md` and `studio.config.yaml`, then run `game-studio`. Keep the safety contract, decision gates and legal pack as a base.
