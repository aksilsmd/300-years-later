# Journal des modifications
Format : Keep a Changelog · Versionnage sémantique.

## [0.4.2] — 2026-10-07
### Added
- **Evidence-backed project state**: `STUDIO_STATE.md` now carries a machine-readable `yaml state` block
  (status vocabulary `planned → … → released` plus an `evidence` path per system) enforced by
  `tools/validate_state.py` in CI and pre-commit. An agent can no longer declare a system `implemented`,
  `tested` or `validated` without a file that proves it. The `game-studio` skill states the rule.
- `tools/repo_audit.py`: structural audit — required files, skills with front matter, internal links,
  every GitHub Action pinned to a commit SHA, no floating container tag, no `latest` in `tools/versions.env`,
  no licensed Unreal content. Wired into CI and the pre-commit hook.
- `.github/CODEOWNERS`; `marketing/README.md` stating which landing is production and which is the tested
  reference, and the rule that forbids them diverging silently.
### Changed
- `tools/doctor.py` separates a missing **core** tool (exit 1) from a missing optional one (reported, exit 0),
  with `--strict` for CI and release checks.
- npm dependencies declared as exact versions instead of ranges, pending committed lockfiles.
### Security
- gitleaks container pinned to `v8.30.1` instead of `latest`; `K6_VERSION` and `GITLEAKS_VERSION` pinned in
  `tools/versions.env`, and the audit fails if the workflow and the declared version drift apart.
- The semgrep gate now also fails on fatal scan errors instead of only on findings.

## [0.4.1] — 2026-10-07
### Added
- Community files in both languages: issue forms (bug, feature, run report), PR checklist, `SUPPORT.md`,
  `GOVERNANCE.md`, `ROADMAP.md`, `CITATION.cff`, `docs/runs/` for real run reports; English sections added to
  `SECURITY.md` (including private vulnerability reporting) and `CODE_OF_CONDUCT.md`.
- Repository presentation: banner (`docs/assets/banner.png`), badges, English + French READMEs rewritten,
  `docs/README.md` documentation index, `ROADMAP.md`, `SUPPORT.md`, `GOVERNANCE.md`, `CITATION.cff`.
- `.github`: Dependabot (actions + npm), issue template chooser, structured run-report form, `.gitattributes`
  for correct language statistics.
- `tools/setup_repo.sh`: one command for the repository description, topics, features and Pages.
### Security
- Every GitHub Action pinned to a commit SHA (mutable tags can be repointed), Dependabot cooldown of 7 days,
  semgrep results published as SARIF in the Security tab with a blocking `p/ci` gate, guide captures no longer
  run through a shell.
### Fixed
- PR checklist referenced Godot tools (`gdlint`) left over from before ADR 0012.
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
