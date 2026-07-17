---
id:            OBS-2026-EXAMPLE-001
ol_version:    1.0
object:        experiments/EXP-0002-ai-generation-lab/generated/interface-001/index.html
object_kind:   website landing page
profiles:      [interface.v1]
observers:     [obs-reference]
date:          2026-07-16
conditions:    headless render 1280x800 (hero) and 1280x3200 (full page); computed styles from DOM
provenance:    known   # generated within the project; see note
---

# Observation Record — interface-001 (worked example)

> Worked example demonstrating Observation Language v1 on a real artifact. The object is
> the generated landing page from EXP-0002. **Provenance is `known`**, so the Attribution
> below is illustrative of the grammar, not an unbiased attribution study (an unbiased
> study requires `provenance: unknown`; see [Record Format §2](../RECORD-FORMAT.md)).

## Evidence

- **E1** — A single typeface family is used across headings, body, buttons, and price. It resolves to "Inter." · _derivation:_ measured
- **E2** — The typeface is loaded as an external dependency (Google Fonts), with a system-font fallback declared. · _derivation:_ reported
- **E3** — Display heading: 60px, weight 800, letter-spacing −0.03em. · _derivation:_ measured
- **E4** — Heading text color is slate `rgb(15,23,42)`; secondary text is slate `rgb(100,116,139)`. · _derivation:_ measured
- **E5** — Distinct colors across the document: 6 meaningful values (white, `rgb(248,250,252)`, `rgb(15,23,42)`, `rgb(100,116,139)`, `rgb(99,102,241)`, gradient partner `rgb(79,70,229)`). · _derivation:_ counted
- **E6** — A single accent hue, indigo `rgb(99,102,241)`, is used for logo mark, one headline word, primary buttons, icon tiles, list checkmarks, and the featured-plan treatment. · _derivation:_ measured
- **E7** — Gradients: 7 instances, all indigo-family at 135°. · _derivation:_ counted
- **E8** — Corner-radius values used: 8px, 10px, 12px, 999px. · _derivation:_ measured
- **E9** — The header applies a background blur over 80%-opacity white. · _derivation:_ measured
- **E10** — Shadows are low-opacity and soft (card `0 4px 24px rgba(15,23,42,0.06)`). · _derivation:_ measured
- **E11** — Three feature cards and three pricing plans are present, each with uniform internal structure. · _derivation:_ counted
- **E12** — Distinct repeated section schemas: 2 (centered head + three-column grid). · _derivation:_ counted
- **E13** — All primary sections are center-aligned; the two grids are symmetric three-columns. · _derivation:_ classified
- **E14** — Feature icons are emoji (📈, 🔔, 🎯). · _derivation:_ classified
- **E15** — Copy includes "Build better habits, one day at a time", "Everything you need to stay consistent", "Simple, transparent pricing", "Made with care." · _derivation:_ reported
- **E16** — Navigation primary button: text-on-background contrast 1.07:1. · _derivation:_ measured · _locus:_ header "Get started"
- **E17** — Hero primary button: text-on-background contrast 4.47:1. · _derivation:_ measured · _locus:_ hero "Start for free"
- **E18** — No depiction of the product's own interface is present. · _derivation:_ classified (absent)
- **E19** — Spacing values used: 8, 12, 24, 28, 88, 96 px. · _derivation:_ measured

## Relations

- **R1** — Visual ordering is carried by size and weight-800 on a two-step neutral scale, with the single accent as the only chromatic emphasis. · _relates:_ [E3, E4, E5, E6]
- **R2** — Feature cards and pricing plans receive an identical treatment vocabulary (border, radius, shadow, accent detail); no zone is treated differently from another. · _relates:_ [E8, E10, E11]
- **R3** — Structure repeats across only two schemas, and each schema's interior is fixed; both structural and surface variation are low. · _relates:_ [E11, E12]
- **R4** — The composition is symmetric throughout; no recurring asymmetry is present. · _relates:_ [E13]
- **R5** — The accent hue co-occurs with both interactive roles and decorative roles. · _relates:_ [E6, E7]
- **R6** — The navigation primary button pairs low-contrast text with the accent background, diverging from the hero primary button's pairing. · _relates:_ [E16, E17]

## Hypotheses

- **H1** — *Perceived conventionality is high:* each recorded dimension falls within common contemporary landing-page conventions (webfont sans, weight-800 negative-tracked display, single indigo accent, soft shadows, rounded cards, emoji icons). · _from:_ [E1, E3, E6, E7, E8, E14, R1, R2] · _refuted if:_ any recorded dimension is shown to fall outside contemporary convention for this object class · _status:_ supported
- **H2** — *Perceived proximity to genre conventions is high* for the "product landing page" genre: hierarchy, section schemas, and symmetric composition match genre norms. · _from:_ [R1, R3, R4] · _refuted if:_ structure or hierarchy is shown to depart from the genre's norms · _status:_ supported
- **H3** — The element pattern (external Inter + single indigo + gradient-clipped word + emoji icons + uniform token-styled cards) is characteristic of a **component/token-default production lineage** rather than a bespoke identity. · _from:_ [E1, E2, E6, E7, E14, R2] · _refuted if:_ the same pattern is shown to be specific to one brand rather than shared across unrelated objects · _status:_ tentative
- **H4** — *(competing)* The pattern reflects a **specific brand identity system**. · _from:_ [E6, E8] · _refuted if:_ the same pattern recurs across unrelated objects with no shared brand · _status:_ weakened — no brand-distinctive cue was recorded [E5, E6 show only default-range values; E18 notes no product depiction]
- **H5** — A legibility failure is present at the navigation primary button. · _from:_ [E16] · _refuted if:_ a corrected render shows adequate contrast · _status:_ supported

## Attribution

- **A1** — _type:_ category · _target:_ "contemporary product landing page" · _from:_ [H1, H2]
  · _confidence:_ supported · _immediacy:_ immediate
  · _discriminability:_ not distinguishable, by any recorded cue, from a large population of other product landing pages · _rank:_ 1
- **A2** — _type:_ production-method · _target:_ "assembled from conventional component/token defaults" · _from:_ [H3]
  · _confidence:_ tentative · _immediacy:_ on-analysis
  · _discriminability:_ overlaps with hand-built work that adopts the same defaults; the two cannot be separated from this object alone · _rank:_ 2
- **A3** — _type:_ brand · _target:_ indeterminate · _from:_ [H4]
  · _confidence:_ speculative · _immediacy:_ —
  · _discriminability:_ no brand-distinctive cue was recorded; retained as a competing attribution per commitment C4 · _rank:_ 3

> **Reading of this record.** The best-supported attribution is to a *category*, not a
> *brand*; brand attribution is indeterminate. This is the inverse of the project's
> first corpus, where cropped fragments were typically brand-attributable. The grammar
> records this outcome without discarding the weaker brand hypothesis, and without using
> any quantitative claim.

## Conformance (OL v1)
- [x] All four stages present
- [x] Evidence free of relation/outside/eval/causal/attribution
- [x] Every relation cites E-ids
- [x] Every hypothesis cites support, states refutation, has status
- [x] Every attribution declares type/target/support/confidence/immediacy/discriminability
- [x] Competing attributions retained and ranked
- [x] No numeric probability without cited estimator
