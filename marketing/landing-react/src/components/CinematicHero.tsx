import { useEffect, useRef, useState } from "react";
import { useReducedMotion } from "framer-motion";
import type { Content, Lang } from "../content";
import type { HeroVideo } from "../media";

type Props = { video: HeroVideo; lang: Lang; t: Content };

// Full-bleed muted loop behind the hero title. Poster first (LCP), video only on
// desktop-class connections, never autoplayed with prefers-reduced-motion. Pause button always present (WCAG 2.2.2).
export function CinematicHero({ video, lang, t }: Props) {
  const reduce = useReducedMotion();
  const ref = useRef<HTMLVideoElement>(null);
  const [allowed, setAllowed] = useState(false);
  const [playing, setPlaying] = useState(false);

  useEffect(() => {
    const nav = navigator as Navigator & { connection?: { saveData?: boolean; effectiveType?: string } };
    const slow = nav.connection?.saveData === true || /(^|-)2g$|3g/.test(nav.connection?.effectiveType ?? "");
    const wide = window.matchMedia("(min-width: 768px)").matches;
    setAllowed(!reduce && !slow && wide);
  }, [reduce]);

  useEffect(() => {
    const el = ref.current;
    if (!el || !allowed) return;
    el.play().then(() => setPlaying(true)).catch(() => setPlaying(false));
  }, [allowed]);

  const toggle = () => {
    const el = ref.current;
    if (!el) return;
    if (el.paused) { el.play().then(() => setPlaying(true)).catch(() => undefined); }
    else { el.pause(); setPlaying(false); }
  };

  return (
    <div className="cine-hero" aria-hidden={false}>
      {allowed ? (
        <video ref={ref} className="cine-hero-media" muted loop playsInline preload="metadata" poster={video.poster} aria-label={video.alt[lang]}>
          {video.webm && <source src={video.webm} type="video/webm" />}
          <source src={video.mp4} type="video/mp4" />
        </video>
      ) : (
        <img className="cine-hero-media" src={video.poster} alt={video.alt[lang]} fetchPriority="high" decoding="async" />
      )}
      <div className="cine-hero-scrim" />
      <span className="rendered-label">{t.renderedLabel}</span>
      {allowed && (
        <button type="button" className="cine-toggle" onClick={toggle} aria-pressed={!playing}>
          {playing ? t.pause : t.play}
        </button>
      )}
    </div>
  );
}
