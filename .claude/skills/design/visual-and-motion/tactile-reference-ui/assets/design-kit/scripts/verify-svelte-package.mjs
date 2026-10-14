import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { existsSync, lstatSync, readFileSync, readdirSync, realpathSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const kitRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const consumerRoot = join(kitRoot, 'artifacts', 'package-consumers', 'svelte');
for (const name of ['tokens', 'svelte']) {
  const installed = join(consumerRoot, 'node_modules', '@tactile-ui', name);
  assert.ok(existsSync(installed), `${name} package must be installed first.`);
  assert.equal(lstatSync(installed).isSymbolicLink(), false, `${name} must be a real tarball installation.`);
  assert.ok(realpathSync(installed).startsWith(realpathSync(join(consumerRoot, 'node_modules'))), `${name} resolved outside the isolated consumer.`);
  const packageJson = JSON.parse(readFileSync(join(installed, 'package.json'), 'utf8'));
  assert.equal(packageJson.version, '0.1.0');
}
const lock = JSON.parse(readFileSync(join(consumerRoot, 'package-lock.json'), 'utf8'));
for (const name of ['tokens', 'svelte']) {
  const entry = lock.packages[`node_modules/@tactile-ui/${name}`];
  assert.equal(entry.link, undefined, 'Workspace links are not permitted in this validation.');
  assert.ok(entry.resolved.endsWith(`tactile-ui-${name}-0.1.0.tgz`), `${name} was not resolved from a package tarball.`);
  const tarball = join(kitRoot, 'dist-packages', `tactile-ui-${name}-0.1.0.tgz`);
  const integrity = `sha512-${createHash('sha512').update(readFileSync(tarball)).digest('base64')}`;
  assert.equal(entry.integrity, integrity, `${name} installed lock integrity differs from the reviewed tarball.`);
}
const installedIndex = readFileSync(join(consumerRoot, 'node_modules', '@tactile-ui', 'svelte', 'dist', 'index.js'), 'utf8');
const publicComponents = [...installedIndex.matchAll(/default as (\w+)/g)].map(match => match[1]);
assert.equal(publicComponents.length, 37, 'The installed Svelte package must export all 37 public components.');
const consumerSource = readFileSync(join(consumerRoot, 'src', 'App.svelte'), 'utf8');
for (const name of publicComponents) assert.ok(new RegExp(`\\b${name}\\b`).test(consumerSource), `${name} was not compiled by the consumer.`);
const serverModule = await import(pathToFileURL(join(consumerRoot, 'dist-ssr', 'entry-server.js')).href);
const rendered = serverModule.renderConsumer();
assert.equal((rendered.body.match(/<h1\b/g) ?? []).length, 1);
assert.ok(rendered.body.includes('An isolated package. A considered interface.'));
assert.ok(rendered.body.includes('data-tui-direction="meadow"'));
assert.ok(rendered.body.includes('consumer-page consumer-isolated'));
assert.ok(rendered.body.includes('data-revealed="true"'));
assert.ok(rendered.body.includes('<dialog'));
assert.ok(rendered.body.includes('12 direction tokens'));
for (const className of ['tui-marketing-hero', 'tui-site-header', 'tui-atmosphere', 'tui-frosted-icon', 'tui-showcase-card', 'tui-file-stack', 'tui-map', 'tui-poster', 'tui-tab', 'tui-motion-stage', 'tui-composer', 'tui-process-card', 'tui-device-frame', 'tui-material-object', 'tui-accordion', 'tui-segmented', 'tui-notice', 'tui-empty-state', 'tui-avatar-stack', 'tui-skeleton']) {
  assert.ok(rendered.body.includes(className), `${className} was missing from the server-rendered package consumer.`);
}
const assets = join(consumerRoot, 'dist', 'assets');
const css = readdirSync(assets).filter(file => file.endsWith('.css')).map(file => readFileSync(join(assets, file), 'utf8')).join('\n');
assert.ok(css.includes('tui-marketing-hero'), 'Packaged marketing CSS must reach the browser bundle.');
assert.ok(css.includes('tui-frosted-icon'), 'Packaged frosted icon CSS must reach the browser bundle.');
assert.ok(readdirSync(assets).some(file => file.startsWith('meadow-landscape') && file.endsWith('.png')), 'Original photographic art must be available through packaged CSS.');
assert.ok(readdirSync(assets).some(file => file.startsWith('InstrumentSerif-Regular') && file.endsWith('.ttf')), 'The serif font must be available through packaged CSS.');
assert.ok(readdirSync(assets).some(file => file.startsWith('Manrope-Variable') && file.endsWith('.ttf')), 'The sans font must be available through packaged CSS.');
const canonicalModule = await import(pathToFileURL(join(consumerRoot, 'dist-canonical-ssr', 'entry-canonical.js')).href);
for (const file of ['MeadowPage.svelte', 'recipe.css']) {
  assert.deepEqual(readFileSync(join(consumerRoot, 'src', file)), readFileSync(join(kitRoot, 'docs', 'examples', file)), `${file} differs from the canonical example.`);
}
const canonical = canonicalModule.renderCanonicalExample();
assert.equal((canonical.body.match(/<h1\b/g) ?? []).length, 1);
assert.ok(canonical.body.includes('Give your next idea a place.'));
assert.ok(canonical.body.includes('tui-composer'));
assert.ok(canonical.body.includes('tui-accordion'));
assert.ok(canonical.body.includes('tui-process-card'));
assert.ok(canonical.body.includes('This local preview is not saved'));
console.log('Svelte tarball consumer passed: real installations, 12 directions, 37 public component imports, browser CSS/art/fonts, and runtime SSR.');
console.log('Copied canonical MeadowPage.svelte example passed runtime SSR.');
