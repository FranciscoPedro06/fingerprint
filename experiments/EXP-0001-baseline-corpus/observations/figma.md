# Observation Record — figma

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://www.figma.com (geo-served in pt-BR; no `/en` path available)
- **Date observed:** 2026-07-15
- **Category / stratum:** Professional tools (design)
- **Company:** Figma
- **Platform/surface:** marketing site
- **Viewport:** 1280×800 desktop (headless capture; full-page at 1280×4800)
- **Screenshots:** `screenshots/figma/` (01 hero, 02 full page)
- **Validity note:** content strings in pt-BR (geo-serving; site returns 404 for `/en/`). Typography, color, layout, and component observations are locale-independent; text-length-dependent observations (line counts) may differ from the en-US rendering. Cookie banner visible in captures.

## Layer 1 — Objective Observations

### Typography
- Typeface: **figmaSans** (custom sans; variable) — confirmed via computed styles.
- H1: 56px, weight 400, letter-spacing −1.25px. Body: 18px, **weight 330** (light variable weight).
- Two-tone heading device observed: black primary sentence + gray secondary sentence within the same heading block ("Expressividade sem limites." black / subline gray).
- Case usage: sentence case throughout; no all-caps channel observed (all-caps appears only inside user-artwork imagery, e.g. "MODULAR LIVING", "VAULT").

### Color
- Principal chrome colors: 2 — white background, black text/CTAs. Secondary grays for sublines.
- **Chroma is confined to content imagery**: layered collage of user artwork (orange card, nature photography, olive-dark audio app, cobalt phone mockup, lime-tinted panel, and a masonry wall spanning magenta/cyan/lime/blue artwork).
- Background treatment: white page; two tinted panels (light green, light gray) framing product demos; masonry section is a full-bleed image wall.
- Accent usage: none in chrome — primary CTAs are solid black with white text.
- Contrast character: dark-on-light, high contrast chrome around high-chroma content.

### Depth & effects
- Gradients: not observed in chrome (gradients appear inside user artwork only, e.g. color-picker demo).
- Shadows: subtle on layered hero cards and floating tool panels.
- Blur/glassmorphism: background photograph in hero collage is blurred (depth-of-field imagery, not UI glass).
- Glow: not observed.

### Shape & borders
- Corner radius: medium-large on hero collage cards and phone mockups; small-medium on CTA buttons ("Comece agora" rounded rectangle); small floating tool panels with small radius.
- Border usage: minimal; separation via tinted panels and shadows; outlined secondary button in nav.

### Space & density
- Whitespace: hero splits left text block / right collage with moderate margins; centered headings with wide side margins; masonry wall runs edge-to-edge with zero gaps.
- Visual density: moderate in hero (nav + 6-line H1 + collage + CTA); **very dense** in masonry section (12+ artwork cells with embedded UI panels); sparse in single-phone gray band.

### Layout & components
- Layout: split hero; centered-heading sections; full-bleed media bands; **masonry/mosaic grid** of unequal cells.
- Cards: as layered, angled collage items in hero; as masonry cells in the tool-showcase wall.
- Component patterns: dropdown top nav (5 items), black filled + outlined button pair, floating mini tool-panels (Texture, Depth, Weight sliders, color picker) overlaid on artwork, phone mockups, footnoted feature links ("Explore as ferramentas →").
- Navigation: single top bar; black CTA at right.

### Motion
- Not directly captured; full-page render completed within virtual-time budget (no blocking intro animation).

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
The chrome/content split is the primary ordering mechanism: everything the company says is achromatic (black on white), everything users made is chromatic (anchor: Layer-1 color observations). Reading chain in hero: chromatic collage mass (right) → black H1 (left) → black CTA. Within text, hierarchy uses size plus the black/gray two-tone device rather than weight.

### Refinement distribution
Inverse of the SaaS-stratum records: the shell is plain (flat white, unornamented type) and the **visual richness is delegated to content imagery** — user artwork carries texture, chroma, and detail. Micro-refinement in chrome exists only in the floating tool panels (sliders, steppers) placed *inside* the artwork.

### Density rhythm
High-variance alternation (02): sparse hero → mid-density tinted panel → sparse gray band (single phone on empty field) → **density spike** (edge-to-edge masonry wall) → sparse text band. The rhythm is not a regular cadence; it builds to one dense peak.

### Predictability
Approximately **4 distinct section schemas**: (a) split hero with collage; (b) centered heading + tinted demo panel; (c) full-bleed single-object band; (d) masonry wall. Low schema repetition in the captured page; the masonry section breaks the margin system the rest of the page establishes.

### Intentional asymmetry
Hero collage layers cards at slight angles and unequal overlaps against a strictly aligned left text column; masonry cells are deliberately unequal in size. The asymmetry is confined to content zones while the chrome grid stays rectilinear — recurs consistently in both hero and masonry sections.

### Design risk
- Genre convention: design-tool marketing demonstrates the tool's own interface prominently. Here the **full product UI is nearly absent**; only fragments (mini panels) appear, embedded in user artwork.
- Genre convention: brands with chromatic logos (Figma's 4-color mark) carry accent color into CTAs. Here CTAs are **solid black**.
- Genre convention: body text at weight 400. Here body runs at **weight 330**.

### Perceived signature
The observer perceived attribution-carrying elements in: the achromatic-chrome/chromatic-content inversion; figmaSans at light body weight; floating mini tool-panels overlaid on user artwork; the angled-collage device. The observer perceived that a cropped masonry cell with an embedded slider panel would be attributable without the logo.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed that this professional-tool site places all chroma in content and none in chrome — a distribution not seen in the three SaaS-stratum records, where chroma (when present) belongs to brand artwork."
- 🟡 "We observed sub-400 body weights on a variable font — the third record in four to use an off-default variable weight (510, 300, 330)."
