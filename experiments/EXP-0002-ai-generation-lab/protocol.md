# EXP-0002 — AI Generation Lab

**Status:** Active (lab mode, iteration 001)
**Started:** 2026-07-16
**Type:** Instrument validation via single-sample deep observation
**Instrument under test:** v0.2 (two-layer)
**Feeds:** Instrument v0.3 design; Atlas Experimental (via human review only)

## Purpose

This experiment does **not** build a corpus. Its purpose is to mature the observation
instrument by pointing it at generated interfaces one at a time and studying, in depth,
both what the instrument captures and what it fails to capture.

Governing principle, adopted project-wide as of 2026-07-16:

> **Never scale an instrument that is still learning to observe.**

We prefer a small number of exhaustively studied samples over a large number of
shallow ones. In this phase the interface is a probe for the instrument, not a
data point in a dataset. We are building the microscope, not collecting slides.

## Relationship to the original EXP-0002 plan

The original plan proposed 16 generated interfaces across 8 strata. That plan is
withdrawn. It scaled collection before the instrument had been stress-tested against
even one generated artifact. Corpus-scale generation is deferred until the instrument
is declared stable (exit criteria below).

## Method (per iteration)

1. **Brief.** Write one neutral generation brief (`briefs/brief-NNN.md`). No style
   vocabulary (no colors, fonts, moods, or design references). Seal it before generation.
2. **Generation.** Generate exactly one interface from the brief. Record the prompt,
   model, date, and parameters verbatim in `generation-log.md`. Store output under
   `generated/interface-NNN/`.
3. **Capture.** Render and screenshot with the EXP-0001 headless pipeline; extract
   computed DOM styles. Archive under `screenshots/interface-NNN/`.
4. **Observation.** Apply instrument v0.2 exhaustively (`observations/interface-NNN.md`).
   Layer 1 objective, Layer 2 relational, unchanged from EXP-0001 for comparability.
5. **Instrument critique.** In `instrument-critique/vNN-findings-NNN.md`, answer:
   what did the instrument capture? what stayed invisible? what was hard to record?
   what is redundant? what is too subjective? what should v0.3 add or change?
6. **Stop.** Do not refine the instrument or generate again without steward approval.

## Independence — declared limitation (highest priority)

The Law of Judge Independence requires that the generating system never be the
validating system. In this lab phase that law is **not yet satisfied**: the interface
is generated and observed within the same model and session. This is acceptable
*only* because the current goal is to test the instrument, not to produce a fair AI
sample. It is recorded here as the primary threat to validity.

**Requirement before any real EXP-0002 data collection:** generation must be moved to
an isolated context (separate agent/session with no knowledge of the Fingerprint
project or its hypotheses), so the generator cannot bias toward or away from the
traits under study.

## Exit criteria (when the instrument is "stable")

Advisory, to be ratified by the steward:

- Two consecutive iterations produce an instrument critique with **no new required
  fields** (only optional refinements).
- Every Layer-1 field is fillable from render/DOM without guesswork.
- Every Layer-2 field has an operational definition that a second observer could apply.
- Redundant fields removed; subjective fields either operationalized or explicitly
  demoted to lowest epistemic tier.

Only then does corpus-scale collection resume.

## Threats to validity (declared upfront)

- Generator = observer (see Independence). Primary limitation this phase.
- Single generating model (Claude). No cross-model variance.
- The brief contains the phrase "modern and professional" — a realistic user prompt,
  but one that may itself invite convergent output. Logged as a deliberate choice.
- n is intentionally tiny; nothing here is a finding about AI interfaces in general.
