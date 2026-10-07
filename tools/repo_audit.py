#!/usr/bin/env python3
"""Structural audit of the repository / Audit structurel du dépôt.

EN: Checks the invariants that keep this kit trustworthy and reproducible — the ones a human reviewer
    would forget: every skill referenced actually exists, every internal link resolves, every GitHub
    Action is pinned to a commit SHA, no container or security tool floats on `latest`, the governance
    files are present. Read-only, no network.
FR: Vérifie les invariants qui rendent ce kit fiable et reproductible : les skills référencés existent,
    les liens internes résolvent, les actions GitHub sont épinglées à un SHA, aucun conteneur ni outil
    de sécurité ne flotte sur `latest`, les fichiers de gouvernance sont là. Lecture seule, sans réseau.

    python3 tools/repo_audit.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", "dist", "build", ".venv", "__pycache__"}

REQUIRED = [
    "README.md", "README.fr.md", "AGENTS.md", "CLAUDE.md", "GEMINI.md",
    "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "GOVERNANCE.md", "SECURITY.md", "SUPPORT.md",
    "ROADMAP.md", "CHANGELOG.md", "LICENSE", "LICENSE-CONTENT.md", "THIRD_PARTY_LICENSES.md",
    "STUDIO_STATE.md", "DECISIONS.md", "QUESTIONS.md", "studio.config.yaml",
    ".github/CODEOWNERS", ".github/dependabot.yml", ".github/pull_request_template.md",
    "media/APPROVALS.md", "docs/README.md", "ARCHITECTURE.md", ".editorconfig",
    ".claude-plugin/plugin.json", ".claude-plugin/marketplace.json",
]
SKILLS = ["game-studio", "studio-setup", "game-build", "game-assets", "game-qa",
          "legal-compliance", "marketing-launch", "privacy-guard"]


def walk(suffix: str):
    for p in ROOT.rglob(f"*{suffix}"):
        if not any(part in SKIP_DIRS for part in p.parts):
            yield p


def check_required(errors: list[str]) -> None:
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing required file: {rel}")
    for name in SKILLS:
        f = ROOT / ".claude" / "skills" / name / "SKILL.md"
        if not f.is_file():
            errors.append(f"missing skill: {f.relative_to(ROOT)}")
            continue
        head = f.read_text(encoding="utf-8")[:400]
        if not head.startswith("---") or "description:" not in head:
            errors.append(f"{f.relative_to(ROOT)}: missing YAML front matter with a description")


def check_links(errors: list[str]) -> None:
    for md in walk(".md"):
        text = md.read_text(encoding="utf-8")
        for m in re.finditer(r"\[[^\]]*\]\(([^)\s]+)\)", text):
            target = m.group(1).split("#")[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if not (md.parent / target).exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link → {target}")


def check_actions(errors: list[str]) -> None:
    sha = re.compile(r"^[0-9a-f]{40}$")
    for wf in (ROOT / ".github" / "workflows").glob("*.yml"):
        text = wf.read_text(encoding="utf-8")
        for m in re.finditer(r"uses:\s*([^\s#]+)", text):
            ref = m.group(1)
            if ref.startswith("./"):
                continue
            if "@" not in ref or not sha.match(ref.split("@", 1)[1]):
                errors.append(f"{wf.relative_to(ROOT)}: action not pinned to a commit SHA → {ref}")
        for m in re.finditer(r"(docker run[^\n]*?|image:\s*)([\w./-]+:latest)", text):
            errors.append(f"{wf.relative_to(ROOT)}: container pinned to a floating tag → {m.group(2)}")
        # Script injection: untrusted event data interpolated straight into a shell step.
        for m in re.finditer(r"\$\{\{\s*(github\.event[\w.\[\]'\"]*|github\.head_ref)\s*\}\}", text):
            errors.append(f"{wf.relative_to(ROOT)}: untrusted interpolation in a workflow → {m.group(1)} "
                          f"(pass it through env: instead)")
        if re.search(r"^on:.*pull_request_target", text, re.M | re.S) and "actions/checkout" in text:
            errors.append(f"{wf.relative_to(ROOT)}: pull_request_target with a checkout runs untrusted code "
                          f"with write permissions")
        if not re.search(r"^permissions:", text, re.M):
            errors.append(f"{wf.relative_to(ROOT)}: no top-level 'permissions:' block "
                          f"(declare the least privilege the workflow needs)")


def check_versions(errors: list[str]) -> None:
    env = ROOT / "tools" / "versions.env"
    if not env.is_file():
        errors.append("missing tools/versions.env")
        return
    for line in env.read_text(encoding="utf-8").splitlines():
        line = line.split("#")[0].strip()
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        if value.strip().strip('"').lower() == "latest":
            errors.append(f"tools/versions.env: {key} is 'latest' — pin a version for reproducibility")
    # the container tag and the declared version must not drift apart
    sec = ROOT / ".github" / "workflows" / "security.yml"
    if sec.is_file():
        m = re.search(r"gitleaks:v([0-9.]+)", sec.read_text(encoding="utf-8"))
        d = re.search(r'GITLEAKS_VERSION="([0-9.]+)"', env.read_text(encoding="utf-8"))
        if m and d and m.group(1) != d.group(1):
            errors.append(f"gitleaks version drift: workflow v{m.group(1)} vs versions.env {d.group(1)}")


def check_no_licensed_content(errors: list[str]) -> None:
    for pattern in ("*.uasset", "*.umap", "*.pak"):
        for p in walk(pattern.lstrip("*")):
            errors.append(f"licensed Unreal content must not be here: {p.relative_to(ROOT)}")
    if (ROOT / "game" / "Content").exists():
        errors.append("game/Content/ must live in the private repository")


def main() -> int:
    errors: list[str] = []
    for check in (check_required, check_links, check_actions, check_versions, check_no_licensed_content):
        check(errors)
    if errors:
        print(f"✗ repository audit: {len(errors)} problem(s)")
        for e in errors:
            print("   -", e)
        return 1
    print("✓ repository audit: required files, skills, internal links, pinned actions, versions — all clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
