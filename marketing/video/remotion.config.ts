import { Config } from "@remotion/cli/config";
// Rendu final haute qualité ; les sources sont des EXR/PNG ou ProRes issus de Movie Render Graph.
Config.setVideoImageFormat("png");
Config.setCodec("h264");
Config.setCrf(16);
Config.setEntryPoint("./src/Root.tsx");
