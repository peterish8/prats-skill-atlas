/* Frame renderer — resumable by design.
   Agent shells usually cap a single command at well under a minute, and a
   full render takes minutes. Every frame that already exists on disk is
   skipped, so you just call this repeatedly until nothing is missing.

     node render.js OUTDIR                      # everything
     node render.js OUTDIR all 120 180          # a range (run 4 in parallel)
     node render.js OUTDIR preview 2.4 6.0 9.1  # stills at given seconds
     node render.js OUTDIR missing              # list gaps
*/
const { createCanvas } = require('@napi-rs/canvas');
const fs = require('fs');
const path = require('path');
const ENGINE = require('./engine.js');

const outDir = process.argv[2] || './frames';
const mode = process.argv[3] || 'all';
fs.mkdirSync(outDir, { recursive: true });

const total = Math.round(ENGINE.DUR * ENGINE.FPS);
const canvas = createCanvas(ENGINE.W, ENGINE.H);
const ctx = canvas.getContext('2d');

if (mode === 'preview') {
  process.argv.slice(4).map(Number).forEach((t, i) => {
    ENGINE.drawFrame(ctx, t);
    fs.writeFileSync(path.join(outDir, 'p_' + String(i).padStart(2, '0') + '.png'),
      canvas.toBuffer('image/png'));
  });
  console.log('preview frames:', process.argv.length - 4);

} else if (mode === 'missing') {
  const have = new Set(fs.readdirSync(outDir).filter(f => /^f_\d+\.png$/.test(f))
    .map(f => parseInt(f.slice(2, -4), 10)));
  const miss = [];
  for (let i = 0; i < total; i++) if (!have.has(i)) miss.push(i);
  console.log(JSON.stringify({ total, have: have.size, missing: miss.length, first: miss.slice(0, 10) }));

} else {
  const a = parseInt(process.argv[4] || '0', 10);
  const b = parseInt(process.argv[5] || '0', 10);
  const from = b > 0 ? a : 0, to = b > 0 ? Math.min(b, total) : total;
  const t0 = Date.now();
  let drew = 0;
  for (let i = from; i < to; i++) {
    const p = path.join(outDir, 'f_' + String(i).padStart(4, '0') + '.png');
    if (fs.existsSync(p) && fs.statSync(p).size > 2000) continue;   // resume
    ENGINE.drawFrame(ctx, i / ENGINE.FPS);
    fs.writeFileSync(p, canvas.toBuffer('image/png'));
    drew++;
  }
  console.log(`rendered ${from}->${to} (${drew} new) in ${((Date.now() - t0) / 1000).toFixed(1)}s`);
}
