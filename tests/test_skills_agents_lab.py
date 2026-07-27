from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import subprocess
import sys
from zipfile import ZipFile

import yaml


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "lab"
SKILL = LAB / "skills/literature-discovery"
VERSION = "0.1.0"
ARCHIVE = ROOT / f"downloads/skills-and-agents-lab-v{VERSION}.zip"
CHECKSUM = ARCHIVE.with_suffix(".zip.sha256")


def load_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    _, frontmatter, body = text.split("---", 2)
    return yaml.safe_load(frontmatter), body


def test_lab_manifest_is_complete_and_public() -> None:
    manifest = yaml.safe_load((LAB / "MANIFEST.yml").read_text(encoding="utf-8"))
    assert manifest["name"] == "skills-and-agents-lab"
    assert manifest["version"] == VERSION
    assert manifest["status"] == "pilot"
    assert len(manifest["benchmark_cases"]) == 3

    package_files = manifest["package_files"]
    assert len(package_files) == len(set(package_files))
    for relative in package_files:
        path = LAB / relative
        assert path.is_file(), relative
        text = path.read_text(encoding="utf-8", errors="ignore")
        assert "/Users/" not in text
        assert "github" + "_pat_" not in text


def test_literature_discovery_skill_contract() -> None:
    metadata, body = load_frontmatter(SKILL / "SKILL.md")
    assert set(metadata) == {"name", "description"}
    assert metadata["name"] == "literature-discovery"
    for phrase in (
        "review protocol",
        "project-context packet",
        "candidate register",
        "final inclusion",
    ):
        assert phrase in metadata["description"].lower()

    required_body = (
        "## Inputs",
        "## Workflow",
        "## Human gates",
        "## Failure and abstention",
        "candidate_id",
        "discovery_route",
        "verification_status",
        "Do not decide final eligibility",
    )
    for phrase in required_body:
        assert phrase in body


def test_literature_scout_agent_is_bounded_and_read_only() -> None:
    metadata, body = load_frontmatter(LAB / "agents/literature-scout.md")
    assert metadata["name"] == "literature-scout"
    assert metadata["model"] == "inherit"
    assert metadata["color"] == "cyan"
    assert set(metadata["tools"]) == {
        "Read",
        "Grep",
        "Glob",
        "WebSearch",
        "WebFetch",
    }
    assert "Write" not in metadata["tools"]
    assert "Bash" not in metadata["tools"]
    assert metadata["description"].count("<example>") >= 2

    for phrase in (
        "staging",
        "Do not decide final inclusion or exclusion",
        "Stop and escalate",
        "Evidence boundary",
        "Output format",
    ):
        assert phrase in body


def test_project_context_packet_has_three_layers_and_authority_fields() -> None:
    text = (LAB / "templates/project-context-packet.md").read_text(encoding="utf-8")
    for phrase in (
        "Stable layer",
        "Current-state layer",
        "Task layer",
        "Authority status",
        "Human decision required",
        "Restricted material",
    ):
        assert phrase in text


def test_three_benchmarks_have_valid_contracts() -> None:
    benchmark_manifest = yaml.safe_load(
        (LAB / "benchmarks/benchmark-manifest.yml").read_text(encoding="utf-8")
    )
    cases = benchmark_manifest["cases"]
    assert [case["id"] for case in cases] == [
        "known-item-recovery",
        "false-gap",
        "boundary-and-abstention",
    ]

    for case in cases:
        case_dir = LAB / "benchmarks" / case["directory"]
        spec = yaml.safe_load((case_dir / "case.yml").read_text(encoding="utf-8"))
        expected = yaml.safe_load((case_dir / "expected.yml").read_text(encoding="utf-8"))
        assert spec["synthetic"] is True
        assert spec["input_files"]
        assert expected["required_assertions"]
        for relative in spec["input_files"]:
            assert (case_dir / relative).is_file(), f"{case['id']}: {relative}"


def test_candidate_register_validator_accepts_benchmarks_and_rejects_bad_rows() -> None:
    validator = SKILL / "scripts/validate_candidate_register.py"
    benchmark_manifest = yaml.safe_load(
        (LAB / "benchmarks/benchmark-manifest.yml").read_text(encoding="utf-8")
    )
    for case in benchmark_manifest["cases"]:
        candidate_register = (
            LAB / "benchmarks" / case["directory"] / "expected-candidate-register.csv"
        )
        result = subprocess.run(
            [sys.executable, str(validator), str(candidate_register)],
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, result.stdout + result.stderr

    invalid = ROOT / "tests/fixtures/invalid-candidate-register.csv"
    result = subprocess.run(
        [sys.executable, str(validator), str(invalid)],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert "source_locator" in result.stdout


def test_release_archive_is_deterministic_and_matches_manifest(tmp_path: Path) -> None:
    builder = ROOT / "scripts/build_lab_package.py"
    first = tmp_path / "first.zip"
    second = tmp_path / "second.zip"
    for output in (first, second):
        subprocess.run(
            [sys.executable, str(builder), "--output", str(output)],
            check=True,
            cwd=ROOT,
        )
    assert first.read_bytes() == second.read_bytes()

    manifest = yaml.safe_load((LAB / "MANIFEST.yml").read_text(encoding="utf-8"))
    prefix = f"skills-and-agents-lab-v{VERSION}/"
    with ZipFile(first) as archive:
        assert archive.namelist() == [
            prefix + relative for relative in manifest["package_files"]
        ]


def test_built_release_and_feedback_routes_exist() -> None:
    assert ARCHIVE.is_file()
    digest, filename = CHECKSUM.read_text(encoding="utf-8").strip().split("  ", 1)
    assert filename == ARCHIVE.name
    assert digest == hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()

    page = (ROOT / "content/skills-and-agents-lab.qmd").read_text(encoding="utf-8")
    assert ARCHIVE.name in page
    assert "issues/new?template=lab-problem.yml" in page
    assert "issues/new?template=lab-revision.yml" in page
    assert (ROOT / ".github/ISSUE_TEMPLATE/lab-problem.yml").is_file()
    assert (ROOT / ".github/ISSUE_TEMPLATE/lab-revision.yml").is_file()


def test_benchmark_candidate_registers_share_the_declared_schema() -> None:
    schema = yaml.safe_load(
        (SKILL / "references/candidate-register-schema.yml").read_text(encoding="utf-8")
    )
    expected_fields = schema["fields"]
    for path in sorted((LAB / "benchmarks").glob("*/expected-candidate-register.csv")):
        with path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            assert reader.fieldnames == expected_fields, path
            assert list(reader), path
