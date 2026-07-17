# Observation Record — apple

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://www.apple.com (US storefront; region banner visible)
- **Date observed:** 2026-07-15
- **Category / stratum:** E-commerce / product (hardware)
- **Company:** Apple
- **Platform/surface:** storefront front page
- **Viewport:** 1280×800 desktop (headless capture; full-page at 1280×4800)
- **Screenshots:** `screenshots/apple/` (01 hero, 02 full page)
- **Capture note:** region-picker banner at top is transient chrome; disregard.

## Layer 1 — Objective Observations

### Typography
- Typeface: **SF Pro Text / SF Pro Display** (computed: "SF Pro Text") — Apple's system family.
- Display headlines (product names): ~56px semibold, centered ("iPhone", "MacBook Air"); one-line benefit lede below ("Now supercharged by M5."), then CTA pair. Nav 12px.
- Weight regime: semibold (600) for display; tight negative tracking at small sizes too (−0.374px at 34px, −0.12px at 12px).
- Case usage: sentence case; ledes end with **terminal periods**; product names capitalized as proper nouns; Apple logo glyph used inline in product wordmarks ( Watch,  Trade In,  Card).

### Color
- Chrome colors: white and near-white gray section fields; near-black text `rgb(29,29,31)`; **blue as the only accent** (filled "Learn more" pill + outlined "Shop/Buy" pill).
- Sections alternate white/light-gradient washes with **black bands** (MacBook Pro, iPad Pro) and photographic tiles (AirPods).
- Entertainment band: full-color streaming posters (content chroma).
- Contrast character: dark-on-light for product shelf; light-on-dark for pro-product tiles.

### Depth & effects
- Gradients: subtle cool wash behind MacBook Air/iPad Air bands; otherwise flat fields.
- Shadows: product photography contains its own studio shadows; no UI shadows.
- Blur/glass/glow: none in chrome.

### Shape & borders
- Corner radius: **pill CTAs** (fully rounded); section bands and tiles are sharp, edge-to-edge rectangles.
- Border usage: none visible; separation by band background changes only.

### Space & density
- Whitespace: generous, symmetric; each band is one centered content stack.
- Visual density: sparse per band — 3 text lines + 2 buttons + 1 product image; full page = 3 full-width bands + 6 half-width tiles + entertainment carousel.

### Layout & components
- Layout: **stacked full-width bands, all center-aligned**, then a 2-column tile grid of the same internal template at half scale, then a poster carousel.
- Cards: the promo tiles function as cards without borders (full-bleed backgrounds).
- Component patterns: identical unit repeated at two scales — product name / one-liner / CTA pair (filled + outlined pill) / product photography; top nav (11 compact items + search + bag); region banner.
- Navigation: single compact top bar, 12px labels.

### Motion
- None blocking; full render in early frame.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
One fixed chain repeated: product name (largest text) → one-line benefit → CTA pair → product photo (largest visual mass). Centered symmetry does the ordering; blue marks the only actionable elements (anchor: accent observations). Between bands, hierarchy is expressed by **band size** (full-width flagship vs. half-width tile) rather than by any typographic change — the template is scale-invariant.

### Refinement distribution
All refinement is in **product photography** (studio lighting, material rendering); chrome is reduced to typography and two pill buttons. Unlike `figma`/`blender` (community content) the refined content is the company's own manufactured object — but the shell/content delegation structure is the same.

### Density rhythm
Metronomic: full-width band, band, band → half-width tiles (doubled beat) → carousel. Each beat has near-identical internal density. No sparse/dense contrast within the shelf; the only rhythm change is the beat subdivision at the tile grid.

### Predictability
**One schema, two scales** — the highest structural predictability in the corpus so far. Given any band, the next band's structure, alignment, and CTA pattern are fully anticipatable; only the product and background treatment change.

### Intentional asymmetry
Essentially none in layout — every stack is centered. Asymmetry appears only inside photography (angled devices, off-center crops). The page is symmetric by system.

### Design risk
- E-commerce genre convention: prices, offers, and urgency near CTAs. Here **no prices** appear on the entire front page (except Trade In credit figures and Card cashback).
- Genre convention: varied section layouts to sustain interest. Here **radical template uniformity** — the same unit repeated ~9 times.
- Genre convention: multiple accent colors for merchandising. Here a single blue, used only for actions.

### Perceived signature
The observer perceived attribution-carrying elements in: centered product-noun display + one-line benefit with terminal period + filled/outlined pill CTA pair + floating studio product photo; the inline  glyph wordmarks. The observer perceived that any single band, cropped, would be attributable without the logo — the template itself is the signature.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed the most schema-uniform page in the corpus — a single repeating band template at two scales."
- 🟡 "We observed accent color used strictly as an interaction marker (blue), with all other chroma delegated to product imagery — the accent-as-action discipline also observed in `obsidian`."
- 🟡 "We observed terminal periods on short marketing ledes — also observed in `obsidian` headings."
