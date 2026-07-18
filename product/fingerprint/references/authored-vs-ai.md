# What "authored" actually looks like — evidence from 23 excellent interfaces

This is not opinion or taste. The research pillar observed **23 real, excellent, un-generic
interfaces** (Aesop, Stripe, Linear, Nothing, Teenage Engineering, MSCHF, McMaster-Carr, Hacker
News, gov.uk, The Pudding, Vercel, Figma, NYTimes, Wikipedia, Obsidian, Cargo, Poolsuite…) and
one AI-generated one, dimension by dimension, with counts. The contrast is concrete. Use it as
the **target**, replacing the abstract "avoid the centroid."

> Epistemic status: single observer, n=23, `🟡` hypotheses not conclusions (EXP-0001). Cite it
> as strong evidence and direction, not law. But the direction is consistent and sharp.

> **Read this as tells to avoid, not a vow of austerity.** "Gradient/glow/glass ≤1/23", "sharp
> corners dominant", "neutral chrome" describe the *reflexes* excellent work skips — they do **not**
> mean beautiful = bare. The same corpus is often warm, elegant, richly typeset, even ornamented
> (Aesop's cream editorial, The Pudding's 12-hue tiles). Excellent interfaces reach beauty through
> type, color, composition, photography, and craft — not through the AI effect-stack. The target is
> **beautiful _and_ un-AI**; escaping into cold/austere/ugly is its own failure.

---

## The finding that matters most: signature is STRUCTURAL, not a skin

Across the corpus, identity is carried by a **stance toward convention — a structural idea —
not by a style.** The evidence is almost violent on this point:

- **MSCHF** keeps a maximally attributable identity with **one** mono typeface, **two** colors
  (gray on black), **zero** images, and **one** row schema repeated ~88 times. A three-row crop
  is instantly recognizable — carried by *none* of the materials (color, imagery, layout
  variation) we normally call "style." Its identity is the **simultaneous refusal of every
  genre convention.**
- **Teenage Engineering**'s identity *is* **density contrast** — the widest swing in the corpus,
  a dense engineering spec-sheet header against product photography where one object owns a whole
  empty viewport. The interface is *deliberately under-designed* (weight-100 lowercase
  everything, including the wordmark) so the hardware carries it.
- **Hacker News, Cargo, gov.uk** — identity through constraint, refusal, or a codified system.
  **Poolsuite** — transplant a whole other era/medium. **Wikipedia** — link-density texture.
  **rauno.me** — substitute a horizontal axis for the expected vertical.

Eleven distinct signature mechanisms were catalogued, and **most are relational or structural**
(how the thing stands toward its genre's conventions), invisible to attribute-level questions
like "which font, which color."

**The lesson for us, stated plainly:** the barbershops failed here. *Ofício* (dark-luxury) and
*Régua* (bold-retro) look opposite but share one skeleton — eyebrow → giant headline → two
buttons → image plate — **repainted.** They have *skins*, not *structural ideas*. That is
exactly why both read as AI. **You do not escape the AI look by repainting the skeleton. You
escape it by having a structural idea about what this interface even is.** The skin is
downstream of the idea; a skin with no idea is an AI page in a costume.

---

## The attribute evidence: excellence does nearly the OPPOSITE of the AI defaults

| Dimension | AI default (what to leave) | What the 23 excellent interfaces do (counts) |
|---|---|---|
| **Typeface** | Inter / Geist / Satoshi + the trendy display pool (Fraunces, Playfair, Space Grotesk, Clash, Archivo, Anton…) | **Inter in only 2/23.** Bespoke/commissioned faces **≥8/23** (Nothing *Ndot*, TE *te-20*, Cargo *Diatype*, MSCHF mono, Vercel *Geist*, gov.uk *Transport*). Deliberately-plain **system** faces **4/23** (HN *Verdana*, McMaster *Arial*, Wikipedia generic, Obsidian ui-sans). → **source type from outside the pool:** either commissioned-and-brand-tied, or a plain system font used with conviction. Almost never the trendy display face. |
| **Weight** | 400 / 700 / 800 | **Off-default weights** 100/300/330 (TE **100**, Nothing **100**, Stripe **300**, Figma **330**). → a weight the pool never reaches for. |
| **Type discipline** | 2–3 sizes, one accent word colored | **Single-typeface pages 7/23** across 5 strata; TE = one face at one extreme weight. → often **one face**, held with discipline. |
| **Where color lives** | In the *chrome*, as decoration (indigo button, gradient headline word, accent tiles) | **Achromatic chrome 6/23**; **chroma delegated to the content 8/23 — the corpus's most recurrent color structure**; single-accent-**as-action-only** 6/23 (color marks interactivity, never decorates). Aesop: *no* chromatic accent at all. → **neutral chrome; color lives in the content (photography, work) or marks an action** — it never decorates the frame. |
| **Effects** | Gradients (7 uses in the one AI sample), glow, glassmorphism, soft shadows on everything | **Gradient-as-brand 1/23. Glow 1/23. Glassmorphism 1/23. Pronounced shadows 0/23.** The entire AI effect stack is nearly *absent* from excellence. Depth, when present, is **photographic** (TE studio lighting), not CSS. → **strip the effects.** |
| **Corners** | 8–12px radius, pill buttons | **Zero-radius pages ≥8/23**; pills only 3/23. → **sharp** is the excellent default, not the exception. |
| **Refinement** | Uniform — every card the same treatment | **Concentrated / bimodal** (TE: extreme refinement on the product photography, interface deliberately plain around it). → **concentrate polish on the one real thing; leave the rest deliberately plain.** |
| **Composition** | Centered, symmetric grids | **Asymmetry as a system** (TE: tiny captions anchored to huge masses), **density contrast** as identity. → asymmetry and density swing on purpose, not centered-by-default. |
| **What the signature attaches to** | A *category* ("a premium barbershop," "a SaaS landing") | A **stance / structural idea** attributable to *this* one. |

---

## How to use this when building

1. **Pick the structural idea first.** Before any color or font: what *is* this interface,
   structurally? What is its stance toward the genre's conventions — which one does it refuse,
   transplant, invert, or push to an extreme? (For a barbershop: is the whole page the price
   board? the appointment book? one continuous pole? the actual day's queue? a single
   photograph of the room?) The idea is the thing a cropped fragment would be attributable to.
2. **Let the attributes fall out of the idea, defaulting *away* from the pool** per the table:
   type from outside the trendy set (or plain system), a weight the pool skips, neutral chrome
   with color in the content or on actions only, no gradient/glow/glass/soft-shadow, sharp
   corners, refinement concentrated on the real content.
3. **Test:** if you can describe your design as a *skin* ("dark and material," "bold and retro")
   but not as a *structural idea*, you have not left the centroid — you have repainted it. A skin
   with no idea is the failure; an idea can survive even with plain materials (MSCHF proves it).
