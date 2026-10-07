import type { Content, Lang } from "../content";
import { GALLERY } from "../media";

// Ne s'affiche que lorsque des rendus validés existent (voir src/media.ts).
export function Gallery({ lang, t }: { lang: Lang; t: Content }) {
  if (GALLERY.length === 0) return null;
  return (
    <section className="gallery" aria-labelledby="gallery-title">
      <h2 id="gallery-title">{t.galleryTitle}</h2>
      <ul className="gallery-grid">
        {GALLERY.map((m) => (
          <li key={m.id}>
            {m.kind === "image"
              ? <img src={m.src} alt={m.alt[lang]} loading="lazy" decoding="async" />
              : <video src={m.src} controls preload="none" aria-label={m.alt[lang]} />}
          </li>
        ))}
      </ul>
    </section>
  );
}
