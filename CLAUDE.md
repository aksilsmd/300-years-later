# CLAUDE.md

The contract for every agent working here lives in **[AGENTS.md](AGENTS.md)** — read it in full, then apply
`.claude/skills/game-studio/SKILL.md`. The map of the repository is in [ARCHITECTURE.md](ARCHITECTURE.md).

@AGENTS.md

## Claude Code specifics
- The eight skills are in `.claude/skills/`; permissions and the plugins to install are in
  `.claude/settings.json`. This repository is also installable as a plugin (`.claude-plugin/`).
- Epic's Unreal MCP plugin needs the editor open, the **Model Context Protocol** and **AllToolsets** plugins
  enabled, and `ModelContextProtocol.StartServer` run in the editor console.
- The MCP plugin grants broad editor access: commit before each batch of MCP actions, and work on a branch.

> **FR —** Tout le contrat est dans `AGENTS.md`. Réponds toujours dans la langue de l'utilisateur.
