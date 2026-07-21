# EXP-0004 — Recognition Study

The measurement instrument: provenance-blind classification of AI-generated vs human-authored
interfaces, per human baseline class. Produces the program's first real number and the
free-text tell-corpus that feeds pattern attribution.

- [`protocol.md`](protocol.md) — the task, the two arms (human panel ground truth + model-judge
  proxy), the calibration gate, metrics, and threats.

**Status:** scaffolded. Judge = Pedro (n=1, blind); model-judge arm deferred. Awaits the
EXP-0003 Claude arm. Upstream: [EXP-0003](../EXP-0003-generator-corpus/). Downstream: EXP-0005.

Contents to be added during the study: `runs/` (per-session response records, provenance still
sealed) and, after scoring, `results/` (accuracy per class, calibration, the tell-corpus).
