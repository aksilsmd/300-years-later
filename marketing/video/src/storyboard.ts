// Storyboard du trailer d'annonce (docs/design/70_MARKETING_GTM.md §4) relié aux plans de data/shotlist.json.
// Chaque segment référence un rendu Unreal validé (public/renders/<shot>.<ext>) et un texte facultatif.
export type Segment = {
  shot: string;            // ID de plan (S01…S12)
  file?: string;           // nom de fichier dans public/renders (sinon carton « plan à rendre »)
  seconds: number;
  era: 0 | 1 | 2 | 3;
  text?: { fr: string; en: string };
};

export const FPS = 24;

export const TRAILER: Segment[] = [
  { shot: "S02", file: "S02.mp4", seconds: 3, era: 0, text: { fr: "An 0. Tu plantes une graine.", en: "Year 0. You plant a seed." } },
  { shot: "S03", file: "S03.mp4", seconds: 3, era: 1, text: { fr: "300 ans plus tard.", en: "300 years later." } },
  { shot: "S01", file: "S01.png", seconds: 6, era: 1, text: { fr: "4 amis. 4 siècles. 1 vallée.", en: "4 friends. 4 centuries. 1 valley." } },
  { shot: "S05", file: "S05.png", seconds: 4, era: 1 },
  { shot: "S06", file: "S06.png", seconds: 4, era: 2 },
  { shot: "S07", file: "S07.png", seconds: 4, era: 3 },
  { shot: "S08", file: "S08.mp4", seconds: 5, era: 0 },
  { shot: "S09", file: "S09.png", seconds: 5, era: 3, text: { fr: "Ne contredisez pas le futur.", en: "Don't contradict the future." } },
  { shot: "S10", file: "S10.png", seconds: 12, era: 3, text: { fr: "Et à la fin, le musée raconte… à sa façon.", en: "And in the end, the museum tells it… its own way." } },
  { shot: "TITLE", seconds: 8, era: 0 },
];

export const VERTICAL: Segment[] = [
  { shot: "S12a", file: "S12_S02.mp4", seconds: 4, era: 0, text: { fr: "An 0. Je plante une graine.", en: "Year 0. I plant a seed." } },
  { shot: "S12b", file: "S12_S03.mp4", seconds: 5, era: 1, text: { fr: "Mon pote, 300 ans plus tard :", en: "My friend, 300 years later:" } },
  { shot: "TITLE", seconds: 6, era: 0 },
];

export const ERA_COLORS = ["#f3d9b1", "#e8eef0", "#3b2a22", "#0d1030"] as const;
export const ERA_INK = ["#2a1a0e", "#1d2733", "#f1dccb", "#e9e6ff"] as const;
export const totalFrames = (s: Segment[]) => s.reduce((n, x) => n + Math.round(x.seconds * FPS), 0);
