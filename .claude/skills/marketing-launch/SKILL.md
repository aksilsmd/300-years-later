---
name: marketing-launch
description: Launch and marketing like a major publisher — game visuals and trailers rendered INSIDE Unreal Engine (Movie Render Graph, Sequencer, high-res shots) from data/shotlist.json, Remotion titling, a modern cinematic landing page (React + Vite + TypeScript + Framer Motion, scroll-driven era sequence, video hero) with zero trackers, Robot Framework / Lighthouse / k6 tests, presskit, Steam page and creator plan. Use for "landing page", "trailer", "video", "screenshots", "marketing", "launch", "lancement", "vidéo".
---

# Skill: marketing-launch

> **FR —** Lancement et marketing : rendus et trailers faits dans Unreal, landing page moderne et cinématique (React + Framer Motion), presskit, page Steam. Aucune image générée ni trompeuse. Répond dans la langue de l'utilisateur ; tous les textes publics existent en FR et en EN.

## 0. Honesty and safety rules (never bypassed)
- **Every game image and video is rendered in Unreal Engine** from `docs/design/33_VISUAL_TARGETS.md` and `data/shotlist.json`. No generative-AI images, no misleading edits, no cinematic presented as gameplay ("Pre-rendered in engine" label on non-gameplay shots).
- Until approved renders exist, the landing page shows **no game image**: it runs in *typographic mode* (type, colour, motion). It switches to *cinematic mode* automatically when media are approved (§3.3).
- Every published media file is listed in `media/APPROVALS.md` with a human approval. You may add rows with status `pending`; only the human sets `approved`.
- Zero tracker, cookie, CDN or third-party font; fonts and media self-hosted; `python3 tools/privacy_scan.py` green.
- Public copy, price and date: you propose (FR + EN), the human validates. Publishing and deployment: the human (hard stop).

## 1. Rendering from the engine
1. Open the map of each shot, apply its era (Level Instance + lighting preset).
2. Place a `CineCameraActor` from the shot's `camera` block (position, target, focal length, aperture) through the Epic MCP plugin or `game/Scripts/render_shots.py`.
3. **Stills:** Movie Render Graph single frame (or `HighResShot`) at 3840×2160, EXR 16-bit → PNG/AVIF/WebP.
4. **Sequences:** Level Sequence + Movie Render Graph (temporal AA 16 samples, motion blur, 24 fps) → image sequence → `ffmpeg` to H.264 MP4 + VP9/AV1 WebM, plus a poster frame.
5. Automatic check (resolution, NaN pixels, metadata stripped with `exiftool -all=`), then add a `pending` row in `media/APPROVALS.md`.
6. Landing shots **L01–L04** (`data/shotlist.json`): the *same* hill and camera rendered in the 4 eras, identical framing, so the landing can cross-fade between them. Also render `L00` (6–10 s seamless loop for the hero).
7. Vertical 9:16 versions (S12) respecting TikTok/Shorts safe zones.

## 2. Trailers
| Trailer | Content | Tools |
|---|---|---|
| Announcement 60 s | storyboard `docs/design/70` §4 | Sequencer + Movie Render Graph, Remotion titling |
| Gameplay 90 s | real played sequences, HUD visible | in-game capture (human OBS capture if needed) |
| Vertical teaser 15 s | S02 → S03 → logo | Remotion `TrailerVertical` on the renders |

`marketing/video/` (Remotion) assembles **approved** renders only, adds titles, FR/EN subtitles and the composer's music: `npm ci && npx remotion render Trailer out/trailer.mp4`. Missing shots show an explicit "shot to render in Unreal" card — never a substitute image. Check the Remotion licence tier (company licence above its size threshold) → human decision.

## 3. Landing page

### 3.1 Design quality (mandatory)
Before writing or changing any landing UI, **load the `frontend-design` skill** if your environment has it (Claude Code: `/plugin install frontend-design@claude-plugins-official`; other agents: read its SKILL.md if available). Follow `docs/design/34_LANDING_CINEMATIQUE.md` (normative for the landing) and `docs/design/30_ART_BIBLE.md` (palette, type). Target: a modern AAA game site (full-bleed video, bold type, scroll storytelling), not a template.

### 3.2 Stack
- **Production:** `marketing/landing-react/` — React 18, Vite, TypeScript, Framer Motion. Copy in `src/content.ts` (FR + EN), media declared in `src/media.ts`, files in `public/media/`.
- **Reference without dependencies:** `marketing/landing/` (HTML/CSS/JS) — functional mock-up and fallback.

### 3.3 Typographic → cinematic switch
`src/media.ts` is the only switch. It stays empty until media are approved. Then:
1. Copy approved files to `public/media/` (`hero-loop.webm/.mp4`, `hero-poster.avif`, `era-0..3.avif`, gallery stills, trailer).
2. Fill `HERO_VIDEO`, `ERA_FRAMES` (L01–L04) and `GALLERY` in `src/media.ts`, each entry with `approvalId` matching `media/APPROVALS.md`.
3. Components switch on their own: `CinematicHero` (muted looping video, poster first, pause button), `EraSequence` (scroll-scrubbed cross-fade of the 4 era frames with `useScroll`/`useTransform`, sticky stage, year counter), `Gallery`.
4. `python3 tools/check_media_approvals.py` must pass (every referenced file approved).

### 3.4 Requirements
`prefers-reduced-motion` (no scrub, no autoplay: static frames + play button) · mobile (video replaced by poster below 768 px or on Save-Data) · AA contrast · keyboard · `lang` + FR/EN toggle · local Open Graph · JS < 300 kB gz excluding media · hero video < 6 MB · LCP < 2.5 s on 4G · CLS < 0.05 · no cookie.

### 3.5 Tests and deployment
`robot --outputdir results tests/robot` · `python3 -m pytest tests/web` · Lighthouse (≥ 90/95/95/90) · `k6 run tests/load/landing_smoke.js`. Deployment (hard stop, after human approval): `pages.yml` workflow or a European static host.

## 4. Steam page, presskit, launch plan
- `marketing/steam/page.md`, `marketing/presskit/index.md` (fact sheet, FR/EN descriptions, 8 approved renders, logo, trailer, dedicated project contact).
- `marketing/launch-plan.md`: calendar from `docs/design/70` §5, 12 "before/after" clip ideas, creator selection criteria (the human does the outreach; French law 2023-451 on influencer disclosure), Next Fest checklist, KPIs.
- Steam capsules: sizes in `docs/design/30`/`70`; the main capsule is commissioned to an illustrator or composed from approved render S01.
- Steam AI disclosure: answer from `legal/steam-content-survey.md`.
