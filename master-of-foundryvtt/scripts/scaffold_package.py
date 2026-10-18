#!/usr/bin/env python3
"""
Foundry VTT Module & System Scaffolder
======================================
Part of the Master of Foundry VTT Suite by GM Charles Corrêa.

Generates complete, production-ready directory scaffolds for Foundry VTT
systems and modules following v12 & v14 modern ApplicationV2 / TypeDataModel standards.
"""

import os
import sys
import json
import argparse

def create_module_scaffold(target_dir: str, package_id: str, title: str, author: str = "Author"):
    base_path = os.path.join(target_dir, package_id)
    os.makedirs(os.path.join(base_path, "scripts"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "templates"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "styles"), exist_ok=True)
    os.makedirs(os.path.join(base_path, "lang"), exist_ok=True)

    # module.json
    manifest = {
        "id": package_id,
        "title": title,
        "description": f"Custom production-ready module for Foundry VTT: {title}.",
        "version": "1.0.0",
        "compatibility": {
            "minimum": "12",
            "verified": "14"
        },
        "authors": [
            {
                "name": author
            }
        ],
        "esmodules": [
            f"scripts/{package_id}.mjs"
        ],
        "styles": [
            f"styles/{package_id}.css"
        ],
        "languages": [
            {
                "lang": "en",
                "name": "English",
                "path": "lang/en.json"
            },
            {
                "lang": "pt-BR",
                "name": "Português (Brasil)",
                "path": "lang/pt-BR.json"
            }
        ],
        "url": f"https://github.com/{author}/{package_id}",
        "manifest": f"https://github.com/{author}/{package_id}/releases/latest/download/module.json",
        "download": f"https://github.com/{author}/{package_id}/releases/latest/download/{package_id}.zip"
    }

    with open(os.path.join(base_path, "module.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    # scripts/module.mjs
    entrypoint = f"""// Module Entrypoint: {title}
const MODULE_ID = "{package_id}";

Hooks.once("init", async () => {{
  console.log(`[${{MODULE_ID}}] Initializing ${{MODULE_ID}} v1.0.0`);
  
  // Register settings safely
  game.settings.register(MODULE_ID, "enableFeature", {{
    name: `${{MODULE_ID}}.settings.enableFeature.name`,
    hint: `${{MODULE_ID}}.settings.enableFeature.hint`,
    scope: "world",
    config: true,
    type: Boolean,
    default: true
  }});
}});

Hooks.once("ready", async () => {{
  console.log(`[${{MODULE_ID}}] System & World Ready. Loaded for user:`, game.user.name);
}});
"""
    with open(os.path.join(base_path, "scripts", f"{package_id}.mjs"), "w", encoding="utf-8") as f:
        f.write(entrypoint)

    # lang/en.json
    en_lang = {
        package_id: {
            "title": title,
            "settings": {
                "enableFeature": {
                    "name": "Enable Core Features",
                    "hint": "Toggle the primary automated features of this module."
                }
            }
        }
    }
    with open(os.path.join(base_path, "lang", "en.json"), "w", encoding="utf-8") as f:
        json.dump(en_lang, f, indent=2, ensure_ascii=False)

    # lang/pt-BR.json
    pt_lang = {
        package_id: {
            "title": title,
            "settings": {
                "enableFeature": {
                    "name": "Habilitar Recursos Centrais",
                    "hint": "Ativa ou desativa as funcionalidades automatizadas principais deste módulo."
                }
            }
        }
    }
    with open(os.path.join(base_path, "lang", "pt-BR.json"), "w", encoding="utf-8") as f:
        json.dump(pt_lang, f, indent=2, ensure_ascii=False)

    # styles/module.css
    with open(os.path.join(base_path, "styles", f"{package_id}.css"), "w", encoding="utf-8") as f:
        f.write(f"/* CSS Styles for {title} */\n.{package_id} {{\n  box-sizing: border-box;\n}}\n")

    print(f"Scaffold successfully generated at: {base_path}")

def main():
    parser = argparse.ArgumentParser(description="Foundry VTT Scaffolder CLI")
    parser.add_argument("--id", required=True, help="Package ID (e.g. my-custom-module)")
    parser.add_argument("--title", required=True, help="Human readable title (e.g. My Custom Module)")
    parser.add_argument("--dest", default=".", help="Destination directory (defaults to current directory)")
    parser.add_argument("--author", default="Developer", help="Author name")
    args = parser.parse_args()

    create_module_scaffold(args.dest, args.id, args.title, args.author)

if __name__ == "__main__":
    main()
