# Corpus

Reviewed observation records, written in the [Observation Language](../observation-language/).
The corpus is the project's data: the accumulated, inspectable observations from which
Atlas entries are drawn.

## What belongs here

- Records that conform to the Observation Language ([Specification §9](../observation-language/v1/SPECIFICATION.md))
  and have passed review.
- Their associated artifacts (screenshots, extracted values), stored beside the record in
  a folder named for its record-id.

## What does not belong here

- Working or in-progress records — those live with their experiment under
  [`experiments/`](../experiments/) until reviewed.
- Interpretation not grounded in cited evidence.

## Provenance and bias

Records intended for attribution study SHOULD be collected with the object's provenance
withheld from the observer (`provenance: unknown`), per the
[Record Format](../observation-language/v1/RECORD-FORMAT.md) and the Law of Judge
Independence.

## Status

The first corpus material is the EXP-0001 baseline (23 interface records) and the EXP-0002
lab sample. These are being migrated to Observation Language v1 form before promotion into
this directory; until then they remain under [`experiments/`](../experiments/).
