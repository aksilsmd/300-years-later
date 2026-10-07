import { useRef } from "react";
import { motion, useMotionValueEvent, useReducedMotion, useScroll, useTransform } from "framer-motion";
import type { Era } from "../App";
import { ERA_NAMES, type Content, type Lang } from "../content";
import type { EraFrames } from "../media";

type Props = { frames: EraFrames; lang: Lang; t: Content; setEra: (e: Era) => void };

// Scroll-scrubbed sequence: the same hill (shots L01–L04, identical framing) cross-fades
// through the 4 eras on a sticky stage while a year counter runs 0 → 900.
// Reduced motion: a plain list of the 4 frames, no scrubbing.
export function EraSequence({ frames, lang, t, setEra }: Props) {
  const reduce = useReducedMotion();
  const track = useRef<HTMLElement>(null);
  const { scrollYProgress } = useScroll({ target: track, offset: ["start start", "end end"] });

  // 4 frames over progress 0..1: each fades in over the previous one.
  const o1 = useTransform(scrollYProgress, [0.2, 0.33], [0, 1]);
  const o2 = useTransform(scrollYProgress, [0.45, 0.58], [0, 1]);
  const o3 = useTransform(scrollYProgress, [0.7, 0.83], [0, 1]);
  const scale = useTransform(scrollYProgress, [0, 1], [1.08, 1]);
  const year = useTransform(scrollYProgress, [0, 0.27, 0.52, 0.77, 1], [0, 300, 600, 900, 900]);
  const yearText = useTransform(year, (v: number) => String(Math.round(v / 10) * 10));
  const opacities = [null, o1, o2, o3];

  useMotionValueEvent(scrollYProgress, "change", (p: number) => {
    setEra((p < 0.27 ? 0 : p < 0.52 ? 1 : p < 0.77 ? 2 : 3) as Era);
  });

  if (reduce) {
    return (
      <section className="era-static" aria-labelledby="eraseq-title">
        <h2 id="eraseq-title">{t.eraSeqTitle}</h2>
        <ol>
          {frames.map((f, i) => (
            <li key={f.id}><img src={f.src} alt={f.alt[lang]} loading="lazy" decoding="async" /><p>{ERA_NAMES[lang][i]}</p></li>
          ))}
        </ol>
      </section>
    );
  }

  return (
    <section ref={track} className="era-seq" aria-labelledby="eraseq-title">
      <div className="era-stage">
        {frames.map((f, i) => (
          <motion.img key={f.id} className="era-frame" src={f.src} alt={f.alt[lang]}
            loading={i === 0 ? "eager" : "lazy"} decoding="async"
            style={{ opacity: opacities[i] ?? 1, scale }} />
        ))}
        <div className="era-overlay">
          <h2 id="eraseq-title">{t.eraSeqTitle}</h2>
          <p className="era-year" aria-hidden="true">
            <span>{t.yearPrefix}</span> <motion.span>{yearText}</motion.span>
          </p>
          <p className="era-hint">{t.eraSeqHint}</p>
        </div>
        <span className="rendered-label">{t.renderedLabel}</span>
      </div>
    </section>
  );
}
