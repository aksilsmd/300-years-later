# Customise the project (or make it your own game)

🇫🇷 [Version française](../05_PERSONNALISER.md)

Everything is designed to be changed. Licence: MIT code, CC BY 4.0 content (credit "The 300 Years Later contributors"). The title and trademark are not covered by the licence.

## 1. Tell the AI what you want
- **Once:** `extra_instructions` in `studio.config.yaml` (e.g. "English first, Steam Deck verified is a priority, no voice chat").
- **Per session:** add your instructions after the start prompt. They override the config; only the safety contract cannot be lifted.

## 2. Change the title
The project carries three names on purpose: the **codename** (CENTURY TEMPS), the **public title**
("Afterloom" today) and the **repository slug** (`300-years-later`, which every URL is built from).
To change only the second:

1. Choose a title and run a trademark search (`legal/21_marque-pi.md`) — that is a human step.
2. ```bash
   python3 tools/apply_public_title.py --to "New Title"           # preview, file by file
   python3 tools/apply_public_title.py --to "New Title" --apply   # write
   ```
3. Check: `python3 tools/repo_audit.py && python3 tools/privacy_scan.py && python3 -m pytest tests/web -q`

The tool never touches the repository slug, the codename, the valley name, the French pitch line "300 ans plus
tard", or the licence attribution entity; it prints what it left alone and why. **Renaming the repository
itself is a separate decision** — GitHub keeps redirects, but it breaks the plugin path, the badges and every
shared link. See [ADR 0021](../../adr/0021-titre-public-afterloom.md).

## 2 bis. The repository's "About" box
The description, website and topics at the top of the GitHub page are **not** in the code — they are repository
settings. No agent can write them, and no `git push` changes them. Their source of truth is
[`.github/about.yml`](../../../.github/about.yml); `bash tools/setup_repo.sh` applies it with your own token,
and prints the text to paste if a write is refused.

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
