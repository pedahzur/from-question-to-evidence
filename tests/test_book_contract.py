from pathlib import Path
import re

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
    "content/12-literature-as-evidence.qmd",
    "content/13-define-review.qmd",
    "content/14-map-concepts-vocabulary.qmd",
    "content/15-discover-literature.qmd",
    "content/16-evaluate-literature.qmd",
    "content/17-read-annotate-compare.qmd",
    "content/18-synthesize-audit-stop.qmd",
    "content/19-review-articles-and-meta-analysis.qmd",
    "content/19-building-event-databases-with-ai.qmd",
    "content/20-historical-sources-as-evidence.qmd",
    "content/19-ai-research-integrity.qmd",
    "content/20-pkm-and-ai-research-infrastructure.qmd",
    "content/21-writing-by-voice-revising-by-ear.qmd",
    "content/skills-and-agents-lab.qmd",
    "content/20-next-steps.qmd",
    "content/references.qmd",
]

LITERATURE_STAGES = [
    "content/13-define-review.qmd",
    "content/14-map-concepts-vocabulary.qmd",
    "content/15-discover-literature.qmd",
    "content/16-evaluate-literature.qmd",
    "content/17-read-annotate-compare.qmd",
    "content/18-synthesize-audit-stop.qmd",
]

STAGE_SECTIONS = [
    "Orientation",
    "Learn",
    "Worked Example",
    "Try It",
    "Guided AI Workflow",
    "Integrity Checkpoint",
    "Save the Artifact",
    "Advanced Practice",
]


def load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_quarto_book_contract() -> None:
    base = load_yaml(ROOT / "_quarto.yml")
    manuscript = load_yaml(ROOT / "_quarto-manuscript.yml")

    assert base["project"]["type"] == "book"
    assert base["book"]["chapters"] == CHAPTERS
    assert manuscript["project"]["output-dir"] == "build-manuscript"
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


def test_quarto_site_profile() -> None:
    site = load_yaml(ROOT / "_quarto-site.yml")
    assert site["project"]["output-dir"] == "build-site"
    assert "html" in site["format"]
    assert site["book"]["search"] is True
    assert site["book"]["page-navigation"] is True
    assert site["book"]["downloads"] == ["docx", "pdf"]


def test_literature_stages_follow_page_pattern() -> None:
    for relative in LITERATURE_STAGES:
        text = (ROOT / relative).read_text(encoding="utf-8")
        headings = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
        assert headings == STAGE_SECTIONS, relative


def test_literature_module_scope_and_ai_boundaries() -> None:
    paths = ["content/12-literature-as-evidence.qmd", *LITERATURE_STAGES]
    combined = "\n".join((ROOT / path).read_text(encoding="utf-8") for path in paths)
    word_count = len(re.findall(r"\b[\w’'-]+\b", combined))
    assert 8_000 <= word_count <= 10_000
    for label in ("Permitted input", "Do not provide", "Verify", "Record"):
        assert combined.count(label) >= len(LITERATURE_STAGES), label


def test_review_articles_and_meta_analysis_chapter_contract() -> None:
    path = ROOT / "content/19-review-articles-and-meta-analysis.qmd"
    text = path.read_text(encoding="utf-8")
    headings = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    assert headings == STAGE_SECTIONS

    required_language = (
        "review family",
        "meta-analysis is not",
        "dependent effect",
        "prediction interval",
        "publication bias",
        "living review",
        "versioned",
        "human validation",
        "conditional future",
    )
    lowered = text.lower()
    for phrase in required_language:
        assert phrase in lowered, phrase

    required_citations = (
        "@pigott2020meta",
        "@hedges2010robust",
        "@irsova2024meta",
        "@moreau2022open",
        "@elliott2017living",
        "@sousa2026ai",
        "@liu2024lost",
        "@yao2023react",
    )
    for citation in required_citations:
        assert citation in text, citation

    assert "AI will replace" not in text


def test_review_chapter_defines_research_skills_agents_and_context() -> None:
    text = (
        ROOT / "content/19-review-articles-and-meta-analysis.qmd"
    ).read_text(encoding="utf-8").lower()
    required_language = (
        "skill is a reusable",
        "agent is a bounded",
        "literature-discovery skill",
        "gap-analysis skill",
        "methodology-audit skill",
        "data-collection skill",
        "project-context skill",
        "project context packet",
        "human gate",
        "least privilege",
        "staging area",
        "false gap",
    )
    for phrase in required_language:
        assert phrase in text, phrase


def test_pkm_ai_chapter_is_operational_and_source_audited() -> None:
    chapter = ROOT / "content/20-pkm-and-ai-research-infrastructure.qmd"
    register = ROOT / "editorial/readwise-pkm-ai-source-register.md"
    assert chapter.is_file()
    assert register.is_file()

    text = chapter.read_text(encoding="utf-8").lower()
    required_language = (
        "pkm and ai solve different research problems",
        "persistent context",
        "provenance",
        "human gate",
        "pkm-ai research loop",
        "candidate register",
        "negative evidence",
        "what ai must not do",
    )
    for phrase in required_language:
        assert phrase in text, phrase

    register_text = register.read_text(encoding="utf-8").lower()
    for label in ("📄academic article", "🗃️pkm", "🤖ai"):
        assert label in register_text
    assert "connector limit" in register_text
    assert "readwise content inspected" in register_text


def test_voice_writing_chapter_is_auditable_and_multilingual() -> None:
    chapter = ROOT / "content/21-writing-by-voice-revising-by-ear.qmd"
    assert chapter.is_file()

    text = chapter.read_text(encoding="utf-8")
    headings = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
    assert headings == STAGE_SECTIONS

    lowered = text.lower()
    required_language = (
        "round-trip method",
        "raw transcript",
        "corrected transcript",
        "listening copy",
        "multilingual",
        "code-switched",
        "privacy",
        "permitted input",
        "do not provide",
        "verify",
        "record",
    )
    for phrase in required_language:
        assert phrase in lowered, phrase

    for citation in (
        "@liu2022typist",
        "@lin2024rambler",
        "@garrison2009tts",
        "@ugan2024decm",
        "@kim2025myth",
    ):
        assert citation in text, citation

    for relative in (
        "docs/tool-cards/wispr-flow.md",
        "docs/tool-cards/speechify.md",
        "templates/voice-round-trip-log.md",
    ):
        assert (ROOT / relative).is_file(), relative

    for card in ("wispr-flow.md", "speechify.md"):
        card_text = (ROOT / "docs/tool-cards" / card).read_text(encoding="utf-8")
        assert "last-verified: 2026-08-01" in card_text
        assert "Next scheduled review: 2026-11-01" in card_text


def test_public_project_documents_exist() -> None:
    for relative in (
        "README.md",
        "ROADMAP.md",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "docs/hebrew-table-of-contents.md",
        "docs/PROJECT-ASSESSMENT-HE.md",
    ):
        assert (ROOT / relative).is_file(), relative


def test_hebrew_table_of_contents_tracks_current_book() -> None:
    path = ROOT / "docs/hebrew-table-of-contents.md"
    text = path.read_text(encoding="utf-8")
    chapter_numbers = re.findall(r"^### (\d+)\.", text, flags=re.MULTILINE)

    assert chapter_numbers == [str(number) for number in range(1, 27)]
    assert "direction: rtl" in text
    assert "## חלק ראשון: ממחקר ראשוני למפת ראיות" in text
    assert "### 20. מקורות היסטוריים כראיות" in text
    assert "### 23. כתיבה בקול, עריכה באמצעות האוזן" in text
    assert "### 24. מעבדת סקילים וסוכנים" in text
