---
name: studio-setup
description: Diagnoses and installs the studio workstation for a realistic Unreal Engine 5.8 game — Epic Games Launcher, Visual Studio 2022, .NET 8, Git LFS, the official Epic plugin for Claude Code (MCP), Node, ffmpeg, Blender, Robot Framework, k6, gitleaks, semgrep — from official sources, with hardware checks. Use on first run, when a tool is missing, or to change versions ("install", "setup", "installe", "configure le poste").
---

# Skill: studio-setup

> **FR —** Diagnostique et installe le poste de studio (Unreal 5.8, Visual Studio, plugin Epic pour Claude Code, outils web et de test) depuis les sources officielles. Répond dans la langue de l'utilisateur.

## Rules
- Pinned versions in `tools/versions.env`. Official sources only (winget, Homebrew, apt, vendors). Never `curl | sh`.
- **The human** creates accounts (Epic, GitHub, Steamworks), accepts licences (Unreal EULA, Visual Studio) and signs in to the launcher. Never type credentials.
- Admin rights: after one consent at step B (`autonomy.level: autonomous`), or without asking in `full` mode.

## Procedure
1. `python3 tools/doctor.py` (Windows: `py tools\doctor.py`).
2. Hardware check (printed by the Windows script): RTX 3070/4070+ recommended, 32-64 GB RAM, 300 GB free. If insufficient, say so and continue on the non-game tracks (landing, legal, data, docs).
3. Windows: `powershell -ExecutionPolicy Bypass -File .claude/skills/studio-setup/scripts/install_windows.ps1 -Plan`, then run without `-Plan` (`-Yes` in autonomous/full mode after the global consent).
   macOS/Linux side tools: `bash .claude/skills/studio-setup/scripts/install_tools_unix.sh --plan`, then without `--plan`.
4. **Claude Code plugins** are pre-declared in `.claude/settings.json` (`enabledPlugins`): the official Epic plugin `unreal-engine-skills-for-claude-code@claude-plugins-official`. If it is not active, run `/plugin install unreal-engine-skills-for-claude-code@claude-plugins-official`. Other agents: use editor Python via `UnrealEditor-Cmd.exe -run=pythonscript`.
5. **Hard stop — Unreal Engine:** give the human the exact steps (Epic Games Launcher → sign in → Unreal Engine → Library → install 5.8 with Windows target and debugging symbols), then continue other tracks.
6. In the editor: enable plugins **Model Context Protocol** and **AllToolsets**, restart, run `ModelContextProtocol.StartServer`. You can do this through editor Python/console once the editor is open.
7. Verify MCP: list the actors of the open map. Set `UE_ROOT`. Re-run `doctor.py`.
8. Write `docs/DEPENDENCIES.md` (tool, exact version, licence, source, date).

## What gets installed
| Item | Role | Licence / cost |
|---|---|---|
| Unreal Engine 5.8 | engine | free under US$1M lifetime gross revenue, then 5 % (Epic Games Store sales exempt) |
| Official Epic plugin for Claude Code + editor plugins Model Context Protocol / AllToolsets | drive the editor | MIT (Claude plugin) |
| Visual Studio 2022 or Rider | C++ build | Community free under Microsoft's conditions |
| Fab (Megascans, kits) | photoreal assets | **paid** since 2025 — human buys |
| MetaHuman (Creator inside the editor) | realistic humans | free under US$1M annual revenue |
| Online Subsystem Steam | sessions, voice, achievements | included; Steam Direct fee |
| Git LFS or Perforce | binary content (private) | depends on host |
| Node, Vite, React, Framer Motion, Remotion | landing, motion design | MIT; **Remotion: company licence above a size threshold** |
| Robot Framework, k6, gitleaks, semgrep | tests & security | tools |

## Troubleshooting
MCP not responding → editor open, plugins enabled, server started, Git Bash on PATH (Windows). Slow builds → shared DDC, antivirus exclusions (with consent). Corporate proxy → configure the company CA; never disable TLS.
