import { TanStackRouterVite } from "@tanstack/router-vite-plugin"
import react from "@vitejs/plugin-react-swc"
import { defineConfig } from "vite"

// import react from '@vitejs/plugin-react';
import { NodeGlobalsPolyfillPlugin } from '@esbuild-plugins/node-globals-polyfill';
import { NodeModulesPolyfillPlugin } from '@esbuild-plugins/node-modules-polyfill';
import {nodePolyfills} from 'vite-plugin-node-polyfills';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    TanStackRouterVite(),
    nodePolyfills(),
  ],
  // optimizeDeps: {
  //   esbuildOptions: {
  //     // Node.js global to browser globalThis
  //     define: {
  //       global: 'globalThis',
  //     },
  //     // Enable esbuild polyfill plugins
  //     plugins: [
  //       NodeGlobalsPolyfillPlugin({
  //         buffer: true,
  //         global: true,
  //       }),
  //       NodeModulesPolyfillPlugin(),
  //     ],
  //   },
  // },
});
