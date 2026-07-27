# What the AI Got Wrong

## Verification status

This v0.1.0 report records problems exposed while the release was designed and the
three synthetic cases were executed manually against the skill contract. It is an
authoring-run report, not an independent evaluation of a named model. The benchmark
inputs and expected outputs were created by the same team, so passing them
demonstrates contract consistency rather than general model accuracy.

No claim about recall, precision, labor saved, or performance on a real literature
database is made in this release.

## 1. A plausible citation entered without provenance

**Failure.** During the boundary case, a plausible title and year could easily be
converted into a candidate row even though no author, venue, identifier, or locator
was available.

**Why it matters.** Once placed beside verified candidates, an invented or
misremembered citation acquires false authority and may later be treated as a
screened source.

**Control added.** The skill now requires a retrievable `source_locator` for the
candidate register. Unsupported citations go to `unresolved-leads.md`; missing
metadata remains missing.

**Residual risk.** A locator may resolve to an unreliable or mismatched page. Human
identity verification remains necessary.

## 2. A zero-result query became a research-gap claim

**Failure.** The initial false-gap query returned no results. Without a vocabulary
audit, the most fluent conclusion was that the subject had not been studied.

**Why it matters.** The supplied expanded searches recovered records using a
conceptual proxy and an approved Spanish term. The apparent gap was partly an
indexing and vocabulary problem.

**Control added.** The coverage memo must test proxies, historical terms,
disciplinary variants, and approved local-language vocabulary. Gap claims remain a
human gate.

**Residual risk.** No finite vocabulary audit proves field-wide absence. Access,
language, and database coverage must remain explicit limitations.

## 3. Deduplication erased evidence about discovery

**Failure.** Resolving two rows with the same persistent identifier could retain
only the first route and query.

**Why it matters.** Route diversity is part of the coverage argument. Erasing the
second route makes later audits underestimate independent paths to the source.

**Control added.** The retained candidate stores all discovery routes and query
identifiers. The known-item benchmark fails if either route is discarded.

**Residual risk.** Title-based near-duplicate resolution remains interpretive when
persistent identifiers are unavailable.

## 4. Scope signaling drifted into eligibility

**Failure.** A 2017 record outside a 2020–2025 boundary invited the categorical
label “excluded.”

**Why it matters.** The scout has no authority to make the final eligibility
decision or amend the date boundary.

**Control added.** The candidate receives the scope signal `unlikely`, a note names
the boundary, and the researcher adjudicates it. Final-decision fields are
prohibited by the candidate schema.

**Residual risk.** Readers may still interpret scope signals as decisions. Training
and interface design should keep staging visibly separate from the verified corpus.

## 5. Broad context encouraged unauthorized retrieval

**Failure.** The boundary packet named a restricted archive. A general-purpose
agent might treat that mention as permission to locate or summarize it.

**Why it matters.** Knowledge of an artifact is not authorization to access it.

**Control added.** The context template separates restricted material from
task-local inputs. The agent is read-only, uses approved public sources, and must
stop on access controls or participant-derived content.

**Residual risk.** Tool permissions cannot interpret every ethics agreement.
Researchers must prepare the context packet and source list before execution.

## What this release still does not establish

The release has not yet been independently forward-tested on a real review. It does
not establish:

- recall against a known scholarly corpus;
- false-exclusion rates across languages or disciplines;
- reliable citation resolution at scale;
- performance under changing search interfaces;
- equivalence across model vendors;
- time or cost savings after human verification.

Those are evaluation questions for a later release. Version 0.1.0 establishes a
bounded procedure, an inspectable output contract, and failure-oriented benchmark
fixtures.
