# Observation Record — rauno-me

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://rauno.me
- **Date observed:** 2026-07-15
- **Category / stratum:** Portfolios (interaction designer)
- **Company:** Rauno Freiberg (personal)
- **Platform/surface:** portfolio (horizontal deck)
- **Viewport:** 1280×800 desktop (headless capture; tall capture confirms horizontal — not vertical — content axis)
- **Screenshots:** `screenshots/rauno-me/` (01 hero, 02 tall capture)

## Layer 1 — Objective Observations

### Typography
- **Single custom font, named "X"** in CSS (grotesk sans) — computed; the font's identity is deliberately anonymized in the stylesheet.
- Hero biography set large (display ~54px rendered; computed sample 32px w500), black `rgb(23,23,23)` on white.
- **Staircase indentation**: successive lines alternate left margins ("Rauno Freiberg / is an Estonian / interaction / designer…"), a typographic composition rather than a text block.
- Case usage: sentence case; no caps channel.

### Color
- Light gray page field `rgb(237,237,237)`; white content card; black text; **one saturated yellow disc** overlapping the hero text; black-and-white slide peeking at right.
- Contrast character: dark-on-light with a single high-chroma geometric accent.

### Depth & effects
- None — flat shapes; the disc is a flat vector circle; no shadows/gradients/blur.

### Shape & borders
- The hero is a sharp-cornered white card on the gray field; the disc is the only curve.
- A filmstrip-style pager at top: small rectangle + row of tick marks.

### Space & density
- Very sparse: one sentence, one shape, a pager; 12 links, **0 images, 0 videos** on the landing surface.
- The tall (4800px) capture shows the same single card vertically centered — content extends **horizontally**, not vertically.

### Layout & components
- Layout: **horizontal deck/filmstrip** of full-height slides; next slide ("Devouring Details") visible at the right edge; tick-mark pager as position indicator.
- Components: slide cards, inline text links (Vercel, Devouring Details), a small crosshair mark at the disc center.
- Navigation: horizontal progression; no menu.

### Motion
- Not directly captured; the deck form implies horizontal transitions.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
A single sentence *is* the page; within it, ordering is choreographed by the staircase indents (reading order becomes a visual path) and by the yellow disc, which sits behind/over the text mass as counterweight (anchor: typography/color observations). Inline links are the only secondary level.

### Refinement distribution
Everything is invested in one composition: the type setting, the indent rhythm, the disc's placement. There is no chrome to refine; the slide is a poster.

### Density rhythm
Horizontal beat structure: one poster-slide per beat, with the next slide's edge always visible as a preview — rhythm is spatial-sequential rather than scroll-vertical. Within a slide, density is minimal.

### Predictability
One schema (full-height slide), repeated horizontally; slide interiors vary. The **axis substitution** (horizontal for vertical) breaks the genre's most basic structural assumption while keeping everything else disciplined.

### Intentional asymmetry
The staircase indents are systematic asymmetry inside the text block; the disc is off-center; the peeking next-slide unbalances the right edge deliberately (it advertises the axis).

### Design risk
- Portfolio-genre convention: vertical scroll, project grid, thumbnails. Here **horizontal filmstrip with zero images** on the landing slide — a typographic self-introduction instead of work samples.
- Convention: fonts declared by name. Here the font is **named "X"** — authorship of the typeface withheld in the code itself.

### Perceived signature
The observer perceived attribution-carrying elements in: the staircase-indented grotesk biography; the flat yellow disc with crosshair; the tick-mark pager. The observer perceived the hero slide as attributable within the design-Twitter/interaction-design community without a name — although the name is the first two words.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed axis substitution (horizontal deck replacing vertical scroll) as a portfolio deviation — a structural, not stylistic, signature mechanism."
- 🟡 "We observed a deliberately anonymized font name ('X') — metadata concealment as part of the design gesture; the instrument's DOM-confirmation step surfaces such cases."
