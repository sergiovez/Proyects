import { defineConfig } from 'vite';
import { viteStaticCopy } from 'vite-plugin-static-copy';

export default defineConfig({
  server: {
    host: true,
    watch: {
      usePolling: true,
    },
  },
  base: "/CSS-Modern-Art-Gallery/",
  plugins: [
    viteStaticCopy({
      targets: [
        {
          src: 'location.html',
          dest: '', // lo copia directamente en la raíz de dist
        }
      ]
    })
  ]
});
