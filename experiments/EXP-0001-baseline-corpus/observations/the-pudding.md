# Observation Record — the-pudding

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://pudding.cool
- **Date observed:** 2026-07-15
- **Category / stratum:** Editorial (visual essays / data journalism)
- **Company:** The Pudding
- **Platform/surface:** publication front page
- **Viewport:** 1280×800 desktop (headless capture; full-page at 1280×4800)
- **Screenshots:** `screenshots/the-pudding/` (01 hero, 02 full page)

## Layer 1 — Objective Observations

### Typography
- **Three typefaces** (computed): **Gooper SemiCondensed** (display serif, story headlines), **Atlas Grotesk** (body/UI), **Atlas Typewriter** (mono — metadata labels).
- Story headlines: 32px, weight 500, −0.8px, set in **all lowercase** ("ethical nba champions", "lawn mowing game").
- Metadata channel in typewriter mono + all-caps/numeric: issue numbers ("#223") and dates ("JUN 2026") on every tile.
- Masthead is a **hand-lettered script logo**; nav rendered as sticker-style badges ("ABOUT", "SUBSCRIBE", "MORE") with irregular hand-drawn outlines.
- Case usage: lowercase headlines; caps confined to mono metadata and sticker badges.

### Color
- Chrome: dark gray `rgb(25,25,25)` background, off-white `rgb(239,239,239)` text.
- **Per-story flat color fields**: each tile has its own saturated background (orange, grass green, cream, cobalt, magenta, lavender, teal, chartreuse, yellow, crimson…) — **>12 distinct hues on one page**.
- Accent usage: no single brand accent; hue belongs to stories, not chrome.
- Contrast character: light-on-dark chrome framing high-chroma flat tiles.

### Depth & effects
- Gradients: none in chrome; none dominant in tiles (flat fields).
- Shadows: minimal; tiles sit flat on the dark field.
- Blur/glassmorphism/glow: not observed.

### Shape & borders
- Corner radius: none observed on tiles (sharp rectangles); rounded only on the search input and issue-number chips.
- Border usage: white keyline on issue chips; tiles borderless.

### Space & density
- Whitespace: uniform gutters in a strict 3-column grid; no viewport-height empty bands.
- Visual density: dense — 21+ story tiles in the full-page capture, each with image, headline, and description; nav row of 6 icon items plus search.

### Layout & components
- Layout: strict 3-column tile grid, feed-style, interrupted twice by in-grid editorial inserts (newsletter block with illustrated envelope character + human-verification quiz; staff-pick block with photo and typewriter-styled name).
- Cards: the dominant unit — flat color field + custom artwork + lowercase serif headline + one-line description + mono metadata.
- Component patterns: hand-drawn icon nav (hearts, lightning, film camera doodles), sticker badges, search input, numbered issue chips.
- Navigation: masthead row + icon nav row; no conventional menu bar.

### Motion
- Not observed in captures.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
Global hierarchy is deliberately **flat**: every story tile has equal size and identical internal structure (anchor: grid observation), so no story outranks another; attention order within the page is driven by tile chroma against the dark chrome. Within a tile the chain is: color field/artwork → lowercase serif headline → gray description → mono metadata. Chrome (nav, search) is visually quieter than every content tile.

### Refinement distribution
All refinement lives inside tile artwork — each tile is a distinct hand-made visual system (pixel game, archival scan, data viz, collage). The chrome is plain dark with typewriter labels and doodle icons whose looseness is itself consistent. Distribution: uniform plain chrome → 21 heterogeneous refined interiors.

### Density rhythm
Uniform feed rhythm: identical tile rows repeat with constant gutters; the only rhythm breaks are the two in-grid inserts, which occupy tile slots rather than full-width bands. No sparse/dense alternation — density is constant and moderate-high.

### Predictability
**One dominant section schema** (story tile) with very high structural repetition — and simultaneously minimal *visual* repetition inside tiles (each tile's palette and style is unique). Structural predictability high; surface predictability low. The two dimensions separate cleanly in this record.

### Intentional asymmetry
The grid is strict and symmetric; asymmetry is content-internal (hand-drawn badges with irregular outlines, tilted artwork inside tiles) and in the irregular placement of the two grid-breaking inserts.

### Design risk
- Genre convention: publication headlines in title/sentence case. Here **all headlines are lowercase**.
- Genre convention: digital publications converge on 1–2 brand colors. Here **no chrome accent exists** and hue is assigned per story.
- Genre convention: mastheads set in typographic wordmarks. Here a hand-lettered script with sticker-badge nav.

### Perceived signature
The observer perceived attribution-carrying elements in: lowercase Gooper serif headlines on dark chrome; typewriter-mono issue numbering; hand-drawn sticker/doodle chrome; the per-story flat color field system. The observer perceived that a single tile (flat color + lowercase serif + "#nnn MON YYYY" mono label) would be attributable without the masthead.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed a second record using monospace as a metadata register distinct from display/body registers (also `vercel`) — in both, mono marks annotation, not code."
- 🟡 "We observed structural predictability and surface unpredictability coexisting — the record separates 'layout schema repetition' from 'visual repetition', suggesting the instrument should count them independently."
