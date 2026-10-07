import type { Content } from "../content";

// Le « grand livre des conséquences » : exemples réels tirés de data/recipes.
export function Ledger({ t }: { t: Content }) {
  return (
    <section className="ledger" aria-labelledby="ledger-title">
      <h2 id="ledger-title">{t.ledgerTitle}</h2>
      <div className="table-wrap" tabIndex={0} role="region" aria-labelledby="ledger-title">
        <table>
          <thead>
            <tr>{t.ledgerHead.map((h) => <th scope="col" key={h}>{h}</th>)}</tr>
          </thead>
          <tbody>
            {t.ledger.map(([a, b, c, d]) => (
              <tr key={a}><th scope="row">{a}</th><td>{b}</td><td>{c}</td><td>{d}</td></tr>
            ))}
          </tbody>
        </table>
      </div>
      <p className="note">{t.ledgerNote}</p>
    </section>
  );
}
