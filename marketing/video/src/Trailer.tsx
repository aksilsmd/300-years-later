import { AbsoluteFill, Img, OffthreadVideo, Sequence, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { ERA_COLORS, ERA_INK, FPS, type Segment } from "./storyboard";

type Props = { segments: Segment[]; lang: "fr" | "en"; available: string[] };

// Carton affiché quand un rendu validé n'existe pas encore : il le dit explicitement,
// pour qu'aucune version provisoire ne puisse être prise pour une image du jeu.
function MissingShot({ seg }: { seg: Segment }) {
  return (
    <AbsoluteFill style={{ background: ERA_COLORS[seg.era], color: ERA_INK[seg.era], justifyContent: "center", alignItems: "center", fontFamily: "Georgia, serif" }}>
      <div style={{ fontSize: 64, fontWeight: 700 }}>Plan {seg.shot} à rendre dans Unreal</div>
      <div style={{ fontSize: 32, marginTop: 16 }}>voir data/shotlist.json</div>
    </AbsoluteFill>
  );
}

function Title({ lang }: { lang: "fr" | "en" }) {
  const frame = useCurrentFrame();
  const o = interpolate(frame, [0, 18], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ background: "#0d1030", color: "#e9e6ff", justifyContent: "center", alignItems: "center", fontFamily: "Georgia, serif", opacity: o }}>
      <div style={{ fontSize: 150, fontWeight: 800, letterSpacing: -4 }}>300 Years Later</div>
      <div style={{ fontSize: 44, marginTop: 24 }}>{lang === "fr" ? "Ajoutez-le à votre liste de souhaits" : "Wishlist it now"}</div>
    </AbsoluteFill>
  );
}

function Caption({ text }: { text: string }) {
  const frame = useCurrentFrame();
  const { height } = useVideoConfig();
  const o = interpolate(frame, [0, 8, 50, 60], [0, 1, 1, 0], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: height * 0.12, opacity: o }}>
      <div style={{ fontFamily: "Georgia, serif", fontSize: height * 0.055, color: "#fff", textShadow: "0 2px 18px rgba(0,0,0,.65)", textAlign: "center", maxWidth: "80%" }}>{text}</div>
    </AbsoluteFill>
  );
}

export function Trailer({ segments, lang, available }: Props) {
  let from = 0;
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      {segments.map((seg) => {
        const dur = Math.round(seg.seconds * FPS);
        const start = from;
        from += dur;
        const has = seg.file && available.includes(seg.file);
        return (
          <Sequence key={seg.shot + start} from={start} durationInFrames={dur}>
            {seg.shot === "TITLE" ? <Title lang={lang} /> :
              has ? (seg.file!.endsWith(".mp4")
                ? <OffthreadVideo src={staticFile(`renders/${seg.file}`)} muted />
                : <Img src={staticFile(`renders/${seg.file}`)} style={{ width: "100%", height: "100%", objectFit: "cover" }} />)
              : <MissingShot seg={seg} />}
            {seg.text && <Caption text={seg.text[lang]} />}
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
}
