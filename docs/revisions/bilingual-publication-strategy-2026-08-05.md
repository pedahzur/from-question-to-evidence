# Bilingual Publication Strategy

## Purpose

The project will publish an English source edition and a Hebrew edition of the
same methods book. The Hebrew edition must remain useful to Hebrew-speaking
students without concealing when it lags behind the English source.

## Edition relationship

- The **English source edition** is the drafting and citation authority during
  manuscript development.
- The **Hebrew edition** is a governed adaptation that follows the same chapter
  identifiers, artifacts, examples, integrity gates, and citations.
- A translated chapter is not current merely because a Hebrew file exists.
- Changes to method, evidence, rights, or learning outcomes require review in both
  editions. Minor copy edits may be recorded without forcing a full translation
  cycle.

## Stable chapter identity

Every target chapter will receive a stable chapter identifier independent of its
display number. A recommended pattern is `FQTE-P{part}-C{chapter}`, for example
`FQTE-P4-C03`. Display numbering may change during restructuring; the stable
identifier must not.

Each Hebrew chapter must record:

```yaml
source-id: FQTE-P4-C03
source-language: en
source-version: <Git commit or release identifier>
translation-status: draft | reviewed | current | stale
translated-at: YYYY-MM-DD
reviewed-by: []
direction: rtl
terminology-version: <identifier>
```

## Translation status

| Status | Meaning | Publication label |
|---|---|---|
| `draft` | Initial translation that may contain unresolved terminology or layout problems | Draft translation |
| `reviewed` | Language and method have received human review, but the source may have advanced | Reviewed translation |
| `current` | Content, citations, artifacts, links, and source version match the declared English edition | Current Hebrew edition |
| `stale` | The English source changed in a way that affects meaning, evidence, pedagogy, or rights | Earlier translation |

## Translation method

Translate meaning and teaching function, not English syntax. Preserve source
quotations in their original language where scholarly practice requires it and
provide a labeled translation. Keep controlled English terms in parentheses on
first mention when they are likely to appear in software, databases, or the
international methods literature.

Machine translation may create a first-pass candidate. It may not assign the
translation status `reviewed` or `current`. A human reviewer must check conceptual
equivalence, Hebrew idiom, gender and number agreement, mixed-script punctuation,
citations, tables, callouts, and right-to-left behavior.

## Terminology governance

Maintain one bilingual glossary for book-level terms. Each entry records the
English term, preferred Hebrew term, allowed variants, prohibited calques, first
use, definition, and terminology version. Exact archival language, participant
language, quotations, and schema field names must not be silently normalized to
the glossary.

## Right-to-left and accessibility checks

Every Hebrew release must test right-to-left navigation, heading order, table
reading order, numbered steps, footnotes, bibliography direction, mixed Hebrew and
English strings, code blocks, downloadable templates, alt text, keyboard access,
and mobile layouts. Diagrams need a Hebrew text alternative even when the visual
itself remains bilingual or English.

## URL and release plan

The English edition remains at the existing book route. The target Hebrew route is
`/field-guide/he/`. Each edition must display its language, release identifier,
last review date, and a direct link to the corresponding chapter in the other
language when available.

No release may imply complete bilingual parity unless every required chapter is
marked `current` against the same source release. Partial Hebrew releases must
publish a visible coverage table.

