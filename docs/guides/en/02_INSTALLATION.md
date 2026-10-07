# Studio workstation installation

🇫🇷 [Version française](../02_INSTALLATION.md)

## 1. Hardware
| | Practical minimum | Recommended |
|---|---|---|
| OS | Windows 10 64-bit | Windows 11 64-bit |
| CPU | 8 cores | 12-16 cores (C++ and shader compilation) |
| Memory | 16 GB (slow) | 32-64 GB |
| GPU | 8 GB VRAM (RTX 2070 / RX 6600 XT) | RTX 3070/4070 or better, 12 GB+ |
| Storage | 300 GB SSD | 1 TB NVMe |
| Network | fibre advised | engine + assets = 100-200 GB to download |

macOS works for Unreal (Epic Games Launcher + Xcode) but the project targets Windows first. Linux is used for side tools (landing, tests).

## 2. Software
The `studio-setup` skill installs everything with `winget`:
```powershell
powershell -ExecutionPolicy Bypass -File .claude/skills/studio-setup/scripts/install_windows.ps1 -Plan   # show the plan
powershell -ExecutionPolicy Bypass -File .claude/skills/studio-setup/scripts/install_windows.ps1         # install
```
| Tool | Why |
|---|---|
| Epic Games Launcher + **Unreal Engine 5.8** | engine (installed in the launcher, by you) |
| Visual Studio 2022 (C++ game + desktop workloads) or Rider | compilation |
| .NET 8, Git, Git LFS, GitHub CLI, Python 3.12 | build tools and kit tools |
| Node LTS, ffmpeg | landing page, video |
| Blender LTS | asset touch-ups |
| Robot Framework, k6, gitleaks, semgrep | tests and security |

## 3. Connect Claude Code to Unreal (Epic's official plugin)
1. The plugin is already declared in `.claude/settings.json` (`enabledPlugins`): Claude Code offers to install it when you open the folder. Otherwise: `/plugin install unreal-engine-skills-for-claude-code@claude-plugins-official` (and `frontend-design@claude-plugins-official` for the landing).
2. In the Unreal editor: *Edit › Plugins*, enable **Model Context Protocol** and **AllToolsets**, restart.
3. Editor console: `ModelContextProtocol.StartServer`
4. On Windows, Git Bash (installed with Git) must be on the `PATH`.
5. Test: ask Claude "list the actors in the open map".

> ⚠️ This plugin gives the AI broad access to the editor, including running Python. Always work on a Git branch and commit before each batch of operations.

## 4. Variables and folders
```powershell
setx UE_ROOT "C:\Program Files\Epic Games\UE_5.8"
```
Create a **private** repository for `game/Content/` (Git LFS or Perforce). Never publish this folder.

## 5. Check
```powershell
py tools\doctor.py
```
Every relevant line must be ✓.
