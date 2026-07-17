# Observation Language

A grammar for recording what is present in a visual object and what it appears to belong
to, under strict epistemic discipline. It is the shared substrate of the Fingerprint
project: corpus records are written in it, and every finding in the project must be
expressible as an attribution grounded, through hypotheses and relations, in cited
evidence.

The language is **object-general** (any visual object), **observer-general** (human or
machine), and **time-durable** (it names no tool, model, or vendor).

## The pipeline

```
Evidence  →  Relations  →  Hypotheses  →  Best-Supported Attribution
```

No stage is skipped. No interpretation appears without cited evidence. Every attribution
declares its confidence and preserves the competing attributions it outranks.

## Versions

- **[v1](v1/)** — current, stable for use.
  - [Specification](v1/SPECIFICATION.md) — the normative grammar.
  - [Controlled Vocabulary](v1/CONTROLLED-VOCABULARY.md) — the lexicon, confidence scale,
    and attribution-target taxonomy (normative).
  - [Record Format](v1/RECORD-FORMAT.md) — on-disk layout, identifiers, multi-observer
    records (normative).
  - [Profiles](v1/profiles/) — optional, additive domain lenses (non-normative).
  - [Template](v1/templates/observation-record.template.md) — blank conformant record.
  - [Worked example](v1/examples/interface-001.example.md) — the grammar applied to a real
    artifact.

## Design stance

The core grammar stays small. Domain-specific attribute catalogs live in
[profiles](v1/profiles/) and version independently, so the language grows in reach without
growing in size. The grammar is written to remain interpretable by an observer who has
never heard of any system in use at the time it was written.

See the [changelog](CHANGELOG.md) for version history and the
[glossary](../docs/glossary.md) for shared terms.
