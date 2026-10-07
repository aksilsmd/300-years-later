// EN — The ONLY switch between typographic mode and cinematic mode (docs/design/34_LANDING_CINEMATIQUE.md).
//      Add entries only for Unreal Engine renders marked "approved/validé" in media/APPROVALS.md,
//      copied into public/media/. Check with: python3 tools/check_media_approvals.py
// FR — SEUL interrupteur entre mode typographique et mode cinématique. N'ajouter que des rendus du
//      moteur « validés » dans media/APPROVALS.md, copiés dans public/media/.
export type Alt = { fr: string; en: string };
export type Media = { id: string; approvalId: string; src: string; alt: Alt; kind: "image" | "video"; poster?: string };
export type HeroVideo = { approvalId: string; webm?: string; mp4: string; poster: string; alt: Alt };
export type EraFrames = [Media, Media, Media, Media];

/** Gallery stills / clips (S04–S11). Empty = section hidden. */
export const GALLERY: Media[] = [];

/** Hero loop (shot L00). null = animated typographic hero.
 *  Example: { approvalId: "L00", webm: "media/hero-loop.webm", mp4: "media/hero-loop.mp4",
 *             poster: "media/hero-poster.avif", alt: { fr: "…", en: "…" } } */
export const HERO_VIDEO: HeroVideo | null = null;

/** Same hill in the 4 eras (shots L01–L04), identical framing. null = typographic strata only. */
export const ERA_FRAMES: EraFrames | null = null;

export const isCinematic = (): boolean => HERO_VIDEO !== null || ERA_FRAMES !== null;
