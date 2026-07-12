import fs from "node:fs/promises";
import path from "node:path";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outputDir = path.resolve("templates");
const previewDir = path.resolve("../temp/template-previews");
await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(previewDir, { recursive: true });

const palette = {
  navy: "#16324F",
  blue: "#2F6690",
  pale: "#EAF2F8",
  line: "#C8D5E1",
  text: "#1F2933",
};

const workbooks = [
  {
    file: "concept-context-grid.xlsx",
    sheets: [
      {
        name: "Concept Grid",
        title: "Concept and Context Grid",
        headers: ["ID", "Concept or Context", "Working Meaning", "Alternative Meanings", "Actor Vocabulary", "Observable Traces", "Rival Explanation", "Exclusion or Boundary", "Notes"],
      },
    ],
  },
  {
    file: "source-family-inventory.xlsx",
    sheets: [
      {
        name: "Source Families",
        title: "Source-Family Inventory",
        headers: ["Family ID", "Source Family", "Linked Concept IDs", "Creator or Institution", "Purpose of Record", "Temporal Coverage", "Location or Repository", "Language", "Access Status", "Likely Silences", "Dependence on Other Families", "Next Action"],
      },
    ],
  },
  {
    file: "search-ai-audit-log.xlsx",
    sheets: [
      {
        name: "Search Log",
        title: "Search Log",
        headers: ["Cycle ID", "Date", "Purpose", "System or Route", "Exact Terms", "Filters", "Results Retained", "New Vocabulary", "Decision", "Next Step"],
      },
      {
        name: "AI Audit",
        title: "AI Assistance Audit",
        headers: ["Entry ID", "Date", "Model and Version", "Research Task", "Input Description", "Protected Data Included?", "Output Summary", "Accepted Suggestions", "Rejected Suggestions", "Verification", "Reviewer", "Decision"],
      },
    ],
  },
  {
    file: "evidence-map-stopping-rule.xlsx",
    sheets: [
      {
        name: "Evidence Map",
        title: "Evidence Map",
        headers: ["Cell ID", "Question Dimension", "Source Family", "Evidence Record IDs", "Coverage Status", "Source Diversity", "Dependence Risk", "Contradiction", "Claim Supported", "Limits", "Last Reviewed"],
      },
      {
        name: "Gap Analysis",
        title: "Gap Analysis",
        headers: ["Gap ID", "Evidence Map Cell", "Gap Type", "Importance", "Consequence for Claim", "Access or Ethical Constraint", "Proposed Action", "Owner", "Review Date", "Status"],
      },
      {
        name: "Collection Plan",
        title: "Collection Plan",
        headers: ["Action ID", "Gap ID", "Action", "Reason", "Source Family", "Owner", "Priority", "Target Date", "Completion Evidence", "Status"],
      },
      {
        name: "Stopping Rule",
        title: "Stopping Rule",
        headers: ["Criterion", "Required Evidence", "Current Assessment", "Unresolved Limit", "Decision", "Reopen Trigger"],
      },
    ],
  },
];

function addDataSheet(workbook, spec) {
  const sheet = workbook.worksheets.add(spec.name);
  const lastColumn = String.fromCharCode(64 + spec.headers.length);
  sheet.showGridLines = false;
  sheet.mergeCells(`A1:${lastColumn}1`);
  sheet.getRange("A1").values = [[spec.title]];
  sheet.getRange("A1").format = {
    fill: palette.navy,
    font: { bold: true, color: "#FFFFFF", size: 16 },
    rowHeight: 30,
    verticalAlignment: "center",
  };
  sheet.getRange(`A2:${lastColumn}2`).values = [spec.headers];
  sheet.getRange(`A2:${lastColumn}2`).format = {
    fill: palette.blue,
    font: { bold: true, color: "#FFFFFF" },
    wrapText: true,
    rowHeight: 32,
    borders: { preset: "outside", style: "thin", color: palette.line },
  };
  sheet.getRange(`A3:${lastColumn}20`).format = {
    fill: "#FFFFFF",
    font: { color: palette.text },
    wrapText: true,
    verticalAlignment: "top",
    borders: { insideHorizontal: { style: "thin", color: palette.line } },
  };
  sheet.getRange(`A1:${lastColumn}20`).format.columnWidth = 18;
  sheet.getRange("A:A").format.columnWidth = 12;
  sheet.freezePanes.freezeRows(2);
  sheet.freezePanes.freezeColumns(1);
  if (spec.headers.includes("Status")) {
    const col = String.fromCharCode(65 + spec.headers.indexOf("Status"));
    sheet.getRange(`${col}3:${col}100`).dataValidation = { rule: { type: "list", values: ["Not Started", "In Progress", "Blocked", "Complete"] } };
  }
  if (spec.headers.includes("Priority")) {
    const col = String.fromCharCode(65 + spec.headers.indexOf("Priority"));
    sheet.getRange(`${col}3:${col}100`).dataValidation = { rule: { type: "list", values: ["High", "Medium", "Low"] } };
  }
}

function addInstructions(workbook, names) {
  const sheet = workbook.worksheets.add("Instructions");
  sheet.showGridLines = false;
  sheet.getRange("A1:B7").values = [
    ["From Question to Evidence", "Workbook Instructions"],
    ["Purpose", `Use the ${names.join(", ")} sheet${names.length > 1 ? "s" : ""} while completing the corresponding field-guide stage.`],
    ["Method", "Create stable IDs, record decisions as they occur, and preserve earlier versions when the question changes."],
    ["AI", "Record consequential AI assistance in the AI Audit sheet or linked project log. Verify every proposed source independently."],
    ["Privacy", "Do not enter protected participant data or restricted archival information into an external AI service."],
    ["License", "CC BY 4.0. Attribution: Ami Pedahzur and Jonathan Grossman, From Question to Evidence (2026)."],
    ["Version", "0.1 discussion draft, 2026-07-12"],
  ];
  sheet.getRange("A1:B1").format = { fill: palette.navy, font: { bold: true, color: "#FFFFFF", size: 15 }, rowHeight: 28 };
  sheet.getRange("A2:A7").format = { fill: palette.pale, font: { bold: true, color: palette.navy } };
  sheet.getRange("A1:B7").format.wrapText = true;
  sheet.getRange("A:A").format.columnWidth = 16;
  sheet.getRange("B:B").format.columnWidth = 72;
  sheet.getRange("A2:B7").format.rowHeight = 34;
}

for (const spec of workbooks) {
  const workbook = Workbook.create();
  for (const sheetSpec of spec.sheets) addDataSheet(workbook, sheetSpec);
  addInstructions(workbook, spec.sheets.map((sheet) => sheet.name));
  const exported = await SpreadsheetFile.exportXlsx(workbook);
  await exported.save(path.join(outputDir, spec.file));
  for (const sheetSpec of spec.sheets) {
    const preview = await workbook.render({ sheetName: sheetSpec.name, range: `A1:${String.fromCharCode(64 + sheetSpec.headers.length)}8`, scale: 1.2, format: "png" });
    await fs.writeFile(path.join(previewDir, `${spec.file}-${sheetSpec.name.replaceAll(" ", "-")}.png`), new Uint8Array(await preview.arrayBuffer()));
  }
  const inspection = await workbook.inspect({ kind: "sheet,table", maxChars: 1800, tableMaxRows: 4, tableMaxCols: 8 });
  console.log(`${spec.file}: ${inspection.ndjson}`);
}
