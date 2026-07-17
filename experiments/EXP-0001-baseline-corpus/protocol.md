# EXP-0001 — Baseline Corpus of Excellent Interfaces

**Status:** Collection complete (23/23; 2 partial records pending visual re-capture). Recurrence analysis drafted (`analysis/recurrences.md`). Awaiting human review before anything feeds the Atlas.
**Started:** 2026-07-15
**Collection completed:** 2026-07-15
**Instrument:** v0.2 (two-layer)
**Type:** Field observation (non-interventional)
**Feeds:** Atlas Experimental (via human review only)

## Purpose

Build an observational corpus of interfaces widely regarded as excellent, **regardless of origin** (human- or AI-made). This corpus is the *baseline*. A second corpus of AI-generated interfaces (EXP-0002) will be collected afterwards. Only then will recurrences be compared (EXP-0003).

This ordering is deliberate: collecting the baseline first prevents the observer from anchoring on "AI look" traits and then finding them everywhere (confirmation bias).

## Corpus stratification

A baseline composed only of high-end SaaS would measure a single aesthetic school, not identity. The corpus is therefore stratified across natures of interface. Excellence is the entry criterion; the stratum guarantees the excellence comes in different aesthetics:

| Stratum | What it contributes to the baseline |
|---|---|
| SaaS / dev tools | The dominant contemporary school (also the school AI tools most imitate) |
| Professional tools | Interfaces shaped by daily expert use, not marketing |
| Editorial | Typography- and content-driven identity |
| E-commerce / product | Density, merchandising, photography-led surfaces |
| Experimental / studio | Interfaces that deliberately break genre conventions |
| Utilitarian systems | Identity through radical plainness (no styling ambition) |
| Portfolios | Single-author identity at maximum concentration |
| Hardware brands | Physical-product design language translated to web |

Each observation record states its stratum. Cross-corpus recurrence counts are reported per-stratum as well as overall.

## The two-layer instrument

- **Layer 1 — Objective:** verifiable facts (typeface, colors, radii, counts). Computed DOM styles preferred over visual inference. Two observers must converge.
- **Layer 2 — Relational:** relationships between elements (hierarchy mechanisms, refinement distribution, density rhythm, predictability, recurring asymmetry, deviation-from-convention, perceived signature). Observer-dependent by nature; every entry must anchor to Layer-1 facts or screenshot regions; evaluative vocabulary remains forbidden. A second observer may legitimately diverge — that divergence is data, not error.

The layers are never merged. A relational note can never be cited later as if it were a Layer-1 fact.

## What this experiment is NOT

- Not a proof of any hypothesis.
- Not a quality judgment of any interface.
- Not a detector, a theory, or a design guide.

## Observer discipline

The observer records **only objective, verifiable observations**. Forbidden vocabulary in observation records: "generic", "looks AI", "bad", "good", "beautiful", "boring", and any causal or evaluative language.

Allowed: descriptions of typeface classification, color counts, gradient presence, shadow intensity, border treatment, spacing distribution, visual density, layout type, typographic hierarchy, presence of glassmorphism/glow/blur, component patterns, card organization, navigation type.

Recurrences across interfaces are recorded as counts ("N of M interfaces use X"). Counts are observations, not conclusions.

Any suspected pattern is recorded strictly as:

> 🟡 Hypothesis — "We observed that…"

Never "We conclude that…". Promotion of any hypothesis is a human decision, downstream, in the Atlas (Law of Judge Independence).

## Procedure (per interface)

1. Navigate the live interface (marketing site and/or product surface) at desktop viewport 1280×800.
2. Capture screenshots of relevant regions (hero, navigation, components, content areas).
3. Record observations using `template.md`, one file per interface, in `observations/`.
4. Archive screenshots in `screenshots/<site-id>/`.

## Corpus (v0.2 — stratified; approved by steward 2026-07-15)

| Stratum | Sites |
|---|---|
| SaaS / dev tools | linear, stripe, vercel |
| Professional tools | figma, obsidian, blender |
| Editorial | the-pudding, nytimes, its-nice-that |
| E-commerce / product | apple, aesop, mcmaster-carr |
| Experimental / studio | mschf, cargo, poolsuite |
| Utilitarian systems | gov-uk, wikipedia, hacker-news |
| Portfolios | bruno-simon, rauno-me, joshwcomeau |
| Hardware | teenage-engineering, nothing |

23 sites total. Original v0.1 list was SaaS-dominant (arc, raycast, github, notion, framer excluded from this version to avoid single-school dominance); re-stratification recorded under Threats to validity.

## Threats to validity (declared upfront)

- Live sites change over time; every observation is dated.
- Marketing pages and product UIs are different surfaces; each record states which surface was observed.
- Single-viewport observation (desktop) in this version.
- Observer is an AI system; per the Law of Judge Independence, nothing here is validated — all outputs remain 🟡 until independent human review.
- **Corrected 2026-07-15:** initial corpus draft was SaaS-dominant; a single-school baseline would confound "excellence" with one aesthetic school. Corpus stratified in response (see Corpus stratification).
- Layer 2 is observer-dependent; with a single observer, relational observations carry no inter-observer reliability yet.
