# Observation Record — obsidian

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://obsidian.md
- **Date observed:** 2026-07-15
- **Category / stratum:** Professional tools (knowledge management)
- **Company:** Obsidian (Dynalist Inc.)
- **Platform/surface:** marketing site
- **Viewport:** 1280×800 desktop (headless capture; full-page at 1280×4800)
- **Screenshots:** `screenshots/obsidian/` (01 hero, 02 full page)

## Layer 1 — Objective Observations

### Typography
- Typeface: **`ui-sans-serif` system font stack** — confirmed via computed styles. No custom webfont for headings or body; the rendered face is OS-dependent (Segoe UI family on the capture machine).
- H1: 60px, weight 600, letter-spacing −1.2px. Lede: 36px, weight 400. Nav: 14px w500; CTA label 20px w500.
- Section headings end with a **terminal period** ("Sharpen your thinking.", "Spark ideas.", "Sync securely.", "Publish instantly.").
- Hierarchy differentiated by size, weight (600 vs 400), and gray steps (`rgb(238,238,238)` vs `rgb(188,188,188)`).
- Case usage: sentence case throughout.

### Color
- Principal colors: 4 — dark charcoal background, off-white `rgb(238,238,238)`, gray `rgb(188,188,188)`, **violet accent `rgb(124,58,237)`** (primary CTA, links, toggle switches).
- Background treatment: solid dark; one light-lavender panel behind the "Shared vaults" mockup; violet-gradient 3D logo crystal as centerpiece imagery.
- Accent usage: frequent for a dark-theme site — filled CTA, text links, plugin toggles, tag chips.
- Contrast character: light-on-dark; embedded app windows shown at near-full brightness (not dimmed).

### Depth & effects
- Gradients: on the 3D logo crystal and its app-icon tile; not used on page surfaces.
- Shadows: subtle on app windows, phone mockup, and icon tile.
- Blur/glassmorphism: not observed.
- Glow: not observed.

### Shape & borders
- Corner radius: 8px on buttons (computed); medium on cards, app windows, and the lavender panel; large on the app-icon tile.
- Border usage: hairline dark borders on cards and embedded windows.

### Space & density
- Whitespace: left-aligned hero with wide right margin above the app window; moderate section gaps (smaller than `vercel`/`linear` gaps relative to content).
- Visual density: moderate — first viewport: nav (5 items + globe + 2 links) + H1 + 2-line lede + 2 CTAs + top of a full app window (sidebar with ~15 items, 2 tabs, graph pane, phone overlay).

### Layout & components
- Layout: left-aligned hero over full-width app screenshot; 2-column text-block + icon section; centered heading + **2×2 card grid** (Links, Graph, Canvas, Plugins); split sections with mockups; 3-column feature row.
- Cards: present — dark feature cards each embedding a functional UI fragment (wiki-link popover, graph view, canvas board, plugin list with toggles).
- Component patterns: top nav, filled violet CTA + violet text-link pair, real app-window screenshots (desktop + overlapping phone), plugin list rows with toggles, member-list mockup, tag chips, footnoted "Learn more." links.
- Navigation: single top bar; globe locale selector.

### Motion
- Not directly captured; page renders fully in early headless frame.

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
Ordering by size and weight on a two-step gray scale, with **violet as a strict action marker**: every violet element in the captured page is interactive (CTA, link, toggle) or brand (logo crystal) (anchor: Layer-1 accent observations). Reading chain in hero: H1 → lede → violet CTA → app window. The app screenshots sit at near-full brightness, competing with the copy rather than receding behind it.

### Refinement distribution
The single most rendered object is the 3D violet logo crystal (gradient, facets, soft shadow); page chrome is otherwise flat and system-fonted. App screenshots are shown as-is — functional density without decorative treatment. Distribution: one polished brand object → plain shell → untreated working UI.

### Density rhythm
Moderate, comparatively even cadence (02): hero text → large app window → text+icon pair → centered heading → card grid (local peak) → split mockup sections → 3-column row. No near-empty viewport-height gaps; content bands abut with regular spacing.

### Predictability
Approximately **5 distinct section schemas** in the captured page ((a) hero+window, (b) stacked text pairs + icon, (c) centered heading + 2×2 grid, (d) split heading/mockup, (e) 3-column features). Schema repetition is low; ordering of schemas does not repeat within the capture.

### Intentional asymmetry
Phone mockup overlaps the desktop window's right edge at an offset; hero text block left-aligned with empty right. Otherwise the page is predominantly rectilinear and centered — the least recurrent asymmetry among records so far (comparative observation, not valuation).

### Design risk
- Genre convention: product marketing sites load custom brand webfonts. This site sets everything in the **OS system font stack**, so its headline typography varies by visitor platform.
- Genre convention: headings without terminal punctuation. Here **every section heading ends with a period**.
- Genre convention (observed in this corpus's SaaS records): embedded product imagery dimmed below copy luminance. Here app windows are shown at near-full brightness with unstyled working content.

### Perceived signature
The observer perceived attribution-carrying elements in: the violet 3D crystal and violet-only accent discipline; period-terminated short imperative headings; unretouched app windows containing graph views; system-font plainness. The observer perceived that a cropped graph-view fragment with violet accents would be attributable within the note-taking genre without the logo.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed a site using the OS system font stack while every other record so far loads a custom or named webfont."
- 🟡 "We observed that embedded product imagery is not dimmed here, unlike all three SaaS-stratum records — the dimming behavior may be stratum-correlated rather than universal."
