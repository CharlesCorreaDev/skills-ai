#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificação de ambiente multiplataforma para a Skill 'website-for-skill'.
Garante que as skills dependentes ('docs-for-markdown' e 'website-for-markdown') estão disponíveis.
"""
import sys
import os
import platform
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def check_skill(skill_name):
    # Procura no repositório atual, diretórios pais e pastas globais de skills
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parents[1]
    
    possible_paths = [
        repo_root / skill_name,
        script_dir.parent.parent / skill_name,
        Path.cwd() / skill_name,
        Path.cwd().parent / skill_name,
        Path.cwd() / "skills" / skill_name,
        Path.home() / ".agents" / "skills" / skill_name,
        Path.home() / ".gemini" / "config" / "skills" / skill_name,
        Path.home() / ".copilot" / "skills" / skill_name,
        Path.home() / ".claude" / "skills" / skill_name
    ]
    
    for p in possible_paths:
        if p.exists() and (p / "SKILL.md").exists():
            print(f"  ✅ Skill '{skill_name}' encontrada em: {p.resolve()}")
            return True
            
    print(f"  ❌ Skill '{skill_name}' NÃO encontrada.")
    print(f"     -> Certifique-se de que '{skill_name}' está presente no repositório ou no diretório de skills.")
    return False

def main():
    print("=========================================================")
    print("🔍 Verificação de Ambiente: Website For Skill")
    print(f"💻 OS: {platform.system()} | 🐍 Python: {sys.version.split()[0]}")
    print("=========================================================\n")
    
    print("📦 Verificando Skills Dependentes (Obrigatórias):")
    docs_md_ok = check_skill("docs-for-markdown")
    website_md_ok = check_skill("website-for-markdown")
    
    print("\n---------------------------------------------------------")
    if docs_md_ok and website_md_ok:
        print("🎉 Todas as skills dependentes estão instaladas e prontas!")
        print("👉 Você pode usar: python Scripts/build_skill.py <url> <nome_da_skill> [diretorio_saida] [--crawl]")
    else:
        print("⚠️ Verifique a presença das skills dependentes antes de prosseguir.")
    print("---------------------------------------------------------")

if __name__ == "__main__":
    main()