import type { Content, Lang } from "../content";

type Props = { lang: Lang; setLang: (l: Lang) => void; t: Content };

export function Header({ lang, setLang, t }: Props) {
  return (
    <header className="top">
      <a className="wordmark" href="#" aria-label="300 Years Later">
        <span className="wm-num">300</span> <span className="wm-txt">Years Later</span>
      </a>
      <nav aria-label="Langue / Language" className="lang">
        {(["fr", "en"] as const).map((l) => (
          <button key={l} type="button" aria-pressed={lang === l} onClick={() => setLang(l)}>
            {l.toUpperCase()}
          </button>
        ))}
      </nav>
      <a className="btn btn-small" href="#final">{t.ctaShort}</a>
    </header>
  );
}
