#!/usr/bin/env python3
"""
Skill Lab Validator
Validates agent skills against SOTA Progressive Disclosure, Frontmatter,
and Markdown standards.
"""

import sys
import re
from pathlib import Path

MAX_SKILL_LINES = 175
TRIGGER_KEYWORDS = ["when", "use", "trigger", "asks to"]

def parse_frontmatter(content: str):
    """Extract YAML frontmatter dictionary-like keys using regex."""
    if not content.startswith("---"):
        return None, "File does not begin with YAML frontmatter delimiter (---)."
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, "Unclosed YAML frontmatter."
    
    fm_text = parts[1]
    data = {}
    
    # Simple YAML key parser for basic string/block fields
    current_key = None
    buffer = []
    
    for line in fm_text.splitlines():
        key_match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", line)
        if key_match:
            if current_key:
                data[current_key] = " ".join(buffer).strip()
            current_key = key_match.group(1)
            val = key_match.group(2).strip()
            buffer = [val] if val and val not in (">-", ">", "|") else []
        elif current_key and line.startswith("  "):
            buffer.append(line.strip())
            
    if current_key:
        data[current_key] = " ".join(buffer).strip()
        
    return data, None

def validate_skill(skill_dir: Path):
    errors = []
    warnings = []
    
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"Missing SKILL.md in {skill_dir.name}")
        return errors, warnings
        
    content = skill_file.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    # 1. Line count check (Progressive disclosure)
    if len(lines) > MAX_SKILL_LINES:
        warnings.append(
            f"SKILL.md has {len(lines)} lines (recommended ≤ {MAX_SKILL_LINES}). "
            "Consider extracting schemas/prompts to references/."
        )
        
    # 2. Frontmatter validation
    fm, err = parse_frontmatter(content)
    if err:
        errors.append(f"Frontmatter error: {err}")
    else:
        name = fm.get("name", "")
        if not name:
            errors.append("Frontmatter missing required 'name' field.")
        elif not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", name):
            errors.append(f"Skill name '{name}' must be lowercase kebab-case.")
        elif name != skill_dir.name and skill_dir.name != "SKILL_TEMPLATE":
            warnings.append(f"Skill name '{name}' differs from directory name '{skill_dir.name}'.")
            
        desc = fm.get("description", "")
        if not desc:
            errors.append("Frontmatter missing required 'description' field.")
        else:
            if len(desc) < 60:
                warnings.append(f"Description is short ({len(desc)} chars). Add clear triggers and use-cases.")
            if not any(kw in desc.lower() for kw in TRIGGER_KEYWORDS):
                warnings.append("Description lacks trigger clauses (e.g. 'Use when user asks to...').")
                
    # 3. Fenced codeblock language check
    in_codeblock = False
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            if not in_codeblock:
                in_codeblock = True
                lang = line.strip()[3:].strip()
                if not lang:
                    warnings.append(f"Line {i}: Fenced code block missing language identifier.")
            else:
                in_codeblock = False
                
    # 4. Broken internal markdown links check
    link_matches = re.findall(r"\[.*?\]\((\./[^)]+)\)", content)
    for link in link_matches:
        target_path = skill_dir / link.split("#")[0]
        if not target_path.exists():
            errors.append(f"Broken relative link: '{link}' -> '{target_path.resolve()}' does not exist.")

    return errors, warnings

def main():
    repo_root = Path(__file__).resolve().parent.parent
    candidate_roots = [repo_root / "skills", repo_root / ".agents" / "skills"]
    skills = []
    
    for r in candidate_roots:
        if r.exists():
            skills.extend([p for p in r.iterdir() if p.is_dir() and not p.name.startswith(".")])
        
    if not skills:
        print("No skills found.")
        sys.exit(0)
        
    has_errors = False
    print(f"🔍 Validating {len(skills)} skills across workspace...\n")
    
    for skill_dir in sorted(skills, key=lambda p: p.name):
        errors, warnings = validate_skill(skill_dir)
        status = "❌ FAIL" if errors else ("⚠️  WARN" if warnings else "✅ PASS")
        print(f"[{status}] {skill_dir.name}")
        
        for w in warnings:
            print(f"  • [WARN] {w}")
        for e in errors:
            print(f"  • [ERROR] {e}")
            has_errors = True
            
    print("-" * 50)
    if has_errors:
        print("Validation failed with errors.")
        sys.exit(1)
    else:
        print("All skills validated successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
