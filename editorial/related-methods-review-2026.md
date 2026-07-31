# Related Methods Review: AI-Assisted Humanities and Social Science Research

Reviewed 31 July 2026. This is a focused methods map, not a comprehensive
systematic review.

## Review question

Which published or institutionally documented approaches resemble the mirrored
newspaper evidence workflow in their use of computation or AI, human review,
source provenance, multilingual retrieval, qualitative interpretation, or
explicit stopping rules?

## Search and screening

The search used combinations of the terms `AI-assisted research workflow`,
`historical newspapers`, `digital source criticism`, `multilingual OCR`,
`human-in-the-loop qualitative coding`, `computational grounded theory`,
`collections as data`, and `active learning systematic review`. Searches
prioritized publishers, project sites, DOI records, and open papers. Wikipedia,
commercial tool comparisons, unsourced tutorials, and social-media claims were
excluded. A work was included when it supplied a documented method, an evaluated
workflow, or an institutional framework relevant to at least two stages of the
pilot. Publication and DOI metadata were checked against the publisher or
project page.

## Comparison

| Approach | What it contributes | Relation to the mirrored-news method | Important difference |
|---|---|---|---|
| Collections as Data and Collections as ML Data | Provenance, rights, documentation, missingness, and responsible computational access to cultural heritage collections. | Grounds the manifest, rights boundary, and decision to treat archive design as evidence. | Primarily guides collection stewards and ML projects; it does not supply an event-matching procedure. |
| Environmental Scan | Compares digitized newspaper holdings with reference metadata to estimate representational bias and missingness. | Supports explicit caution about what the searchable archive includes and omits. | Works at corpus and publishing-landscape scale; the pilot works at event and article scale. |
| Impresso and HIPE | Multilingual historical-media processing, OCR-aware entity recognition, semantic enrichment, linking, and transparent exploration. | Closest technical precedent for crossing languages while retaining source context. | Builds infrastructure and trained components; the pilot is a lightweight researcher-controlled workflow over a public interface. |
| Computational grounded theory | Cycles between computational pattern detection, close interpretation, and confirmation. | Supports the movement from broad search patterns to close reading and checked claims. | Oriented toward concepts and themes within text corpora, not cross-archive event identity. |
| LLM-assisted qualitative coding | Human-developed codebooks, prompt refinement, gold-standard validation, and scaled application of codes. | Supports information-origin classification and human validation of model suggestions. | Assumes a defined corpus and coding unit; the pilot must first discover and verify the sources themselves. |
| ASReview and active-learning screening | Machine prioritization, researcher inclusion decisions, saved labels, benchmarks, and stopping criteria. | Closely resembles candidate triage and the preservation of researcher decisions. | Screens research records for relevance, not politically asymmetric accounts of one historical event. |

## Assessment

The pilot does not claim methodological novelty for multilingual search,
human-in-the-loop analysis, source criticism, or transparent screening
separately. Its contribution lies in joining these practices around a contested
historical event when the archives use different names, inherit different
information chains, and expose imperfect OCR through a public search interface.

The distinctive unit is the event crosswalk. It requires shared dates, places,
actors, and operational details, while preserving each report as a separate
record. It therefore sits between corpus-level digital history and conventional
close reading. Negative searches, source dependence, match confidence, rights
status, and reopening conditions remain visible rather than disappearing into a
finished narrative.

This integration is useful, but its evidence remains a pilot. It was tested on a
small set of Mandate-era newspaper reports, not across multiple archives,
languages, and research teams. A stronger evaluation would compare independent
researchers, measure recall against a hand-built benchmark, vary OCR quality,
and test whether the same stopping rule produces comparable corpora.

## Verified primary and project sources

- Padilla et al., *Always Already Computational: Collections as Data: Final
  Report* (2019), <https://doi.org/10.5281/zenodo.3152935>.
- Lee, “The ‘Collections as ML Data’ Checklist for Machine Learning and
  Cultural Heritage” (2023), <https://doi.org/10.1002/asi.24765>.
- Beelen et al., “Whose News? Critical Methods for Assessing Bias in Large
  Historical Datasets” (2025), <https://doi.org/10.1017/chr.2025.10007>.
- Impresso, “Objectives,” <https://impresso-project.ch/project/objectives/>.
- Impresso, “HIPE Shared Task,” <https://impresso-project.ch/hipe/>.
- Nelson, “Computational Grounded Theory” (2020),
  <https://doi.org/10.1177/0049124117729703>.
- Dunivin, “Scaling Hermeneutics” (2025),
  <https://doi.org/10.1140/epjds/s13688-025-00548-8>.
- Than et al., “Updating ‘The Future of Coding’” (2025),
  <https://doi.org/10.1177/00491241251339188>.
- van de Schoot et al., “An Open Source Machine Learning Framework for
  Efficient and Transparent Systematic Reviews” (2021),
  <https://doi.org/10.1038/s42256-020-00287-7>.
