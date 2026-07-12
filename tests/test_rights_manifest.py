from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def test_publishable_assets_have_complete_rights_records() -> None:
    records = yaml.safe_load(
        (ROOT / "editorial/rights-manifest.yml").read_text(encoding="utf-8")
    )
    required = {"creator", "source", "rights_basis", "attribution", "reviewed_on"}
    publishable = [record for record in records if record["publish"]]
    assert publishable
    for record in publishable:
        assert required <= record.keys()
        assert all(record[field] for field in required)
        assert not record["path"].lower().endswith(".pdf")


def test_legacy_audit_uses_controlled_dispositions() -> None:
    text = (ROOT / "editorial/legacy-audit.csv").read_text(encoding="utf-8")
    allowed = {
        "retain-rewrite",
        "update",
        "archive-provenance",
        "exclude-rights",
        "remove-residue",
    }
    rows = [line.split(",") for line in text.strip().splitlines()[1:]]
    assert len(rows) >= 20
    assert {row[2] for row in rows} <= allowed
