---
id:            OBS-YYYY-NNNN
ol_version:    1.0
object:        <stable reference or path to the observed object>
object_kind:   <free label, e.g. "website landing page">
profiles:      [interface.v1]        # or [] if none
observers:     [<observer id>]
date:          YYYY-MM-DD
conditions:    <render / viewport / instrument conditions>
provenance:    unknown               # known | unknown | withheld
---

# Observation Record — <object short name>

> Observation Language v1. Stages are mandatory and ordered:
> Evidence → Relations → Hypotheses → Attribution. No stage skipped.

## Evidence
- **E1** — <what is present> · _derivation:_ measured · _locus:_ <optional>
- **E2** — <what is present> · _derivation:_ counted

## Relations
- **R1** — <how E-units relate> · _relates:_ [E1, E2]

## Hypotheses
- **H1** — <tentative characterization / comparison> · _from:_ [E1, R1]
  · _refuted if:_ <what would weaken it> · _status:_ open

## Attribution
- **A1** — _type:_ <brand|category|genre|design-system|production-method|…>
  · _target:_ "<specific target or indeterminate>" · _from:_ [H1]
  · _confidence:_ <speculative|tentative|supported|strong>
  · _immediacy:_ <immediate|on-inspection|on-analysis>
  · _discriminability:_ <what it could be confused with>
  · _rank:_ 1

## Conformance (OL v1)
- [ ] All four stages present
- [ ] Evidence free of relation/outside/eval/causal/attribution
- [ ] Every relation cites E-ids
- [ ] Every hypothesis cites support, states refutation, has status
- [ ] Every attribution declares type/target/support/confidence/immediacy/discriminability
- [ ] Competing attributions retained and ranked
- [ ] No numeric probability without cited estimator
