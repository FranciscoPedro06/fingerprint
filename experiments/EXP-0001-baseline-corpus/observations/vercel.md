# Observation Record — vercel

> Instrument version: v0.2 (two-layer)

## Metadata

- **URL:** https://vercel.com
- **Date observed:** 2026-07-15
- **Category / stratum:** SaaS / dev tools (hosting/infrastructure)
- **Company:** Vercel
- **Platform/surface:** marketing site
- **Viewport:** 1280×800 desktop (headless capture; full-page at 1280×4800)
- **Screenshots:** `screenshots/vercel/` (01 hero, 02 full page)

## Layer 1 — Objective Observations

### Typography
- Typefaces: **GeistSans** (sans) for headings/UI; **Geist Mono** for annotation text — confirmed via computed styles. Both are Vercel's own typefaces.
- H1: 64px, weight 400, letter-spacing **−3.84px** (−6% of em — pronounced negative tracking). Nav/buttons: 14px, weight 400.
- Hero annotation block set in Geist Mono 16px, all-caps, gray ("FOR CODING AGENTS / TO SHIP APPS AND AGENTS / AUTOMATED BY AGENTS").
- Feature lists in section columns also all-caps mono ("DURABLE ORCHESTRATION", "GLOBAL DELIVERY").
- Case usage: sentence case for headings; ALL-CAPS reserved for mono annotation channel.

### Color
- Principal colors: **3, all neutral** — pure black background `rgb(0,0,0)`, off-white text `rgb(237,237,237)`, mid gray `rgb(161,161,161)`. **No chromatic hue observed anywhere in captured regions** (logos included — logo wall rendered monochrome white).
- Background treatment: solid pure black throughout.
- Accent usage: none chromatic; emphasis via white fills (primary buttons) and luminance.
- Contrast character: light-on-dark; high contrast for H1/CTAs, reduced for annotations and embedded imagery.

### Depth & effects
- Gradients: none observed at page level.
- Shadows: not observed as separation mechanism.
- Blur/glassmorphism: not observed.
- **Glow: present** — the hero triangle logo is rendered black-on-black with a white rim/backlight glow; a subtle radial light also silhouettes it.
- Embedded product screenshots (Notion AI chat, Zapier site, Mintlify docs) rendered dimmed/desaturated inside dark frames.

### Shape & borders
- Corner radius: pill (fully rounded) on hero CTAs ("Deploy Now" white fill, "Talk to Sales" outlined); small radius on nav buttons ("Get a Demo", "Log In", "Sign Up") and cards.
- Border usage: hairline dark-gray borders on secondary buttons, cards, and screenshot frames.

### Space & density
- Whitespace: very large empty bands — hero content occupies a narrow horizontal strip in an otherwise empty viewport; near-viewport-height gaps between sections (02).
- Visual density: sparse — first viewport: nav + 2-word H1 + 2 CTAs + centered triangle + 3-line mono annotation + logo wall (7 logos) at fold.

### Layout & components
- Layout: hero is a **three-part horizontal composition** (left H1+CTAs, center glowing triangle, right mono annotation); sections alternate heading side vs. screenshot side; closing "Recently shipped" 2-column card grid.
- Cards: present — dark cards with hairline borders (Passport, Containers), one containing a terminal/CLI mockup.
- Component patterns: top nav (4 items + 3 buttons), pill CTAs, monochrome logo wall, dimmed embedded product screenshots, all-caps mono feature lists, terminal mockup.
- Navigation: single top bar; no sidebar.

### Motion
- Not directly captured; hero renders fully in early headless frame (no long-running intro animation blocking paint, unlike `linear`).

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
Ordering carried by **luminance on a strictly neutral scale** (anchor: 3 neutral colors, zero chroma): brightest mass is the triangle's glow, then H1 white, then gray annotations, then dimmed screenshots. Reading chain in hero: glow (center) → H1 (left) → white CTA. A second channel exists: **typeface switching** (sans = statement, mono = annotation) orders content by register, not just size — mono all-caps consistently marks metadata/features across the page.

### Refinement distribution
Rendering refinement concentrates on a single object: the glowing triangle (rim light, radial falloff). Everything else is deliberately flat: solid black, unornamented type, hairline borders. Embedded product screenshots carry their own internal density but are dimmed. Distribution: one refined centerpiece → flat field → dimmed borrowed imagery.

### Density rhythm
Very long sparse bands punctuated by dense embedded screenshots (02): empty black gap → hero strip → logo band → gap → heading+screenshot pair → gap → repeat. The empty gaps are larger relative to content than in `linear` or `stripe` (same-viewport comparison of full-page captures).

### Predictability
Approximately **3 distinct section schemas**: (a) tripartite hero; (b) alternating heading-beside-dimmed-screenshot; (c) card grid. Schema (b) repeats with sides mirrored; given one section, the next is largely anticipatable with side alternation as the only variation.

### Intentional asymmetry
The hero's tripartite composition places unequal masses (text block left, icon center, small mono block right-offset) rather than centering; section screenshots alternate left/right across the scroll. Recurs consistently.

### Design risk
- Genre convention: SaaS marketing uses at least one chromatic accent for CTAs. This interface is **entirely achromatic** in captured regions.
- Genre convention: hero brand marks are rendered at full visibility. Here the logo is **black-on-black, visible only via rim glow**.
- Genre convention: monospace is reserved for code samples. Here **mono is a primary annotation channel** for marketing copy.
- Genre convention (within this corpus's stratum): display tracking around −1 to −2%. Here −6%.

### Perceived signature
The observer perceived attribution-carrying elements in: the pure-black field with glowing triangle; Geist sans/mono register system with all-caps mono annotations; total absence of chroma; pill CTAs in white. The observer perceived that the mono annotation block alone (all-caps gray on black) would be attributable within the dev-tools genre without the logo.

## Recurrence notes (cross-corpus, filled during analysis only)

_Deferred to analysis stage._

## 🟡 Hypotheses (single-site stage — recorded, not counted)

- 🟡 "We observed that all three SaaS-stratum sites dim their own embedded product imagery below the luminance of marketing copy."
- 🟡 "We observed that all three SaaS-stratum sites carry text hierarchy primarily by neutral luminance steps rather than by hue or weight."
- 🟡 "We observed negative display tracking in all three SaaS-stratum sites (−1.4px, −0.86px, −3.84px at 43–64px sizes)."
