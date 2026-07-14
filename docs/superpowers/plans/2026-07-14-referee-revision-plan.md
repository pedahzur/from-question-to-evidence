# Referee Revision Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Revise *From Question to Evidence* from a strong two-module discussion draft into a manuscript that answers the external referee's safety, conceptual, pedagogical, evidentiary, and scope objections.

**Architecture:** Preserve the existing Quarto book and its fixed stage-page pattern. Build from the four completed referee passes on `revise/referee-pass-2026-07-14`, then complete five larger programs: epistemological positioning, a fully worked oral-history example, a collection module, instructor/pilot apparatus, and a press-facing verification and response package.

**Tech Stack:** Quarto source (`.qmd`), BibTeX/Chicago notes, DOCX/PDF/HTML rendering, editable DOCX/XLSX resources, Python contract tests, and GitHub releases.

## Global Constraints

- Treat the current revision branch, not release `v0.2.0-draft`, as the editorial baseline.
- Do not reintroduce product-specific AI instructions; distinguish durable method from tool-dependent guidance.
- Do not use real participant data in examples, prompts, screenshots, templates, or tests.
- Keep English as the canonical first edition; Hebrew remains a later adaptation.
- Preserve live notes and verified citation metadata in rendered manuscript files.
- Use American spelling throughout, except in titles and quotations.
- Use **stage** for the book's core procedural unit.
- Use **coverage** only for coverage of a declared map, protocol, or corpus boundary, never as completeness of the phenomenon.
- Keep the terrorism example, but add a non-database example in which evidence is co-produced with participants.
- Do not publish a revised GitHub release until the authors approve the scope decision and the final rendered manuscript.

---

## Recommended Editorial Route

The recommended route is to retain the long-form living-field-guide ambition and add a full **Collection as Evidence** module. This best matches the original project and directly answers the referee's strongest scope objection. The faster alternative is to retitle and rescope the current manuscript as a short guide to building an evidence base; that route should be chosen only if the authors do not want to write the collection module in this revision cycle.

The plan below assumes the full-book route after the decision gate in Task 1.

## Current Disposition of the Referee's Priority Items

| # | Referee request | Current status on revision branch | Remaining action |
|---|---|---|---|
| 1 | Correct dangerous de-identification advice | Resolved | Verify wording against current ethics/data-protection guidance before release. |
| 2 | Add a second fully worked non-terrorism example | Outstanding | Carry a composite oral-history project through all seven evidence-map stages and the collection module. |
| 3 | Pilot with real readers | Outstanding | Create and run a documented novice/expert pilot after the substantive revision. |
| 4 | Confront interpretivist/constructivist critique | Partial | Promote the current paragraph into an early, load-bearing methodological chapter. |
| 5 | Add a collection module or rescope | Outstanding | Recommended: add the collection module. |
| 6 | Resolve one-module/two-module contradiction | Resolved | Retain regression test. |
| 7 | Standardize movement/stage | Resolved | Confirm remaining uses of “movement” are ordinary subject-matter uses. |
| 8 | Make Module 1 parallel to Module 2 | Substantially resolved | Check the final rendered pages and strengthen any thin Advanced Practice sections. |
| 9 | Define coverage matrix and working/frozen map | Resolved | Add a full visual specimen and regression test. |
| 10 | Disambiguate dimension and define source family earlier | Partial | Adopt boundary axis / question dimension / audit dimension; define source family at first front-matter use. |
| 11 | Distinguish evidence maps; add ethics and AI access caveats | Resolved in substance | Verify and cite evidence-gap-map precedent; retain caveats. |
| 12 | Correct citation/style errors | Partial | PROV-O, NIST, and em dashes are fixed; verify Chicago first-note handling of three-author works in rendered output. |
| 13 | Show the three central artifacts | Partial | Module 1 now has table fragments; add full captioned specimens of the released evidence map and synthesis matrix. |
| 14 | Engage design-methodology and AI-methods literature | Outstanding | Add and verify the missing canon and a balanced AI-methods literature set. |
| 15 | Add repository/templates and move AI guidance earlier | Partial | Repository and resources exist; make them prominent in the manuscript and move the AI chapter forward. |
| 16 | Convert checkpoints and add module crosswalk | Resolved | Retain contract tests and inspect rendered format. |
| 17 | Unify spelling and small language/cross-reference items | Partial | Complete a controlled copy-edit after structural revision. |

## Task 1: Record the Scope and Publication Decision

**Files:**
- Create: `docs/revisions/scope-and-publication-decision.md`
- Modify after author decision: `index.qmd`
- Modify after author decision: `_quarto.yml`
- Modify after author decision: `README.md`
- Modify after author decision: `ROADMAP.md`

- [ ] Write a one-page decision memo comparing two deliverables: a full living field guide with a collection module, and a short guide/Element focused on building an evidence base.
- [ ] State the recommended full-book route, the additional work it requires, and the shorter-route title: *From Question to Evidence: Building a Defensible Evidence Base*.
- [ ] Obtain Ami and Jonathan's explicit decision before drafting the collection module or changing the subtitle.
- [ ] Update the opening, roadmap, and repository description so every surface describes the same product.
- [ ] Commit as `docs(scope): record post-review publication route`.

**Acceptance criterion:** The title, subtitle, opening promise, chapter list, roadmap, and repository description describe one agreed product without deferring a central part of that product ambiguously.

## Task 2: Complete the Referee Comment Matrix and Style Sheet

**Files:**
- Create: `editorial/referee-response-matrix.md`
- Create: `editorial/style-sheet.md`
- Modify: `tests/test_book_contract.py`
- Modify: `tests/test_citations.py`

- [ ] Enter every numbered referee comment into a matrix with fields for severity, classification, response strategy, affected source files, status, verification evidence, and final response language.
- [ ] Mark the work already completed in commits `e086da8`, `5fc64de`, `20ec97b`, and `49907d2`; do not silently count a partial fix as resolved.
- [ ] Lock terminology in the style sheet: stage, collection plan, page pattern, source family, working map, frozen map, boundary axis, question dimension, and audit dimension.
- [ ] Lock American spelling and the existing hyphenation/number conventions.
- [ ] Add tests that reject procedural uses of “movement,” “one exemplary module,” unsafe de-identification shortcuts, and unqualified claims that coverage represents the phenomenon.
- [ ] Commit as `docs(editorial): map referee comments and lock terminology`.

**Acceptance criterion:** Every referee comment has one owner, one disposition, one manuscript location, and one observable completion test.

## Task 3: Make the Epistemological Position Load-Bearing

**Files:**
- Create: `content/02a-position-judgment-and-limits.qmd`
- Modify: `_quarto.yml`
- Modify: `index.qmd`
- Modify: `content/01-origins-and-purpose.qmd`
- Modify: `content/02-evidence-map-overview.qmd`
- Modify: `content/08-test-coverage.qmd`
- Modify: `content/18-synthesize-audit-stop.qmd`
- Modify: `bibliography/references.bib`
- Modify: `editorial/fact-check-log.md`

- [ ] Draft a 1,500–2,000-word early chapter explaining that the guide makes judgment inspectable rather than claiming epistemic completeness.
- [ ] State the visibility-to-rigor premise: a decision record improves criticism because readers can reconstruct selections, exclusions, transformations, and limits.
- [ ] Present the strongest interpretivist and constructivist objection to evidence, gaps, coverage, bounded questions, and stopping rules without caricature.
- [ ] Explain how the workflow changes for emergent questions, co-produced corpora, reflexive fieldwork, and categories treated as findings rather than inputs.
- [ ] Define coverage consistently as coverage of the researcher's declared map or protocol.
- [ ] Correct PROV-O transfer by preserving the entity/activity/agent mapping while stating what the ontology does not capture: intent, silence, relation, and power.
- [ ] Add and verify appropriate work by Charmaz and Schwartz-Shea/Yanow, plus case-design and inference literature where it genuinely bears on the argument.
- [ ] Commit as `feat(method): establish epistemic scope and limits`.

**Acceptance criterion:** A qualitative-methods reviewer can identify the guide's epistemological commitments, intended users, limits, and adaptation path before encountering the first procedural stage.

## Task 4: Move AI Integrity Earlier and Deepen Its Evidence Base

**Files:**
- Modify: `_quarto.yml`
- Modify: `content/19-ai-research-integrity.qmd`
- Modify: `index.qmd`
- Modify: `bibliography/references.bib`
- Modify: `editorial/fact-check-log.md`

- [ ] Move the existing AI and Research Integrity chapter to immediately precede the first guided workflow; keep the filename stable unless link testing shows a reason to rename it.
- [ ] Add a stable-versus-drifting sidebar: scholarly responsibility, data minimization, verification, and audit records are stable; model names, interfaces, pricing, context limits, retention policies, and retrieval behavior drift.
- [ ] Add an affirmative account of bounded AI value: vocabulary expansion, alternative generation, adversarial checking, and pattern comparison.
- [ ] Retain the current cost/access paragraph and expand it only where evidence supports the claim.
- [ ] Replace the single-source AI frame with a small verified set covering research integrity, qualitative-data risk, model evaluation limits, and human accountability.
- [ ] Add a visible pre-flight checklist before the first prompt-based exercise.
- [ ] Commit as `feat(ai): move integrity guidance before workflows`.

**Acceptance criterion:** No reader reaches a guided AI exercise before seeing the book's privacy, verification, access, and accountability rules.

## Task 5: Carry a Composite Oral-History Example Through the Workflow

**Default example:** A composite oral-history study of how tenants experienced and remembered a municipal housing redevelopment. It extends the existing municipal example while changing the corpus from retrieved publications to co-produced interviews, field notes, consent records, administrative documents, and researcher memos.

**Files:**
- Modify: `index.qmd`
- Modify: `content/02-evidence-map-overview.qmd`
- Modify: `content/03-frame.qmd` through `content/09-produce-evidence-map.qmd`
- Modify where useful: `content/13-define-review.qmd` through `content/18-synthesize-audit-stop.qmd`
- Create: `examples/oral-history/README.md`
- Create: `examples/oral-history/question-frame.md`
- Create: `examples/oral-history/concept-grid.csv`
- Create: `examples/oral-history/source-family-inventory.csv`
- Create: `examples/oral-history/search-log.csv`
- Create: `examples/oral-history/evidence-register.csv`
- Create: `examples/oral-history/coverage-and-stopping-rule.csv`

- [ ] Write a one-paragraph case protocol stating that the example is invented/composite and contains no real participant data.
- [ ] At every Module 1 Worked Example section, add the oral-history case's corresponding decision and a filled artifact fragment.
- [ ] Show how the researcher becomes part of provenance through interview design, recruitment, rapport, transcription, interpretation, and preservation.
- [ ] Show how consent and withdrawal conditions constrain the map before collection begins.
- [ ] Demonstrate why silence, refusal, memory, unequal access, and co-production cannot be treated as ordinary empty cells.
- [ ] Carry the case to a justified stopping rule without claiming population coverage or saturation automatically.
- [ ] Retain the terrorism case as the documentary/database contrast and use explicit comparison sentences rather than alternating examples without explanation.
- [ ] Commit as `feat(example): add full oral-history evidence-map case`.

**Acceptance criterion:** The reader can follow one non-database project from question frame to frozen map, inspect each intermediate artifact, and see where the method changes because evidence is co-produced.

## Task 6: Add Complete, Captioned Artifact Specimens

**Files:**
- Create: `assets/figures/filled-evidence-map.svg`
- Create: `assets/figures/filled-concept-grid.svg`
- Create: `assets/figures/filled-synthesis-matrix.svg`
- Create: `examples/completed-resources/`
- Modify: `content/02-evidence-map-overview.qmd`
- Modify: `content/04-decompose.qmd`
- Modify: `content/17-read-annotate-compare.qmd`
- Modify: `tests/test_book_contract.py`
- Modify: `tests/test_rendered_site.py`

- [ ] Produce a compact filled specimen of the working/frozen evidence map using the oral-history case.
- [ ] Produce a filled concept-grid specimen with two or three question dimensions and explicit rival meanings.
- [ ] Produce a filled synthesis-matrix specimen with source IDs, claims, evidence, method, dependence, limitation, and verification location.
- [ ] Caption each visual so the reader knows what decision it demonstrates and where to download the editable version.
- [ ] Add completed sample workbooks separate from blank templates.
- [ ] Test that all figures and download links appear in DOCX, PDF, and HTML builds.
- [ ] Commit as `feat(resources): add filled artifact specimens`.

**Acceptance criterion:** The book's three central artifacts are visible in the manuscript, legible in every format, and available as completed examples and blank editable resources.

## Task 7: Write the Collection as Evidence Module

**Files:**
- Create: `content/21-collection-as-evidence.qmd`
- Create: `content/22-plan-permission-and-access.qmd`
- Create: `content/23-capture-encounters-and-records.qmd`
- Create: `content/24-record-context-and-provenance.qmd`
- Create: `content/25-transform-without-losing-lineage.qmd`
- Create: `content/26-secure-store-and-preserve.qmd`
- Create: `content/27-audit-and-release-the-corpus.qmd`
- Modify: `_quarto.yml`
- Modify: `ROADMAP.md`
- Modify: `content/20-next-steps.qmd`
- Create: `templates/collection-protocol.docx`
- Create: `templates/permission-access-register.xlsx`
- Create: `templates/field-capture-log.xlsx`
- Create: `templates/transformation-provenance-log.xlsx`
- Create: `templates/collection-audit-handoff.xlsx`
- Modify: `scripts/build_templates.mjs`
- Modify: `tests/test_templates.py`
- Modify: `tests/test_book_contract.py`

- [ ] Approve a six-stage module specification before drafting prose.
- [ ] Cover ethical permission and access as preconditions, not afterthoughts.
- [ ] Cover documents, interviews, observation, audio, images, web material, and born-digital records without pretending one capture procedure fits all.
- [ ] Treat OCR, transcription, translation, coding preparation, and file conversion as transformations that require lineage and quality checks.
- [ ] Cover naming, metadata, storage, backup, access control, chain of custody, preservation, withdrawal, and deletion obligations.
- [ ] End with an auditable corpus handoff linking records to permissions, provenance, transformations, restrictions, and the evidence map.
- [ ] Use the oral-history project throughout and short documentary contrasts where useful.
- [ ] Give each stage the established eight-part page pattern, allowing longer Advanced Practice sections where expert judgment is the point.
- [ ] Build and visually verify all five editable resources.
- [ ] Commit the specification, content, and resources in reviewable increments rather than one monolithic commit.

**Acceptance criterion:** The title's promise now extends from question and literature discovery through responsible collection and preparation of a research corpus.

## Task 8: Add Instructor Apparatus and Run a Reader Pilot

**Files:**
- Create: `instructor/README.md`
- Create: `instructor/learning-objectives.md`
- Create: `instructor/artifact-rubrics.md`
- Create: `pilot/pilot-protocol.md`
- Create: `pilot/task-script.md`
- Create: `pilot/feedback-form.md`
- Create after the pilot: `pilot/pilot-results.md`
- Modify after the pilot: affected `content/*.qmd` and `templates/*`

- [ ] Define observable learning objectives for each module and each saved artifact.
- [ ] Create a four-level rubric for question framing, provenance, source diversity, traceability, ethical constraint handling, verification, and stopping-rule justification.
- [ ] Design a pilot with 6–8 graduate-student readers and 2–3 experienced researchers, subject to availability.
- [ ] Ask each participant to complete one full pathway and record time, stalls, misinterpretations, skipped sections, artifact quality, and perceived burden.
- [ ] Check institutional requirements before collecting or publishing participant feedback; if formal research approval is required, obtain it before recruitment.
- [ ] Analyze novice and experienced-reader results separately so “two readers, two speeds” is tested rather than asserted.
- [ ] Revise the scaffold where readers consistently stall; do not preserve all eight sections merely for symmetry.
- [ ] Report the pilot honestly, including sample limits and changes made.
- [ ] Commit as `feat(pedagogy): add instructor apparatus and pilot evidence`.

**Acceptance criterion:** The manuscript can point to documented reader use, concrete learning outcomes, and revisions made because of observed difficulties.

## Task 9: Complete Literature, Citation, and Copy-Editing Passes

**Files:**
- Modify: `bibliography/references.bib`
- Modify: `editorial/fact-check-log.md`
- Create: `editorial/citation-audit-v0.3.md`
- Modify: `index.qmd` and `content/*.qmd`
- Modify if needed: CSL configuration in `_quarto-manuscript.yml`
- Modify: `tests/test_citations.py`

- [ ] Add only sources that carry an explicit argumentative load; verify metadata against DOI, publisher, library, standards-body, or project records.
- [ ] Address the referee's missing conversations: inference/design, case-study research, data display and matrices, case selection, constructivist grounded theory, interpretive research design, evidence-gap maps, and AI/research-methods integrity.
- [ ] Render the notes and verify Chicago treatment of every first citation with two or three authors; fix output rather than only the BibTeX source.
- [ ] Run a controlled American-spelling pass and correct the remaining small language issues without revising quotations or titles.
- [ ] Verify all proper nouns, standards titles, agency names, dates, URLs, and DOIs.
- [ ] Commit as `fix(editorial): complete source and style audit`.

**Acceptance criterion:** Every citation resolves, every reference is used, first-note forms follow the chosen Chicago rule, and the copy-edit does not create inconsistencies across formats.

## Task 10: Verify, Respond, and Package the Revised Draft

**Files:**
- Create: `editorial/response-to-referee.md`
- Modify: `CHANGELOG.md`
- Modify: `CITATION.cff`
- Modify: `README.md`
- Modify: `tests/test_deliverables.py`
- Create in outputs: `From-Question-to-Evidence-Revision-Draft.docx`
- Create in outputs: `From-Question-to-Evidence-Revision-Draft.pdf`
- Create in outputs: `Referee-Response-and-Revision-Summary.md`

- [ ] Run the full source, citation, rights, template, rendered-site, and deliverable test suite.
- [ ] Render DOCX, PDF, and HTML from a clean tree and inspect every page/sheet for overflow, clipping, orphan headings, broken notes, and unreadable exhibits.
- [ ] Re-read the referee report line by line against `editorial/referee-response-matrix.md`.
- [ ] Draft a response organized by reviewer concern: acknowledge, state the change or reasoned limitation, and give exact revised locations.
- [ ] Distinguish completed revisions from future-work commitments; do not claim the reader pilot until it has occurred.
- [ ] Update version metadata to `0.3.0-draft` only after the substantive and pilot gates pass.
- [ ] Present the final manuscript and response package to Ami and Jonathan for approval before merging to `main` or creating a GitHub release.

**Verification commands:**

```bash
uv run pytest -q
uv run python scripts/check_content.py
quarto render --profile manuscript
quarto render --profile site
git diff --check
git status --short
```

**Acceptance criterion:** Tests and builds pass, visual inspection is complete, every referee comment has a documented disposition, and the authors approve the package before publication.

## Suggested Sequence and Effort

1. **Immediate editorial repair:** Tasks 1–4 and remaining copy/citation checks, approximately 3–5 focused working days after the scope decision.
2. **Demonstration and artifacts:** Tasks 5–6, approximately 5–8 working days.
3. **Collection module:** Task 7, approximately 10–15 working days including resource design and review.
4. **Reader pilot:** Task 8, approximately 4–6 weeks elapsed time for recruitment, use, analysis, and revision; hands-on editorial work is smaller.
5. **Final audit and response:** Tasks 9–10, approximately 3–5 working days after pilot-driven changes stabilize.

The scope decision and the reader pilot are the critical path. Copy edits and terminology fixes should not delay conceptual drafting, but the manuscript should not be represented as publisher-ready until the second example, scope issue, methodological positioning, and reader-testing claims are resolved.

## Self-Review

- Every critical and major referee request maps to at least one task.
- Existing fixes are preserved and marked accurately rather than planned again.
- External actions—author scope approval, participant recruitment, ethics review, merge, and release—have explicit gates.
- No task requires real participant data in AI systems or public artifacts.
- Every substantive program ends with an inspectable manuscript, resource, test, or response artifact.
