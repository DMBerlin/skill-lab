# Skill Lab

A curated collection of agent skills designed for autonomous, progressive-disclosure execution across AI agent environments (Google Antigravity, Claude Code, OpenAI Assistants, and Cursor/Copilot).

Maintained through human steering and AI pair-programming.

---

## 🏛️ SOTA Skill Architecture (The 3-Tier Model)

Every skill in this repository adheres to a strict 3-tier progressive disclosure model to maximize prompt cache hits, minimize context bloat, and ensure precise trigger routing:

1. **Tier 1: Discovery & Routing (Frontmatter)**
   - Stored in the YAML header of `SKILL.md`.
   - Injected into the agent's catalog index (~50–80 tokens).
   - Contains explicit trigger keywords, action verbs, and anti-triggers.

2. **Tier 2: Execution Runbook (`SKILL.md`)**
   - The active instructions loaded only upon skill invocation (≤ 150 lines).
   - Contains high-signal protocol phases, validation gates, and relative links to deep documentation.

3. **Tier 3: On-Demand Depth (`references/` and `examples/`)**
   - Read by the agent via file tools only when specifically needed.
   - `references/`: Subagent prompt templates, schemas, and classification matrices.
   - `examples/`: Canonical few-shot pairs and multi-round disposition logs.

---

## 📂 Repository Layout

```text
skill-lab/
├── .agents/
│   └── skills/
│       └── commit -> ../../skills/commit # Symlink for native workspace agent discovery
├── AGENTS.md                   # AI steering instructions for maintaining this repo
├── .editorconfig               # Whitespace, charset, and indentation standards
├── .markdownlint.json          # Markdown formatting rules
├── README.md                   # Repository overview & index
├── scripts/
│   └── validate_skills.py      # Automated linter for skills & progressive disclosure
├── templates/
│   └── SKILL_TEMPLATE/         # Canonical starting template for new skills
└── skills/
    ├── artifact-second-opinion/
    │   ├── SKILL.md            # Adversarial review convergence loop
    │   ├── references/         # Reviewer prompt & triage matrix
    │   └── examples/           # Multi-round disposition log
    ├── commit/
    │   ├── SKILL.md            # Atomic conventional commit protocol
    │   ├── references/         # Allowed types, scopes, and formatting
    │   └── examples/           # Dependency ordering and reversibility
    └── humanize-prose/
        ├── SKILL.md            # William Zinsser non-fiction writing principles
        ├── references/         # Banned AI slop catalog & substitutions
        └── examples/           # Before & after transformation pairs
```

---

## 🚀 Available Skills

| Skill | Category | Location | Trigger Summary |
| :--- | :--- | :--- | :--- |
| [`artifact-second-opinion`](./skills/artifact-second-opinion/SKILL.md) | `review` | `skills/` | Independent writer-reviewer convergence loop for ADRs, RFCs, specs, policies, and prompts. |
| [`humanize-prose`](./skills/humanize-prose/SKILL.md) | `editing` | `skills/` | Strips AI boilerplate, corporate buzzwords, and synthetic patterns using Zinsser principles. |
| [`commit`](./skills/commit/SKILL.md) | `workflow` | `skills/` | Creates atomic, conventional git commits ordered by layer with zero trailers. |

---

## 🛠️ Authoring New Skills

When adding a new skill to this lab:
1. Copy the boilerplate from `templates/SKILL_TEMPLATE/` into `skills/<your-skill-name>/`.
2. Ensure the frontmatter contains rich trigger clauses (`Use when user asks to:...`).
3. Keep `SKILL.md` under 150 lines by offloading prompts, schemas, and few-shots to `references/` and `examples/`.
4. Validate compliance:
   ```bash
   python3 scripts/validate_skills.py
   ```

All AI agents operating in this workspace automatically follow the governance rules in [`AGENTS.md`](./AGENTS.md).
