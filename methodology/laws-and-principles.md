# Laws and Principles

Two tiers. **Laws** are non-negotiable and constrain everything the project does.
**Principles** are operating guidance derived from the laws and from experience; they may
be refined as the project learns.

---

## Laws

### Law of Judge Independence

The system that generates an object must never be the system that validates observations
about it. Validation and generation are kept in separate contexts. Where a single observer
both describes and attributes, that limitation is declared, and independent observers are
sought before an attribution is treated as more than one observer's view.

*Consequence:* attribution studies are run with the object's provenance withheld from the
observer, and multi-observer records preserve divergence rather than reconciling it.

### Law of Method

Methods are durable; content is perishable. The core of the project stores methods of
observation, not the specific things observed at a moment in time. A particular typeface,
color, or platform belongs in records and profiles, never in the core grammar or the
methodology.

*Consequence:* the [Observation Language](../observation-language/) names no tool, model,
vendor, or trend; domain specifics live in [profiles](../observation-language/v1/profiles/)
and in the [corpus](../corpus/).

### Law of Observation

The project describes and asks; it does not prescribe. Its outputs characterize what is
present and what it appears to belong to. It does not instruct anyone how an object should
be made.

*Consequence:* records contain evidence, relations, hypotheses, and attributions — never
recommendations.

### Law of Grounding

No conclusion without cited evidence. Every hypothesis cites the evidence and relations
that support it; every attribution cites the hypotheses it rests on and declares its
confidence. Competing explanations are preserved and ranked, not discarded.

*Consequence:* this law is enforced structurally by the Observation Language pipeline and
its conformance criteria.

---

## Principles

### Separate the phenomenon from its instances

A **phenomenon** is a recurring mechanism of recognition (for example, "recognition by
proximity to genre convention"). A **fingerprint** is a concrete instance through which a
phenomenon manifests at a point in time (for example, a specific accent color in wide use).
Fingerprints change; phenomena persist. The two are recorded separately (see the
[Atlas](../atlas/)).

### Status is always explicit

No hypothesis is presented as established fact. Findings carry status — experimental or
validated — and the transition between them requires independent human review under the
Law of Judge Independence.

### Never scale an instrument that is still learning to observe

Before collecting at scale, the instrument of observation must be shown to observe well.
The project prefers a small number of exhaustively studied samples, each followed by a
critique of the instrument, over a large number of shallow ones. Corpus-scale collection
resumes only when the instrument is stable (defined per experiment).

*Origin:* adopted after EXP-0002 iteration 001, where a single deeply studied sample
produced more instrument insight than a planned sixteen-sample corpus would have.

### Build the reusable artifact, not the one-off

Nothing is produced solely for the experiment at hand. Each artifact is written so that an
unrelated researcher could reuse it to study interfaces, branding, design systems,
products, physical systems, or any visual object.
