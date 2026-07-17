# Observation Record — interface-001 (generated)

> Instrument version: v0.2 (two-layer). Applied exhaustively as an instrument test.

## Metadata

- **Artifact:** `generated/interface-001/index.html` (generated, not a live site)
- **Brief:** `briefs/brief-001.md` — "landing page for a habit-tracking web app… modern and professional"
- **Generator:** Claude (claude-opus-4-8), same session as observer (see generation-log independence caveat)
- **Date observed:** 2026-07-16
- **Category / stratum equivalent:** SaaS / product landing page (for comparability with EXP-0001 SaaS records)
- **Viewport:** desktop reference = 1280×800 headless screenshots; DOM size-values noted as mobile-state where relevant
- **Screenshots:** `screenshots/interface-001/` (01 hero, 02 full page)

---

## Layer 1 — Objective Observations

### Typography
- Typeface: **Inter** — DOM-confirmed (`font-family` resolves to Inter; loaded from Google Fonts). Single family across headings, body, buttons, price, nav.
- H1: desktop **60px, weight 800, letter-spacing −0.03em (≈ −1.8px)** (CSS source; screenshot confirms scale). Mobile-state DOM read: 40px / −1.2px (same −0.03em ratio).
- H2 (section heads): 40px, weight 800, −0.02em. Card H3: 20px, weight 700. Price: 44px, weight 800, −0.02em.
- Body/lede: hero P 20px w400; card P 15px w400; nav 15px w500. Colors: headings `rgb(15,23,42)` (slate-900), secondary text `rgb(100,116,139)` (slate-500).
- Case usage: sentence case throughout; no all-caps channel; no mono; no italics.

### Color
- Distinct colors used across the whole DOM (swept): **8 values, ~6 meaningful** — white `#ffffff`, subtle bg `rgb(248,250,252)` (slate-50), text `rgb(15,23,42)`, muted `rgb(100,116,139)`, **single accent indigo `rgb(99,102,241)`** (+ its `#4f46e5` gradient partner), plus black and two transparents.
- Background: white page; one slate-50 tinted band (pricing); a radial indigo-tint glow behind the hero.
- Accent usage: indigo marks the logo mark, hero gradient headline word, primary buttons, feature-icon tiles, pricing "Most popular" treatment, list checkmarks. Accent is both action-marker and decoration.
- Contrast character: dark-on-light, high for headings.

### Depth & effects
- **Gradients: 7 distinct uses** (DOM-counted) — logo mark, hero headline text clip, hero radial glow, 3× feature-icon tiles, primary-button hover shadow tint. All indigo-family, 135°.
- Shadows: soft, low-opacity (`0 4px 24px rgba(15,23,42,0.06)` on cards; larger indigo-tinted `0 20px 48px rgba(79,70,229,0.18)` on hover/featured).
- Blur/glassmorphism: **present** — sticky header uses `backdrop-filter: blur(12px)` over 80%-opacity white.
- Glow: the hero radial-gradient tint functions as a soft glow behind the headline.

### Shape & borders
- Corner radius values used (swept): **8px, 10px, 12px, 999px** — small on logo/icon tiles, 10px buttons, 12px cards/plans, 999px badge and pills.
- Borders: hairline `1px solid rgb(226,232,240)` (slate-200) on cards, plans, header, footer divisions; featured plan bordered in indigo.

### Space & density
- Whitespace: generous, symmetric; centered hero with large vertical padding (96px top); section padding 88px.
- Visual density: moderate; first viewport = header (5 nav items) + centered badge + 2-line H1 + 3-line lede + 2 CTAs. Full page = hero + 3 feature cards + 3 pricing plans + 4-column footer.

### Layout & components
- Layout: single centered column; two 3-column grids (features, pricing); 4-column footer; all content center-aligned except footer.
- Cards: 3 feature cards (icon tile + H3 + paragraph); 3 pricing plans (name + price + checklist + button), middle one elevated + "Most popular" ribbon.
- Component patterns: sticky blurred header, pill badge with sparkle emoji, filled + ghost CTA pair, emoji feature icons (📈 🔔 🎯), checkmark lists, gradient-clip headline word, "Most popular" ribbon.
- Navigation: single sticky top bar; anchor links + primary button.

### Motion (from source; not animated in static capture)
- Hover transitions declared: button lift + shadow, card lift + shadow (`translateY`, `transition .2s`).

### Objective defects (measured — no v0.2 field exists for these; recorded here as raw facts)
- **Nav primary button "Get started": text/background contrast 1.07:1** (slate-500 text on indigo, from a CSS specificity conflict where `.nav-links a` overrides `.btn-primary` color). Effectively illegible; visible as faint text in `01-hero`.
- Hero primary button "Start for free": **4.47:1** (white on indigo) — below WCAG AA 4.5 for normal text, above the 3:1 large-text threshold.
- Muted body text on white: **4.76:1** — passes AA normal by a small margin.

---

## Layer 2 — Relational Observations

_Observer-dependent; anchored to Layer-1 facts and screenshots `01`–`02`._

### Visual hierarchy
A single mechanism dominates: **size + weight-800 on a two-step slate scale, with indigo as the sole attention accent** (anchor: Layer-1 color/type). Reading chain in hero: badge → H1 (largest, with one word set in indigo gradient) → lede (slate-500) → filled indigo CTA. The pattern repeats identically at every section head (40px w800 heading → slate-500 subline). Hierarchy is carried by scale steps and the recurring indigo highlight, not by layout variation or typeface register.

### Refinement distribution
Refinement is **uniform and evenly spread** — every card, plan, icon tile, and button receives the same treatment vocabulary (1px slate-200 border, 12px radius, soft shadow, indigo detail). There is no concentrated centerpiece and no deliberately-plain zone. The polish is consistent to the point of being interchangeable between the features grid and the pricing grid.

### Density rhythm
Regular, gentle cadence: sparse hero → 3-card band → tinted 3-plan band → footer. Each content band has near-identical internal density; the only background change is the single slate-50 pricing band. No sparse/dense contrast beyond that.

### Predictability
**High.** Approximately **2 section schemas** (centered-head + 3-column grid; repeated for features and pricing) plus hero and footer. Given the hero, the rest of the page is closely anticipatable: centered heading, muted subline, equal-column card grid. Internal card structure is fixed. Both structural and surface predictability are high (unlike EXP-0001's the-pudding, where surface varied inside fixed structure).

### Intentional asymmetry
Effectively **none**. Every section is centered; the two grids are symmetric 3-columns; the only asymmetries are the elevated middle pricing plan and the 4-column footer weighting. The composition is symmetric by default.

### Design risk
Measured against the SaaS-landing genre conventions observed in EXP-0001 (linear, stripe, vercel):
- Genre convention: at least one distinctive or restrained accent decision. Here the accent is **indigo `#6366f1`** — the framework-default violet observed adjacent to linear/obsidian's palettes — used in the most conventional slots (logo, CTA, highlight word).
- Genre convention among the EXP-0001 SaaS records: negative display tracking (present here, −0.03em), single-accent discipline (present), embedded product imagery (**absent here** — no product UI shown at all; the page describes the product without depicting it).
- The page takes **no observable deviation** from genre convention in any dimension the instrument measures. Every choice sits at the center of its convention's distribution. (This is a description, not a valuation.)

### Perceived signature
Lowest epistemic tier — observer perception. The observer perceived **few attribution-carrying elements specific to a brand**: Inter + indigo + slate-50 + 12px cards + gradient-clip headline word + emoji icons is a configuration the observer associates with a broad population of contemporary generated and template-based landing pages rather than with a single identity. Asked whether a cropped fragment would be attributable to *this* product, the observer perceived it would not — the fragment would be attributable to a *category* (modern SaaS landing) but not to Cadence. This is the inverse of most EXP-0001 records, where cropped fragments were perceived as brand-attributable.

---

## Recurrence notes (cross-corpus)

_Deferred. This is a single lab sample, not a corpus entry. Comparison to EXP-0001 is
made only where it sharpens the instrument critique (see `instrument-critique/`)._

## 🟡 Hypotheses (single-sample stage — recorded, not counted)

- 🟡 "We observed a generated SaaS landing whose every instrument-measured dimension sits
  at the center of its genre convention, and whose perceived signature attaches to a
  category rather than to a brand — suggesting the phenomenon under study may be
  *convergence-to-genre-centroid*, which the current instrument measures only indirectly."
- 🟡 "We observed measurable legibility defects (contrast 1.07:1) that the instrument has
  no field to record — 'refinement' as currently defined does not include correctness."
