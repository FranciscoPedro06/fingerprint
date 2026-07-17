# Observation Language — Specification

**Version:** 1.0
**Status:** Stable for use
**Scope:** Normative. This document defines the Observation Language (OL). Its annexes
([Controlled Vocabulary](CONTROLLED-VOCABULARY.md), [Record Format](RECORD-FORMAT.md))
are equally normative. [Profiles](profiles/) are non-normative.

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** are used
as defined in RFC 2119.

---

## 1. Purpose and scope

The Observation Language is a grammar for recording (a) what is present in a visual
object and (b) what that object appears to belong to or originate from, under strict
epistemic discipline.

It is designed to be:

- **Object-general.** Applicable to any visual object: interfaces, websites, brands,
  design systems, digital products, printed matter, physical systems, environments, or
  any other artifact that can be observed.
- **Observer-general.** Usable by any observer capable of visual observation, human or
  machine. The grammar never depends on the identity or internals of the observer.
- **Time-durable.** It references no tool, model, vendor, or technology. A record written
  under OL v1 today MUST remain interpretable by an observer who has never heard of any
  system in use at the time of writing.

## 2. Non-goals

The Observation Language is **not**:

- a detector or classifier of any property (including provenance);
- a quality rubric or scoring system;
- a metric space, a similarity measure, or any quantitative model;
- specific to any medium, industry, or generative process;
- a fixed checklist of attributes. Attribute catalogs are supplied by
  [profiles](profiles/) and are always optional and additive.

Where a capability above is desired, it is built **on top of** the OL as a separate
artifact, never inside it.

## 3. Foundational commitments

These commitments hold in every record. They are the invariants the grammar exists to
enforce.

- **C1 — Separation.** Description precedes and is recorded independently of
  interpretation. What is present is stated before what it might mean.
- **C2 — Grounding.** No interpretation may appear without citing the evidence that
  supports it.
- **C3 — Traceability.** Every recorded statement carries a stable identifier, and every
  derived statement cites the identifiers it depends on.
- **C4 — Preservation of alternatives.** Competing explanations are retained and ranked,
  never silently discarded. A single surviving explanation is a result, not a starting
  assumption.
- **C5 — Declared confidence.** Every attribution declares its confidence on the defined
  ordinal scale. Numeric probabilities MUST NOT be used unless produced by a separately
  validated estimator that is cited.
- **C6 — Explicit observer-relativity.** Interpretive statements record whose observation
  they are. When multiple observers contribute, divergence between them is preserved as
  data, not reconciled away.
- **C7 — Reproducibility target.** Evidence SHOULD be re-derivable by an independent
  observer from the same object under the same stated conditions. Where it is not
  re-derivable, the record MUST say so.

## 4. The observation pipeline

Every observation proceeds through four ordered stages:

```
Evidence  →  Relations  →  Hypotheses  →  Best-Supported Attribution
```

The order is mandatory. A stage MUST NOT draw on information reserved for a later stage,
and MUST NOT skip a stage. A stage that yields nothing MUST be recorded as
`none recorded` with a brief reason; it MUST NOT be omitted.

Each stage has a defined input, output, epistemic status, and admissibility rules.

### 4.1 Evidence

- **Definition.** Individually verifiable statements about what is present in the object.
- **Output unit.** One evidence statement. Identifier `E<n>` (see §5).
- **Epistemic status.** Observer-independent target (C7). Two observers examining the same
  object under the same conditions should record the same evidence.
- **Admissible content.** Attributes that can be measured, counted, classified against a
  stated scheme, or reported as present/absent. Each unit SHOULD declare its **derivation
  method** (see [Controlled Vocabulary §3](CONTROLLED-VOCABULARY.md)) and MAY declare a
  **locus** (where in the object it holds).
- **Prohibited content.** Relations between elements (reserve for §4.2); any reference to
  objects, populations, or conventions outside the object (reserve for §4.3); evaluation,
  causation, or attribution of any kind. The evidence lexicon in the Controlled Vocabulary
  is binding.

### 4.2 Relations

- **Definition.** Statements about how evidence units relate to one another **within the
  object**: co-occurrence, contrast, repetition, proportion, hierarchy, distribution,
  rhythm, alignment, grouping.
- **Output unit.** One relation. Identifier `R<n>`. Each relation **MUST** cite the `E`
  identifiers it relates.
- **Epistemic status.** Observer-relative but anchored. A second observer MAY record
  different relations over the same evidence; both are valid and both are kept (C6).
- **Prohibited content.** Reference to anything outside the object; evaluation; any claim
  about origin, category, or convention (reserve for §4.3).

### 4.3 Hypotheses

- **Definition.** Tentative statements that go beyond the object: characterizations,
  comparisons to conventions, genres, populations, or candidate sources. This is the first
  stage at which the outside world may be invoked.
- **Output unit.** One hypothesis. Identifier `H<n>`. Each hypothesis **MUST**:
  1. cite the `E` and/or `R` identifiers that support it;
  2. state a **refutation condition** — what observation would weaken or overturn it;
  3. carry a **status**: `open`, `supported`, `weakened`, or `retired`
     (see [Controlled Vocabulary §5](CONTROLLED-VOCABULARY.md)).
     The status `confirmed` does not exist; confirmation is not an act of this language.
- **Competing hypotheses.** Mutually exclusive explanations each receive their own `H`
  identifier and are retained side by side (C4).
- **Observational constructs.** Characterizations such as *perceived conventionality* or
  *perceived proximity to genre conventions* are hypotheses. They MUST cite evidence and
  MUST state a refutation condition like any other hypothesis. They MUST NOT be phrased as
  measured quantities.

### 4.4 Best-supported attribution

- **Definition.** The ranked judgment of what the object appears to belong to or originate
  from, given the surviving hypotheses.
- **Output unit.** One attribution. Identifier `A<n>`. Each attribution **MUST** declare:
  1. **target type** — from the attribution-target taxonomy
     ([Controlled Vocabulary §6](CONTROLLED-VOCABULARY.md));
  2. **target** — the specific thing attributed to, or `indeterminate`;
  3. **supporting hypotheses** — the `H` identifiers relied upon; an attribution MAY cite
     only hypotheses that themselves cite evidence;
  4. **confidence** — on the ordinal scale ([Controlled Vocabulary §4](CONTROLLED-VOCABULARY.md));
  5. **immediacy** — how the attribution formed: `immediate`, `on-inspection`, or
     `on-analysis`. (The founding question of this field is how quickly recognition
     occurs; immediacy records it observationally.)
  6. **discriminability** — what the object could be confused with, if anything.
- **Preservation.** When more than one attribution is defensible, each is recorded with its
  own confidence and **ranked**. The lower-ranked attributions are retained, not deleted
  (C4). Collapsing to a single attribution when alternatives remain defensible is
  non-conformant.

## 5. Identifiers and citation

- Identifiers are assigned per record, monotonically, and are **never reused** within a
  record: `E1, E2, …`, `R1, R2, …`, `H1, H2, …`, `A1, A2, …`.
- Citation uses bracketed lists: `[E1, E3]`, `[R2]`, `[H1, H4]`.
- A statement MUST cite at least the identifiers required by its stage (§4).
- Cross-record citation (for corpus-level work) uses `‹record-id›:E1` form; the record-id
  is the record's front-matter identifier ([Record Format](RECORD-FORMAT.md)).

## 6. Confidence

Confidence is an **ordinal** judgment about the strength of support **within the record**,
not a claim about truth and not a probability. The canonical levels
(`speculative`, `tentative`, `supported`, `strong`) and their criteria are defined in
[Controlled Vocabulary §4](CONTROLLED-VOCABULARY.md). Numeric probability is prohibited by
C5 unless a cited, validated estimator produced it.

## 7. Profiles

The grammar is object-general and therefore names no domain-specific attributes. A
**profile** is a non-normative catalog of evidence dimensions relevant to a class of
objects (for example, [the interface profile](profiles/interface.v1.md)). A profile:

- **MAY** suggest what evidence to look for and how to derive it;
- **MUST NOT** add, remove, or reorder pipeline stages;
- **MUST NOT** weaken any foundational commitment or admissibility rule;
- is cited in a record's front matter so readers know which lens guided evidence
  collection.

New object domains are supported by writing new profiles. The core grammar does not grow
to accommodate them. This is the mechanism by which the language remains small and stable
while its reach expands.

## 8. Versioning and stability

- The OL uses major.minor versioning. **Core-grammar changes** (stages, commitments,
  identifier or citation rules, confidence semantics) require a **major** version.
  Clarifications and annex additions that do not alter conformance are **minor**.
- Profiles version independently of the core and never trigger a core version change.
- Every record declares the OL version it conforms to ([Record Format](RECORD-FORMAT.md)).
  A record's meaning is fixed by the version it names.

## 9. Conformance

A record is **OL v1 conformant** if and only if all of the following hold:

1. All four stages are present, each either populated or explicitly `none recorded`.
2. No Evidence statement contains a relation, an outside reference, an evaluation, a
   causal claim, or an attribution (§4.1).
3. Every Relation cites the `E` identifiers it relates (§4.2).
4. Every Hypothesis cites supporting `E`/`R` identifiers, states a refutation condition,
   and carries a valid status (§4.3).
5. Every Attribution declares target type, target, supporting `H` identifiers, confidence,
   immediacy, and discriminability; and cites only hypotheses that cite evidence (§4.4).
6. Where more than one attribution is defensible, competing attributions are retained and
   ranked (C4).
7. No numeric probability appears without a cited validated estimator (C5).
8. Interpretive stages identify their observer; multi-observer divergence, where present,
   is preserved (C6).

A tool or observer MAY check items 1–7 mechanically. Item 8 is checked by inspection.

## 10. Relationship to the rest of the project

The Observation Language is the shared substrate of the Fingerprint project. Corpus
records are written in it; the [Atlas](../../atlas/) catalogs phenomena and fingerprints
discovered through it; [experiments](../../experiments/) exercise and stress-test it.
Nothing in the project may introduce a conclusion that is not expressible as an OL
attribution grounded, through hypotheses and relations, in cited evidence.
