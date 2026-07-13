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

// Design preset: compact_reference_guide, with a form-layout override.
const colors = {
  navy: "16324F",
  blue: "2F6690",
  pale: "EAF2F8",
  line: "C8D5E1",
  muted: "52606D",
};
const border = { style: BorderStyle.SINGLE, size: 4, color: colors.line };
const borders = { top: border, bottom: border, left: border, right: border };

function fieldRow(label, guidance) {
  return new TableRow({
    children: [
      new TableCell({
        borders,
        width: { size: 2600, type: WidthType.DXA },
        shading: { fill: colors.pale, type: ShadingType.CLEAR },
        margins: { top: 120, bottom: 120, left: 140, right: 140 },
        verticalAlign: "center",
        children: [new Paragraph({
          spacing: { before: 0, after: 0, line: 300 },
          children: [new TextRun({ text: label, bold: true, color: colors.navy })],
        })],
      }),
      new TableCell({
        borders,
        width: { size: 6760, type: WidthType.DXA },
        margins: { top: 120, bottom: 120, left: 140, right: 140 },
        children: [
          new Paragraph({
            spacing: { before: 0, after: 80, line: 300 },
            children: [new TextRun({ text: guidance, italics: true, color: colors.muted })],
          }),
          new Paragraph({ spacing: { before: 0, after: 80, line: 300 }, children: [new TextRun(" ")] }),
        ],
      }),
    ],
  });
}

function fieldTable(fields) {
  return new Table({
    width: { size: 9360, type: WidthType.DXA },
    columnWidths: [2600, 6760],
    rows: fields.map(([label, guidance]) => fieldRow(label, guidance)),
  });
}

function sectionHeading(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    keepNext: true,
    children: [new TextRun(text)],
  });
}

const identityFields = [
  ["Project and review ID", "Use stable identifiers that connect this protocol to the evidence map and project log."],
  ["Review question", "Write the question this review must answer, not only the topic."],
  ["Review purpose", "Identify the leading function: conceptual, theoretical, empirical, methodological, or orienting."],
  ["Anticipated product", "State format, audience, approximate length, deadline, and collaborators."],
  ["Version and date", "Create a new version when scope or decision rules change."],
];

const boundaryFields = [
  ["Substantive boundaries", "Record period, setting, population, cases, disciplines, and publication types justified by the question."],
  ["Inclusion logic", "Complete: A work belongs when..."],
  ["Exclusion logic", "Complete: A work remains outside when..."],
  ["Languages", "List languages searched, translation capacity, and known language exclusions."],
  ["Practical constraints", "Separate time, access, and resource limits from substantive exclusions."],
  ["Ethical constraints", "Record restrictions required by privacy, confidentiality, copyright, or participant protection."],
];

const workflowFields = [
  ["Discovery routes", "List databases, catalogues, citation chains, authors, institutions, venues, repositories, and web routes to attempt."],
  ["Full-text threshold", "State when a candidate must be read in full and when targeted reading is adequate."],
  ["AI permitted input", "Describe public or non-sensitive material approved for model assistance."],
  ["AI prohibited input", "Describe confidential, copyrighted, restricted, or identifiable material that must not enter external systems."],
  ["Verification rule", "State how citations, quotations, classifications, and AI outputs will be checked."],
  ["Audit record", "Identify which search and AI decisions are material enough to preserve."],
];

const completionFields = [
  ["Expected synthesis", "State whether the product is a taxonomy, comparison, lineage, methodological account, or another form."],
  ["Initial stopping rule", "Complete: The review is adequate for its present purpose when..."],
  ["Unresolved limits", "Name known gaps, inaccessible materials, and weakly covered perspectives."],
  ["Reopening trigger", "List evidence or changes that would justify another search and reading cycle."],
  ["Review and approval", "Record author, reviewer, decision date, and approved version."],
];

const document = new Document({
  styles: {
    default: {
      document: {
        run: { font: "Calibri", size: 22, color: "1F2933" },
        paragraph: { spacing: { before: 0, after: 120, line: 300 } },
      },
    },
    paragraphStyles: [
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 32, bold: true, color: colors.navy, font: "Calibri" },
        paragraph: { spacing: { before: 360, after: 200, line: 300 }, outlineLevel: 0 },
      },
      {
        id: "Heading2",
        name: "Heading 2",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 26, bold: true, color: colors.blue, font: "Calibri" },
        paragraph: { spacing: { before: 280, after: 140, line: 300 }, outlineLevel: 1 },
      },
    ],
  },
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440, header: 708, footer: 708 },
      },
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 0, after: 0 },
          children: [
            new TextRun({ text: "From Question to Evidence  |  CC BY 4.0  |  Page ", color: colors.muted, size: 18 }),
            new TextRun({ children: [PageNumber.CURRENT], color: colors.muted, size: 18 }),
          ],
        })],
      }),
    },
    children: [
      new Paragraph({
        spacing: { before: 0, after: 60, line: 300 },
        children: [new TextRun({ text: "Literature Review Protocol", bold: true, size: 44, color: colors.navy })],
      }),
      new Paragraph({
        spacing: { before: 0, after: 260, line: 300 },
        children: [new TextRun({ text: "Literature as Evidence - Stage 1", bold: true, size: 24, color: colors.blue })],
      }),
      new Paragraph({
        spacing: { before: 0, after: 240, line: 300 },
        children: [new TextRun("Define the review before broad discovery begins. Preserve earlier versions when the question, scope, or decision rules change.")],
      }),
      sectionHeading("Review identity and purpose"),
      fieldTable(identityFields),
      sectionHeading("Boundaries and decision rules"),
      fieldTable(boundaryFields),
      sectionHeading("Discovery, AI, and verification"),
      fieldTable(workflowFields),
      sectionHeading("Synthesis and completion"),
      fieldTable(completionFields),
      sectionHeading("Integrity check"),
      new Paragraph("Do not hide practical exclusions inside substantive criteria. Do not enter confidential, restricted, or identifiable material into an external AI system. Record access limits and uncertainty without converting them into claims of scholarly absence."),
      new Paragraph({
        spacing: { before: 240, after: 0, line: 300 },
        children: [new TextRun({
          text: "Attribution: Ami Pedahzur and Jonathan Grossman, From Question to Evidence (discussion draft, 2026). Licensed CC BY 4.0.",
          italics: true,
          color: colors.muted,
        })],
      }),
    ],
  }],
});

const buffer = await Packer.toBuffer(document);
fs.writeFileSync("templates/literature-review-protocol.docx", buffer);
