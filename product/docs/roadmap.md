# Product Roadmap

The product moves on the fast velocity; it may only stand on research that has reached a
stable state. Each milestone names the research version it depends on.

---

## v0.2 — Execution layer ✅ (current)

The pivot (2026-07-17): Fingerprint stops being a reflection-only mirror and becomes the layer
that guides Claude *through* building, refactoring, and improving interfaces — not only
reviewing them. Claude stays the executor; Fingerprint changes how it thinks.

- [x] Rewrote `SKILL.md` to the execution-layer constitution: four laws (Observation, Honest
      Second Look, Grounding, Handed-Back Authorship) + the six-step loop (intent → observe →
      reflect → execute → honest-second-look → hand-back) covering build / analyze / refactor.
- [x] `description` frontmatter widened to auto-trigger on build requests ("create a landing
      page," "build a UI," "refactor this dashboard") as well as reviews.
- [x] New `references/deviation.md` — the craft of building off the genre centroid: the three
      tests (deliberate / coherent / legible), the centroid map, where to spend deviation.
- [x] Rewrote `capabilities-and-limits.md` and `first-contact.md` for the build path.
- [x] Reconciled `product/README.md`, `docs/product-architecture.md`, `docs/roadmap.md`,
      version → 0.2.0. Law of Judge Independence clarified as research-integrity, not a product ban.
- [x] Reconciled the softer references (`voice.md`, `reflection-flows.md`, `inputs.md`,
      `examples/session-transcripts.md`) to the build path.
- [x] Installable packaging — plugin + marketplace, verified end to end (`claude plugin`).
- [x] **v0.2.1 — the anti-centroid sharpening (Pedro's correction, 2026-07-17).** The v0.2
      examples had escaped the SaaS centroid straight into the *editorial / premium-minimal*
      centroid (cream + serif + sage) — itself the newest AI tell. Encoded the real discipline:
      the AI look *moves*; **verifiable origin** for every visual decision (never "it's pretty");
      a silent reference pass over *real* companies (not showcases); reflex-flag list (Inter/
      Geist/Satoshi, editorial beige/green, giant hero, glassmorphism…) allowed only when
      justified; and a mandatory skeptical self-critique ending in the **logo test** (iterate if
      it still reads AI-generated). Rewrote `deviation.md`; sharpened `SKILL.md` (Law of
      Grounding now covers generation; observe + second-look steps); de-contaminated the build
      examples in `session-transcripts.md` and `first-contact.md`; added the "escaped into the
      editorial centroid" anti-pattern.
- [ ] NEXT: a runnable eval proving "create a front" feels different from a normal prompt, and
      that it survives the logo test — `claude plugin eval` with a no-plugin baseline arm.
- [ ] NEXT (deeper craft): per-genre centroid maps drawn from EXP-0001/EXP-0002 so the reference
      pass has real recurrence data to lean on, not just genre intuition.

Depends on: `observation-language/v1`, `interface.v1` profile, `methodology` laws.

## v0.1 — Foundation ✅ (done)

The Skill exists, runs, and holds its shape. This is the spine everything else hangs from.

- [x] Product pillar established (`product/`), separated cleanly from research.
- [x] Product architecture defined (`docs/product-architecture.md`).
- [x] The Skill artifact: `SKILL.md` core (identity, when to engage, the loop, boundaries).
- [x] Voice guide with the interrogative-voice craft and side-by-side examples.
- [x] Reflection flows: entry paths, session progression, working state, opt-in memory.
- [x] Observation bridge: the silent pipeline and the rule of the curtain.
- [x] Capabilities and limits with warm decline patterns.
- [x] Worked session transcripts, including anti-patterns.
- [x] First contact / first-run experience — the thirty-second "why it's different" moment.
- [x] Input handling for the real entry points (screenshot, URL, HTML/code, Figma, description) with safety and privacy behavior.

Depends on: `observation-language/v1`, `interface.v1` profile, `methodology` laws.

Hierarchy this phase locks in: **Research serves Product, never the reverse.** Research → Atlas → Observation Engine → Reasoning → Skill → User. The user only ever meets the last block.

## v0.2 — Sharpen the eye

Make the observation richer and the reflections more precise, without widening scope.

- [ ] Expand the observation bridge with per-dimension "what to look for" cues drawn from
      EXP-0001 recurrence findings (as background for the eye, never as content to hand over).
- [ ] A concrete library of grounded question patterns per dimension (color, type, spacing,
      copy, motion), so reflections stay fresh instead of formulaic.
- [ ] Handling for multi-screen / flow-level observation (today's design assumes a single
      screen).
- [ ] Calibration set: 15–20 gold-standard reflection turns to test voice against.

Depends on: stable EXP-0001 recurrence analysis; interface instrument at v0.3 if ratified.

## v0.3 — Memory and continuity

Make the partner feel like it *knows the person* across sessions — safely.

- [ ] Opt-in carried memory: stated intentions, design values, recurring tendencies.
- [ ] Explicit surfacing UX: the person always sees what's remembered; one command to forget.
- [ ] "Your emerging signature" reflection — tendencies offered as observation, never score.

## v0.4 — Robustness

- [ ] Graceful behavior on degraded input (tiny crop, low-res screenshot, partial code).
- [ ] Clear behavior when asked to observe something it genuinely can't (audio, video, PDF
      of a print piece) — decline or adapt honestly.
- [ ] Stress-tested decline patterns against persistent pressure for verdicts/fixes.

## v1.0 — Public

- [ ] Full evaluation pass (see `../fingerprint/` test plan) green.
- [x] Onboarding: a first-run experience that teaches the person what this is in one exchange. *(built in v0.1; refine against real first-use sessions before public.)*
- [ ] Public documentation and a short "how it thinks" explainer (curtain lifted, plainly).
- [ ] Versioned release with pinned research dependencies stated.

---

## Explicit non-goals (any version)

These will not be built, ever, without overturning a project law:

- **Taste imposed as truth** — building is in scope, but never presenting Fingerprint's choices
  as the objectively correct design, and never overwriting a choice the person claimed as
  theirs. Choices stay legible and reversible.
- **Silent shipping of the centroid** — delivering the generic default without the honest
  second look that says where it came out average.
- A **score, rating, or AI-detector** verdict.
- A reusable **template / style-kit / house-style** library applied blindly across projects.
- A **silent** profile of the user built without their awareness.

> Note: an interface **generator** used to sit on this list. As of v0.2 (2026-07-17, Pedro's
> explicit direction), building *is* the product — wrapped in intent → observe → reflect →
> execute → honest-second-look → hand-back. What stays forbidden is imposing taste and shipping
> the average silently, not the act of building itself.

If a future request points at the remaining items, it's a scope question for Pedro — not a
product task to quietly pick up.
