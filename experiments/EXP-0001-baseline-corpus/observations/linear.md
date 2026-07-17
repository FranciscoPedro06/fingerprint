# Observation Record — linear

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://linear.app (home), https://linear.app/pricing
- **Date observed:** 2026-07-15
- **Category / stratum:** SaaS / dev tools
- **Company:** Linear
- **Platform/surface:** marketing site
- **Viewport:** 1280×800 desktop (headless capture; full-page at 1280×4800)
- **Screenshots:** `screenshots/linear/` (01 hero, 02 full page, 03 pricing)

## Layer 1 — Objective Observations

### Typography
- Typeface: **Inter Variable** (sans-serif) — confirmed via computed styles on live DOM, used for H1, body, and buttons.
- H1: 64px, weight 510 (variable-font intermediate weight), letter-spacing −1.408px (negative tracking).
- Body: 16px, weight 400, normal tracking. Button labels: 13px.
- Hierarchy differentiated by size and color (bright white headings `rgb(247,248,248)` vs. muted gray secondary text `rgb(138,143,152)`), less by weight (510 vs. 400 is a narrow span).
- Case usage: sentence case throughout, including nav and buttons. Small all-caps not observed in nav; small "FIG 0.2/0.3/0.4" labels in mono-style annotation appear in feature section.

### Color
- Approximate principal colors: 3 — near-black background `rgb(8,9,10)`, off-white text `rgb(247,248,248)`, muted gray `rgb(138,143,152)`. One accent (violet/indigo) appears sparsely (pricing toggle switches, small status icons in product screenshots).
- Background treatment: solid near-black; no page-level gradient observed on captured regions.
- Accent usage: rare; confined to interactive toggles and status indicators inside embedded product imagery. Marketing copy and CTAs carry no accent color.
- Contrast character: light-on-dark; high contrast for headings, deliberately reduced contrast for secondary text and embedded product UI (product screenshots rendered dimmer than headline copy).

### Depth & effects
- Gradients: not observed at page level in captured regions; subtle dark-on-dark vignetting around embedded product frames.
- Shadows: subtle; embedded app frames separate from background mainly via hairline borders and slight luminance shift rather than pronounced shadows.
- Blur/glassmorphism: not observed in captured regions.
- Glow: not observed in captured regions.

### Shape & borders
- Corner radius: mixed — fully rounded (pill, 9999px) on primary CTA buttons ("Sign up", "Get started"); medium radius on embedded app frames and cards.
- Border usage: hairline low-contrast borders (dark gray on near-black) delimiting cards, pricing columns, and app frames.

### Space & density
- Whitespace: large vertical bands between sections (full-page capture shows section gaps of roughly one viewport-height around the hero); hero text block occupies left half, right half empty.
- Visual density: sparse at marketing level (first viewport: nav + 2-line H1 + 2-line subcopy + 1 embedded app frame); dense inside embedded product screenshots (lists, sidebars, metadata chips).

### Layout & components
- Layout: single-column flow of full-width sections; internal two-column splits (left heading, right paragraph) in feature sections; 4-column card grid on pricing.
- Cards: present — 3 outlined feature cards with isometric line illustrations; 4 pricing columns separated by hairline rules.
- Component patterns: top nav bar (7 items + login/signup), pill CTA buttons, logo wall (8 customer logos, monochrome), pricing table with check/cross glyphs, toggle switches, numbered figure annotations ("FIG 0.2", "1.0 Intake →").
- Navigation: single top bar; no sidebar on marketing surface.

### Motion
- Hero region renders progressively (initial paint shows nav only; content appears after several seconds of animation) — captured indirectly via early screenshot showing empty hero.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`03`._

### Visual hierarchy
Ordering is carried almost entirely by **luminance steps on a single neutral scale** (anchor: three text colors in Layer 1 — 247/248/248, 138/143/152, on background 8/9/10; accent nearly absent; weight span narrow at 510 vs 400). Reading chain in hero: H1 (largest + brightest) → subcopy (same position axis, dimmed) → embedded product frame (dimmest large element). The same mechanism repeats in every section observed: bright heading, dimmed supporting text, further-dimmed imagery. Size and luminance move together; color and weight are barely used as ordering mechanisms.

### Refinement distribution
Micro-detail is **concentrated inside the embedded product frames** (status chips, hairline dividers, per-item icons — see 02, sections "Make product operations self-driving" onward) and in annotation devices ("FIG 0.2", "1.0 Intake →" numbered indexes). The page shell around them is kept plain: solid background, no page-level effects, wide empty bands. Distribution: plain outer shell → dense inner artifacts.

### Density rhythm
Full-page capture (02) shows a regular alternation: sparse text band → dense product-image band → sparse text band, with section gaps on the order of a viewport height around the hero. The cadence is consistent across the page; density peaks always coincide with embedded product imagery, never with marketing copy.

### Predictability
High schema repetition: approximately **2–3 distinct section schemas** across the captured page (a: left heading + right paragraph + product visual below; b: centered manifesto text; c: card row). Given one section, the structure of the next is largely anticipatable; variation happens inside the product imagery, not in the page schema.

### Intentional asymmetry
Hero text block occupies the left half with the right half empty (01); numbered annotations sit offset from the content they label; the heading/paragraph split places unequal masses left/right. These asymmetries recur consistently across sections (02) rather than appearing once.

### Design risk
- Genre convention: SaaS marketing CTAs use a high-chroma accent button. This interface renders primary CTAs as **white/neutral pills**, with accent color confined to toggles and status glyphs.
- Genre convention: product screenshots are displayed at full brightness as proof artifacts. This interface **dims its own product imagery below the brightness of the marketing copy** (anchor: Layer 1 contrast observation).
- Genre convention: display headings use bold weights (≥600). This interface uses an intermediate variable weight (510) with negative tracking at 64px.

### Perceived signature
The observer perceived attribution-carrying elements in: the near-black `rgb(8,9,10)` field with a single-luminance-ramp text system; Inter at intermediate weight with tight negative tracking at display size; the "FIG n.n" / numbered-index annotation device; dimmed embedded product frames with hairline borders. The observer perceived that a cropped fragment containing the annotation device plus dimmed frame would be attributable without the logo.

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed that this interface uses Inter while being widely cited as a benchmark of interface excellence." (Relevant to any future hypothesis linking Inter to AI origin — the baseline contains Inter too.)
- 🟡 "We observed that accent color occupies a very small fraction of the visible surface; hierarchy is carried by luminance steps of a single neutral scale."
