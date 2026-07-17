# Building off the centroid

This is the craft of the build path: how to create an interface that carries a fingerprint
instead of landing on the genre's default. It is the single most important reference when the
task is to *make* something, not just look at it.

The research finding this rests on: the "AI look" is not a set of ugly traits. It is the
**absence of deviation** — every value sits at the center of the genre's conventions, so the
result reads as "a category" ("a SaaS landing," "a dashboard") rather than as anyone's work.
Excellent interfaces are not more decorated; they have made *choices*, and those choices are
attributable to an author. Your job when building is to make real choices and keep them
coherent and legible.

---

## The three tests every deliberate choice must pass

A deviation is not "add something unusual." Unusual-for-its-own-sake is just a different
centroid (the "quirky AI" look). A choice earns its place only if it is:

1. **Deliberate** — made for a reason tied to what this interface is *for*, not to look
   different. If you can't say why, it's decoration, not authorship.
2. **Coherent** — part of one point of view, not one loud element in an otherwise average
   page. Ten scattered novelties read *more* generic, not less. One committed idea, carried
   through, reads authored.
3. **Legible** — nameable and reversible by the person. You can state it in a sentence
   ("I set the whole thing in a slab serif to make it feel like print, not software"), and
   they can keep it or kill it. A choice they can't see isn't theirs.

If a choice fails any of the three, it is not a fingerprint — it is noise.

## Know the centroid so you can leave it on purpose

You cannot deviate from a center you can't name. Before building, name — silently — what the
*most probable* version of this exact request looks like. That is your baseline, the thing you
will step off deliberately where it matters. From the corpus work, the current default centroid
for AI-generated interfaces clusters hard around:

- **Type:** one neutral geometric sans (Inter and its siblings) for everything; one or two
  weights; tight default tracking.
- **Color:** a single saturated accent (indigo/violet most of all) over a ramp of cool grays;
  roughly six values total; a gradient on the primary button or hero.
- **Depth:** soft even shadows on every card, backdrop-blur on a sticky header, medium-large
  corner radius (~12px) applied uniformly.
- **Layout:** centered hero, three feature cards, alternating left/right sections, a CTA band,
  a fat footer. Even vertical rhythm, generous even padding everywhere.
- **Copy:** abstract benefit-speak — "Effortlessly powerful," "Built for modern teams,"
  "Everything you need." Nouns without specifics.
- **Motion:** fade-and-rise on scroll, uniform easing, a hover lift on cards.

None of these is *wrong*. The problem is choosing *all* of them *by default*, so no dial was
ever touched. Naming the centroid is not a list of things to avoid — it is the map of where
"average" lives so you can decide, per dimension, whether to sit there (fine, if it's a
decision) or move.

## Where to spend deviation

You do not deviate on every axis — that is chaos, and it is its own centroid. Authored
interfaces usually commit hard on **one or two** dimensions and stay quiet on the rest. Pick
where to spend based on the intent you surfaced:

- Choose the **one idea** that expresses what this interface is for — the "if you remember one
  thing" move. A typographic voice, a structural rhythm, a color relationship, a density, a
  single motion behavior.
- Carry that idea *through* the whole thing so it reads as a system, not a sticker.
- Let the other dimensions be calm and conventional in service of it. Restraint elsewhere is
  what makes the one committed idea legible.

Deviation per dimension, as a menu (not a mandate):

- **Type** — a real typographic point of view: a serif where the genre expects sans; a
  distinctive display face paired with a plain body; unusual weight or size contrast;
  intentional tracking. Type is the fastest route from "category" to "author."
- **Color** — a relationship, not just a hue: an off-palette neutral (warm gray, ink, cream
  instead of cool gray), a restrained two-color scheme with real contrast logic, or a
  single unexpected accent used with discipline. Avoid the reflexive indigo-on-cool-gray.
- **Space & density** — most defaults are evenly, safely padded. A real density decision
  (tight and information-rich, or dramatically spacious) is a strong, cheap fingerprint.
- **Structure** — break the hero → three cards → CTA → footer template when the content wants
  a different shape. Let the *content* dictate structure instead of pouring it into the mold.
- **Copy** — specifics instead of benefit-speak. Concrete nouns, real numbers, a voice. Copy
  is where the centroid is most obvious and easiest to leave.
- **Motion & depth** — usually the place to *under*-do it. Removing the reflexive shadows,
  blur, and fade-ins is itself a deviation, and often the most tasteful one.

## Coherence beats novelty

A single committed idea, carried through consistently, always reads more authored than five
unrelated flourishes. When you build, hold the point of view in mind and ask of each element:
does this belong to the same idea? Scattered "interesting" choices are the failure mode — they
produce the "trying too hard" look, which is just the generic look wearing a costume.

## Then take the honest second look

After you build, this reference hands off to the loop's step 5. Turn the centroid map back on
your own output: where did it default anyway? Which of your choices are real and which are
reflexes you didn't catch? Name it plainly to the person. Building with intention and then
lying about how it came out is worse than never deviating — trustworthiness is the whole point.

## Legibility: the handoff that keeps it theirs

Never ship the choices silently. When you deliver, say — briefly, in plain language — what you
decided and what you deliberately passed on:

> "I made two real calls here: the whole thing is set in a slab serif so it reads like print
> rather than software, and I kept the palette to ink-on-cream with a single oxblood accent
> instead of the usual indigo. Everything else I kept conventional so those two carry. The
> obvious fork I didn't take was a cooler, more standard SaaS palette — say the word and I'll
> show you that version."

That paragraph is what converts your build from *imposition* into *their* decision. It is not
optional polish; it is the Law of Handed-Back Authorship in practice.
