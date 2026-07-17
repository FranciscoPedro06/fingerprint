# Observation Record — bruno-simon

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://bruno-simon.com
- **Date observed:** 2026-07-15
- **Category / stratum:** Portfolios (creative developer)
- **Company:** Bruno Simon (personal)
- **Platform/surface:** portfolio (WebGL application)
- **Viewport:** 1280×800 desktop (headless; WebGL rendered via software rasterizer in tall capture)
- **Screenshots:** `screenshots/bruno-simon/` (01 pre-render gradient, 02 rendered 3D scene)
- **Capture note:** the portfolio is a single WebGL canvas (interactive driving game); static captures show the start state only. Interactive behavior not exercised in this observation.

## Layer 1 — Objective Observations

### Typography
- DOM fonts (computed): **Nunito** (rounded sans), **Amatic SC** (hand-written condensed), **Pally-Medium**. On-canvas lettering ("CLICK & START") is hand-drawn-style with a sketched arrow.
- Most "typography" is rendered inside the 3D scene, not as DOM text (26 text elements vs. one full-viewport canvas).

### Color
- Dark aubergine field with a **purple grid of × marks** (perspective floor); saturated content palette: pink/coral foliage, orange glowing ground disc with white rim light, red low-poly truck with lit amber headlights, lavender accents.
- Contrast character: dark field, high-chroma warm centerpiece.

### Depth & effects
- Real-time 3D rendering: perspective, modeled lighting, **emissive glow** (platform rim, headlights), soft gradients in the sky field. All depth is diegetic (in-scene), not UI styling.

### Shape & borders
- No UI chrome observed in the start state — no buttons, cards, or nav; the scene is the interface.
- Forms are low-poly 3D geometry (faceted trees, boxy truck).

### Space & density
- One centered composition (truck on glowing disc) surrounded by large dark emptiness with the grid texture.

### Layout & components
- Layout: a game scene: vehicle + scenic props (bench, lamp, trees) on a spotlit disc; instruction lettering beside it; 1 canvas element; 19 links in DOM (presumably in-scene or overlay menus).
- Navigation: driving the vehicle (interactive; not exercised).

### Motion
- The entire surface is an interactive real-time render; static captures underrepresent it by design.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshot `02`._

### Visual hierarchy
A theatrical spotlight structure: one glowing disc holds all content against a near-empty dark field (anchor: composition observation). Ordering: lit centerpiece → hand-drawn instruction → everything else fades into grid texture. There is no page hierarchy because there is no page — the hierarchy is staging.

### Refinement distribution
All refinement lives in the 3D scene (modeling, lighting, palette harmony); the DOM shell is invisible. The refinement register is *game art direction* rather than interface polish.

### Density rhythm
Not applicable as scroll rhythm; spatially, one dense island in a sparse field.

### Predictability
No schema; the genre expectation (portfolio = list of work) is replaced entirely by a playable environment. Within the corpus, the analogue of `poolsuite`'s strategy: adopt a different medium's conventions wholesale (here: video-game conventions).

### Intentional asymmetry
The scene composition is casually asymmetric (truck off-center, props clustered left) as staged photography would be.

### Design risk
- Portfolio-genre convention: work samples, about, contact. Here **a driving game is the entire interface**; content is discovered by playing.
- Web convention: text as primary medium. Here text is diegetic scenery.
- Accessibility/performance conventions traded against experience — the deviation is total and famous precisely for it.

### Perceived signature
The observer perceived attribution-carrying elements in: the low-poly truck on a glowing disc; hand-drawn instruction lettering; the purple ×-grid void. The observer perceived the start frame alone as attributable within the creative-dev community — the piece functions as its author's signature in the literal sense.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed a second medium-transplant record (with `poolsuite`): identity via adopting a complete foreign convention system (video game). In the portfolio stratum the transplant is single-author and playful rather than nostalgic."
