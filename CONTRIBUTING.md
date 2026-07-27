# Contributing

Thank you for helping improve *From Question to Evidence*. The project welcomes corrections, methodological criticism, accessible examples, template improvements, and proposals for new modules.

## Start with an Issue

Open an issue before undertaking a substantial change. Describe:

- the research decision or reader problem;
- the page, template, or module affected;
- the proposed change;
- evidence or standards supporting the change;
- any privacy, copyright, accessibility, or maintenance implications.

Small corrections may proceed directly to a pull request.

For the Skills and Agents Lab, use the dedicated issue forms:

- [report a reproducible problem](https://github.com/pedahzur/from-question-to-evidence/issues/new?template=lab-problem.yml);
- [propose a governed revision](https://github.com/pedahzur/from-question-to-evidence/issues/new?template=lab-revision.yml).

Name the package version and affected artifact. Use synthetic or redacted inputs and
report both observed and expected behavior.

## Editorial Rules

- Organize stable prose around research decisions rather than products.
- Every stage page uses the approved sequence: Orientation, Learn, Worked Example, Try It, Guided AI Workflow, Integrity Checkpoint, Save the Artifact, Advanced Practice.
- Distinguish author claims, evidence, reviewer inference, and source dependence.
- Calibrate transparency to method, ethics, law, and participant protection.
- Put volatile product comparisons in dated tool cards rather than the methodological core.
- Preserve prior versions when a change alters scope, decision logic, or a reusable artifact.

## Sources and Citations

- Verify author, title, date, venue, version, DOI or stable publisher URL before adding a record.
- Check that a source supports the claim for which it is cited.
- Prefer original papers, official standards, primary documentation, and authoritative publisher records.
- Do not create citations from model memory.
- Add unresolved factual claims to `editorial/fact-check-log.md` rather than presenting them as established.

## AI and Sensitive Material

- Never place confidential, restricted, identifiable, or unlawfully copied material in an external AI system.
- Record consequential AI assistance that can change corpus composition or research claims.
- Treat model outputs as proposals or transformation records, not evidence.
- Verify every proposed citation, quotation, source, repository, and classification independently.

## Rights

Do not add third-party PDFs, book chapters, screenshots, datasets, photographs, or copied web text without a documented publication basis. Update `editorial/rights-manifest.yml` when a pull request adds a new class of material.

Contributors agree that accepted prose and templates are released under CC BY 4.0 and accepted code under the MIT License.

## Local Setup

Requirements:

- Python 3.12 or later
- `uv`
- Quarto
- Node.js with the document and spreadsheet dependencies used by the builder scripts
- A TeX runtime for PDF rendering

Run:

```bash
uv sync
uv run pytest -q
uv run python scripts/check_content.py
quarto render --profile manuscript
quarto render --profile site
```

Regenerate reader resources before committing changes to their builders:

```bash
node scripts/build_templates.mjs
node scripts/build_question_worksheet.mjs
node scripts/build_literature_protocol.mjs
```

## Pull-Request Checklist

- Tests pass.
- Both Quarto profiles render.
- New citations resolve.
- New templates open and have been visually inspected.
- Skills pass the official validator, agents remain least-privilege, and benchmark contracts pass.
- The lab ZIP and SHA-256 checksum are regenerated when a package file changes.
- Links resolve in the rendered site.
- The rights manifest and fact-check log are current.
- No private paths, credentials, restricted files, build directories, or cache files are tracked.
- The changelog describes reader-visible changes.
