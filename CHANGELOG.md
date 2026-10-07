# Journal des modifications
Format : Keep a Changelog · Versionnage sémantique.

## [0.4.1] — 2026-10-07
### Added
- Repository presentation: banner (`docs/assets/banner.png`), badges, English + French READMEs rewritten,
  `docs/README.md` documentation index, `ROADMAP.md`, `SUPPORT.md`, `GOVERNANCE.md`, `CITATION.cff`.
- `.github`: Dependabot (actions + npm), issue template chooser, structured run-report form, `.gitattributes`
  for correct language statistics.
- `tools/setup_repo.sh`: one command for the repository description, topics, features and Pages.
### Fixed
- CI: gitleaks runs from its official container instead of the licensed action; `npm audit` scoped to shipped
  dependencies; the Unreal workflow no longer fails when no self-hosted runner exists; semgrep telemetry off.

## [0.4.0] — 2026-10-07
### Added / Ajouté
- **Bilingual, autonomous studio**: `studio.config.yaml` (autonomy `guided`/`autonomous`/`full`, hard stops, defaults, `extra_instructions`), `DECISIONS.md`, `QUESTIONS.md`; precedence user message > config > defaults, safety contract above all.
- All 8 skills rewritten in English with a French summary; replies in the user's language.
- `README.md` (EN) + `README.fr.md`; bilingual `CLAUDE.md` / `AGENTS.md`; `GEMINI.md`; `.github/copilot-instructions.md`; English guides in `docs/guides/en/`; PDF guide in FR and EN (`--lang`).
- Cinematic landing: spec `docs/design/34_LANDING_CINEMATIQUE.md`, shots L00–L04, components `CinematicHero` and `EraSequence` (scroll-scrubbed, Framer Motion), automatic switch from typographic mode once renders are approved; `tools/check_media_approvals.py` in CI.
- `.claude/settings.json`: Epic Unreal plugin and `frontend-design` pre-declared in `enabledPlugins`.

## [0.3.0] — 2026-10-07
### Modifié
- Bascule vers **Unreal Engine 5.8** et une direction artistique **réaliste** (ADR 0012) : TDD, bible artistique, playbook et skills réécrits.
- Aucune image de jeu dans le dépôt : cahier de rendu (`docs/design/33_VISUAL_TARGETS.md`) et liste de plans exécutable (`data/shotlist.json`).
### Ajouté
- Corpus juridique complet (`legal/`, 22 documents).
- Landing page de référence testée et version React + Vite + TypeScript + Framer Motion ; projet Remotion pour les titrages.
- Tests Robot Framework, Playwright, k6 ; CI données/confidentialité/landing, sécurité (gitleaks, semgrep, ZAP), publication manuelle, CI Unreal (runner Windows).
- Guides A→Z, installation, temps et coûts, sécurité, personnalisation, autres IA, FAQ ; schémas ; guide PDF.

## [0.2.0] — 2026-10-07
- Dossier de production (bible narrative, scripts, scénarios, paramètres, monde, audio, UX, production, QA, risques, juridique, marketing, live ops) et données de jeu.

## [0.1.0] — 2026-10-07
- Étude de marché et concept.
