# Product Roadmap

The product moves on the fast velocity; it may only stand on research that has reached a
stable state. Each milestone names the research version it depends on.

---

## v0.3 — The Kit + genre calibration ✅ (current)

Two more outputs (a ledger barbershop "Corvo", a precision dental clinic "Meridiano") exposed the
two remaining holes, and Pedro authorized fixing them (the "A/B/C" + "make the skill perfect"
mandate, 2026-07-17):

- [x] **The Kit** (`references/the-kit.md`): named the **genre-independent** atoms the model
      re-assembles on *every* brief — its own fingerprint. Evidenced across four outputs (Ofício,
      Régua, Corvo, Meridiano): the `·`-caps eyebrow, the one-word-colored headline ending in a
      period, the stat triplet, mono labels, cream/charcoal-with-grid background, the right-side
      hero plate, "DESDE 20XX", two-button hero — plus verbatim self-citation ("LUZ DE TUNGSTÉNIO"
      in two outputs). Rule: **3+ Kit atoms = you shipped your own fingerprint, not theirs**,
      regardless of restyle. This is the concrete attack on "mais do mesmo."
- [x] **Genre calibration** (SKILL.md loop step 1): read the **expressive ↔ functional** spectrum
      first. Expressive → full escape-the-centroid. Functional (dashboard, form, checkout, docs) →
      clarity, hierarchy, convention-done-impeccably, correctness; distinctiveness is *not* the
      goal and a forced "structural idea" is the failure (gov.uk = radical conventionality). The
      Kit is refused on both. (Answers the C-boundary: serve both, adapt — don't refuse functional.)
- [x] **Theme ≠ structure** (SKILL.md loop step 3): a structural idea reorganizes the
      *composition*, not the copy; a page that *mentions* a ledger but keeps the hero skeleton has
      a theme, not a structure (the Corvo lesson).
- [x] Stress-test (the "A") folded into the Kit evidence + the genre table; VERSION → 0.3.0.
- [ ] NEXT: the independent judge remains the real ceiling — an eval / cold second-pass reviewer,
      because the maker grades on a curve (the Kit's own honest-limit note).

## v0.2 — Execution layer ✅ (done)

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
- [x] **v0.2.2 — the self-critique ruthlessness fix (live dogfood, 2026-07-17).** Pedro ran
      "crie um frontend para uma barbearia" on v0.2.1. It reasoned well (asked intent, cited real
      barbershops, tabled its choices) but the **honest second look graded on a curve**: it went
      charcoal + brass + serif and believed that *left* the centroid, used the weak logo test
      ("would it pass as a barbershop?" → yes) and shipped — while two humans read the output as
      "muita cara de IA" instantly. Fixes: named the **dark-luxury / material centroid** as a
      third live AI look (so going dark/material is not mistaken for an escape); made the **logo
      test the cross-genre swap** (whiskey/tailor/steakhouse), retiring the within-genre false
      pass; turned the second look into an **audit** (run the full reflex-flag list against your
      own output, no spot-checking) that names the centroid it landed on, catches **origin
      asserted-vs-shown**, and forbids grading on a curve; required the reference pass to reach
      the **individual brand** (and to flag input-starvation when there's no real material).
      Edited `deviation.md`, `SKILL.md`, added the barbershop self-critique anti-pattern to
      `session-transcripts.md`. VERSION/plugin.json → 0.2.2.
- [x] **v0.2.3 — grounded the escape in evidence (research→product, 2026-07-17).** Two more
      barbershop outputs (dark-luxury "Ofício", bold-retro "Régua") proved the skill was rotating
      through *skins* on the *same skeleton* — the AI look is concrete visual repetition (a small
      shared pool of fonts/colors/tics + one hero skeleton). Mined EXP-0001 (23 excellent real
      interfaces) + EXP-0002 (the generated one) into `references/authored-vs-ai.md`: the counted
      contrast (Inter in only 2/23; bespoke or plain-system type dominates; gradients/glow/glass
      ≤1/23 each; pronounced shadows 0/23; sharp corners ≥8/23; chroma delegated to content, not
      chrome) and the deepest finding — **signature is a structural idea (a stance toward
      convention), not a skin.** MSCHF stays unmistakable with one font, two colors, no images.
      Wired "structural idea before skin, then default away from the pool" into SKILL.md (loop
      step 3) and deviation.md. VERSION/plugin.json → 0.2.3.
- [ ] NEXT: a runnable eval proving "create a front" feels different from a normal prompt, and
      that it survives the *cross-genre* logo test — `claude plugin eval` with a no-plugin baseline arm.
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
