# Observation Record — hacker-news

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://news.ycombinator.com
- **Date observed:** 2026-07-15
- **Category / stratum:** Utilitarian systems (community forum)
- **Company:** Y Combinator
- **Platform/surface:** forum front page
- **Viewport:** 1280×800 desktop (headless capture)
- **Screenshots:** `screenshots/hacker-news/` (01 hero; 02 partial)

## Layer 1 — Objective Observations

### Typography
- **Single typeface: Verdana** (system web-safe sans, unchanged since 2007) — computed.
- Two sizes only: story titles **13.33px** black; metadata **9.33px** gray `rgb(130,130,130)`.
- Case usage: sentence case; no styling variation beyond the two-size/two-color pair.

### Color
- **Orange header bar `rgb(255,102,0)`**; beige content field `rgb(246,246,239)`; black titles; gray metadata; domain names in parenthetical gray.
- No other color. Links unstyled (black, no underline).

### Depth & effects
- None. Flat table layout.

### Shape & borders
- No radii, no borders, no buttons on the front page; upvote affordance is a small gray triangle glyph.

### Space & density
- **30 ranked story rows** in one viewport-and-a-half; two-line rows (title; metadata) with minimal padding; the right half of the page is empty beyond text width.
- Header is a single 20px-tall strip containing the entire nav ("new | past | comments | ask | show | jobs | submit").

### Layout & components
- Layout: numbered single-column list, table-based; rank numerals, triangle votes, title+domain, metadata line with pipe-separated actions ("hide | 183 comments").
- Components: exactly these; nothing else exists on the page.
- Navigation: pipe-separated text links in the orange strip.

### Motion
- None.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshot `01`._

### Visual hierarchy
Two levels total (title vs. metadata), expressed by ~4px of size and one gray step (anchor: typography observations). Rank ordering — the page's real hierarchy — is expressed **numerically** (1., 2., 3.), not visually: importance is data, not styling.

### Refinement distribution
None anywhere, uniformly. The single designed gesture on the page is the orange strip.

### Density rhythm
Constant two-line pulse × 30; no interruptions of any kind.

### Predictability
One schema, 30 identical repetitions, unchanged (publicly) for ~18 years. Maximal structural and temporal predictability.

### Intentional asymmetry
The content column is left-anchored with the right side of wide viewports left empty — the layout ignores modern screens rather than adapting to them.

### Design risk
- Web-genre convention: responsive layouts, styled links, engagement affordances. Here a fixed-width table with unstyled links and 9px metadata.
- The risk is **refusing 18 years of genre evolution**; the deviation grows each year the page does not change while the genre does.

### Perceived signature
The observer perceived attribution-carrying elements in: the orange strip; beige field; Verdana two-size text texture; pipe-separated nav. The observer perceived a cropped pair of rows as instantly attributable — like `mschf` and `cargo`, the signature is carried by an extreme, consistently-held constraint set rather than by styling.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed a page whose ranking hierarchy is numeric rather than visual — hierarchy as data instead of styling; not observed elsewhere in the corpus."
- 🟡 "We observed that temporal constancy (an unchanged design while its genre evolves) functions as a signature mechanism — suggesting signature has a time dimension the instrument does not yet capture."
