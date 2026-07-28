---
title: "Source Review: Large Language Models Are Democracy Coders with Attitudes"
type: source-review
status: incorporated
reviewed: 2026-07-28
citation-key: weidmann2026democracy
doi: 10.1017/S1049096525101248
---

# Source Review

## Verified bibliographic record

Nils B. Weidmann, Mats Faulborn, and David García, “Large Language Models Are Democracy Coders with Attitudes,” *PS: Political Science & Politics* 59, no. 1 (January 2026): 17–23, https://doi.org/10.1017/S1049096525101248.

The article was published online by Cambridge University Press on 30 July 2025 and assigned to the January 2026 issue. The publisher identifies it as an open-access article under CC BY 4.0. The authors link their replication documentation and data through Harvard Dataverse at https://doi.org/10.7910/DVN/I34X6P.

## Research question and design

The article asks whether general-purpose LLMs can supplement expert coding of subjective democracy indicators. It organizes coding difficulty along two dimensions:

1. whether the material needed for coding is supplied to the coder; and
2. how much interpretation the coding decision requires.

The difficult corner combines unspecified source material with extensive interpretation. Democracy coding occupies this corner because experts must synthesize broad country knowledge and apply contestable ordinal categories.

The authors use 53 ordinal Type-C V-Dem indicators for 171 countries in 2023. They prompt GPT-4o (checkpoint `GPT-4o-2024-08-06`) and Llama-3.1-70B in a zero-shot setting using the V-Dem questions and response categories. The V-Dem 2024 release postdates the models' training data, reducing the risk that the systems simply retrieved the target scores. Results are compared with V-Dem's aggregated expert codings and with the degree of disagreement among expert coders.

## Main findings

- Both models reproduced broad relative patterns without task-specific adaptation. Average country-level correlations with V-Dem were 0.64 for GPT-4o and 0.50 for Llama-3.1.
- Correlation concealed directional disagreement in absolute scores. GPT-4o scored democratic quality lower than the expert aggregate by 0.28 on average and did so for approximately 80 percent of countries. Llama-3.1 scored it higher by 0.50 on average and did so for 97 percent of countries.
- Both models diverged more for countries on which human coders disagreed more.
- Averaging the two models reduced the mean difference to approximately 0.10, but the authors warn that an ensemble is useful only when the direction and strength of model-specific tendencies have been measured.
- The reported LLM run cost less than EUR 150, compared with an estimated human-coding cost of several tens of thousands of euros.

The article properly calls deviations from the V-Dem aggregate *differences* rather than *errors*: the expert scores are a comparison standard, not an observed ground truth.

## Assessment

### What the paper contributes to the field guide

The two-dimensional coding-task framework is durable and directly useful. It explains why event-field extraction from a supplied newspaper article is usually a safer automation target than a synthetic judgment about institutional quality. It also strengthens the book's distinction between clerical compression and delegated interpretation.

The empirical comparison demonstrates why validation must measure absolute agreement, class- and subgroup-specific differences, and performance on difficult cases. A high correlation is not enough. The findings also supply concrete evidence for the book's warning that model ensembles are not independent expert panels.

### Limits to preserve in the manuscript

- The experiment examines two model checkpoints, one country-year, and one family of expert-coded political indicators.
- It uses zero-shot prompts and does not establish the best possible performance after retrieval, fine-tuning, or measurement-model adjustment.
- V-Dem's aggregated coding is a sophisticated reference measure, not ground truth.
- Simple averaging worked because the two observed tendencies opposed one another. That result cannot be generalized to uncalibrated model combinations.
- The study supports local benchmarking and human-model comparison. It does not show that LLMs should autonomously code contested concepts.

## Manuscript incorporation

| Location | Function |
|---|---|
| `content/19-building-event-databases-with-ai.qmd` — Orientation | Distinguish supplied-material extraction from interpretation-heavy synthetic coding |
| `content/19-building-event-databases-with-ai.qmd` — Validate before scaling | Show why correlation can conceal directional disagreement and difficult-case failure |
| `content/19-building-event-databases-with-ai.qmd` — Advanced Practice | Qualify ensemble averaging and require model-specific calibration |
| `content/19-ai-research-integrity.qmd` — Bias and Missing Perspectives | Add directional judgment as a form of model-specific bias |
| `content/19-review-articles-and-meta-analysis.qmd` — agent specialization | Explain why multiple model outputs do not constitute independent expert corroboration |
