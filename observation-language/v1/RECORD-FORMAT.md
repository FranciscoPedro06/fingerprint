# Observation Language — Record Format

**Version:** 1.0
**Status:** Normative annex to the [Specification](SPECIFICATION.md).

This annex defines how an OL record is laid out on disk so that records are uniform,
machine-locatable, and comparable across a corpus.

---

## 1. File and identity

- One record describes one **object** under one set of **conditions**. A different render,
  viewport, or state is a different record.
- A record is a UTF-8 Markdown file. Its **record-id** (front-matter `id`) is unique within
  the corpus and is the anchor for cross-record citation (`‹record-id›:E1`).

## 2. Front matter

```yaml
---
id:            <corpus-unique record id, e.g. OBS-2026-0001>
ol_version:    1.0
object:        <what was observed, stable reference or path>
object_kind:   <free label, e.g. "website landing page">
profiles:      [<profile ids used, e.g. interface.v1>]   # may be empty
observers:     [<observer id(s)>]                          # one or more
date:          <YYYY-MM-DD>
conditions:    <render/viewport/instrument conditions relevant to reproducibility>
provenance:    <known | unknown | withheld>   # is the object's origin known to the observer?
---
```

`provenance` matters for bias control: an observer who already knows the object's origin
cannot produce an unbiased attribution. Records used to study attribution SHOULD be taken
with `provenance: unknown`.

## 3. Body layout

The four stages appear in order, each as a section. Identifiers are assigned per §5 of the
Specification.

```markdown
## Evidence
- **E1** — <statement>  · _derivation:_ measured · _locus:_ <optional>
- **E2** — <statement>  · _derivation:_ counted

## Relations
- **R1** — <relation> · _relates:_ [E1, E2]

## Hypotheses
- **H1** — <hypothesis> · _from:_ [E1, R1] · _refuted if:_ <condition> · _status:_ open
- **H2** — <competing hypothesis> · _from:_ [E2] · _refuted if:_ <condition> · _status:_ open

## Attribution
- **A1** — _type:_ category · _target:_ "<…>" · _from:_ [H1]
  · _confidence:_ supported · _immediacy:_ immediate
  · _discriminability:_ <what it could be confused with>
- **A2** — _type:_ production-method · _target:_ "<…>" · _from:_ [H2]
  · _confidence:_ tentative · _immediacy:_ on-analysis · _discriminability:_ <…>
  · _rank:_ 2
```

An empty stage is written explicitly:

```markdown
## Relations
_none recorded — <reason>_
```

## 4. Multiple observers

Evidence is a shared, objective substrate (C7); interpretation is per-observer (C6).
When more than one observer contributes to a record:

- The **Evidence** section is shared and agreed (disagreements about evidence are resolved
  by re-derivation, or the disputed unit is dropped and noted).
- **Relations**, **Hypotheses**, and **Attribution** are recorded **per observer**, under a
  labeled subsection:

```markdown
## Hypotheses

### Observer: obs-A
- **H1** — … · _from:_ [E1] · _refuted if:_ … · _status:_ open

### Observer: obs-B
- **H1** — … · _from:_ [E2] · _refuted if:_ … · _status:_ open
```

Identifiers restart per observer subsection and are namespaced by observer in cross-
reference (`obs-A/H1`). **Divergence between observers is retained** and is a primary
signal for attribution studies; it is never averaged or reconciled into a single view.

## 5. Conformance block (optional but recommended)

A record MAY end with a checklist mirroring Specification §9, to make conformance visible:

```markdown
## Conformance (OL v1)
- [x] All four stages present
- [x] Evidence free of relation/outside/eval/causal/attribution
- [x] Every relation cites E-ids
- [x] Every hypothesis cites support, states refutation, has status
- [x] Every attribution declares type/target/support/confidence/immediacy/discriminability
- [x] Competing attributions retained and ranked
- [x] No numeric probability without cited estimator
```

## 6. Storage convention

- Corpus records live under [`corpus/`](../../corpus/) once reviewed; working records live
  with their experiment under [`experiments/`](../../experiments/).
- Associated artifacts (screenshots, extracted values) live beside the record in a folder
  named for the record-id.
