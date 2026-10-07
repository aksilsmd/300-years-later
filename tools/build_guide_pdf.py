#!/usr/bin/env python3
"""Construit le guide PDF illustré du studio (Chromium headless via Playwright).

Contenu : couverture, sommaire, guides docs/guides/*.md, schémas docs/diagrams/*.svg,
captures RÉELLES (landing page de référence, sorties des outils du kit) et, plus tard,
les rendus du jeu marqués « validé » dans media/APPROVALS.md — jamais d'autres images.

    python3 tools/build_guide_pdf.py            # régénère captures + PDF
Sortie : docs/guide/300-years-later-guide.pdf
Dépendances : playwright (navigateur Chromium installé), markdown.
"""
from __future__ import annotations

import html
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

import markdown
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
GUIDES = ROOT / "docs" / "guides"
CAPS = GUIDES / "captures"
OUT = ROOT / "docs" / "guide" / "300-years-later-guide.pdf"

TERMINAL_CMDS = [
    ("01_doctor", "python3 tools/doctor.py", "Diagnostic de l'environnement (étape A)"),
    ("02_validate", "python3 tools/validate_data.py", "Validation des données du jeu"),
    ("03_privacy", "python3 tools/privacy_scan.py", "Scan de confidentialité avant publication"),
    ("04_licences", "python3 tools/license_audit.py", "Audit des licences"),
]


def run(cmd: str) -> str:
    out = subprocess.run(cmd, shell=True, cwd=ROOT, capture_output=True, text=True, timeout=300)
    text = (out.stdout + out.stderr).strip()
    text = text.replace(str(Path.home()), "~")  # aucun chemin personnel dans les captures
    return text


def terminal_html(title: str, cmd: str, output: str) -> str:
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;background:#fbf6ee;font-family:system-ui,sans-serif}}
.win{{margin:24px;border-radius:12px;overflow:hidden;box-shadow:0 1px 0 #2a1a0e;border:2px solid #2a1a0e;width:1100px}}
.bar{{background:#2a1a0e;color:#f3d9b1;padding:10px 16px;font-size:14px}}
pre{{margin:0;background:#1d1712;color:#f1e6d8;padding:18px 20px;font:14px/1.5 "DejaVu Sans Mono",Menlo,Consolas,monospace;white-space:pre-wrap}}
.p{{color:#e08a4f}}</style></head><body><div class="win" id="w"><div class="bar">{html.escape(title)}</div>
<pre><span class="p">$</span> {html.escape(cmd)}
{html.escape(output)}</pre></div></body></html>"""


def capture(page) -> list[tuple[str, str]]:
    CAPS.mkdir(parents=True, exist_ok=True)
    shots: list[tuple[str, str]] = []
    tmp = CAPS / "_tmp.html"
    for name, cmd, title in TERMINAL_CMDS:
        tmp.write_text(terminal_html(title, cmd, run(cmd)), encoding="utf-8")
        page.set_viewport_size({"width": 1160, "height": 800})
        page.goto(tmp.as_uri())
        page.locator("#w").screenshot(path=str(CAPS / f"{name}.png"))
        shots.append((f"{name}.png", title))
    tmp.unlink(missing_ok=True)
    landing = (ROOT / "marketing" / "landing" / "index.html").as_uri()
    for name, vw, title in [("10_landing_desktop", (1440, 900), "Landing page de référence — bureau"),
                            ("11_landing_mobile", (390, 844), "Landing page de référence — mobile")]:
        ctx = page.context.browser.new_context(viewport={"width": vw[0], "height": vw[1]}, reduced_motion="reduce")
        p = ctx.new_page()
        p.goto(landing)
        p.wait_for_timeout(600)
        p.screenshot(path=str(CAPS / f"{name}.png"))
        shots.append((f"{name}.png", title))
        if name == "10_landing_desktop":
            p.evaluate("document.querySelector(\".layer[data-era='3']\").scrollIntoView({block:'center'})")
            p.wait_for_timeout(400)
            p.screenshot(path=str(CAPS / "12_landing_strates.png"))
            shots.append(("12_landing_strates.png", "Landing — la page prend la couleur de l'époque lue"))
        ctx.close()
    return shots


def approved_game_media() -> list[tuple[Path, str]]:
    """Rendus du jeu validés (lignes « validé » de media/APPROVALS.md)."""
    reg = ROOT / "media" / "APPROVALS.md"
    items = []
    for line in reg.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 8 and cells[7].lower() == "validé":
            f = ROOT / "media" / cells[1]
            if f.is_file() and f.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}:
                items.append((f, f"Plan {cells[0]}"))
    return items


def md_to_html(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    body = markdown.markdown(text, extensions=["tables", "fenced_code"])
    # chemins relatifs des images → URI absolus
    body = re.sub(r'src="(\.\./[^"]+)"', lambda m: f'src="{(path.parent / m.group(1)).resolve().as_uri()}"', body)
    body = re.sub(r'href="(?!https?:|#)([^"]+)"', r'href="#"', body)  # liens internes neutralisés dans le PDF
    return body


CSS = """
@page { size: A4; margin: 18mm 16mm 20mm; @bottom-right { content: counter(page); } }
body { font: 10.5pt/1.55 system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; color: #2a1a0e; }
h1, h2, h3 { font-family: Georgia, "Times New Roman", serif; line-height: 1.15; }
h1 { font-size: 24pt; margin: 0 0 10pt; page-break-before: always; }
h2 { font-size: 15pt; margin: 16pt 0 6pt; } h3 { font-size: 12pt; }
table { border-collapse: collapse; width: 100%; font-size: 9pt; margin: 8pt 0; page-break-inside: avoid; }
th, td { border-bottom: .6pt solid #c9b8a6; padding: 4pt 6pt 4pt 0; text-align: left; vertical-align: top; }
th { color: #8c3f12; }
code, pre { font-family: "DejaVu Sans Mono", Menlo, Consolas, monospace; font-size: 8.8pt; }
pre { background: #f6efe4; padding: 8pt; border-radius: 4pt; white-space: pre-wrap; }
img { max-width: 100%; page-break-inside: avoid; }
figure { margin: 10pt 0; page-break-inside: avoid; } figcaption { font-size: 9pt; color: #6b5a4c; }
blockquote { border-left: 3pt solid #b5541c; margin: 8pt 0; padding: 2pt 10pt; color: #4a3829; }
.cover { height: 250mm; display: flex; flex-direction: column; justify-content: flex-end; background: #f3d9b1; margin: -18mm -16mm 0; padding: 0 16mm 30mm; }
.cover .y { font: 800 120pt/0.85 Georgia, serif; letter-spacing: -4pt; }
.cover .t { font: 600 26pt Georgia, serif; } .cover p { font-size: 12pt; max-width: 120mm; }
.toc li { margin: 2pt 0; }
.note { background: #fbe8e4; border: 1pt solid #a8342a; padding: 8pt; border-radius: 4pt; }
"""


def build() -> None:
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        shots = capture(page)
        guides = sorted(GUIDES.glob("[0-9][0-9]_*.md"))
        toc = "".join(f"<li>{html.escape(g.stem[3:].replace('_', ' ').capitalize())}</li>" for g in guides)
        parts = [f"""<section class="cover"><div class="y">300</div><div class="t">Years Later — guide du studio</div>
<p>Construire un jeu coopératif 3D réaliste sous Unreal Engine 5.8 avec une IA, de A à Z : installation, code, tests, conformité, médias, lancement.</p>
<p>Édition du {date.today().strftime('%d/%m/%Y')} · licence CC BY 4.0</p></section>
<h1>Sommaire</h1><ol class="toc"><li>À lire d'abord</li>{toc}<li>Schémas</li><li>Captures d'écran</li><li>Images du jeu</li></ol>
<h1>À lire d'abord</h1>
<p class="note"><b>Ce guide ne contient aucune image du jeu</b> tant qu'aucun rendu n'a été produit dans Unreal Engine et validé par un humain. Les captures présentées sont réelles : la landing page de référence et les sorties des outils du kit. Les schémas expliquent le fonctionnement ; ils ne représentent pas le jeu.</p>
<p>Le jeu visé est un titre indépendant réaliste de haute qualité, pas une production de plusieurs centaines de millions. Les budgets et durées sont détaillés dans le guide « Temps et coûts ».</p>"""]
        for g in guides:
            parts.append(md_to_html(g).replace("<h1>", "<h1>", 1))
        parts.append("<h1>Schémas</h1>")
        for svg in sorted((ROOT / "docs" / "diagrams").glob("*.svg")):
            parts.append(f'<figure><img src="{svg.as_uri()}"><figcaption>{html.escape(svg.stem[3:].replace("_", " "))}</figcaption></figure>')
        parts.append("<h1>Captures d'écran</h1><p>Captures réelles réalisées lors de la génération de ce guide.</p>")
        for f, title in shots:
            parts.append(f'<figure><img src="{(CAPS / f).as_uri()}"><figcaption>{html.escape(title)}</figcaption></figure>')
        media = approved_game_media()
        parts.append("<h1>Images du jeu</h1>")
        if media:
            for f, title in media:
                parts.append(f'<figure><img src="{f.as_uri()}"><figcaption>{html.escape(title)} — rendu Unreal validé</figcaption></figure>')
        else:
            parts.append("<p>Aucun rendu validé à ce jour. Les plans à produire sont décrits dans <code>docs/design/33_VISUAL_TARGETS.md</code> et <code>data/shotlist.json</code> ; ils apparaîtront ici automatiquement une fois marqués « validé » dans <code>media/APPROVALS.md</code>.</p>")
        doc = f"<!doctype html><html lang='fr'><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(parts)}</body></html>"
        tmp = OUT.parent / "_guide.html"
        OUT.parent.mkdir(parents=True, exist_ok=True)
        tmp.write_text(doc, encoding="utf-8")
        page.goto(tmp.as_uri())
        page.wait_for_timeout(800)
        page.pdf(path=str(OUT), format="A4", print_background=True, display_header_footer=True,
                 header_template="<span></span>",
                 footer_template="<div style='font-size:8px;width:100%;text-align:right;padding-right:16mm;color:#6b5a4c'><span class='pageNumber'></span> / <span class='totalPages'></span></div>",
                 margin={"top": "18mm", "bottom": "20mm", "left": "16mm", "right": "16mm"})
        tmp.unlink(missing_ok=True)
        browser.close()
    print(f"✓ {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    sys.exit(build())
