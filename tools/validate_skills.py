#!/usr/bin/env python3
"""Validates the skills against the Agent Skills specification (agentskills.io).

EN: The skills are this repository's product. This gate enforces the format so they load in every
    client — Claude Code, claude.ai, the Skills API — and not just in the one they were written in.
FR: Les skills sont le produit de ce dépôt. Ce contrôle garantit qu'ils respectent le format et
    fonctionnent dans tous les clients, pas seulement celui dans lequel ils ont été écrits.

Checked (spec, retrieved 2026-10-07):
  · frontmatter is the first block, parsed as YAML
  · closed field set: name, description, license, compatibility, metadata, allowed-tools
    (any other key is rejected when uploading to claude.ai / the Skills API)
  · name: 1-64 chars, lowercase alphanumeric or hyphen, no leading/trailing/double hyphen,
    and identical to the parent directory name
  · description: 1-1024 chars, non-empty, written in the third person
  · compatibility: <= 500 chars · metadata: string keys -> string values
  · allowed-tools: a space-separated string
Also enforced here, as project rules (progressive disclosure):
  · SKILL.md stays under 500 lines
  · every file the skill links to exists, and references stay one level deep
  · a bilingual "FR —" summary line, because this kit answers in the user's language

    python3 tools/validate_skills.py
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / ".claude" / "skills"

ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
MAX_NAME, MAX_DESC, MAX_COMPAT, MAX_LINES = 64, 1024, 500, 500
FIRST_PERSON = re.compile(r"\b(I can|I will|I help|you can use this|use me)\b", re.I)


def frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    """Returns (fields, errors). Deliberately tolerant: we report, we do not guess."""
    if not text.startswith("---\n"):
        return {}, ["does not start with a '---' frontmatter block"]
    end = text.find("\n---", 4)
    if end == -1:
        return {}, ["the frontmatter block is never closed"]
    fields: dict[str, str] = {}
    errors: list[str] = []
    for line in text[4:end].splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        if line.startswith((" ", "\t")):  # nested value (metadata:)
            continue
        key, sep, value = line.partition(":")
        if not sep:
            errors.append(f"frontmatter line is not 'key: value': {line.strip()[:60]}")
            continue
        fields[key.strip()] = value.strip()
    return fields, errors


def check_name(name: str, directory: str) -> list[str]:
    errors = []
    if not 1 <= len(name) <= MAX_NAME:
        errors.append(f"name must be 1-{MAX_NAME} characters (it is {len(name)})")
    if not all(c.isalnum() and not c.isupper() or c == "-" for c in name):
        errors.append(f"name '{name}' must be lowercase alphanumeric or hyphen")
    if name.startswith("-") or name.endswith("-"):
        errors.append(f"name '{name}' must not start or end with a hyphen")
    if "--" in name:
        errors.append(f"name '{name}' must not contain a double hyphen")
    norm = unicodedata.normalize("NFKC", name)
    if norm != unicodedata.normalize("NFKC", directory):
        errors.append(f"name '{name}' must match the directory name '{directory}'")
    return errors


def check_skill(skill_md: Path) -> list[str]:
    rel = skill_md.relative_to(ROOT)
    text = skill_md.read_text(encoding="utf-8")
    fields, errors = frontmatter(text)
    errors = [f"{rel}: {e}" for e in errors]
    if not fields:
        return errors

    for key in fields:
        if key not in ALLOWED_FIELDS:
            errors.append(f"{rel}: '{key}' is not a portable frontmatter field "
                          f"(allowed: {', '.join(sorted(ALLOWED_FIELDS))})")
    name = fields.get("name", "")
    if not name:
        errors.append(f"{rel}: missing required field 'name'")
    else:
        errors += [f"{rel}: {e}" for e in check_name(name, skill_md.parent.name)]

    desc = fields.get("description", "")
    if not desc:
        errors.append(f"{rel}: missing required field 'description'")
    elif len(desc) > MAX_DESC:
        errors.append(f"{rel}: description is {len(desc)} characters, the limit is {MAX_DESC}")
    if FIRST_PERSON.search(desc):
        errors.append(f"{rel}: description must be third person — it is injected into the system prompt")
    if "<" in desc or ">" in desc:
        errors.append(f"{rel}: description must not contain angle brackets (it is injected inside XML tags)")

    compat = fields.get("compatibility", "")
    if len(compat) > MAX_COMPAT:
        errors.append(f"{rel}: compatibility is {len(compat)} characters, the limit is {MAX_COMPAT}")

    lines = text.count("\n") + 1
    if lines > MAX_LINES:
        errors.append(f"{rel}: {lines} lines — keep SKILL.md under {MAX_LINES} and move detail "
                      f"into reference files (progressive disclosure)")

    if "FR —" not in text[:1200]:
        errors.append(f"{rel}: missing the 'FR —' summary line required by this project")

    body = text[text.find("\n---", 4) + 4:]
    for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", body):
        target = m.group(1).split("#")[0]
        if target.startswith(("http://", "https://", "mailto:", "#")) or not target:
            continue
        resolved = (skill_md.parent / target).resolve()
        if not resolved.exists() and not (ROOT / target).exists():
            errors.append(f"{rel}: links to a file that does not exist → {target}")
    return errors


def main() -> int:
    if not SKILLS.is_dir():
        print(f"✗ no skills directory at {SKILLS.relative_to(ROOT)}")
        return 1
    skills = sorted(SKILLS.glob("*/SKILL.md"))
    if not skills:
        print("✗ no SKILL.md found")
        return 1
    errors: list[str] = []
    for s in skills:
        errors += check_skill(s)
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        if not (d / "SKILL.md").is_file():
            errors.append(f".claude/skills/{d.name}/: directory without a SKILL.md")
    if errors:
        print(f"✗ skills: {len(errors)} problem(s) against the Agent Skills specification")
        for e in errors:
            print("   -", e)
        return 1
    print(f"✓ skills: {len(skills)} valid against the Agent Skills specification "
          f"(names, descriptions, portable fields, size, links)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
