# Observation Record — wikipedia

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://en.wikipedia.org/wiki/Main_Page
- **Date observed:** 2026-07-15
- **Category / stratum:** Utilitarian systems (encyclopedia)
- **Company:** Wikimedia Foundation
- **Platform/surface:** encyclopedia main page (Vector 2022 skin)
- **Viewport:** 1280×800 desktop (headless capture; full page at 1280×3200)
- **Screenshots:** `screenshots/wikipedia/` (01 hero, 02 full page)
- **Capture note:** campaign banner below header is transient; disregard.

## Layer 1 — Objective Observations

### Typography
- Two-register system (computed): **generic `sans-serif` stack** for body/UI (16px w400) and **Linux Libertine serif** for the wordmark/headings register (28.8px w400). No custom brand font — generic stacks by design.
- Case usage: sentence case; small-caps "WIKIPEDIA" wordmark; italic used for conventions (player of the match notes).
- Dense inline **link coloring `rgb(51,102,204)`** throughout body text.

### Color
- Near-white page `rgb(248,249,250)`; white content panels; black text; blue links; **pastel section headers** (mint "From today's featured article", lavender-blue "In the news") with hairline borders.
- Photography as content thumbnails only.
- Contrast character: dark-on-light, high.

### Depth & effects
- None — flat panels with 1px borders; no shadows, gradients, blur, glow.

### Shape & borders
- Corner radius: essentially zero (slight 2px on some inputs); 1px gray borders delimit boxed sections.
- The page is structured as **bordered boxes** in the classic style.

### Space & density
- Dense text; tight line spacing; two-column main grid of boxed sections; right "Appearance" settings rail (text size / width / color controls exposed to the reader).
- Inline link density is very high (dozens per paragraph block).

### Layout & components
- Layout: centered welcome banner + 2-column boxed sections (featured article / in the news; did-you-know / on-this-day), each box = pastel header bar + white body.
- Components: search-first header, tabbed page chrome (Read / View source / View history), utility links (Donate/Create account/Log in), reader-controlled appearance settings.
- Navigation: hamburger + search; content itself is link-saturated.

### Motion
- None.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
Ordering by **boxes and their pastel header bars**, then by text flow; within text, blue links create a second reading layer that competes with black prose (anchor: link-density observation). No display typography exists — the largest text on the page is 28.8px. Hierarchy is organizational, not rhetorical: it classifies rather than persuades.

### Refinement distribution
Uniform and minimal; the interface invests nothing in polish anywhere. Notably, the page **hands appearance decisions to the reader** (text/width/color controls in the rail) — refinement of the reading experience is delegated to its user.

### Density rhythm
Constant high text density inside boxes; box boundaries provide the only punctuation. No sparse regions.

### Predictability
One repeated schema (pastel-headed box) fills the page; internals are prose+links throughout. Highly predictable structure; content (like `the-pudding`'s tiles) varies daily within fixed frames.

### Intentional asymmetry
None structural — symmetric two-column boxes; asymmetry only in content lengths.

### Design risk
- Web-genre convention: brand webfonts, depth, marketing voice. Here **generic font stacks** (deliberately unspecified — the reader's OS decides), zero depth, and an interface that exposes its own configurability instead of an identity.
- Genre convention: minimize visible links to reduce noise. Here maximal inline linking is the core interaction.

### Perceived signature
The observer perceived attribution-carrying elements in: the boxed pastel-header layout; serif small-caps wordmark over generic sans body; the saturated blue link mesh in dense prose. The observer perceived a cropped paragraph with its link mesh alone would be attributable — the signature lives in a *textual texture* rather than in any styled component.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed a second record (with `obsidian`) that does not specify its own typeface — but here even the fallback is generic (`sans-serif`), making typographic non-choice part of the system's neutrality."
- 🟡 "We observed signature carried by link-density texture — a mechanism distinct from typeface, palette, or layout, not previously catalogued in this corpus."
