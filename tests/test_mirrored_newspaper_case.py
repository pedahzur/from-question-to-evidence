from pathlib import Path
import csv
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "content/10-mirrored-newspaper-evidence.qmd"
EXAMPLE = ROOT / "examples/mirrored-newspaper-evidence"
PRESENTATION = ROOT / "presentations/mirrored-newspaper-evidence-he.pptx"
RELATED_METHODS = ROOT / "editorial/related-methods-review-2026.md"
POSTS = (
    ROOT / "communications/mirrored-newspaper-evidence-post-he.md",
    ROOT / "communications/mirrored-newspaper-evidence-post-en.md",
)


def test_case_chapter_is_auditable_and_bounded() -> None:
    text = CHAPTER.read_text(encoding="utf-8").lower()
    required = (
        "eight-step reconstruction",
        "failed searches",
        "information origin",
        "event crosswalk",
        "confirmed, probable, theater-level, or rejected",
        "stopping rule",
        "did not establish event identity",
        "does not republish newspaper scans",
    )
    for phrase in required:
        assert phrase in text, phrase


def test_example_package_has_consistent_csv_widths() -> None:
    expected = {
        "search-log.csv": 16,
        "source-manifest.csv": 11,
        "event-crosswalk.csv": 6,
    }
    for filename, row_count in expected.items():
        with (EXAMPLE / filename).open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        assert len(rows) - 1 == row_count
        width = len(rows[0])
        assert all(len(row) == width for row in rows)


def test_example_package_contains_links_not_scans() -> None:
    manifest = (EXAMPLE / "source-manifest.csv").read_text(encoding="utf-8")
    assert "https://www.nli.org.il/he/newspapers/" in manifest
    assert not list(EXAMPLE.glob("*.pdf"))
    assert not list(EXAMPLE.glob("*.png"))
    assert not list(EXAMPLE.glob("*.jpg"))


def test_hebrew_presentation_is_editable_and_has_source_notes() -> None:
    assert PRESENTATION.stat().st_size > 10_000
    with ZipFile(PRESENTATION) as archive:
        names = set(archive.namelist())
    assert "ppt/slides/slide11.xml" in names
    assert len([name for name in names if name.startswith("ppt/notesSlides/notesSlide") and name.endswith(".xml")]) == 11


def test_related_methods_and_bilingual_posts_are_present() -> None:
    review = RELATED_METHODS.read_text(encoding="utf-8")
    for approach in (
        "Collections as Data",
        "Environmental Scan",
        "Impresso",
        "Computational grounded theory",
        "LLM-assisted qualitative coding",
        "ASReview",
    ):
        assert approach in review
    for post in POSTS:
        word_count = len(post.read_text(encoding="utf-8").split())
        assert 450 <= word_count <= 600
