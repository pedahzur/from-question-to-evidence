from pathlib import Path
import re
import subprocess

import yaml


ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "content/02-evidence-map-overview.qmd"
SCRIPT = ROOT / "assets/evidence-map-pilot.js"
LOADER = ROOT / "assets/evidence-map-pilot-loader.html"


def test_evidence_map_module_declares_dual_output_visual_companion() -> None:
    text = MODULE.read_text(encoding="utf-8")

    assert 'data-evidence-map-pilot' in text
    assert 'when-profile="site"' in text
    assert 'when-profile="manuscript"' in text
    assert "Interactive visual companion" in text
    assert "Seven-stage pathway" in text
    assert len(re.findall(r'data-stage="[^"]+"', text)) == 7
    assert len(re.findall(r'data-map-node="[^"]+"', text)) >= 10


def test_visual_companion_assets_are_wired_into_site_profile() -> None:
    site = yaml.safe_load((ROOT / "_quarto-site.yml").read_text(encoding="utf-8"))
    html = site["format"]["html"]
    resources = site["project"]["resources"]

    assert "assets/evidence-map-pilot.js" in resources
    assert html["include-after-body"] == "assets/evidence-map-pilot-loader.html"
    assert SCRIPT.is_file()
    assert LOADER.is_file()


def test_visual_companion_javascript_is_valid_and_accessible_by_contract() -> None:
    result = subprocess.run(
        ["node", "--check", str(SCRIPT)],
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr

    source = SCRIPT.read_text(encoding="utf-8")
    for required in (
        "aria-selected",
        "aria-pressed",
        "textContent",
        "prefers-reduced-motion",
        "resize",
    ):
        assert required in source


def test_rendered_site_contains_visual_companion_assets() -> None:
    page = ROOT / "build-site/content/02-evidence-map-overview.html"
    if not page.is_file():
        return

    html = page.read_text(encoding="utf-8")
    assert "data-evidence-map-pilot" in html
    assert "assets/evidence-map-pilot.js" in html
    assert (ROOT / "build-site/assets/evidence-map-pilot.js").is_file()
