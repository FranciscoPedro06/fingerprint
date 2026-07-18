# Fingerprint — Product Architecture

**Status:** v0.2 (execution layer)
**Audience:** whoever builds and evolves the product. Not the end user.

---

## 1. What the product is

Fingerprint is a **design-intelligence layer**, shipped as a Skill, that runs on top of Claude
and changes *how* Claude thinks whenever the work touches an interface — creating, analyzing,
refactoring, or improving one. The person keeps using Claude normally; nothing announces
itself. But the reasoning underneath changes shape, and the person feels it in the first
thirty seconds.

People can feel, almost instantly, when an interface "looks like AI" or looks generic — but
they usually cannot say why. The research found the why: the "AI look" is the **absence of
deviation** — the interface sits on its genre's convention centroid, so no one ever made a
choice. Fingerprint exists to defeat that in two directions: it **builds with deliberate,
owned choices** so output carries a fingerprint, and it **makes automatic choices visible**
when reviewing so the person's authorship gets stronger.

It is neither a mirror that refuses to touch anything nor a factory stamping a house style. It
is the difference between *defaulting* and *deciding*.

### One-sentence definition

> Fingerprint is the way Claude thinks about interfaces: it understands intent, observes
> before acting, builds (or reflects) with deliberate and legible choices instead of generic
> defaults, and takes an honest second look at the result — never imposing its taste, never
> deciding for the person, always handing authorship back.

## 2. What it is not

These are hard boundaries, not defaults. Each traces to a project law.

| It does not… | Because of… |
|---|---|
| impose its own taste as the correct design | Law of Handed-Back Authorship — choices stay legible and reversible, never imposed |
| decide for the person, or overwrite a claimed intention | the product *strengthens* authorship, never replaces it |
| ship the genre centroid silently and call it done | Law of the Honest Second Look — it says where its own build came out generic |
| hand out reusable templates or a house style kit | Law of Method — the product carries methods, never perishable content; every build is chosen for *this* intent |
| score, rate, or classify as "AI-made" vs "human-made" | no verdicts; the person judges |
| assert traits without pointing at evidence | Law of Grounding — no conclusion without cited support |
| expose research machinery (Atlas IDs, EXP numbers, pipeline terms) unprompted | the research is invisible; the curtain stays down |

## 3. The system behind the curtain

The user talks to one calm, perceptive partner. Underneath, that partner runs the research
apparatus, silently:

```
        ┌─────────────────────── what the user sees ───────────────────────┐
        │   a design director asking good questions about their interface   │
        └───────────────────────────────────────────────────────────────────┘
                                       ▲
                                       │  translated to interrogative, grounded voice
                                       │
   ┌───────────────────────────────────┴────────────────────────────────────┐
   │                     what runs behind the curtain                        │
   │                                                                         │
   │   Observation Language pipeline (never named to the user):              │
   │     Evidence ──▶ Relations ──▶ Hypotheses ──▶ Best-supported Attribution│
   │                                                                         │
   │   interface.v1 profile  ─ which evidence dimensions to look for         │
   │   methodology laws      ─ the voice and the boundaries                  │
   │   atlas / corpus        ─ prior grounded pattern (read-only, when stable)│
   └─────────────────────────────────────────────────────────────────────────┘
```

The bridge from apparatus to conversation is specified in
[`../fingerprint/references/observation-bridge.md`](../fingerprint/references/observation-bridge.md).
The rule is absolute: research vocabulary is a source, never a script. The user hears a
person, not a pipeline.

## 4. The Skill artifact

The product ships as a standard Skill: a directory whose entry point is `SKILL.md` (YAML
frontmatter + core behavior), with deeper material in `references/` loaded only when needed.
This mirrors the project's own law — *core small, depth at the edges*.

```
product/fingerprint/
  SKILL.md                          # always-loaded core: identity, the four laws, the loop, boundaries
  references/
    first-contact.md                # the first-run "why this is different" moment, on build and review
    inputs.md                       # receiving each input type (screenshot, URL, code, Figma, codebase) safely
    authored-vs-ai.md               # EVIDENCE: 23 excellent real interfaces vs AI defaults; signature is structural, not a skin
    the-kit.md                      # the genre-independent atoms the model reuses on every brief (its own fingerprint) + count rule
    deviation.md                    # the build craft: making choices off the genre centroid
    voice.md                        # personality & the interrogative voice, with examples
    reflection-flows.md             # the conversation flows and how sessions move
    observation-bridge.md           # invisible use of the research apparatus
    capabilities-and-limits.md      # exactly what it does and doesn't, and how it declines
  examples/
    session-transcripts.md          # worked sessions across build, review, and refactor — good and bad
  VERSION
```

`SKILL.md` stays lean so it loads cheaply and reads clearly. Everything that would bloat it
lives in `references/` and is pulled in only for the situation that needs it.

## 5. The core interaction loop

Every design task — building or looking — runs the same shape, whether the user pastes a URL,
drops a screenshot, shares code, or asks for something to be created:

1. **Understand intent** — get what this is actually *for*, and where it should refuse to be
   generic. One or two sharp questions, not a requirements interrogation. If enough was given,
   proceed.
2. **Observe (silent)** — run the pipeline internally: the surrounding codebase and the genre
   centroid (for a build), or the artifact's `interface.v1` dimensions (for a review). Never
   skip to interpretation.
3. **Reflect — decide where to deviate** — pick the deliberate, coherent choices that give the
   thing a fingerprint (build), or the one or two observations that reveal where a choice was
   never made (review).
4. **Execute** — when the task is to build, Claude produces the real, working artifact with
   the choices from step 3. (If the task was only to look, skip.)
5. **Honest second look** — turn the same critical eye on the just-built output; say plainly
   where it still landed on the centroid.
6. **Hand authorship back** — name the choices made and a fork not taken; let *them* decide.
   The Skill never closes the loop as though its version is final.

The loop is small on purpose. Depth comes from running it well, not from a longer script. Full
build craft: [`../fingerprint/references/deviation.md`](../fingerprint/references/deviation.md).

## 6. State and memory

Two horizons, defined fully in
[`../fingerprint/references/reflection-flows.md`](../fingerprint/references/reflection-flows.md):

- **Working state (within a session):** what the person is building; which decisions they
  have claimed as intentional; which patterns have already been surfaced (so the Skill does
  not repeat itself); recurring defaults noticed across the session.
- **Carried memory (across sessions), opt-in:** the person's stated intentions and recurring
  tendencies, so the partner can say *"the soft-shadow default has shown up in the last few
  things you've shared — worth a look?"* Nothing is carried without the person's awareness.

## 7. Versioning

The product versions independently of the research (two velocities). Product releases use
semantic-ish versioning; the observation apparatus it depends on is pinned by version
(`interface.v1`, `observation-language/v1`) so a product release always states which stable
research it stands on. See [`roadmap.md`](roadmap.md) and [`versioning.md`](versioning.md).

## 8. Quality bar

Treat this as software used daily by many people. Concretely:

- Every observation the Skill voices must be traceable to something actually present.
- The Skill would rather ask one sharp question than list ten shallow ones.
- The Skill never flatters and never scolds. It is precise and calm.
- A first-time user should feel they are talking to an unusually perceptive colleague, and
  should never once sense the machinery.
