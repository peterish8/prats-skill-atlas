#!/usr/bin/env node
import { access, cp, mkdir } from 'node:fs/promises';
import { constants } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const kit = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const args = process.argv.slice(2);
const value = name => args[args.indexOf(name) + 1];
if (!args.includes('--target') || !args.includes('--framework') || !['react','svelte'].includes(value('--framework'))) {
  console.error('Usage: node scripts/copy-kit.mjs --target <new-directory> --framework react|svelte [--dry-run]');
  process.exit(1);
}
const target = path.resolve(value('--target'));
const framework = value('--framework');
const relation = path.relative(kit, target);
if (!relation || (!relation.startsWith('..') && !path.isAbsolute(relation))) throw new Error('Choose a destination outside the source kit.');
const exists = async p => { try { await access(p, constants.F_OK); return true; } catch { return false; } };
if (await exists(target)) throw new Error(`Destination already exists; choose a new directory: ${target}`);
const roots = ['packages','examples','dist-packages','scripts','docs','references','README.md','package.json','package-lock.json','tsconfig.base.json'];
const available = [];
for (const name of roots) if (await exists(path.join(kit,name))) available.push(name);
const filter = p => !p.split(path.sep).some(x => ['node_modules','.svelte-kit','build','.git','artifacts'].includes(x)) && path.basename(p) !== 'bundle-skill.mjs';
console.log(JSON.stringify({dryRun:args.includes('--dry-run'),source:kit,target,framework,copy:available},null,2));
if (!args.includes('--dry-run')) {
  await mkdir(target,{recursive:true});
  for (const name of available) await cp(path.join(kit,name),path.join(target,name),{recursive:true,filter,errorOnExist:true,force:false});
  console.log('Copied the portable kit. Your application and package.json were not modified.');
}
const tokens = path.join(target,'dist-packages','tactile-ui-tokens-0.1.0.tgz');
const component = path.join(target,'dist-packages',`tactile-ui-${framework}-0.1.0.tgz`);
console.log(`From your application directory, install both tarballs together:\nnpm install "${tokens}" "${component}"`);
console.log("Import '@tactile-ui/tokens/styles.css' once, then import components from '@tactile-ui/"+framework+"'.");
