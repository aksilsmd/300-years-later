import type { Content } from "../content";
import { STEAM_URL } from "../content";

function Final({ t }: { t: Content }) {
  return (
    <section className="final" id="final" aria-labelledby="final-title">
      <h2 id="final-title">{t.finalTitle}</h2>
      {STEAM_URL ? (
        <a className="btn" href={STEAM_URL} rel="noopener">{t.cta}</a>
      ) : (
        <>
          <a className="btn" href="#final" aria-describedby="steam-note">{t.cta}</a>
          <p id="steam-note" className="note">{t.steamNote}</p>
        </>
      )}
    </section>
  );
}

function Bottom({ t }: { t: Content }) {
  return (
    <footer className="foot">
      <p>{t.foot1}</p>
      <nav aria-label="Legal">
        {t.footLinks.map(([href, label]) => <a key={href} href={href}>{label}</a>)}
      </nav>
      <p className="small">{t.foot2}</p>
    </footer>
  );
}

export const Footer = { Final, Bottom };
