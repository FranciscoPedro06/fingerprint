# Fingerprint

**A design-intelligence layer for Claude Code — and an open research program for detecting, explaining, and reducing the visual signature of AI-generated interfaces.**

Fingerprint helps Claude Code build, refactor, and review interfaces with deliberate choices instead of silently reproducing the most probable design for a category.

You continue using Claude normally. When the work touches an interface, Fingerprint changes the reasoning underneath:

- it identifies what kind of surface it is working on;
- understands the real intent before changing pixels;
- observes the existing project and brand material before acting;
- makes visual decisions with a traceable reason;
- builds inside the project's existing stack;
- audits its own result against concrete gates;
- tells you what it chose, what it did not choose, and where the result still feels generic.

> Fingerprint does not apply a house style. Its purpose is to help the interface carry the fingerprint of the product, organization, or person behind it.

---

## Table of contents

- [What Fingerprint is](#what-fingerprint-is)
- [Current status](#current-status)
- [Quick start](#quick-start)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Method 1: Claude Code plugin](#method-1-claude-code-plugin-recommended)
  - [Method 2: Personal skill](#method-2-personal-skill)
  - [Method 3: Local development](#method-3-local-development)
- [Verify the installation](#verify-the-installation)
- [How to use Fingerprint](#how-to-use-fingerprint)
- [Prompt examples](#prompt-examples)
- [How Fingerprint behaves](#how-fingerprint-behaves)
- [How it works](#how-it-works)
- [Update](#update)
- [Uninstall](#uninstall)
- [Troubleshooting](#troubleshooting)
- [Limits and non-goals](#limits-and-non-goals)
- [Repository structure](#repository-structure)
- [Development and contribution](#development-and-contribution)
- [Research program](#research-program)
- [Version and licensing](#version-and-licensing)

---

## What Fingerprint is

Fingerprint has two connected layers.

### 1. The installable product

The product is a Claude Code Skill located in [`product/fingerprint/`](product/fingerprint/).

It activates when Claude is asked to work on an interface, including tasks such as:

- creating a page, screen, component, or layout;
- refactoring an existing frontend;
- reviewing a screenshot or live interface;
- analyzing why a design feels generic;
- improving hierarchy, typography, composition, accessibility, or visual identity.

Claude remains the executor. Fingerprint changes how Claude reasons about the interface before, during, and after execution.

### 2. The research program

The repository is also an open research effort investigating why AI-generated interfaces are recognizable, which recurring structures carry that signal, and whether targeted interventions can measurably reduce it.

The research is detector-first: the long-term goal is not merely to give a model a better style guide, but to build an independently validated system that can detect, explain, and reduce recurring AI visual signatures.

---

## Current status

- **Product version:** `0.4.0`
- **Product state:** installable and maintained, but feature-frozen
- **Research direction:** detector-first
- **Observation language:** `v1`, stable
- **Independent detector:** not yet validated

The generation Skill is a downstream layer of the research program. It can build, refactor, and review interfaces today, but it still audits its own output. That is a known limitation: the system that creates an interface is not an independent judge of that same interface.

No new generation capability is intended to ship until a validated discriminator can support it.

---

## Quick start

Already have Claude Code installed? Run these commands **inside Claude Code**:

```text
/plugin marketplace add FranciscoPedro06/fingerprint
/plugin install fingerprint@fingerprint
```

Then open a project and ask Claude to work on an interface:

```text
Review this frontend, identify the choices that make it feel generic,
and refactor it without replacing the existing stack or design system.
```

Fingerprint is designed to activate automatically when the task calls for it.

---

## Prerequisites

### Required

- Claude Code
- Git, for the personal-skill and local-development installation methods
- Internet access for Claude Code authentication and plugin installation

### Claude Code requirements

According to the official Claude Code setup documentation, the supported baseline includes:

- macOS 10.15 or newer;
- Ubuntu 20.04, Debian 10, or newer;
- Windows 10 or newer through WSL or Git for Windows;
- at least 4 GB of RAM;
- Node.js 18 or newer when using the npm installation path.

### Install Claude Code

Using npm:

```bash
npm install -g @anthropic-ai/claude-code
```

Do not use `sudo npm install -g`. It can create permission and update problems.

Verify the installation:

```bash
claude --version
claude doctor
```

Start Claude Code in a project:

```bash
cd /path/to/your/project
claude
```

On Windows, use either:

- WSL 1 or WSL 2; or
- Git Bash through Git for Windows.

---

## Installation

Choose one installation method.

| Method | Best for | Scope | Update model |
|---|---|---|---|
| Plugin | Most users | Claude Code installation | Marketplace update |
| Personal skill | Users who want a simple global copy | Current user | Pull and copy again |
| Local development | Contributors and experimentation | Current Claude session | Reads working tree live |

### Method 1: Claude Code plugin — recommended

This is the easiest path and provides versioned plugin updates.

Start Claude Code:

```bash
claude
```

Inside the Claude Code session, add the marketplace:

```text
/plugin marketplace add FranciscoPedro06/fingerprint
```

Install the plugin:

```text
/plugin install fingerprint@fingerprint
```

Restart Claude Code after installation so the new session loads the plugin cleanly.

#### What the two commands do

1. `/plugin marketplace add ...` registers this repository as a Claude Code plugin marketplace.
2. `/plugin install ...` installs the `fingerprint` plugin declared by that marketplace.

The marketplace declaration is stored in [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json), and the plugin manifest is stored in [`product/fingerprint/.claude-plugin/plugin.json`](product/fingerprint/.claude-plugin/plugin.json).

---

### Method 2: Personal skill

Use this method when you want Fingerprint copied directly into your personal Claude Code skills directory.

#### Linux, macOS, or WSL

```bash
git clone https://github.com/FranciscoPedro06/fingerprint.git
mkdir -p ~/.claude/skills
cp -r fingerprint/product/fingerprint ~/.claude/skills/fingerprint
```

Verify the copy:

```bash
test -f ~/.claude/skills/fingerprint/SKILL.md \
  && echo "Fingerprint skill installed" \
  || echo "Fingerprint skill not found"
```

#### Windows PowerShell

```powershell
git clone https://github.com/FranciscoPedro06/fingerprint.git

$Target = Join-Path $HOME ".claude\skills\fingerprint"

New-Item `
    -ItemType Directory `
    -Path (Split-Path $Target) `
    -Force | Out-Null

Copy-Item `
    -Path ".\fingerprint\product\fingerprint" `
    -Destination $Target `
    -Recurse `
    -Force
```

Verify the copy:

```powershell
$Skill = Join-Path $HOME ".claude\skills\fingerprint\SKILL.md"

if (Test-Path $Skill) {
    Write-Host "Fingerprint skill installed: $Skill"
} else {
    Write-Error "Fingerprint skill was not found."
}
```

Restart Claude Code after copying the skill.

> The expected final path is `~/.claude/skills/fingerprint/SKILL.md`.
> Avoid accidentally creating `~/.claude/skills/fingerprint/fingerprint/SKILL.md`.

---

### Method 3: Local development

Use local development when you want to inspect or modify the Skill without installing a fixed copy.

Clone the repository:

```bash
git clone https://github.com/FranciscoPedro06/fingerprint.git
cd fingerprint
```

Start Claude Code with the plugin directory:

```bash
claude --plugin-dir ./product/fingerprint
```

This loads Fingerprint from the working tree for that session. Changes made to the local files become available after restarting the session.

This method is appropriate for:

- testing documentation changes;
- modifying `SKILL.md`;
- refining references or examples;
- evaluating behavior before opening a pull request.

---

## Verify the installation

Verification should confirm both the installation state and actual behavior.

### 1. Verify Claude Code

```bash
claude --version
claude doctor
```

### 2. Verify the plugin

Inside Claude Code:

```text
/plugin
```

Confirm that `fingerprint` appears in the installed plugins and that its version matches [`product/fingerprint/VERSION`](product/fingerprint/VERSION).

### 3. Verify a personal skill

Linux, macOS, or WSL:

```bash
ls -la ~/.claude/skills/fingerprint
cat ~/.claude/skills/fingerprint/VERSION
```

PowerShell:

```powershell
Get-ChildItem "$HOME\.claude\skills\fingerprint"
Get-Content "$HOME\.claude\skills\fingerprint\VERSION"
```

### 4. Run a functional test

Open a frontend project and ask:

```text
Analyze this interface before changing it.

Tell me which decisions appear intentional, which appear inherited from common
AI-generated interface patterns, and which one or two changes would give this
specific product a clearer identity. Then implement the improvement inside the
existing stack and audit the result.
```

A healthy Fingerprint session should:

- inspect the project or artifact before prescribing changes;
- avoid adding a new framework without permission;
- ask only for information that materially changes the result;
- distinguish functional correctness from expressive design;
- identify concrete visual evidence instead of making vague taste claims;
- build real output when asked to build;
- state the chosen direction and one meaningful alternative not taken;
- acknowledge any residual genericness or failed audit gate.

---

## How to use Fingerprint

You do not need to learn a second interface or a separate workflow.

Use Claude Code normally and describe the interface task.

### Build a new interface

```text
Create a landing page for this product.

Before building, inspect the repository and ask only the questions needed to
understand who the page is for, what it must accomplish, and what real material
can make the design specific to this product.
```

### Refactor an existing interface

```text
Refactor this dashboard without changing the framework or adding a design system.

Prioritize clarity, hierarchy, accessibility, and consistency with the existing
application. Do not force novelty into a functional surface.
```

### Review an interface

```text
Review this screen.

Separate correctness problems from aesthetic observations. Point to concrete
evidence in typography, color, spacing, layout, copy, effects, and component
structure. Do not rate it or give an AI-generated verdict.
```

### Investigate genericness

```text
Why does this landing page feel generic?

Identify the exact combination of layout, type, color, effects, copy, and
components that creates that impression. Distinguish choices I made from defaults
that may have arrived through the framework or the model.
```

### Improve without copying

```text
I like the density and directness of this reference, but do not clone it.

Extract the principle that makes the reference effective, then produce a
structural direction grounded in my product, content, and users.
```

---

## Prompt examples

### Good: contains real origin material

```text
Create a portfolio for a structural engineer.

The practice began from field notebooks used during bridge inspections. The
portfolio should make technical evidence and construction constraints feel more
important than personal branding. Use the actual projects in this repository and
build in the current Next.js stack.
```

Why this helps: the field notebooks, bridge inspections, and project evidence provide verifiable material that can shape composition, typography, density, and content hierarchy.

### Weak: gives only mood words

```text
Make a premium, modern, clean portfolio.
```

Why it is weak: “premium,” “modern,” and “clean” do not identify what makes this portfolio belong to a specific practice. They usually pull generation toward the current category average.

A stronger version:

```text
Make a portfolio for this architecture practice.

Its work is defined by exposed structural systems, local stone, and buildings that
show how they carry weight. Inspect the project photography and case studies before
choosing the page structure. The interface should make construction logic visible.
```

### Functional surface

```text
Improve this checkout.

Keep familiar checkout conventions. Focus on field clarity, error recovery,
keyboard navigation, contrast, mobile behavior, and reducing uncertainty before
payment. Do not add expressive complexity that competes with completion.
```

### Expressive surface

```text
Build the campaign page from the material in ./campaign-assets.

The campaign comes from handwritten maintenance logs found in the workshop. Use
that origin to decide the page's structure, not merely its texture or copy. Produce
a working implementation and then run the full Fingerprint audit.
```

---

## How Fingerprint behaves

Fingerprint first classifies the interface surface. This prevents it from applying the full expressive-design process to every UI task.

### Trivial surface

Examples:

- fixing padding;
- changing one token;
- repairing a broken control;
- adjusting a component inside an established system.

Expected behavior:

- match the surrounding code;
- make the correction;
- stop without inventing a broader redesign.

### Functional surface

Examples:

- dashboards;
- data tables;
- forms;
- checkouts;
- settings;
- documentation;
- internal tools.

Primary goals:

- clarity;
- hierarchy;
- familiarity;
- correctness;
- accessibility;
- efficient task completion.

Convention is often the correct answer. Fingerprint should not force a novel structural idea when novelty makes the interface harder to use.

### Expressive surface

Examples:

- landing pages;
- brand pages;
- portfolios;
- editorial experiences;
- campaign websites.

Primary goals:

- beauty;
- specificity;
- authorship;
- a structural idea grounded in the actual product or brand;
- deliberate deviation from category defaults.

Expressive work receives the full process and audit.

---

## How it works

The installable Skill is defined by [`product/fingerprint/SKILL.md`](product/fingerprint/SKILL.md).

Its operational loop is:

```text
classify surface
    → understand intent
    → observe
    → decide the structural idea
    → build or reflect
    → audit
    → hand authorship back
```

### 1. Classify the surface

Fingerprint decides whether the work is trivial, functional, or expressive and calibrates effort accordingly.

### 2. Understand intent

It asks one or two high-value questions when the existing context is insufficient.

The questions seek concrete origins:

- a real object;
- a founder's reason;
- an existing workflow;
- a physical environment;
- actual content;
- constraints that affect the interface.

Mood words alone are not enough.

### 3. Observe before acting

Depending on the task, Fingerprint examines:

- the existing codebase and stack;
- components and design tokens;
- brand material;
- screenshots or live pages;
- typography;
- color;
- effects;
- shape and spacing;
- layout;
- copy;
- motion.

Claims must match the available evidence. A screenshot supports visual observation, but not exact runtime behavior. Source code supports precise token inspection, but does not prove the rendered result.

### 4. Decide structure before skin

On expressive surfaces, Fingerprint looks for a structural idea rather than merely selecting a style.

A structural idea changes what the page is and how it is composed. A skin only repaints a familiar skeleton.

Examples of structural directions:

- make the page behave like the real appointment book;
- make the product itself own the composition;
- invert the expected reading axis;
- push density contrast to an intentional extreme;
- organize the experience around a real price board, queue, archive, or instrument.

### 5. Build the real thing

Fingerprint does not stop at commentary when the user asks for implementation.

The delivery contract includes:

- use the existing stack and conventions;
- do not add a framework or design system without permission;
- produce working code;
- preserve semantic structure;
- maintain visible focus states;
- use meaningful alternative text;
- support layouts from 360 px upward;
- meet WCAG AA contrast floors:
  - body text: at least `4.5:1`;
  - large text and UI boundaries: at least `3:1`.

### 6. Audit before delivery

The audit is based on checkable gates rather than a general “looks good” impression.

It checks:

- recurring generator-kit atoms;
- whether the design survives a cross-genre logo test;
- whether every reflexive design choice has a verifiable origin;
- whether a real structural idea changed the composition;
- contrast;
- whether an alternative direction was made visible;
- which current design centroid the result may still occupy;
- whether the pixels actually support the story claimed by the copy;
- beauty, spacing, kerning, legibility, and overall craft.

If a gate fails, Fingerprint should iterate or state the remaining failure plainly.

### 7. Hand authorship back

The final explanation should briefly identify:

- what was chosen;
- where each major choice came from;
- one meaningful direction that was not taken;
- what remains open for the user to keep, reject, or revise.

Fingerprint makes decisions, but it does not present its taste as objective truth.

---

## Update

Installed copies do not necessarily receive a new Fingerprint version automatically. Update it using the same method used for installation.

### Update a plugin installation

Inside Claude Code:

```text
/plugin marketplace update fingerprint
/plugin update fingerprint@fingerprint
```

Restart Claude Code after updating.

Confirm the installed version:

```text
/plugin
```

Compare it with [`product/fingerprint/VERSION`](product/fingerprint/VERSION).

### Update a personal skill

#### Linux, macOS, or WSL

From the cloned repository:

```bash
cd fingerprint
git pull
rm -rf ~/.claude/skills/fingerprint
cp -r product/fingerprint ~/.claude/skills/fingerprint
```

The clean replacement prevents files removed by a newer release from remaining in the installed copy.

#### Windows PowerShell

```powershell
Set-Location .\fingerprint
git pull

$Target = Join-Path $HOME ".claude\skills\fingerprint"

Remove-Item `
    -Path $Target `
    -Recurse `
    -Force `
    -ErrorAction SilentlyContinue

Copy-Item `
    -Path ".\product\fingerprint" `
    -Destination $Target `
    -Recurse `
    -Force
```

Restart Claude Code.

### Update a local-development checkout

```bash
cd fingerprint
git pull
claude --plugin-dir ./product/fingerprint
```

The local-development method reads the checkout directly, so no separate copy step is required.

---

## Uninstall

### Remove the plugin

Inside Claude Code, inspect the available plugin commands:

```text
/plugin
```

Use the uninstall action shown by the current Claude Code plugin interface for `fingerprint@fingerprint`.

Plugin command surfaces can change between Claude Code releases; using `/plugin` ensures that the action matches the installed version.

### Remove a personal skill

Linux, macOS, or WSL:

```bash
rm -rf ~/.claude/skills/fingerprint
```

PowerShell:

```powershell
Remove-Item `
    -Path "$HOME\.claude\skills\fingerprint" `
    -Recurse `
    -Force
```

Restart Claude Code.

### Remove a local checkout

```bash
rm -rf fingerprint
```

Only remove the checkout after confirming it contains no uncommitted work.

---

## Troubleshooting

### `claude: command not found`

Check Node.js and npm:

```bash
node --version
npm --version
```

Install Claude Code again:

```bash
npm install -g @anthropic-ai/claude-code
```

Then run:

```bash
claude doctor
```

On Windows, run Claude Code through WSL or Git Bash.

---

### The marketplace cannot be added

Confirm that the repository is reachable:

```bash
git ls-remote https://github.com/FranciscoPedro06/fingerprint.git HEAD
```

Inside Claude Code, retry:

```text
/plugin marketplace add FranciscoPedro06/fingerprint
```

Common causes include:

- no internet connection;
- a corporate proxy or firewall blocking GitHub;
- GitHub authentication or rate-limit issues;
- an outdated Claude Code installation.

Update Claude Code:

```bash
claude update
```

Then restart it and retry.

---

### The plugin is installed but does not activate

1. Restart Claude Code.
2. Confirm the plugin appears under `/plugin`.
3. Open a repository containing frontend work.
4. Use an explicit interface request.

Example:

```text
Use Fingerprint to review and refactor this interface.
Inspect the existing stack first and audit the result before delivery.
```

Fingerprint may intentionally do very little on a trivial task. That is expected behavior, not necessarily a loading failure.

---

### The installed version is old

Refresh both the marketplace and plugin:

```text
/plugin marketplace update fingerprint
/plugin update fingerprint@fingerprint
```

Restart Claude Code and check `/plugin` again.

---

### Personal skill installed in the wrong directory

Expected path:

```text
~/.claude/skills/fingerprint/SKILL.md
```

Incorrect nested path:

```text
~/.claude/skills/fingerprint/fingerprint/SKILL.md
```

Linux, macOS, or WSL diagnosis:

```bash
find ~/.claude/skills/fingerprint -maxdepth 3 -name SKILL.md -print
```

PowerShell diagnosis:

```powershell
Get-ChildItem `
    "$HOME\.claude\skills\fingerprint" `
    -Filter "SKILL.md" `
    -Recurse
```

If the file is nested incorrectly, remove the target and copy `product/fingerprint` again.

---

### Removed reference files remain after an update

This occurs when a new copy is merged over an old personal-skill directory.

Perform a clean replacement:

```bash
rm -rf ~/.claude/skills/fingerprint
cp -r product/fingerprint ~/.claude/skills/fingerprint
```

---

### Windows PowerShell copied the directory incorrectly

Inspect the target:

```powershell
Get-ChildItem `
    "$HOME\.claude\skills\fingerprint" `
    -Recurse `
    -Depth 2
```

`SKILL.md`, `VERSION`, `references`, `examples`, and `evals` should be directly inside the `fingerprint` directory.

---

### Claude Code has authentication or installation problems

Run:

```bash
claude doctor
```

Claude Code requires network access for authentication and model requests. Corporate environments may also require HTTP/HTTPS proxy and trusted-certificate configuration.

Consult the official Claude Code setup and corporate-proxy documentation for environment-specific configuration.

---

### Fingerprint asks for more context instead of building

This is expected when an expressive task contains no real brand or product material.

Without access to a real origin, project content, or reference material, a model can only reconstruct the category average from memory.

Provide concrete input such as:

- repository content;
- product screenshots;
- brand assets;
- photography;
- a founder story;
- physical artifacts;
- actual copy;
- target users and constraints.

---

### Fingerprint preserves a conventional design

On dashboards, forms, checkouts, settings, and other functional surfaces, convention may be the correct answer.

Fingerprint should pursue clarity and correctness rather than forcing novelty into a task-oriented interface.

---

## Limits and non-goals

Fingerprint deliberately does **not**:

- impose its taste as the objectively correct answer;
- decide permanently on behalf of the user;
- provide a numeric design score;
- declare that an interface was or was not generated by AI;
- clone another site's visual identity;
- apply one reusable house style to every project;
- silently ship an obviously generic result;
- make precise claims that the available artifact cannot support;
- treat self-audit as independent scientific validation.

When asked to copy a reference exactly, the intended behavior is to extract the useful principle and build a direction grounded in the user's own product.

When asked for an AI-generation verdict, the intended behavior is to identify concrete proximity to genre conventions without pretending that this is a validated detector result.

---

## Repository structure

| Path | Responsibility |
|---|---|
| [`product/`](product/) | The installable Fingerprint product and product-side documentation |
| [`product/fingerprint/`](product/fingerprint/) | Claude Code Skill artifact |
| [`product/fingerprint/SKILL.md`](product/fingerprint/SKILL.md) | Operational definition of the Skill |
| [`product/fingerprint/references/`](product/fingerprint/references/) | Supporting build, review, input, voice, and audit guidance |
| [`product/fingerprint/examples/`](product/fingerprint/examples/) | Worked session transcripts |
| [`product/fingerprint/evals/`](product/fingerprint/evals/) | Evaluation prompts and provisional rubric |
| [`research/`](research/) | Detector-first research program and synthesized findings |
| [`observation-language/`](observation-language/) | Model-independent grammar for structured observation |
| [`methodology/`](methodology/) | Research laws and methodological constraints |
| [`experiments/`](experiments/) | Self-contained experiments |
| [`corpus/`](corpus/) | Reviewed observation records and experimental data |
| [`atlas/`](atlas/) | Catalog of observed phenomena and patterns |
| [`docs/`](docs/) | Cross-cutting research documentation |
| [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json) | Claude Code marketplace declaration |

### Start reading here

For the product:

1. [`product/README.md`](product/README.md)
2. [`product/fingerprint/SKILL.md`](product/fingerprint/SKILL.md)
3. [`product/fingerprint/references/deviation.md`](product/fingerprint/references/deviation.md)
4. [`product/fingerprint/references/the-kit.md`](product/fingerprint/references/the-kit.md)
5. [`product/fingerprint/references/authored-vs-ai.md`](product/fingerprint/references/authored-vs-ai.md)

For the research:

1. [`research/PROGRAM.md`](research/PROGRAM.md)
2. [`observation-language/`](observation-language/)
3. [`methodology/`](methodology/)
4. [`experiments/`](experiments/)

---

## Development and contribution

### Clone and load the plugin locally

```bash
git clone https://github.com/FranciscoPedro06/fingerprint.git
cd fingerprint
claude --plugin-dir ./product/fingerprint
```

### Files that define product behavior

The most important implementation files are:

```text
product/fingerprint/SKILL.md
product/fingerprint/references/
product/fingerprint/examples/
product/fingerprint/evals/
product/fingerprint/.claude-plugin/plugin.json
product/fingerprint/VERSION
.claude-plugin/marketplace.json
```

### Before opening a pull request

1. Read the current root README and [`product/README.md`](product/README.md).
2. Confirm that the proposed behavior does not conflict with the product laws in `SKILL.md`.
3. Keep the product and research layers distinct.
4. Do not represent self-graded output as independent evidence.
5. Keep plugin metadata and `VERSION` synchronized when changing the product version.
6. Load the plugin locally and exercise the affected path.
7. Check relative Markdown links.
8. Explain what changed, why it changed, and how it was verified.

### Suggested local checks

Check Markdown links and referenced files with a link checker available in your environment.

At minimum, inspect local relative links:

```bash
grep -oE '\]\([^)]+\)' README.md \
  | sed -E 's/^\]\((.*)\)$/\1/' \
  | grep -vE '^(https?://|#|mailto:)' \
  | sort -u
```

Confirm product metadata:

```bash
cat product/fingerprint/VERSION
cat product/fingerprint/.claude-plugin/plugin.json
cat .claude-plugin/marketplace.json
```

Start a local session:

```bash
claude --plugin-dir ./product/fingerprint
```

---

## Research program

Fingerprint's research asks a falsifiable question:

> What separates the distribution of AI-generated interfaces from human-authored ones such that people recognize membership quickly, often without being able to articulate why?

The project reframes the “AI look” as a distribution problem rather than one visual style.

Two properties are central:

- **low variance:** unrelated briefs often produce the same structures with different paint;
- **co-occurrence:** individually ordinary design atoms recur together as a recognizable bundle.

The detector-first program is organized around four stages:

1. **Detect** — determine whether blind observers can distinguish the relevant output classes.
2. **Explain** — identify the features, co-occurrence bundles, and variance signatures carrying the signal.
3. **Reduce** — test whether a targeted intervention measurably moves an interface out of the recognizable region.
4. **Validate independently** — keep generation and final judgment separate.

The human recognizer remains the reference. A model-based judge is only a scalable proxy after it demonstrates agreement with human evaluation.

---

## Version and licensing

### Version

The current product version is stored in:

```text
product/fingerprint/VERSION
```

Plugin metadata is stored in:

```text
product/fingerprint/.claude-plugin/plugin.json
```

At the time of this README revision, the product version is **0.4.0**.

### Licensing

- Product code and Skill: **MIT**
- Research and documentation artifacts: **CC-BY-4.0**

Per-directory licensing notes govern any differences.

---

## One-minute summary

Install:

```text
/plugin marketplace add FranciscoPedro06/fingerprint
/plugin install fingerprint@fingerprint
```

Use:

```text
Build, review, or refactor this interface.
Inspect the project first, ground every major visual choice in real material,
preserve the existing stack, and audit the final result before delivery.
```

Update:

```text
/plugin marketplace update fingerprint
/plugin update fingerprint@fingerprint
```

Fingerprint is not a template and not a validated AI detector. It is a design-intelligence layer that helps Claude Code make its interface decisions visible, grounded, and specific — while the repository develops the independent research needed to measure that goal honestly.
