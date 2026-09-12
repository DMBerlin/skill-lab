# Workspace Instructions: Skill Lab

This repository is a curated collection of agent skills maintained by humans through AI steering.
Any agent modifying or adding skills in this repository must adhere to the **SOTA Agent Skill Architecture** defined below.

---

## 1. Skill Architecture: The 3-Tier Rule

Every skill in `skills/<skill-name>/` must be strictly decoupled into three layers to optimize context windows, prompt caching, and progressive disclosure:

1. **Tier 1: Discovery & Routing (Frontmatter)**
   - Stored in the YAML frontmatter of `SKILL.md`.
   - The primary agent only reads `name` and `description` to decide whether to activate the skill.
   - Must contain rich triggers ("Use when user asks to..."), concrete action verbs, and negative triggers ("Do NOT use for...").
2. **Tier 2: Execution Runbook (`SKILL.md`)**
   - The core operational manual loaded when the skill activates.
   - Keep lean: **aim for ≤ 150 lines (under 1,000 tokens)**.
   - Contains: Role/Objective, Pre-requisites, Step-by-step phases, Verification gates, and relative markdown links to deep references.
   - Avoid embedding bulky prompts, large tables, or multi-paragraph background theory.
3. **Tier 3: On-Demand Depth (`references/` and `examples/`)**
   - Loaded by the agent only when necessary.
   - `references/`: Detailed rubrics, schemas, system prompts for subagents, domain specifications.
   - `examples/`: Realistic few-shot pairs (before/after transformations, canonical disposition logs).
   - `scripts/` (optional): Deterministic scripts for repetitive or mathematical operations.

---

## 2. Frontmatter Standard

Every `SKILL.md` must start with valid YAML frontmatter:

```yaml
---
name: <kebab-case-name>
description: >-
  <Summary of capability>.
  Use when the user asks to: <trigger 1>, <trigger 2>, <trigger 3>.
  Do NOT use for: <anti-trigger 1>, <anti-trigger 2>.
metadata:
  version: 1.0.0
  category: <workflow|editing|review|architecture|testing>
  tags: [<tag1>, <tag2>]
---
```

---

## 3. Memoization & Prompt Caching Rules

1. **Static Before Dynamic**: Place immutable rules, schemas, and instructions at the top. Never include dynamic timestamps, session IDs, or volatile data in skill documentation.
2. **Keyed Lists over ASCII Tables**: For LLM instruction prompts, prefer keyed bullet lists or compact YAML over large ASCII tables (`| --- | --- |`). They consume fewer tokens and prevent table-parsing hallucinations.
3. **Positive Substitution Patterns**: Avoid purely negative constraints (e.g., "never use X"). Always pair prohibitions with positive replacements (e.g., "Instead of X, use Y").
4. **Deterministic Spacing**: Use clean 2-space indentation and single blank lines between sections.

---

## 4. Portability & Fallback Protocol

Skills that leverage subagents or external tools must include a **Capability Fallback**:
- **Level 1 (Native Subagents)**: Invoke dedicated subagent or task runner.
- **Level 2 (In-Thread Roleplay)**: If subagents are unavailable, run an isolated cold-reader prompt in the existing thread.
- **Level 3 (User Export)**: If automated execution is not possible, emit the prompt for the user to run externally.

---

## 5. Adding a New Skill (Checklist)

When creating or modifying a skill:
1. Initialize folder structure: `skills/<name>/` with `SKILL.md`, `references/`, and `examples/` (or copy from `templates/SKILL_TEMPLATE/`).
2. Write rich, trigger-dense frontmatter.
3. Keep `SKILL.md` concise and modular.
4. Add at least one concrete few-shot example in `examples/`.
5. Run the validator:
   ```bash
   python3 scripts/validate_skills.py
   ```
