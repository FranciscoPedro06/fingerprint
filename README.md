# Fingerprint

Fingerprint is an open research infrastructure for describing how observers recognize
visual identity, authorship, aesthetic convergence, and recurring pattern in designed
objects.

It is **not** a detector and does not classify objects as machine- or human-made. Its
purpose is to build a durable, reusable **observational language** and the research
apparatus around it, so that recognition itself can be studied with discipline: evidence
before interpretation, no conclusion without cited support, competing explanations
preserved.

## Why this exists

Observers can often recognize, almost instantly, that an object belongs to a certain
brand, studio, genre, era, or production method. That recognition is ordinarily left
implicit. Fingerprint exists to make it explicit and inspectable — to separate what is
actually present in an object from what an observer infers from it, and to record the path
between them.

## Structure

| Directory | Responsibility |
|---|---|
| [`observation-language/`](observation-language/) | The core grammar for observation. The heart of the project. Object-general, model-independent. |
| [`methodology/`](methodology/) | The laws and principles that govern how research is conducted. |
| [`experiments/`](experiments/) | Self-contained experiments (`EXP-NNNN`) that exercise and stress-test the language. |
| [`corpus/`](corpus/) | Reviewed observation records, written in the observation language. The project's data. |
| [`atlas/`](atlas/) | The catalog of phenomena and fingerprints discovered through observation, with explicit status. |
| [`research/`](research/) | Synthesized findings and notes that draw across experiments and corpus. |
| [`docs/`](docs/) | Cross-cutting documentation: glossary, governance, contribution. |

## Reading order

1. [`observation-language/`](observation-language/) — the grammar everything else is written in.
2. [`methodology/`](methodology/) — the rules the project holds itself to.
3. [`experiments/`](experiments/) — how the language was developed and tested.

## Principles in one paragraph

Description precedes interpretation. Every interpretation cites its evidence. Every
attribution declares its confidence and keeps the alternatives it outranks. The
observation language names no tool, model, or vendor, so that records written today remain
readable long after any specific technology is gone. Domain knowledge lives at the edges,
in profiles, so the core stays small and durable.

## Status

Early. The observation language is at v1 and stable for use; the corpus and atlas are
being populated through the experiment track. Nothing enters the validated atlas without
independent human review.

## Licensing

Documentation and research artifacts are intended for open reuse. Per-directory license
notes govern where they differ; see [`docs/`](docs/).
