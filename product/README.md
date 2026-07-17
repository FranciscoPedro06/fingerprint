# Product

This pillar holds **Fingerprint the product** — the thing a person actually uses.

Everything else in this repository is research infrastructure:
[`observation-language/`](../observation-language/) is the grammar,
[`methodology/`](../methodology/) is the law, [`experiments/`](../experiments/),
[`corpus/`](../corpus/), [`atlas/`](../atlas/) and [`research/`](../research/) are the
apparatus that keeps the grammar honest. None of that is the product. It is the engine
behind the curtain.

The product is a single **Skill**: a design-intelligence layer that runs on top of Claude and
changes *how* Claude thinks whenever the work touches an interface. The person keeps using
Claude normally — but when they say "create a landing page," "analyze my frontend," or
"refactor this dashboard," the reasoning underneath understands intent first, observes before
acting, builds with deliberate and legible choices instead of generic defaults, and takes an
honest second look at the result. It builds, refactors, and reviews — but it never imposes its
own taste, never decides for the person, and always hands authorship back. Its job is to defeat
the "AI look" (the absence of deviation) in both directions: making real choices when building,
and making automatic choices visible when reviewing.

## Structure

| Path | Responsibility |
|---|---|
| [`fingerprint/`](fingerprint/) | The Skill artifact — the installable, runnable product. `SKILL.md` is its entry point. |
| [`docs/`](docs/) | Product-side documentation: architecture, roadmap, versioning, release notes. Distinct from the research `docs/`. |

## The line that must never blur

The **Law of Judge Independence** is a research-integrity law: the system that *generates* the
Atlas never *validates* it. That law governs the research apparatus — it is not a ban on the
product building things. The product's own version of it is the **Honest Second Look**: after
Claude builds, it turns the same critical eye on its own output and says plainly where it still
landed on the centroid. Maker and honest critic live in the same turn.

What the product inherits, unconditionally:

- **Observation before action** (Law of Observation). It looks at what is concretely present —
  a reference, a codebase, its own draft — before interpreting or building, and when it
  reflects, it describes and asks rather than lecturing.
- **Handed-back authorship.** It makes real choices when building, but keeps them *legible* —
  named, with an alternative shown — and never imposes its taste as the correct answer or
  decides for the person. No verdicts ("this looks AI-made"); the person judges.
- **Grounding.** No claim it can't point at. When unsure, it says so.

If a proposed product behavior would break one of these, the behavior is wrong, not the law.

## Two velocities

Per the project's standing law of **two velocities**: the research moves slowly and
deliberately; the product may move faster. But the product may only *use* research that has
reached a stable state. The product never reaches back into the research to change it, and
research findings are only ever surfaced to a user through the invisible bridge described in
[`fingerprint/references/observation-bridge.md`](fingerprint/references/observation-bridge.md),
never as raw Atlas entries or experiment numbers.

## Status

v0.2 — the execution layer. The Skill now guides Claude *through* building, refactoring, and
improving interfaces (not only reviewing them), using the intent → observe → reflect → execute
→ honest-second-look → hand-back loop. See [`docs/roadmap.md`](docs/roadmap.md) for what is
built and what comes next.
