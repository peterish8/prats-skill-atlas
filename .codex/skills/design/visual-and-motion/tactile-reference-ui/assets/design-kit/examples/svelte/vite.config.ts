import { fileURLToPath } from 'node:url';
import adapter from '@sveltejs/adapter-static';
import { sveltekit } from '@sveltejs/kit/vite';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';
import { defineConfig } from 'vite';
export default defineConfig({
  plugins: [sveltekit({adapter:adapter(),preprocess:vitePreprocess()})],
  server: { fs: { allow: [fileURLToPath(new URL('../..', import.meta.url))] } },
  optimizeDeps: { exclude: ['@tactile-ui/tokens', '@tactile-ui/svelte'] }
});
