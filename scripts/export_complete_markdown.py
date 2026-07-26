from __future__ import annotations

from datetime import date
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT_DIR = ROOT / "build-manuscript"
DOCX = MANUSCRIPT_DIR / "From-Question-to-Evidence.docx"
MARKDOWN = MANUSCRIPT_DIR / "From-Question-to-Evidence.md"


def main() -> int:
    pandoc = shutil.which("pandoc")
    if pandoc is None:
        raise SystemExit("pandoc is required to export the complete Markdown manuscript")
    if not DOCX.is_file():
        raise SystemExit(f"missing rendered manuscript: {DOCX}")

    subprocess.run(
        [
            pandoc,
            str(DOCX),
            "--to=gfm",
            "--standalone",
            "--wrap=none",
            "--metadata",
            "title=From Question to Evidence",
            "--metadata",
            "subtitle=A Living Field Guide for Qualitative Research",
            "--metadata",
            "status=revision-draft",
            "--metadata",
            f"updated={date.today().isoformat()}",
            f"--output={MARKDOWN}",
        ],
        check=True,
    )

    text = MARKDOWN.read_text(encoding="utf-8")
    text = text.replace("# Table of contents\n\n", "", 1)
    MARKDOWN.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
