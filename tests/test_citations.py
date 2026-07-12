from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def test_bibliography_has_verified_foundation() -> None:
    bibliography = (ROOT / "bibliography/references.bib").read_text(encoding="utf-8")
    keys = re.findall(r"^@\w+\{([^,]+),", bibliography, flags=re.MULTILINE)
    assert len(keys) >= 8
    assert len(keys) == len(set(keys))


def test_all_citation_keys_resolve() -> None:
    bibliography = (ROOT / "bibliography/references.bib").read_text(encoding="utf-8")
    known = set(re.findall(r"^@\w+\{([^,]+),", bibliography, flags=re.MULTILINE))
    cited: set[str] = set()
    for path in (ROOT / "content").glob("*.qmd"):
        text = path.read_text(encoding="utf-8")
        cited.update(re.findall(r"@([A-Za-z][A-Za-z0-9:_-]+)", text))
    assert cited
    assert cited <= known
