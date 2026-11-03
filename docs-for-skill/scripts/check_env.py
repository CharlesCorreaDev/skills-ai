#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificação de ambiente multiplataforma para a Skill 'docs-for-skill'.
"""
import sys
import os
import platform
import shutil
import importlib.util

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def check_package(pkg, display):
    spec = importlib.util.find_spec(pkg)
    if spec:
        print(f"  ✅ {display}")
        return True
    print(f"  ❌ {display} NÃO instalado.")
    return False

def check_tool(tool, hints):
    if shutil.which(tool):
        print(f"  ✅ Ferramenta '{tool}' encontrada.")
        return True
    print(f"  ⚠️ '{tool}' não encontrada.")
    os_name = platform.system()
    hint = hints.get(os_name, hints.get("default", ""))
    if hint: print(f"     -> Instale com: {hint}")
    return False

def main():
    print("=========================================================")
    print("🔍 Verificação de Ambiente: Docs For Skill")
    print(f"💻 OS: {platform.system()} | 🐍 Python: {sys.version.split()[0]}")
    print("=========================================================\n")
    
    print("📦 Dependências Python (Herança da Docs For Markdown):")
    check_package("markitdown", "markitdown (Caso precise converter o documento base)")
    
    print("\n🛠️ Ferramentas de Sistema (Otimização de Estrutura):")
    tree_hints = {
        "Windows": "winget install GNU.tree  ou  choco install tree",
        "Darwin": "brew install tree",
        "Linux": "sudo apt-get install tree",
        "default": "Instale o utilitário 'tree' para visualizar a estrutura da skill."
    }
    check_tool("tree", tree_hints)
    
    gh_hints = {
        "Windows": "winget install GitHub.cli  ou  choco install gh",
        "Darwin": "brew install gh",
        "Linux": "sudo apt install gh",
        "default": "Instale o GitHub CLI (`gh`)."
    }
    gh_found = check_tool("gh", gh_hints)
    if gh_found:
        import subprocess
        try:
            res = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True, encoding="utf-8")
            if res.returncode == 0:
                print("  ✅ Conta do GitHub conectada com sucesso via `gh`!")
            else:
                print("  ⚠️ GitHub CLI instalado, mas NÃO autenticado. Execute `gh auth login` para conectar.")
        except Exception:
            pass
    
    print("\n✅ Verificação concluída. O ambiente está pronto para estruturar skills.")

if __name__ == "__main__":
    main()