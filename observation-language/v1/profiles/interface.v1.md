# Profile: interface.v1

**Scope:** Screen-based user interfaces and websites.
**Status:** Non-normative catalog of evidence dimensions. Every item is **optional** and
**additive**. This profile prompts Evidence collection only; it changes nothing in the
[grammar](../SPECIFICATION.md).

Derived from the two-layer interface instrument used in the project's first corpus
(EXP-0001) and extended with dimensions that instrument was found to miss (EXP-0002,
instrument critique 001): contrast/legibility, spacing scale, copy, external
dependencies, and motion.

---

## How to use

For each dimension below that applies, record one or more Evidence units (`E<n>`) with a
derivation method. Then proceed to Relations, Hypotheses, and Attribution as usual. Do
**not** turn these dimensions into a checklist to be "filled"; absence of a dimension is
itself admissible evidence (`present/absent`).

## Dimensions

### Typography
- Typeface(s) and classification; whether custom, licensed, system, or generic-fallback — _measured / classified_
- Size, weight, and letter-spacing per role (display, body, label) — _measured_
- Case usage; presence of a distinct label or annotation register (e.g., monospace) — _classified_

### Color
- Count of distinct colors, reported as `instances / distinct` — _counted_
- Background treatment (solid / tint / gradient / imagery) — _classified_
- Accent colors and where they occur — _measured / counted_
- Contrast ratios for text-on-background pairs (nav, hero, buttons, body) — _measured_

### Depth and effects
- Gradients: `instances / distinct` and where — _counted_
- Shadows: presence and specification — _measured_
- Blur / translucency / glass treatments — _classified_
- Glow or emissive treatments — _classified_

### Shape and spacing
- Corner-radius scale: values used and count — _measured_
- Border usage (weight, color, where) — _measured_
- Spacing scale: distinct padding/margin/gap values — _measured_

### Structure and layout
- Layout type(s) (single column / grid / split / asymmetric) — _classified_
- Component inventory (nav, cards, pricing table, forms, media, etc.) — _counted_
- Section-schema count (distinct repeated section structures) — _counted_
- Navigation type and item count — _counted_

### Language (copy)
- Verbatim of headline, subhead, primary CTA labels, section titles — _reported_
- Presence of recurring phrasings or set expressions — _classified_

### Motion
- Declared transitions/animations extracted from source; note that static capture cannot
  verify runtime behavior — _reported_

### Provenance-relevant facts
- External dependencies loaded (fonts, scripts, kits) — _reported_
- Framework or design-system signatures present in markup or assets — _classified_

### Correctness (kept separate from aesthetic evidence)
- Legibility failures (e.g., text-background contrast below a stated threshold) — _measured_
- Overflow, broken states, or non-functional controls observed — _classified_

Correctness facts are ordinary Evidence, but they are listed apart so that a later
"detail distribution" relation is never confused with whether the interface works.

## Viewport procedure

Record the viewport(s) used. When extracting computed values from a live render, the
extraction viewport MUST match the screenshot viewport, or both states MUST be recorded.
(This procedure exists because mismatched viewports produced reconciliation errors in
EXP-0002.)
