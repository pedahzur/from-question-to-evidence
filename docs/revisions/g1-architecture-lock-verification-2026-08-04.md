# G1 Architecture-Lock Verification

## Decision

- **Project:** *From Question to Evidence: A Living Field Guide for Qualitative Research*
- **Gate:** G1, Architecture lock
- **Decision date:** 4 August 2026
- **Decision authority:** Ami Pedahzur
- **Result:** Passed

G1 passes because the approved architecture, chapter-disposition plan, book contract, terminology sheet, research-lifecycle crosswalk, and revised roadmap now form one consistent package. This gate does not authorize a public release, source-file renumbering, or a change in authorship credit.

## Acceptance evidence

| G1 criterion | Evidence | Result |
|---|---|---|
| Every current and planned chapter has one purpose, one destination, and one principal artifact or claim | The chapter-disposition map and target content map in `plan/manuscript-gap-closure-2026-08-04/manuscript-gap-closure-plan.md` assign each current and planned unit a disposition and destination. `ROADMAP.md` specifies the purpose, required work, principal artifacts, dependency, and gate for each Part. | Pass |
| No numbered chapter exists mainly to document a software release | The book contract, terminology sheet, approval record, lifecycle crosswalk, and roadmap place installation guidance, dated tool cards, product comparisons, implementation instructions, benchmarks, the full Readwise audit, and the Skills and Agents Lab in companion material. | Pass |
| The book promise can be stated in one sentence and mapped to Parts I–VI | `docs/revisions/book-contract-2026-08-04.md` states the one-sentence promise and gives one reader outcome and principal durable result for every Part. The roadmap repeats the promise and makes the six-Part dependency chain explicit. | Pass |
| The research lifecycle subsumes all secondary sequences | `docs/revisions/research-lifecycle-crosswalk-2026-08-04.md` maps the evidence-map, literature, mirrored-newspaper, review and meta-analysis, event-database, historical-sources, PKM-AI, writing-by-voice, and composite oral-history pathways to the ten stages. It also records legitimate omissions and treats AI integrity as an overlay rather than an eleventh stage. | Pass |
| No manuscript prose has been line-edited prematurely | The G1 change set is confined to architecture, planning, approval, terminology, contract, crosswalk, verification, and roadmap records. No file under `content/` or other manuscript source path changed during G1. | Pass |

## Consistency checks

- The reader-facing term is `research lifecycle`; `master lifecycle` remains limited to older internal records or governance contexts.
- The lifecycle order is Position, Frame, Design evidence, Discover, Collect, Prepare, Analyze, Test claims, Express, and Release and maintain.
- The six Parts, composite municipal oral-history case, provisional 75,000–90,000-word body target, and companion boundary match the approved package.
- Working Edition 0.2 remains frozen and citable.
- Jonathan is not an active workflow dependency. His existing authorship credit is unchanged.
- The public release authority belongs to the active editorial decision maker and is exercised through a separate release decision after the relevant gates pass.

## Repository verification

- Documentation whitespace check: passed.
- Existing automated test suite: 57 passed.
- Manuscript source check: no changed file under `content/`.
- Public release check: no release, tag, deployment, or public-edition change was made.

## Authorized next work

WS2 may begin. Its first bounded deliverable is the specification and source plan for “Judgment, Position, and the Limits of Evidence,” followed by the AI pre-flight gate. Drafting must remain on the revision branch. No public release or source-file renumbering is authorized.
