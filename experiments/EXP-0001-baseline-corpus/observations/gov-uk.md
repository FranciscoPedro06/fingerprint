# Observation Record — gov-uk

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://www.gov.uk
- **Date observed:** 2026-07-15
- **Category / stratum:** Utilitarian systems (government)
- **Company:** UK Government Digital Service
- **Platform/surface:** service portal front page
- **Viewport:** 1280×800 desktop (headless capture; full page at 1280×3200)
- **Screenshots:** `screenshots/gov-uk/` (01 hero, 02 full page)
- **Capture note:** cookie banner (flat, in-flow, not overlaid) at top of captures.

## Layer 1 — Objective Observations

### Typography
- **Single typeface: GDS Transport** (the government's own face, derived from road-signage Transport) — computed; only family found.
- H1: 55px, weight 700, letter-spacing normal. Links/buttons/body: 19px — **a large uniform base size**.
- Case usage: sentence case everywhere; no all-caps channel; no italics observed.

### Color
- Flat white page; **flag-blue header band `rgb(29,112,184)`-family** with white H1; black body text; blue links `rgb(29,112,184)`; **green action buttons `rgb(0,112,60)`**; small pastel tints on three "Featured" icon tiles (pink, lavender, green).
- Contrast character: high, dark-on-light; the blue band is the only large color mass.

### Depth & effects
- None — no gradients, no shadows, no blur, no glow.

### Shape & borders
- Corner radius: **0px everywhere** (computed on buttons; visual on inputs/tiles).
- Borders: hairline gray rules between list items; thick blue section rules; square search input with square icon button.

### Space & density
- Uniform vertical rhythm of list rows; moderate density — content is lists, not cards.
- First viewport: cookie banner + blue band (logo, menu, H1, search).

### Layout & components
- Layout: single main column + narrow right rail ("Featured", app promo); content organized as **link lists with one-line descriptions** ("Benefits — Includes eligibility, appeals…"), 17 category rows, chevron affordances.
- Components: search-first band, arrow-bulleted "Popular" links, underlined blue links, green primary buttons, icon tiles.
- Navigation: "Menu" dropdown + search; the page body is itself a category index.

### Motion
- None.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
Three fixed signals do all ordering: **blue = link, green = action, black = information** (anchor: color observations), with size distinguishing H1/section/body. No luminance games, no imagery: hierarchy is a small closed vocabulary applied uniformly — closer to a signage system than to web design.

### Refinement distribution
Perfectly uniform: every row, rule, and link is styled identically; there is no hero object and no decorated zone. The refinement is in the consistency itself and in the bespoke signage typeface.

### Density rhythm
Even list pulse throughout; a single color-band beat at top (blue), then constant white list rhythm. No sparse/dense alternation.

### Predictability
Two schemas (link-list row; icon-tile rail item) with near-total repetition. Given any row, every subsequent row's anatomy is known. Among the corpus's most predictable structures — by explicit design-system mandate rather than by template economy.

### Intentional asymmetry
Main-column/rail split is the only asymmetry; within columns everything is left-aligned and uniform.

### Design risk
- Web-genre convention: rounded corners, shadows, brand personality, marketing imagery. Here **all are absent by policy** — zero radius, zero depth, zero photography on the front page.
- Genre convention: 14–16px body text. Here **19px** base.
- The deviation direction matches `nytimes` (print conventions) and `mcmaster` (catalog austerity), but here the plainness is a codified public design system.

### Perceived signature
The observer perceived attribution-carrying elements in: the flag-blue band + crown logo; GDS Transport's signage letterforms; the blue-link/green-button vocabulary; square everything. The observer perceived that a cropped list row (underlined blue 19px link + gray one-liner + hairline) would be attributable among government-service sites.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed a single-typeface page whose hierarchy is a closed three-color signal vocabulary — identity via constraint system, recognizable without any decorative element."
- 🟡 "We observed the third record (nytimes, mcmaster-carr, gov-uk) achieving distinctiveness through zero-radius/zero-depth austerity — 'radical plainness' recurs across the utilitarian strata as predicted at corpus design time."
