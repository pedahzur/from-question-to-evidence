from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
COMPANION = ROOT / "lab/historical-evidence-chain"


def test_book_contract_names_the_revised_scope() -> None:
    config = yaml.safe_load((ROOT / "_quarto.yml").read_text(encoding="utf-8"))
    subtitle = config["book"]["subtitle"].lower()
    description = config["book"]["description"].lower()

    assert "historically grounded social research" in subtitle
    assert "big data" in description
    assert "large language models" in description


def test_foundational_papers_are_integrated_as_sources() -> None:
    bibliography = (ROOT / "bibliography/references.bib").read_text(encoding="utf-8")
    assert "@article{grossman2020bigdata" in bibliography
    assert "@techreport{grossman2022digitalsources" in bibliography

    for relative in (
        "content/01-origins-and-purpose.qmd",
        "content/20-historical-sources-as-evidence.qmd",
        "content/20-pkm-and-ai-research-infrastructure.qmd",
    ):
        text = (ROOT / relative).read_text(encoding="utf-8")
        assert "@grossman2020bigdata" in text, relative
        assert "@grossman2022digitalsources" in text, relative


def test_historical_evidence_chain_companion_is_versioned_and_complete() -> None:
    required = (
        "README.md",
        "SOURCE-PROVENANCE.md",
        "UPSTREAM-LICENSE.md",
        "docs/article/historical-evidence-chain.md",
        "docs/codebook/salem-codebook.md",
        "docs/codebook/human-coding-form.md",
        "prompts/01-transcription.md",
        "prompts/02-extraction.md",
        "prompts/03-audit.md",
        "schemas/airtable-implementation.md",
        "schemas/redcap-implementation.md",
        "metadata/controlled-vocabulary.yaml",
        "metadata/schema-notes.md",
    )
    for relative in required:
        assert (COMPANION / relative).is_file(), relative

    provenance = (COMPANION / "SOURCE-PROVENANCE.md").read_text(encoding="utf-8")
    assert "488aa604ba8f0ec4fb76232f15d3f15835749c62" in provenance
    assert "https://github.com/pedahzur/historical-evidence-chain" in provenance


def test_integration_and_bilingual_governance_are_documented() -> None:
    for relative in (
        "docs/revisions/historical-big-data-llm-integration-charter-2026-08-05.md",
        "docs/revisions/bilingual-publication-strategy-2026-08-05.md",
        "editorial/source-review-big-data-pkm-historical-evidence-2026-08-05.md",
    ):
        assert (ROOT / relative).is_file(), relative

    strategy = (
        ROOT / "docs/revisions/bilingual-publication-strategy-2026-08-05.md"
    ).read_text(encoding="utf-8")
    for phrase in (
        "English source edition",
        "Hebrew edition",
        "translation status",
        "stable chapter identifier",
        "right-to-left",
    ):
        assert phrase in strategy, phrase
