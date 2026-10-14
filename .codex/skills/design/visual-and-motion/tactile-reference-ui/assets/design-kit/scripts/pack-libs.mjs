#!/usr/bin/env node
import { mkdir } from 'node:fs/promises';
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const kit=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const destination=path.join(kit,'dist-packages');
await mkdir(destination,{recursive:true});
// Invoke npm's own JS CLI; no shell interpolation or Windows cmd quoting.
const npmCli=process.env.npm_execpath;
if (!npmCli) throw new Error('Run through npm run pack:libs.');
for (const name of ['tokens','react','svelte']) {
  const result=spawnSync(process.execPath,[npmCli,'pack','--workspace',`@tactile-ui/${name}`,'--pack-destination',destination],{cwd:kit,stdio:'inherit',shell:false});
  if (result.error) throw result.error;
  if (result.status!==0) process.exit(result.status??1);
}
