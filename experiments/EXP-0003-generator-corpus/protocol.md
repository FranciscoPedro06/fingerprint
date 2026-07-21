# EXP-0003 — Brief Battery + Generator Corpus

**Status:** Scaffolded; collection blocked on generator access (see §8).
**Started:** 2026-07-18
**Type:** Corpus construction — the two-sided, provenance-blind, brief-matched image corpus.
**Feeds:** EXP-0004 (recognition study) and EXP-0005 (pattern attribution).
**Governed by:** [Research Program](../../research/PROGRAM.md), Law of Judge Independence,
"never scale an instrument still learning to observe."

## Purpose

Produce the raw material the whole program depends on: interfaces generated from the **same
sealed briefs** by (a) a set of AI generators and (b) three classes of human authors, captured
through **one identical pipeline**, with provenance **sealed away from every downstream
observer**. Without this corpus there is nothing to detect, explain, or reduce.

This experiment collects and captures only. It does **not** observe, score, or compare —
that is EXP-0004 and EXP-0005. Keeping collection separate from judgement is what lets the
judgement be blind.

## The two sides

**AI side** — each brief run through each generator in scope. The generator set is extensible
to Lovable, Bolt, v0, Framer AI, ChatGPT, Cursor, Replit, Firebase Studio; the **first corpus is
Claude-only** (Pedro's decision, 2026-07-18). One output per (brief × generator), first-shot, no
iterative refinement (iterative polish is a separate variable, deferred). Within-brief repeat
generations are allowed and encouraged, to measure the generator's own variance.

> **Scope limitation of a single-generator corpus.** With only Claude on the AI side, the study
> can test **H1** (can a blind judge tell Claude-made from human-made?), **H4** (Claude vs
> trend-following human), and begin **H2** (which features/bundles carry the signal *for
> Claude*). It **cannot** test **H3** — whether the signature is shared across generators — which
> requires at least a second generator. H3 is explicitly deferred until the set widens. Every
> claim from this corpus is scoped to *"Claude, at this version and date,"* never "AI in general."

**Human side** — for each brief/genre, matched counterparts in three reference classes
(defined in the [Program §5](../../research/PROGRAM.md)):

1. **typical-professional** — real shipped sites of ordinary quality;
2. **curated-excellent** — the EXP-0001 class of recognized excellence;
3. **trend-following-human** — human-made sites that deliberately follow current fashion
   (the control that tests whether recognition tracks *authorship* or *fashion*).

Human-side samples are found, not commissioned: real interfaces matched to each brief's genre
and content shape. Where an exact brief match does not exist in the wild, the closest genuine
interface of that genre and class is used and the imperfect match is logged.

## The brief battery

Twelve neutral briefs spanning the expressive↔functional spectrum, in
[`briefs/brief-battery.md`](briefs/brief-battery.md). Briefs carry **no style vocabulary**
(no colors, fonts, moods, or design references) and are **sealed before generation**. Genre
spread is deliberate: the "AI look" behaves differently on an expressive landing page than on
a functional dashboard, and the corpus must let that difference surface.

## Capture pipeline (identical for every sample)

One pipeline for all sides, so that fidelity and polish can never masquerade as the signal:

- Render at a fixed viewport (1280×800 hero + full-page), headless, per the EXP-0001 pipeline.
- Export **neutral PNG** only. No DOM, no URL, no framework hints travel with the image an
  observer sees.
- Where computed-style extraction is done for the later feature vector, it is stored in the
  **sealed manifest**, never beside the observer-facing image.
- Record capture parameters per sample (viewport, engine, date).

## Blinding procedure (load-bearing)

1. Every sample gets an **opaque sample-id** (e.g. `S-0007`) at capture time.
2. The observer-facing artifact is the PNG named by sample-id only — no source, class, brief,
   or generator in the filename or the image.
3. All provenance (brief-id, genre, source-class, generator+version or site+date, capture
   params, human-side match quality) lives in a **sealed manifest** kept out of the directory
   any EXP-0004 observer or model-judge can read.
4. The manifest is unsealed only during scoring, by whoever computes results — never by an
   observer while judging.

Manifest row schema (sealed): `sample-id · brief-id · genre · source-class ·
{generator+version | site+capture-date} · capture-params · match-quality · notes`.

## Sequencing — pilot before battery

Per the standing law, the pipeline is proven small before it scales:

- **Pilot:** 2–3 briefs spanning the spectrum (one expressive, one mixed, one functional),
  run through the reachable generators + one human counterpart per class. Confirm: identical
  capture across sides, clean blinding, no provenance leak, comparable framing.
- **Critique:** does any step leak provenance? is the capture truly identical across sides?
  is any generator's output systematically un-capturable? Fix before scaling.
- **Battery:** only after the pilot is clean does the full 12-brief battery run.

## Independence — two separate requirements

**1. Collector ≠ open-seal judge.** The person or process that collects and seals the corpus
MUST NOT be the recognizing observer of the same samples in EXP-0004 with the seal open.
Collection knows provenance by necessity; judgement must not.

**2. Generator must be naive (the isolation requirement — load-bearing for the Claude arm).**
For a Claude sample to represent *what Claude produces*, it must be generated by a Claude context
with **no knowledge of Fingerprint, its hypotheses, "the Kit," or the anti-centroid work**. A
context that knows the theory will generate atypically — either performing the tells or dodging
them — and poison the corpus. This is the same requirement EXP-0002 flagged as mandatory before
any real collection.

*Consequence:* samples MUST NOT be generated from a session (like the one that designed this
program) that is saturated with the theory. Each Claude sample is generated in an isolated
context that receives **only the sealed brief text** and nothing else. The generation prompt,
model version, date, and the fact of isolation are logged in the manifest.

## Decisions (Pedro, 2026-07-18)

- **Generators:** Claude only, for now. Single-generator scope limitation applies (above).
- **Collection ethics:** confirmed — public-output-only, no ToS circumvention, no defeating
  bot-protection. Continuous with EXP-0001 policy.

## Open — gates the AI arm

- **How the naive Claude arm is generated.** Per the isolation requirement, samples cannot come
  from this theory-saturated session. The remaining choice is *how* the isolated, brief-only
  generation is run. Pending Pedro's decision.

## Threats to validity (declared upfront)

- **Polish / fidelity confound** — mitigated by one identical capture pipeline and brief/genre
  matching. The primary construction risk.
- **Access asymmetry** — some generators are easier to reach than others; an under-sampled
  generator must not be read as representative. Log coverage per generator.
- **Human-match imperfection** — real sites rarely match a brief exactly; every imperfect match
  is logged as `match-quality` so it can be controlled for.
- **Non-stationarity** — every AI sample is stamped generator + version + date; the corpus is a
  dated snapshot, not a timeless population.
- **First-shot choice** — using first-shot AI output (no refinement) is a deliberate, logged
  decision; iterative-refinement corpora are a later, separate variable.
