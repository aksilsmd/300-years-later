// Médias affichés par la galerie et le héros.
// RÈGLE : n'ajouter ici que des rendus du moteur listés « validé » dans media/APPROVALS.md,
// copiés dans public/media/. Tant que la liste est vide, la galerie et la vidéo ne s'affichent pas.
export type Media = { id: string; src: string; alt: { fr: string; en: string }; kind: "image" | "video" };

export const GALLERY: Media[] = [];
export const HERO_VIDEO: Media | null = null; // ex. { id: "trailer", src: "media/trailer_loop.mp4", kind: "video", alt: {...} }
