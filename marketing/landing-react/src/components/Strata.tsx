import { useEffect, useRef } from "react";
import type { Era } from "../App";
import type { Content } from "../content";

type Props = { t: Content; setEra: (e: Era) => void };

// En lisant les strates, la page prend la couleur de l'époque (réponse au défilement de l'utilisateur).
export function Strata({ t, setEra }: Props) {
  const listRef = useRef<HTMLOListElement>(null);

  useEffect(() => {
    const items = listRef.current?.querySelectorAll<HTMLLIElement>("li[data-era]");
    if (!items) return;
    const io = new IntersectionObserver(
      (entries) => entries.forEach((en) => en.isIntersecting && setEra(Number(en.target.getAttribute("data-era")) as Era)),
      { rootMargin: "-45% 0px -45% 0px" },
    );
    items.forEach((i) => io.observe(i));
    return () => io.disconnect();
  }, [setEra]);

  return (
    <section className="strata" id="regle" aria-labelledby="strata-title">
      <h2 id="strata-title">{t.strataTitle}</h2>
      <ol className="layers" ref={listRef}>
        {t.layers.map((l, i) => (
          <li className="layer" data-era={i} key={l.year}>
            <p className="layer-year">{l.year}</p>
            <h3>{l.title}</h3>
            <p>{l.text}</p>
          </li>
        ))}
      </ol>
    </section>
  );
}
