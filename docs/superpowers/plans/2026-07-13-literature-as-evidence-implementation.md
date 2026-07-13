# Literature as Evidence Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a complete six-stage *Literature as Evidence* module, five editable resources, refreshed manuscript/site packages, and publish the organized project as `pedahzur/from-question-to-evidence`.

**Architecture:** Keep Quarto Markdown as the single source for the site and manuscript. Add an overview and six stage pages using the established eight-section contract, generate DOCX/XLSX resources from scripts, test source structure and rendered outputs, then publish only verified tracked source to GitHub.

**Tech Stack:** Quarto; QMD; BibTeX; Python 3.12 with pytest, python-docx, openpyxl, PyMuPDF, and PyYAML; JavaScript with `@oai/artifact-tool`; Git; GitHub CLI.

## Global Constraints

- English is canonical; Hebrew follows later.
- The module is 8,000–10,000 words across one overview and six stages.
- Every stage uses: Orientation, Learn, Worked Example, Try It, Guided AI Workflow, Integrity Checkpoint, Save the Artifact, Advanced Practice.
- The terrorism-database inquiry is primary; archival institutional change is the compact secondary example.
- AI actions state permitted input, prohibited input, verification, and audit-record requirements.
- Product-specific guidance stays outside the stable methodological core.
- Legacy prose is rewritten; copied third-party material and unverified quotations are excluded.
- Resources: one DOCX protocol and four XLSX workbooks.
- The GitHub repository is public; content remains CC BY 4.0 and code MIT.

## File Map

Create `content/12-literature-as-evidence.qmd` through `content/18-synthesize-audit-stop.qmd`; five resources under `templates/`; `scripts/build_literature_protocol.mjs`; `docs/PROJECT-ASSESSMENT-HE.md`; `ROADMAP.md`; `CONTRIBUTING.md`; and `CHANGELOG.md`.

Rename `content/10-ai-research-integrity.qmd` to `content/19-ai-research-integrity.qmd` and `content/11-next-steps.qmd` to `content/20-next-steps.qmd`.

Modify the Quarto configuration, template builder, tests, bibliography, framing chapters, editorial audits, README, rights manifest, and citation metadata.

## Task 1: Define the Module Contract

**Files:** `tests/test_book_contract.py`, `_quarto.yml`, and `content/*.qmd`.

- [ ] Add the seven new paths to `CHAPTERS` and define `LITERATURE_STAGES`.
- [ ] Add this failing structural test:

```python
STAGE_SECTIONS = [
    "Orientation", "Learn", "Worked Example", "Try It",
    "Guided AI Workflow", "Integrity Checkpoint",
    "Save the Artifact", "Advanced Practice",
]

def test_literature_stages_follow_page_pattern() -> None:
    for relative in LITERATURE_STAGES:
        text = (ROOT / relative).read_text(encoding="utf-8")
        headings = re.findall(r"^## (.+)$", text, flags=re.MULTILINE)
        assert headings == STAGE_SECTIONS, relative
```

- [ ] Run `uv run pytest tests/test_book_contract.py -q`; expect missing-file failures.
- [ ] Rename the two later chapters with patch-based moves and create seven metadata-complete QMD shells.
- [ ] Update `_quarto.yml` so the literature module follows the evidence-map stages and precedes AI integrity.
- [ ] Run `uv run pytest tests/test_book_contract.py -q && uv run python scripts/check_content.py`; expect PASS.
- [ ] Commit with `git commit -m "test(content): define literature module contract"`.

## Task 2: Write the Complete Module

**Files:** `content/12-literature-as-evidence.qmd` through `content/18-synthesize-audit-stop.qmd`.

- [ ] Add a failing test that joins those files, counts 8,000–10,000 words, and requires `Permitted input`, `Do not provide`, `Verify`, and `Record` at least six times each.
- [ ] Run the focused test; expect a word-count failure.
- [ ] Write the overview: central claim, distinction among bibliography/reading list/review/synthesis, six movements, artifact flow, two-speed audience, examples, AI division of labor, and site-only resource cards.
- [ ] Write Stage 1 on review purpose, question, scope, inclusion/exclusion logic, and the versioned review protocol.
- [ ] Write Stage 2 on contested concepts, historical terms, disciplinary synonyms, translations, acronyms, adjacent terms, and exclusions.
- [ ] Write Stage 3 on database search, backward/forward citation chaining, author and institution tracing, review-source orientation, web discovery, and route logging.
- [ ] Write Stage 4 on relevance, publication context, evidence base, method, citation lineage, limitations, and intended argumentative role; metrics remain signals rather than verdicts.
- [ ] Write Stage 5 on author claim, evidence, method, limitation, reviewer interpretation, and cross-source comparison.
- [ ] Write Stage 6 on synthesis by pattern/dispute/lineage/method, coverage audit, dependence, stopping, and reopening.
- [ ] Run structural, size, citation-key, and content checks.
- [ ] Commit with `git commit -m "feat(content): add literature as evidence module"`.

## Task 3: Build Five Reader Resources

**Files:** `scripts/build_templates.mjs`, `scripts/build_literature_protocol.mjs`, `tests/test_templates.py`, `_quarto-site.yml`, `templates/`.

- [ ] Extend `EXPECTED` with these exact contracts:

```python
"literature-concept-vocabulary-map.xlsx": ["Concepts", "Vocabulary", "Instructions"],
"literature-search-ai-log.xlsx": ["Search Routes", "Citation Chaining", "AI Audit", "Instructions"],
"literature-source-evaluation.xlsx": ["Source Register", "Claim Register", "Instructions"],
"literature-synthesis-stopping-rule.xlsx": ["Synthesis Matrix", "Coverage Audit", "Memo Plan", "Stopping Rule", "Instructions"],
```

- [ ] Add a DOCX test requiring `Literature Review Protocol`, `Review purpose`, `Inclusion logic`, `Exclusion logic`, `Reopening trigger`, and `CC BY 4.0`.
- [ ] Run `uv run pytest tests/test_templates.py -q`; expect missing-file failures.
- [ ] Extend `build_templates.mjs` with the four tested workbooks and stable ID/date/provenance/decision fields; retain an empty reader row and Instructions sheet.
- [ ] Create `build_literature_protocol.mjs` using the existing worksheet visual language and sections for identity, purpose, question, boundaries, inclusion, exclusion, routes, AI/data restrictions, synthesis, stopping, reopening, version, and license.
- [ ] Run `node scripts/build_templates.mjs && node scripts/build_literature_protocol.mjs`.
- [ ] Add direct site links to the five resources and preserve manuscript-safe descriptions.
- [ ] Run template and internal-link tests; expect PASS.
- [ ] Commit with `git commit -m "feat(resources): add literature review templates"`.

## Task 4: Verify Sources and Legacy Use

**Files:** `bibliography/references.bib`, `tests/test_citations.py`, `editorial/legacy-audit.csv`, `editorial/fact-check-log.md`.

- [ ] Raise the unique bibliography-key floor from 8 to 16 and run the test; expect failure.
- [ ] Verify and add authoritative records for literature-review methods, citation searching, search reporting, qualitative synthesis, concept formation, transparency, and AI-assisted scholarship. Confirm title, authors, venue, year, and DOI or publisher URL before entry.
- [ ] Record `How Not to Drown`, `Technology in the Service of Literature Reviews`, `TEXTBOOK OUTLINE + TEXT`, the 2018 assessment, and the prospectus in the legacy audit with `rewrite`, `background only`, or `exclude` and a rights rationale.
- [ ] Add externally verifiable claims to the fact-check log with status and source/action.
- [ ] Run `uv run pytest tests/test_citations.py -q && uv run python scripts/check_content.py`; expect PASS.
- [ ] Commit with `git commit -m "docs(research): verify literature module sources"`.

## Task 5: Organize Public Project Documentation

**Files:** `README.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `CITATION.cff`, `docs/PROJECT-ASSESSMENT-HE.md`, framing chapters, editorial note, rights manifest.

- [ ] Add a failing test requiring all five public project documents.
- [ ] Revise Origins and Purpose to describe two completed modules; revise Beyond the Pilot so collection/post-production is next.
- [ ] Update the editorial note to Jonathan with the new module, artifacts, and review questions.
- [ ] Preserve the approved Hebrew assessment at `docs/PROJECT-ASSESSMENT-HE.md`.
- [ ] Write ROADMAP with completed/next/later modules; CONTRIBUTING with editorial, citation, rights, privacy, test, and build rules; CHANGELOG with 0.1 and 0.2 entries.
- [ ] Rewrite README with purpose, status, modules, layout, prerequisites, build/test commands, licensing, citation, and contribution route.
- [ ] Set `CITATION.cff` to `0.2.0-draft`, date `2026-07-13`; extend the rights manifest to the new public documents.
- [ ] Run book-contract and rights tests; expect PASS.
- [ ] Commit with `git commit -m "docs(project): organize public field guide repository"`.

## Task 6: Render and Verify the Expanded Book

**Files:** `tests/test_deliverables.py`, generated `build-site/` and `build-manuscript/`.

- [ ] Raise deliverable expectations to at least 19 Heading 1 paragraphs and 15,000 words; require `Literature as Evidence`, `Synthesis Matrix`, and `Stopping Rule`; retain live-note assertions.
- [ ] Run deliverable tests against the old build; expect failure.
- [ ] Run `quarto render --profile site` and `quarto render --profile manuscript`.
- [ ] Run `uv run pytest -q && uv run python scripts/check_content.py`; expect full PASS.
- [ ] Inspect overview and one stage at desktop and narrow widths; inspect DOCX headings/live notes; render representative PDF pages and check title, contents, module transition, stage, references, and overflow.
- [ ] Commit test changes with `git commit -m "test(build): verify expanded manuscript and site"`.

## Task 7: Refresh the Sharing Package

**Files:** canonical manuscript, site ZIP, source ZIP, and verification report under `/Users/amipedahzur/Documents/Codex/2026-07-12/new-chat/outputs/`.

- [ ] Copy verified DOCX/PDF to the canonical discussion-draft filenames without overwriting the user's separately renamed PDF copy.
- [ ] Zip `build-site/` as the preview and create the source ZIP from `git ls-files`, excluding Git metadata, builds, caches, and private material.
- [ ] Update the verification report with word/page counts, template/test counts, render and link checks, visual inspection, branch, commit, and limitations.
- [ ] Verify every output is non-empty; open the manuscript files and list both ZIP archives.

## Task 8: Create and Populate GitHub

**Target:** `https://github.com/pedahzur/from-question-to-evidence`.

- [ ] Run `gh --version && gh auth status`; require an authenticated `pedahzur` account.
- [ ] Run `git status -sb`, `git diff --check`, and inspect `git ls-files`; require a clean worktree with no builds, caches, private archives, secrets, or absolute user paths.
- [ ] Run `gh repo view pedahzur/from-question-to-evidence`; require a not-found result. Stop on a name collision.
- [ ] Rename the branch with `git branch -m main`.
- [ ] Create the remote with:

```bash
gh repo create pedahzur/from-question-to-evidence \
  --public \
  --source=. \
  --remote=origin \
  --description "An open-access living field guide for qualitative research in the information age"
git push -u origin main
```

- [ ] Add topics with `gh repo edit`: `qualitative-research`, `research-methods`, `open-access`, `scholarly-communication`, `artificial-intelligence`. Leave homepage blank until hosting is approved.
- [ ] Verify visibility, default branch, URL, description, topics, README, licenses, content, templates, bibliography, tests, documentation, and audits through GitHub.
- [ ] Confirm ignored generated builds and private legacy material are absent.

## Final Verification

- [ ] Confirm `git status -sb` is clean and tracks `origin/main`.
- [ ] Run `uv run pytest -q` after publication.
- [ ] Open the public repository and verify README rendering and file organization.
- [ ] Report the repository URL, latest commit, manuscript statistics, checks, artifacts, and remaining editorial limitations.
