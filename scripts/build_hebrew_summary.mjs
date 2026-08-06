import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";

let docx;
try {
  docx = await import("docx");
} catch (error) {
  const modulesRoot = process.env.CODEX_NODE_MODULES;
  if (!modulesRoot) {
    throw error;
  }
  docx = await import(pathToFileURL(path.join(modulesRoot, "docx", "dist", "index.mjs")));
}

const {
  AlignmentType,
  Document,
  Footer,
  Packer,
  PageBreak,
  PageNumber,
  Paragraph,
  TextRun,
} = docx;

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const SOURCE = path.join(ROOT, "docs", "hebrew-five-page-summary-2026-08-06.md");
const OUTPUT = path.join(
  ROOT,
  "build-manuscript",
  "From-Question-to-Evidence-Hebrew-Five-Page-Summary.docx",
);

const colors = {
  ink: "17212B",
  accent: "356B73",
  muted: "66727C",
};

function parsePages(markdown) {
  const body = markdown.replace(/^---[\s\S]*?---\s*/, "");
  const pageChunks = body.split(/<div style="page-break-after: always;"><\/div>/);

  return pageChunks.map((chunk) => {
    const lines = chunk
      .replace(/<\/?div[^>]*>/g, "")
      .split("\n")
      .map((line) => line.trim());
    const headingIndex = lines.findIndex((line) => line.startsWith("### עמוד "));
    if (headingIndex === -1) {
      throw new Error("Every summary page must begin with a numbered page heading.");
    }
    return {
      heading: lines[headingIndex].replace(/^###\s+/, ""),
      paragraphs: lines.slice(headingIndex + 1).filter(Boolean),
    };
  });
}

function inlineRuns(text, options = {}) {
  const runs = [];
  const pattern = /\*\*([^*]+)\*\*|\*([^*]+)\*/g;
  let cursor = 0;
  let match;
  while ((match = pattern.exec(text)) !== null) {
    if (match.index > cursor) {
      runs.push(new TextRun({
        text: text.slice(cursor, match.index),
        rightToLeft: true,
        ...options,
      }));
    }
    runs.push(new TextRun({
      text: match[1] ?? match[2],
      bold: Boolean(match[1]),
      italics: Boolean(match[2]),
      rightToLeft: true,
      ...options,
    }));
    cursor = pattern.lastIndex;
  }
  if (cursor < text.length) {
    runs.push(new TextRun({
      text: text.slice(cursor),
      rightToLeft: true,
      ...options,
    }));
  }
  return runs;
}

function rtlParagraph(text) {
  return new Paragraph({
    alignment: AlignmentType.JUSTIFIED,
    bidirectional: true,
    spacing: { before: 0, after: 72, line: 264 },
    widowControl: false,
    children: inlineRuns(text, { font: "Arial", size: 22, color: colors.ink }),
  });
}

function pageHeading(text) {
  return new Paragraph({
    alignment: AlignmentType.RIGHT,
    bidirectional: true,
    keepNext: true,
    spacing: { before: 0, after: 150, line: 300 },
    children: [new TextRun({
      text,
      bold: true,
      rightToLeft: true,
      font: "Arial",
      size: 31,
      color: colors.accent,
    })],
  });
}

function titleBlock() {
  return [
    new Paragraph({
      alignment: AlignmentType.RIGHT,
      bidirectional: true,
      keepNext: true,
      spacing: { before: 0, after: 45, line: 430 },
      children: [new TextRun({
        text: "משאלת מחקר לראיות",
        bold: true,
        rightToLeft: true,
        font: "Arial",
        size: 48,
        color: colors.ink,
      })],
    }),
    new Paragraph({
      alignment: AlignmentType.RIGHT,
      bidirectional: true,
      keepNext: true,
      spacing: { before: 0, after: 210, line: 300 },
      children: [new TextRun({
        text: "תקציר נגיש לסטודנטים לתואר ראשון",
        rightToLeft: true,
        font: "Arial",
        size: 24,
        color: colors.muted,
      })],
    }),
  ];
}

const pages = parsePages(fs.readFileSync(SOURCE, "utf8"));
if (pages.length !== 5) {
  throw new Error(`Expected five pages, found ${pages.length}.`);
}

const children = [];
pages.forEach((page, index) => {
  if (index === 0) {
    children.push(...titleBlock());
  }
  children.push(pageHeading(page.heading));
  children.push(...page.paragraphs.map(rtlParagraph));
  if (index < pages.length - 1) {
    children.push(new Paragraph({ children: [new PageBreak()] }));
  }
});

const document = new Document({
  creator: "Ami Pedahzur and Jonathan Grossman",
  title: "משאלת מחקר לראיות — תקציר בן חמישה עמודים",
  description: "תקציר בעברית מודרנית ונגישה לסטודנטים לתואר ראשון",
  styles: {
    default: {
      document: {
        run: { font: "Arial", size: 22, color: colors.ink, rightToLeft: true },
        paragraph: { spacing: { before: 0, after: 72, line: 264 } },
      },
    },
  },
  sections: [{
    properties: {
      page: {
        size: { width: 11906, height: 16838 },
        margin: {
          top: 850,
          right: 1000,
          bottom: 850,
          left: 1000,
          header: 425,
          footer: 425,
        },
      },
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 0 },
          children: [
            new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 17, color: colors.muted }),
            new TextRun({ text: " / ", font: "Arial", size: 17, color: colors.muted }),
            new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Arial", size: 17, color: colors.muted }),
          ],
        })],
      }),
    },
    children,
  }],
});

fs.mkdirSync(path.dirname(OUTPUT), { recursive: true });
const buffer = await Packer.toBuffer(document);
fs.writeFileSync(OUTPUT, buffer);
console.log(OUTPUT);
