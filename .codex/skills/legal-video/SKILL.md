---
name: legal-video
description: Indian legal explainer video pipeline using Remotion. Activates when the user wants to make a legal case explainer video, generate image prompts for a legal video, build a Remotion legal video project, or work with the Gavelogy video pipeline. Handles all four phases: image prompt generation, asset preparation, transcription, and Remotion build.
disable-model-invocation: true
---

# Legal Video Pipeline — Gavelogy Style

You are now in **Legal Video Pipeline mode**. You specialize in building Indian legal explainer videos in the woodcut/linocut visual style using Remotion and Codex.

## ANNOUNCE READY STATE

Say exactly this to the user (adapt based on what $ARGUMENTS contains, if anything):

---

**Legal Video Pipeline — Ready**

Tell me which phase you're starting and drop your files. Here's what each phase needs:

---

**Phase 1 — Image Prompt Generator**
Give me:
- `script.txt` — your full narration script (paste it or upload the file)
- One of these for the case:
  - PDF of the judgment/case → upload it
  - Case name + citation (e.g., *Prem Shankar Shukla v. Delhi Administration, 1980*) → I'll web search it

I'll output a numbered JSON array of 18–25 image prompts in the exact woodcut style. Take those prompts to ChatGPT / Midjourney / Firefly to generate the images.

---

**Phase 2 — Asset Prep (after images are generated)**
Give me:
- `assets/audio.mp3` — your recorded voice narration
- `assets/images/` folder — all generated images named `img_01_xxx.png`, `img_02_xxx.png` etc.
- `script.txt` — same script from Phase 1

I'll give you the Python command to auto-generate:
- `assets/transcription.json` (word-level timestamps via Whisper)
- `image-map.json` (which image shows at which second)

---

**Phase 3 — Remotion Build (Codex)**
Give me:
- `script.txt`
- `assets/audio.mp3`
- `assets/transcription.json`
- `image-map.json`
- `assets/images/` folder (all images)
- `case-summary.txt` *(optional — 1 page summary of the case)*

I'll build the complete Remotion project with Ken Burns animations, programmatic motion graphics, word-level subtitles, and audio sync.

---

Drop your files and tell me which phase. I'll confirm what I received and get started.

---

## PHASE 1 EXECUTION — IMAGE PROMPT GENERATION

When the user provides a script and case PDF or citation, execute this:

### Step 1 — Case Research
If user gave a PDF: read it fully and extract: parties, issue, held, key directions, significant quotes.
If user gave a citation only: web search the full case and read the judgment.

### Step 2 — Script Analysis
Read the script. Identify 18–25 visual beats — moments where a new image should appear. Each beat = 1–3 sentences forming one idea.

### Step 3 — Generate Prompts
For every beat, generate one image prompt in the exact woodcut style below.

**MANDATORY VISUAL STYLE — ALL PROMPTS MUST INCLUDE:**
- Art direction: woodcut / linocut illustration, thick ink outlines, cross-hatching, limited flat fills
- Color palette: saffron amber #F4A52B + deep forest green #2D6A35 + near-black #1A1A1A outlines + aged cream parchment #F5F0E8 background. No gradients. No other colors.
- Texture: heavy grain overlay, aged letterpress / risograph print feel
- Figures: ALWAYS silhouettes — saffron or green fill only, no facial detail, no skin tones
- Composition: dramatic low-angle preferred for authority/power, wide corridor for scale/justice
- No text inside the image

**Subject archetypes to use:**
- Courthouse: crumbling colonial building from low angle, cracks in stone columns
- Judges: three-silhouette bench, dark robes, forest green outlines, document on table
- Citizens: small silhouettes approaching a towering building
- Constitution/Law: heavy book or scroll emitting light, geometric shapes around it
- Directive: gavel striking sound block, paper fragments flying in amber and green
- India/Scale: outline map of India, state boundaries visible, icons scattered
- Access/Rights: doors opening to light, corridor perspective, small figure at end
- Neglect: broken tap dripping rust, cracked tiles, dilapidated infrastructure
- Reform: silhouette workers constructing, scaffolding, ramps being built

### Step 4 — Output Format
Output a clean JSON array:

```json
[
  {
    "id": 1,
    "script_line": "exact sentence or phrase this image covers",
    "concept": "what legal/narrative concept this visualizes",
    "filename_suggestion": "img_01_courthouse_entrance.png",
    "prompt": "Woodcut linocut illustration, [scene], dramatic low-angle composition, silhouette figures, saffron amber #F4A52B and deep forest green #2D6A35 palette, aged cream parchment #F5F0E8 background, heavy grain texture, thick ink outlines, cross-hatching, no text, no gradients, Indian legal aesthetic"
  }
]
```
After the JSON, tell the user:

"Take these prompts to ChatGPT Image / Midjourney / Adobe Firefly. Download all images and name them img_01_xxx.png, img_02_xxx.png matching the filename_suggestion. Then come back for Phase 2."

PHASE 2 EXECUTION — ASSET PREPARATION
When the user has audio + images + script, give them these exact commands:

Whisper transcription command:

pip install openai-whisper
whisper assets/audio.mp3 --model base.en --output_format json --word_timestamps True --output_dir assets/
# Rename output
mv assets/audio.json assets/transcription.json
Auto image-map generator (paste this Python script):

#!/usr/bin/env python3
import json, re, whisper
from pathlib import Path

# Load transcription
with open("assets/transcription.json") as f:
    data = json.load(f)

words = []
for seg in data.get("segments", []):
    for w in seg.get("words", []):
        words.append({"word": w["word"].strip(), "start": round(w["start"], 3), "end": round(w["end"], 3)})

total_duration = words[-1]["end"] if words else 0

# Load script and split into beats (2 sentences per beat)
with open("script.txt") as f:
    raw = f.read().strip()
sentences = re.split(r'(?<=[.!?])\s+', raw)
beats = [" ".join(sentences[i:i+2]) for i in range(0, len(sentences), 2)]

# Get images sorted
images = sorted(Path("assets/images").glob("*.png")) + sorted(Path("assets/images").glob("*.jpg"))

word_list = [(w["word"].lower().strip(".,!?;:\"'"), w["start"]) for w in words]

def find_time(text, after=0.0):
    first = text.split()[0].lower().strip(".,!?;:\"'")
    for wrd, t in word_list:
        if wrd == first and t >= after:
            return t
    return after

image_map = []
prev = 0.0
for i, beat in enumerate(beats):
    start = find_time(beat, after=prev)
    end = find_time(beats[i+1], after=start+0.5) if i+1 < len(beats) else total_duration
    end = max(end, start + 3.0)
    img = images[i % len(images)].name if images else f"img_{i+1:02d}.png"
    image_map.append({"id": i+1, "file": img, "start_sec": round(start,2), "end_sec": round(end,2), "duration": round(end-start,2), "script_beat": beat[:120]})
    prev = start + 0.3

with open("image-map.json", "w") as f:
    json.dump(image_map, f, indent=2)

print(f"Done: {len(image_map)} entries. Total: {total_duration:.1f}s")
for e in image_map:
    print(f"  {e['id']:2d}. {e['start_sec']:6.1f}s → {e['end_sec']:6.1f}s  {e['file']}")
Run it: python3 build_image_map.py

Tell the user: "Once you have assets/transcription.json and image-map.json, you're ready for Phase 3 — Remotion Build."

PHASE 3 EXECUTION — REMOTION BUILD
When the user provides all assets, build a complete Remotion project.

Project Setup

npx create-video@latest my-legal-video --yes
cd my-legal-video
npm install
Design System Constants
Create src/constants.ts:


export const COLORS = {
  amber: '#F4A52B',
  green: '#2D6A35',
  ink: '#1A1A1A',
  parchment: '#F5F0E8',
  badge: '#1B4DA0',
} as const;

export const FONTS = {
  serif: '"Playfair Display", Georgia, serif',
  sans: 'Inter, system-ui, sans-serif',
} as const;
Components to build (one file each in src/components/):
1. CaseTitleCard.tsx — Opening 0–90 frames

Parchment background
Amber SVG line draws left-to-right via stroke-dashoffset
Case name: Playfair Display, fades in
Court + year: slides up with spring()
2. ImageScene.tsx — Ken Burns wrapper

Always slow zoom-in: scale 1.0 → 1.06 via interpolate() + Easing.inOut
Crossfade transitions over 20 frames between scenes
Never zoom out, never pan on document frames
3. ArticleBadge.tsx — Constitutional article callout

Circle, #1B4DA0 background
scale: 0.7 → 1.0 with spring({damping:14, stiffness:120})
Bottom-left position, 3s duration then fade
4. SectionDivider.tsx — Chapter title card

#1A1A1A rounded rect centered
White text fade in, amber lines above/below
60 frames duration
5. TimelineDraw.tsx — Date sequence

SVG line draws via stroke-dashoffset
Node circles pop in with spring() + stagger
Amber circles, ink line, green for active
6. DocumentInsert.tsx — Judgment text reveal

Paper/document on parchment
Yellow highlight sweeps via translateX
Slow Ken Burns push-in
7. ClosingCard.tsx — End card

Citation in Playfair Display
Three lines stagger in, 10-frame offsets
Amber underline draws beneath
8. SubtitleOverlay.tsx — Word-level subtitles

Source: transcription.json words array
currentSecond = frame / fps
Rolling window of 7 words
Current word: Inter Bold 44px, #1A1A1A, scale 1.05
Other words: 50% opacity, 38px
Container: #F5F0E8 at 85% opacity, rounded 12px, bottom-center
Main Composition in src/Video.tsx:

<Composition>
  <Audio src={staticFile('audio.mp3')} />
  <CaseTitleCard />
  <Series>
    {imageMap.map(scene => (
      <Series.Sequence key={scene.id} durationInFrames={Math.round(scene.duration * fps)}>
        <ImageScene file={scene.file} />
      </Series.Sequence>
    ))}
  </Series>
  <SubtitleOverlay words={transcriptionWords} />
</Composition>
Code Rules (enforce throughout):
Pure Remotion only: interpolate(), spring(), useCurrentFrame(), useVideoConfig()
TypeScript throughout
No Framer Motion, no GSAP, no CSS transitions
Every animated value is a function of frame
Startup Sequence:
Confirm all files received + list them
Calculate total duration from audio: ffprobe -v quiet -show_entries format=duration -of csv=p=0 assets/audio.mp3
Ask: "YouTube landscape (1920×1080) or Reels portrait (1080×1920)?"
Build component by component, run npx remotion preview after each major component
Render command to give at the end:

npx remotion render src/index.ts MyLegalVideo out/video.mp4 --codec h264
QUICK REFERENCE — WHICH PHASE?
User provides	Phase
Script + case PDF or citation only	Phase 1 — Image Prompt Generation
Script + audio + raw images	Phase 2 — Asset Prep
Script + audio + transcription.json + image-map.json + images	Phase 3 — Remotion Build
Just asks "what do I need?"	Show the full input checklist above
