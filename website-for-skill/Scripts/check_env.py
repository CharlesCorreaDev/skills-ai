#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-platform environment & hardware budget check for 'website-for-skill'.
Verificação de ambiente e orçamento de hardware multiplataforma para a Skill 'website-for-skill'.
"""
import os
import platform
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_skill import find_skill_script, get_system_memory_info


def check_skill(skill_name):
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
        Path.home() / ".claude" / "skills" / skill_name,
    ]

    for p in possible_paths:
        if p.exists() and (p / "SKILL.md").exists():
            print(f"  ✅ Skill '{skill_name}' encontrada em: {p.resolve()}")
            return True

    print(f"  ❌ Skill '{skill_name}' NÃO encontrada.")
    return False


def main():
    mem = get_system_memory_info()
    print("=================================================================")
    print("🔍 Verificação de Ambiente & Hardware: Website For Skill")
    print(f"💻 OS: {platform.system()} | 🐍 Python: {sys.version.split()[0]}")
    print(f"🧠 RAM Disponível: {mem['avail_gb']} GB livres de {mem['total_gb']} GB ({mem['used_percent']}% em uso)")
    print("=================================================================\n")

    print("📦 Verificando Skills Dependentes (Obrigatórias):")
    docs_md_ok = check_skill("docs-for-markdown")
    website_md_ok = check_skill("website-for-markdown")

    scrape_script = find_skill_script("website-for-markdown", "scrape_to_md.py")
    if scrape_script:
        sys.path.insert(0, str(scrape_script.parent))
        try:
            from scrape_to_md import detect_hardware_budget
            budget = detect_hardware_budget()
            print("\n🖥️ Orçamento Adaptativo Calculado para a Máquina Operante:")
            print(f"  ├─ Processador : {budget['cpu_model']} ({budget['cpu_cores']} núcleos)")
            print(f"  ├─ Perfil Eco  : {budget['tier']}")
            print(f"  └─ Limite Auto : {budget['workers']} worker(s) | Lote: {budget['batch_size']} págs | Pausa: {budget['delay_ms']}ms")
        except Exception:
            pass

    print("\n-----------------------------------------------------------------")
    if docs_md_ok and website_md_ok:
        print("🎉 Todas as skills dependentes estão instaladas e prontas!")
        print("👉 Uso: python Scripts/build_skill.py <url> <nome_da_skill> [diretorio_saida] [--crawl]")
    else:
        print("⚠️ Verifique a presença das skills dependentes antes de prosseguir.")
    print("-----------------------------------------------------------------")


if __name__ == "__main__":
    main()
