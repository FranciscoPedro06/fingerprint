# Building off the centroid

This is the craft of the build path: how to create an interface whose visual language feels
**inevitable for that specific brand**, instead of landing on whatever aesthetic the current
generation of tools produces. It is the single most important reference when the task is to
*make* something.

The goal is **not** a "beautiful" interface. Beautiful is cheap and it is exactly what the
centroid optimizes for. The goal is a visual language every one of whose decisions has a
**verifiable origin** — so the result could not be swapped for hundreds of other current
interfaces.

**Start with the structural idea, not the skin.** The strongest evidence we have — 23 excellent
real interfaces, observed dimension by dimension in
[`authored-vs-ai.md`](authored-vs-ai.md) — is that identity is carried by a *structural stance
toward convention* (refusal, transplant, inversion, extreme density, making the page *be* the one
real thing), not by a style. MSCHF stays unmistakable with one font, two colors, and no images.
"Dark and material" or "bold and retro" are skins; if you can only describe your design as a
skin, you have repainted the centroid, not left it. Decide the structural idea first; the choices
below fall out of it, and default *away* from the pool. That reference also holds the counted
attribute contrast (Inter in only 2/23; gradients/glow/glass ≤1/23 each; chroma delegated to
content, not chrome; sharp corners dominant) — read it as the target.

---

## The AI look is a moving target

The research finding — the "AI look" is the *absence of deviation*, sitting on the genre's
convention centroid — is correct but incomplete on its own. The critical addition: **the
centroid moves.** As generators converge on a new aesthetic, that aesthetic *becomes* the new
tell. Escaping one centroid into another fashionable one is lateral movement, not authorship.

There is not one AI look. There are at least three live ones right now:

- **The SaaS-indigo centroid** (the older tell): Inter everywhere, a single saturated
  indigo/violet accent over cool grays, soft shadows on every card, a gradient hero button,
  backdrop-blur header, "Effortlessly powerful."
- **The editorial / premium-minimal centroid** (the *light* premium tell — the one that fools
  people who think they've escaped the AI look): Inter / Geist / Satoshi; an elegant serif
  display paired with a grotesk body; a giant headline; warm editorial beige (around `#F5F1E8`);
  dark green or "soft black"; heavy whitespace; pill buttons; an ultra-clean grid; a minimal
  centered hero; high-radius cards.
- **The dark-luxury / material centroid** (the *dark* premium tell — the trap that springs on
  any "premium," "craft," "lounge," "atelier," or "old-world" brief): warm charcoal / near-black;
  brass, gold, oxblood, leather, tungsten; a serif display (often with one word set in italic
  and in the accent color) plus condensed tracked-out caps; "apothecary / atelier" materiality;
  a stat triplet with hairline dividers (`40' · 1:1 · 11`); lone editorial index numbers
  (`01`) with no real system; a wordmark ending in a period; captioned photo plates that stand
  in for real photography. This is what tools produce for a barbershop, a whiskey, a tailor, a
  steakhouse, a specialty roaster — **the same page, logo swapped.**

All three are produced by Lovable, Bolt, v0, Framer AI, Relume, Webflow AI and fill current
showcases. The two premium ones are the dangerous ones, because they *feel like taste*.

**The specific trap to internalize:** escaping indigo-SaaS by going *cream-and-serif* is
changing lanes. Escaping *that* by going *dark-charcoal-and-brass* is changing lanes again on
the same highway. Going dark, going material, going "apothecary" is **not** deviation — the
dark-luxury look is a centroid with a full tank of its own. If a "premium / craft" brief makes
you reach for charcoal + brass + serif, that reach is the reflex, not the escape. Treat all
three premium defaults with *more* suspicion than the obvious SaaS one, precisely because they
feel earned.

## The one rule: verifiable origin

**No visual decision may be made because it "looks nice."** Every decision — every font, color,
radius, spacing choice, layout move — must trace to something checkable:

- the **brand's actual identity** (what it is, who made it, what it believes, where it comes
  from), or
- the **genre's function** (what this kind of interface has to do for the people who use it), or
- the **content's real needs** (this specific text, data, imagery), or
- a **named convention you are deliberately breaking**, with the reason you're breaking it.

If the only justification you can give is "it's clean" / "it's modern" / "it looks good," it is
not a decision. It is a reflex, and reflexes are the centroid. This is simply the Law of
Grounding applied to generation: you never claim (or draw) what you can't point at.

## Before you draw: the silent reference pass

Run this quietly, before generating anything. Do not narrate it.

1. **Identify the genre** precisely — not "a landing page" but "a landing page for an
   independent coffee roaster," "a dashboard for warehouse logistics," "a portfolio for a
   structural engineer."
2. **Gather dozens of _real_ references** from that world — actual companies, institutions, and
   products that live in it. **Not** Dribbble shots, Awwwards showcases, or AI-tool galleries:
   those are themselves centroids and will pull you straight back in. Real coffee roasters, real
   logistics tools, real engineering firms.
3. **Find the decisions present in almost all of them.** Those are the genre's *conventions* —
   the things a user of this genre expects.
4. **Find the excellent references that break those conventions** — the ones that are
   unmistakably themselves.
5. **Understand _why_ the breaks work** — what about the brand's identity or the content made
   that deviation right, rather than arbitrary.
6. **Build a language from principles, never by copying a reference.** You are extracting *how to
   reason*, not lifting a look. Copying one excellent reference just relocates you onto *its*
   centroid.
7. Let that language decide the type, color, structure, and density — so each falls out of the
   brand and the genre, not out of habit.

**The pass must reach the _individual brand_, not stop at the genre.** Researching "what do
premium barbershops look like" and extracting the common denominator delivers you *to* the
premium-barbershop centroid — the exact failure. The references are a map of the conventions to
know; the deviation has to come from *this* place — its actual room, its actual barbers, its
neighborhood, its founder's reason. If you have none of that — the brief was just "premium /
lounge," the gallery is empty placeholders — you have no fuel for real deviation, and no palette
choice will fake it. In that case, say so and get the real material, rather than dressing the
genre centroid in nicer clothes. An empty captioned photo plate ("main room · tungsten light")
is the visible symptom of building premium-*anything* with no actual specifics of *this* one.

## Interrogate every choice, out loud in your head

While generating, keep asking:

- *"Am I choosing this typeface because it belongs to **this** project — or because it's the
  font every AI reaches for?"* (Inter, Geist, Satoshi should trip this wire instantly.)
- *"Is this color born from the brand's identity — or is it just a safe color?"* (Indigo, and now
  editorial beige / dark green, are both "safe.")
- *"Does this layout exist because it solves the problem — or because it's the hero every AI
  produces?"*
- **The logo test — use the ruthless version.** Not *"would this pass as a real interface in
  its genre?"* (that gives a false pass — a premium barbershop page *does* look like a plausible
  premium barbershop). The real test is the **cross-genre swap:** *"cover the logo, swap the
  nouns — could this exact page be a whiskey brand, a tailor, a steakhouse, a specialty coffee
  roaster?"* If yes, it belongs to the genre's premium centroid, not to this brand. Keep
  refining.

## Reflex flags — suspect by default, allowed only with a verifiable reason

These are the moves the current generation reaches for automatically. **None is banned.** You do
not avoid them on principle — that would just be a new dogma. You may use any of them *when you
can objectively justify its presence* from brand, genre, function, or content. But the moment you
reach for one, it must trigger the question "why this, here, for them?" — because by default it's
a reflex:

- Inter / Geist / Satoshi as a first-choice typeface.
- Editorial beige (`#F5F1E8` and neighbors); "soft black"; editorial dark green.
- The saturated-indigo-over-cool-gray SaaS palette.
- A giant centered hero; a headline four lines tall; an isolated hero CTA.
- Large empty whitespace with no function.
- Rows of identical cards.
- Exaggerated corner radius; pill buttons everywhere.
- Modern gradients, glow, glassmorphism.
- Uniform soft shadows on every surface.
- Components that look lifted straight from a template.

A useful instinct: if a choice would feel at home in a v0 / Bolt / Framer AI showcase, it needs a
*stronger* justification than usual, not a weaker one.

## Spend deviation on grounded ideas, not on new styles

Authored interfaces commit hard on **one or two** dimensions and stay quiet on the rest — but the
commitment must come from the brand, not from swapping to a different fashionable style. The
danger is answering "make it less generic" with "make it editorial." Instead: what does *this
brand* make the type, the color, the density, the structure want to be? A logistics tool and a
coffee roaster should not arrive at the same "tasteful minimal" answer — if they do, the answer
came from you, not from them.

## The mandatory self-critique before delivery

This is the Honest Second Look, sharpened. It is an **audit, not a vibe-check**, and its
gravest failure mode is *grading on a curve* — congratulating yourself for the one centroid you
escaped while waving through the five you didn't. Do not do the thing where you praise the
palette as "a big bet that leaves the centroid" when the palette is itself a centroid. Before
you hand anything over, answer — plainly, to the person:

- **Run the full reflex-flag list against your _own_ output, item by item.** Not a spot-check.
  Go down the list — typeface, palette, radius, buttons, hero, stat triplets, index numbers,
  tracked-caps eyebrows, captioned photo plates, gradients/glow — and for each one you used,
  state its verifiable origin *or* admit it's a reflex you didn't catch. Catching one tell
  (the italic headline) and stopping is the failure; the stat row and the `01` plate are tells
  too.
- **Which centroid did I actually land on?** Name it honestly. "I went dark and material"
  usually means you landed on the dark-luxury centroid, not that you left it.
- **Origin: asserted vs shown.** Does the copy *claim* heritage the pixels never earn — "since
  2014," a captioned "main room" over an empty plate, "hand-forged"? Words buying authorship
  the design didn't build is a tell, not a save.
- **Which references influenced me** — and did they reach the *individual brand*, or stop at the
  genre's premium references (which just deliver the genre's premium centroid)?
- **The logo test, ruthless version:** cover the logo, swap the nouns — could this be another
  premium brand in a different genre? If yes, you're on the centroid.

If the cross-genre swap still works, or the flag-list audit turns up reflexes with no origin,
**you are not done. Iterate before delivering.** And if you lack the real material to deviate —
no photos, no room, no founder story, only "premium/lounge" — say so honestly: without this
brand's specifics there is nothing to deviate *toward*, and the result will drift to the genre
centroid no matter how nicely executed. Shipping the centroid and calling it authored is the one
unforgivable failure; congratulating yourself for it is worse.

## Legibility: the handoff that keeps it theirs

When you deliver, state — briefly, in plain language — what you decided, *where each decision came
from*, and what you deliberately passed on. Naming the origin is what separates this from taste
imposed: "I chose X because the brand is Y," not "I chose X because it looks good." That paragraph
is the Law of Handed-Back Authorship in practice, and it is only honest if every choice in it
actually has the verifiable origin it claims.
