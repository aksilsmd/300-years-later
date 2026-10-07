#!/usr/bin/env python3
"""Rename the public title, and only the public title / Renomme le titre public, et lui seul.

EN: The project carries three names on purpose — the code name CENTURY TEMPS, the public title
    (today "300 Years Later", ADR 0021 proposes "Afterloom"), and the repository slug
    `300-years-later`. Changing the public title by hand means editing ~90 places across READMEs,
    the landing pages, the press kit, the Steam page and the tests, and getting one of them wrong
    is how a project ends up with two names in public. This tool does the replacement in one pass.

    What it never touches: the repository slug and every URL built from it, the code name, the
    valley name Brumecombe, the French prose "300 ans plus tard" (which is the pitch, not the
    title), the licence attribution entity, and the ADR that records the decision.

FR: Le projet porte trois noms volontairement : le nom de code CENTURY TEMPS, le titre public
    (aujourd'hui « 300 Years Later », l'ADR 0021 propose « Afterloom ») et l'identifiant du dépôt
    `300-years-later`. Renommer le titre public à la main, c'est éditer ~90 endroits ; en oublier
    un, c'est se retrouver avec deux noms en public. Cet outil fait le remplacement d'un coup.

    Ce qu'il ne touche jamais : l'identifiant du dépôt et les URL qui en découlent, le nom de code,
    le nom de la vallée, la phrase « 300 ans plus tard » (c'est l'accroche, pas le titre), l'entité
    d'attribution des licences, et l'ADR qui consigne la décision.

    python3 tools/apply_public_title.py --to "Afterloom"           # dry run, shows every change
    python3 tools/apply_public_title.py --to "Afterloom" --apply   # writes the files
    python3 tools/apply_public_title.py --to "Afterloom" --apply --from "300 Years Later"

After --apply, run the gates and the landing tests:
    python3 tools/repo_audit.py && python3 tools/privacy_scan.py && python3 -m pytest tests/web -q
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CURRENT = "300 Years Later"

SKIP_DIRS = {".git", "node_modules", "dist", "build", ".venv", "__pycache__", ".pytest_cache"}
TEXT_SUFFIXES = {
    ".md", ".txt", ".yml", ".yaml", ".json", ".html", ".css", ".js", ".ts", ".tsx", ".py",
    ".sh", ".cff", ".robot", ".toml", ".env",
}

# Files whose occurrences are deliberate and must survive a rename.
#   LICENSE / LICENSE-CONTENT.md : "The 300 Years Later contributors" is the attribution entity.
#     Changing it rewrites who the licence grants from — a legal decision, not a find-and-replace.
#   docs/adr/0021 : the ADR records the decision; it must keep quoting the old title.
#   CHANGELOG.md : history is history.
KEEP: set[str] = {
    "LICENSE",
    "LICENSE-CONTENT.md",
    "CHANGELOG.md",
    "docs/adr/0021-titre-public-afterloom.md",
    "tools/apply_public_title.py",
}


def candidates() -> list[Path]:
    """Git-tracked files only. An ignored file such as .claude/settings.local.json holds machine-local
    state — including the anonymous commit identity — and rewriting it would break the local setup."""
    import subprocess

    try:
        out = subprocess.run(
            ["git", "-C", str(ROOT), "ls-files", "-z"],
            capture_output=True, text=True, check=True,
        ).stdout
        paths = [ROOT / rel for rel in out.split("\0") if rel]
    except (OSError, subprocess.CalledProcessError):
        print("! git unavailable, falling back to a filesystem walk (ignored files are skipped by name)")
        paths = [p for p in ROOT.rglob("*")
                 if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)]

    keep: list[Path] = []
    for p in sorted(set(paths)):
        if not p.is_file():
            continue
        rel = p.relative_to(ROOT).as_posix()
        # extensionless files count only when they are protected, so the report stays honest
        if p.suffix.lower() in TEXT_SUFFIXES or rel in KEEP:
            keep.append(p)
    return keep


def main() -> int:
    ap = argparse.ArgumentParser(description="Rename the public title across the repository.")
    ap.add_argument("--to", required=True, help='the new public title, e.g. "Afterloom"')
    ap.add_argument("--from", dest="old", default=CURRENT, help=f'the title to replace (default: "{CURRENT}")')
    ap.add_argument("--apply", action="store_true", help="write the files (default: dry run)")
    args = ap.parse_args()

    old, new = args.old, args.to
    if not new.strip():
        print("✗ --to cannot be empty")
        return 1
    if old == new:
        print("✗ --from and --to are the same")
        return 1
    if re.search(r"[<>/\\]", new):
        print("✗ the title must not contain < > / or \\")
        return 1

    # "The <title> contributors" is the entity the two licences grant from, and it must read the same
    # in LICENSE, CITATION.cff and the plugin manifests. Renaming it is a legal decision, so the tool
    # steps over it and reports it instead.
    attribution = f"The {old} contributors"
    pattern = re.compile(f"{re.escape(attribution)}|{re.escape(old)}")

    changed: list[tuple[str, int]] = []
    kept: list[tuple[str, int]] = []
    attributions = 0

    for path in candidates():
        rel = path.relative_to(ROOT).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        found = pattern.findall(text)
        if not found:
            continue
        here = sum(1 for m in found if m == attribution)
        attributions += here
        hits = len(found) - here
        if rel in KEEP:
            kept.append((rel, len(found)))
            continue
        if not hits:
            kept.append((rel, here))
            continue
        changed.append((rel, hits))
        if args.apply:
            path.write_text(
                pattern.sub(lambda m: m.group(0) if m.group(0) == attribution else new, text),
                encoding="utf-8",
            )

    total = sum(n for _, n in changed)
    verb = "replaced" if args.apply else "would replace"
    print(f'{verb} {total} occurrence(s) of "{old}" with "{new}" in {len(changed)} file(s)')
    for rel, n in changed:
        print(f"   {n:>3}  {rel}")
    if kept:
        print("\nleft untouched on purpose:")
        for rel, n in kept:
            print(f"   {n:>3}  {rel}")
    if attributions:
        print(f'\n{attributions} occurrence(s) of "{attribution}" kept everywhere — the licence'
              "\nattribution entity. Change it only with a decision written down, in one pass across"
              "\nLICENSE, LICENSE-CONTENT.md, CITATION.cff and .claude-plugin/.")

    if not changed:
        print(f'\nNothing to do — "{old}" does not appear outside the protected files.')
        return 0

    if args.apply:
        print(
            "\nNext, in this order:\n"
            "  1. python3 tools/repo_audit.py && python3 tools/privacy_scan.py\n"
            "  2. python3 -m pytest tests/web -q      (the landing asserts on the title)\n"
            "  3. reread .github/about.yml, marketing/steam/page.md and marketing/presskit/index.md\n"
            "     by eye — a title reads differently in a sentence written for the old one\n"
            "  4. the repository slug is NOT renamed: doing that breaks the plugin path, the badges\n"
            "     and every shared link. ADR 0021 explains what to fix first if you decide to.\n"
            "  5. trademark search before any public announcement (legal/21_marque-pi.md)"
        )
    else:
        print(f'\nDry run. Add --apply to write. Nothing has changed.')
    return 0


if __name__ == "__main__":
    sys.exit(main())
