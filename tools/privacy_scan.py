#!/usr/bin/env python3
"""Scan de confidentialité : bloque la publication de données personnelles,
de secrets et de traceurs. Aucune dépendance externe. Aucun appel réseau.

Usage :
    python3 tools/privacy_scan.py [--denylist CHEMIN] [--staged]

Liste locale de termes interdits (vos nom, e-mail, pseudo, employeur…) :
    ~/.config/300yl/denylist.txt   (un terme par ligne, jamais versionnée)
ou la variable d'environnement PRIVACY_DENYLIST=/chemin/vers/fichier.

Code de sortie : 0 = propre, 1 = problème trouvé.
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SKIP_DIRS = {".git", "node_modules", "dist", ".godot", "build", "__pycache__", "results", ".venv"}
TEXT_EXT = {".md", ".txt", ".json", ".py", ".sh", ".ps1", ".js", ".jsx", ".ts", ".tsx", ".css",
            ".html", ".yml", ".yaml", ".toml", ".cfg", ".gd", ".tscn", ".robot", ".env", ".svg", ".csv", ".po", ".pot"}

# Adresses e-mail tolérées (génériques ou documentaires)
EMAIL_ALLOW = re.compile(r"(@example\.(com|org)|@users\.noreply\.github\.com|noreply@|@anthropic\.com$)", re.I)

PATTERNS: dict[str, re.Pattern[str]] = {
    "e-mail": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"),
    "téléphone FR": re.compile(r"(?<!\d)(?:\+33\s?|0)[1-9](?:[ .-]?\d{2}){4}(?!\d)"),
    "IBAN": re.compile(r"\bFR\d{2}(?:\s?\d{4}){5}\s?\d{3}\b"),
    "jeton GitHub": re.compile(r"\b(ghp|gho|ghu|ghs|ghr|github_pat)_[A-Za-z0-9_]{20,}"),
    "clé AWS": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "clé privée": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY-----"),
    "clé API générique": re.compile(r"\b(sk-[A-Za-z0-9]{20,}|xox[baprs]-[A-Za-z0-9-]{10,})"),
    "SteamID64": re.compile(r"\b7656119\d{10}\b"),
    "traceur": re.compile(r"(googletagmanager|google-analytics|gtag\(|facebook\.net/|connect\.facebook|hotjar|segment\.com|mixpanel|doubleclick|clarity\.ms)", re.I),
    # Une ressource EXTERNE est chargée par le navigateur (script, feuille de style, préchargement).
    # canonical / alternate / hreflang sont des métadonnées de référencement : aucune requête, aucun traceur.
    # An EXTERNAL resource is fetched by the browser; canonical/alternate are SEO metadata, not a request.
    "ressource CDN externe": re.compile(
        r"<script[^>]+src=[\"']https?://(?!store\.steampowered\.com)"
        r"|<link(?![^>]*\brel=[\"'](?:canonical|alternate|me)[\"'])[^>]+href=[\"']https?://(?!store\.steampowered\.com)",
        re.I),
}

# Fichiers qui documentent volontairement les motifs ci-dessus
SELF_DOC = {"tools/privacy_scan.py", "SECURITY.md"}


def load_denylist(path: str | None) -> list[str]:
    candidates = [path, os.environ.get("PRIVACY_DENYLIST"),
                  str(Path.home() / ".config" / "300yl" / "denylist.txt")]
    for c in candidates:
        if c and Path(c).is_file():
            terms = [t.strip() for t in Path(c).read_text(encoding="utf-8").splitlines()]
            return [t for t in terms if t and not t.startswith("#")]
    return []


def files_to_scan(staged: bool) -> list[Path]:
    if staged:
        out = subprocess.run(["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
                             cwd=ROOT, capture_output=True, text=True, check=False).stdout
        return [ROOT / p for p in out.splitlines() if p]
    result = []
    for p in ROOT.rglob("*"):
        if p.is_file() and not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            result.append(p)
    return result


def scan(paths: list[Path], denylist: list[str]) -> list[str]:
    issues: list[str] = []
    deny_re = [re.compile(r"(?<![\w])" + re.escape(t) + r"(?![\w])", re.I) for t in denylist]
    for p in paths:
        rel = p.relative_to(ROOT).as_posix()
        if p.suffix.lower() not in TEXT_EXT and p.name not in {".gitignore", "Makefile"}:
            # fichiers binaires : vérifier seulement le nom et les métadonnées texte des PNG/PDF
            data = p.read_bytes()[:200_000]
            for i, rx in enumerate(deny_re):
                if rx.search(data.decode("latin-1", "ignore")):
                    issues.append(f"{rel}: terme de la liste locale n°{i + 1} trouvé dans un fichier binaire")
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for n, line in enumerate(text.splitlines(), 1):
            for i, rx in enumerate(deny_re):
                if rx.search(line):
                    issues.append(f"{rel}:{n}: terme de la liste locale n°{i + 1}")
            if rel in SELF_DOC:
                continue
            for label, rx in PATTERNS.items():
                for m in rx.finditer(line):
                    if label == "e-mail" and EMAIL_ALLOW.search(m.group(0)):
                        continue
                    issues.append(f"{rel}:{n}: {label} → {m.group(0)[:60]}")
    return issues


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--denylist")
    ap.add_argument("--staged", action="store_true", help="ne scanner que les fichiers indexés (pré-commit)")
    args = ap.parse_args()
    denylist = load_denylist(args.denylist)
    paths = files_to_scan(args.staged)
    issues = scan(paths, denylist)
    print(f"[privacy_scan] {len(paths)} fichiers, {len(denylist)} termes locaux, {len(issues)} problème(s)")
    for i in issues:
        print("  ✗", i)
    if not denylist:
        print("  ℹ Astuce : créez ~/.config/300yl/denylist.txt avec vos nom, e-mail, pseudo, employeur.")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main())
