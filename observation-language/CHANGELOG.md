# Observation Language — Changelog

Format: each version records what changed in the **core grammar**. Profile changes are
listed separately because they never affect core conformance.

## v1.0 — 2026-07-16

First public version. Establishes:

- The four-stage pipeline: Evidence → Relations → Hypotheses → Best-Supported Attribution.
- Seven foundational commitments (separation, grounding, traceability, preservation of
  alternatives, declared confidence, explicit observer-relativity, reproducibility target).
- Identifier and citation scheme (`E/R/H/A`, bracketed citation, cross-record form).
- Ordinal confidence scale with a prohibition on unearned numeric probability.
- Attribution-target taxonomy spanning specific (brand, author) to generic (category,
  genre, design-system, production-method) targets, with `indeterminate` as a valid result.
- The profile mechanism: domain attribute catalogs live outside the core and version
  independently.
- Conformance criteria (Specification §9).

Lineage: the pipeline and the two-layer discipline generalize the interface observation
instrument developed in EXP-0001 and stress-tested in EXP-0002. The move from an
attribute checklist to an attribution grammar was motivated by the EXP-0002 finding that
the most important observation was not any single attribute but *what the object appeared
to belong to*.

### Profiles
- `interface.v1` — added. Screen-based interfaces and websites.
