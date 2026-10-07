#!/usr/bin/env python3
"""Audit des licences : chaque dossier d'assets tiers ou d'addon doit contenir
SOURCE.md et LICENSE, avec une licence autorisée (CC0, MIT, OFL, Apache-2.0).
Les dossiers générés par nos scripts contiennent un GENERATED.md à la place.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCOPES = ["game/Plugins", "marketing/landing-react/public/fonts", "marketing/landing/fonts", "media"]
ALLOWED = re.compile(r"(CC0|Creative Commons Zero|MIT License|SIL Open Font License|OFL|Apache License)", re.I)


def main() -> int:
    issues, checked = [], 0
    for scope in SCOPES:
        base = ROOT / scope
        if not base.is_dir():
            continue
        for d in sorted(p for p in base.iterdir() if p.is_dir()):
            checked += 1
            if (d / "GENERATED.md").is_file():
                continue
            lic = next((d / n for n in ("LICENSE", "LICENSE.md", "LICENSE.txt", "OFL.txt") if (d / n).is_file()), None)
            if not (d / "SOURCE.md").is_file():
                issues.append(f"{d.relative_to(ROOT)}: SOURCE.md manquant")
            if lic is None:
                issues.append(f"{d.relative_to(ROOT)}: fichier LICENSE manquant")
            elif not ALLOWED.search(lic.read_text(encoding="utf-8", errors="ignore")[:4000]):
                issues.append(f"{d.relative_to(ROOT)}: licence non reconnue comme autorisée — demander à l'humain")
    tpl = ROOT / "THIRD_PARTY_LICENSES.md"
    if not tpl.is_file():
        issues.append("THIRD_PARTY_LICENSES.md manquant")
    print(f"[license_audit] {checked} dossier(s) vérifié(s), {len(issues)} problème(s)")
    for i in issues:
        print("  ✗", i)
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
