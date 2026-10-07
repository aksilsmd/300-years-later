#!/usr/bin/env python3
"""Render the brand images from the design tokens / Rend les images de marque depuis les jetons.

EN: docs/assets/*.png used to be produced by hand, which is how the repository ended up showing a
    banner carrying the old title next to alt text carrying the new one. These images are now
    generated from design-system/tokens.json and the strings below, so a title change is one command
    away from being visible everywhere.

    Nothing here depicts the game. Per the safety contract (AGENTS.md §4.6) no game image exists
    outside Unreal Engine: these are typographic and geometric only — a stratigraphic core, four
    bands, four discs, and type.

FR: docs/assets/*.png étaient faites à la main — c'est ainsi que le dépôt a fini par afficher une
    bannière portant l'ancien titre à côté d'un texte alternatif portant le nouveau. Ces images sont
    désormais générées depuis design-system/tokens.json et les textes ci-dessous.

    Rien ici ne représente le jeu (contrat de sécurité §4.6) : uniquement de la typographie et de la
    géométrie — une carotte stratigraphique, quatre bandes, quatre disques, et du texte.

    python3 tools/render_brand_assets.py            # writes docs/assets/*.png
    python3 tools/render_brand_assets.py --check    # fails if the files on disk are out of date
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("✗ Pillow is required: python3 -m pip install --break-system-packages Pillow")
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "docs" / "assets"
TOKENS = json.loads((ROOT / "design-system" / "tokens.json").read_text(encoding="utf-8"))["tokens"]
C = TOKENS["color"]

TITLE = "AFTERLOOM"
ERAS = ["0", "300", "600", "900"]

# The one place a string lives. Keep the pitch to three short lines: the card is read at thumbnail size.
COPY = {
    "fr": {
        "tagline": "un studio de jeu vidéo que votre IA fait tourner",
        "pitch": ["Quatre amis, quatre siècles, une vallée. Ce",
                  "que vous laissez derrière vous vieillit chez",
                  "les autres."],
        "command": "git clone … && claude",
        "meta": "OPEN SOURCE · MIT\nFR · EN",
        "era_prefix": "AN",
        "stats": [("8", "skills d'agent"), ("5.8", "Unreal Engine"),
                  ("35", "recettes"), ("22", "docs juridiques")],
    },
    "en": {
        "tagline": "the game studio your coding agent runs",
        "pitch": ["Four friends, four centuries, one valley. What",
                  "you leave behind ages in somebody else's",
                  "game."],
        "command": "git clone … && claude",
        "meta": "OPEN SOURCE · MIT\nFR · EN",
        "era_prefix": "YEAR",
        "stats": [("8", "agent skills"), ("5.8", "Unreal Engine"),
                  ("35", "ageing recipes"), ("22", "legal drafts")],
    },
}

FONTS = {
    "black": "/usr/share/fonts/opentype/inter/Inter-Black.otf",
    "bold": "/usr/share/fonts/opentype/inter/Inter-Bold.otf",
    "regular": "/usr/share/fonts/opentype/inter/Inter-Regular.otf",
    "mono": "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "mono_bold": "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf",
}


def rgb(token: str, over: str = "af-paper") -> tuple[int, int, int]:
    """Token to an RGB triple. The rule tokens are rgba(), which PNG has no use for, so they are
    flattened over the paper colour — the only surface they are ever drawn on."""
    v = C[token].strip()
    if v.startswith("#"):
        return tuple(int(v[i:i + 2], 16) for i in (1, 3, 5))  # type: ignore[return-value]
    nums = [p.strip() for p in v[v.index("(") + 1:v.rindex(")")].split(",")]
    r, g, b = (int(n) for n in nums[:3])
    a = float(nums[3])
    base = rgb(over) if over != token else (255, 255, 255)
    return tuple(round(c * a + base[i] * (1 - a)) for i, c in enumerate((r, g, b)))  # type: ignore[return-value]


def font(kind: str, size: int) -> ImageFont.FreeTypeFont:
    path = FONTS[kind]
    if not Path(path).is_file():
        raise SystemExit(f"✗ missing font: {path}\n  Debian/Ubuntu: apt-get install fonts-inter fonts-dejavu-core")
    return ImageFont.truetype(path, size)


def tracked(draw: ImageDraw.ImageDraw, xy, text: str, f, fill, tracking: float = 0.0) -> float:
    """Draw text letter by letter so the design system's -0.035em tracking is honoured."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=f, fill=fill)
        x += draw.textlength(ch, font=f) + tracking
    return x - xy[0]


def core(draw: ImageDraw.ImageDraw, x: int, y: int, w: int, h: int, lang: str) -> None:
    """The stratigraphic core: four bands, one disc per band, radius doubling as it goes down."""
    band = h // 4
    radii = [6, 18, 32, 52]
    prefix = COPY[lang]["era_prefix"]
    f_era = font("mono", 26)
    for i, year in enumerate(ERAS):
        top = y + i * band
        draw.rectangle([x, top, x + w, top + band], fill=rgb(f"af-bed-{i}"))
        if i:
            draw.line([(x, top), (x + w, top)], fill=rgb("af-rule"), width=1)
        cx, cy, r = x + w // 3, top + band // 2, radii[i]
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=rgb(f"af-era-{i}"))
        label = f"{prefix} {year}"
        draw.text((x + w - 40 - draw.textlength(label, font=f_era), top + 26),
                  label, font=f_era, fill=rgb("af-ink-soft"))


def render(lang: str, size: tuple[int, int], out: Path) -> None:
    w, h = size
    copy = COPY[lang]
    im = Image.new("RGB", (w, h), rgb("af-paper"))
    d = ImageDraw.Draw(im)

    core(d, 0, 0, int(w * 0.183), h, lang)
    x = int(w * 0.216)

    tracked(d, (x, int(h * 0.075)), TITLE, font("black", 124), rgb("af-ink"), tracking=-4.3)
    d.text((x, int(h * 0.235)), copy["tagline"], font=font("regular", 46), fill=rgb("af-ink-soft"))

    y = int(h * 0.345)
    f_pitch = font("regular", 44)
    for line in copy["pitch"]:
        d.text((x, y), line, font=f_pitch, fill=rgb("af-ink"))
        y += 66

    # Command block: sunken paper, hairline, 3px survey-red left edge (design system §6).
    by, bh = int(h * 0.545), 74
    bw = int(d.textlength(copy["command"], font=font("mono", 34))) + 64
    d.rectangle([x, by, x + bw, by + bh], fill=rgb("af-paper-sunk"), outline=rgb("af-rule"), width=1)
    d.rectangle([x, by, x + 4, by + bh], fill=rgb("af-signal"))
    d.text((x + 36, by + 20), copy["command"], font=font("mono", 34), fill=rgb("af-ink"))

    for i, line in enumerate(copy["meta"].split("\n")):
        f_meta = font("mono", 26)
        d.text((w - 76 - d.textlength(line, font=f_meta), int(h * 0.085) + i * 38),
               line, font=f_meta, fill=rgb("af-ink-soft"))

    # Measure caption: a rule, then value over monospace label (design system §6).
    ry = int(h * 0.825)
    d.line([(x, ry), (w - 76, ry)], fill=rgb("af-rule"), width=1)
    step = (w - 76 - x) // len(copy["stats"])
    for i, (value, label) in enumerate(copy["stats"]):
        cx = x + i * step
        d.text((cx, ry + 24), value, font=font("bold", 42), fill=rgb("af-ink"))
        d.text((cx, ry + 82), label, font=font("mono", 26), fill=rgb("af-ink-soft"))

    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "PNG", optimize=True)


# 2560×1280 is the 2× asset for a 1280×640 share card. banner.png keeps its historical name — it is
# what README.md has always pointed at — but it is now the English card, rendered from these tokens
# like everything else, rather than the hand-made image that still carried the pre-rename title.
TARGETS = [
    ("fr", (2560, 1280), ASSETS / "social-card.png"),
    ("en", (2560, 1280), ASSETS / "banner.png"),
]


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12] if p.is_file() else "absent"


def main() -> int:
    ap = argparse.ArgumentParser(description="Render the brand images from the design tokens.")
    ap.add_argument("--check", action="store_true", help="fail if what is on disk differs from a fresh render")
    args = ap.parse_args()

    stale: list[str] = []
    for lang, size, out in TARGETS:
        before = digest(out)
        target = out if not args.check else Path(
            subprocess.run(["mktemp", "--suffix=.png"], capture_output=True, text=True, check=True).stdout.strip())
        render(lang, size, target)
        after = digest(target)
        rel = out.relative_to(ROOT)
        if args.check:
            target.unlink(missing_ok=True)
            if before != after:
                stale.append(f"{rel} (on disk {before}, fresh render {after})")
            else:
                print(f"✓ {rel} up to date")
        else:
            kb = round(out.stat().st_size / 1024, 1)
            print(f"✓ {rel}  {size[0]}×{size[1]}  {kb} KB")

    if stale:
        print(f"✗ {len(stale)} brand image(s) out of date — run python3 tools/render_brand_assets.py")
        for s in stale:
            print("   -", s)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
