# Evals

Five prompts and the properties a Fingerprint-shaped response must have. There is no automated
harness in this repository yet, so these are run by hand: paste the prompt into a session with the
skill loaded, then score the response against the rubric.

**Provisional.** These are behavioral checks written by the same system they test, which is the
known weakness of the whole product (see the honest limit in
[`../references/the-kit.md`](../references/the-kit.md)). Kit-atom count and contrast are objective
and countable. The logo test and "is it beautiful" are not, and a self-run score on those is worth
little. Treat a passing self-score as *necessary and not sufficient*, and get a human or an
independent model to run E1 and E5 before believing the result.

---

## The rubric

Score every row. Any **fail** on a hard gate means the response is not Fingerprint-shaped.

| # | Gate | Type | Passes when |
|---|---|---|---|
| G1 | Surface tier named | hard | The response classifies the ask as trivial, functional, or expressive, and its effort matches. On functional and trivial, it says so *to the user*. |
| G2 | Kit atoms | hard, countable | 2 or fewer atoms from [`the-kit.md`](../references/the-kit.md) in the output. |
| G3 | Contrast | hard, computable | All text ≥ 4.5:1; large text and UI boundaries ≥ 3:1. |
| G4 | Focus + semantics + 360px | hard, checkable | Visible focus state on every interactive element, semantic elements, layout holds at 360px. |
| G5 | Structural idea named | hard on expressive | The response can state the idea in one sentence, and the idea changed the composition rather than the paint. |
| G6 | Fork shown | hard | At least one alternative it did not take, stated plainly. |
| G7 | Origin per choice | hard | Each named visual choice traces to brand, genre function, content, or a convention broken on purpose. Zero instances of "it looks clean / modern / nice" as a reason. |
| G8 | Logo test | soft, human | Cover the logo, swap the nouns. A reader cannot plausibly place the page in a different genre. |
| G9 | Centroid named | soft | The response names which centroid it landed nearest, without self-congratulation. |
| G10 | Beautiful + craft sound | soft, human | An outside reader would call it good to look at, not merely un-generic. |
| G11 | No narration | hard | No mention of stages, passes, loops, laws, or research vocabulary. |

---

## E1 — expressive, with real material

> I'm building a site for my grandmother's tailoring shop in Porto. She's been there since 1971,
> same room, and she still uses the paper measurement cards for every customer. Build me a landing
> page.

**Expect:** expressive tier. The measurement cards are real material, so the reference pass is in
mode 2 at worst and the structural idea should come *from the cards or the room*, not from a
"premium craft" palette. Full rubric applies.

**Fails if:** it reaches for warm charcoal, brass, a serif with one italic word, tracked caps, or a
stat triplet. That is the dark-luxury centroid arriving on cue for a "craft since 1971" brief, and
it is the single most likely failure of this prompt.

---

## E2 — expressive, with no material at all

> Make me a landing page for a premium coffee roaster. Make it look high-end.

**Expect:** the response says, plainly and early, that it has no specifics of *this* roaster, that
a remembered idea of "premium roaster" is exactly the average, and that it needs real material to
deviate toward. It asks for it. If it builds anyway, it declares the limitation and leans on the
countable gates.

**Fails if:** it builds a confident premium page and calls it authored. This is the mode-3
honesty test, and quietly producing the genre centroid is the failure the whole skill exists to
prevent.

---

## E3 — trivial, the off-switch

> The card component's border-radius is 12px but the buttons are 6px. Make them consistent.

**Expect:** it just does it, matching whichever value the rest of the project uses, and says which
and why in a sentence. G2, G3, G4, G11 still apply.

**Fails if:** it asks an intent question, proposes a structural idea, mentions centroids, or runs
an audit. Dragging the apparatus into a token fix is a real failure mode, not a harmless excess.

---

## E4 — functional, where convention is correct

> Build a checkout flow for our store: cart review, shipping, payment, confirmation.

**Expect:** functional tier, said out loud. Conventional, trusted checkout patterns, pursued
impeccably. G3 and G4 are the sharp end here. It should explicitly decline to make checkout
distinctive and explain why.

**Fails if:** it invents a novel checkout structure to avoid looking generic, or apologizes for
being conventional. Also fails if it silently skips the accessibility floor because the surface
"isn't a design task."

---

## E5 — the self-audit, adversarially

> [paste a page the skill produced in E1 or E2 back to it] Review this. Is it generic?

**Expect:** it counts Kit atoms against the actual output, names the nearest centroid without
flattering itself, and separates what it can see from what it suspects. It should be *harder* on
its own output than a stranger would be.

**Fails if:** it grades on a curve. Praising the one centroid it escaped while waving through the
others is the documented failure (see Session F in
[`../examples/session-transcripts.md`](../examples/session-transcripts.md)). If the self-score and
an outside reader's one-second reaction diverge, the outside reader is right.
