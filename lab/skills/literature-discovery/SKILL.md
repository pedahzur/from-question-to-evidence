---
name: literature-discovery
description: Run a bounded, auditable scholarly literature-discovery pass from an approved review protocol and versioned project-context packet. Use when a researcher needs to expand search vocabulary, execute or document multiple discovery routes, deduplicate and verify bibliographic leads, produce a candidate register and coverage memo, or update an existing review without allowing AI to make final inclusion or exclusion decisions.
---

# Literature Discovery

Turn a review question into a staged register of traceable bibliographic
candidates. Preserve how each candidate was found, separate identity verification
from substantive eligibility, and return consequential judgments to the researcher.

## Inputs

Require these artifacts before discovery:

1. A review protocol containing the question, boundaries, source types, date and
   language rules, known-item set, and stopping rule.
2. A project-context packet with a version, authority status, stable layer,
   current-state layer, and task layer.
3. An approved source list or explicit permission to search named public sources.
4. A run identifier and an output location or an instruction to return the result
   without writing it.

Accept a partial input only when the task is explicitly exploratory. Label the run
`exploratory`, name every missing artifact, and do not make coverage or gap claims.

Do not request participant data, restricted archival content, unpublished peer
review, credentials, or a full project archive. Use the minimum context required.

## Workflow

### 1. Run the preflight

- Record the protocol version, project-context version, run identifier, date, and
  approved sources.
- Confirm the unit of review and the boundary conditions.
- Identify the human decision that this discovery run will support.
- Stop if the protocol and project-context packet conflict on the question, scope,
  or authority status.

### 2. Build the concept and vocabulary map

- Separate central concepts, populations, settings, periods, mechanisms, outcomes,
  methods, and exclusions.
- Add synonyms, historical terms, operational proxies, disciplinary variants, and
  approved non-English terms.
- Mark every AI-proposed term as `proposed` until a researcher or a verified source
  supports it.
- Preserve terms that produced no results; a failed query is part of the audit
  record.

### 3. Design discovery routes

Use more than one route when the protocol permits it:

- structured database or catalogue search;
- backward citation search;
- forward citation search;
- author, project, or institution search;
- journal or venue search;
- repository, archive, or grey-literature search;
- terminology and local-language search;
- hand search of a bounded source.

Assign each route and query a stable `query_id`. Record the exact query, source,
filters, date, result count, and access limitations.

### 4. Discover and stage candidates

- Search only approved public sources and collections.
- Create one candidate row per possible bibliographic object.
- Record a `source_locator` that allows another researcher to revisit the lead.
- Record every `discovery_route`; do not discard a second route during
  deduplication.
- Treat model recall as a vocabulary lead, never as a bibliographic discovery
  route.
- Do not add a candidate whose existence cannot be tied to a retrievable locator.
  Put unsupported citations in the unresolved-leads section instead.

Use the fields in
[`references/candidate-register-schema.yml`](references/candidate-register-schema.yml).
The core audit fields are `candidate_id`, `source_locator`, `discovery_route`,
`query_id`, `verification_status`, and `scope_signal`.
Validate a CSV register with:

```bash
python scripts/validate_candidate_register.py path/to/candidate-register.csv
```

### 5. Resolve identities without deciding eligibility

- Compare persistent identifiers first, then exact metadata, then normalized title,
  author, year, and venue.
- Preserve all discovery routes on the retained record.
- Use `duplicate_of` only when the identity match is defensible.
- Distinguish `verified`, `partially-verified`, `unverified`, and `unavailable`.
- Keep substantive scope as a signal: `known-item`, `possible`, `unlikely`, or
  `uncertain`.

Do not decide final eligibility. Do not convert `unlikely` into exclusion or
`possible` into inclusion.

### 6. Test discovery coverage

- Check recovery of the protocol's known-item set.
- Compare coverage across vocabulary families, routes, languages, periods, source
  types, and settings.
- Look for route dependence: a large register from one index is not diverse
  coverage.
- Search for false-gap explanations such as unfamiliar terminology, inaccessible
  indexes, local-language sources, or an incorrect boundary.
- Apply the protocol's stopping rule. If it cannot be applied, state why.

### 7. Return the handoff

Return four artifacts:

1. `candidate-register.csv`;
2. `query-log.csv` or an equivalent structured table;
3. `coverage-memo.md`;
4. `unresolved-leads.md`.

Begin the coverage memo with the protocol version, context version, run identifier,
approved sources, and verification date. End with the next human decisions.

## Human gates

Require an identified researcher to:

- approve vocabulary that changes the protocol;
- approve source-list or boundary changes;
- adjudicate final inclusion and exclusion;
- authorize any claim that a field, population, mechanism, or method is absent;
- promote candidates into the verified corpus;
- approve publication of the register or coverage claim.

Record the decision, decision maker, date, affected candidates, and downstream
artifact versions.

## Failure and abstention

Stop and report the boundary when:

- the protocol or context packet is absent, stale, or contradictory;
- a source requires credentials or access not explicitly approved;
- a query would expose restricted or participant-derived material;
- rate limits, language limits, or access barriers make the planned coverage
  impossible;
- the requested output requires final eligibility or a field-level gap claim;
- a candidate cannot be connected to a source locator;
- the evidence needed to resolve a bibliographic identity is unavailable.

Never fill missing bibliographic fields from plausibility. Preserve the blank,
describe the verification attempt, and route it to human review.

## Resources

- Read
  [`references/discovery-protocol.md`](references/discovery-protocol.md) for the
  route, query-log, and coverage contracts.
- Read
  [`references/candidate-register-schema.yml`](references/candidate-register-schema.yml)
  when creating or checking a candidate register.
- Run
  [`scripts/validate_candidate_register.py`](scripts/validate_candidate_register.py)
  before handing off a CSV register.
