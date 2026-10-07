import { useEffect, useRef, useState } from "react";
import { animate, motion, useReducedMotion } from "framer-motion";
import type { Era } from "../App";
import { ERA_NAMES, type Content, type Lang } from "../content";
import { HERO_VIDEO } from "../media";
import { CinematicHero } from "./CinematicHero";

type Props = { lang: Lang; t: Content; era: Era; setEra: (e: Era) => void };

const wait = (ms: number) => new Promise((r) => setTimeout(r, ms));

// Moment orchestré unique de la page : les siècles défilent (0 → 900) puis reviennent à l'an 0.
export function Hero({ lang, t, era, setEra }: Props) {
  const reduce = useReducedMotion();
  const [year, setYear] = useState(0);
  const yearRef = useRef(0);
  yearRef.current = year;

  useEffect(() => {
    if (reduce) return;
    let cancelled = false;
    const countTo = (to: number, duration: number) =>
      new Promise<void>((resolve) => {
        const controls = animate(yearRef.current, to, {
          duration, ease: [0.22, 1, 0.36, 1],
          onUpdate: (v: number) => !cancelled && setYear(Math.round(v)),
          onComplete: () => resolve(),
        });
        if (cancelled) controls.stop();
      });
    (async () => {
      await wait(700);
      for (const e of [1, 2, 3] as const) {
        if (cancelled) return;
        setEra(e);
        await countTo(e * 300, 0.9);
        await wait(450);
      }
      await wait(900);
      if (cancelled) return;
      setEra(0);
      await countTo(0, 1.1);
    })();
    return () => { cancelled = true; };
  }, [reduce, setEra]);

  return (
    <section className={HERO_VIDEO ? "hero hero--cine" : "hero"} aria-labelledby="hero-title">
      {HERO_VIDEO && <CinematicHero video={HERO_VIDEO} lang={lang} t={t} />}
      <p className="hero-era" aria-live="polite">{ERA_NAMES[lang][era]}</p>
      <h1 id="hero-title" className="year" aria-label={lang === "fr" ? "An 0 à an 900" : "Year 0 to year 900"}>
        <span className="year-prefix">{t.yearPrefix}</span>
        <span className="year-num">{year}</span>
      </h1>
      <motion.p className="hero-line" initial={reduce ? false : { opacity: 0 }} animate={{ opacity: 1 }} transition={{ delay: 0.3, duration: 0.8 }}>
        {t.heroLine}
      </motion.p>
      <p className="hero-sub">{t.heroSub}</p>
      <div className="hero-actions">
        <a className="btn" href="#final">{t.cta}</a>
        <a className="link" href="#regle">{t.howLink}</a>
      </div>
    </section>
  );
}
