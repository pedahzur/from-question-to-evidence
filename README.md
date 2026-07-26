# From Question to Evidence

*A Living Field Guide for Qualitative Research*

This repository contains the English first-edition source, editable resources, and reproducible website for an open-access field guide by Ami Pedahzur and Jonathan Grossman.

The guide follows a qualitative project from its first question to a documented corpus, an analysis, and a public claim. It treats the research record as a scholarly Second Brain: a system that connects capture, organization, distillation, and expression while preserving the decisions that shape a corpus. Generative AI appears as a bounded research aid. It does not replace source reading, verification, ethical judgment, or responsibility for synthesis.

## Publication Route

The project is being developed as a long-form living field guide, not as a short guide limited to evidence-base construction. Reviewed modules will be published in increments, but they belong to one book covering evidence mapping, literature, collection, preparation, analysis, claim testing, writing, responsible sharing, and maintenance.

The working scope decision is recorded in [docs/revisions/scope-and-publication-decision.md](docs/revisions/scope-and-publication-decision.md). Ami Pedahzur approved this route on 25 July 2026. Jonathan Grossman's confirmation remains a gate before the Collection as Evidence module is drafted for publication or a revised release is issued.

## Current Draft

Version `0.2.0-draft` contains the first two complete modules:

1. **From Question to Evidence Map** — seven stages from framing to a collection strategy and stopping rule.
2. **Literature as Evidence** — six stages from review protocol to synthesis, coverage audit, and stopping rule.

The working branch also contains **Review Articles and Meta-Analysis in Transition**, which connects the literature workflow to contemporary evidence synthesis, and **Building Event Databases with AI**, a bridge chapter on large-scale source discovery, candidate-record verification, event resolution, dynamic codebooks, validation, and explicit Bayesian updating. The next revision program adds an early chapter on epistemic judgment and limits, moves AI integrity before the first guided workflow, carries a composite oral-history case through the method, supplies complete artifact specimens, and adds the Collection as Evidence module. See [ROADMAP.md](ROADMAP.md).

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

The site is written to `build-site/`. The manuscript profile writes DOCX, PDF, and complete Markdown files to `build-manuscript/`. The Markdown export is regenerated automatically from the rendered Word manuscript so citations and footnotes remain aligned across formats.

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
