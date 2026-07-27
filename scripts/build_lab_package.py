#!/usr/bin/env python3
"""Build a deterministic Skills and Agents Lab release archive."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

import yaml


ROOT = Path(__file__).resolve().parents[1]
LAB = ROOT / "lab"
MANIFEST = LAB / "MANIFEST.yml"
FIXED_TIMESTAMP = (2026, 7, 27, 0, 0, 0)


def load_manifest() -> dict:
    manifest = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    version = (LAB / "VERSION").read_text(encoding="utf-8").strip()
    if manifest["version"] != version:
        raise ValueError(
            f"manifest version {manifest['version']} does not match VERSION {version}"
        )
    return manifest


def validate_package_paths(relative_paths: list[str]) -> None:
    if len(relative_paths) != len(set(relative_paths)):
        raise ValueError("package_files contains duplicate paths")
    for relative in relative_paths:
        pure = PurePosixPath(relative)
        if pure.is_absolute() or ".." in pure.parts:
            raise ValueError(f"unsafe package path: {relative}")
        source = LAB / relative
        if not source.is_file():
            raise FileNotFoundError(f"manifest-listed file does not exist: {relative}")


def build_archive(output: Path) -> Path:
    manifest = load_manifest()
    package_files = manifest["package_files"]
    validate_package_paths(package_files)

    output.parent.mkdir(parents=True, exist_ok=True)
    prefix = f"{manifest['name']}-v{manifest['version']}/"
    with ZipFile(output, mode="w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in package_files:
            info = ZipInfo(prefix + relative, date_time=FIXED_TIMESTAMP)
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            archive.writestr(info, (LAB / relative).read_bytes(), compresslevel=9)

    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    checksum = output.with_suffix(".zip.sha256")
    checksum.write_text(f"{digest}  {output.name}\n", encoding="utf-8")
    return checksum


def main() -> int:
    manifest = load_manifest()
    default_output = (
        ROOT
        / "downloads"
        / f"{manifest['name']}-v{manifest['version']}.zip"
    )
    parser = argparse.ArgumentParser(
        description="Build the deterministic Skills and Agents Lab ZIP."
    )
    parser.add_argument("--output", type=Path, default=default_output)
    args = parser.parse_args()

    checksum = build_archive(args.output)
    print(f"built {args.output}")
    print(f"wrote {checksum}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
