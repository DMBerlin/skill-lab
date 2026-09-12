# Conventional Commit Types & Scopes

Use standard conventional commit prefixes with optional kebab-case scopes.

---

## 1. Allowed Types

- `feat`: A new skill, capability, or user-facing feature.
- `fix`: Bug fix, broken link repair, or correction to existing behavior.
- `refactor`: Structural changes that do not alter the external behavior or interface (e.g. modularizing a skill into 3-tier architecture).
- `docs`: Documentation changes only (e.g. README, guides, reference updates).
- `chore`: Maintenance, repository setup, configuration files, linters, or tooling.
- `style`: Formatting, whitespace, or layout adjustments that do not affect semantics.
- `test`: Adding or updating validation scripts, tests, or evaluation prompts.

---

## 2. Formatting Contract

```text
<type>(<scope>): <imperative subject>

<single-line body explaining rationale or context>
```

### Constraints
- **Subject line:** Under 72 characters, lowercase start, imperative mood ("add", "fix", "refactor", not "added", "fixing"), no trailing period.
- **Body:** Exactly one single line explaining the *why*. Do not include bullet lists, multi-line explanations, or empty fluff.
- **Trailers:** Strictly zero trailers (no `Co-authored-by:`, `Signed-off-by:`, etc.).
