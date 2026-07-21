# Fingerprint Research Program

**Status:** Active — supersedes the prior direction as of 2026-07-18.
**Voice:** research agenda. This document states the question, the hypotheses, the
architecture that serves them, and the experiment sequence. It contains no design
heuristics and prescribes no visual choices.

---

## 0. Direction change (governance)

The project previously held: *research serves the product; the product is a generation
Skill.* That is superseded.

**New direction — detector-first.** Fingerprint's core is a system that can **detect,
explain, and reduce** the visual signature of AI-generated interfaces. Generation (the
Skill) becomes a **downstream consumer of a validated discriminator**, not the center of
the project. The Skill is not deleted and is not edited under this program; it is paused
in place and reframed as downstream.

Why the inversion: "reduce" is meaningless without "detect." The generation Skill's
standing weakness is that it has no independent detector, so it grades its own output on a
curve — the Judge-Independence problem, unsolved across every prior iteration. This program
builds the missing instrument first and makes the whole enterprise falsifiable.

---

## 1. The reframe: distribution, not location

The prior frame located the "AI look" at a **point** in design space — a centroid — and
tried to move away from it. This failed structurally: there are only a few fashionable
centroids at a time (SaaS-indigo → editorial-premium → dark-luxury → terminal-brutalist),
and moving off one lands on another. Moving the **mean** left everything else intact.

A human does not recognize a location. Recognition of "this looks like AI" behaves like
recognition of a brand or a face: fast, confident, and usually **unaccompanied by an
explanation**. That is pattern recognition over a *distribution*, and a distribution has
three properties — only one of which the prior program attacked:

1. **Mean** (the centroid) — perishable, plural, and *not* where the signal lives.
2. **Variance** — how tightly outputs cluster. AI output has abnormally **low variance**:
   across wildly different briefs it returns the same skeleton re-skinned. The tell is
   "I have seen this exact configuration hundreds of times." A variance signature, not a
   style.
3. **Co-occurrence structure** — which features *travel together*. Individually innocent
   atoms (tracked eyebrow, one-word-colored headline ending in a period, two-button hero,
   stat-triplet) form a recognizable **bundle**. The pattern is a *joint* object, not a
   list of marginals.

**Working hypothesis of the program:** the "AI look" is **membership in a low-variance,
tightly-correlated distribution**, not proximity to a point. Escaping to a different
centroid preserves the variance and co-occurrence structure, so recognizability survives —
which is exactly what the prior program observed and could not explain.

---

## 2. Central question

> **What separates the distribution of AI-generated interfaces from the distribution of
> human-authored ones, such that a human observer classifies membership in milliseconds
> and usually cannot articulate why?**

---

## 3. Hypotheses (each falsifiable, each scoped to its corpus)

- **H1 — Existence.** Provenance-blind human observers separate AI-generated from
  human-authored interfaces above chance. *If false, the premise collapses — and that is a
  real, informative outcome.*
- **H2 — Distributional locus.** The discriminative signal lives more in **variance**
  (low choice-entropy across briefs) and **co-occurrence** than in any single marginal
  feature. *Test:* a discriminator using only variance/co-occurrence features rivals one
  using marginals; ablating a single feature barely dents recognition, ablating a bundle
  does.
- **H3 — Phenomenon vs fingerprint (moving target).** The *location* of the AI
  distribution shifts across generators and versions, but a **shared** variance +
  co-occurrence signature persists across generators. *Test:* features that predict "AI"
  for one generator also predict it for others; the shared predictor is structural, not
  attribute-level.
- **H4 — The confound (deepest risk).** Observers may be recognizing **current web
  fashion / trend-conformity**, not model authorship. *Test:* the trend-following-human
  control (§5). If trend-following human work is indistinguishable from AI output, the
  true phenomenon is *centroid-of-the-moment membership*, not *made-by-a-model* — a
  sharper, truer claim, not a failure.
- **H5 — Reducibility (the product claim).** A targeted intervention on a candidate
  lowers the blind detector's recognition rate and keeps it down under a cross-genre
  swap.

---

## 4. Reoriented architecture (what serves what now)

Nothing durable is thrown away; the existing infrastructure was, if anything, built for
this question before we knew it.

| Pillar | Role under the prior direction | Role now |
|---|---|---|
| **Observation Language v1** | grammar for single-object observation | unchanged core; **+ a distributional profile** (corpus-level: choice-entropy, co-occurrence / PMI, cluster tightness) as an *additive* profile — grow at the edges, never inflate the core |
| **interface.v1 profile** | two-layer single-interface instrument | unchanged; Layer-1 = the raw feature vector, Layer-2 = the structural/co-occurrence observations. Attribution-target space made explicit for **human-authored vs generator-authored**, kept blind to the observer |
| **Atlas** | catalogue of recurrences | home of **numbered patterns** (fingerprints), each with a *measured discriminative weight*, refutation condition, and generator/version/date stamp; **phenomena** = the durable mechanisms |
| **Corpus** | 23 curated human interfaces + 1 lab sample | must now hold **both** the human reference distributions (three classes, §5) **and** the AI generator distribution, brief-matched, provenance withheld |
| **Experiments** | instrument maturation | the new sequence, §6 |
| **Product / Skill** | the product | **paused, untouched**; reframed as downstream consumer of a validated discriminator |

Three existing laws become load-bearing rather than peripheral:

- **Judge Independence** — the generator's context never sees the detector. This is what
  makes the blind discriminator valid; it is now the program's central law.
- **Phenomenon vs fingerprint** — already encodes the moving-target problem (H3): the
  phenomenon persists, the month's fingerprints die.
- **Never scale an instrument still learning to observe** — each experiment runs small,
  is critiqued, then scales.

---

## 5. The human baseline: three reference distributions (sequenced)

"AI-generated" means nothing without a defined "human-authored" it is contrasted against.
The program uses **three** human reference classes, collected and analyzed in sequence,
because each answers a different question:

1. **Typical-professional** — real shipped sites of ordinary quality (not award winners).
   The clean first contrast to establish whether the phenomenon exists at all (H1).
2. **Curated-excellent** — the EXP-0001 class of recognized excellence. Bounds the *upper*
   end of human authorship; tests whether "AI look" is really "absence of excellence."
3. **Trend-following-human** — the hard control: human-made sites that deliberately follow
   the current fashion. Directly tests H4. This is the class that can falsify the whole
   "authorship" claim and replace it with the "trend-centroid" claim.

Each is a separate distribution, never pooled into a generic "human" bucket — the
comparison against each is a distinct result.

---

## 6. The experiment sequence

Ordered so that the **measurement instrument is built before anything is measured at
scale**, and so that generation (the product) re-enters only at the end, judged by an
independent instrument.

### EXP-0003 — Brief Battery + Generator Corpus
Build the two-sided, provenance-blind, brief-matched image corpus.

- **Brief battery.** A fixed set of neutral briefs spanning the expressive↔functional
  spectrum (genre matters — a functional dashboard and an expressive landing page are
  different populations). Briefs carry no style vocabulary; sealed before use, per the
  EXP-0002 discipline.
- **AI side.** Each brief run through the generator set: **Lovable, Bolt, v0, Framer AI,
  Claude, ChatGPT, Cursor, Replit, Firebase Studio** (extensible). Prompt, tool, version,
  date logged verbatim.
- **Human side.** For each brief/genre, matched counterparts in the three baseline classes
  (§5).
- **Capture.** One standardized pipeline for every sample (fixed viewport, neutral PNG,
  provenance stripped from the artifact) so that fidelity/polish cannot masquerade as the
  signal.
- **Declared constraints.** Collection is public-output only, no ToS circumvention, no
  defeating bot-protection — continuous with the EXP-0001 capture policy. Several
  generators cannot be driven programmatically and require account access or manual
  capture; this is a hard external dependency, flagged in §8.

### EXP-0004 — Recognition Study (measures H1, H4)
The first real number the project produces.

- Provenance-blind, forced-choice: *human-made or AI-made?* + confidence + response
  immediacy (time) + free-text *"what tipped you off."*
- **Small human panel first** as the ground-truth arm; a model-judge arm runs in
  parallel for later calibration (§7).
- **Primary metric:** recognition accuracy vs chance, **reported per baseline class**.
  Accuracy against the *trend-following-human* class is the acid test for H4.
- **Outputs:** the accuracy ceiling (how real the phenomenon is) and the free-text
  tell-corpus — treated as *hypotheses*, not ground truth, since the whole point is that
  people recognize before they can explain.

### EXP-0005 — Pattern Attribution (measures H2, H3 — the "explain")
Derive the numbered patterns instead of hand-authoring a reflex list.

- From the EXP-0003 corpus: marginal distributions; choice-entropy per dimension per
  source; **co-occurrence / PMI matrices**; cluster tightness per source.
- From the EXP-0004 free-text: cluster the human-named tells; cross-reference against the
  statistical patterns.
- **Ablation:** mask a feature or a bundle (via controlled edit/regenerate) and re-measure
  recognition (EXP-0004 apparatus) — this is what separates a *marginal* tell from a
  *bundle* tell (H2).
- **Cross-generator generality** check (H3): does a pattern predict "AI" across generators,
  or only for one?
- **Output:** numbered **Atlas patterns**, each carrying: discriminative weight, marginal
  vs bundle, cross-generator generality, refutation condition, generator/version/date
  stamp. *This* is what would later let any tool say "you combined pattern #18 + #42 + #63"
  truthfully.

### EXP-0006 — Reduction (measures H5 — the product loop)
Generation re-enters, judged independently.

- Take candidate interfaces; apply targeted interventions informed by EXP-0005.
- Re-run the **blind EXP-0004 detector** as the outcome metric — never a self-critique.
- **Success:** recognition rate drops and *stays down* under a cross-genre swap.
- This closes the Judge-Independence gap that every prior product iteration left open.

---

## 7. Model-judge calibration (per the ratified decision)

The recognizer of record is a **human panel**; a model-judge is a **scalable proxy only
after** it is shown to track humans.

- EXP-0004 runs human and model arms in parallel on the same blind samples.
- Establish agreement (label-agreement rate, rank correlation on confidence/immediacy)
  **before** the model-judge is trusted to scale EXP-0005/0006.
- State the acceptance criterion for "model-judge trustworthy" up front, and re-verify it
  whenever generators or model versions change (non-stationarity, §9).

---

## 8. External dependencies (owner: Pedro)

The program cannot proceed past EXP-0003 setup without decisions/access that are not mine
to take:

- **Generator access.** Claude and ChatGPT I can drive. Lovable, Bolt, v0, Framer AI,
  Cursor, Replit, and Firebase Studio need account access or manual capture. Which
  generators are in scope for the first corpus, and how their outputs are captured, is a
  Pedro decision.
- **Human panel.** EXP-0004's ground truth needs real human observers. Who they are, how
  many, and how they are shown samples is a Pedro decision. Until a panel exists, EXP-0004
  runs model-only and is explicitly labeled *uncalibrated*.
- **Collection ethics.** Public-output-only and no-circumvention are assumed from existing
  policy; confirm before any at-scale capture.

---

## 9. Threats to validity (foregrounded, as controls)

- **Trend vs authorship (H4)** — controlled by the trend-following-human baseline. The
  single most important control; without it the study may measure fashion and call it AI.
- **Polish / fidelity confound** — controlled by one standardized capture pipeline and
  brief/genre matching. If AI samples were thumbnails and human samples production sites,
  the study would measure polish.
- **Judge sharing our priors** — a model-judge is a proxy, gated behind human calibration
  (§7); humans are ground truth for the recognition claim.
- **Non-stationarity** — the AI distribution shifts every model release. Every corpus is
  stamped generator + version + date; only **phenomenon-level** claims are meant to be
  durable, and even those are re-checked over time.
- **Scope / base rates** — "AI look" is always relative to *which* generators, *which*
  briefs, *which* era. Every claim is scoped to its corpus; no claim is stated as universal.
- **Small n / premature scaling** — the standing law applies: instrument first, scale
  only after the instrument is shown to observe well.

---

## 10. What this program does *not* do

- It does not prescribe visual choices, propose heuristics, or define a "correct" style.
- It does not treat the human free-text rationalizations as ground truth.
- It does not let a generator validate itself.
- It does not edit or delete the existing Skill; the Skill is out of scope until a
  validated discriminator exists to stand behind it.
