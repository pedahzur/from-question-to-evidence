import fs from "node:fs";
import {
  AlignmentType,
  BorderStyle,
  Document,
  Footer,
  HeadingLevel,
  Packer,
  PageNumber,
  Paragraph,
  ShadingType,
  Table,
  TableCell,
  TableRow,
  TextRun,
  WidthType,
} from "docx";

const border = { style: BorderStyle.SINGLE, size: 4, color: "C8D5E1" };
const borders = { top: border, bottom: border, left: border, right: border };
const fields = [
  ["Current research question", ""],
  ["Research purpose", ""],
  ["Unit of inquiry", ""],
  ["Phenomenon", ""],
  ["Place or setting", ""],
  ["Period", ""],
  ["Actors and institutions", ""],
  ["What would count as an answer?", ""],
  ["This project does not attempt to", ""],
  ["Assumptions requiring examination", ""],
  ["Evidence required", ""],
  ["Version and date", ""],
];

const rows = fields.map(([label, value]) => new TableRow({
  height: { value: 620 },
  children: [
    new TableCell({
      borders,
      width: { size: 2800, type: WidthType.DXA },
      shading: { fill: "EAF2F8", type: ShadingType.CLEAR },
      margins: { top: 100, bottom: 100, left: 140, right: 140 },
      children: [new Paragraph({ children: [new TextRun({ text: label, bold: true, color: "16324F" })] })],
    }),
    new TableCell({
      borders,
      width: { size: 6560, type: WidthType.DXA },
      margins: { top: 100, bottom: 100, left: 140, right: 140 },
      children: [new Paragraph({ children: [new TextRun(value)] })],
    }),
  ],
}));

const document = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 34, bold: true, color: "16324F", font: "Arial" }, paragraph: { spacing: { before: 120, after: 180 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true, run: { size: 26, bold: true, color: "2F6690", font: "Arial" }, paragraph: { spacing: { before: 160, after: 100 }, outlineLevel: 1 } },
    ],
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1000, right: 1440, bottom: 1000, left: 1440 } } },
    footers: { default: new Footer({ children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new TextRun("From Question to Evidence  |  CC BY 4.0  |  Page "), new TextRun({ children: [PageNumber.CURRENT] })] })] }) },
    children: [
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Question-Framing Worksheet")] }),
      new Paragraph({ children: [new TextRun({ text: "Stage 1: Frame the Question", bold: true, color: "2F6690" })] }),
      new Paragraph({ spacing: { after: 220 }, children: [new TextRun("Complete this worksheet before broad collection begins. Revise by creating a new version rather than overwriting the reasoning behind the first frame.")] }),
      new Table({ width: { size: 9360, type: WidthType.DXA }, columnWidths: [2800, 6560], rows }),
      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("Integrity check")] }),
      new Paragraph("The frame should not expose participant identities, restricted archival information, or unpublished allegations. Record ethical limits alongside intellectual boundaries."),
      new Paragraph({ spacing: { before: 220 }, children: [new TextRun({ text: "Attribution: Ami Pedahzur and Jonathan Grossman, From Question to Evidence (discussion draft, 2026). Licensed CC BY 4.0.", italics: true, color: "52606D" })] }),
    ],
  }],
});

const buffer = await Packer.toBuffer(document);
fs.writeFileSync("templates/question-framing.docx", buffer);
