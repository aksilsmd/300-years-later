#!/usr/bin/env bash
# Publie ce dépôt sur GitHub en PUBLIC, après contrôles de confidentialité.
# Usage : bash publish.sh [nom-du-depot]
# Prérequis : git, GitHub CLI (gh) connecté avec « gh auth login », python3.
set -euo pipefail
cd "$(dirname "$0")"
REPO="${1:-300-years-later-ai-game-studio}"
DESC="Studio de jeu vidéo IA open source : skills Claude Code pour créer un jeu coop 3D réaliste sous Unreal Engine 5.8 — conception, code, tests, juridique, trailer, landing page."

echo "▸ 1/5 Vérification de GitHub CLI"
gh auth status >/dev/null 2>&1 || { echo "Connectez-vous d'abord : gh auth login"; exit 1; }
LOGIN="$(gh api user --jq .login)"
ID="$(gh api user --jq .id)"

echo "▸ 2/5 Identité Git anonyme (adresse noreply de GitHub, jamais votre e-mail personnel)"
git config user.name "$LOGIN"
git config user.email "${ID}+${LOGIN}@users.noreply.github.com"
# Réécrit l'auteur des commits locaux existants avec cette identité anonyme
git -c core.hooksPath=/dev/null commit --amend --no-edit --reset-author >/dev/null 2>&1 || true

echo "▸ 3/5 Contrôles : confidentialité, données, licences, contenu Unreal"
python3 tools/privacy_scan.py
python3 tools/validate_data.py
python3 tools/license_audit.py
if git ls-files | grep -Ei '\.(uasset|umap|pak)$|^game/Content/'; then echo "Contenu Unreal sous licence détecté : publication annulée."; exit 1; fi
if git ls-files | grep -Ei '(^|/)\.env(\.|$)|secret|denylist|\.pem$|\.key$|steam_appid'; then echo "Fichier sensible détecté : publication annulée."; exit 1; fi

echo "▸ 4/5 Confirmation"
echo "   Dépôt : github.com/$LOGIN/$REPO (PUBLIC)"
read -r -p "   Publier maintenant ? [o/N] " r; [[ "$r" =~ ^[oOyY]$ ]] || { echo "Annulé."; exit 0; }

echo "▸ 5/5 Création et envoi"
gh repo create "$REPO" --public --source . --push --description "$DESC"
gh repo edit "$LOGIN/$REPO" --add-topic claude-code,ai-agents,game-development,unreal-engine,unreal-engine-5,game-design,skills,gdpr,open-source,co-op-game || true
gh api -X PUT "repos/$LOGIN/$REPO/private-vulnerability-reporting" >/dev/null 2>&1 || echo "   (Activez manuellement : Settings › Security › Private vulnerability reporting)"
echo "✓ Publié : https://github.com/$LOGIN/$REPO"
echo "  Conseil : Settings › General › Social preview — n'y mettez qu'une image validée (media/APPROVALS.md) ou laissez vide."
