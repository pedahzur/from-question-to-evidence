from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "content/19-building-event-databases-with-ai.qmd"


def test_event_database_chapter_is_in_the_book_sequence() -> None:
    config = yaml.safe_load((ROOT / "_quarto.yml").read_text(encoding="utf-8"))
    chapters = config["book"]["chapters"]
    event_chapter = "content/19-building-event-databases-with-ai.qmd"

    assert event_chapter in chapters
    assert chapters.index(event_chapter) == chapters.index(
        "content/19-review-articles-and-meta-analysis.qmd"
    ) + 1
    assert chapters.index(event_chapter) < chapters.index(
        "content/19-ai-research-integrity.qmd"
    )


def test_event_database_chapter_preserves_the_audit_chain() -> None:
    text = CHAPTER.read_text(encoding="utf-8")

    for required in (
        "candidate record",
        "verified record",
        "event resolution log",
        "source span",
        "codebook version",
        "validation sample",
        "likelihood ratio",
        "sensitivity analysis",
    ):
        assert required in text.lower()


def test_event_database_chapter_keeps_bayesian_judgment_human() -> None:
    text = CHAPTER.read_text(encoding="utf-8").lower()

    assert "posterior odds" in text
    assert "prior odds" in text
    assert "researcher assigns" in text
    assert "model confidence" in text
    assert "not a likelihood ratio" in text


def test_event_database_chapter_has_guided_workflow_and_sources() -> None:
    text = CHAPTER.read_text(encoding="utf-8")

    for heading in (
        "## Orientation",
        "## Learn",
        "## Worked Example",
        "## Try It",
        "## Guided AI Workflow",
        "## Integrity Checkpoint",
        "## Save the Artifact",
        "## Advanced Practice",
    ):
        assert heading in text

    for citation in (
        "@gilardi2023chatgpt",
        "@pangakis2023annotation",
        "@beelen2023bias",
        "@fairfield2017bayesian",
        "@xiong2024uncertainty",
        "@weidmann2026democracy",
    ):
        assert citation in text


def test_event_database_chapter_distinguishes_correlation_from_agreement() -> None:
    text = CHAPTER.read_text(encoding="utf-8").lower()

    for required in (
        "absolute agreement",
        "not ground truth",
        "more pessimistic",
        "more optimistic",
        "averaging is not a substitute for calibration",
        "model-specific outputs",
    ):
        assert required in text
