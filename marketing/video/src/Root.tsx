import { Composition, registerRoot } from "remotion";
import { Trailer } from "./Trailer";
import { TRAILER, VERTICAL, FPS, totalFrames } from "./storyboard";

// Liste des rendus présents, tenue à jour par marketing-launch (fichiers de public/renders validés).
// Exemple : ["S01.png", "S02.mp4"]
const AVAILABLE: string[] = [];

function Root() {
  return (
    <>
      <Composition id="Trailer" component={Trailer} durationInFrames={totalFrames(TRAILER)} fps={FPS} width={3840} height={2160}
        defaultProps={{ segments: TRAILER, lang: "fr" as const, available: AVAILABLE }} />
      <Composition id="TrailerEN" component={Trailer} durationInFrames={totalFrames(TRAILER)} fps={FPS} width={3840} height={2160}
        defaultProps={{ segments: TRAILER, lang: "en" as const, available: AVAILABLE }} />
      <Composition id="TrailerVertical" component={Trailer} durationInFrames={totalFrames(VERTICAL)} fps={FPS} width={1080} height={1920}
        defaultProps={{ segments: VERTICAL, lang: "fr" as const, available: AVAILABLE }} />
    </>
  );
}

registerRoot(Root);
