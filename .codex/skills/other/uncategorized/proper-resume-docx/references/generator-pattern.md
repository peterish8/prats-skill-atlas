# Generator Pattern

Use this pattern when writing a Node `docx` generator for Prathick resumes. Adapt content, dates, links, and sections to the user’s latest request.

## Runtime

Use the current Codex workspace dependency paths when available:

```powershell
$env:NODE_PATH = "<workspace node_modules path>"
& "<workspace node.exe>" generate_resume.js
```

In Claude/Linux contexts, the equivalent pattern is:

```bash
NODE_PATH=/home/claude/.npm-global/lib/node_modules node generate.js
```

## Required Imports

```js
const {
  Document,
  Packer,
  Paragraph,
  TextRun,
  AlignmentType,
  BorderStyle,
  TabStopType,
  LevelFormat,
  ExternalHyperlink,
  UnderlineType,
} = require("docx");
const fs = require("fs");
```

## Constants

```js
const DARK = "1A1A1A";
const LINK = "1155CC";
const GREY = "444444";
const FONT = "Arial";
const RIGHT_TAB = 9360;
const FULL_LINE = { line: 276, lineRule: "auto" };
```

## Helpers

```js
const tr = (text, opts = {}) =>
  new TextRun({
    text,
    bold: opts.bold || false,
    italics: opts.italic || false,
    size: opts.size || 20,
    font: FONT,
    color: opts.color || DARK,
    underline: opts.underline,
  });

const sec = (text) =>
  new Paragraph({
    spacing: { before: 200, after: 60, ...FULL_LINE },
    border: {
      bottom: {
        style: BorderStyle.SINGLE,
        size: 8,
        color: "000000",
        space: 2,
      },
    },
    children: [tr(text.toUpperCase(), { bold: true, size: 24 })],
  });

const name = (text = "Prathick Dhanes R") =>
  new Paragraph({
    spacing: { before: 0, after: 40, ...FULL_LINE },
    children: [tr(text, { bold: true, size: 36 })],
  });

const linkRun = (label, url) =>
  new ExternalHyperlink({
    link: url,
    children: [
      tr(label, {
        color: LINK,
        underline: { type: UnderlineType.SINGLE },
      }),
    ],
  });

const linkRow = (items) => {
  const children = [];
  items.forEach((item, index) => {
    children.push(linkRun(item.label, item.url));
    if (index < items.length - 1) {
      children.push(tr("  •  ", { color: "666666" }));
    }
  });
  return new Paragraph({
    spacing: { before: 0, after: 160, ...FULL_LINE },
    children,
  });
};

const row = (left, right, opts = {}) =>
  new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: RIGHT_TAB }],
    spacing: { before: opts.before || 0, after: 0, ...FULL_LINE },
    children: [
      tr(left, { bold: true, size: 24 }),
      new TextRun({ text: "\t", size: 20, font: FONT }),
      tr(right, { color: GREY }),
    ],
  });

const sub = (left, right = "") =>
  new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: RIGHT_TAB }],
    spacing: { before: 0, after: 60, ...FULL_LINE },
    children: [
      tr(left, { italic: true, color: GREY }),
      new TextRun({ text: "\t", size: 20, font: FONT }),
      tr(right, { italic: true, color: GREY }),
    ],
  });

const p = (text, opts = {}) =>
  new Paragraph({
    spacing: {
      before: opts.before || 0,
      after: opts.after ?? 40,
      ...FULL_LINE,
    },
    children: [tr(text, { italic: opts.italic || false })],
  });

const b = (text) =>
  new Paragraph({
    numbering: { reference: "bullets", level: 0 },
    spacing: { before: 20, after: 20, ...FULL_LINE },
    children: [tr(text)],
  });

const sk = (label, value) =>
  new Paragraph({
    spacing: { before: 40, after: 40, ...FULL_LINE },
    children: [tr(`${label}: `, { bold: true }), tr(value)],
  });

const lnk = (label, url) =>
  new Paragraph({
    spacing: { before: 20, after: 20, ...FULL_LINE },
    children: [
      tr(`${label} `, { bold: true }),
      new ExternalHyperlink({
        link: url,
        children: [
          tr(url.replace("https://", ""), {
            color: LINK,
            underline: { type: UnderlineType.SINGLE },
          }),
        ],
      }),
    ],
  });

const gap = () =>
  new Paragraph({
    spacing: { before: 60, after: 0, ...FULL_LINE },
    children: [tr("")],
  });
```

## Document Skeleton

```js
const doc = new Document({
  numbering: {
    config: [
      {
        reference: "bullets",
        levels: [
          {
            level: 0,
            format: LevelFormat.BULLET,
            text: "-",
            alignment: AlignmentType.LEFT,
            style: {
              paragraph: { indent: { left: 360, hanging: 180 } },
            },
          },
        ],
      },
    ],
  },
  styles: {
    default: {
      document: {
        run: { font: FONT, size: 20 },
      },
    },
  },
  sections: [
    {
      properties: {
        page: {
          size: { width: 12240, height: 15840 },
          margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
        },
      },
      children: [
        name(),
        linkRow([
          { label: "LinkedIn", url: "https://www.linkedin.com/in/prathick-dhanes/" },
          { label: "GitHub", url: "https://github.com/peterish8" },
        ]),
        sec("Professional Summary"),
        p("Concise professional summary goes here.", { before: 80, after: 80 }),
        sec("Freelancing Experience"),
        row("Role / Project", "Date", { before: 80 }),
        sub("Stack / role details", "Location or live URL"),
        b("Strong result-oriented bullet with technologies and scope."),
        sec("Projects"),
        row("Project Name", "Date", { before: 80 }),
        sub("Stack", "Live link or platform"),
        b("Strong result-oriented bullet."),
        sec("Skills"),
        sk("Languages", "TypeScript, JavaScript, Dart, Python, Rust, SQL"),
      ],
    },
  ],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.writeFileSync("Prathick_Resume.docx", buffer);
});
```

## Content Rules

- Put project status/TODOs outside the resume.
- Bullets should start with strong verbs: Built, Delivered, Implemented, Designed, Created, Contributed.
- Avoid vague claims like “worked on” unless it is truly all that is known.
- Do not overclaim production, users, metrics, merges, or dates unless verified.
- For master resumes, include breadth. For one-page resumes, pick the strongest 4-6 projects and compress.
