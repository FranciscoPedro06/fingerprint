# Product Roadmap

The product moves on the fast velocity; it may only stand on research that has reached a
stable state. Each milestone names the research version it depends on.

---

## v0.1 — Foundation ✅ (current)

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

- An interface **generator** or "apply the fix" button.
- A **score, rating, or AI-detector** verdict.
- A **template / style-kit** library.
- A **silent** profile of the user built without their awareness.

If a future request points here, it's a research or scope question for Pedro — not a product
task to quietly pick up.
