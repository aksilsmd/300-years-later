// Test de charge de la landing page (k6). Usage :
//   k6 run -e BASE_URL=https://<url-de-preproduction> tests/load/landing_smoke.js
// Ne lancez jamais ce test contre un site qui ne vous appartient pas.
import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  stages: [
    { duration: "30s", target: 50 },
    { duration: "1m", target: 200 },   // pic type « vidéo virale »
    { duration: "30s", target: 0 },
  ],
  thresholds: {
    http_req_duration: ["p(95)<500"],
    http_req_failed: ["rate<0.01"],
  },
};

const BASE = __ENV.BASE_URL || "http://localhost:4173";

export default function () {
  const res = http.get(`${BASE}/`);
  check(res, {
    "statut 200": (r) => r.status === 200,
    "aucun cookie déposé": (r) => !r.headers["Set-Cookie"],
    "titre présent": (r) => r.body.includes("300 Years Later"),
  });
  sleep(1);
}
