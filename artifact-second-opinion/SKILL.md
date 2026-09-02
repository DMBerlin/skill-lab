---
name: artifact-second-opinion
description: >-
  Runs an independent writer-reviewer convergence loop on a written artifact
  using the active workspace's instructions, authoritative contracts, and
  bounded context. Use for design documents, specifications, ADRs, policies,
  instructions, skill text, and other prose contracts whose ambiguity would be
  expensive downstream. Not for code diffs.
---

# Artifact second opinion

## Purpose

A writer carries context that the artifact may not. An independent reviewer
sees only what a future reader will see and can expose missing assumptions,
contradictions, and ambiguous decisions.

This skill runs a writer-reviewer convergence loop. It discovers the active
workspace's governing context, gives an independent reviewer the artifact and
evidence without the writer's rationale, judges every finding, applies accepted
changes, and repeats until the reviewer verdicts GOLD with no standing dispute.

## Scope

Use this skill for written artifacts whose defects could cause incorrect or
costly downstream work, including:

- design proposals and technical specifications;
- architecture decision records and interface contracts;
- policies, operating procedures, and agent instructions;
- schema and reference documentation;
- reusable skills and prompt contracts.

Do not use it for code diffs. Use the workspace's code-review workflow instead.
Do not publish, commit, merge, approve, or otherwise cross a human gate unless
the user separately requests that action.

## Protocol

### 1. Establish the workspace contract

Before reviewing:

1. Identify the active workspace root and the artifact under review. If the
   artifact is not clear, ask the user instead of guessing.
2. Read the instruction files that apply to the artifact. Common locations
   include `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`,
   `.github/copilot-instructions.md`, `.github/instructions/`,
   `CONTRIBUTING.md`, and documents they reference.
3. Identify only the authoritative contracts needed to prove or disprove claims
   in the artifact, such as prior decisions, schemas, public interfaces,
   requirements, style guides, and implementation source files.
4. Establish the source-of-truth order from explicit workspace instructions and
   the artifact's purpose. If relevant sources conflict and the workspace does
   not settle precedence, ask the user.
5. Record the review boundary: included concerns, excluded concerns, and facts
   that remain unverified.

Keep grounding bounded. Do not read the whole workspace without a concrete
reason, follow unrelated references, or import assumptions from another
project. Do not read outside the active workspace unless the user explicitly
authorizes it or the artifact directly depends on an external public contract.

### 2. Spawn an independent reviewer

Spawn one review-only sub-agent with:

- a different model family, preferably from a different provider;
- a fresh context with no access to the writer's private rationale;
- the artifact path, workspace root, applicable instructions, authoritative
  contracts, source-of-truth order, and review boundary;
- an explicit instruction to cite exact files and sections for consistency
  claims and to report unverified claims instead of guessing.

If a cross-family reviewer is unavailable, use a fresh isolated context and
disclose the reduced independence in the final report.

GOLD means the artifact is shippable as-is: no blocker or major finding, no
material open question, and no finding that still requires an in-scope change.
Minor or nit suggestions may accompany GOLD only when explicitly non-blocking.

Require this output:

```text
## Verdict
GOLD | NEEDS-CHANGES

## Findings
Numbered; each:
[blocker|major|minor|nit] [confidence: high|medium|low]
- where: exact artifact location
- problem: the defect or ambiguity
- evidence: exact supporting source
- fix: smallest in-scope correction
- consequence: required for blocker/major findings
If none, write `None.`

## Questions
Ambiguities that cannot be settled from the supplied evidence.
If none, write `None.`
```

### 3. Judge every finding

Classify each finding before editing:

| Class | Meaning | Action |
|-------|---------|--------|
| Defect | The artifact is wrong, contradictory, or silent in a way that makes it incorrect or unusable. | Apply the smallest complete fix, or escalate if the fix exceeds scope or authority. |
| Context gap | The artifact permits a reasonable misreading because supporting context is missing. | Add the context needed to make the intended reading explicit. |
| Disputed | Citable authoritative evidence contradicts the finding. | Do not apply; cite the evidence and explain why. |
| Deferred | The finding may be valid, but its non-material benefit does not justify an in-scope change now. | Record the rationale, surface it to the reviewer and user, and escalate if the reviewer considers it material. |
| Scope suggestion | The idea may be useful but expands the artifact's agreed purpose. | Record it for the user; do not apply silently. |

Weigh evidence strength, expected downstream impact, interpretation risk,
reversibility, and the cost of the smallest in-scope fix. These are judgment
prompts, not numeric scores. Apply when leaving the problem is costlier than
fixing it. Clarify when a reasonable cold reader could reach the reviewer's
interpretation. Escalate decisions that depend on unstated priorities, product
values, risk tolerance, or authority. Use Deferred only for explicit,
non-material residual risk; it never overrides a blocker, major finding, or
material open question.

Never silently drop a finding.

### 4. Apply and return dispositions

The writer owns artifact edits. The reviewer never edits files. Address every
reviewer Question in the disposition report. An answer-only disposition is
valid only when it cites authoritative evidence already available to future
readers and the artifact is unambiguous. If a material Question depends on
writer-private context, add that context to the artifact or escalate it to the
user. An unanswered material Question blocks convergence.

Apply accepted changes, then give the reviewer a compact disposition report:

For example:

| # | Class | Rationale | Action |
|---|-------|-----------|--------|
| 1 | Defect | The artifact contradicts the cited contract. | Reworded the affected section. |
| 2 | Disputed | The cited source establishes the existing statement. | No edit. |

For a no-edit dispute, quote the authoritative evidence. Ask the reviewer to
re-read the updated artifact, explicitly address every disposition, and
re-assert any finding it still believes remains.

### 5. Converge

A review round is one reviewer report followed by the writer's dispositions and
any resulting edits. The initial reviewer report is round one. Full reviews and
targeted delta reviews both count toward the maximum of three reviewer rounds.

Repeat judgment, editing, and review until:

- the reviewer verdicts GOLD;
- no standing disputed finding remains;
- no blocker or major finding remains unresolved;
- no reasonable ambiguity with material downstream impact remains open in the
  reviewer's Questions section; and
- the reviewer explicitly addresses every disputed disposition.

Use these safeguards:

- Stop after three reviewer rounds and escalate residual disagreements or
  material Questions to the user.
- If only nit-level changes were applied, request a targeted delta review rather
  than another broad review. The targeted review still counts as a round, and a
  final reviewer GOLD is mandatory.
- If the reviewer changes to GOLD after push-back without addressing the
  argument, ask whether it accepts the evidence or is merely deferring.
- Do not broaden the artifact to satisfy scope suggestions without user
  approval.

### 6. Report the result

Report:

- the final verdict and number of full and targeted rounds, whose sum cannot
  exceed three;
- what was added, removed, or reworded in each round;
- every disputed finding and how it was resolved;
- unresolved or deferred decisions;
- whether cross-family review was available;
- the workspace instructions and contracts that governed the review.

GOLD means the independent readings converged. It does not replace an approval,
publication, commit, or release gate owned by a human or the workspace.

## Interpretation rules

- The active workspace defines domain language, architecture, style, and
  delivery rules. This skill supplies the review process, not project policy.
- Prefer explicit workspace instructions over conventions inferred from file
  names or technology labels.
- If no workspace style guide applies, preserve the artifact's established
  style and optimize for clarity, precision, and consistency.
- Treat missing evidence as uncertainty, not permission to invent facts.
- If a dispute exposes a reasonable alternate interpretation, change the
  artifact. At disposition time, a no-edit dispute requires an already
  unambiguous artifact and quoted authoritative evidence. If the reviewer
  re-asserts it, the dispute remains standing and blocks convergence until the
  reviewer withdraws it, the disputed passage changes, or the round cap
  escalates it to the user.
