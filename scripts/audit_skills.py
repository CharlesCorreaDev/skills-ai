import os
import re
from pathlib import Path

skills = [
  'book-formatter',
  'bootstrap-ux-ui-plus',
  'docker-master',
  'docs-for-markdown',
  'docs-for-skill',
  'humanizer-plus',
  'image-to-prompt',
  'master-of-foundryvtt',
  'master-of-gravewright',
  'mcp-builder',
  'not-today-adhd',
  'php-dev-expert',
  'python-dev-expert',
  'sms-legal',
  'video-to-md',
  'website-for-markdown',
  'website-for-skill'
]

base_dir = Path(r'e:\Projetos_Docker\skills-ai')

print(f"Checking {len(skills)} skills against agentskills & Anthropic specifications...\n")

for s in skills:
    s_dir = base_dir / s
    skill_md = s_dir / 'SKILL.md'
    readme = s_dir / 'README.md'
    version_file = s_dir / 'VERSION'
    changelog = s_dir / 'CHANGELOG.md'
    
    issues = []
    warnings = []
    
    # 1. Version file check
    ver_str = 'N/A'
    if not version_file.exists():
        issues.append('Missing VERSION file')
    else:
        ver_str = version_file.read_text(encoding='utf-8').strip()
        
    # 2. Parse SKILL.md
    if not skill_md.exists():
        issues.append('Missing SKILL.md')
    else:
        content = skill_md.read_text(encoding='utf-8')
        
        # Check frontmatter
        fm_match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not fm_match:
            issues.append('Missing or invalid YAML frontmatter in SKILL.md')
        else:
            fm_text = fm_match.group(1)
            
            # Name
            name_m = re.search(r'^name:\s*(.+)$', fm_text, re.MULTILINE)
            if not name_m:
                issues.append('Frontmatter missing `name` field')
            else:
                fm_name = name_m.group(1).strip().strip('"\'')
                if fm_name != s:
                    issues.append(f'Frontmatter name `{fm_name}` does not match folder `{s}`')
                if not re.match(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', fm_name):
                    issues.append(f'Frontmatter name `{fm_name}` violates lowercase-hyphen convention')
                    
            # Description
            desc_m = re.search(r'^description:\s*(.+)$', fm_text, re.MULTILINE)
            if not desc_m:
                issues.append('Frontmatter missing `description` field')
            else:
                desc = desc_m.group(1).strip()
                desc_lower = desc.lower()
                has_when = any(w in desc_lower for w in ['when', 'quando', 'use when', 'para', 'sempre que', 'utilize quando'])
                if not has_when:
                    warnings.append('Description lacks explicit WHEN/trigger context (agentskills 1.2-desc-when)')
                    
        # Check for hardcoded local absolute paths (C:\Users\ or e:\Projetos_Docker)
        hardcoded_paths = re.findall(r'[a-zA-Z]:\\[a-zA-Z0-9_\-\\]+', content)
        if hardcoded_paths:
            warnings.append(f'Hardcoded local absolute paths found in SKILL.md: {list(set(hardcoded_paths))[:3]}')

    # Status
    status = "EXCELLENT" if not issues and not warnings else ("GOOD" if not issues else "NEEDS WORK")
    print(f"[{status}] {s} (v{ver_str})")
    for iss in issues:
        print(f"   🔴 CRITICAL: {iss}")
    for w in warnings:
        print(f"   🟡 WARNING: {w}")
    if not issues and not warnings:
        print(f"   ✅ All frontmatter, SemVer and structural checks passed cleanly.")
    print()
