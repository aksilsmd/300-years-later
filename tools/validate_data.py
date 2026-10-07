#!/usr/bin/env python3
"""Valide les données de jeu (data/) : schéma des recettes, unicité des id,
cohérence recettes ↔ Chronique, placeholders FR/EN identiques, contrats.

Fonctionne sans dépendance (validation minimale intégrée) ; utilise
`jsonschema` si installé pour une validation complète.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SLOT = re.compile(r"\{(\w+)\}")


def load(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"JSON invalide : {p.relative_to(ROOT)} — {e}")


def minimal_recipe_check(r: dict) -> list[str]:
    errs = []
    for k in ("id", "input", "conditions", "outputs"):
        if k not in r:
            errs.append(f"champ manquant « {k} »")
    if not re.fullmatch(r"[a-z0-9_]{2,40}", str(r.get("id", ""))):
        errs.append("id invalide")
    for hop, variants in r.get("outputs", {}).items():
        if hop not in {"1", "2", "3"}:
            errs.append(f"saut invalide {hop}")
        for v in variants:
            if "type" not in v or "weight" not in v:
                errs.append(f"variante incomplète au saut {hop}")
    return errs


def main() -> int:
    errors: list[str] = []
    schema = load(DATA / "schemas" / "recipe.schema.json")
    try:
        from jsonschema import Draft202012Validator  # type: ignore
        validator = Draft202012Validator(schema)
        full = True
    except ImportError:
        validator, full = None, False

    phrases = load(DATA / "phrases" / "chronicle_fr_en.json")
    allowed = set(phrases["slots_allowed"])
    keys = set()
    for t in phrases["templates"]:
        keys.add(t["key"])
        if len(t["fr"]) != len(t["en"]):
            errors.append(f"{t['key']}: nombre de variantes FR/EN différent")
        for fr, en in zip(t["fr"], t["en"]):
            a, b = set(SLOT.findall(fr)), set(SLOT.findall(en))
            if a != b:
                errors.append(f"{t['key']}: placeholders FR {sorted(a)} ≠ EN {sorted(b)}")
            if not a <= allowed:
                errors.append(f"{t['key']}: placeholder non autorisé {sorted(a - allowed)}")
    keys |= set(phrases.get("finals", {}).keys())

    ids: set[str] = set()
    count = 0
    for f in sorted((DATA / "recipes").glob("*.json")):
        for r in load(f):
            count += 1
            rid = r.get("id", "?")
            errs = [e.message for e in validator.iter_errors(r)] if validator else minimal_recipe_check(r)
            errors += [f"{f.name}/{rid}: {e}" for e in errs]
            if rid in ids:
                errors.append(f"{f.name}/{rid}: id dupliqué")
            ids.add(rid)
            if r.get("chronicle") and r["chronicle"] not in keys:
                errors.append(f"{f.name}/{rid}: modèle de Chronique inconnu {r['chronicle']}")

    contract_ids: set[str] = set()
    for f in sorted((DATA / "contracts").glob("*.json")):
        for c in load(f):
            for k in ("id", "chapter", "main", "text"):
                if k not in c:
                    errors.append(f"{f.name}/{c.get('id', '?')}: champ manquant « {k} »")
            if c.get("id") in contract_ids:
                errors.append(f"{f.name}/{c['id']}: id dupliqué")
            contract_ids.add(c.get("id"))

    load(DATA / "tuning.json")

    mode = "jsonschema complet" if full else "validation minimale (installez jsonschema pour la complète)"
    print(f"[validate_data] {count} recettes, {len(contract_ids)} contrats, {len(keys)} modèles — {mode}")
    for e in errors:
        print("  ✗", e)
    print("  ✓ données valides" if not errors else f"  {len(errors)} erreur(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
