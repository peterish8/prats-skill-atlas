#!/usr/bin/env node
/**
 * Checks a planning folder written by the precision-plan skill:
 *   node check-plans.mjs <planning-dir>
 *
 * - every requirement id in REQUIREMENTS.md is claimed by at least one plan
 * - every plan claims only ids that exist
 * - every plan has the required frontmatter fields and at least one <task>
 * - every depends_on points at a plan that exists, and no plan depends on a later wave
 * - every task has <files>, <read_first>, <action>, <verify>, <acceptance_criteria>, <done>
 *   (checkpoint tasks are exempt)
 * Exits 1 with a list of problems, 0 when clean.
 */
import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';

const dir = process.argv[2];
if (!dir) {
  console.error('usage: node check-plans.mjs <planning-dir>');
  process.exit(2);
}

const problems = [];
const walk = (path) => statSync(path).isDirectory() ? readdirSync(path).flatMap((name) => walk(join(path, name))) : [path];
const planFiles = walk(dir).filter((file) => /\d{2}-\d{2}-PLAN\.md$/.test(file));
const lf = (text) => text.split('\r\n').join('\n');
const reqText = (() => { try { return lf(readFileSync(join(dir, 'REQUIREMENTS.md'), 'utf8')); } catch { return ''; } })();
const reqIds = new Set([...reqText.matchAll(/\*\*([A-Z]{2,5}-\d{2})\*\*/g)].map((m) => m[1]));
if (reqIds.size === 0) problems.push('REQUIREMENTS.md: no **ID-NN** requirement ids found');

const plans = new Map();
for (const file of planFiles) {
  const text = lf(readFileSync(file, 'utf8'));
  const id = file.match(/(\d{2}-\d{2})-PLAN\.md$/)[1];
  const front = text.match(/^---\n([\s\S]*?)\n---/);
  const where = relative(dir, file);
  if (!front) { problems.push(`${where}: no frontmatter`); continue; }
  const field = (name) => front[1].match(new RegExp(`^${name}:\\s*(.*)$`, 'm'))?.[1]?.trim();
  for (const name of ['phase', 'plan', 'type', 'wave', 'depends_on', 'files_modified', 'autonomous', 'requirements', 'must_haves']) {
    if (field(name) === undefined) problems.push(`${where}: missing frontmatter "${name}"`);
  }
  const list = (raw) => (raw ?? '').replace(/[[\]"]/g, '').split(',').map((s) => s.trim()).filter(Boolean);
  const requirements = list(field('requirements'));
  if (requirements.length === 0) problems.push(`${where}: requirements is empty`);
  for (const req of requirements) if (!reqIds.has(req)) problems.push(`${where}: unknown requirement ${req}`);
  const tasks = [...text.matchAll(/<task type="([^"]+)"[^>]*>([\s\S]*?)<\/task>/g)];
  if (tasks.length === 0) problems.push(`${where}: no <task>`);
  for (const [, type, body] of tasks) {
    if (type.startsWith('checkpoint')) continue;
    for (const tag of ['files', 'read_first', 'action', 'verify', 'acceptance_criteria', 'done']) {
      if (!body.includes(`<${tag}>`)) problems.push(`${where}: a "${type}" task has no <${tag}>`);
    }
  }
  if (!/<verification>/.test(text)) problems.push(`${where}: no <verification> block`);
  plans.set(id, { where, wave: Number(field('wave')), depends: list(field('depends_on')), requirements });
}

const claimed = new Set([...plans.values()].flatMap((plan) => plan.requirements));
for (const id of reqIds) if (!claimed.has(id)) problems.push(`REQUIREMENTS.md: ${id} is claimed by no plan`);
for (const [id, plan] of plans) {
  for (const dep of plan.depends) {
    const target = plans.get(dep);
    if (!target) problems.push(`${plan.where}: depends_on ${dep}, which does not exist`);
    else if (dep.slice(0, 2) === id.slice(0, 2) && target.wave >= plan.wave) problems.push(`${plan.where}: depends on ${dep} in the same or a later wave`);
  }
}

if (problems.length > 0) {
  console.error(`${problems.length} problem(s) in ${plans.size} plans:`);
  for (const problem of problems) console.error(`- ${problem}`);
  process.exit(1);
}
console.log(`ok: ${plans.size} plans, ${reqIds.size} requirements, all covered`);
