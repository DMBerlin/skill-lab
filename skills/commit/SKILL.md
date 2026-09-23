---
name: commit
description: >-
  Creates atomic, conventional git commits ordered by implementation layer
  with a single-line body and zero trailers to ensure clean reversibility.
  Use when the user asks to: commit changes, commit progress, save stage,
  make conventional commits, create atomic commits, or stage and commit work.
  Do NOT use for: pushing to remotes, merging branches, or tagging releases.
metadata:
  version: 1.0.0
  category: workflow
  tags: [git, commit, conventional-commits, atomic, maintainer]
---

# Commit

## Objective
Record repository modifications as clean, atomic, conventional git commits ordered by layer of dependency. Every commit must be easily reversible without leaving broken dependencies or orphan references.

---

## The Five Commit Invariants

1. **Conventional Format:** Use standard types (`feat`, `fix`, `refactor`, `docs`, `chore`, `style`, `test`) with optional scope: `<type>(<scope>): <subject>`. Subject must be imperative, lowercase, and without an ending period.
2. **Atomic Granularity:** Exactly one logical concern per commit. Never mix configuration changes with business logic or documentation updates.
3. **Zero Trailers:** Strictly omit trailers (no `Co-authored-by:`, `Signed-off-by:`, or issue metadata). Author and signature are handled natively by git config and GPG keys.
4. **Single-Line Body:** If a body is needed, format it as subject, blank line, and exactly one single sentence explaining the *why*. Never use bullet points or multi-line bodies.
5. **Implementation-Order Sequencing:** Sequence commits from foundational layers to higher-order layers (tooling/config -> governance/core -> implementations/skills -> docs/meta). This guarantees that reverting a higher commit cleanly unrolls without corrupting foundations.

---

## Execution Protocol

### 1. Audit Working State
1. Run `git status -u` and `git diff` to inspect all staged, unstaged, and untracked files.
2. Group files into distinct, atomic logical chunks.

### 2. Sequence Dependencies
Order the atomic chunks chronologically by dependency layer:
- **Layer 1 (Infra / Config):** `.editorconfig`, `.gitignore`, linter configs, base tooling.
- **Layer 2 (Governance / Scripts):** Work instructions, validator scripts, templates.
- **Layer 3 (Features / Skills):** Core skills, refactored skills, supporting references.
- **Layer 4 (Documentation):** `README.md`, top-level release notes.

See [Commit Sequences](./examples/commit-sequences.md) for sequence patterns.

### 3. Stage & Commit Atomically
For each atomic chunk in sequence:
1. Stage only the files belonging to the specific chunk:
   ```bash
   git add <file1> <file2>
   ```
2. Commit using the strict format (consult [Conventional Types](./references/conventional-types.md)):
   ```bash
   git commit -m "<type>(<scope>): <subject>" -m "<single-line explanation of why>"
   ```
3. **Hook Failure Recovery:** If a pre-commit hook or linter fails, resolve the reported code or formatting issue directly and re-stage. Never bypass hooks with `--no-verify` unless the user explicitly commands it.

### 4. Verify History & Working Tree
1. Confirm that commits were created cleanly and signed:
   ```bash
   git log -n <count> --oneline --show-signature
   ```
2. Confirm the working tree is in the expected state with zero unintended leftovers:
   ```bash
   git status --porcelain
   ```

---

## Reference Pointers
- Type and scope definitions: [Conventional Types & Scopes](./references/conventional-types.md)
- Dependency sequencing examples: [Commit Sequences](./examples/commit-sequences.md)
