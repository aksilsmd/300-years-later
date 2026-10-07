#!/usr/bin/env python3
"""Check that every media file referenced by the landing / video projects is approved.

EN: Fails if a file in marketing/landing-react/public/media/ or referenced in src/media.ts
    has no row with status "approved"/"validé" in media/APPROVALS.md.
FR: Échoue si un média utilisé par la landing n'a pas de ligne « validé » dans media/APPROVALS.md.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APPROVALS = ROOT / "media" / "APPROVALS.md"
MEDIA_DIR = ROOT / "marketing" / "landing-react" / "public" / "media"
MEDIA_TS = ROOT / "marketing" / "landing-react" / "src" / "media.ts"
EXTS = {".png", ".jpg", ".jpeg", ".webp", ".avif", ".mp4", ".webm", ".mov", ".gif"}
OK = {"approved", "validé", "valide", "validated"}


def approved_files() -> set[str]:
    names = set()
    for line in APPROVALS.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 8 or cells[0].startswith(("ID", "---", "*")):
            continue
        status = cells[7].strip("`*").lower()
        if status in OK and cells[1]:
            names.add(Path(cells[1].strip("`")).name)
    return names


def used_files() -> set[str]:
    used = set()
    if MEDIA_DIR.exists():
        used |= {p.name for p in MEDIA_DIR.rglob("*") if p.suffix.lower() in EXTS}
    if MEDIA_TS.exists():
        code = re.sub(r"/\*.*?\*/", "", MEDIA_TS.read_text(encoding="utf-8"), flags=re.S)
        code = re.sub(r"//.*", "", code)
        for m in re.finditer(r"[\"']([^\"']+\.(?:png|jpe?g|webp|avif|mp4|webm|mov|gif))[\"']", code, re.I):
            used.add(Path(m.group(1)).name)
    return used


def main() -> int:
    ok, used = approved_files(), used_files()
    missing = sorted(used - ok)
    if missing:
        print("✗ Media used without approval in media/APPROVALS.md:")
        for name in missing:
            print("   -", name)
        return 1
    print(f"✓ media approvals: {len(used)} file(s) used, all approved")
    return 0


if __name__ == "__main__":
    sys.exit(main())
