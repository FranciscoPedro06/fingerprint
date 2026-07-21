# Building off the centroid

The craft of the build path: how to make an interface whose visual language feels inevitable for
*this specific brand*, instead of landing on whatever aesthetic the current generation of tools
produces.

The four live centroids and the audit rubric live in `SKILL.md`. This file is the craft between
them: where a choice is allowed to come from, how to run the reference pass, and which moves
should trip a wire the moment you reach for them.

---

## The one rule: verifiable origin

**No visual decision may be made because it "looks nice."** Every font, color, radius, spacing
value, and layout move must trace to something checkable:

- the **brand's actual identity** (what it is, who made it, what it believes, where it comes
  from), or
- the **genre's function** (what this kind of interface has to do for the people using it), or
- the **content's real needs** (this specific text, data, imagery), or
- a **named convention you are deliberately breaking**, with the reason.

If the only justification available is "it's clean" or "it's modern" or "it looks good," it is not
a decision. It is a reflex, and reflexes are the centroid.

## Start with the structural idea, not the skin

The strongest evidence available (23 excellent real interfaces, observed dimension by dimension in
[`authored-vs-ai.md`](authored-vs-ai.md)) says identity is carried by a **stance toward
convention**, not by a style. MSCHF stays unmistakable with one font, two colors, and no images.
"Dark and material" and "bold and retro" are skins. If you can only describe your design as a
skin, you repainted the centroid rather than leaving it.

Decide the structural idea first. The attributes fall out of it, defaulting away from the pool per
that file's counted table: Inter in only 2/23, bespoke or plainly-systemic faces dominant,
gradient and glow and glassmorphism at 1/23 each, pronounced shadows at 0/23, zero-radius pages at
8/23 or more, chroma delegated to the content rather than the chrome.

Read those counts as **tells that excellent work skips, not as a vow of poverty.** The same corpus
is often warm and richly typeset. Beauty there comes from type, color, composition, photography,
and craft, and never from the AI effect stack.

## The reference pass

Run it quietly, before generating anything. Never narrate it.

1. **Identify the genre precisely.** Not "a landing page" but "a landing page for an independent
   coffee roaster," "a dashboard for warehouse logistics," "a portfolio for a structural
   engineer."
2. **Gather real references from that world.** Actual companies, institutions, and products.
   **Not** Dribbble shots, Awwwards showcases, or AI-tool galleries: those are centroids and will
   pull you back in.
3. **Find the decisions present in almost all of them.** Those are the genre's conventions, the
   things a user of this genre expects.
4. **Find the excellent ones that break those conventions**, and understand *why* the break works.
   What about that brand's identity or content made the deviation right rather than arbitrary?
5. **Build a language from principles, never by copying a reference.** You are extracting how to
   reason, not lifting a look. Copying one excellent reference relocates you onto *its* centroid.

**The pass must reach the individual brand, not stop at the genre.** Researching "what do premium
barbershops look like" and extracting the common denominator delivers you *to* the
premium-barbershop centroid, which is the exact failure. The references map the conventions to
know. The deviation has to come from *this* place: its actual room, its actual barbers, its
neighborhood, its founder's reason.

**When you cannot run it for real.** See the three modes in `SKILL.md` step 2. Without web access
and without this brand's material, a "reference pass" is you consulting your own memory, and your
memory of a genre is the centroid itself. In that state you have no fuel for deviation and no
palette choice will fake it. Say so and get the real material. An empty captioned photo plate
("main room · tungsten light") is the visible symptom of building premium-anything with no
specifics of *this* one.

## Interrogate every choice, in your head

- *Am I choosing this typeface because it belongs to **this** project, or because it is the font
  every AI reaches for?* Inter, Geist, and Satoshi should trip the wire instantly.
- *Is this color born from the brand's identity, or is it just a safe color?* Indigo is safe. So,
  now, are editorial beige and dark green.
- *Does this layout exist because it solves the problem, or because it is the hero every AI
  produces?*
- *Cover the logo and swap the nouns: could this exact page be a whiskey brand, a tailor, a
  steakhouse, a specialty roaster?* The weak version of this test ("would it pass as a real
  barbershop page?") gives a false pass, because a premium barbershop page **does** look like a
  plausible premium barbershop. Only the cross-genre swap discriminates.

## Reflex flags

The moves the current generation reaches for automatically. **None is banned.** Avoiding them on
principle would just be a new dogma. Use any of them when you can objectively justify its presence
from brand, genre, function, or content. But reaching for one must trigger "why this, here, for
them?", because by default it is a reflex.

- Inter, Geist, or Satoshi as a first-choice typeface.
- Editorial beige (`#F5F1E8` and neighbors), "soft black," editorial dark green.
- The saturated-indigo-over-cool-gray SaaS palette.
- A giant centered hero, a headline four lines tall, an isolated hero CTA.
- Large empty whitespace with no function.
- Rows of identical cards.
- Exaggerated corner radius, pill buttons everywhere.
- Gradients, glow, glassmorphism.
- Uniform soft shadows on every surface.
- Components that look lifted straight from a template.

A useful instinct: if a choice would feel at home in a v0 or Bolt or Framer AI showcase, it needs
a *stronger* justification than usual, not a weaker one.

## Spend deviation on grounded ideas, not on new styles

Authored interfaces commit hard on one or two dimensions and stay quiet on the rest, but the
commitment has to come from the brand rather than from swapping to a different fashionable style.
The danger is answering "make it less generic" with "make it editorial." A logistics tool and a
coffee roaster should not arrive at the same tasteful-minimal answer. If they do, the answer came
from you, not from them.

## The handoff

When you deliver, state briefly and in plain language what you decided, **where each decision came
from**, and what you deliberately passed on. Naming the origin is what separates this from taste
imposed: "I chose X because the brand is Y," never "I chose X because it looks good." That
paragraph is only honest if every choice in it actually has the origin it claims.
