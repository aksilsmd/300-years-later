#!/usr/bin/env python3
"""Validates STUDIO_STATE.md — the project's claimed state must be backed by evidence.

EN: An agent can write anything in a Markdown file. This gate makes one class of lie impossible:
    a system declared `implemented` or beyond must name an `evidence` path that EXISTS in the repository.
FR: Une IA peut écrire n'importe quoi dans un fichier Markdown. Ce contrôle rend un mensonge impossible :
    un système déclaré `implemented` ou au-delà doit désigner un chemin `evidence` PRÉSENT dans le dépôt.

    python3 tools/validate_state.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE = ROOT / "STUDIO_STATE.md"

ORDER = ["planned", "specified", "implemented", "built", "tested", "validated", "released"]
NEEDS_EVIDENCE = set(ORDER[ORDER.index("specified"):])  # specified and beyond
PHASES = set("ABCDEFGHIJKLMNOZ")
BUILD_STATUS = {"not_started", "failing", "passing"}


def load_block(text: str) -> str:
    m = re.search(r"```yaml state\n(.*?)```", text, re.S)
    if not m:
        raise SystemExit("✗ STUDIO_STATE.md: missing the ```yaml state block")
    return m.group(1)


def parse(block: str) -> tuple[dict[str, str], dict[str, tuple[str, str | None]]]:
    """Minimal parser for the fixed shape of the block — no YAML dependency needed."""
    project: dict[str, str] = {}
    systems: dict[str, tuple[str, str | None]] = {}
    section = None
    for raw in block.splitlines():
        line = raw.split("#")[0].rstrip()
        if not line.strip():
            continue
        if not line.startswith(" "):
            section = line.strip().rstrip(":")
            continue
        if section == "project":
            k, _, v = line.strip().partition(":")
            project[k.strip()] = v.strip()
        elif section == "systems":
            m = re.match(r"\s*([\w_]+)\s*:\s*\{(.*)\}\s*$", line)
            if not m:
                raise SystemExit(f"✗ STUDIO_STATE.md: cannot read system line: {line.strip()}")
            name, body = m.group(1), m.group(2)
            fields = dict(
                (p.split(":", 1)[0].strip(), p.split(":", 1)[1].strip())
                for p in body.split(",") if ":" in p
            )
            ev = fields.get("evidence", "").strip().strip('"')
            systems[name] = (fields.get("status", "").strip(), None if ev in {"", "null", "~"} else ev)
    return project, systems


def main() -> int:
    if not STATE.is_file():
        print("✗ STUDIO_STATE.md is missing")
        return 1
    project, systems = parse(load_block(STATE.read_text(encoding="utf-8")))
    errors: list[str] = []

    phase = project.get("phase", "")
    if phase not in PHASES:
        errors.append(f"project.phase '{phase}' is not one of {sorted(PHASES)}")
    if project.get("build_status") not in BUILD_STATUS:
        errors.append(f"project.build_status must be one of {sorted(BUILD_STATUS)}")
    if project.get("playable") not in {"true", "false"}:
        errors.append("project.playable must be true or false")
    if project.get("playable") == "true" and project.get("build_status") != "passing":
        errors.append("project.playable is true while build_status is not 'passing'")

    if not systems:
        errors.append("no system listed")
    for name, (status, evidence) in systems.items():
        if status not in ORDER:
            errors.append(f"{name}: unknown status '{status}' (expected one of {ORDER})")
            continue
        if status in NEEDS_EVIDENCE:
            if not evidence:
                errors.append(f"{name}: status '{status}' requires an evidence path")
            elif not (ROOT / evidence).exists():
                errors.append(f"{name}: evidence '{evidence}' does not exist in the repository")

    if errors:
        print("✗ STUDIO_STATE.md is not backed by evidence:")
        for e in errors:
            print("   -", e)
        print("\n   A status is a claim. Either produce the evidence, or lower the status.")
        return 1
    proven = sum(1 for s, _ in systems.values() if s in NEEDS_EVIDENCE)
    print(f"✓ studio state: phase {phase}, {len(systems)} system(s), {proven} backed by an existing evidence file")
    return 0


if __name__ == "__main__":
    sys.exit(main())
