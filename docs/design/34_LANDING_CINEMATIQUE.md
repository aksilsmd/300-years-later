# 34 — Cinematic landing page / Landing page cinématique

> **FR —** Cahier normatif de la landing page. Elle fonctionne en deux modes : **typographique** (aujourd'hui, aucune image de jeu) puis **cinématique** dès que des rendus Unreal sont validés dans `media/APPROVALS.md`. Le basculement est automatique : il suffit de remplir `marketing/landing-react/src/media.ts`. Aucune image générée par IA, aucun faux gameplay.
>
> **EN —** Normative spec for the landing page. Two modes: **typographic** (now, no game image) then **cinematic** as soon as Unreal renders are approved in `media/APPROVALS.md`. The switch is automatic: fill `marketing/landing-react/src/media.ts`. No AI-generated image, no fake gameplay.

Owner skill: `marketing-launch` (+ `frontend-design` loaded before any UI work). Related: `30_ART_BIBLE.md`, `33_VISUAL_TARGETS.md`, `70_MARKETING_GTM.md`, `data/shotlist.json` (L00–L04).

## 1. Intent
A visitor understands the whole game in 10 seconds without reading: **the same hill, four centuries; what you leave behind grows old.** The page itself ages as you scroll (colour, type, imagery move from dawn to neon). Reference level: modern AAA game sites — full-bleed video hero, huge type, scroll storytelling, very little text.

## 2. Page structure
| # | Section | Typographic mode (now) | Cinematic mode (approved renders) |
|---|---|---|---|
| 1 | Hero | animated year counter 0 → 900 → 0, era colours | `CinematicHero`: L00 muted 8 s seamless loop, poster first, title over a dark scrim, pause button |
| 2 | Era sequence | — (hidden) | `EraSequence`: sticky stage, L01→L04 cross-fade scrubbed by scroll (400 svh), year counter, slow 1.08 → 1 scale |
| 3 | The rule (strata) | 4 strata of text, page colour follows era | unchanged (text explains what the images showed) |
| 4 | Co-op | text | text |
| 5 | Ledger ("what you leave") | animated table | unchanged |
| 6 | Museum | quote | + S10 still |
| 7 | Gallery | hidden | S04–S11 stills and clips, staggered reveal, clips play on demand |
| 8 | Modes, FAQ | text | text |
| 9 | Final CTA + legal footer | Steam button (disabled until `STEAM_URL`) | + trailer (click to play, never autoplay with sound) |

## 3. Motion system (Framer Motion)
- One orchestrated moment per screen; everything else is subtle (opacity + 24 px rise, 600 ms, `ease [0.22, 1, 0.36, 1]`).
- Scroll-driven: `useScroll({ target, offset: ["start start", "end end"] })` + `useTransform`; era thresholds 0.27 / 0.52 / 0.77 also drive `html[data-era]` (page palette).
- Only `opacity` and `transform` are animated (GPU-friendly). No scroll-jacking: native scroll is never blocked.
- View Transitions API (optional): FR ↔ EN switch cross-fade where supported.
- Light parallax on the hero title (≤ 40 px) disabled under 768 px.

## 4. Media specs (all rendered in Unreal Engine — `data/shotlist.json`)
| ID | Use | Delivery | Budget |
|---|---|---|---|
| L00 | hero loop | 2560×1440 → MP4 H.264 (CRF 23) + WebM VP9 (CRF 34) + AVIF poster (first frame) | ≤ 6 MB video, ≤ 200 kB poster |
| L01–L04 | era sequence | 2560×1440 AVIF q60 + WebP fallback, **identical camera** | ≤ 450 kB each |
| S04–S11 | gallery | 1920×1080 AVIF/WebP + 1280 px variant (`srcset`) | ≤ 300 kB each |
| Trailer | final CTA | MP4 1080p, captions FR/EN (`.vtt`) | streamed, `preload="none"` |

Every file: metadata stripped, row in `media/APPROVALS.md` (status approved), checked by `python3 tools/check_media_approvals.py`. Non-gameplay shots carry the label "Rendered in the game engine / Rendu dans le moteur du jeu".

## 5. Fallbacks and accessibility
- `prefers-reduced-motion`: no autoplay, no scrub — the 4 era frames appear as a static list; year counter static.
- Mobile < 768 px or Save-Data / 2G-3G: poster image instead of the video.
- Video: muted, `playsInline`, pause control always visible (WCAG 2.2.2), no flashing > 3 Hz.
- AA contrast on every era palette and over video (scrim ≥ 55 % black at the text zone). Keyboard navigable, visible focus, `lang` updated on switch, skip link.
- No JavaScript: the vanilla reference `marketing/landing/` remains readable.

## 6. Performance budgets (CI-enforced)
LCP < 2.5 s on 4G (poster is the LCP element, `fetchpriority="high"`) · CLS < 0.05 · INP < 200 ms · JS < 300 kB gzip excluding media · Lighthouse ≥ 90 perf / 95 a11y / 95 best practices / 90 SEO · k6 p95 < 500 ms.

## 7. Privacy and law
Self-hosted fonts and media, no cookie, no analytics, no external embed (YouTube trailer = link only, never an iframe). Legal footer links to `legal/` pages; `/.well-known/security.txt`. Loi Toubon: French version complete.

## 8. Switch procedure (typographic → cinematic)
1. Render L00–L04 (and gallery shots) in Unreal following `marketing-launch` §1.
2. Human sets `approved` in `media/APPROVALS.md` (hard stop for publication).
3. Copy files to `marketing/landing-react/public/media/`; fill `HERO_VIDEO`, `ERA_FRAMES`, `GALLERY` in `src/media.ts`.
4. `python3 tools/check_media_approvals.py && npm run build && robot tests/robot && python3 -m pytest tests/web` then Lighthouse.
5. Visual review on desktop, mobile, reduced motion; human approves deployment.

## 9. Acceptance criteria
- [ ] Both modes build and pass tests; with `media.ts` empty, **no** `<img>`/`<video>` of game content is in the DOM.
- [ ] Cinematic mode: L01–L04 align pixel-perfect (same camera), scrub smooth at 60 fps on a mid-range laptop.
- [ ] All budgets of §6 met; reduced-motion and mobile fallbacks verified by screenshots.
- [ ] Every media file approved; label shown on pre-rendered shots.
