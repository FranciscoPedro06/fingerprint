# Observation Record — stripe

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://stripe.com/en-us (locale forced to en-US; site geo-redirects to pt-BR by default)
- **Date observed:** 2026-07-15
- **Category / stratum:** SaaS / dev tools (fintech infrastructure)
- **Company:** Stripe
- **Platform/surface:** marketing site
- **Viewport:** 1280×800 desktop (headless capture; full-page at 1280×4800)
- **Screenshots:** `screenshots/stripe/` (01 hero, 02 full page)
- **Capture note:** cookie-consent and locale banners visible in captures (fresh headless profile); disregard as page content.

## Layer 1 — Objective Observations

### Typography
- Typeface: **sohne-var** (Söhne, variable; sans-serif) — confirmed via computed styles; used across H1, body, buttons.
- H1 (computed on first h1): 43.2px, **weight 300** (light), letter-spacing −0.864px. Lede paragraph: 32px, weight 300, −0.64px. Button labels: 14px, weight 400.
- Computed H1 color returned `rgb(129,184,26)` on one sample — inconsistent with rendered navy; consistent with an **animated color/gradient on heading text** (recorded as instrument note, not as a page color).
- Hierarchy differentiated by size and a **two-tone color split within the same heading**: first clause dark navy, continuation slate blue `rgb(100,116,141)`.
- Case usage: sentence case throughout, including nav and CTAs.

### Color
- Principal UI colors: ~4 — white background, dark navy text (≈#0A2540), slate secondary `rgb(100,116,141)`, violet-blue interactive `rgb(83,58,253)`. Plus a **multichrome gradient family** (orange→pink→violet→blue) used as artwork.
- Background treatment: white solid page; large diagonal gradient artwork zones; one full-bleed dark photographic band ("Building the economic infrastructure for AI"); light lavender-tinted panels behind card grids.
- Accent usage: violet-blue on primary CTAs ("Get started", "Contact sales") and links; gradient family recurs inside product-card artwork (billing meter, Visa card art, dotted globe, stat-section light trails).
- Contrast character: dark-on-light overall; high contrast headings; one light-on-dark section.

### Depth & effects
- Gradients: **≥6 distinct uses** — hero diagonal ribbon, billing-card wash, issued-card artwork, dotted globe, tinted section panels, stat-section light trails.
- Shadows: subtle, on device mockups and white cards over tinted panels.
- Blur/glassmorphism: not observed in captured regions.
- Glow: not observed as UI treatment (light-trail artwork in one section is imagery, not component glow).
- Motion: hero gradient ribbon and heading color are animated (headless early-frame variance + computed-style variance).

### Shape & borders
- Corner radius: small on buttons (4px, computed); medium on cards and embedded mockups; device mockups fully rounded per hardware shape.
- Border usage: hairline light borders on secondary buttons and cards; card separation mostly via background-tint contrast rather than borders.

### Space & density
- Whitespace: hero occupies ~1 viewport with text confined to left ~60%; sections separated by generous but smaller-than-viewport gaps.
- Visual density: moderate — first viewport: nav (5 dropdown items) + metric line + 4-line H1 + 2 CTAs; logo wall (8 logos) enters at fold. Embedded product mockups are locally dense (order summaries, account tables).

### Layout & components
- Layout: single-column flow; 2- and 3-column card grids; 4-column stat row; alternating white / tinted / dark full-bleed bands; diagonal artwork crossing the top-right corner.
- Cards: present — feature cards each containing a product mockup over a gradient or tinted wash.
- Component patterns: dropdown top nav, rectangular 4px CTAs (filled violet primary + outlined secondary), logo wall, embedded device/app mockups, data-table mockup, stat tiles (135+, $1.9T, 99.999%, 200M+), full-bleed video promo band.
- Navigation: single top bar, 5 dropdown groups + Pricing; Sign in + Contact sales at right.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
Chroma is the strongest ordering mechanism: the page's highest-saturation mass (gradient ribbon) frames the top-right while text stays in a navy/slate two-step scale (anchor: Layer-1 color observations). Reading chain in hero: ribbon (chroma mass) → H1 dark-navy clause → slate continuation → violet CTA. Within text, hierarchy is carried by size plus the two-tone split rather than weight (both H1 and lede computed at weight 300).

### Refinement distribution
Micro-detail concentrates in two places: inside embedded product mockups (payment sheets, billing meters, account tables — see 02, card grid) and in the rendered gradient artwork (ribbon, card art, globe). The page shell between them is flat white with plain typography. Distribution: plain shell → two refined poles (product mockups, brand artwork).

### Density rhythm
Alternation across the scroll (02): sparse hero → dense logo band → moderate card grids (locally dense mockups) → dark full-bleed band → sparse centered stats → dense artwork band. Cadence is regular but the alternation is carried by **background changes** (white → tint → dark → tint) as much as by content density.

### Predictability
Approximately **4 distinct section schemas** in the captured page: (a) left heading + lede; (b) card grid with embedded mockups; (c) full-bleed dark media band; (d) centered stat row. More schema variety than a single repeating pattern; section backgrounds signal schema changes before content does.

### Intentional asymmetry
The diagonal gradient ribbon cuts the hero's top-right corner, unbalancing an otherwise left-aligned column layout; the diagonal motif recurs in card artwork and the issued-card section (02). Recurs consistently as a diagonal axis against a rectilinear grid.

### Design risk
- Genre convention: financial-infrastructure sites use restrained, low-chroma palettes. This interface places a **multichrome animated gradient** as its most prominent visual mass.
- Genre convention: display headings at bold weights. This interface sets display text at **weight 300** with negative tracking.
- Genre convention: one text color per heading. This interface splits a single H1 into **two colors mid-sentence**.

### Perceived signature
The observer perceived attribution-carrying elements in: the diagonal multichrome ribbon; the navy/slate two-tone heading device; Söhne light at display size; violet 4px-radius CTAs; white product mockups floating over gradient washes. The observer perceived that the ribbon alone, cropped, would be attributable without the logo.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed that display typography uses a light (300) variable weight with negative tracking — the second SaaS-stratum site whose display weight is below the bold convention." (Count properly at analysis stage.)
- 🟡 "We observed that micro-detail concentrates inside embedded product imagery while the page shell remains plain — also observed in the `linear` record."
