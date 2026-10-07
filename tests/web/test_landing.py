"""Tests de la landing de référence avec Playwright (Python). Équivalent rapide des tests Robot.

    python3 -m pytest tests/web -q
"""
from __future__ import annotations

from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[2]
URL = (ROOT / "marketing" / "landing" / "index.html").as_uri()


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        b = p.chromium.launch()
        yield b
        b.close()


def open_page(browser, **ctx):
    context = browser.new_context(**ctx)
    page = context.new_page()
    external: list[str] = []
    errors: list[str] = []
    page.on("request", lambda r: external.append(r.url) if not r.url.startswith(("file:", "data:")) else None)
    page.on("pageerror", lambda e: errors.append(str(e)))
    page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
    page.goto(URL)
    return page, external, errors


def test_titre_et_cta(browser):
    page, external, errors = open_page(browser)
    assert "Afterloom" in page.title()
    assert page.locator(".hero .btn").inner_text() == "Ajouter à ma liste de souhaits"
    assert external == [] and errors == []


def test_bascule_anglais(browser):
    page, _, _ = open_page(browser)
    page.click(".lang button[data-lang=en]")
    assert page.locator(".hero .btn").inner_text() == "Add to my wishlist"
    assert page.evaluate("document.documentElement.lang") == "en"


def test_mouvement_reduit(browser):
    page, _, _ = open_page(browser, reduced_motion="reduce")
    page.wait_for_timeout(1500)
    assert page.locator("#year-num").inner_text() == "0"


def test_strates_changent_epoque(browser):
    page, _, _ = open_page(browser, viewport={"width": 1280, "height": 800})
    page.wait_for_timeout(7000)  # fin de l'animation d'introduction
    for i in range(4):
        page.evaluate("i=>{const el=document.querySelector(`.layer[data-era='${i}']`);const r=el.getBoundingClientRect();"
                      "window.scrollTo(0,window.scrollY+r.top+r.height/2-window.innerHeight/2)}", i)
        page.wait_for_timeout(600)
        assert page.evaluate("document.documentElement.dataset.era") == str(i)


def test_aucun_cookie_ni_stockage(browser):
    page, _, _ = open_page(browser)
    assert page.context.cookies() == []
    assert page.evaluate("localStorage.length + sessionStorage.length") == 0


def test_lien_evitement_clavier(browser):
    page, _, _ = open_page(browser)
    page.keyboard.press("Tab")
    assert page.evaluate("document.activeElement.className") == "skip"


def test_liens_legaux_valides(browser):
    page, _, _ = open_page(browser)
    for href in page.eval_on_selector_all(".foot nav a", "els => els.map(e => e.getAttribute('href'))"):
        assert (ROOT / "marketing" / "landing" / href).is_file(), href
