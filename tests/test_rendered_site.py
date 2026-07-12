from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "build-site"


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        values = dict(attrs)
        if values.get("href"):
            self.links.append(values["href"] or "")


def test_internal_links_resolve() -> None:
    broken: list[str] = []
    for page in SITE.rglob("*.html"):
        collector = LinkCollector()
        collector.feed(page.read_text(encoding="utf-8"))
        for href in collector.links:
            parsed = urlparse(href)
            if parsed.scheme or href.startswith(("#", "mailto:")):
                continue
            target = unquote(parsed.path)
            candidate = (page.parent / target).resolve()
            if target.endswith("/"):
                candidate = candidate / "index.html"
            if not candidate.exists():
                broken.append(f"{page.relative_to(SITE)} -> {href}")
    assert not broken, "\n".join(broken)


def test_site_has_no_private_archive_residue() -> None:
    for page in SITE.rglob("*.html"):
        text = page.read_text(encoding="utf-8")
        assert "Private & Shared" not in text
        assert "/Users/" not in text
