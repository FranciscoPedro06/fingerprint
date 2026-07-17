# EXP-0001 — Cross-Corpus Recurrence Notes

> Status: 🟡 Experimental — every item below is an observation or a hypothesis, never a conclusion.
> Corpus: 23 sites, 8 strata. 21 complete records; 2 partial (aesop, mcmaster-carr — DOM/text only, visual re-capture pending).
> Single observer (AI system). No inter-observer reliability. Counts are of *records*, not of ground truth; DOM-confirmed facts are marked (D), visually-classified facts (V).

## 1. Typography

- **Sans-serif is the primary voice in 20 of 23 records.** The 3 serif-led records are all in the editorial stratum (the-pudding, nytimes, its-nice-that) — serif-as-voice appears fully stratum-correlated in this corpus. (D/V)
- **Inter appears in 2 of 23 records** (linear: Inter Variable w510 −1.4px; blender: Inter w800, normal tracking) — the same typeface in configurations so different that no shared "look" observation survives at the settings level. (D)
- **Single-typeface pages: 7 of 23** (mschf, cargo, gov-uk, hacker-news, joshwcomeau, teenage-engineering, rauno-me) — across 5 different strata, coexisting with austerity (gov-uk) and whimsy (joshwcomeau). (D)
- **System/web-safe/generic stacks: 4 of 23** (obsidian ui-sans-serif; wikipedia generic sans-serif; hacker-news Verdana; mcmaster-carr Arial). (D)
- **Bespoke/commissioned faces: ≥8 of 23** (vercel Geist, figma figmaSans, gov-uk GDS Transport, teenage-engineering te-20, nothing Ndot/NType82, cargo CargoDiatype, poolsuite pixel set, mschf MSCHFSansMono). (D)
- **Negative display tracking: 8 records DOM-confirmed** (linear −1.408, stripe −0.864, vercel −3.84, figma −1.25, obsidian −1.2, apple −0.374, cargo −0.81, the-pudding −0.8). Normal-or-positive tracking: ≥9 records, including one positive (its-nice-that +0.09). (D)
- **Off-default variable weights (neither 400 nor 700) on display/body: 5 records** (linear 510, stripe 300, figma 330, teenage-engineering 100, nothing 100). (D)
- **Monospace as a non-code annotation register: 4 records** (vercel, the-pudding, nothing, mschf-as-total). (D)
- **Terminal periods on headings/ledes: 3 records** (obsidian, apple, blender-partial). (V)

## 2. Color

- **Dark-base (light-on-dark) chrome: 8 of 23**; light-base: 15, of which **6 are non-pure-white** (aesop cream, hacker-news beige, poolsuite pink, rauno-me gray, wikipedia off-white, nothing gray). (D)
- **Achromatic chrome (no accent hue in interface elements): 6 records** (vercel, figma, its-nice-that, nytimes, aesop, cargo). (D/V)
- **Single-accent-as-action discipline (one hue, marking interactivity only): 6 records** (obsidian violet, apple blue, gov-uk blue/green closed vocabulary, teenage-engineering orange, joshwcomeau pink, hacker-news orange-header). (D/V)
- **Chroma delegated to content while chrome stays neutral: 8 strong cases** across 5 strata (figma, blender, the-pudding, its-nice-that, nytimes, apple, teenage-engineering, nothing). The inverse (personality in chrome, plain content) observed once (joshwcomeau). (V)

## 3. Depth & effects

- **Gradient as a primary brand device: 1 of 23** (stripe). Subtle washes elsewhere (apple): 1. Absent: 21. (V)
- **Glow as UI treatment: 1 of 23** (vercel); diegetic glow in one WebGL scene (bruno-simon). (V)
- **Glassmorphism as core language: 1 of 23** (nothing) — tied there to photography-first surfaces. (V)
- **Zero-corner-radius pages: ≥8 of 23** (nytimes, gov-uk, mcmaster-carr, hacker-news, mschf, teenage-engineering, poolsuite, aesop; plus sharp-dominant the-pudding, its-nice-that, cargo). (D/V)
- **Pill CTAs: 3 of 23** (linear, vercel, apple). Pronounced shadows: 0 of 23. (D/V)

## 4. Structure & layout

- **Dimmed embedded product imagery: 3 of 3 SaaS records, 0 of 20 others** (obsidian shows product at full brightness) — fully stratum-correlated in this corpus. (V)
- **Section-schema counts are low across the corpus**: 10 records operate with 1–2 schemas (apple, mschf, hacker-news, wikipedia, the-pudding, its-nice-that, gov-uk, cargo, rauno-me, poolsuite); the maximum observed is ~6 (nytimes). Layout variety and perceived excellence do not co-occur in any consistent way in this corpus. (V)
- **Structural predictability and surface predictability dissociate** in at least 4 records (the-pudding, its-nice-that, mschf, wikipedia): rigid schemas with heterogeneous interiors, or rigid schemas as the deviation itself. (V)

## 5. Signature mechanisms catalogued (Layer 2 — observer-tier, lowest epistemic status)

Distinct mechanisms by which records were perceived attributable:

| Mechanism | Records |
|---|---|
| Neutral-luminance ramp hierarchy | linear, vercel |
| Typeface-register voices ("who is speaking") | nytimes, vercel, nothing |
| Template uniformity as signature | apple |
| Codified constraint system | gov-uk |
| Convention refusal (exhaustive / empty / frozen) | mschf, cargo, hacker-news |
| Wholesale convention transplant (other medium/era) | poolsuite, bruno-simon |
| Curation over chrome (low-signature chrome) | its-nice-that |
| Link-density texture | wikipedia |
| Density contrast as identity | teenage-engineering |
| Chrome whimsy around conventional structure | joshwcomeau |
| Axis substitution (horizontal for vertical) | rauno-me |

🟡 "We observed that perceived signature in the excellence corpus rides on at least 11 distinct mechanisms, most of which are **relational or structural** (how elements relate to conventions, to content, or to each other) rather than attribute-level (which font, which color)."

## 6. Consolidated 🟡 hypotheses for the Atlas Experimental

1. 🟡 "We observed serif-as-primary-voice only in the editorial stratum (3/3 editorial; 0/20 elsewhere)."
2. 🟡 "We observed dimming of self-product imagery only in the SaaS stratum (3/3 SaaS; 0/20 elsewhere)."
3. 🟡 "We observed the same typeface (Inter) producing unrelated observable configurations at different weight/tracking settings — typeface identity alone may underdetermine 'look'."
4. 🟡 "We observed negative display tracking concentrated in product/SaaS-adjacent records (7 of 8 cases) and absent from utilitarian/editorial records."
5. 🟡 "We observed effects widely assumed ubiquitous (gradients, glow, glassmorphism) in ≤1 record each across 23 excellent interfaces."
6. 🟡 "We observed single-font discipline in 7 records spanning 5 strata — reduction recurs across unrelated aesthetics."
7. 🟡 "We observed chroma-delegation-to-content as the corpus's most recurrent color structure (8 records, 5 strata)."
8. 🟡 "We observed that low schema variety coexists with strong perceived identity in 10 records — predictable structure does not preclude signature."
9. 🟡 "We observed signature arising from relationship-to-convention (refusal, transplant, freezing) in 5 records — a mechanism class invisible to attribute-level observation."

## 7. Instrument feedback (for v0.3)

- Split **Predictability** into *structural* (schema repetition) and *surface* (visual repetition) — they dissociated in ≥4 records.
- Split **Perceived signature** into *chrome-signature* and *content-signature* (its-nice-that exposed the ambiguity).
- Add a **time dimension** field (hacker-news: constancy-while-genre-evolves functions as signature; instrument currently has no way to record it).
- "Predictability as schema count" is undefined for single-gesture pages (cargo) and single-screen apps (poolsuite, bruno-simon) — define scope.

## 8. Threats to validity (analysis stage)

- Single AI observer; Layer 2 has no inter-observer reliability; all Layer-2 counts are one observer's perceptions.
- 2 partial records lack visual evidence (bot-protected; not circumvented per policy).
- Locale variance: figma observed in pt-BR; stripe forced to en-US; nothing via intl store.
- Captures dated 2026-07-15; live sites change.
- Stratum sizes are small (2–3); stratum-correlation observations (serif↔editorial, dimming↔SaaS) rest on n=3 and are hypotheses, not findings.
- Selection bias: the corpus was chosen by reputation-for-excellence; counts describe this corpus only.
