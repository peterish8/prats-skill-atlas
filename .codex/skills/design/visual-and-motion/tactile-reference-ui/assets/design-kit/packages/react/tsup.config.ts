import { defineConfig } from 'tsup';

export default defineConfig({
  entry: ['src/index.tsx'],
  format: ['esm'],
  dts: true,
  external: ['react', '@tactile-ui/tokens'],
  banner: { js: "'use client';" }
});
