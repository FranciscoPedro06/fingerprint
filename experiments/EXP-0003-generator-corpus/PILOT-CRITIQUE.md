# Pilot critique — blinding pipeline

**Date:** 2026-07-20
**Ran by:** the collector (Claude), per the Independence requirement. The collector knows
provenance by necessity and is therefore disqualified as an EXP-0004 observer of these samples.
**Covers:** protocol §"Sequencing — pilot before battery", the *Critique* step: *does any step leak
provenance? is the capture truly identical across sides?*

**Verdict: the blinding pipeline works. The corpus does not yet support EXP-0004.**
`samples/` is a valid demonstration that provenance can be stripped cleanly. It is **not** a
runnable recognition set, for the reasons in A and B below. Do not judge it and report a number.

---

## A. The corpus has no human side — H1 is untestable

The protocol defines two sides: an AI side and a human side in three reference classes
(typical-professional, curated-excellent, trend-following-human). **The human side is empty.**
All six samples are AI-generated.

EXP-0004's primary question is whether a blind judge can tell Claude-made from human-made. With
no human samples there are no true negatives, so accuracy, calibration, and d′ are all undefined.
A judge run on this set would produce a number that means nothing, and the number would be
believed anyway. This is the blocking gap, and it is a *collection* gap, not a tooling one.

## B. `ai-fingerprint` is not a class this experiment defines

Half the corpus is Claude-with-Fingerprint. EXP-0003's AI side is *generators*, and its isolation
requirement is explicit: a Claude context that knows Fingerprint, its hypotheses, or the Kit
"will generate atypically — either performing the tells or dodging them — and poison the corpus."

The `ai-fingerprint` arm is theory-saturated **by construction**. It is therefore not admissible
as EXP-0003 AI-side material. It is legitimate and interesting evidence, but it belongs to
**EXP-0006 (reduce)** — *does the intervention move an interface out of the recognizable region?* —
which is a different question with a different design, and one that still needs the detector to
exist first.

Recommendation: move the `ai-fingerprint` arm out of this corpus and into an EXP-0006 holding
area, so it cannot be mistaken for generator-representative samples later.

## C. Capture was not identical across arms — now partly fixed, still not clean

| Arm | Captured | Engine | Status |
|---|---|---|---|
| `ai-claude` | 2026-07-18 | not logged | **unverified** |
| `ai-fingerprint` | 2026-07-20 | Chromium headless (Edge), scale 1 | logged |

Geometry now matches (1280×800 hero, 1280×4200 full-page, both arms). The **engine and date do
not**, and the protocol names the polish/fidelity confound as "the primary construction risk." A
renderer difference is exactly the kind of artifact that can masquerade as signal.

**Action before any real run: re-capture the `ai-claude` arm from its HTML through the same
engine, in one session, and log the parameters.** The HTML is preserved, so this is cheap.

## D. Leaks found and closed

1. **PNG metadata (real, closed).** Ancillary chunks (`tEXt`, `tIME`, `pHYs`, `iCCP`, `eXIf`) can
   carry the rendering engine, a timestamp, or a colour profile. With two arms captured on
   different days by different engines, provenance was recoverable **from the file bytes with no
   design judgement at all.** `tools/blind.py` now copies only the critical chunks. Verified: the
   observer-facing PNGs contain `IHDR`, `IDAT`, `IEND` and nothing else.
2. **Ordering (real, closed).** Sample-ids are assigned from a shuffled list; the seed lives in
   the sealed manifest only.
3. **Filenames and directories (real, closed).** The sealed tree encodes source class in its
   directory names. Observer-facing files are `S-NNNN-{hero,full}.png` and nothing more.

## E. Residual channels — declared, not solved

- **File size.** A page's byte size is a property of the page and cannot be normalised away
  without altering the image. In a set this small a judge could plausibly cluster on it. Mitigated
  only by scale.
- **Pedro holds the key.** `_sealed/` is on the judge's own disk. The blinding is honour-system
  for him by construction; the tooling makes the honest path easy, it cannot make the dishonest
  one impossible. This is already acknowledged in EXP-0004 §"Because the judge is also the project
  author" and it is the strongest argument for the external human panel.
- **n = 6.** Far below any usable power. Pilot scale, by design.

## F. Capture defect to fix

At least one sample shows a clipped nav button, consistent with a web-font loading race: the
screenshot fires before webfonts settle. `--virtual-time-budget` alone does not guarantee font
readiness. Add an explicit `document.fonts.ready` wait before capture, then re-run both arms.

---

## What has to happen before EXP-0004 runs

1. Collect the human side — all three classes, matched to briefs B01/B07/B10 at minimum.
2. Move `ai-fingerprint` out to EXP-0006.
3. Re-capture every arm through one engine in one session, with a fonts-ready wait.
4. Re-run `tools/blind.py`.
5. Only then judge, and judge with someone who is not the collector.
