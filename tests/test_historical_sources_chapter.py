from pathlib import Path
import re

import yaml


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "content/20-historical-sources-as-evidence.qmd"
RESOURCE = ROOT / "templates/historical-evidence-chain-register.md"


def test_historical_sources_chapter_is_in_the_book_sequence() -> None:
    config = yaml.safe_load((ROOT / "_quarto.yml").read_text(encoding="utf-8"))
    chapters = config["book"]["chapters"]
    historical = "content/20-historical-sources-as-evidence.qmd"

    assert historical in chapters
    assert chapters.index(historical) == chapters.index(
        "content/19-building-event-databases-with-ai.qmd"
    ) + 1
    assert chapters.index("content/19-ai-research-integrity.qmd") < chapters.index(
        "content/02-evidence-map-overview.qmd"
    )


def test_historical_sources_chapter_follows_the_page_pattern() -> None:
    text = CHAPTER.read_text(encoding="utf-8")
    headings = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    assert headings == [
        "Orientation",
        "Learn",
        "Worked Example",
        "Try It",
        "Guided AI Workflow",
        "Integrity Checkpoint",
        "Save the Artifact",
        "Advanced Practice",
    ]


def test_historical_evidence_chain_preserves_epistemic_boundaries() -> None:
    text = CHAPTER.read_text(encoding="utf-8").lower()
    required_language = (
        "historical evidence chain",
        "source witness",
        "diplomatic transcription",
        "source-stated",
        "normalized",
        "inferred",
        "claim in source",
        "historical claim",
        "downstream claim audit",
        "procedurally unsupported",
        "archival page",
        "append-only",
        "discovery loop",
        "validation loop",
        "verification debt",
        "retrieval is selection",
    )
    for phrase in required_language:
        assert phrase in text, phrase


def test_historical_sources_chapter_marks_pilot_status_and_sources() -> None:
    text = CHAPTER.read_text(encoding="utf-8")

    assert "not a completed experiment" in text
    assert "no empirical findings" in text
    for citation in (
        "@pedahzur2026historical",
        "@wineburg1991historical",
        "@trouillot1995silencing",
        "@muehlberger2019transkribus",
        "@beelen2023bias",
        "@lebo2013provo",
        "@murugaraj2025topicrag",
        "@zhou2025humanities",
    ):
        assert citation in text, citation


def test_historical_evidence_chain_resource_is_linked() -> None:
    assert RESOURCE.is_file()
    text = CHAPTER.read_text(encoding="utf-8")
    assert "../templates/historical-evidence-chain-register.md" in text
    assert 'fig-alt="Eight numbered boxes' in text
