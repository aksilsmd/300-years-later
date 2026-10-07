#!/usr/bin/env bash
# EN — One-off GitHub repository setup: About box (description, homepage, topics), features, Pages,
#      release. Every one of these is a repository *setting*, so it needs the owner's own token: no
#      agent can do it, and no `git push` changes it. Run this yourself, once.
# FR — Configuration unique du dépôt GitHub : encart « About » (description, site, mots-clés), options,
#      Pages, release. Tout cela relève des *réglages* du dépôt, donc de votre jeton de propriétaire :
#      aucune IA ne peut le faire, et aucun `git push` ne le change. À lancer vous-même, une fois.
#
#   gh auth login && bash tools/setup_repo.sh
#
# Values come from .github/about.yml — edit that file, not this script.
# If anything is refused, the script prints exactly what to paste where, and carries on.
set -uo pipefail

cd "$(dirname "$0")/.."
ABOUT=".github/about.yml"
[ -f "$ABOUT" ] || { echo "✗ $ABOUT is missing."; exit 1; }

DESC="$(sed -n 's/^description: //p' "$ABOUT" | head -1)"
HOMEPAGE_RAW="$(sed -n 's/^homepage: //p' "$ABOUT" | head -1)"
PREVIEW="$(sed -n 's/^social_preview: //p' "$ABOUT" | head -1)"
TOPICS=()
while IFS= read -r t; do [ -n "$t" ] && TOPICS+=("$t"); done < <(sed -n 's/^  - //p' "$ABOUT")

manual=0
note() { manual=1; echo "   → à faire à la main / do by hand: $*"; }

command -v gh >/dev/null || { echo "✗ GitHub CLI (gh) is required: https://cli.github.com"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "✗ Run 'gh auth login' first."; exit 1; }

REPO="$(gh repo view --json nameWithOwner -q .nameWithOwner)" || exit 1
case "$HOMEPAGE_RAW" in
  auto|"") HOMEPAGE="https://github.com/${REPO}#readme" ;;
  *)       HOMEPAGE="$HOMEPAGE_RAW" ;;
esac

echo "→ $REPO"
echo "   description: ${#DESC} characters (GitHub allows 350)"
echo "   topics:      ${#TOPICS[@]} (GitHub allows 20)"
[ "${#DESC}" -le 350 ] || { echo "✗ description too long, shorten it in $ABOUT"; exit 1; }
[ "${#TOPICS[@]}" -le 20 ] || { echo "✗ too many topics, trim $ABOUT"; exit 1; }

# ---------------------------------------------------------------- About box
args=(--description "$DESC" --homepage "$HOMEPAGE")
for t in "${TOPICS[@]}"; do args+=(--add-topic "$t"); done
if gh repo edit "$REPO" "${args[@]}" >/dev/null 2>&1; then
  echo "✓ About box: description, homepage and ${#TOPICS[@]} topics applied"
else
  echo "✗ About box refused (token without 'repo' scope, or not the owner)"
  note "github.com/${REPO} → ⚙ next to About → paste the description and the topics printed below"
fi

# ---------------------------------------------------------------- Features
if gh repo edit "$REPO" --enable-issues --enable-discussions --enable-wiki=false >/dev/null 2>&1; then
  echo "✓ Issues on, Discussions on, Wiki off"
else
  note "Settings → General → Features: Issues ✓, Discussions ✓, Wiki ✗"
fi

# ---------------------------------------------------------------- Social preview (no API endpoint)
echo "✓ Social preview file ready: $PREVIEW"
note "Settings → General → Social preview → Upload an image → $PREVIEW"

# ---------------------------------------------------------------- Pages
if gh api -X POST "repos/${REPO}/pages" -f "build_type=workflow" >/dev/null 2>&1 \
   || gh api -X PUT "repos/${REPO}/pages" -f "build_type=workflow" >/dev/null 2>&1; then
  echo "✓ Pages source set to GitHub Actions"
else
  note "Settings → Pages → Source: GitHub Actions (or it is already set)"
fi

# ---------------------------------------------------------------- Release
VERSION="$(grep -m1 -oE '## \[[0-9]+\.[0-9]+\.[0-9]+\]' CHANGELOG.md | tr -d '#[] ')"
if [ -n "$VERSION" ] && ! gh release view "v$VERSION" >/dev/null 2>&1; then
  NOTES="$(awk "/^## \\[$VERSION\\]/{f=1;next} /^## \\[/{f=0} f" CHANGELOG.md)"
  if gh release create "v$VERSION" --title "v$VERSION" --notes "$NOTES" >/dev/null 2>&1; then
    echo "✓ Release v$VERSION published"
  else
    note "Releases → Draft a new release → tag v$VERSION → paste the CHANGELOG section"
  fi
elif [ -n "$VERSION" ]; then
  echo "✓ Release v$VERSION already exists"
fi

# ---------------------------------------------------------------- Paste-ready fallback
if [ "$manual" -eq 1 ]; then
  cat <<EOF

────────────────────────────────────────────────────────────────────────────
À COLLER / TO PASTE — github.com/${REPO}, gear icon next to "About"

Description:
$DESC

Website:
$HOMEPAGE

Topics (one per line, GitHub adds them as you type):
EOF
  printf '%s\n' "${TOPICS[@]}"
  echo "────────────────────────────────────────────────────────────────────────────"
fi

cat <<'EOF'

Reminder / Rappel : Settings → Emails → "Keep my email addresses private".
EOF
