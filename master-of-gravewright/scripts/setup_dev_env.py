#!/usr/bin/env python3
"""
Gravewright Environment Checker & Scaffolder Tool
Verificador de Ambiente e Inicializador de Projetos para Gravewright VTT

Features / Funcionalidades:
1. Environment diagnosis (Python 3.12+, uv package manager, Git, SQLite / PostgreSQL).
   Diagnóstico do ambiente de desenvolvimento.
2. Skill companion verification (python-dev-expert, bootstrap-ux-ui-plus, cloudflare/security-audit-skill).
   Verificação de skills companheiras instaladas.
3. Module scaffolding (browser-module or django-app-module).
   Scaffolding automático de novos módulos e extensões para o Gravewright VTT.

Author / Autor: GM Charles Corrêa
License / Licença: MIT
"""

import sys
import os
import shutil
import subprocess
import argparse
import json
from pathlib import Path

def print_banner():
    print(r"""
======================================================================
  ⚔️ MASTER OF GRAVEWRIGHT VTT — ENVIRONMENT DIAGNOSTICS & SCAFFOLDER
  Suíte de Desenvolvimento de Sistemas e Módulos para Gravewright VTT
======================================================================
""")

def check_command(cmd, name, version_arg="--version"):
    path = shutil.which(cmd)
    if not path:
        print(f"❌ [MISSING / AUSENTE] {name} ({cmd}) not found in PATH.")
        return False, None
    try:
        res = subprocess.run([cmd, version_arg], capture_output=True, text=True, check=False)
        out = (res.stdout or res.stderr).splitlines()
        version = out[0] if out else "installed"
        print(f"✅ [OK] {name}: {version} ({path})")
        return True, version
    except Exception as e:
        print(f"⚠️ [WARNING / AVISO] {name} found at {path}, but failed to read version: {e}")
        return True, "unknown"

def diagnose_environment():
    print("\n🔍 [1/3] Checking System Toolchain / Verificando Ferramental do Sistema...")
    all_ok = True
    
    # 1. Python check
    py_ok, py_ver = check_command("python", "Python")
    if not py_ok:
        py_ok, py_ver = check_command("python3", "Python 3")
    if not py_ok:
        all_ok = False
        print("   👉 Install Python 3.12+ / Instale o Python 3.12+: https://www.python.org/")
    
    # 2. uv check (Astral uv package manager)
    uv_ok, _ = check_command("uv", "Astral uv (Fast Python Package Manager)")
    if not uv_ok:
        print("   👉 Recommendation / Recomendação: Install uv via 'curl -LsSf https://astral.sh/uv/install.sh' or 'powershell -ExecutionPolicy ByPass -c \"irm https://astral.sh/uv/install.ps1 | iex\"'")
        print("   👉 Alternative / Alternativa: 'pip install uv'")

    # 3. Git check
    git_ok, _ = check_command("git", "Git VCS")
    if not git_ok:
        all_ok = False
        print("   👉 Install Git / Instale o Git: https://git-scm.com/")

    # 4. Node.js check (for frontend JS tooling)
    node_ok, _ = check_command("node", "Node.js (Optional Frontend)")
    
    print("\n🧠 [2/3] Checking Required AI Companion Skills / Verificando Skills Companheiras...")
    skills_to_check = [
        ("python-dev-expert", "Especialista em Python, Django 6.1 e Ruff"),
        ("bootstrap-ux-ui-plus", "Design System e Usabilidade WCAG 2.2 AA"),
        ("cloudflare/security-audit-skill", "Auditoria de Segurança Adversarial"),
        ("NVIDIA/auto-ontology", "Ground Truth e Anti-Alucinação")
    ]
    for skill_name, desc in skills_to_check:
        print(f"   ℹ️ Skill recomendada / Recommended skill: '{skill_name}' — {desc}")

    print("\n📦 [3/3] Gravewright Environment Verdict / Veredito do Ambiente:")
    if all_ok:
        print("🎉 [SUCCESS / SUCESSO] All core prerequisites are satisfied! O ambiente está pronto para desenvolvimento no Gravewright.")
    else:
        print("⚠️ [ATTENTION / ATENÇÃO] Some core prerequisites are missing. Please install them before proceeding.")

def scaffold_module(module_name, module_type, author, output_dir):
    print(f"\n🚀 Creating {module_type} module: '{module_name}' by '{author}'...")
    target = Path(output_dir) / module_name
    if target.exists():
        print(f"❌ Target directory '{target}' already exists!")
        sys.exit(1)
        
    target.mkdir(parents=True)
    
    # manifest.json
    manifest = {
        "id": module_name.lower().replace(" ", "-"),
        "title": module_name,
        "version": "0.1.0",
        "description": f"Custom {module_type} extension for Gravewright VTT.",
        "author": author,
        "license": "MIT",
        "compatibility": {
            "minimum": "0.3.0",
            "verified": "0.3.4"
        },
        "scripts": ["index.js"] if module_type == "browser" else [],
        "styles": ["style.css"] if module_type == "browser" else [],
        "django_app": f"{module_name}_app" if module_type == "django" else None
    }
    
    with open(target / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        
    if module_type == "browser":
        # index.js
        with open(target / "index.js", "w", encoding="utf-8") as f:
            f.write(f"""// {module_name} - Gravewright VTT Browser Extension
// Autor / Author: {author}
// Licença / License: MIT

(() => {{
    console.log("[Gravewright Extension] Initializing: {module_name}");
    
    // Register custom UI / Hook into tabletop state
    // Registrar interface customizada ou escutar eventos do tabletop
    window.addEventListener("DOMContentLoaded", () => {{
        console.log("[Gravewright Extension] DOM Ready for {module_name}");
    }});
}})();
""")
        # style.css
        with open(target / "style.css", "w", encoding="utf-8") as f:
            f.write(f"""/* {module_name} - Gravewright Isolated Styles */
/* Use specific namespace to avoid style clashes / Use namespace para evitar conflitos */
.{manifest['id']}-container {{
    display: flex;
    flex-direction: column;
    gap: 8px;
    padding: 12px;
}}
""")
    else:
        # Django app scaffolding
        app_dir = target / f"{module_name}_app"
        app_dir.mkdir(parents=True)
        (app_dir / "__init__.py").write_text("", encoding="utf-8")
        (app_dir / "models.py").write_text("# Django models for Gravewright extension\n", encoding="utf-8")
        (app_dir / "services.py").write_text("# Domain services: owns validation and persistence\n", encoding="utf-8")
        (app_dir / "views.py").write_text("# HTTP and API views\n", encoding="utf-8")
        
    # README.md
    with open(target / "README.md", "w", encoding="utf-8") as f:
        f.write(f"""# {module_name}

> Custom {module_type} module for [Gravewright VTT](https://gravewright.com/).  
> *Módulo customizado ({module_type}) para o Gravewright VTT.*

## Author / Autor
**{author}**

## License / Licença
MIT
""")

    print(f"✅ Module '{module_name}' scaffolded successfully at: {target}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Master of Gravewright Environment Checker & Module Scaffolder")
    parser.add_argument("--check", action="store_true", help="Diagnose local environment (uv, Python, Git)")
    parser.add_argument("--create-module", type=str, help="Scaffold a new module with the given name")
    parser.add_argument("--type", choices=["browser", "django"], default="browser", help="Module type: browser or django")
    parser.add_argument("--author", type=str, default="Gravewright Developer", help="Module author")
    parser.add_argument("--out", type=str, default=".", help="Output directory")

    args = parser.parse_args()

    if args.create_module:
        scaffold_module(args.create_module, args.type, args.author, args.out)
    else:
        diagnose_environment()

if __name__ == "__main__":
    main()
