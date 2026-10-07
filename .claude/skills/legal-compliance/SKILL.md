---
name: legal-compliance
description: Maintains the project's complete legal pack (legal/) — terms/EULA, privacy policy, DPIA, processing register, cookies, legal notice, DSA and moderation, minors (GDPR/COPPA/UK Children's Code), virtual currencies (EU CPC 2025 principles), accessibility (EAA), creators, playtests, freelance contracts, security disclosure, AI transparency, ethics, age rating, tax and Unreal royalties, trademark, Epic/Fab/MetaHuman licences. Produces drafts for professional review. Use in phase P7, before any release, or for "legal", "GDPR", "licence", "trademark", "RGPD", "juridique".
---

# Skill: legal-compliance

> **FR —** Tient à jour le corpus juridique `legal/` (brouillons à faire valider par un professionnel). Répond dans la langue de l'utilisateur ; les documents juridiques restent en français et en anglais.

**You are not a lawyer. Every document keeps the header "DRAFT — to be validated by a legal professional / BROUILLON — à faire valider par un professionnel du droit".**

## Sources of truth
`legal/README.md` (index + obligations matrix), `docs/design/60_LEGAL_COMPLIANCE.md`, `PRIVACY.md`, `SECURITY.md`.

## Work
1. Update each document from the **actual code**: processing really present, durations, processors, accessibility options really shipped.
2. Fill `[…]` fields only with information **given by the human**; never invent identity, address or numbers. In autonomous mode, list missing fields in `QUESTIONS.md` and keep going.
3. Never put the human's personal contact details in the public repo: use a dedicated project address.
4. Produce `legal/steam-content-survey.md` (proposed answers incl. AI section), `legal/trademark-check.md` (results entered by the human), English versions of the player-facing documents (01, 03, 04, 05, 08, 09, 12, 13) in `legal/en/`.
5. Prepare `legal/REVIEW_PACKET.md` for the lawyer: documents, open questions (DSA and EAA applicability, DPIA, assignments), changes since last review. Lawyer review is queued, non-blocking for development, **blocking for public release**.
6. After validation: integrate texts in the game (Privacy menu, Credits, Terms at first online launch) and on the landing page (footer, `/.well-known/security.txt`).

## Checks required from game-qa
Telemetry no-op without consent; voice never written; capsules without personal data; friends-only default; reporting tools reachable; no real-money purchase or paid currency; no tracker or external resource on the landing; no Epic/Fab/MetaHuman asset in the public repo.

## Always escalate to the human (never decide alone)
Employment contract constraints; company structure; Fab/Remotion licence tier; Unreal royalty thresholds; age rating; DSA/EAA applicability; consumer mediator.
