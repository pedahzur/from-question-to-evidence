from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN = ROOT / "docs/hebrew-five-page-summary-2026-08-06.md"
DOCX = ROOT / "build-manuscript/From-Question-to-Evidence-Hebrew-Five-Page-Summary.docx"


def test_hebrew_summary_has_five_explicit_rtl_pages() -> None:
    text = MARKDOWN.read_text(encoding="utf-8")

    assert 'language: he' in text
    assert 'direction: rtl' in text
    assert 'source-commit: 3253c53' in text
    assert '<div dir="rtl" style="text-align: right;">' in text
    assert text.count("### עמוד ") == 5
    assert text.count('page-break-after: always') == 4


def test_hebrew_summary_represents_the_current_book() -> None:
    text = MARKDOWN.read_text(encoding="utf-8")

    required_concepts = [
        "מוח שני מחקרי",
        "מפת הראיות",
        "ספרות האקדמית כאל ראיות",
        "מאגר אירועים",
        "שרשרת ראיות היסטורית",
        "חוב אימות",
        "הסקה בייסיאנית",
        "מעבדת הסקילים והסוכנים",
    ]
    for concept in required_concepts:
        assert concept in text

    assert "שני המודולים המפותחים ביותר" in text
    assert "עדיין נמצאים בפיתוח" in text


def test_built_hebrew_docx_declares_rtl_layout() -> None:
    assert DOCX.exists()
    with ZipFile(DOCX) as archive:
        document_xml = archive.read("word/document.xml").decode("utf-8")

    assert document_xml.count("w:type=\"page\"") == 4
    assert "w:bidi" in document_xml
    assert "w:rtl" in document_xml
    assert "משאלת מחקר לראיות" in document_xml
