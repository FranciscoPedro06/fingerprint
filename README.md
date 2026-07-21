# Fingerprint

**The first system built to detect, explain, and reduce the visual signature of
AI-generated interfaces.**

When a person looks at a screen and says *"this looks like AI made it,"* they are almost never
applying a rule — they recognize it, the way they recognize a face or a brand, in
milliseconds, and usually can't say why. Fingerprint's core question is that recognition:

> **What separates the distribution of AI-generated interfaces from human-authored ones, such
> that a human classifies membership instantly and can't articulate the reason?**

## The reframe: it's a distribution, not a style

It is tempting to treat the "AI look" as a *style* — a centroid you escape by choosing
differently (leave SaaS-indigo for editorial, leave editorial for brutalist). That fails
structurally: there are only a few fashionable centroids at a time, and moving off one lands on
another. The recognizability survives because it never lived in the *location*.

The signal lives in the shape of the **distribution**, not its center:

- **Low variance** — across wildly different briefs, AI returns the same skeleton re-skinned.
  The tell is *"I've seen this exact configuration a hundred times."*
- **Co-occurrence** — individually innocent atoms (a tracked eyebrow, a one-word-colored
  headline ending in a period, a two-button hero, a stat-triplet) travel together as a
  recognizable **bundle**. The pattern is a joint object, not a checklist.

So the "AI look" is **membership in a low-variance, tightly-correlated distribution** — which
is why swapping styles never removed it, and why a detector, not a style guide, is the thing
worth building.

## The program

Fingerprint is, first, an open research program that makes this falsifiable. Read
**[`research/PROGRAM.md`](research/PROGRAM.md)** for the full agenda; the short version is four
experiments:

| | Experiment | What it produces |
|---|---|---|
| **Detect** | [EXP-0003](experiments/EXP-0003-generator-corpus/) + [EXP-0004](experiments/EXP-0004-recognition-study/) | A two-sided, provenance-blind corpus (the same sealed briefs from AI generators and from three classes of human authors), then the first real number: can a blind observer tell them apart, and how well, per class? |
| **Explain** | EXP-0005 | The features, and above all the *co-occurrence bundles* and *variance signatures*, that carry the signal — as **numbered Atlas patterns** with measured discriminative weight, not a hand-written list. |
| **Reduce** | EXP-0006 | Whether a targeted intervention actually moves an interface out of the recognizable region — judged by the blind detector, never by the maker's self-grade. |

The human recognizer of record is a small **human panel**; a model-judge is a scalable proxy
only after it is shown to track the panel. The generator that produces an object never
validates observations about it (Law of Judge Independence).

## The research apparatus

| Directory | Responsibility |
|---|---|
| [`research/`](research/) | The program (`PROGRAM.md`) and cross-experiment syntheses. **Start here.** |
| [`observation-language/`](observation-language/) | The core grammar for observation. Object-general, model-independent. The heart of the method. |
| [`methodology/`](methodology/) | The laws and principles that govern how the research is conducted. |
| [`experiments/`](experiments/) | Self-contained experiments (`EXP-NNNN`) — corpus, recognition, attribution, reduction. |
| [`corpus/`](corpus/) | Reviewed observation records: the two-sided, provenance-blind data. |
| [`atlas/`](atlas/) | The catalog of phenomena and numbered patterns, with status and discriminative weight. |
| [`docs/`](docs/) | Cross-cutting documentation: glossary, governance. |

The research holds itself to a discipline: description precedes interpretation, every
interpretation cites its evidence, every attribution declares its confidence and keeps the
alternatives it outranks, and the language names no tool, model, or vendor — so records written
today stay readable long after any specific technology is gone.

## The generation layer (downstream — feature-frozen)

The repository also contains **[`product/`](product/)**, a generation Skill for Claude Code
that tries to build interfaces off the centroid. As of 2026-07-18 it is **repositioned as a
downstream consumer** of the detector: its standing weakness is that it has no independent
detector, so it grades its own output on a curve — exactly the gap the program above exists to
close. **No new capability ships until a validated discriminator can stand behind it.**
Maintenance of its internal discipline continues (v0.4.0 made its checkable gates explicit and
halved its prose), but that is housekeeping, not progress against the real gap.

It remains installable. In Claude Code:

```
/plugin marketplace add FranciscoPedro06/fingerprint
/plugin install fingerprint@fingerprint
```

Then open any project and start working on an interface — Claude loads Fingerprint on its own
when the task calls for it. For the other two install paths (personal skill, local
development) and what the Skill actually does, see [`product/README.md`](product/README.md).

## Status

Detector-first, research phase. The observation language is at **v1** and stable. The
generator corpus (EXP-0003) is scaffolded and awaiting generator access; the recognition study
(EXP-0004) runs uncalibrated until a human panel exists. Nothing enters the validated atlas
without independent human review.

## Licensing

Code is **MIT**. Research and documentation artifacts are **CC-BY-4.0**, intended for open
reuse. Per-directory notes govern where they differ; see [`docs/`](docs/).
