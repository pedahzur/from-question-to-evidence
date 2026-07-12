from pathlib import Path
import re

import yaml


FORBIDDEN_MARKERS = ("TO" + "DO", "T" + "BD", "FIX" + "ME")
NOTION_UUID = re.compile(r"\b[0-9a-f]{32}\b", re.IGNORECASE)
REQUIRED_METADATA = {"title", "description", "author", "date", "last-reviewed", "license"}


def validate_text(relative_path: str, text: str) -> list[str]:
    errors: list[str] = []
    if any(marker in text for marker in FORBIDDEN_MARKERS):
        errors.append(f"{relative_path}: contains a forbidden draft marker")
    if NOTION_UUID.search(text):
        errors.append(f"{relative_path}: contains a legacy Notion UUID")
    if text.count("\n# ") > 1:
        errors.append(f"{relative_path}: contains duplicate level-one headings")
    return errors


def main(root: Path | None = None) -> int:
    project_root = root or Path(__file__).resolve().parents[1]
    errors: list[str] = []
    for path in sorted((project_root / "content").glob("*.qmd")):
        relative = path.relative_to(project_root).as_posix()
        text = path.read_text(encoding="utf-8")
        errors.extend(validate_text(relative, text))
        try:
            _, frontmatter, _ = text.split("---", 2)
            metadata = yaml.safe_load(frontmatter) or {}
        except ValueError:
            errors.append(f"{relative}: missing YAML front matter")
            continue
        missing = sorted(REQUIRED_METADATA - metadata.keys())
        if missing:
            errors.append(f"{relative}: missing metadata {', '.join(missing)}")

    if errors:
        for error in errors:
            print(error)
        return 1
    print("content contract passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
