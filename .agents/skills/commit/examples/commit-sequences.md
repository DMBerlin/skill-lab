# Commit Sequencing & Reversibility Examples

Atomic commits must be ordered from foundational layers to higher-order layers.
This allows clean rollbacks without breaking underlying dependencies.

---

## Example Sequence: Skill Architecture Refactor

### Commit 1 (Foundation / Tooling)
```text
chore(repo): add markdown and editor configuration

Establish base formatting rules with editorconfig and markdownlint.
```

### Commit 2 (Quality & Governance)
```text
feat(governance): add agent instructions and skill validation script

Introduce AGENTS.md rules and automated validator for progressive disclosure.
```

### Commit 3 (Templates)
```text
feat(templates): add sota skill authoring template

Provide canonical 3-tier structure template for authoring new skills.
```

### Commit 4 (Refactor Core Skills)
```text
refactor(skills): modularize humanize-prose and artifact-second-opinion

Extract deep schemas to references and few-shots to examples for 3-tier compliance.
```

### Commit 5 (Documentation)
```text
docs(readme): update repository documentation and skill index

Document 3-tier architecture, available skills, and authoring guidelines.
```
