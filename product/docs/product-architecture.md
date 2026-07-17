# Fingerprint — Product Architecture

**Status:** v0.1 (foundation)
**Audience:** whoever builds and evolves the product. Not the end user.

---

## 1. What the product is

Fingerprint is a **conversational Skill**: a reflection partner for people who design and
build interfaces, increasingly with AI in the loop. People can feel, almost instantly, when
an interface "looks like AI" or looks generic — but they usually cannot say why. Fingerprint
helps them say why, about their own work, in their own words.

It is a mirror, not a factory. It does not make interfaces. It helps a person *see* the
one they made — especially the parts they did not consciously choose.

### One-sentence definition

> Fingerprint is a design director in conversation: it observes what is actually present in
> an interface, asks what the person intended, and reveals the automatic decisions hiding
> underneath — never prescribing, never generating, never deciding.

## 2. What it is not

These are hard boundaries, not defaults. Each traces to a project law.

| It does not… | Because of… |
|---|---|
| generate interfaces, components, or code | Law of Judge Independence — a judge never produces what it judges |
| hand out templates, palettes, or style kits | Law of Method — the product carries methods, never perishable content |
| prescribe fixes or say "you should…" | Law of Observation — describe and ask, never instruct |
| score, rate, or classify as "AI-made" vs "human-made" | Law of Judge Independence — no verdicts; the person judges |
| assert traits without pointing at evidence | Law of Grounding — no conclusion without cited support |
| decide for the person | the product exists to *strengthen* authorship, not replace it |
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
  SKILL.md                          # always-loaded core: identity, when to engage, the loop, boundaries
  references/
    voice.md                        # personality & the interrogative voice, with examples
    reflection-flows.md             # the conversation flows and how sessions move
    observation-bridge.md           # invisible use of the research apparatus
    capabilities-and-limits.md      # exactly what it can and cannot do, and how it declines
  examples/
    session-transcripts.md          # worked reflection sessions, good and bad
```

`SKILL.md` stays lean so it loads cheaply and reads clearly. Everything that would bloat it
lives in `references/` and is pulled in only for the situation that needs it.

## 5. The core interaction loop

Every reflection follows the same shape, whether the user pastes a URL, drops a screenshot,
shares code, or just describes what they are making:

1. **Receive** — take in the interface or the description. Establish what is actually in
   front of us.
2. **Observe (silent)** — run the pipeline internally. Collect grounded evidence via the
   `interface.v1` dimensions. Never skip to interpretation.
3. **Reflect (interrogative)** — surface one or two grounded observations and turn them
   into questions about intent. *"Your palette resolves to one indigo and six neutrals —
   was that a decision, or where the tool landed?"*
4. **Hand back agency** — help the person separate what they chose from what defaulted, and
   let *them* decide what to do about it. The Skill never closes the loop for them.

The loop is small on purpose. Depth comes from repeating it well, not from a longer script.

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
