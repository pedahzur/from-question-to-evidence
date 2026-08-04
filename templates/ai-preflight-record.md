---
title: AI Pre-Flight Record
version: 0.1.0
status: blank-resource
last-reviewed: 2026-08-04
---

# AI Pre-Flight Record

Complete and approve this record before the first guided AI workflow in a project. Complete a separate record when the task, material, system, authority, or release audience changes. An unresolved stop condition prohibits the affected AI use.

## 1. Record identity

| Field | Entry |
|---|---|
| Project and version | |
| Pre-flight record ID | |
| Lifecycle stage and research task | |
| Researcher responsible for the task | |
| Person authorized to approve this use | |
| Date completed | |
| Review or expiry date | |
| Linked epistemic-position statement | |
| Linked protocol, ethics approval, data agreement, or community rule | |

## 2. Purpose and necessity

| Decision question | Entry |
|---|---|
| What bounded task is proposed? | |
| What research artifact may the task change? | |
| What may the system propose, retrieve, transform, compare, or check? | |
| What must remain a human decision? | |
| What non-AI method could perform the task? | |
| What specific benefit justifies AI assistance? | |
| What is the smallest input sufficient for the task? | |

**Necessity decision:** ☐ justified ☐ not justified ☐ requires consultation

If AI adds no defined benefit, use the non-AI method.

## 3. Authority and applicable rules

Record the rule and the person or body able to interpret it. Do not assume that public availability authorizes automated processing or republication.

| Authority or rule | Applies? | Evidence or locator | Decision owner | Cleared? |
|---|---|---|---|---|
| Law or regulation | | | | |
| Institutional policy | | | | |
| Ethics or IRB approval | | | | |
| Consent terms or participant agreement | | | | |
| Community or partner authority | | | | |
| Archive, repository, licence, or terms of access | | | | |
| Data-use or confidentiality agreement | | | | |
| Copyright or other rights | | | | |
| Funder, publisher, or venue rule | | | | |

**Authority decision:** ☐ cleared ☐ cleared with restrictions ☐ unresolved ☐ prohibited

## 4. Material and sensitivity classification

Use the project's institutional classification scheme where one exists. Describe protected material without copying it into this record.

| Material class | Present? | Examples by source ID or category | Permitted processing environment | Restrictions |
|---|---|---|---|---|
| Public and rights-cleared | | | | |
| Public but rights, context, or aggregation restricted | | | | |
| Internal or unpublished, without personal data | | | | |
| Personal, participant-produced, confidential, or pseudonymized | | | | |
| Legally, ethically, contractually, or communally prohibited | | | | |

Participant-produced, confidential, restricted, or pseudonymized material must not enter an external AI system by default. Use requires explicit authorization and an approved processing environment.

**Classification decision:** ☐ external processing permitted ☐ local or institutional system only ☐ abstracted input only ☐ processing prohibited ☐ unresolved

## 5. System and access conditions

| Field | Entry |
|---|---|
| Processing environment: local, institutional, or external | |
| Provider, product, model, and version | |
| Account and access-control conditions | |
| Retention and deletion terms verified on | |
| Training or secondary-use setting verified on | |
| Data location or subprocessors, if consequential | |
| Search, connector, or external-tool access | |
| Linked dated tool card or institutional assessment | |
| Known language, region, modality, or accessibility limits | |

If consequential provider conditions cannot be confirmed, do not supply protected or unpublished material.

## 6. Input minimization and provenance

| Control | Planned action |
|---|---|
| Remove material not needed for the task | |
| Replace full records with abstracts, schema, or synthetic examples where possible | |
| Preserve the source and AI-produced derivative separately | |
| Assign stable source and output identifiers | |
| Record prompt, settings, date, and system version | |
| Prevent protected content from entering the audit log | |
| Record transformations, redactions, and exclusions | |

## 7. Risk assessment and controls

| Risk | Plausible harm or failure | Affected people or research object | Control | Residual risk | Owner |
|---|---|---|---|---|---|
| Privacy, confidentiality, or re-identification | | | | | |
| Rights, consent, or contractual breach | | | | | |
| Fabricated source, quotation, fact, or reference | | | | | |
| Distorted summary, lost qualification, or false equivalence | | | | | |
| Directional bias or missing language, region, or perspective | | | | | |
| Invalid coding, extraction, linkage, or measurement | | | | | |
| Insecure access, retention, or unintended disclosure | | | | | |
| Unrecorded drift or irreproducible decision | | | | | |
| Transfer of authorship, interpretation, or causal judgment | | | | | |
| Other | | | | | |

## 8. Validation plan

Define the test before accepting consequential output.

| Field | Entry |
|---|---|
| Unit or operation being validated | |
| Human-coded or otherwise authoritative benchmark | |
| Sampling and oversampling rule | |
| Error categories | |
| Language, region, source family, subgroup, or difficulty checks | |
| Acceptance thresholds and rationale | |
| Reviewer and adjudication route | |
| Failure response | |
| Revalidation trigger | |

AI output remains a candidate until it passes the declared source, transformation, or benchmark check. A fluent response is not validation.

## 9. Logging, disclosure, and preservation

| Requirement | Planned record |
|---|---|
| Consequential prompts and outputs to preserve | |
| Accepted and rejected suggestions | |
| Search failures, abstentions, and unresolved items | |
| Human decisions and reasons | |
| Change made to question, vocabulary, corpus, codebook, analysis, or prose | |
| Disclosure required by institution, funder, venue, or audience | |
| Retention, deletion, correction, and preservation route | |

The log supports reconstruction of the decision. It need not reproduce protected inputs or every exploratory exchange.

## 10. Stop and escalation conditions

Check every condition that applies.

- ☐ Authority, consent, rights, or data classification is unresolved.
- ☐ The material requires an approved environment that is unavailable.
- ☐ Provider retention, training, access, or secondary-use conditions cannot be established.
- ☐ The proposed task transfers interpretation, authorship, causal judgment, or release authority to the system.
- ☐ A valid benchmark or source-level verification procedure cannot be designed.
- ☐ Risk remains disproportionate to the task's research value.
- ☐ The system fails the declared validation threshold or shows consequential subgroup, language, or source-family error.
- ☐ An affected participant, community, archive, partner, or authority requires pause, withdrawal, or review.
- ☐ The task, material, system, model, access route, or release audience has changed since approval.

**Escalation route and responsible person:**

## 11. Gate decision

Select one decision and record its scope.

- ☐ **Approved:** the bounded task may proceed under the controls above.
- ☐ **Approved with restrictions:** proceed only under the restrictions recorded below.
- ☐ **Local or institutional processing only:** no external processing.
- ☐ **Deferred:** resolve the named questions before use.
- ☐ **Prohibited:** the task or material must not be processed with AI.

**Restrictions, unresolved questions, or reasons for prohibition:**

**Approver:**

**Approval date:**

**Next review or expiry:**

## 12. Closeout after use

| Question | Entry |
|---|---|
| Did actual input remain within the approved class and scope? | |
| Did the system, settings, or connected tools change? | |
| Did validation pass, and where is the evidence? | |
| Which outputs were accepted, rejected, corrected, or left unresolved? | |
| Did AI assistance change a consequential research decision or artifact? | |
| Were required disclosures, deletions, corrections, and preservation actions completed? | |
| Must the epistemic-position statement, protocol, or pre-flight record be reopened? | |

**Closeout decision:** ☐ complete ☐ corrective action required ☐ escalated ☐ approval withdrawn
