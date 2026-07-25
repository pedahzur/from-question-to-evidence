from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_opening_states_the_decade_long_origin_and_llm_turn() -> None:
    opening = (ROOT / "index.qmd").read_text(encoding="utf-8")
    body = opening.split("---", 2)[2]
    first_words = " ".join(body.split()[:260])

    assert "Nearly a decade ago" in first_words
    assert "workflow" in first_words
    assert "processing power" in first_words
    assert "large language models" in first_words
    assert "reproducible" in first_words


def test_site_profile_uses_accessible_reading_grid() -> None:
    site = yaml.safe_load((ROOT / "_quarto-site.yml").read_text(encoding="utf-8"))
    grid = site["format"]["html"]["grid"]

    assert grid["sidebar-width"] == "300px"
    assert grid["body-width"] == "800px"
    assert grid["margin-width"] == "240px"
    assert grid["gutter-width"] == "2rem"


def test_styles_define_accessible_type_and_navigation_spacing() -> None:
    styles = (ROOT / "styles.scss").read_text(encoding="utf-8")

    for rule in (
        "$font-size-root: 19px;",
        "$line-height-base: 1.65;",
        "$sidebar-font-size: 1rem;",
        "$toc-font-size: 0.95rem;",
        ".sidebar-navigation .sidebar-item",
        ".opening-deck",
        ":focus-visible",
    ):
        assert rule in styles
