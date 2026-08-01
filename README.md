# From Question to Evidence

*A Living Field Guide for Qualitative Research*

**Read the guide:** <https://pedahzur.github.io/from-question-to-evidence/>

This repository contains the English discussion draft, editable resources, and reproducible website source for an open-access field guide by Ami Pedahzur and Jonathan Grossman. The site republishes automatically on every push to `main` after the full test suite passes.

The guide helps researchers connect questions, concepts, discovery, collection, evidence, and claims while preserving the decisions that shape a research corpus. Generative AI appears as a bounded research aid. It does not replace source reading, verification, ethical judgment, or responsibility for synthesis.

## Current Draft

Version `0.2.0-draft` contains two complete exemplary modules:

1. **From Question to Evidence Map** — seven stages from framing to a collection strategy and stopping rule.
2. **Literature as Evidence** — six stages from review protocol to synthesis, coverage audit, and stopping rule.

The next planned module covers collection and post-production. See [ROADMAP.md](ROADMAP.md).

The latest discussion-draft release packages the manuscript as both Word and PDF, together with a browsable site preview and a reproducible source archive: [v0.2.0-draft](https://github.com/pedahzur/from-question-to-evidence/releases/tag/v0.2.0-draft).

## Repository Layout

- `content/` — canonical Quarto manuscript pages.
- `templates/` — editable DOCX and XLSX reader resources.
- `scripts/` — content checks and deterministic resource builders.
- `bibliography/` — verified BibTeX records.
- `editorial/` — legacy-material, rights, and fact-check audits.
- `docs/` — design specifications, implementation plans, and project assessment.
- `tests/` — source, citation, template, site, rights, and deliverable contracts.

Generated sites and manuscripts are excluded from Git. They are built from the tracked source so releases can package validated artifacts without making the repository opaque.

## Build

Requirements are Python 3.12+, `uv`, Quarto, Node.js with the builder dependencies, and a TeX runtime for PDF output.

```bash
uv sync
uv run pytest -q
uv run python scripts/check_content.py
quarto render --profile manuscript
quarto render --profile site
```

The site is written to `build-site/`. The manuscript profile writes DOCX and PDF files to `build-manuscript/`.

Publishing is automated: `.github/workflows/publish.yml` renders both profiles, runs the test suite, and deploys `build-site/` to GitHub Pages on every push to `main`. A failing test blocks deployment.

Reader-resource builders:

```bash
node scripts/build_templates.mjs
node scripts/build_question_worksheet.mjs
node scripts/build_literature_protocol.mjs
```

## Contributing

Corrections and methodologically grounded improvements are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing substantial changes. Public contributions must not include restricted archival material, confidential manuscripts, participant data, or third-party files without a documented publication basis.

## Citation

Repository citation metadata is provided in [CITATION.cff](CITATION.cff). This remains a discussion draft; cite the version actually consulted.

## Licenses

Manuscript content and templates are licensed under [CC BY 4.0](LICENSE-CONTENT.md). Project code is licensed under the [MIT License](LICENSE-CODE).
