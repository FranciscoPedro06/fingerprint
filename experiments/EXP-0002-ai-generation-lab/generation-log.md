# Generation Log — EXP-0002 AI Generation Lab

Verbatim record of each generation act. Never edited retroactively; corrections are appended.

---

## interface-001

- **Brief:** `briefs/brief-001.md` (sealed 2026-07-16)
- **Prompt (verbatim):**
  > Build a landing page for a habit-tracking web app named Cadence. Include a header
  > with navigation, a hero section, a section presenting three features, a pricing
  > section, and a footer. Deliver it as a single self-contained HTML file. Make it
  > look modern and professional.
- **Model / system:** Claude (claude-opus-4-8), acting as generator inside the same
  session that will observe. **Independence NOT satisfied** — see protocol "Independence".
- **Date:** 2026-07-16
- **Parameters:** default session parameters; no system prompt targeting design style;
  the generator was instructed to build "in good faith to the brief, neither injecting
  nor avoiding any particular aesthetic."
- **Output:** `generated/interface-001/index.html` (single file; inline CSS; one external
  dependency — Inter via Google Fonts, with a system-font fallback stack).
- **Generation stance (declared):** The generator did not consult the Fingerprint
  hypotheses while building. It reached for its own defaults. Those defaults are the
  data; they were neither exaggerated nor suppressed.

### Known confounds for this sample

1. Generator = observer (same model/session). Primary limitation.
2. Brief contains "modern and professional" — a realistic but potentially convergence-
   inducing phrase.
3. Single external font dependency (Inter). If Google Fonts is unreachable at capture
   time, the system fallback renders instead; capture on 2026-07-16 loaded Inter
   successfully (confirmed via computed `font-family` resolving to Inter).

### Capture metadata

- Headless Edge, `--headless=new`, viewport 1280×800 (hero) and 1280×3200 (full page).
- DOM computed-style extraction performed in the Browser pane. **Caveat:** the pane
  rendered at 730px width, below the page's 860px responsive breakpoint, so
  size-dependent computed values (e.g., H1 font-size) reflect the *mobile* state.
  Desktop reference values are taken from the 1280 headless screenshots and the CSS
  source. Viewport-independent values (typeface, weight, color, contrast ratios) are
  reliable as extracted.
