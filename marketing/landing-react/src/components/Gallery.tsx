import { motion, useReducedMotion } from "framer-motion";
import type { Content, Lang } from "../content";
import { GALLERY } from "../media";

// Shown only when approved renders exist (src/media.ts). Clips play on demand only.
export function Gallery({ lang, t }: { lang: Lang; t: Content }) {
  const reduce = useReducedMotion();
  if (GALLERY.length === 0) return null;
  return (
    <section className="gallery" aria-labelledby="gallery-title">
      <h2 id="gallery-title">{t.galleryTitle}</h2>
      <ul className="gallery-grid">
        {GALLERY.map((m, i) => (
          <motion.li key={m.id}
            initial={reduce ? false : { opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-10%" }}
            transition={{ duration: 0.6, delay: (i % 3) * 0.08 }}>
            {m.kind === "image"
              ? <img src={m.src} alt={m.alt[lang]} loading="lazy" decoding="async" />
              : <video src={m.src} poster={m.poster} controls preload="none" playsInline aria-label={m.alt[lang]} />}
          </motion.li>
        ))}
      </ul>
      <p className="rendered-note">{t.renderedLabel}</p>
    </section>
  );
}
