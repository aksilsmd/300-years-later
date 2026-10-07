import { useEffect, useState } from "react";
import { CONTENT, type Lang } from "./content";
import { Header } from "./components/Header";
import { Hero } from "./components/Hero";
import { Strata } from "./components/Strata";
import { Ledger } from "./components/Ledger";
import { Gallery } from "./components/Gallery";
import { Footer } from "./components/Footer";
import { EraSequence } from "./components/EraSequence";
import { ERA_FRAMES } from "./media";

export type Era = 0 | 1 | 2 | 3;

export default function App() {
  const [lang, setLang] = useState<Lang>("fr");
  const [era, setEra] = useState<Era>(0);
  const t = CONTENT[lang];

  // L'époque pilote les variables CSS de toute la page (styles.css : html[data-era]).
  useEffect(() => { document.documentElement.dataset.era = String(era); }, [era]);
  useEffect(() => { document.documentElement.lang = lang; }, [lang]);

  return (
    <>
      <a className="skip" href="#contenu">{t.skip}</a>
      <Header lang={lang} setLang={setLang} t={t} />
      <main id="contenu">
        <Hero lang={lang} t={t} era={era} setEra={setEra} />
        {ERA_FRAMES && <EraSequence frames={ERA_FRAMES} lang={lang} t={t} setEra={setEra} />}
        <Strata t={t} setEra={setEra} />
        <section className="coop" aria-labelledby="coop-title">
          <h2 id="coop-title">{t.coopTitle}</h2>
          <div className="coop-text">{t.coop.map((p) => <p key={p}>{p}</p>)}</div>
        </section>
        <Ledger t={t} />
        <section className="museum" aria-label={t.museumBy}>
          <blockquote>
            <p>{t.museumQuote}</p>
            <footer>{t.museumBy}</footer>
          </blockquote>
          <p className="museum-text">{t.museumText}</p>
        </section>
        <Gallery lang={lang} t={t} />
        <section className="modes" aria-labelledby="modes-title">
          <h2 id="modes-title">{t.modesTitle}</h2>
          <dl>{t.modes.map(([dt, dd]) => <div key={dt}><dt>{dt}</dt><dd>{dd}</dd></div>)}</dl>
        </section>
        <section className="faq" aria-labelledby="faq-title">
          <h2 id="faq-title">{t.faqTitle}</h2>
          {t.faq.map(([q, a]) => <details key={q}><summary>{q}</summary><p>{a}</p></details>)}
        </section>
        <Footer.Final t={t} />
      </main>
      <Footer.Bottom t={t} />
    </>
  );
}
