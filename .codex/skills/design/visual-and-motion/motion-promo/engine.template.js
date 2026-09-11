/* ============================================================================
   MOTION PROMO ENGINE — starter template
   ----------------------------------------------------------------------------
   One pure function drives everything:   drawFrame(ctx, tSeconds)

   Because it is pure and seekable, the SAME file powers
     - the live HTML preview (browser canvas)
     - the MP4 render      (node + @napi-rs/canvas)
   so what you scrub in the browser is exactly what encodes. Never fork them.

   TO USE: edit BRAND + TIMELINE below, then write one draw function per scene.
   ========================================================================== */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.PROMO = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  /* ==========================================================================
     1. CONFIG — the only part you normally edit
     ========================================================================== */
  var W = 720, H = 1280, FPS = 30;          // 9:16. Use 1920x1080 for 16:9.

  var BRAND = {
    name: 'BRANDNAME',
    font: '"Helvetica Neue", Helvetica, "Liberation Sans", Arial, sans-serif',
    ink: '#ffffff',
    accent: '#7a5cff',
    hot: '#2bff8c'                          // the "just happened" highlight colour
  };

  // Scenes run back to back. `end` of the last one is the film's duration.
  // Keep beats between 1.5s and 4s — shorter reads as a glitch, longer drags.
  var TIMELINE = [
    { name: 'hook', end: 4.00, fn: sceneHook },
    { name: 'logo', end: 7.45, fn: sceneLogo },
    { name: 'ui', end: 11.90, fn: sceneUI },
    { name: 'grid', end: 16.77, fn: sceneGrid }
  ];

  var DUR = TIMELINE[TIMELINE.length - 1].end;

  /* ==========================================================================
     2. MATH — easing. Choosing the right curve is most of the "feel".
        smooth    : general motion. Safe default.
        easeOut   : arrivals — fast in, settles. Camera pushes, entrances.
        easeIn    : exits — slow then whips away.
        easeOut4  : hard arrivals, e.g. a card slamming into place.
        easeBack  : slight overshoot. Use sparingly, it reads as "cute".
        NEVER use easeIn (cubic) for a long move — nothing happens, then it
        lurches. That reads as dropped frames, not motion.
     ========================================================================== */
  function clamp(v, a, b) { a = a === undefined ? 0 : a; b = b === undefined ? 1 : b; return v < a ? a : v > b ? b : v; }
  function lerp(a, b, t) { return a + (b - a) * t; }
  function inv(t, a, b) { return clamp((t - a) / (b - a)); }       // time -> 0..1
  function smooth(t) { return t * t * (3 - 2 * t); }
  function easeOut(t) { return 1 - Math.pow(1 - t, 3); }
  function easeOut4(t) { return 1 - Math.pow(1 - t, 4); }
  function easeIn(t) { return t * t * t; }
  function easeInOut(t) { return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; }
  function easeBack(t) { var c = 1.3; return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2); }

  /* colour — both helpers take AND return hex so they compose freely.
     (A mixer that returns rgb() will silently break any hexa() downstream.) */
  function hexa(h, a) {
    var n = parseInt(h.slice(1), 16);
    return 'rgba(' + ((n >> 16) & 255) + ',' + ((n >> 8) & 255) + ',' + (n & 255) + ',' + a + ')';
  }
  function mix(h1, h2, t) {
    var a = parseInt(h1.slice(1), 16), b = parseInt(h2.slice(1), 16);
    var r = Math.round(lerp((a >> 16) & 255, (b >> 16) & 255, t));
    var g = Math.round(lerp((a >> 8) & 255, (b >> 8) & 255, t));
    var l = Math.round(lerp(a & 255, b & 255, t));
    return '#' + (((1 << 24) + (r << 16) + (g << 8) + l).toString(16).slice(1));
  }
  function rng(seed) { var s = seed; return function () { s = (s * 1664525 + 1013904223) % 4294967296; return s / 4294967296; }; }

  /* ==========================================================================
     3. PRIMITIVES
     ========================================================================== */
  function rr(ctx, x, y, w, h, r) {                       // rounded rect
    r = Math.min(r, Math.abs(w) / 2, Math.abs(h) / 2);
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y); ctx.quadraticCurveTo(x + w, y, x + w, y + r);
    ctx.lineTo(x + w, y + h - r); ctx.quadraticCurveTo(x + w, y + h, x + w - r, y + h);
    ctx.lineTo(x + r, y + h); ctx.quadraticCurveTo(x, y + h, x, y + h - r);
    ctx.lineTo(x, y + r); ctx.quadraticCurveTo(x, y, x + r, y);
    ctx.closePath();
  }

  function glow(ctx, x, y, r, color, a, add) {            // radial bloom
    if (r <= 0 || a <= 0) return;
    ctx.save();
    if (add !== false) ctx.globalCompositeOperation = 'lighter';
    var g = ctx.createRadialGradient(x, y, 0, x, y, r);
    g.addColorStop(0, hexa(color, a));
    g.addColorStop(0.30, hexa(color, a * 0.55));
    g.addColorStop(0.62, hexa(color, a * 0.18));
    g.addColorStop(1, hexa(color, 0));
    ctx.fillStyle = g; ctx.fillRect(x - r, y - r, r * 2, r * 2);
    ctx.restore();
  }
  function glowE(ctx, x, y, rx, ry, color, a, add) {      // elliptical bloom
    ctx.save();
    ctx.translate(x, y); ctx.scale(1, ry / rx); ctx.translate(-x, -y);
    glow(ctx, x, y, rx, color, a, add);
    ctx.restore();
  }

  /*  ---- THE ONE THAT MAKES IT LOOK EXPENSIVE ----------------------------
      Cheap motion graphics put a soft oval behind an object and call it glow.
      Real product renders bloom in the SHAPE OF THE OBJECT. shapeBloom draws
      blurred, progressively larger copies of the object's own silhouette.
      `path` is a function that traces the shape at a given scale.            */
  function shapeBloom(ctx, path, color, amount, layers) {
    layers = layers || [[4.2, 0.26], [3.1, 0.34], [2.2, 0.40], [1.5, 0.44], [1.15, 0.40]];
    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    for (var i = 0; i < layers.length; i++) {
      var k = layers[i][0], a = layers[i][1] * amount;
      try { ctx.filter = 'blur(' + (12 + k * 20).toFixed(0) + 'px)'; } catch (e) { }
      path(k);
      ctx.fillStyle = hexa(color, a); ctx.fill();
    }
    try { ctx.filter = 'none'; } catch (e) { }
    ctx.restore();
  }

  /*  A swell that breathes once across a beat, with a smaller second pulse.
      Use it on glow amplitude so light never sits at a constant level —
      static glow is the #1 tell of an amateur render.                        */
  function swell(p) {
    var big = Math.sin(clamp(p) * Math.PI);
    var small = 0.5 - 0.5 * Math.cos(clamp(p) * Math.PI * 3.1);
    return 0.34 + 0.50 * big + 0.18 * small * big;
  }

  /* text with letter-spacing (canvas letterSpacing is not portable) */
  function setFont(ctx, weight, size) { ctx.font = weight + ' ' + size + 'px ' + BRAND.font; }
  function trackW(ctx, txt, sp) {
    var w = 0; for (var i = 0; i < txt.length; i++) w += ctx.measureText(txt[i]).width + sp;
    return txt.length ? w - sp : 0;
  }
  function trackFill(ctx, txt, x, y, sp) {
    var c = x; for (var i = 0; i < txt.length; i++) { ctx.fillText(txt[i], c, y); c += ctx.measureText(txt[i]).width + sp; }
    return c;
  }

  /*  Typewriter. Returns how far it got. The last character typed flashes
      BRAND.hot then cools to ink — that tiny detail is what sells "live".   */
  function typeOut(ctx, txt, x, y, p, size, ink, hot, hotHold) {
    setFont(ctx, '700', size);
    var n = Math.min(txt.length, Math.floor(clamp(p) * (txt.length + 0.6)));
    var cx = x;
    for (var i = 0; i < n; i++) {
      var recent = i >= n - 2 ? (i === n - 1 ? 1 : 0.65) : 0;
      ctx.fillStyle = recent > 0 && hotHold > 0 ? mix(ink, hot, hotHold * recent) : ink;
      ctx.fillText(txt[i], cx, y);
      cx += ctx.measureText(txt[i]).width;
    }
    return { x: cx, done: n >= txt.length, n: n };
  }

  /*  Premium icon slab: near-black glass, coloured halo hugging its
      silhouette, lit top-left edge, bright gradient symbol inside.
      bodyA fades the slab while leaving the symbol lit — that is how you
      dissolve a container and leave its contents glowing.                    */
  function slab(ctx, o) {
    var s = o.size, h = s / 2, r = s * 0.325, a = o.alpha === undefined ? 1 : o.alpha;
    var bodyA = o.bodyA === undefined ? 1 : o.bodyA;
    if (a <= 0.004) return;
    ctx.save();
    ctx.globalAlpha = a;
    ctx.translate(o.x, o.y);
    if (o.rot) ctx.rotate(o.rot);
    var g = ctx.createLinearGradient(-h * 0.8, -h, h * 0.8, h);
    g.addColorStop(0, o.c1); g.addColorStop(1, o.c2);

    ctx.save();                                            // halo
    ctx.globalAlpha = a * bodyA;
    ctx.globalCompositeOperation = 'lighter';
    try { ctx.filter = 'blur(' + (s * 0.185).toFixed(1) + 'px)'; } catch (e) { }
    rr(ctx, -h * 1.05, -h * 1.02, s * 1.10, s * 1.10, r * 1.08);
    var hg = ctx.createLinearGradient(-h, -h, h, h);
    hg.addColorStop(0, hexa(o.halo || o.c2, 0.85));
    hg.addColorStop(0.5, hexa(o.c2, 1));
    hg.addColorStop(1, hexa(o.halo || o.c2, 0.90));
    ctx.fillStyle = hg; ctx.fill();
    try { ctx.filter = 'none'; } catch (e) { }
    ctx.restore();

    ctx.save();                                            // contact shadow
    ctx.globalAlpha = a * bodyA;
    rr(ctx, -h, -h + s * 0.05, s, s, r);
    ctx.shadowColor = 'rgba(0,0,0,0.85)'; ctx.shadowBlur = s * 0.24; ctx.shadowOffsetY = s * 0.09;
    ctx.fillStyle = '#000'; ctx.fill();
    ctx.restore();

    ctx.save();                                            // glass body
    ctx.globalAlpha = a * bodyA;
    rr(ctx, -h, -h, s, s, r);
    var bg = ctx.createLinearGradient(-h, -h, h * 0.5, h);
    bg.addColorStop(0, '#181822'); bg.addColorStop(0.42, '#0a0a12'); bg.addColorStop(1, '#020206');
    ctx.fillStyle = bg; ctx.fill();
    ctx.restore();

    ctx.save();                                            // lit edge
    ctx.globalAlpha = a * bodyA;
    rr(ctx, -h, -h, s, s, r); ctx.clip();
    var eg = ctx.createLinearGradient(-h, -h, h * 0.6, h * 0.9);
    eg.addColorStop(0, hexa(o.c1, 0.75));
    eg.addColorStop(0.30, 'rgba(255,255,255,0.16)');
    eg.addColorStop(0.72, 'rgba(255,255,255,0.03)');
    eg.addColorStop(1, hexa(o.c2, 0.28));
    rr(ctx, -h + s * 0.018, -h + s * 0.018, s - s * 0.036, s - s * 0.036, r * 0.94);
    ctx.lineWidth = s * 0.036; ctx.strokeStyle = eg; ctx.stroke();
    ctx.restore();

    ctx.save();                                            // symbol
    ctx.shadowColor = hexa(o.glowCol || o.c1, 0.95);
    ctx.shadowBlur = s * (o.glowCol ? 0.40 : 0.30);
    var fill = o.symbolCol || g;
    if (o.symbol2 && o.morph > 0.001) {                    // crossfade symbols,
      if (o.morph < 0.999) {                               // container unchanged
        ctx.save(); ctx.globalAlpha = 1 - o.morph;
        ctx.scale(1 - o.morph * 0.35, 1 - o.morph * 0.35);
        o.symbol(ctx, s * 0.84, fill); ctx.restore();
      }
      ctx.save(); ctx.globalAlpha = o.morph;
      ctx.scale(0.68 + o.morph * 0.32, 0.68 + o.morph * 0.32);
      o.symbol2(ctx, s * 0.84, fill); ctx.restore();
    } else {
      o.symbol(ctx, s * 0.84, fill);
    }
    ctx.restore();
    ctx.restore();
  }

  /*  A ring of objects that starts clustered and expands outward while
      growing and slowly rotating. Reads as deliberate; scattered diagonal
      fly-bys read as filler.                                                 */
  function ringAt(items, i, p, opt) {
    opt = opt || {};
    var e = easeOut(clamp(p));
    var rad = lerp(opt.r0 || 90, opt.r1 || 415, e);
    var ang = (items[i].angle + clamp(p) * (opt.spin === undefined ? 0.30 : opt.spin)) * 6.2832;
    return {
      x: W / 2 + Math.cos(ang) * rad * (opt.rx || 0.92),
      y: H / 2 + Math.sin(ang) * rad * (opt.ry || 1.34),
      size: items[i].size * lerp(0.46, 1.18, e),
      rot: Math.sin(ang) * 0.12,
      alpha: smooth(inv(p, 0, 0.12)) * (1 - smooth(inv(p, 0.88, 1.0)))
    };
  }

  function watermark(ctx) {
    if (!BRAND.name) return;
    var s = 38, gap = 15, track = 2.6;
    ctx.save();
    ctx.globalAlpha = 0.30;
    setFont(ctx, '700', s * 1.02);
    var w = trackW(ctx, BRAND.name, track);
    ctx.fillStyle = BRAND.ink;
    ctx.textBaseline = 'alphabetic';
    trackFill(ctx, BRAND.name, W - 62 - w, 98 + s * 0.88, track);
    ctx.restore();
  }

  /* ==========================================================================
     4. SCENES — local time t starts at 0 for each one.
        Every scene owns its own fade in/out. Cut hard where the reference
        cuts hard; do not smooth a cut into a dissolve.
     ========================================================================== */

  function sceneHook(ctx, t, dur) {
    var fade = smooth(inv(t, 0, 0.15)) * (1 - smooth(inv(t, dur - 0.14, dur)));
    ctx.save(); ctx.globalAlpha = fade;

    var push = easeOut(inv(t, 0, dur * 0.8));              // slow camera push-in
    glow(ctx, W / 2, H * 0.42, lerp(280, 420, push), BRAND.accent, 0.55);

    var p = inv(t, 0.30, 1.05);
    var hold = clamp(1 - (t - (0.30 + p * 0.75)) / 0.30);
    setFont(ctx, '700', 66);
    var msg = 'Your headline';
    var x = (W - trackW(ctx, msg, 0.4)) / 2;
    ctx.shadowColor = 'rgba(180,210,255,0.55)'; ctx.shadowBlur = 22;
    typeOut(ctx, msg, x, H * 0.42, p, 66, BRAND.ink, BRAND.hot, hold);
    ctx.restore();
  }

  function sceneLogo(ctx, t, dur) {
    var fade = smooth(inv(t, 0, 0.18)) * (1 - smooth(inv(t, dur - 0.30, dur)));
    ctx.save(); ctx.globalAlpha = fade;

    // shockwave out of the impact point — travels at a CONSTANT rate
    var rp = inv(t, 0, 0.88);
    if (rp > 0 && rp < 1) {
      var r = lerp(14, 800, rp), th = lerp(60, 200, rp);
      var ra = (1 - smooth(inv(rp, 0.40, 1))) * 0.95;
      var g = ctx.createRadialGradient(W / 2, H * 0.455, Math.max(1, r - th), W / 2, H * 0.455, r + th * 0.55);
      g.addColorStop(0, hexa(BRAND.accent, 0));
      g.addColorStop(0.50, hexa(BRAND.accent, 0.62 * ra));
      g.addColorStop(0.66, hexa(BRAND.accent, 0.95 * ra));
      g.addColorStop(1, hexa(BRAND.accent, 0));
      ctx.save(); ctx.globalCompositeOperation = 'lighter';
      ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      ctx.restore();
    }

    // wordmark: holds small and hot, then SNAPS (~2 frames) to its final state
    var snap = smooth(inv(t, 0.97, 1.05));
    var size = lerp(29, 48, snap);
    var col = snap > 0.5 ? BRAND.ink : mix('#d81028', '#ff7a1a', smooth(inv(t, 0.02, 0.9)));
    setFont(ctx, '700', size);
    ctx.fillStyle = col;
    ctx.shadowColor = hexa(snap > 0.5 ? '#ffffff' : '#ff2f6e', 0.8);
    ctx.shadowBlur = lerp(30, 14, snap);
    ctx.textBaseline = 'alphabetic';
    trackFill(ctx, BRAND.name, W * 0.495 - trackW(ctx, BRAND.name, 1.4) / 2, H * 0.481 + size * 0.4, 1.4);
    ctx.restore();
  }

  function sceneUI(ctx, t, dur) {
    var fade = smooth(inv(t, 0, 0.10)) * (1 - smooth(inv(t, dur - 0.15, dur)));
    var queries = ['First query', 'Second query', 'Third query'];
    var each = dur / queries.length;
    ctx.save(); ctx.globalAlpha = fade;

    for (var i = 0; i < queries.length; i++) {
      var t0 = i * each, p = (t - t0) / each;
      if (p < -0.14 || p > 1.10) continue;

      // vertical carousel: in from below, out through the top
      var inP = easeOut(inv(p, -0.14, 0.12));
      var outP = easeIn(inv(p, 0.88, 1.04));
      var slide = lerp(300, 0, inP) - outP * 330;
      var scl = lerp(0.72, 1, inP) * lerp(1, 0.62, outP);
      var alpha = Math.min(1, inP * 1.6) * (1 - smooth(outP));
      if (alpha <= 0.004) continue;

      setFont(ctx, '700', 41);
      var pw = Math.max(590, ctx.measureText(queries[i]).width + 215), ph = 94;
      var cx = W / 2, cy = H * 0.503 + slide;

      ctx.save();
      ctx.globalAlpha = fade * alpha;
      shapeBloom(ctx, function (k) {
        var bw = pw * (1 + (k - 1) * 0.30) * scl, bh = ph * k * scl;
        rr(ctx, cx - bw / 2, cy - bh / 2, bw, bh, bh / 2);
      }, BRAND.accent, swell(clamp(p)));

      ctx.translate(cx, cy); ctx.scale(scl, scl); ctx.translate(-cx, -cy);
      rr(ctx, cx - pw / 2, cy - ph / 2, pw, ph, ph / 2);
      ctx.shadowColor = hexa(BRAND.accent, 1); ctx.shadowBlur = 48;
      ctx.lineWidth = 7; ctx.strokeStyle = BRAND.accent; ctx.stroke();
      ctx.shadowBlur = 0;
      ctx.fillStyle = '#08080f'; ctx.fill();

      var tp = inv(p, 0.06, 0.52);
      var per = (0.52 - 0.06) * each / (queries[i].length + 0.6);
      var n = Math.floor(clamp(tp) * (queries[i].length + 0.6));
      var hold = clamp(1 - (t - (t0 + 0.06 * each + n * per)) / 0.28);
      typeOut(ctx, queries[i], cx - pw / 2 + 46, cy + 14, tp, 41, BRAND.ink, BRAND.hot, hold);
      ctx.restore();
    }
    ctx.restore();
  }

  function sceneGrid(ctx, t, dur) {
    var fade = smooth(inv(t, 0, 0.10));
    var sym = function (ctx, s, fill) {                    // replace with real icons
      ctx.save(); ctx.scale(s / 100, s / 100); ctx.fillStyle = fill;
      ctx.beginPath(); ctx.arc(0, 0, 30, 0, 6.2832); ctx.fill(); ctx.restore();
    };
    var items = [];
    for (var i = 0; i < 8; i++) items.push({ angle: i / 8 - 0.25, size: 180, symbol: sym });

    ctx.save();
    var b = 1 - smooth(inv(t, 0, 0.34));                   // arrival burst
    if (b > 0.01) glow(ctx, W / 2, H / 2, lerp(300, 780, 1 - b), BRAND.accent, 0.85 * b * fade);

    var p = inv(t, 0, dur * 0.62);
    for (var j = 0; j < items.length; j++) {
      var q = ringAt(items, j, p);
      slab(ctx, {
        x: q.x, y: q.y, size: q.size, rot: q.rot, alpha: fade * q.alpha,
        c1: '#ffffff', c2: BRAND.accent, halo: BRAND.accent, symbol: items[j].symbol
      });
    }
    ctx.restore();
  }

  /* ==========================================================================
     5. MASTER
     ========================================================================== */
  function drawFrame(ctx, t) {
    t = Math.max(0, Math.min(DUR - 0.0001, t));
    ctx.save();
    ctx.globalCompositeOperation = 'source-over';
    ctx.globalAlpha = 1;
    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, W, H);
    ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';

    var start = 0;
    for (var i = 0; i < TIMELINE.length; i++) {
      if (t < TIMELINE[i].end) { TIMELINE[i].fn(ctx, t - start, TIMELINE[i].end - start); break; }
      start = TIMELINE[i].end;
    }
    watermark(ctx);
    ctx.restore();
  }

  return {
    W: W, H: H, FPS: FPS, DUR: DUR, BRAND: BRAND, TIMELINE: TIMELINE,
    drawFrame: drawFrame,
    // exported so scenes in other files can reuse them
    u: {
      clamp: clamp, lerp: lerp, inv: inv, smooth: smooth, easeOut: easeOut,
      easeOut4: easeOut4, easeIn: easeIn, easeInOut: easeInOut, easeBack: easeBack,
      hexa: hexa, mix: mix, rng: rng, rr: rr, glow: glow, glowE: glowE,
      shapeBloom: shapeBloom, swell: swell, setFont: setFont, trackW: trackW,
      trackFill: trackFill, typeOut: typeOut, slab: slab, ringAt: ringAt
    }
  };
});
