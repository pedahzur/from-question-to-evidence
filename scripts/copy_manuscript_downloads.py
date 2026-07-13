from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "build-manuscript"
SITE = ROOT / "build-site"
FILENAMES = ("From-Question-to-Evidence.docx", "From-Question-to-Evidence.pdf")


def main() -> int:
    SITE.mkdir(parents=True, exist_ok=True)
    missing = [filename for filename in FILENAMES if not (MANUSCRIPT / filename).is_file()]
    if missing:
        names = ", ".join(missing)
        raise SystemExit(
            f"Missing manuscript downloads: {names}. Render --profile manuscript before --profile site."
        )
    for filename in FILENAMES:
        shutil.copy2(MANUSCRIPT / filename, SITE / filename)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
