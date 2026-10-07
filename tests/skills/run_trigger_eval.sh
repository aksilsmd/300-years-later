#!/usr/bin/env bash
# EN — Does each skill trigger on the queries it should, and stay quiet on the near-misses?
#      Needs Claude Code and jq. It calls the model, so it costs tokens and is NOT run in CI.
# FR — Chaque skill se déclenche-t-il sur les bonnes requêtes, et reste-t-il muet sur les pièges ?
#      Nécessite Claude Code et jq. Appelle le modèle : coûte des jetons, donc hors CI.
#
#   bash tests/skills/run_trigger_eval.sh              # every skill, 1 run per query
#   bash tests/skills/run_trigger_eval.sh game-qa 3    # one skill, 3 runs per query
set -uo pipefail
cd "$(dirname "$0")/../.."

command -v claude >/dev/null || { echo "✗ Claude Code (claude) is required"; exit 1; }
command -v jq     >/dev/null || { echo "✗ jq is required"; exit 1; }

CORPUS="tests/skills/triggers.json"
ONLY="${1:-}"
RUNS="${2:-1}"
pass_all=0

triggered() {  # $1 = prompt, $2 = skill name
  claude -p "$1" --output-format json 2>/dev/null \
    | jq -e --arg s "$2" 'any(.. | objects | select(.type? == "tool_use" and .name? == "Skill");
                              (.input.skill? // "") | contains($s))' >/dev/null
}

for skill in $(jq -r '.skills[].name' "$CORPUS"); do
  [ -n "$ONLY" ] && [ "$ONLY" != "$skill" ] && continue
  echo "── $skill"
  hit=0; tot=0; leak=0
  while IFS= read -r q; do
    for _ in $(seq "$RUNS"); do
      tot=$((tot+1)); triggered "$q" "$skill" && hit=$((hit+1))
    done
  done < <(jq -r --arg s "$skill" '.skills[] | select(.name==$s) | .should[]' "$CORPUS")
  while IFS= read -r q; do
    for _ in $(seq "$RUNS"); do
      triggered "$q" "$skill" && { leak=$((leak+1)); echo "   ✗ fired on a near-miss: ${q:0:70}"; }
    done
  done < <(jq -r --arg s "$skill" '.skills[] | select(.name==$s) | .should_not[]' "$CORPUS")
  rate=$(awk -v h="$hit" -v t="$tot" 'BEGIN{printf "%.2f", (t?h/t:0)}')
  thr=$(jq -r '.threshold.should_trigger_rate' "$CORPUS")
  ok=$(awk -v r="$rate" -v t="$thr" 'BEGIN{print (r>=t)?1:0}')
  if [ "$ok" = 1 ] && [ "$leak" = 0 ]; then echo "   ✓ trigger rate $rate, no false positive"
  else echo "   ✗ trigger rate $rate (threshold $thr), $leak false positive(s)"; pass_all=1; fi
done
exit $pass_all
