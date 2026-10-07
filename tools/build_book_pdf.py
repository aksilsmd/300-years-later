#!/usr/bin/env python3
"""Typeset the novel as a PDF / Compose le roman en PDF.

EN: Reads book/<lang>/*.md — one file per chapter, YAML front matter for part, number, voice and
    title — and typesets a real book: cover, half title, copyright page, contents, part openers,
    chapters, folios. Colours and type come from design-system/tokens.json, so the book and the
    repository look like the same project.

    The body is set in the serif reserved by the design system (§3) for the world's own voice:
    chronicle, museum plates, and this novel. Nothing here is loaded from the network — no remote
    font, no CDN (AGENTS.md §4.3) — so the PDF is identical offline.

FR: Lit book/<langue>/*.md — un fichier par chapitre, en-tête YAML pour la partie, le numéro, la voix
    et le titre — et compose un vrai livre : couverture, faux-titre, page de droits, sommaire,
    ouvertures de partie, chapitres, folios. Les couleurs et la typographie viennent de
    design-system/tokens.json. Aucune ressource réseau.

    python3 tools/build_book_pdf.py                  # FR
    python3 tools/build_book_pdf.py --lang fr --open # et ouvre le fichier produit
    python3 tools/build_book_pdf.py --html-only      # sort le HTML de composition, pour déboguer
"""
from __future__ import annotations

import argparse
import html as html_mod
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "design-system" / "tokens.json").read_text(encoding="utf-8"))["tokens"]
C = TOKENS["color"]

# The book's own identity. The game's public title lives in studio.config.yaml; this is the title of
# the book inside the fiction, and tools/apply_public_title.py deliberately does not touch it.
BOOK = {
    "fr": {
        "title": "Le Livre des Traces",
        "subtitle": "Roman fondateur d'Afterloom",
        "parts": {1: ("Partie I", "Ce qui tombe", "an 0")},
        "contents": "Sommaire",
        "cover_note": "Vallée de Brumecombe · an 0",
        "colophon_title": "À propos de ce volume",
        "chapter_word": "Chapitre",
        "state": (
            "Ce volume contient la <strong>Partie I</strong> du roman, soit huit chapitres sur les "
            "quarante prévus. Les parties II à V — « Ce qui s'écrit » (an 300), « Ce qui se fabrique » "
            "(an 600), « Ce qui se range » (an 900) et « Ce qui tient » — existent à ce jour sous "
            "forme de plan détaillé, chapitre par chapitre, dans "
            "<em>docs/design/14_ROMAN_LIVRE_DES_TRACES.md</em>. Elles ne sont pas rédigées. "
            "Ce livre ne prétend pas être fini."
        ),
        "rights": (
            "Texte sous licence Creative Commons Attribution 4.0 (CC BY 4.0). "
            "Créditez « The 300 Years Later contributors ».<br>"
            "Personnages, lieux, peuples et croyances sont entièrement inventés : "
            "aucune religion, culture, organisation ou personne réelle n'y est représentée."
        ),
    },
}


# --------------------------------------------------------------------------- markdown, minimal
def inline(text: str) -> str:
    """Just what the manuscript uses: emphasis, strong, and typographic apostrophes."""
    text = html_mod.escape(text, quote=False)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    return text.replace("'", "’")


def parse_chapter(path: Path) -> dict:
    raw = path.read_text(encoding="utf-8")
    meta: dict = {}
    body = raw
    if raw.startswith("---"):
        end = raw.index("\n---", 3)
        for line in raw[3:end].strip().splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                meta[k.strip()] = v.strip()
        body = raw[end + 4:]

    blocks: list[str] = []
    for chunk in [c.strip() for c in body.split("\n\n") if c.strip()]:
        if chunk == "*":
            blocks.append('<p class="dinkus">*</p>')
        else:
            blocks.append(f"<p>{inline(chunk)}</p>")
    # The first paragraph of every scene opens flush left; the rest are indented, as a book does.
    out: list[str] = []
    opener = True
    for b in blocks:
        if b.startswith('<p class="dinkus"'):
            out.append(b)
            opener = True
            continue
        out.append(b.replace("<p>", '<p class="opener">', 1) if opener else b)
        opener = False

    meta["chapter"] = int(meta.get("chapter", 0))
    meta["part"] = int(meta.get("part", 1))
    meta["html"] = "\n".join(out)
    return meta


# --------------------------------------------------------------------------- composition
def core_svg(height: int = 300) -> str:
    """The stratigraphic core of the brand: four beds, one disc each, radius doubling downward."""
    band = height / 4
    rows = []
    for i, r in enumerate((3, 6, 11, 19)):
        y = i * band
        rows.append(f'<rect x="0" y="{y:.1f}" width="86" height="{band:.1f}" fill="{C[f"af-bed-{i}"]}"/>')
        rows.append(f'<circle cx="29" cy="{y + band / 2:.1f}" r="{r}" fill="{C[f"af-era-{i}"]}"/>')
    return f'<svg viewBox="0 0 86 {height}" preserveAspectRatio="none" class="core">{"".join(rows)}</svg>'


def css() -> str:
    return f"""
/* Margins live here, not in the Playwright call: the cover is rendered as its own full-bleed pass
   so no folio lands on it, and the two passes are merged at the end. */
@page {{ size: 148mm 210mm; margin: 18mm 16mm 20mm 16mm; }}
@page.cover-page {{ margin: 0; }}

:root {{
  --paper: {C['af-paper']}; --ink: {C['af-ink']}; --soft: {C['af-ink-soft']};
  --rule: {C['af-rule']}; --signal: {C['af-signal']};
}}
* {{ box-sizing: border-box; }}
/* Chromium never paints a background into the @page margin area — neither from <html> nor from a
   fixed layer, both are clipped to the content box — so every sheet would print with a white border.
   The paper is therefore laid down underneath each page at the merge step, in paint_paper(). */
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; background: transparent; }}
body {{
  margin: 0; background: {C['af-paper']}; color: var(--ink);
  font-family: "Source Serif 4", "Liberation Serif", Georgia, serif;
  font-size: 10.6pt; line-height: 1.62; text-align: justify; hyphens: auto;
}}
.sheet {{ page-break-after: always; }}
.sheet:last-child {{ page-break-after: auto; }}

/* ---------------------------------------------------------------- cover */
.cover {{ position: relative; width: 148mm; height: 210mm; background: var(--paper); overflow: hidden; }}
.cover .core {{ position: absolute; inset: 0 auto 0 0; width: 34mm; height: 210mm; }}
.cover .field {{ position: absolute; left: 34mm; right: 0; top: 0; bottom: 0; padding: 22mm 14mm; }}
.cover h1 {{
  font-family: Inter, "Helvetica Neue", Arial, sans-serif; font-weight: 900;
  font-size: 30pt; line-height: 1.0; letter-spacing: -0.035em;
  margin: 0 0 6mm; text-align: left; text-transform: uppercase;
}}
.cover .sub {{ font-size: 11pt; color: var(--soft); font-style: italic; margin: 0; text-align: left; }}
.cover .partline {{
  position: absolute; left: 14mm; right: 14mm; bottom: 34mm; padding-top: 3mm;
  border-top: 0.4pt solid var(--rule); text-align: left;
}}
.cover .partline b {{ display: block; font-family: Inter, sans-serif; font-size: 13pt; letter-spacing: -0.02em; }}
.mono {{ font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: 8pt;
         letter-spacing: 0.06em; color: var(--soft); text-transform: uppercase; }}
.cover .mono.place {{ position: absolute; left: 14mm; bottom: 18mm; }}

/* ---------------------------------------------------------------- front matter */
.halftitle {{ padding-top: 70mm; text-align: center; }}
.halftitle h2 {{ font-family: Inter, sans-serif; font-weight: 800; letter-spacing: -0.03em;
                 text-transform: uppercase; font-size: 15pt; margin: 0; }}
.rights {{ display: flex; flex-direction: column; justify-content: flex-end; min-height: 160mm;
           font-size: 8.4pt; line-height: 1.5; color: var(--soft); text-align: left; }}
.rights p {{ margin: 0 0 4mm; }}
.rights .note {{ border-left: 2pt solid var(--signal); padding-left: 4mm; color: var(--ink); }}
.rights h3 {{ font-family: Inter, sans-serif; font-size: 9pt; text-transform: uppercase;
              letter-spacing: 0.08em; color: var(--ink); margin: 0 0 2mm; }}

h2.sectiontitle {{ font-family: Inter, sans-serif; font-size: 10pt; text-transform: uppercase;
                   letter-spacing: 0.12em; font-weight: 700; margin: 0 0 8mm;
                   padding-bottom: 2mm; border-bottom: 0.4pt solid var(--rule); }}
.toc {{ text-align: left; }}
.toc .row {{ display: flex; align-items: baseline; gap: 3mm; margin: 0 0 2.6mm; }}
.toc .n {{ font-family: "DejaVu Sans Mono", monospace; font-size: 8pt; color: var(--soft); width: 7mm; }}
.toc .t {{ flex: 1; }}
.toc .v {{ font-family: "DejaVu Sans Mono", monospace; font-size: 7.5pt; color: var(--soft); }}

/* ---------------------------------------------------------------- part opener */
.partopen {{ position: relative; height: 170mm; display: flex; flex-direction: column; justify-content: center; }}
.partopen .k {{ font-family: "DejaVu Sans Mono", monospace; font-size: 8pt; letter-spacing: 0.14em;
                color: var(--soft); text-transform: uppercase; margin-bottom: 4mm; }}
.partopen h2 {{ font-family: Inter, sans-serif; font-weight: 900; font-size: 24pt; letter-spacing: -0.035em;
                margin: 0 0 5mm; text-align: left; }}
.partopen .era {{ font-style: italic; color: var(--soft); text-align: left; }}

/* ---------------------------------------------------------------- chapters */
.chapter {{ page-break-before: always; }}
.chapter header {{ margin-bottom: 10mm; }}
.chapter .k {{ font-family: "DejaVu Sans Mono", monospace; font-size: 7.6pt; letter-spacing: 0.14em;
               color: var(--soft); text-transform: uppercase; }}
.chapter h3 {{ font-family: Inter, sans-serif; font-weight: 800; font-size: 15pt; letter-spacing: -0.03em;
               margin: 2mm 0 0; text-align: left; }}
.chapter.veille h3 {{ font-style: italic; font-weight: 600; }}
.chapter p {{ margin: 0; text-indent: 4.5mm; orphans: 2; widows: 2; }}
.chapter p.opener {{ text-indent: 0; }}
.chapter p.opener::first-line {{ font-variant: small-caps; letter-spacing: 0.02em; }}
.chapter p.dinkus {{ text-indent: 0; text-align: center; margin: 4.5mm 0; color: var(--soft); letter-spacing: 0.4em; }}

.colophon p {{ text-indent: 0; font-size: 9pt; color: var(--soft); text-align: left; }}
"""


def build_cover(lang: str) -> str:
    b = BOOK[lang]
    _, (part_k, part_title, _) = 1, b["parts"][1]
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><title>cover</title>
<style>{css()}
@page {{ margin: 0; }}
html, body {{ width: 148mm; height: 210mm; margin: 0; }}
</style></head><body>
<div class="cover">{core_svg()}
  <div class="field">
    <h1>{html_mod.escape(b['title'])}</h1>
    <p class="sub">{html_mod.escape(b['subtitle'])}</p>
    <div class="partline"><span class="mono">{part_k}</span><b>{html_mod.escape(part_title)}</b></div>
    <div class="mono place">{html_mod.escape(b['cover_note'])}</div>
  </div>
</div></body></html>"""


def build_html(lang: str, chapters: list[dict]) -> str:
    b = BOOK[lang]
    part_no, (part_k, part_title, part_era) = 1, b["parts"][1]

    toc = "\n".join(
        f'<div class="row"><span class="n">{c["chapter"]:02d}</span>'
        f'<span class="t">{inline(c["title"])}</span>'
        f'<span class="v">{inline(c.get("voice", ""))}</span></div>'
        for c in chapters
    )

    body = []
    for c in chapters:
        kind = " veille" if c.get("kind") == "veille" else ""
        label = "Veille I" if c.get("kind") == "veille" else f'{b["chapter_word"]} {c["chapter"]}'
        body.append(
            f'<section class="chapter{kind}"><header>'
            f'<div class="k">{label} · {inline(c.get("voice",""))} · {inline(c.get("place",""))}</div>'
            f'<h3>{inline(c["title"])}</h3></header>{c["html"]}</section>'
        )

    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<title>{html_mod.escape(b['title'])}</title><style>{css()}</style></head><body>

<div class="sheet halftitle"><h2>{html_mod.escape(b['title'])}</h2></div>

<div class="sheet"><div class="rights">
  <h3>{html_mod.escape(b['colophon_title'])}</h3>
  <p class="note">{b['state']}</p>
  <p>{b['rights']}</p>
  <p>Composé le {date.today().strftime('%d/%m/%Y')} par <em>tools/build_book_pdf.py</em>,
     d'après <em>design-system/tokens.css</em>. Aucune ressource distante.</p>
</div></div>

<div class="sheet"><h2 class="sectiontitle">{html_mod.escape(b['contents'])}</h2>
  <div class="toc">{toc}</div></div>

<div class="sheet"><div class="partopen">
  <div class="k">{part_k} · {html_mod.escape(part_era)}</div>
  <h2>{html_mod.escape(part_title)}</h2>
  <p class="era">Le monde avant l'histoire. Comment une distraction devient un commencement.</p>
</div></div>

{''.join(body)}
</body></html>"""


def paint_paper(path: Path) -> Path:
    """A single 148×210 mm sheet filled with the paper colour, used as the backing for every body
    page. Done here rather than in CSS because the @page margin area is outside anything the browser
    will paint."""
    from reportlab.lib.colors import HexColor
    from reportlab.lib.units import mm
    from reportlab.pdfgen import canvas as rl_canvas

    c = rl_canvas.Canvas(str(path), pagesize=(148 * mm, 210 * mm))
    c.setFillColor(HexColor(C["af-paper"]))
    c.rect(0, 0, 148 * mm, 210 * mm, stroke=0, fill=1)
    c.showPage()
    c.save()
    return path


def main() -> int:
    ap = argparse.ArgumentParser(description="Typeset the novel as a PDF.")
    ap.add_argument("--lang", default="fr", choices=sorted(BOOK))
    ap.add_argument("--html-only", action="store_true", help="write the composition HTML and stop")
    args = ap.parse_args()

    src = ROOT / "book" / args.lang
    files = sorted(src.glob("*.md"))
    if not files:
        print(f"✗ no chapters in {src.relative_to(ROOT)}")
        return 1
    chapters = sorted((parse_chapter(f) for f in files), key=lambda c: c["chapter"])

    out_dir = ROOT / "book" / "build"
    out_dir.mkdir(parents=True, exist_ok=True)
    html_path = out_dir / f"livre-des-traces-{args.lang}.html"
    cover_path = out_dir / f"couverture-{args.lang}.html"
    html_path.write_text(build_html(args.lang, chapters), encoding="utf-8")
    cover_path.write_text(build_cover(args.lang), encoding="utf-8")
    words = sum(len(re.sub(r"<[^>]+>", " ", c["html"]).split()) for c in chapters)
    print(f"✓ {len(chapters)} chapitres, {words} mots → {html_path.relative_to(ROOT)}")
    if args.html_only:
        return 0

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("✗ Playwright is required: python3 -m pip install --break-system-packages playwright")
        return 1

    pdf_path = out_dir / f"livre-des-traces-{args.lang}.pdf"
    cover_pdf = out_dir / f".cover-{args.lang}.pdf"
    body_pdf = out_dir / f".body-{args.lang}.pdf"
    foot = (
        '<div style="width:100%;font-family:DejaVu Sans Mono,monospace;font-size:7px;'
        f'color:{C["af-ink-soft"]};padding:0 16mm 9mm;display:flex;justify-content:space-between;">'
        f'<span>{BOOK[args.lang]["title"]}</span><span class="pageNumber"></span></div>'
    )
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Cover: full bleed, no running foot.
        page.goto(cover_path.as_uri(), wait_until="load")
        page.pdf(path=str(cover_pdf), prefer_css_page_size=True, print_background=True,
                 margin={"top": "0", "bottom": "0", "left": "0", "right": "0"})
        # Body: margins come from the stylesheet, folios from the footer template.
        page.goto(html_path.as_uri(), wait_until="load")
        page.pdf(path=str(body_pdf), prefer_css_page_size=True, print_background=True,
                 display_header_footer=True, header_template="<div></div>", footer_template=foot)
        browser.close()

    from pypdf import PdfReader, PdfWriter

    writer = PdfWriter()
    paper = paint_paper(out_dir / f".paper-{args.lang}.pdf")
    for part, needs_paper in ((cover_pdf, False), (body_pdf, True)):
        for pg in PdfReader(str(part)).pages:
            if needs_paper:
                sheet = PdfReader(str(paper)).pages[0]
                sheet.merge_page(pg)
                writer.add_page(sheet)
            else:
                writer.add_page(pg)
    paper.unlink(missing_ok=True)
    writer.add_metadata({
        "/Title": BOOK[args.lang]["title"],
        "/Subject": BOOK[args.lang]["subtitle"],
        "/Author": "The 300 Years Later contributors",
    })
    # Each body page carries its own copy of the paper rectangle; fold the identical ones together.
    if hasattr(writer, "compress_identical_objects"):
        writer.compress_identical_objects()
    with open(pdf_path, "wb") as fh:
        writer.write(fh)
    cover_pdf.unlink(missing_ok=True)
    body_pdf.unlink(missing_ok=True)

    pages = len(PdfReader(str(pdf_path)).pages)
    kb = round(pdf_path.stat().st_size / 1024, 1)
    print(f"✓ {pdf_path.relative_to(ROOT)}  {pages} pages  {kb} KB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
