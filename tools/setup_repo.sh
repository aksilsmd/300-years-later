#!/usr/bin/env bash
# EN — One-off GitHub repository setup: description, topics, features, social preview, Pages.
#      Everything here needs owner rights, so it is NOT done by the AI. Run it yourself once.
# FR — Configuration unique du dépôt GitHub : description, mots-clés, options, image sociale, Pages.
#      Tout cela demande les droits du propriétaire : à lancer vous-même, une fois.
#
#   gh auth login && bash tools/setup_repo.sh
set -euo pipefail

command -v gh >/dev/null || { echo "✗ GitHub CLI (gh) is required: https://cli.github.com"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "✗ Run 'gh auth login' first."; exit 1; }

REPO="$(gh repo view --json nameWithOwner -q .nameWithOwner)"
echo "→ Configuring $REPO"

DESC="Open-source AI game studio kit: give it to Claude Code, Gemini, Codex or Kimi and it builds a realistic 3D co-op game in Unreal Engine 5.8 from A to Z — bilingual FR/EN"

gh repo edit "$REPO" \
  --description "$DESC" \
  --homepage "https://github.com/${REPO}#readme" \
  --add-topic unreal-engine \
  --add-topic claude-code \
  --add-topic ai-agents \
  --add-topic agent-skills \
  --add-topic game-development \
  --add-topic game-design \
  --add-topic coop-game \
  --add-topic gdpr \
  --add-topic framer-motion \
  --add-topic open-source \
  --enable-issues --enable-discussions --enable-wiki=false

echo "→ Social preview image (docs/assets/banner.png)"
gh api -X PATCH "repos/${REPO}" -f description="$DESC" >/dev/null 2>&1 || true
echo "   Upload it by hand: Settings → General → Social preview → Upload an image → docs/assets/banner.png"

echo "→ GitHub Pages (landing page), source = GitHub Actions"
gh api -X POST "repos/${REPO}/pages" -f "build_type=workflow" >/dev/null 2>&1 \
  || gh api -X PUT "repos/${REPO}/pages" -f "build_type=workflow" >/dev/null 2>&1 \
  || echo "   Pages already configured, or enable it in Settings → Pages → Source: GitHub Actions."

cat <<'EOF'

✓ Done. Two things only you can do, in the web interface:
  1. Settings → General → Social preview → upload docs/assets/banner.png
  2. Actions tab → "Deploy landing (manual)" → Run workflow, when you want the landing online

Reminder: Settings → Emails → "Keep my email addresses private" keeps your address out of GitHub.
EOF
