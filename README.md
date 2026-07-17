# Fingerprint

**A design-intelligence layer for Claude Code.** Install it once. Then keep using Claude
normally — but every time the work touches an interface, Claude thinks differently.

Ask Claude to *"create a landing page,"* *"analyze my frontend,"* or *"refactor this
dashboard,"* and instead of racing to output the most probable, most average version, it:

- **understands what makes this one _yours_** before building,
- **makes deliberate, visible choices** instead of silent generic defaults,
- **builds the real thing** (Claude is still the executor),
- and **takes an honest second look**, telling you where it still came out generic.

The result carries a fingerprint instead of the interchangeable *"AI look."* You feel the
difference in the first thirty seconds.

> The "AI look" is not a set of ugly traits. It's the **absence of deviation** — the interface
> sits exactly on the center of its genre's conventions, so nobody ever made a choice.
> Fingerprint exists to defeat that, in both directions: making real choices when building, and
> making automatic ones visible when reviewing.

---

## Install

Pick one. All three give Claude the Fingerprint layer; they differ only in how it's delivered.

### 1. As a plugin (recommended — one command, versioned updates)

In Claude Code:

```
/plugin marketplace add FranciscoPedro06/fingerprint
/plugin install fingerprint@fingerprint
```

That's it. Open any project and start working on an interface — Claude loads Fingerprint on
its own when the task calls for it.

### 2. As a personal skill (simplest — works in every project)

Copy the skill into your personal skills directory:

```bash
git clone https://github.com/FranciscoPedro06/fingerprint
cp -r fingerprint/product/fingerprint ~/.claude/skills/fingerprint
```

Now `/fingerprint` is available everywhere, and Claude auto-invokes it on design tasks.

### 3. For local development / trying it out

```bash
git clone https://github.com/FranciscoPedro06/fingerprint
claude --plugin-dir ./fingerprint/product/fingerprint
```

Loads Fingerprint for that session only — good for hacking on it.

---

## How it works

You never talk to two systems. There is only Claude. Underneath, when the task is about a
screen, Claude runs one small loop:

```
intent  →  observe (silent)  →  reflect / decide where to deviate  →
execute (build the real thing)  →  honest second look  →  hand authorship back
```

Fingerprint never imposes its own taste, never decides for you, and never ships the average
silently. It makes choices *legible* — it tells you what it chose and what it passed on — so
the work stays yours to keep or overrule.

The product lives in **[`product/`](product/)**. Start with
[`product/fingerprint/SKILL.md`](product/fingerprint/SKILL.md) (what Claude becomes) and
[`product/fingerprint/references/deviation.md`](product/fingerprint/references/deviation.md)
(the craft of building off the centroid).

---

## The research behind it

Fingerprint stands on an open research effort into *why AI-generated interfaces are
recognizable* — the recurring visual traits that make a screen read as "made by AI." The
product only ever uses research that has reached a stable state; the research never bends to
serve the product's convenience. That apparatus lives here too:

| Directory | Responsibility |
|---|---|
| [`observation-language/`](observation-language/) | The core grammar for observation. Object-general, model-independent. The heart of the research. |
| [`methodology/`](methodology/) | The laws and principles that govern how the research is conducted. |
| [`experiments/`](experiments/) | Self-contained experiments (`EXP-NNNN`) that exercise and stress-test the language. |
| [`corpus/`](corpus/) | Reviewed observation records, written in the observation language. The data. |
| [`atlas/`](atlas/) | The catalog of phenomena and fingerprints discovered through observation, with explicit status. |
| [`research/`](research/) | Synthesized findings that draw across experiments and corpus. |
| [`docs/`](docs/) | Cross-cutting research documentation: glossary, governance, contribution. |

The research holds itself to a discipline: description precedes interpretation, every
interpretation cites its evidence, every attribution declares its confidence and keeps the
alternatives it outranks, and the language names no tool, model, or vendor — so records written
today stay readable long after any specific technology is gone.

**None of that machinery is ever exposed to the person using the product.** It is the engine
behind the curtain; they meet only the last block — Claude, thinking well about their screen.

---

## Status

The product is at **v0.2** (the execution layer — it builds, refactors, and reviews). The
observation language it stands on is at **v1** and stable; the corpus and atlas are being
populated through the experiment track. Nothing enters the validated atlas without independent
human review.

## Licensing

Code (the product / Skill) is **MIT**. Research and documentation artifacts are **CC-BY-4.0**,
intended for open reuse. Per-directory notes govern where they differ; see [`docs/`](docs/).
