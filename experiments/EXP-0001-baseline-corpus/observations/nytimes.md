# Observation Record — nytimes

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://www.nytimes.com (US edition served)
- **Date observed:** 2026-07-15
- **Category / stratum:** Editorial (news)
- **Company:** The New York Times
- **Platform/surface:** publication front page
- **Viewport:** 1280×800 desktop (headless capture; full-page at 1280×4800)
- **Screenshots:** `screenshots/nytimes/` (01 hero, 02 full page)
- **Validity notes:** DOM extraction unavailable (domain blocked in the observation browser) — typography recorded by visual classification only, without computed-style confirmation. A pt-BR consent modal and an empty ad slot are visible in captures; disregard as page content.

## Layer 1 — Objective Observations

### Typography
- **Register system of at least three faces** (visual classification; not DOM-confirmed): blackletter masthead; serif display for headlines and summaries (consistent with the Times' known Cheltenham/Imperial system); sans-serif for section labels, kickers, and utility UI.
- Headlines in **title case**; section kickers and labels in **all-caps sans** ("U.S.", "WAR IN THE MIDDLE EAST", "THE EVENING", "OPINION" bylines).
- Many hierarchy levels visible: section kicker → headline → summary → byline/read-time ("6 MIN READ"), each with distinct size/face.
- Italic serif used for opinion writer attribution.

### Color
- Chrome colors: white background, black text. Blue reserved for a small market ticker; red for "LIVE" badge.
- Chromatic content: photography throughout; data-visualization colors in embedded widgets (orange smoke-forecast map; purple/red AQI and heat-index chips).
- Background treatment: flat white; no tinted panels except utility widgets.
- Contrast character: dark-on-light, uniformly high.

### Depth & effects
- Gradients: none.
- Shadows: none observed.
- Blur/glassmorphism/glow: none.
- **Structure is drawn entirely with hairline rules**: single and double horizontal rules, vertical column dividers.

### Shape & borders
- Corner radius: **zero** — rectangles throughout, including buttons ("SUBSCRIBE FOR $0.25/WEEK", "LOG IN") and images.
- Border usage: hairline gray rules as the primary separation device across the page.

### Space & density
- Whitespace: tight but consistent gutters; no empty bands anywhere.
- Visual density: **very dense** — 30+ stories in the full-page capture; first content viewport contains ~8 headlines plus nav (12 dropdown sections + editions row).

### Layout & components
- Layout: multi-column newspaper grid — wide main well (2 columns) + narrow right rail (Opinion/Most Shared); asymmetric column widths; lead story package top-left.
- Cards: none in the web-card sense; story units are typographic blocks separated by rules.
- Component patterns: masthead + date line, dropdown section nav, briefing strip ("Catch Up on Today's Biggest Stories"), live-coverage packages, embedded interactive map with legend, weather/AQI widget tables, carousel (World Cup section with pager dots), circular headshots in opinion rail, "Got a Tip?" band.
- Navigation: horizontal section bar under masthead; editions row above.

### Motion
- None blocking; page renders complete in early frame.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
Ordering carried by **typeface-register contrast and position**, not by color or luminance (anchor: all-black text, zero accent chrome): serif display = story, caps sans = classification, size grades importance, and the lead package's top-left position outranks size in at least one case (right-rail feature headline is larger than some main-well headlines but reads as secondary). Five-plus simultaneous hierarchy levels operate without any hue.

### Refinement distribution
**Uniform micro-refinement**: rule weights, gutter widths, and typographic detail are consistent across the entire surface; no region is more polished than another. No hero object exists. Visual variation is supplied entirely by photography and embedded data graphics.

### Density rhythm
Constant high density with sectional punctuation: section-title rules ("War in the Middle East", "U.S. Immigration Crackdown", "World Cup") act as pauses inside an otherwise continuous text field. Rhythm is periodic (section bands) rather than alternating sparse/dense.

### Predictability
~6 distinct module types (lead package, headline stack, briefing strip, widget table, carousel, opinion rail). Module internals are strictly consistent; their sequence down the page varies. Predictability is high at module level, moderate at page-sequence level.

### Intentional asymmetry
Column widths are deliberately unequal (main well vs. rail); the lead package's dominance is positional; photo sizes vary by editorial weighting. The asymmetry encodes judgment about story importance and recurs as a system, not as decoration.

### Design risk
- Web-genre convention: rounded corners, shadows, and card surfaces. Here **zero radius, zero shadows** — structure by hairline rules alone.
- Web-genre convention: sans-serif display. Here serif display under a **blackletter masthead**.
- Web-genre convention: color-coded links/CTAs. Here essentially monochrome chrome with color delegated to photography and data graphics.
(The deviations replicate print-newspaper conventions on the web — recorded as deviation from the *web* genre.)

### Perceived signature
The observer perceived attribution-carrying elements in: the blackletter masthead; the serif-display/caps-sans register pair; hairline single/double rules; title-case dense headline stacks; read-time bylines in small caps sans. The observer perceived that even a cropped text-only fragment (headline + summary + rule) would be attributable without the masthead.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed hierarchy operated by typeface-register contrast with zero reliance on hue or luminance — a mechanism not present in any SaaS/tool record so far."
- 🟡 "We observed a page with zero corner radius and zero shadow — the first such record; radius/shadow presence may be genre-correlated rather than universal."
