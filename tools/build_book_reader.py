#!/usr/bin/env python3
"""Build the web reader / Construit la liseuse web.

EN: Injects book/<lang>/*.md into book/reader/template.html and writes one self-contained page.
    The page paginates the text at runtime against the real page box, so a chapter reflows when the
    window changes instead of being frozen at build time. No remote font, script or stylesheet
    (AGENTS.md §4.3); the file works offline and from a file:// URL.

FR: Injecte book/<langue>/*.md dans book/reader/template.html et produit une page autonome. La page
    pagine le texte à l'exécution contre la vraie boîte de page : un chapitre se recompose quand la
    fenêtre change. Aucune police, aucun script, aucune feuille de style distante ; le fichier
    fonctionne hors ligne et depuis un file://.

    python3 tools/build_book_reader.py
    python3 tools/build_book_reader.py --lang fr
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from build_book_pdf import BOOK, inline, parse_chapter  # noqa: E402  (same manuscript parser)

EXTRA = {
    "fr": {
        "shortTitle": "Le Livre des Traces",
        "next": (
            "Vous avez lu les huit chapitres de la Partie I. Les quatre parties suivantes — "
            "« Ce qui s'écrit » (an 300), « Ce qui se fabrique » (an 600), « Ce qui se range » (an 900) "
            "et « Ce qui tient » — sont planifiées chapitre par chapitre dans "
            "<em>docs/design/14_ROMAN_LIVRE_DES_TRACES.md</em>, et ne sont pas encore rédigées. "
            "Cette liseuse les affichera telles quelles dès qu'elles seront écrites : il suffira "
            "d'ajouter les fichiers dans <em>book/fr/</em>."
        ),
    },
}


def main() -> int:
    ap = argparse.ArgumentParser(description="Build the self-contained web reader.")
    ap.add_argument("--lang", default="fr", choices=sorted(BOOK))
    args = ap.parse_args()
    lang = args.lang

    src = ROOT / "book" / lang
    files = sorted(src.glob("*.md"))
    if not files:
        print(f"✗ no chapters in {src.relative_to(ROOT)}")
        return 1
    chapters = sorted((parse_chapter(f) for f in files), key=lambda c: c["chapter"])

    b = BOOK[lang]
    part_key, part_title, part_era = b["parts"][1]
    data = {
        "title": b["title"],
        "shortTitle": EXTRA[lang]["shortTitle"],
        "subtitle": b["subtitle"],
        "partKey": part_key,
        "partTitle": part_title,
        "coverNote": b["cover_note"],
        "colophonTitle": b["colophon_title"],
        "state": b["state"],
        "rights": b["rights"],
        "next": EXTRA[lang]["next"],
        "chapters": [
            {
                "n": c["chapter"],
                "title": inline(c["title"]),
                "voice": c.get("voice", ""),
                "place": c.get("place", ""),
                "kind": c.get("kind", ""),
                "label": "Veille I" if c.get("kind") == "veille" else f'{b["chapter_word"]} {c["chapter"]}',
                # one HTML block per paragraph, exactly what the PDF uses
                "blocks": [blk for blk in c["html"].split("\n") if blk.strip()],
            }
            for c in chapters
        ],
    }

    template = (ROOT / "book" / "reader" / "template.html").read_text(encoding="utf-8")
    marker = "/*__BOOK_DATA__*/ null"
    if marker not in template:
        print("✗ template.html no longer contains the data marker")
        return 1
    # </script> inside the data would close the block early; escape it.
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    page = template.replace(marker, payload)

    out = ROOT / "book" / "build" / f"liseuse-{lang}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")

    blocks = sum(len(c["blocks"]) for c in data["chapters"])
    kb = round(out.stat().st_size / 1024, 1)
    print(f"✓ {out.relative_to(ROOT)}  {len(data['chapters'])} chapitres, {blocks} blocs, {kb} KB")

    for bad in ("http://", "https://", "//cdn", "fonts.googleapis"):
        if bad in page.replace('xmlns="http://www.w3.org/2000/svg"', ""):
            print(f"✗ remote reference found in the reader: {bad}")
            return 1
    print("✓ aucune ressource distante")
    return 0


if __name__ == "__main__":
    sys.exit(main())
