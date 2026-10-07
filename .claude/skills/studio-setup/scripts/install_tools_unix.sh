#!/usr/bin/env bash
# Outils annexes sous macOS/Linux (landing page, vidéo, tests, sécurité).
# Le jeu Unreal se développe sous Windows (recommandé) ; macOS est possible via Epic Games Launcher + Xcode.
#   --plan : affiche sans exécuter
set -euo pipefail
PLAN=0; [ "${1:-}" = "--plan" ] && PLAN=1
run() { if [ $PLAN -eq 1 ]; then echo "   [plan] $*"; else echo "▸ $*"; eval "$@"; fi; }

if command -v brew >/dev/null; then
  run "brew install node@22 ffmpeg k6 gitleaks gh git-lfs pipx"
  run "brew install --cask blender"
elif command -v apt-get >/dev/null; then
  echo "Les commandes suivantes nécessitent sudo : accord de l'humain requis."
  run "sudo apt-get update && sudo apt-get install -y ffmpeg git-lfs pipx"
  echo "Node LTS : https://nodejs.org · k6 : https://grafana.com/docs/k6/latest/set-up/install-k6/ · gitleaks : https://github.com/gitleaks/gitleaks/releases"
fi
run "pipx install semgrep || true"
run "pipx install robotframework && pipx inject robotframework robotframework-browser && rfbrowser init"
run "git lfs install"
echo "Vérifiez : python3 tools/doctor.py"
