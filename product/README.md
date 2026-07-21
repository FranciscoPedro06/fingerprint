# Product

> **Status (2026-07-20): repositioned as a downstream layer; feature-frozen, under maintenance.**
> The project moved to a [detector-first program](../research/PROGRAM.md): the core is now a
> system that detects, explains, and reduces the AI visual signature, and this generation Skill
> becomes a *consumer* of a validated discriminator rather than the center of the project. Its
> standing weakness — no independent detector, so it grades its own output on a curve — is
> exactly what the program exists to fix, and no amount of internal refinement closes it.
> **No new capability ships until that discriminator exists.** v0.4.0 is internal-discipline
> maintenance only: the checkable gates were promoted into the loop, effort is now calibrated to
> the surface, and the prose was cut roughly in half. Everything below describes it as it stands.

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

## Install

Pick one. All three give Claude the Fingerprint layer; they differ only in how it's delivered.

### 1. As a plugin (recommended — one command, versioned updates)

In Claude Code:

```
/plugin marketplace add FranciscoPedro06/fingerprint
/plugin install fingerprint@fingerprint
```

That's it. Open any project and start working on an interface — Claude loads Fingerprint on
its own when the task calls for it.

### 2. As a personal skill (simplest — works in every project)

Copy the skill into your personal skills directory:

```bash
git clone https://github.com/FranciscoPedro06/fingerprint
cp -r fingerprint/product/fingerprint ~/.claude/skills/fingerprint
```

Now `/fingerprint` is available everywhere, and Claude auto-invokes it on design tasks.

### 3. For local development / trying it out

```bash
git clone https://github.com/FranciscoPedro06/fingerprint
claude --plugin-dir ./fingerprint/product/fingerprint
```

Loads Fingerprint for that session only — good for hacking on it.

## How it works

You never talk to two systems. There is only Claude. Underneath, when the task is about a
screen, Claude runs one small loop:

```
intent  →  observe (silent)  →  reflect / decide where to deviate  →
execute (build the real thing)  →  honest second look  →  hand authorship back
```

It makes choices *legible* — it names what it chose and what it passed on — so the work stays
yours to keep or overrule. Start with [`fingerprint/SKILL.md`](fingerprint/SKILL.md) (what
Claude becomes) and
[`fingerprint/references/deviation.md`](fingerprint/references/deviation.md) (the craft of
building off the centroid).

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

v0.4.0 — the calibrated layer. The Skill guides Claude *through* building, refactoring, and
improving interfaces, not only reviewing them. The loop now opens with a surface gate (trivial /
functional / expressive) so effort matches the task, and closes with a scored audit rather than a
vibe-check: Kit-atom count, the cross-genre logo test, contrast, a named structural idea, a fork
shown. It carries a delivery contract with a WCAG AA floor, and `evals/` holds the prompts and
rubric it is checked against. See [`docs/roadmap.md`](docs/roadmap.md) for what comes next.
