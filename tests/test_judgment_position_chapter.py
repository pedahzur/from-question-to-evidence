from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
CHAPTER = ROOT / "content/judgment-position-limits.qmd"


def test_judgment_position_chapter_opens_part_one() -> None:
    config = yaml.safe_load((ROOT / "_quarto.yml").read_text(encoding="utf-8"))
    chapters = config["book"]["chapters"]
    chapter = "content/judgment-position-limits.qmd"

    assert chapter in chapters
    assert chapters.index(chapter) == chapters.index(
        "content/01-origins-and-purpose.qmd"
    ) + 1
    assert chapters.index(chapter) < chapters.index(
        "content/19-ai-research-integrity.qmd"
    )


def test_judgment_position_chapter_preserves_epistemic_distinctions() -> None:
    text = CHAPTER.read_text(encoding="utf-8").lower()

    for phrase in (
        "evidence becomes reviewable",
        "position is not a confession",
        "coverage is not representation",
        "auditability is not neutrality",
        "authority is distributed",
        "synthetic and composited case",
        "epistemic-position statement",
        "ai pre-flight record",
    ):
        assert phrase in text, phrase


def test_judgment_position_chapter_links_artifacts_and_sources() -> None:
    text = CHAPTER.read_text(encoding="utf-8")

    for artifact in (
        "../templates/epistemic-position-statement.md",
        "../templates/ai-preflight-record.md",
    ):
        assert artifact in text, artifact

    for citation in (
        "@haraway1988situated",
        "@england1994personal",
        "@finlay2002swamp",
        "@soedirgo2020active",
        "@tuck2009suspending",
        "@trouillot1995silencing",
        "@jacobs2021qtd",
    ):
        assert citation in text, citation


def test_ai_integrity_chapter_requires_preflight_gate() -> None:
    text = (ROOT / "content/19-ai-research-integrity.qmd").read_text(
        encoding="utf-8"
    ).lower()

    for phrase in (
        "ai pre-flight record",
        "epistemic-position statement",
        "stop condition",
        "prohibited delegation",
        "gate decision",
    ):
        assert phrase in text, phrase
