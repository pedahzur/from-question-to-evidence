# Skills and Agents Lab v0.1.0

## Objective

Publish one complete companion release that operationalizes the literature-review
chapter while preserving its methodological boundaries. The release must be useful
without a specific model vendor and inspectable without running an agent.

## Release contract

The release contains:

1. `literature-discovery`, a reusable skill that turns a review protocol and an
   approved project-context packet into a documented discovery run.
2. `literature-scout`, a read-only agent that may execute the skill against
   approved sources and return staged candidates.
3. A project-context packet template with stable, current-state, and task layers.
4. Three synthetic benchmark cases:
   - known-item recovery and route preservation;
   - false-gap prevention through vocabulary expansion;
   - boundary enforcement and abstention.
5. A report distinguishing observed authoring-run errors from anticipated risks.
6. A deterministic, versioned ZIP package with a SHA-256 checksum.
7. A public Quarto page with download, source, problem-report, and revision-proposal
   links.

## Scholarly boundaries

- Candidate records are leads, not evidence.
- The skill and agent may not make final inclusion or exclusion decisions.
- Bibliographic identities and source links require verification.
- Absence in a bounded search is not absence in a field.
- Restricted or participant-derived material is never required by the benchmark.
- The project context packet is a map to authoritative artifacts, not a replacement
  for those artifacts.
- Any model-generated interpretation must retain source identifiers and an
  abstention route.

## Package structure

```text
lab/
  VERSION
  MANIFEST.yml
  feedback.md
  skills/literature-discovery/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
  agents/literature-scout.md
  templates/project-context-packet.md
  benchmarks/
    benchmark-manifest.yml
    01-known-item-recovery/
    02-false-gap/
    03-boundary-and-abstention/
  reports/what-ai-got-wrong.md
downloads/
  skills-and-agents-lab-v0.1.0.zip
  skills-and-agents-lab-v0.1.0.zip.sha256
```

## Implementation sequence

1. Add failing source and release-contract tests.
2. Initialize the skill with the official skill scaffold.
3. Implement the skill, references, validator, and UI metadata.
4. Implement and validate the least-privilege agent.
5. Add the context template and benchmark fixtures.
6. Exercise the validator against canonical and deliberately invalid registers.
7. Write the failure report with exact verification status.
8. Add the Quarto companion page, feedback forms, and project documentation.
9. Build the deterministic archive and checksum.
10. Run skill, agent, unit, content, Quarto, link, and accessibility checks.

## Acceptance criteria

- The official skill validator passes.
- The agent validator passes and confirms read-only tools.
- All three benchmark contracts pass.
- The candidate-register validator accepts the canonical fixtures and rejects an
  invalid record that lacks provenance.
- The ZIP contains only manifest-listed public files and reproduces byte-for-byte
  across consecutive builds.
- The rendered page links to an existing ZIP, checksum, source directory, and two
  issue forms.
- Existing manuscript, citation, accessibility, rights, and site tests remain green.
- The release contains no credentials, participant data, private paths, or fabricated
  scholarly citations.
