#!/usr/bin/env python3
"""Diagnostic de l'environnement du studio. Lecture seule, aucun appel réseau.
Affiche ce qui est installé, ce qui manque, et la commande pour l'installer.
"""
from __future__ import annotations

import platform
import shutil
import subprocess
import sys

TOOLS = [
    # (commande, argument version, rôle, obligatoire pour, comment installer)
    ("git", "--version", "Versionnage", "tout", "https://git-scm.com"),
    ("git-lfs", "--version", "Contenu binaire (dépôt privé)", "game-build", "https://git-lfs.com"),
    ("python3", "--version", "Outils du kit", "tout", "https://python.org"),
    ("dotnet", "--version", ".NET (UnrealBuildTool)", "game-build", "winget install Microsoft.DotNet.SDK.8"),
    ("node", "--version", "Landing page / Remotion", "marketing-launch", "https://nodejs.org (LTS)"),
    ("npm", "--version", "Paquets web", "marketing-launch", "fourni avec Node"),
    ("ffmpeg", "-version", "Encodage vidéo, GIF", "marketing-launch", "winget install Gyan.FFmpeg"),
    ("blender", "--version", "Retouches d'assets", "game-assets", "https://www.blender.org/download/lts/"),
    ("robot", "--version", "Tests E2E Robot Framework", "game-qa", "pip install robotframework robotframework-browser"),
    ("k6", "version", "Tests de charge web", "game-qa", "winget install GrafanaLabs.k6"),
    ("gitleaks", "version", "Détection de secrets", "game-qa", "winget install Gitleaks.Gitleaks"),
    ("semgrep", "--version", "Analyse statique sécurité", "game-qa", "pip install semgrep"),
    ("gh", "--version", "Publication GitHub (par l'humain)", "publication", "https://cli.github.com"),
]


def version_of(cmd: str, arg: str) -> str | None:
    if not shutil.which(cmd):
        return None
    try:
        out = subprocess.run([cmd, arg], capture_output=True, text=True, timeout=20)
        line = (out.stdout or out.stderr).strip().splitlines()
        return line[0][:60] if line else "installé"
    except Exception:  # noqa: BLE001
        return "installé (version illisible)"


def find_unreal() -> str | None:
    """Cherche UnrealEditor via UE_ROOT ou les emplacements d'installation par défaut (lecture seule)."""
    import os
    from pathlib import Path
    candidates = []
    if os.environ.get("UE_ROOT"):
        candidates.append(Path(os.environ["UE_ROOT"]))
    candidates += [Path("C:/Program Files/Epic Games/UE_5.8"), Path("/Users/Shared/Epic Games/UE_5.8"), Path.home() / "UnrealEngine"]
    for c in candidates:
        for rel in ("Engine/Binaries/Win64/UnrealEditor.exe", "Engine/Binaries/Mac/UnrealEditor.app", "Engine/Binaries/Linux/UnrealEditor"):
            if (c / rel).exists():
                return str(c / rel)
    return None


def main() -> int:
    print(f"Système : {platform.system()} {platform.release()} — Python {sys.version.split()[0]}\n")
    missing_required = 0
    for cmd, arg, role, needed, how in TOOLS:
        v = version_of(cmd, arg)
        mark = "✓" if v else "✗"
        print(f" {mark} {cmd:<9} {role:<28} [{needed}] {v or 'MANQUANT → ' + how}")
        if not v and needed == "tout":
            missing_required += 1
    ue = find_unreal()
    print(f" {'✓' if ue else '✗'} {'unreal':<9} {'Unreal Engine 5.8':<28} [game-build] {ue or 'MANQUANT → Epic Games Launcher (voir studio-setup)'}")
    print("\nLes outils manquants sont installés par le skill « studio-setup ».")
    return 1 if missing_required else 0


if __name__ == "__main__":
    sys.exit(main())
