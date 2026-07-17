# Observation Language — Controlled Vocabulary

**Version:** 1.0
**Status:** Normative annex to the [Specification](SPECIFICATION.md).

This annex fixes the words and closed lists the grammar relies on. Where the Specification
refers to a "defined scale" or "taxonomy," the definition is here.

---

## 1. Why a controlled vocabulary

The pipeline's discipline depends on keeping description and interpretation lexically
separable. A word that smuggles a judgment into the Evidence stage defeats commitment C1.
This annex lists which words belong to which stage, so that conformance can be checked by
inspection and, in part, mechanically.

## 2. Register of the stages

| Stage | Speaks about | May reference outside the object? | Carries judgment? |
|---|---|---|---|
| Evidence | what is present | no | no |
| Relations | how present things relate | no | no |
| Hypotheses | what it might mean or resemble | yes | tentative only |
| Attribution | what it appears to belong to | yes | declared, ranked |

## 3. Evidence lexicon

### 3.1 Admissible predicates

Evidence statements assert presence, value, count, or classification:

- *is / has / contains / consists of*
- *count is N / N distinct / N instances*
- *value is X / resolves to X / measures X*
- *present / absent*
- *classified as X against ‹scheme›*

### 3.2 Derivation methods (declare one per unit)

- **measured** — read from an instrument or computed value (e.g., a rendered dimension).
- **counted** — enumerated by direct count.
- **classified** — assigned to a category under a named scheme, by the observer.
- **reported** — taken from a stated source attached to the object (e.g., embedded
  metadata), not independently verified.
- **inferred** — deduced from other evidence within the object; MUST name the basis. Use
  sparingly; inferred evidence has lower reproducibility.

### 3.3 Prohibited in Evidence

- **Evaluative:** good, bad, beautiful, ugly, clean, cluttered, elegant, generic,
  cheap, premium, polished, refined, dated, modern.
- **Attributive:** looks like, resembles, appears to be, branded, templated, hand-made,
  or any reference to a source or production method.
- **Causal:** because, in order to, so that, driven by, results from.
- **Relational-internal** (belongs in Relations): dominates, contrasts with, echoes,
  balances, outranks.
- **Comparative-external** (belongs in Hypotheses): typical of, unlike, conventional,
  common, unusual, on-trend.

If a needed statement cannot be made without a prohibited word, it is not evidence; move
it to the stage that admits it.

## 4. Confidence scale

Confidence is ordinal and describes strength of support **within the record** (C5). It is
not a probability and MUST NOT be written as one.

| Level | Criterion |
|---|---|
| **speculative** | Raised as a possibility. Little or no cited support; alternatives entirely open. |
| **tentative** | Some cited support. One or more alternatives remain roughly as well supported. |
| **supported** | Multiple, ideally independent, evidence/relations cited. Alternatives are cited but weaker. |
| **strong** | Convergent independent support. Every defensible alternative requires discounting specific cited evidence. |

`strong` is the ceiling of this language. It never means "certain" or "confirmed."

## 5. Hypothesis status values

| Status | Meaning |
|---|---|
| **open** | Stated; not yet weighed against its refutation condition. |
| **supported** | Evidence has accumulated; refutation condition not met. |
| **weakened** | Evidence against it has appeared; retained but demoted. |
| **retired** | Refutation condition met, or superseded. Kept in the record, marked retired; never deleted. |

There is deliberately no `confirmed`.

## 6. Attribution-target taxonomy

The `target type` of an attribution is one of:

| Type | The object appears to belong to / originate from… |
|---|---|
| **brand** | a specific named brand or organization. |
| **product-line** | a specific product or product family within a brand. |
| **author** | a specific individual maker. |
| **studio** | a specific studio, agency, or team. |
| **category** | a class of objects defined by function (e.g., "project-management landing page"). |
| **genre** | a class defined by style or convention (e.g., "editorial long-form"). |
| **design-system** | a specific reusable system, framework, kit, or template lineage. |
| **production-method** | a way of making (e.g., "assembled from a component library," "single-author hand-built"). |
| **era** | a time period or generation of practice. |
| **medium** | a material or channel convention (e.g., "print conventions transplanted to screen"). |
| **tradition** | a school or movement of practice. |
| **indeterminate** | no target is better supported than the alternatives. |

Attribution to `category`, `genre`, `design-system`, or `production-method` is as valid a
result as attribution to `brand`. A frequent, well-supported attribution to one of the
generic types — rather than to a specific brand or author — is itself a finding.

## 7. Immediacy scale

How the attribution formed, recorded observationally:

| Level | Meaning |
|---|---|
| **immediate** | Formed on first exposure, before deliberate analysis. |
| **on-inspection** | Formed after brief, directed looking. |
| **on-analysis** | Formed only after working through evidence and relations. |

## 8. Relation kinds (open list)

Relations name how evidence units stand to one another. This list is a starting
vocabulary, not a closed set; observers MAY introduce a clearly defined kind.

co-occurrence · contrast · repetition · proportion · hierarchy · distribution · rhythm ·
alignment · grouping · containment · symmetry · substitution.
