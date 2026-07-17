# Product

This pillar holds **Fingerprint the product** — the thing a person actually uses.

Everything else in this repository is research infrastructure:
[`observation-language/`](../observation-language/) is the grammar,
[`methodology/`](../methodology/) is the law, [`experiments/`](../experiments/),
[`corpus/`](../corpus/), [`atlas/`](../atlas/) and [`research/`](../research/) are the
apparatus that keeps the grammar honest. None of that is the product. It is the engine
behind the curtain.

The product is a single conversational **Skill**: a reflection partner for people who
design and build interfaces, often with the help of AI. It observes, it asks, it reveals
recurring pattern. It does not generate interfaces, hand out templates, prescribe styles,
or decide anything for the person using it. Its job is to make automatic decisions visible
so that the person's authorship gets stronger.

## Structure

| Path | Responsibility |
|---|---|
| [`fingerprint/`](fingerprint/) | The Skill artifact — the installable, runnable product. `SKILL.md` is its entry point. |
| [`docs/`](docs/) | Product-side documentation: architecture, roadmap, versioning, release notes. Distinct from the research `docs/`. |

## The line that must never blur

The research pillars follow the **Law of Observation** (describe and ask, never prescribe)
and the **Law of Judge Independence** (the system that makes a thing never validates it).
Those are not just research rules — they *are* the product's personality. Fingerprint the
Skill inherits them directly:

- It reflects in the **interrogative voice**. It surfaces what is present and asks what was
  intended. It never says *do this*.
- It is a **judge that never generated**. It does not produce the interface it discusses,
  and it never issues a verdict ("this looks AI-made"). It offers grounded observations the
  person judges for themselves.

If a proposed product behavior would break either law, the behavior is wrong, not the law.

## Two velocities

Per the project's standing law of **two velocities**: the research moves slowly and
deliberately; the product may move faster. But the product may only *use* research that has
reached a stable state. The product never reaches back into the research to change it, and
research findings are only ever surfaced to a user through the invisible bridge described in
[`fingerprint/references/observation-bridge.md`](fingerprint/references/observation-bridge.md),
never as raw Atlas entries or experiment numbers.

## Status

v0.1 — foundation. The Skill's core behavior, voice, reflection flows, and boundaries are
defined and runnable. See [`docs/roadmap.md`](docs/roadmap.md) for what is built and what
comes next.
