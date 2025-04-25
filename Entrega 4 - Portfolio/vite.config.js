import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    host: true,
    watch: {
      usePolling: true,
    },
  },
  base: "/CSS-Portfolio/",
});
