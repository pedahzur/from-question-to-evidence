# Task Plan: Manuscript Gap-Closure Program

## Goal

Create a detailed, executable editorial plan that closes the gaps identified in the 4 August 2026 manuscript audit and moves *From Question to Evidence* toward a coherent, tested, full-lifecycle qualitative-methods textbook.

## Phases

- [x] Phase 1: Confirm the current manuscript, audit findings, roadmap, and existing project plans.
- [x] Phase 2: Convert every blocker and major weakness into a workstream with dependencies and acceptance criteria.
- [x] Phase 3: Produce a chapter-disposition map, six-part target architecture, pilot program, and release gates.
- [x] Phase 4: Review the plan for feasibility, sequencing, ownership, and scope control.
- [x] Phase 5: Integrate the final plan into the Methods Textbook project record and verify it.

## Key Questions

1. Which current chapters remain core, and which move to specialist, interlude, companion, or archive status?
2. Which missing modules must be written before the subtitle and project description become accurate?
3. What must be decided before drafting begins?
4. What evidence will show that the pedagogy works for novice and experienced readers?
5. What gates must be passed before a numbered draft or public release?

## Decisions Made

- The plan will preserve the approved long-form, open-access living-field-guide route.
- Jonathan is not an active dependency; Ami holds active editorial decision authority.
- The plan will not line-edit or rewrite manuscript chapters.
- Work will be sequenced architecture first, missing spine second, pilot third, line edit and publication last.
- The final effort range is 90–130 focused editorial days plus 6–8 weeks of elapsed pilot time.
- The target architecture contains 45 content units to be consolidated into approximately 32–36 numbered chapters.
- On 4 August 2026, Ami approved the architecture package as proposed: the six-part structure, chapter-disposition map, ten-stage lifecycle, composite municipal oral-history case, and provisional 75,000–90,000-word body target with a separate companion boundary.
- Structural implementation will proceed on `feature/manuscript-gap-closure`; Working Edition 0.2 remains frozen.

## Errors Encountered

- `uv run pytest -q` could not open the default user cache under sandboxed execution. Rerun with a task-specific cache under `/private/tmp`; no project file or test logic was implicated.
- The first vault-note copy used paths relative to the canonical checkout instead of the staging checkout. The bundle and source-snapshot operations succeeded; the missing note copies were rerun from explicit absolute staging paths, with unrelated vault changes left untouched.

## Status

**Architecture approved; G0 passed; WS1/G1 in progress** — the formal decision, pre-restructure baseline, restorable bundles, dedicated revision branch, and public-release freeze are verified. No manuscript prose has changed. The next bounded deliverables are the book contract and terminology sheet; G1 remains open until its complete acceptance package is verified.
