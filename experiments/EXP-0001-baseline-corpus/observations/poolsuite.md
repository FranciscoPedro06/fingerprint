# Observation Record — poolsuite

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://poolsuite.net
- **Date observed:** 2026-07-15
- **Category / stratum:** Experimental / studio (internet radio)
- **Company:** Poolsuite
- **Platform/surface:** web app (single-viewport)
- **Viewport:** 1280×800 desktop (headless capture)
- **Screenshots:** `screenshots/poolsuite/` (01 hero)

## Layer 1 — Objective Observations

### Typography
- **Four custom bitmap/pixel faces** (computed): Pixolde, Ishmeria, Everyday, ChiKareGo2 (a System-7-style face), over a ui-sans-serif fallback. Serif wordmark "POOLSUITE" in window title bar.
- All-caps pixel type for chrome labels ("BECOME A MEMBER / LOG IN", "WED 15 JUL 1997"); mixed case for player metadata.
- Type rendering is deliberately aliased (1-bit pixel edges).

### Color
- Flat **pink page field `rgb(246,213,213)`**; window interior black-and-white (dithered static noise); window chrome white with 1px black rules; mint-cyan play button; red "ON AIR" status dot.
- Contrast character: 1-bit black-on-white inside the OS pastiche, framed by pastel pink.

### Depth & effects
- Dithered noise texture fills the video window ("Mallorca92.avi", "591×455" status bar).
- Hard-edged retro window shadow; no soft shadows, no gradients, no blur, no glow.

### Shape & borders
- Corner radius: **zero everywhere**; all elements are 1px-black-bordered rectangles; beveled button styling in period style.

### Space & density
- Single-viewport composition: menu-bar strip (top corners: member link; date+clock), one central floating window (video + player + channel selector), and a 9-item labeled icon dock at bottom.
- 125 images, 41 links in DOM (icons and pixel assets); no scroll content.

### Layout & components
- Layout: **operating-system pastiche** (classic Mac System 7): title bar with close/zoom widgets, filename status bar, transport buttons (play/stop/prev/next), channel dropdown with LIVE badge, volume slider, icon dock ("Player, Newsroom, Mixtapes, Members, Events, Instagram, Vacation, Guestbook, Settings").
- The system clock renders the **current date transposed to 1997** ("WED 15 JUL 1997" on 2026-07-15).

### Motion
- Static-noise animation implied by the video window (still frame in capture).

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshot `01`._

### Visual hierarchy
The borrowed OS metaphor performs all ordering: window = content, dock = navigation, menu bar = status (anchor: component observations). Attention chain: noise-filled window (largest, highest-contrast mass) → player controls → dock icons. No typographic scale cascade exists; hierarchy is inherited from the OS grammar, not designed per-element.

### Refinement distribution
Refinement is spent on **fidelity of the pastiche**: dithering, bevels, pixel-font consistency, period-correct widgets. Nothing is polished in the contemporary sense; everything is precise in the archival sense. Uniform distribution at high fidelity.

### Density rhythm
Single-screen application — no scroll rhythm. Composition rhythm is the OS's: strip / window / dock.

### Predictability
Internally maximal (every element obeys one strict system — System 7's), externally minimal (nothing about the music-streaming genre predicts a 1997 desktop). Internal consistency and genre unpredictability dissociate.

### Intentional asymmetry
None — the metaphor is symmetric (centered window, centered dock, cornered menu items) and is followed strictly.

### Design risk
- Genre convention: streaming products use dark modern player UI, album art, chroma-rich gradients. Here a **wholesale transplantation of an alien convention system** (90s desktop OS) replaces the genre's conventions entirely — including falsifying the system date by −29 years.
- Unlike `mschf` (refusal by exhaustive list) and `cargo` (refusal by emptiness), this record replaces one convention set with another complete one.

### Perceived signature
The observer perceived attribution-carrying elements in: the pink field framing 1-bit OS chrome; pixel typefaces; the dated menu bar (1997 transposition); the "Mallorca92.avi" filename device. The observer perceived any cropped window fragment as attributable within the music-web genre.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed a third distinct signature mechanism in the experimental stratum: wholesale transplantation of a complete historical convention system (vs. mschf's exhaustive refusal and cargo's emptiness) — the stratum suggests signature can come from the *relationship to conventions* rather than from visual attributes."
