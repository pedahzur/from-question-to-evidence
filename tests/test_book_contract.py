from pathlib import Path

import yaml

from scripts.check_content import validate_text


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = [
    "index.qmd",
    "content/01-origins-and-purpose.qmd",
    "content/02-evidence-map-overview.qmd",
    "content/03-frame.qmd",
    "content/04-decompose.qmd",
    "content/05-map-source-families.qmd",
    "content/06-search-iteratively.qmd",
    "content/07-evaluate.qmd",
    "content/08-test-coverage.qmd",
    "content/09-produce-evidence-map.qmd",
    "content/10-ai-research-integrity.qmd",
    "content/11-next-steps.qmd",
    "content/references.qmd",
]


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_quarto_book_contract() -> None:
    base = load_yaml(ROOT / "_quarto.yml")
    manuscript = load_yaml(ROOT / "_quarto-manuscript.yml")

    assert base["project"]["type"] == "book"
    assert base["book"]["chapters"] == CHAPTERS
    assert manuscript["project"]["output-dir"] == "_output/manuscript"
    assert manuscript["bibliography"] == "bibliography/references.bib"
    assert set(manuscript["format"]) == {"docx", "pdf"}


def test_all_chapters_have_required_metadata() -> None:
    required = {"title", "description", "author", "date", "last-reviewed", "license"}
    for relative in CHAPTERS:
        path = ROOT / relative
        text = path.read_text(encoding="utf-8")
        _, frontmatter, _ = text.split("---", 2)
        metadata = yaml.safe_load(frontmatter)
        assert required <= metadata.keys(), relative


def test_content_checker_rejects_forbidden_markers() -> None:
    errors = validate_text("content/example.qmd", "A paragraph with " + "TO" + "DO inside.")
    assert errors == ["content/example.qmd: contains a forbidden draft marker"]
