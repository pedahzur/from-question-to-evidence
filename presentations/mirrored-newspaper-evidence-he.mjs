import fs from "node:fs/promises";
import path from "node:path";
import { Presentation, PresentationFile } from "@oai/artifact-tool";

const W = 1280;
const H = 720;
const C = {
  paper: "#F7F4EE",
  ink: "#18212B",
  muted: "#66717D",
  line: "#C9C3B8",
  teal: "#177E89",
  tealPale: "#DDEFF0",
  rust: "#B85C38",
  rustPale: "#F3E1D8",
  gold: "#D6A84B",
  white: "#FFFFFF",
};

function rect(slide, x, y, w, h, fill = C.white, line = C.line, radius = "rounded-xl", name = "panel") {
  return slide.shapes.add({
    geometry: radius ? "roundRect" : "rect",
    name,
    position: { left: x, top: y, width: w, height: h },
    fill,
    line: { style: "solid", fill: line, width: 1 },
    ...(radius ? { borderRadius: radius } : {}),
  });
}

function rule(slide, x, y, w, color = C.line, width = 1, name = "rule") {
  return slide.shapes.add({
    geometry: "straightConnector1",
    name,
    position: { left: x, top: y, width: w, height: 0 },
    fill: "none",
    line: { style: "solid", fill: color, width },
  });
}

function addText(slide, value, x, y, w, h, options = {}) {
  const box = slide.shapes.add({
    geometry: "textbox",
    name: options.name || "text",
    position: { left: x, top: y, width: w, height: h },
    fill: "none",
    line: { style: "solid", fill: "none", width: 0 },
  });
  const displayValue = /[\u0590-\u05FF]/.test(value)
    ? value.split("\n").map((line) => `\u202B${line}\u202C`).join("\n")
    : value;
  box.text = displayValue;
  box.text.style = {
    fontSize: options.size || 24,
    typeface: options.font || "Arial",
    color: options.color || C.ink,
    bold: options.bold || false,
    alignment: options.align || "right",
    verticalAlignment: options.valign || "top",
    autoFit: options.autoFit || "shrinkText",
    insets: options.insets || { top: 0, right: 0, bottom: 0, left: 0 },
  };
  return box;
}

function addTitle(slide, title, number, kicker = "FROM QUESTION TO EVIDENCE") {
  addText(slide, kicker, 48, 34, 470, 28, {
    size: 14,
    bold: true,
    color: C.teal,
    align: "left",
    name: "kicker",
  });
  addText(slide, title, 560, 32, 672, 72, {
    size: 34,
    bold: true,
    align: "right",
    name: "slide-title",
  });
  rule(slide, 48, 116, 1184, C.line, 1, "title-rule");
  addText(slide, String(number).padStart(2, "0"), 1184, 670, 48, 22, {
    size: 12,
    color: C.muted,
    align: "right",
    name: "slide-number",
  });
}

function notes(slide, urls, extra = "") {
  const block = [
    extra,
    "[Sources]",
    ...urls.map((url) => `- ${url}`),
    "[/Sources]",
  ].filter(Boolean).join("\n");
  slide.speakerNotes.textFrame.setText(block);
  slide.speakerNotes.setVisible(true);
}

function addPill(slide, label, x, y, w, fill, color = C.ink) {
  rect(slide, x, y, w, 38, fill, fill, "rounded-xl", `pill-${label}`);
  addText(slide, label, x + 12, y + 7, w - 24, 24, {
    size: 16,
    bold: true,
    color,
    align: "center",
    name: `pill-label-${label}`,
  });
}

function buildDeck() {
  const deck = Presentation.create({ slideSize: { width: W, height: H } });

  // 1. Cover
  {
    const s = deck.slides.add();
    s.background.fill = C.paper;
    rect(s, 48, 48, 10, 624, C.teal, C.teal, null, "accent-bar");
    addText(s, "שיטת תמונת־הראי", 300, 158, 900, 100, {
      size: 54,
      bold: true,
      align: "right",
      name: "cover-title",
    });
    addText(s, "מחיפוש רב־לשוני לראיה היסטורית ניתנת לבדיקה", 355, 282, 845, 88, {
      size: 29,
      color: C.muted,
      align: "right",
      name: "cover-subtitle",
    });
    addPill(s, "עיתונות עברית + ערבית", 906, 425, 294, C.tealPale, C.teal);
    addPill(s, "בינה מלאכותית בפיקוח חוקר", 596, 425, 286, C.rustPale, C.rust);
    addText(s, "מקרה פיילוט: פלוגות השדה ופלגות הלילה המיוחדות, 1938", 480, 536, 720, 54, {
      size: 20,
      bold: true,
      align: "right",
    });
    addText(s, "עמי פדהצור · יולי 2026", 72, 640, 360, 28, {
      size: 15,
      color: C.muted,
      align: "right",
    });
    notes(s, [
      "https://github.com/pedahzur/from-question-to-evidence",
      "https://www.nli.org.il/he/newspapers/titles?lang=%D7%A2%D7%A8%D7%91%D7%99%D7%AA",
    ]);
  }

  // 2. Research problem
  {
    const s = deck.slides.add();
    s.background.fill = C.paper;
    addTitle(s, "הבעיה: שני ארכיונים, לא שאילתה אחת", 2);
    rect(s, 680, 160, 552, 430, C.white, C.line, "rounded-xl", "hebrew-archive");
    rect(s, 48, 160, 552, 430, C.white, C.line, "rounded-xl", "arabic-archive");
    addPill(s, "העיתונות העברית", 988, 184, 220, C.tealPale, C.teal);
    addPill(s, "העיתונות הערבית", 356, 184, 220, C.rustPale, C.rust);
    addText(s, "שמות הארגונים", 722, 264, 450, 40, { size: 26, bold: true });
    addText(s, "מנהיגות · דוקטרינה · משמעת\nניידות · מסורת ארגונית", 722, 322, 450, 112, {
      size: 23,
      color: C.muted,
    });
    addText(s, "מקומות ותוצאות", 90, 264, 450, 40, { size: 26, bold: true });
    addText(s, "ירי · נפגעים · כיתור\nחיפושים · מעצרים · תנועה", 90, 322, 450, 112, {
      size: 23,
      color: C.muted,
    });
    rule(s, 560, 388, 160, C.gold, 4, "bridge");
    addText(s, "הגשר: אירוע", 541, 416, 198, 34, {
      size: 20,
      bold: true,
      color: C.gold,
      align: "center",
    });
    addText(s, "כשל בשם אינו היעדר במציאות", 328, 624, 624, 38, {
      size: 25,
      bold: true,
      color: C.ink,
      align: "center",
    });
    notes(s, [
      "https://github.com/pedahzur/from-question-to-evidence/blob/codex/mirrored-newspaper-evidence/content/10-mirrored-newspaper-evidence.qmd",
    ]);
  }

  // 3. Pilot evidence
  {
    const s = deck.slides.add();
    s.background.fill = C.paper;
    addTitle(s, "מה הפיילוט יצר", 3);
    addText(s, "המספרים מתארים חבילת שחזור, לא מדגם מייצג של העיתונות הערבית.", 256, 142, 976, 48, {
      size: 20,
      color: C.muted,
    });
    const stats = [
      ["16", "שאילתות מתועדות", C.tealPale, C.teal],
      ["11", "רשומות עיתונות ערביות", C.rustPale, C.rust],
      ["6", "שורות הצלבת אירועים", "#EEE8D8", "#8A6A20"],
    ];
    stats.forEach(([n, label, fill, color], i) => {
      const x = 864 - i * 408;
      rect(s, x, 244, 368, 280, fill, fill, "rounded-xl", `stat-${i}`);
      addText(s, n, x + 30, 286, 308, 104, {
        size: 72,
        bold: true,
        color,
        align: "center",
        valign: "middle",
      });
      addText(s, label, x + 30, 416, 308, 52, {
        size: 23,
        bold: true,
        color: C.ink,
        align: "center",
      });
    });
    addText(s, "נשמרו גם חיפושי אפס, תוצאות שגויות ומקורות תלויי־דיווח.", 248, 588, 984, 52, {
      size: 23,
      bold: true,
    });
    notes(s, [
      "https://github.com/pedahzur/from-question-to-evidence/tree/codex/mirrored-newspaper-evidence/examples/mirrored-newspaper-evidence",
    ]);
  }

  // 4. Eight-step workflow
  {
    const s = deck.slides.add();
    s.background.fill = C.paper;
    addTitle(s, "שמונה החלטות שמותירות מסלול בדיקה", 4);
    const steps = [
      ["1", "תחימת השאלה"],
      ["2", "אוצר מילים רב־לשוני"],
      ["3", "שמירת חיפושים שנכשלו"],
      ["4", "מעבר מארגון לאירוע"],
      ["5", "אימות OCR מול הסריקה"],
      ["6", "סיווג מקור המידע"],
      ["7", "הצלבת אירועים"],
      ["8", "כלל עצירה ופתיחה מחדש"],
    ];
    steps.forEach(([num, label], i) => {
      const col = i % 4;
      const row = Math.floor(i / 4);
      const x = 960 - col * 302;
      const y = 160 + row * 216;
      rect(s, x, y, 272, 168, C.white, C.line, "rounded-xl", `step-${num}`);
      addText(s, num, x + 188, y + 20, 56, 48, {
        size: 30,
        bold: true,
        color: row === 0 ? C.teal : C.rust,
        align: "center",
      });
      addText(s, label, x + 24, y + 82, 220, 58, {
        size: 21,
        bold: true,
        align: "right",
        valign: "middle",
      });
    });
    notes(s, [
      "https://github.com/pedahzur/from-question-to-evidence/blob/codex/mirrored-newspaper-evidence/content/10-mirrored-newspaper-evidence.qmd",
    ]);
  }

  // 5. Search pivot
  {
    const s = deck.slides.add();
    s.background.fill = C.paper;
    addTitle(s, "נקודת המפנה: מן היחידה אל הזירה", 5);
    rule(s, 196, 345, 888, C.gold, 3, "search-line");
    const nodes = [
      [938, "שמות יחידות", "0 תוצאות שימושיות", C.rustPale, C.rust],
      [662, "שמות אנשים", "ממצא מכריע אחד", "#EEE8D8", "#8A6A20"],
      [386, "מקומות ותשתית", "221 תוצאות לצינור", C.tealPale, C.teal],
      [110, "פרטי פעולה", "אירועים בני־השוואה", C.white, C.ink],
    ];
    nodes.forEach(([x, title, body, fill, color], i) => {
      rect(s, x, 250, 232, 190, fill, color, "rounded-xl", `pivot-${i}`);
      addText(s, String(i + 1), x + 82, 272, 68, 48, {
        size: 27,
        bold: true,
        color,
        align: "center",
      });
      addText(s, title, x + 18, 328, 196, 34, {
        size: 20,
        bold: true,
        align: "center",
      });
      addText(s, body, x + 18, 374, 196, 42, {
        size: 17,
        color: C.muted,
        align: "center",
      });
    });
    addText(s, "חיפוש שנכשל משנה את אסטרטגיית האיסוף. הוא אינו נמחק מן התיעוד.", 190, 514, 900, 70, {
      size: 26,
      bold: true,
      align: "center",
    });
    notes(s, [
      "https://github.com/pedahzur/from-question-to-evidence/blob/codex/mirrored-newspaper-evidence/examples/mirrored-newspaper-evidence/search-log.csv",
    ]);
  }

  // 6. Source provenance
  {
    const s = deck.slides.add();
    s.background.fill = C.paper;
    addTitle(s, "אין ״קול ערבי״ אחד: מסווגים את שרשרת המידע", 6);
    const rows = [
      ["דיווח מקומי", "כתב או שליח של העיתון", "יכול לתמוך בתצפית מקומית", C.tealPale],
      ["הודעה רשמית", "משטרה, ביטחון או ממשלה", "תומכת במה שהמוסד פרסם", "#EEE8D8"],
      ["דיווח תלוי", "סיכום עיתון עברי או מקור אחר", "מלמד על מעבר המידע, לא על עצמאותו", C.rustPale],
    ];
    addText(s, "מה מותר לטעון?", 48, 166, 300, 36, { size: 18, bold: true, color: C.muted, align: "left" });
    addText(s, "מאין הגיע המידע?", 492, 166, 300, 36, { size: 18, bold: true, color: C.muted, align: "center" });
    addText(s, "סוג הרשומה", 972, 166, 260, 36, { size: 18, bold: true, color: C.muted });
    rows.forEach(([kind, origin, claim, fill], i) => {
      const y = 222 + i * 132;
      rect(s, 48, y, 1184, 108, fill, fill, "rounded-xl", `provenance-${i}`);
      addText(s, claim, 76, y + 26, 372, 58, { size: 20, bold: true, align: "left" });
      addText(s, origin, 492, y + 26, 300, 58, { size: 20, align: "center" });
      addText(s, kind, 926, y + 26, 278, 58, { size: 22, bold: true });
    });
    notes(s, [
      "https://github.com/pedahzur/from-question-to-evidence/blob/codex/mirrored-newspaper-evidence/examples/mirrored-newspaper-evidence/source-manifest.csv",
      "https://impresso-project.ch/datalab/notebooks/newsagency-processing-with-impresso-hf/",
    ]);
  }

  // 7. Event crosswalk example
  {
    const s = deck.slides.add();
    s.background.fill = C.paper;
    addTitle(s, "דוגמה: דבוריה, 11 ביולי 1938", 7);
    rule(s, 156, 348, 968, C.gold, 4, "event-link");
    rect(s, 756, 178, 476, 340, C.tealPale, C.teal, "rounded-xl", "hebrew-frame");
    rect(s, 48, 178, 476, 340, C.rustPale, C.rust, "rounded-xl", "arabic-frame");
    addText(s, "מסגרת עברית", 800, 212, 388, 42, { size: 25, bold: true, color: C.teal });
    addText(s, "וינגייט כמארגן שיטה\nכוח מעורב\nמשמעת ותנועה בלילה", 800, 292, 388, 144, {
      size: 24,
      bold: true,
      color: C.ink,
    });
    addText(s, "מסגרת ערבית", 92, 212, 388, 42, { size: 25, bold: true, color: C.rust });
    addText(s, "נפגעים מקומיים\nכיתור הכפר\nחיפושים בבתים", 92, 292, 388, 144, {
      size: 24,
      bold: true,
      color: C.ink,
    });
    rect(s, 526, 272, 228, 152, C.white, C.gold, "rounded-xl", "match-box");
    addText(s, "התאמה מאומתת", 548, 296, 184, 38, {
      size: 21,
      bold: true,
      color: "#8A6A20",
      align: "center",
    });
    addText(s, "תאריך + מקום\n+ 5 פרטים משותפים", 548, 350, 184, 56, {
      size: 17,
      align: "center",
      color: C.muted,
    });
    addText(s, "אותו אירוע. זווית תצפית ושרשרת מידע שונות.", 226, 570, 828, 48, {
      size: 26,
      bold: true,
      align: "center",
    });
    notes(s, [
      "https://www.nli.org.il/he/newspapers/?a=d&d=falastin19380712-01.2.5",
      "https://www.nli.org.il/he/newspapers/?a=d&d=falastin19380712-01.2.19",
      "https://www.nli.org.il/he/newspapers/?a=d&d=difaa19380712-01.2.102",
    ]);
  }

  // 8. AI and human gates
  {
    const s = deck.slides.add();
    s.background.fill = C.paper;
    addTitle(s, "חלוקת העבודה: המכונה מציעה, החוקר מכריע", 8);
    const xs = [1046, 798, 550, 302, 54];
    xs.slice(0, -1).forEach((x, i) => {
      const leftX = xs[i + 1];
      rule(s, leftX + 184, 337, x - (leftX + 184), C.line, 2, `connector-${i}`);
    });
    const boxes = [
      ["הרחבת כתיבים", "AI", C.tealPale, C.teal],
      ["מיון OCR", "AI", C.tealPale, C.teal],
      ["הצעת התאמה", "AI", C.tealPale, C.teal],
      ["בדיקת סריקה", "חוקר", C.rustPale, C.rust],
      ["טענה ודרגת ביטחון", "חוקר", C.rustPale, C.rust],
    ];
    boxes.forEach(([label, who, fill, color], i) => {
      const x = xs[i];
      rect(s, x, 248, 184, 180, fill, color, "rounded-xl", `gate-${i}`);
      addText(s, who, x + 22, 270, 140, 32, {
        size: 17,
        bold: true,
        color,
        align: "center",
      });
      addText(s, label, x + 18, 328, 148, 68, {
        size: 20,
        bold: true,
        align: "center",
        valign: "middle",
      });
    });
    addText(s, "המודל אינו קובע זהות אירוע, אינו משלים טקסט חסר ואינו מסיק היעדר מחיפוש אפס.", 156, 514, 968, 88, {
      size: 25,
      bold: true,
      align: "center",
    });
    notes(s, [
      "https://doi.org/10.1140/epjds/s13688-025-00548-8",
      "https://doi.org/10.1177/00491241251339188",
      "https://doi.org/10.1177/0049124117729703",
    ]);
  }

  // 9. Related approaches
  {
    const s = deck.slides.add();
    s.background.fill = C.paper;
    addTitle(s, "היכן השיטה יושבת ביחס לגישות קיימות", 9);
    const items = [
      ["Collections as Data", "מקור, זכויות, היעדר ותיעוד"],
      ["Environmental Scan", "הטיות וכיסוי של מאגר היסטורי"],
      ["Impresso", "עיתונות רב־לשונית ו־OCR"],
      ["Computational Grounded Theory", "גילוי, קריאה ואישור"],
      ["LLM-assisted coding", "קודבוק ואימות מול תקן אנושי"],
      ["ASReview", "מיון מועמדים וכלל עצירה"],
    ];
    items.forEach(([name, desc], i) => {
      const col = i % 2;
      const row = Math.floor(i / 2);
      const x = col === 0 ? 656 : 48;
      const y = 160 + row * 154;
      rect(s, x, y, 576, 126, C.white, C.line, "rounded-xl", `approach-${i}`);
      addText(s, name, x + 248, y + 24, 300, 36, { size: 20, bold: true });
      addText(s, desc, x + 24, y + 70, 524, 34, { size: 18, color: C.muted });
      rect(s, x + 24, y + 24, 10, 80, i < 3 ? C.teal : C.rust, i < 3 ? C.teal : C.rust, null, `approach-mark-${i}`);
    });
    addText(s, "התרומה היא אינטגרציה סביב אירוע שנוי במחלוקת, לא אלגוריתם חדש.", 178, 630, 924, 42, {
      size: 25,
      bold: true,
      align: "center",
    });
    notes(s, [
      "https://collectionsasdata.github.io/statement/",
      "https://doi.org/10.1017/chr.2025.10007",
      "https://impresso-project.ch/project/objectives/",
      "https://doi.org/10.1177/0049124117729703",
      "https://doi.org/10.1140/epjds/s13688-025-00548-8",
      "https://doi.org/10.1038/s42256-020-00287-7",
    ]);
  }

  // 10. Contribution and limits
  {
    const s = deck.slides.add();
    s.background.fill = C.paper;
    addTitle(s, "מה השיטה מאפשרת, ומה עדיין דורש בדיקה", 10);
    rect(s, 680, 166, 552, 388, C.tealPale, C.teal, "rounded-xl", "contribution");
    rect(s, 48, 166, 552, 388, C.rustPale, C.rust, "rounded-xl", "limits");
    addText(s, "תרומה אפשרית", 724, 204, 464, 44, { size: 28, bold: true, color: C.teal });
    addText(s, "• הרחבת שדה הראייה בין שפות\n• שקיפות בהחלטות איסוף\n• הפרדת מקור, דיווח ופרשנות\n• השוואה בלי למזג קולות\n• מסלול שחזור לחוקר אחר", 724, 278, 464, 210, {
      size: 23,
      bold: true,
    });
    addText(s, "מגבלות הפיילוט", 92, 204, 464, 44, { size: 28, bold: true, color: C.rust });
    addText(s, "• מאגר אחד ותקופה קצרה\n• OCR לא אחיד\n• תלות בהודעות רשמיות\n• אין עדיין מדד recall\n• נדרשת השוואה בין חוקרים", 92, 278, 464, 210, {
      size: 23,
      bold: true,
    });
    addText(s, "הצעד הבא: מבחן חוזר בארכיון נוסף, עם benchmark ידני ושני חוקרים בלתי תלויים.", 154, 606, 972, 52, {
      size: 23,
      bold: true,
      align: "center",
    });
    notes(s, [
      "https://github.com/pedahzur/from-question-to-evidence/blob/codex/mirrored-newspaper-evidence/editorial/related-methods-review-2026.md",
      "https://doi.org/10.1002/asi.24765",
    ]);
  }

  // 11. Close
  {
    const s = deck.slides.add();
    s.background.fill = C.ink;
    addText(s, "היעד אינו תשובה מהירה יותר.", 180, 172, 920, 78, {
      size: 44,
      bold: true,
      color: C.white,
      align: "center",
    });
    addText(s, "היעד הוא טענה שאפשר לעקוב אחר הדרך שהובילה אליה.", 180, 286, 920, 100, {
      size: 36,
      bold: true,
      color: C.tealPale,
      align: "center",
      valign: "middle",
    });
    rule(s, 430, 438, 420, C.gold, 4, "closing-rule");
    addText(s, "טענה תחומה ← הצלבה ← מקור ← חיפוש ← שאלה", 244, 492, 792, 44, {
      size: 24,
      color: C.white,
      align: "center",
    });
    addText(s, "github.com/pedahzur/from-question-to-evidence", 388, 638, 504, 24, {
      size: 15,
      color: C.line,
      align: "center",
    });
    notes(s, [
      "https://github.com/pedahzur/from-question-to-evidence",
    ]);
  }

  return deck;
}

export async function generateDeck(outputDir) {
  await fs.mkdir(outputDir, { recursive: true });
  const deck = buildDeck();
  for (const [index, slide] of deck.slides.items.entries()) {
    const stem = `slide-${String(index + 1).padStart(2, "0")}`;
    const png = await deck.export({ slide, format: "png", scale: 1 });
    await fs.writeFile(path.join(outputDir, `${stem}.png`), new Uint8Array(await png.arrayBuffer()));
    const layout = await slide.export({ format: "layout" });
    await fs.writeFile(path.join(outputDir, `${stem}.layout.json`), await layout.text());
  }
  const montage = await deck.export({ format: "webp", montage: true, scale: 0.5 });
  await fs.writeFile(path.join(outputDir, "deck-montage.webp"), new Uint8Array(await montage.arrayBuffer()));
  const pptx = await PresentationFile.exportPptx(deck);
  await pptx.save(path.join(outputDir, "mirrored-newspaper-evidence-he.pptx"));
  return { deck, outputDir };
}
