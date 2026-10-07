# Skill trigger evaluation / Évaluation du déclenchement des skills

**EN —** A skill is only useful if the agent reaches for it at the right moment. `triggers.json` holds, for each
of the eight skills, realistic queries that **should** select it and deliberate near-misses that **should not**.
`run_trigger_eval.sh` runs them through Claude Code and reports the trigger rate.

**FR —** Un skill n'est utile que si l'IA le choisit au bon moment. `triggers.json` contient, pour chacun des huit
skills, des requêtes réalistes qui **doivent** l'activer et des pièges proches qui **ne doivent pas**.

```bash
bash tests/skills/run_trigger_eval.sh              # all skills, 1 run per query
bash tests/skills/run_trigger_eval.sh game-qa 3    # one skill, 3 runs per query
```

It calls the model, so it costs tokens and is **not** part of CI — run it after changing a skill's
`description`. A skill passes at ≥ 75 % on `should` and 0 false positives on `should_not`.

When a skill under-triggers, the fix is almost always the `description`, not the body: make it name the words
users actually type, in both languages, and state the boundary explicitly ("do not trigger when…").
Changing a description is cheap; re-run this before and after.
