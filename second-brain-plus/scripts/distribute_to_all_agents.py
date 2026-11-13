#!/usr/bin/env python3
"""
distribute_to_all_agents.py - Universal Multi-Agent Skill & Command Distributor
Distribuidor Universal de Skills, Comandos e Workflows para Todos os Agentes de IA.

Deploys second-brain-plus to:
- Google Antigravity / Gemini (~/.gemini)
- Claude Code (~/.claude)
- OpenAI Codex (~/.codex)
- GitHub Copilot CLI (~/.copilot)
- Cursor IDE (~/.cursor)
- Universal Agents (~/.agents)
- OpenCode (~/.opencode)
- Hermes Agent (~/.hermes)
- Ollama (~/.ollama)

Bilingual support: English (EN) and Portuguese (PT-BR).
Suporte bilíngue: Inglês (EN) e Português (PT-BR).
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

AGENT_ROOTS = [
    ".gemini",
    ".claude",
    ".codex",
    ".copilot",
    ".cursor",
    ".agents",
    ".opencode",
    ".hermes",
    ".ollama"
]

def make_junction_or_copy(source: Path, target: Path):
    """
    EN: Create a Directory Junction on Windows (or symlink/copy fallback).
    PT-BR: Cria uma Junction no Windows (ou fallback de link simbólico/cópia).
    """
    if target.exists() or target.is_symlink():
        try:
            if target.is_dir() and not target.is_symlink():
                shutil.rmtree(target)
            else:
                target.unlink()
        except Exception:
            # Fallback to rmdir if junction
            subprocess.run(f'cmd /c rmdir "{target}"', shell=True, capture_output=True)

    target.parent.mkdir(parents=True, exist_ok=True)
    
    # Try Windows directory junction first
    res = subprocess.run(f'cmd /c mklink /J "{target}" "{source}"', shell=True, capture_output=True)
    if res.returncode == 0:
        return True
    
    # Fallback to recursive copy
    try:
        shutil.copytree(source, target)
        return True
    except Exception as e:
        print(f"    ⚠️ Warning: Could not link/copy to {target}: {e}")
        return False

def deploy_to_all_agents():
    home = Path.home()
    source_skill = Path(__file__).resolve().parent.parent
    source_workflows = source_skill / "workflows"

    print("=" * 70)
    print("🌐 UNIVERSAL AI AGENT DEPLOYMENT / DISTRIBUIÇÃO UNIVERSAL MULTI-AGENTE")
    print(f"   Origem da Skill: {source_skill}")
    print("=" * 70 + "\n")

    success_count = 0

    for agent_dir_name in AGENT_ROOTS:
        agent_dir = home / agent_dir_name
        if not agent_dir.exists():
            continue

        print(f"📦 [Agente] Processando '{agent_dir_name}' em {agent_dir}...")

        # 1. Target skills folders (standard and config/skills if gemini)
        skill_targets = [agent_dir / "skills"]
        if agent_dir_name == ".gemini":
            skill_targets.append(agent_dir / "config" / "skills")

        for s_base in skill_targets:
            s_base.mkdir(parents=True, exist_ok=True)
            # Main skill
            ok1 = make_junction_or_copy(source_skill, s_base / "second-brain-plus")
            # Aliases
            ok2 = make_junction_or_copy(source_skill, s_base / "second-brain")
            ok3 = make_junction_or_copy(source_skill, s_base / "tdah")
            if ok1:
                print(f"  ✓ Skills instaladas em: {s_base.relative_to(home)}")

        # 2. Target commands & workflows folders
        command_targets = [
            agent_dir / "commands",
            agent_dir / "workflows",
            agent_dir / "config" / "workflows"
        ]
        if agent_dir_name == ".gemini":
            command_targets.append(agent_dir / "antigravity" / "commands")

        for c_base in command_targets:
            c_base.mkdir(parents=True, exist_ok=True)
            if source_workflows.exists():
                for wf in source_workflows.glob("*.md"):
                    target_file = c_base / wf.name
                    target_file.write_text(wf.read_text(encoding="utf-8"), encoding="utf-8")
        
        print(f"  ✓ Comandos (/second-brain e /tdah) sincronizados em '{agent_dir_name}'.")
        success_count += 1

    # Also deploy to local project .agents if in a repo
    cwd_agents = Path.cwd() / ".agents"
    if cwd_agents.exists() or Path.cwd().name == "skills-ai":
        cwd_agents.mkdir(parents=True, exist_ok=True)
        make_junction_or_copy(source_skill, cwd_agents / "skills" / "second-brain-plus")
        make_junction_or_copy(source_skill, cwd_agents / "skills" / "second-brain")
        make_junction_or_copy(source_skill, cwd_agents / "skills" / "tdah")
        (cwd_agents / "commands").mkdir(parents=True, exist_ok=True)
        (cwd_agents / "workflows").mkdir(parents=True, exist_ok=True)
        for wf in source_workflows.glob("*.md"):
            (cwd_agents / "commands" / wf.name).write_text(wf.read_text(encoding="utf-8"), encoding="utf-8")
            (cwd_agents / "workflows" / wf.name).write_text(wf.read_text(encoding="utf-8"), encoding="utf-8")
        print("  ✓ Sincronizado no workspace local (.agents).")

    print("\n" + "=" * 70)
    print(f"✅ SUCESSO! Distribuído para {success_count} agentes de IA instalados.")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    deploy_to_all_agents()
