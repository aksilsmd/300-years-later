import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// base relative : fonctionne sur GitHub Pages comme sur tout hébergeur statique
export default defineConfig({
  base: "./",
  plugins: [react()],
  build: { sourcemap: false, assetsInlineLimit: 0 },
});
