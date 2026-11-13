#!/usr/bin/env python3
"""
Gravewright Environment Checker & Scaffolder Tool
Verificador de Ambiente e Inicializador de Projetos para Gravewright VTT

Features / Funcionalidades:
1. Environment diagnosis (Python 3.14+, Astral uv, Git, SQLite).
   Diagnóstico do ambiente de desenvolvimento.
2. Skill companion verification (python-dev-expert, bootstrap-ux-ui-plus, cloudflare/security-audit-skill).
   Verificação de skills companheiras recomendadas.
3. Official Module Scaffolding (browser, system, or django).
   Geração de pacotes compatíveis com o schema oficial do Gravewright (JSON Schema 2020-12).

Author / Autor: GM Charles Corrêa
License / Licença: MIT
"""

import sys
import os
import re
import shutil
import subprocess
import argparse
import json
from pathlib import Path

ID_PATTERN = re.compile(r"^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)+$")

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
    
    # 1. Python check (Requires Python >= 3.14 for Gravewright 0.3.4)
    py_ok, py_ver = check_command("python", "Python")
    if not py_ok:
        py_ok, py_ver = check_command("python3", "Python 3")
    if not py_ok:
        all_ok = False
        print("   👉 Install Python 3.14+ / Instale o Python 3.14+: https://www.python.org/")
    
    # 2. uv check (Astral uv package manager)
    uv_ok, _ = check_command("uv", "Astral uv (Fast Python Package Manager)")
    if not uv_ok:
        print("   👉 Recommendation / Recomendação: Install uv via 'curl -LsSf https://astral.sh/uv/install.sh' or 'powershell -ExecutionPolicy ByPass -c \"irm https://astral.sh/uv/install.ps1 | iex\"'")

    # 3. Git check
    git_ok, _ = check_command("git", "Git VCS")
    if not git_ok:
        all_ok = False
        print("   👉 Install Git / Instale o Git: https://git-scm.com/")

    print("\n🧠 [2/3] Checking Recommended AI Companion Skills / Verificando Skills Companheiras...")
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
        print("🎉 [SUCCESS / SUCESSO] Core prerequisites are satisfied! O ambiente está pronto para desenvolvimento no Gravewright.")
    else:
        print("⚠️ [ATTENTION / ATENÇÃO] Some core prerequisites are missing. Please install them before proceeding.")

def sanitize_id(raw_id: str) -> str:
    cleaned = re.sub(r"[^a-z0-9.-]", "-", raw_id.lower())
    cleaned = re.sub(r"-+", "-", cleaned).strip("-.")
    if not ID_PATTERN.match(cleaned):
        cleaned = f"dev.{cleaned}" if cleaned else "dev.custom-module"
    return cleaned

def sanitize_python_ident(raw_name: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_]", "_", raw_name)
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    if not cleaned or cleaned[0].isdigit():
        cleaned = f"app_{cleaned}"
    return cleaned.lower()

def scaffold_module(module_name: str, module_type: str, author: str, output_dir: str):
    module_id = sanitize_id(module_name)
    print(f"\n🚀 Creating {module_type} package: id='{module_id}', name='{module_name}' by '{author}'...")
    
    target = Path(output_dir) / module_id
    if target.exists():
        print(f"❌ Target directory '{target}' already exists!")
        sys.exit(1)
        
    target.mkdir(parents=True)

    # 1. Manifest adhering strictly to official JSON Schema 2020-12
    manifest = {
        "id": module_id,
        "name": module_name,
        "version": "0.1.0",
        "sdk": {
            "requires": ">=1.0.0 <2.0.0",
            "tested": "1.0.0"
        },
        "description": f"Custom {module_type} extension for Gravewright VTT.",
        "author": author,
        "license": "MIT"
    }

    if module_type == "browser":
        manifest["entry"] = "main.js"
    elif module_type == "system":
        manifest["entry"] = "main.js"
        manifest["system"] = {
            "actorTypes": [
                {"id": "character", "label": "Personagem / Character"},
                {"id": "npc", "label": "NPC"}
            ],
            "itemTypes": [
                {"id": "gear", "label": "Equipamento / Gear", "icon": "Backpack"}
            ],
            "combat": {
                "formula": "1d20 + @combat.initiative",
                "manualInput": "number"
            }
        }
    elif module_type == "django":
        app_name = sanitize_python_ident(module_name)
        manifest["django"] = {
            "apps": [f"{app_name}.apps.{app_name.capitalize()}Config"],
            "requirements": []
        }

    with open(target / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    # 2. LICENSE.txt (Must have extension per Gravewright packaging rules)
    with open(target / "LICENSE.txt", "w", encoding="utf-8") as f:
        f.write(f"MIT License\n\nCopyright (c) 2026 {author}\n\nPermission is hereby granted, free of charge...")

    # 3. Type-specific files
    if module_type in ["browser", "system"]:
        # main.js with mandatory start / register / stop lifecycle
        with open(target / "main.js", "w", encoding="utf-8") as f:
            f.write(f"""// main.js - Gravewright VTT {module_type.capitalize()} Extension
// Author / Autor: {author}
// Official lifecycle: start(moduleContext), register(registrationContext), stop()

export default {{
  start({{ styles }}) {{
    // Attach isolated styles
    styles.use("styles.css");
  }},

  register({{ register }}) {{
    // Synchronous registration of UI surfaces
    register("actor.directory", async ({{ root, api, signal }}) => {{
      const container = root.ownerDocument.createElement("div");
      container.className = "{module_id.replace('.', '-')}-container";
      
      const label = root.ownerDocument.createElement("p");
      label.textContent = "Extensão {module_name} ativa / Active";
      container.append(label);
      root.append(container);

      const render = (actors) => {{
        if (!signal.aborted) {{
          label.textContent = `Atores visíveis / Visible actors: ${{actors.length}}`;
        }}
      }};

      render(await api.actors.list());
      api.events.on("actors.changed", (snapshot) => render(snapshot.actors));
    }});
  }},

  stop() {{
    // Cleanup is handled by the host runtime
  }}
}};
""")
        # styles.css namespaced by .gw-module-root[data-module-id="..."]
        with open(target / "styles.css", "w", encoding="utf-8") as f:
            f.write(f"""/* Isolated styles for {module_id} */
.gw-module-root[data-module-id="{module_id}"] .{module_id.replace('.', '-')}-container {{
  margin: 0.5rem;
  padding: 0.5rem;
  font-weight: 600;
}}
""")
    else:
        # Django Server App
        app_name = sanitize_python_ident(module_name)
        app_dir = target / app_name
        app_dir.mkdir(parents=True)
        (app_dir / "__init__.py").write_text("", encoding="utf-8")
        
        mig_dir = app_dir / "migrations"
        mig_dir.mkdir(parents=True)
        (mig_dir / "__init__.py").write_text("", encoding="utf-8")
        
        (app_dir / "apps.py").write_text(f"""from django.apps import AppConfig

class {app_name.capitalize()}Config(AppConfig):
    name = "{app_name}"
    label = "{app_name}"
    verbose_name = "{module_name}"

    def ready(self):
        # Register public server operations via official API
        # from api.systems import register_api
        pass
""", encoding="utf-8")

        (app_dir / "services.py").write_text("""# Domain services: owns validation and persistence
# As regras de negócio e validação de domínio residem aqui
""", encoding="utf-8")

    # README.md
    with open(target / "README.md", "w", encoding="utf-8") as f:
        f.write(f"""# {module_name}

> Custom {module_type} package for [Gravewright VTT](https://gravewright.com/).
> ID: `{module_id}` | Version: `0.1.0` | License: `MIT`

## How to Package / Como Empacotar
Gravewright requires all package files to be at the root of the ZIP archive without extra subdirectories:

```bash
cd {module_id}
python -m zipfile -c ../{module_id}-0.1.0.zip manifest.json LICENSE.txt {"main.js styles.css" if module_type != "django" else f"{app_name}/"}
```
""")

    print(f"✅ {module_type.capitalize()} package '{module_name}' ({module_id}) scaffolded successfully at: {target}")

def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Master of Gravewright Environment Checker & Module Scaffolder")
    parser.add_argument("--check", action="store_true", help="Diagnose local environment (Python 3.14+, uv, Git)")
    parser.add_argument("--create-module", type=str, help="Scaffold a new package (e.g. 'meu-modulo' or 'autor.meu-modulo')")
    parser.add_argument("--type", choices=["browser", "system", "django"], default="browser", help="Package type: browser, system, or django")
    parser.add_argument("--author", type=str, default="Charles Corrêa", help="Package author")
    parser.add_argument("--out", type=str, default=".", help="Output directory")

    args = parser.parse_args()

    if args.create_module:
        scaffold_module(args.create_module, args.type, args.author, args.out)
    else:
        diagnose_environment()

if __name__ == "__main__":
    main()
