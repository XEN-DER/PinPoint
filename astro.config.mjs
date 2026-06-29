// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import { socketIoPlugin } from './socketPlugin.js';

// https://astro.build/config
export default defineConfig({
  vite: {
    plugins: [tailwindcss(), socketIoPlugin()],
  },
});
