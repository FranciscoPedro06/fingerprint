# Observation Language — Profiles

**Status:** Non-normative.

A **profile** is a catalog of evidence dimensions relevant to a class of objects. Profiles
help an observer collect thorough, comparable evidence without the core grammar having to
name domain-specific attributes.

## What a profile may and may not do

A profile **MAY**:
- list evidence dimensions worth checking for a domain;
- suggest a derivation method for each (measured / counted / classified / reported);
- group dimensions for convenience.

A profile **MUST NOT**:
- add, remove, or reorder the four pipeline stages;
- introduce required fields (profiles are prompts, not forms);
- weaken any foundational commitment or admissibility rule in the
  [Specification](../SPECIFICATION.md);
- carry evaluation, comparison, or attribution (those are later stages, not evidence).

## Why profiles instead of a bigger core

The grammar stays small and durable because domain knowledge lives here, at the edge, and
versions independently. Supporting a new domain — brands, physical systems, motion —
means writing a new profile, not changing the language. A profile going out of date never
threatens the validity of past records written in the core grammar.

## Available profiles

- [`interface.v1`](interface.v1.md) — screen-based user interfaces and websites.

## Writing a new profile

Name it `‹domain›.v‹n›.md`. State its scope, list dimensions as evidence prompts with a
suggested derivation method, and include the standard reminder that every listed item is
optional and additive.
