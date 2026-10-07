# marketing/

**EN —** Which file is the reference, which is production, and what must never diverge.
**FR —** Quel fichier fait référence, lequel est en production, et ce qui ne doit jamais diverger.

| Folder | Role | Status |
|---|---|---|
| `landing-react/` | **Production landing page.** React 19 · Vite 8 · TypeScript · Framer Motion 13. Cinematic mode (video hero + scroll-driven era sequence) switches on by itself once `src/media.ts` holds approved renders. Spec: [`docs/design/34_LANDING_CINEMATIQUE.md`](../docs/design/34_LANDING_CINEMATIQUE.md). | the one that gets deployed |
| `landing/` | **Reference build, no dependencies.** Plain HTML/CSS/JS. It is the fallback that works without Node, the target of the Playwright, Robot Framework and OWASP ZAP tests, and the page screenshotted in the PDF guides. | must stay functional |
| `video/` | Remotion project: titles, subtitles and assembly over **approved Unreal renders only** (`media/APPROVALS.md`). Never a substitute image. | tooling |
| `steam/`, `presskit/`, `launch-plan.md` | Store page copy, press kit, launch calendar. Public copy is proposed by the AI and approved by the human. | drafts |

## Reproducibility / Reproductibilité
Dependencies are declared as **exact versions**, not ranges: without a committed `package-lock.json`, a range
resolves differently on every machine and on every CI run. The lockfiles are the real fix and are generated the
first time someone runs `npm install` with network access — commit them, and CI switches to `npm ci` on its own
(the workflow already tests for them). Exact versions must point at a **current** release: pinning `4.0.0` when the
project is at `4.0.534` pins three years of missing fixes.

## The rule about divergence
The two landings share **content and structure**, not code. When the copy, the sections or the legal links change,
**both** are updated in the same commit. The React one may have motion the reference one does not; the reference one
must never be missing a section, a legal link or a language the React one has. CI tests the reference build, so a
section that only exists in React is a section nobody tests.

## Never, on either landing
No tracker, cookie, analytics, external CDN or third-party font. No game image that is not an approved in-engine
render (`python3 tools/check_media_approvals.py` enforces it). No YouTube or social embed — links only.
