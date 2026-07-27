# Discovery Protocol Contract

## Purpose

Use this contract to keep literature discovery reproducible and distinct from
screening. Discovery finds and verifies possible bibliographic objects. A later
human-governed process determines substantive eligibility.

## Query log

Record one row for every executed query:

| Field | Meaning |
|---|---|
| `query_id` | Stable identifier within the run |
| `run_id` | Identifier shared by all artifacts in one discovery run |
| `source` | Database, catalogue, archive, venue, or public search system |
| `discovery_route` | Structured search, citation search, author search, hand search, or another approved route |
| `query_exact` | Exact syntax or navigation sequence |
| `filters` | Date, language, source type, field, or access filters |
| `executed_at` | Date and time, including time zone where useful |
| `result_count` | Count reported or observed before deduplication |
| `access_status` | Complete, partial, blocked, or unavailable |
| `notes` | Syntax changes, export limits, or other qualifications |

Do not silently rewrite a failed query. Log the failed form and the corrected form
as separate rows.

## Candidate identity

Prefer a persistent identifier and an authoritative landing page. A search-result
snippet alone supports staging but not verified identity. Model-generated
bibliographic text without a retrievable locator belongs in `unresolved-leads.md`,
not in the candidate register.

Preserve multiple discovery routes. When two records resolve to one object, retain
the first candidate identifier, add the later identifier to the resolution log, and
merge route and query identifiers without losing either.

## Coverage memo

Use these headings:

1. **Run identity** — protocol, context, run, reviewer, date.
2. **Sources and routes completed** — including partial or blocked routes.
3. **Known-item recovery** — recovered, missed, and explanation.
4. **Vocabulary coverage** — concepts, proxies, historical and local-language terms.
5. **Distribution checks** — periods, settings, languages, source types, and methods.
6. **Unresolved coverage risks** — barriers and plausible false gaps.
7. **Stopping-rule assessment** — satisfied, not satisfied, or not assessable.
8. **Human decisions required** — explicit, bounded questions.

## Acceptable conclusions

Use bounded language:

- “No candidates were recovered through the routes executed.”
- “Coverage remains uncertain because the local-language index was not searched.”
- “The known-item set was recovered across two independent routes.”

Do not write:

- “No literature exists.”
- “The field has ignored this issue.”
- “The review is comprehensive.”

Those conclusions require a broader evidentiary argument and human approval.
