---
name: humanize-prose
description: >-
  Humanizes and refines AI-drafted text, technical documents, proposals, and
  communications using William Zinsser's non-fiction writing principles:
  Clarity, Simplicity, Brevity, and Humanity.
  Use when the user asks to: de-slop prose, remove AI clichés, polish writing,
  tighten sentences, strip corporate buzzwords, or make writing sound natural.
  Do NOT use for: raw code diffs, structured JSON/YAML schemas, or log streams.
metadata:
  version: 1.1.0
  category: editing
  tags: [writing, style, humanize, prose, zinsser]
---

# Humanize Prose

## Objective
Transform synthetic, AI-generated drafts into clear, punchy, and natural prose by applying William Zinsser's four foundational principles of non-fiction writing.

---

## The Four Zinsser Principles

### Principle 1: Clarity (Clear Thinking Equals Clear Writing)
- **Direct Logic:** Each sentence must lead inescapably to the next. If a thought can be misinterpreted, rewrite it until it cannot.
- **Natural Formatting:**
  - Avoid bolding the opening phrase of every bullet item (`**Item:** description`). Write integrated, natural sentences.
  - Use sentence case for section headings (`## Core architecture`, not `## Core Architecture`).
- **Punctuation Balance:** Replace crutch em dashes (`—`) with periods for distinct thoughts, or commas and parentheses for subordinate clauses.
- **Preserve Technical Rigor:** Keep domain terminology, API interfaces, schema fields, and architecture components exact. Never sacrifice technical precision for casual style.

### Principle 2: Simplicity (Strip the Clutter)
- **Cut Jargon:** Remove corporate buzzwords and stereotypical LLM tells (`delve`, `leverage`, `tapestry`, `pivotal`, `beacon`, `foster`). Refer to [Banned Lexicon & Substitutions](./references/banned-lexicon.md).
- **Active Verbs:** Replace passive hedging and noun-heavy phrases with concrete, active verbs.
- **Dismantle Synthetic Formulas:**
  - Convert parallel negations (*"It is not just X, it is Y"*) directly into the core claim (*"It is Y"*).
  - Eliminate self-answering rhetorical questions (*"Why does this matter? Because..."*).
  - Drop the three-item list pattern when one or two points suffice.

### Principle 3: Brevity (Every Word Must Earn Its Place)
- **Delete Preamble:** Cut introductory throat-clearing (*"Let's dive in"*, *"Here is what you need to know"*, *"In summary"*). Start directly with the main idea in sentence one.
- **Deflate Significance Inflation:** Strip breathless qualifiers (*"marks a monumental milestone"*, *"serves as a testament to"*). State the facts and metrics plainly.
- **Prune Redundancy:** If sentence B repeats what sentence A already established, delete sentence B.

### Principle 4: Humanity (Warmth, Cadence, and Voice)
- **Rhythm & Burstiness:** Vary sentence length. Pair short, decisive statements with fluid, explanatory sentences.
- **Grounded Tone:** Write like a pragmatic peer: direct, honest, and relaxed. Avoid performative cheer, artificial enthusiasm, and excessive exclamation marks.
- **Zero Fabrication:** Never invent fictional anecdotes, metrics, or quotes to simulate personality.

---

## Execution Protocol

1. **Ingest & Extract:** Identify the core thesis, requirements, and technical assertions of the input text.
2. **Apply Principles:** Filter the text through all four principles simultaneously. For guidance on specific phrase swaps, inspect [Banned Lexicon & Substitutions](./references/banned-lexicon.md).
3. **Audit Against Verification Checklist:** Confirm the revision satisfies every check before delivery:
   - [ ] **Technical Fidelity:** All code tokens, command flags, schema attributes, and API names are preserved verbatim.
   - [ ] **Zero Lexicon Violations:** No terms from [Banned Lexicon & Substitutions](./references/banned-lexicon.md) (`delve`, `leverage`, `tapestry`, etc.) remain.
   - [ ] **Formula Purge:** No parallel negations (*"not just X, but Y"*), rhetorical self-questions, or crutch em dashes (`—`).
   - [ ] **Semantic Parity:** No technical caveats, error conditions, or core claims were dropped during condensation.
4. **Compare with Ground Truth:** Verify tone and cadence against [Transformation Examples](./examples/transformations.md).
5. **Deliver Clean Prose:** Return the revised text directly. Do not append meta-commentary, change logs, or conversational sign-offs unless the user explicitly requests them.

---

## Resources
- [Banned Lexicon & Substitutions](./references/banned-lexicon.md)
- [Transformation Examples (Before & After)](./examples/transformations.md)
