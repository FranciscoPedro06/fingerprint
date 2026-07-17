# Versioning

The product and the research move at **two velocities** and are versioned separately. This
file states how product versions work and how they stay honestly tied to the research they
stand on.

---

## Product version

Format: `MAJOR.MINOR.PATCH`, tracked in `product/fingerprint/VERSION` and mirrored in the
Skill's release notes.

- **MAJOR** — a change to what the product fundamentally is or how it behaves at the level of
  its constitution (the four laws). Expected to be extremely rare; a MAJOR bump is really a
  product redefinition and belongs to Pedro, not to routine work.
- **MINOR** — new capability or a meaningful behavioral improvement that stays inside the
  existing laws (e.g. richer observation cues, opt-in memory).
- **PATCH** — wording, examples, decline-pattern tuning, bug fixes in behavior. No new
  capability.

The current version is **0.1.0**.

## Pinned research dependencies

Every product release states, explicitly, which stable research versions it stands on. The
product never depends on research that has not reached a stable state.

Current pins (v0.1.0):

| Dependency | Pinned version |
|---|---|
| Observation Language | `v1` |
| Interface profile | `interface.v1` |
| Methodology (laws) | current (`methodology/laws-and-principles.md`) |

When a pinned dependency changes in a way that affects the product, that is a product change
and gets its own version bump and release note — the product does not silently inherit
research drift.

## The one-way rule

The product reads from stable research; it never writes back to it. Nothing in `product/`
edits `observation-language/`, `methodology/`, `atlas/`, `corpus/`, or `experiments/`. If
product work reveals something the research should absorb, that's raised as a research note
for the slow track — not patched across the curtain.

## Release notes

Each release gets an entry in `product/docs/releases/` (`vMAJOR.MINOR.PATCH.md`) stating:
what changed in behavior, which files moved, the research pins, and anything a user would
feel. v0.1.0's entry is the first.
