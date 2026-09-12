---
name: artifact-second-opinion
description: >-
  Runs an independent writer-reviewer adversarial convergence loop on written
  artifacts using workspace instructions, authoritative contracts, and bounded
  evidence.
  Use when the user asks to: get a second opinion on a document, review an ADR,
  verify a technical specification, audit agent instructions, or stress-test a
  policy or skill text for ambiguity.
  Do NOT use for: code diffs or pull requests (use code review tools instead).
metadata:
  version: 2.0.0
  category: review
  tags: [review, convergence, adr, spec, verification]
---

# Artifact Second Opinion

## Objective
Subject a written artifact to an adversarial cold-reader review. An independent reviewer—isolated from the writer's internal assumptions—evaluates the artifact against authoritative workspace contracts, exposes ambiguities, and converges through a structured disposition loop until the artifact achieves a `GOLD` verdict.

---

## Scope & Non-Goals
- **In Scope:** Technical proposals, ADRs, interface contracts, agent instructions, policy documents, and schema specifications whose ambiguity would create expensive downstream defects.
- **Out of Scope:** Source code diffs. Do not publish, commit, or merge changes unless explicitly requested by the user.

---

## Protocol

### 1. Ground Workspace Contracts
1. Locate the artifact and active workspace root. Ask the user if the target artifact is unclear.
2. Read governing instruction files (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `CONTRIBUTING.md`).
3. Identify authoritative contracts: relevant schemas, prior decisions, interfaces, and source files.
4. Establish precedence: if sources conflict without an explicit rule, escalate to the user.
5. Establish bounds: do not read unreferenced project files or import external assumptions.

### 2. Spawn Independent Reviewer
Spawn one review-only agent with a fresh context containing only the artifact and cited contracts.

**Capability Fallback Matrix:**
- **Level 1 (Subagent Tool):** Invoke a dedicated reviewer subagent (`invoke_subagent` / `Task`), ideally using an alternate model family.
- **Level 2 (In-Thread Cold Reader):** If subagent tools are unavailable, isolate the prompt in a fresh context window.
- **Level 3 (User Export):** If execution is strictly bounded, format the reviewer prompt for the user to run externally.

Initialize the reviewer with the prompt and schema from [Reviewer Prompt Template](./references/reviewer-prompt.md).

### 3. Triage & Classify Findings
Classify every reviewer finding using the criteria in [Classification & Triage Matrix](./references/triage-matrix.md):
- `Defect`: Apply the smallest complete fix in-scope.
- `Context Gap`: Add minimal missing background to remove the ambiguity.
- `Disputed`: Do not edit. Cite authoritative contradictory workspace evidence.
- `Deferred`: Log minor, non-material issues. (Never defer blockers or major findings).
- `Scope Suggestion`: Record for user consideration; do not apply silently.

### 4. Apply Edits & Return Dispositions
- The writer applies edits. The reviewer never edits files directly.
- Address every reviewer finding and question in a structured disposition table.
- For disputed items, quote the authoritative evidence directly.
- See [Sample Multi-Round Disposition Log](./examples/disposition-log.md).

### 5. Converge (Max 3 Rounds)
Repeat the review-edit-disposition loop until:
- The reviewer returns `GOLD` (no blockers, major findings, or material questions remain).
- All disputed dispositions are explicitly resolved or withdrawn.
- **Hard Stop:** Stop after 3 reviewer rounds. If disagreements remain, escalate to the user.

### 6. Deliver Report
Report the final verdict, round count, summaries of edits made, resolutions of disputed points, and governing contracts.

---

## Resources & Deep References
- Reviewer system prompt & output schema: [Reviewer Prompt Template](./references/reviewer-prompt.md)
- Finding taxonomy & decision heuristics: [Triage Matrix](./references/triage-matrix.md)
- Concrete multi-round walkthrough: [Sample Disposition Log](./examples/disposition-log.md)
