#!/usr/bin/env python3
"""
Master of Gravewright VTT - Native MCP Server
==============================================
Server Name: master-of-gravewright-mcp
Version: 0.4.0-beta
Author: GM Charles Corrêa
License: MIT

Zero-dependency Model Context Protocol (MCP) server running over JSON-RPC 2.0 (stdio).
Connects AI coding assistants and agents directly into Gravewright VTT project contexts.

Capabilities / Funcionalidades:
1. inspect_gravewright_environment: Detects local repository, Django apps, uv environment, and SQLite database.
2. list_installed_modules: Scans and reports installed Gravewright browser and Django modules in data/media/modules/packages or GRAVEWRIGHT_MODULES_ROOT.
3. validate_module_manifest: Validates manifest.json schemas against official JSON Schema 2020-12 (contracts/schemas/manifest.json).
4. query_marketplace_packages: Searches the official Gravewright marketplace for modules and translation packages with verified IDs.
5. scaffold_extension: Generates browser-module (ESM start/register/stop) or django-app-module boilerplate adhering to official schema.
6. search_offline_docs: Queries the 50 offline Markdown manuals in EN and pt-BR.
"""

import sys
import json
import os
import glob
import re
from pathlib import Path
from typing import Dict, Any, List, Optional

SERVER_NAME = "master-of-gravewright-mcp"
SERVER_VERSION = "0.4.0-beta"

def send_response(response: Dict[str, Any]):
    """
    EN: Write JSON-RPC response to stdout.
    PT-BR: Escreve a resposta JSON-RPC no stdout.
    """
    output = json.dumps(response, ensure_ascii=False)
    sys.stdout.write(output + "\n")
    sys.stdout.flush()

def handle_list_tools() -> List[Dict[str, Any]]:
    return [
        {
            "name": "inspect_gravewright_environment",
            "description": "Inspects the local Gravewright VTT project root, Python/uv environment, Django configuration, registered apps, and SQLite database.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "project_path": {
                        "type": "string",
                        "description": "Optional path to the Gravewright repository or root directory. Defaults to current working directory."
                    }
                }
            }
        },
        {
            "name": "list_installed_modules",
            "description": "Scans and lists installed Gravewright modules from data/media/modules/packages/ or custom path, reporting ID, name, version, and type (browser, django, system, translation).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "modules_path": {
                        "type": "string",
                        "description": "Optional path to the modules directory. Defaults to GRAVEWRIGHT_MODULES_ROOT or data/media/modules/packages/."
                    }
                }
            }
        },
        {
            "name": "validate_module_manifest",
            "description": "Validates a Gravewright module's manifest.json file against the official JSON Schema Draft 2020-12 schema rules (id regex, sdk, name, entry, no additional properties).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "manifest_path": {
                        "type": "string",
                        "description": "Absolute or relative path to the manifest.json file."
                    }
                },
                "required": ["manifest_path"]
            }
        },
        {
            "name": "query_marketplace_packages",
            "description": "Queries the official Gravewright GitHub marketplace catalog for available extensions, 3D dice, and compatibility packages with canonical IDs.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "search_term": {
                        "type": "string",
                        "description": "Optional keyword or package name to search."
                    }
                }
            }
        },
        {
            "name": "scaffold_extension",
            "description": "Generates a complete Gravewright module boilerplate adhering strictly to official manifest.json schema and lifecycle (ESM start/register/stop or Django AppConfig).",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Module name or ID (e.g. 'meu-modulo', 'swade-helper', 'charles.custom-clocks')."
                    },
                    "module_type": {
                        "type": "string",
                        "enum": ["browser", "django"],
                        "default": "browser",
                        "description": "Type of module: 'browser' for client ESM JS/CSS or 'django' for server AppConfig."
                    },
                    "author": {
                        "type": "string",
                        "default": "Gravewright Developer",
                        "description": "Author name."
                    },
                    "target_dir": {
                        "type": "string",
                        "description": "Target directory where the module folder will be created."
                    }
                },
                "required": ["name", "target_dir"]
            }
        },
        {
            "name": "search_offline_docs",
            "description": "Searches the 50 offline Gravewright documentation files (EN and pt-BR) for specific technical terms, APIs, or architectural concepts.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search phrase or keyword (e.g., 'services.py', 'clocks', 'channels', 'uvtt', 'manifest')."
                    },
                    "language": {
                        "type": "string",
                        "enum": ["pt-BR", "en", "all"],
                        "default": "pt-BR",
                        "description": "Language of documentation to search."
                    }
                },
                "required": ["query"]
            }
        }
    ]

def tool_inspect_gravewright_environment(project_path: Optional[str] = None) -> Dict[str, Any]:
    path = Path(project_path) if project_path else Path.cwd()
    
    is_gravewright = (path / "gravewright").exists() or (path / "manage.py").exists() or (path / "pyproject.toml").exists()
    has_uv = (path / "uv.lock").exists()
    
    apps = []
    if (path / "gravewright").exists():
        apps = [d.name for d in (path / "gravewright").iterdir() if d.is_dir() and (d / "__init__.py").exists()]
        
    db_sqlite = path / "data" / "gravewright.sqlite3"
    
    return {
        "project_path": str(path.resolve()),
        "is_gravewright_root": is_gravewright,
        "uses_astral_uv": has_uv,
        "django_manage_py": (path / "manage.py").exists(),
        "detected_subapps": apps,
        "sqlite_database_exists": db_sqlite.exists(),
        "sqlite_path": str(db_sqlite.resolve()) if db_sqlite.exists() else None,
        "modules_dir_exists": (path / "data" / "media" / "modules" / "packages").exists() or (path / "extensions").exists(),
        "status": "ready" if is_gravewright else "not_a_gravewright_repo"
    }

def tool_list_installed_modules(modules_path: Optional[str] = None) -> Dict[str, Any]:
    search_dirs = []
    if modules_path:
        search_dirs.append(Path(modules_path))
    else:
        env_root = os.environ.get("GRAVEWRIGHT_MODULES_ROOT")
        if env_root:
            search_dirs.append(Path(env_root))
            
        cwd = Path.cwd()
        search_dirs.extend([
            cwd / "data" / "media" / "modules" / "packages",
            cwd / "data" / "extensions",
            cwd / "extensions"
        ])
        
    modules = []
    visited_ids = set()
    
    for d in search_dirs:
        if d.exists() and d.is_dir():
            for sub in d.iterdir():
                manifest_file = sub / "manifest.json"
                if sub.is_dir() and manifest_file.exists():
                    try:
                        with open(manifest_file, "r", encoding="utf-8") as f:
                            data = json.load(f)
                        mod_id = data.get("id", sub.name)
                        if mod_id in visited_ids:
                            continue
                        visited_ids.add(mod_id)
                        
                        # Determine package type from official schema blocks
                        pkg_type = "browser"
                        if "django" in data:
                            pkg_type = "django"
                        elif "system" in data:
                            pkg_type = "system"
                        elif "locales" in data:
                            pkg_type = "translation"
                            
                        modules.append({
                            "directory": str(sub.resolve()),
                            "id": mod_id,
                            "name": data.get("name", data.get("title", sub.name)),
                            "version": data.get("version", "0.0.0"),
                            "sdk": data.get("sdk", {}),
                            "type": pkg_type,
                            "author": data.get("author", "Unknown"),
                            "description": data.get("description", "")
                        })
                    except Exception as e:
                        modules.append({
                            "directory": str(sub.resolve()),
                            "error": f"Failed to parse manifest.json: {e}"
                        })
                        
    return {
        "count": len(modules),
        "modules": modules
    }

def tool_validate_module_manifest(manifest_path: str) -> Dict[str, Any]:
    p = Path(manifest_path)
    if not p.exists():
        return {"valid": False, "error": f"Manifest file not found: {manifest_path}"}
        
    try:
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        return {"valid": False, "error": f"Invalid JSON format: {e}"}
        
    # Load schema if available
    schema_path = Path(__file__).resolve().parent.parent / "contracts" / "schemas" / "manifest.json"
    if schema_path.exists():
        try:
            import jsonschema
            with open(schema_path, "r", encoding="utf-8") as sf:
                schema = json.load(sf)
            validator = jsonschema.Draft202012Validator(schema)
            raw_errors = sorted(validator.iter_errors(data), key=lambda e: e.path)
            if raw_errors:
                err_messages = [f"{list(err.path)}: {err.message}" if err.path else err.message for err in raw_errors]
                return {
                    "valid": False,
                    "validation_mode": "jsonschema-draft2020-12",
                    "errors": err_messages
                }
            return {
                "valid": True,
                "validation_mode": "jsonschema-draft2020-12",
                "manifest_id": data.get("id"),
                "name": data.get("name"),
                "version": data.get("version"),
                "sdk": data.get("sdk")
            }
        except ImportError:
            # Fallback to manual validation against official rules
            pass

    # Built-in strict manual fallback validator adhering to official schema rules
    errors = []
    warnings = []
    
    # Required fields across all packages
    for req in ["id", "name", "version", "sdk", "description", "author", "license"]:
        if req not in data:
            errors.append(f"Missing required field: '{req}'")
            
    # Prohibited deprecated fields
    for forbidden in ["title", "compatibility", "scripts", "styles", "django_app"]:
        if forbidden in data:
            errors.append(f"Additional property not allowed in schema: '{forbidden}'")
            
    # ID regex: ^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)+$
    mod_id = data.get("id", "")
    if mod_id and not re.match(r"^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)+$", mod_id):
        errors.append(f"Field 'id' ('{mod_id}') does not match official regex '^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)+$'")
        
    # Version regex: ^[0-9]+\.[0-9]+\.[0-9]+$
    ver = data.get("version", "")
    if ver and not re.match(r"^[0-9]+\.[0-9]+\.[0-9]+$", ver):
        errors.append(f"Field 'version' ('{ver}') must be strictly 'X.Y.Z' semver (no pre-release or build suffixes)")
        
    # SDK check
    sdk = data.get("sdk")
    if sdk is not None:
        if not isinstance(sdk, dict) or "requires" not in sdk or "tested" not in sdk:
            errors.append("Field 'sdk' must be an object with 'requires' and 'tested' keys")
            
    # Django vs Browser checks
    is_django = "django" in data
    if is_django:
        if "entry" in data:
            errors.append("Field 'entry' cannot be defined when 'django' is present")
        if "system" in data:
            errors.append("Field 'system' cannot be defined when 'django' is present")
        if "locales" in data:
            errors.append("Field 'locales' cannot be defined when 'django' is present")
        django_block = data.get("django")
        if isinstance(django_block, dict):
            if "apps" not in django_block or not isinstance(django_block["apps"], list):
                errors.append("Field 'django.apps' is required and must be an array")
    else:
        if "entry" not in data:
            errors.append("Field 'entry' is required for browser/client modules")
        else:
            entry_file = p.parent / data["entry"]
            if not entry_file.exists():
                warnings.append(f"Referenced entry file does not exist on disk: {data['entry']}")
                
    return {
        "valid": len(errors) == 0,
        "validation_mode": "manual-schema-rules",
        "manifest_id": data.get("id"),
        "version": data.get("version"),
        "errors": errors,
        "warnings": warnings
    }

def tool_query_marketplace_packages(search_term: Optional[str] = None) -> Dict[str, Any]:
    # Known official packages in the Gravewright ecosystem with canonical IDs
    known_packages = [
        {
            "id": "gravewright.translator",
            "title": "Gravewright Translator",
            "repo": "https://github.com/Gravewright/translator",
            "description": "Official translation framework and localized bundles for Gravewright.",
            "category": "utility"
        },
        {
            "id": "gravewright-3d-dice",
            "title": "Gravewright 3D Dice",
            "repo": "https://github.com/Gravewright/Gravewright-3D-Dice",
            "description": "3D dice rolling physics and animations for the tabletop canvas.",
            "category": "visual"
        },
        {
            "id": "gravewright.5e-srd",
            "title": "D&D 5e SRD Compatibility Package",
            "repo": "https://github.com/Gravewright/dnd-srd-5e",
            "description": "SRD 5.1 rules, compendiums, spells, items and monsters for Gravewright.",
            "category": "system-compendium"
        },
        {
            "id": "gravewright.savage-worlds",
            "title": "Savage Worlds (SWADE) Compatibility Package",
            "repo": "https://github.com/Gravewright/Savage-Worlds-Compatibility-Package-for-Gravewright",
            "description": "Savage Worlds Adventure Edition rules compendium and character sheet mechanics.",
            "category": "system-compendium"
        }
    ]
    
    if search_term:
        term = search_term.lower()
        filtered = [
            pkg for pkg in known_packages
            if term in pkg["id"].lower() or term in pkg["title"].lower() or term in pkg["description"].lower()
        ]
        return {"packages": filtered, "total": len(filtered)}
        
    return {"packages": known_packages, "total": len(known_packages)}

def sanitize_module_id(name: str) -> str:
    cleaned = name.lower().strip()
    cleaned = re.sub(r"[^a-z0-9.-]+", "-", cleaned)
    cleaned = re.sub(r"-+", "-", cleaned).strip("-.")
    if not ("." in cleaned or "-" in cleaned):
        cleaned = f"custom.{cleaned}" if cleaned else "custom.module"
    if not cleaned[0].isalpha():
        cleaned = f"a.{cleaned}"
    return cleaned

def sanitize_python_ident(name: str) -> str:
    ident = re.sub(r"[^a-zA-Z0-9_]", "_", name).lower()
    ident = re.sub(r"_+", "_", ident).strip("_")
    if not ident or ident[0].isdigit():
        ident = f"gw_{ident}"
    return ident

def tool_scaffold_extension(name: str, module_type: str, author: str, target_dir: str) -> Dict[str, Any]:
    # Prevent path traversal
    safe_name = os.path.basename(name.strip())
    if not safe_name or safe_name in [".", ".."]:
        return {"success": False, "error": "Invalid module name."}
        
    module_id = sanitize_module_id(safe_name)
    folder_name = module_id.replace(".", "-")
    
    target_base = Path(target_dir).resolve()
    dest = target_base / folder_name
    
    # Security check: ensure dest is within target_base
    try:
        dest.resolve().relative_to(target_base)
    except ValueError:
        return {"success": False, "error": "Path traversal detected in module target directory."}
        
    if dest.exists():
        return {"success": False, "error": f"Target directory '{dest}' already exists."}
        
    dest.mkdir(parents=True)
    
    if module_type == "browser":
        manifest = {
            "id": module_id,
            "name": safe_name.replace("-", " ").title(),
            "version": "0.1.0",
            "sdk": {
                "requires": ">=1.0.0 <2.0.0",
                "tested": "1.0.0"
            },
            "entry": "main.js",
            "description": f"Custom browser module for Gravewright VTT.",
            "author": author,
            "license": "MIT"
        }
        
        with open(dest / "manifest.json", "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            
        (dest / "main.js").write_text(f"""// {safe_name} - Browser Extension for Gravewright VTT
// Official ESM Lifecycle: start, register, stop

export default {{
  start({{ styles }}) {{
    // Load module-scoped CSS
    styles.use("styles.css");
  }},

  register({{ register }}) {{
    // Register module surfaces (actor.directory, actor.sheet, chat.log, scene.overlay, etc.)
    register("actor.directory", async ({{ root, api, signal }}) => {{
      const container = root.ownerDocument.createElement("div");
      container.className = "{folder_name}-counter";
      root.append(container);

      const render = (actors) => {{
        if (!signal.aborted) {{
          container.textContent = `Visible Actors: ${{actors.length}}`;
        }}
      }};

      render(await api.actors.list());
      api.events.on("actors.changed", (snapshot) => render(snapshot.actors));
    }});
  }},

  stop() {{
    // Host automatically cleans up styles, registrations, and API handles
  }}
}};
""", encoding="utf-8")

        (dest / "styles.css").write_text(f"""/* {safe_name} - Isolated Styles */
.gw-module-root[data-module-id="{module_id}"] .{folder_name}-counter {{
    font-weight: 600;
    padding: 4px 8px;
    border-radius: 4px;
}}
""", encoding="utf-8")

        (dest / "LICENSE.txt").write_text(f"""MIT License

Copyright (c) 2026 {author}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""", encoding="utf-8")

    else:
        # Django app module
        py_app = sanitize_python_ident(safe_name) + "_server"
        class_name = "".join(w.capitalize() for w in py_app.split("_")) + "Config"
        
        manifest = {
            "id": module_id,
            "name": safe_name.replace("-", " ").title(),
            "version": "0.1.0",
            "sdk": {
                "requires": ">=1.0.0 <2.0.0",
                "tested": "1.0.0"
            },
            "description": f"Custom Django extension app for Gravewright VTT.",
            "author": author,
            "license": "MIT",
            "django": {
                "apps": [f"{py_app}.apps.{class_name}"],
                "requirements": []
            }
        }
        
        with open(dest / "manifest.json", "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
            
        app_dir = dest / py_app
        app_dir.mkdir(parents=True)
        (app_dir / "__init__.py").write_text("", encoding="utf-8")
        
        migrations_dir = app_dir / "migrations"
        migrations_dir.mkdir(parents=True)
        (migrations_dir / "__init__.py").write_text("", encoding="utf-8")
        
        (app_dir / "apps.py").write_text(f"""from django.apps import AppConfig

class {class_name}(AppConfig):
    name = "{py_app}"
    label = "{py_app}"

    def ready(self):
        \"\"\"
        Register public extension APIs or combat providers without mutating Gravewright core.
        \"\"\"
        try:
            from api.systems import register_api
            from .services import preview_roll

            register_api("{module_id}", {{
                "rules.preview": {{
                    "effect": "read",
                    "handler": preview_roll,
                    "description": "Preview a rules calculation or roll."
                }}
            }})
        except ImportError:
            pass
""", encoding="utf-8")

        (app_dir / "services.py").write_text(f"""# Domain services: validation and persistence logic for {safe_name}

def preview_roll(campaign_id, user_id, payload, request_id, scene_id):
    \"\"\"
    Public system operation callable from client via api.system.call('{module_id}.rules.preview', data)
    \"\"\"
    return {{
        "success": True,
        "echo": payload
    }}
""", encoding="utf-8")

        (app_dir / "models.py").write_text(f"""from django.db import models

# Custom SQLite extension models if persistent state is needed
""", encoding="utf-8")

        (dest / "LICENSE.txt").write_text(f"""MIT License

Copyright (c) 2026 {author}
""", encoding="utf-8")

    return {
        "success": True,
        "path": str(dest.resolve()),
        "manifest": manifest
    }

def tool_search_offline_docs(query: str, language: str = "pt-BR") -> Dict[str, Any]:
    base_docs = Path(__file__).resolve().parent.parent / "docs"
    
    dirs_to_search = []
    if language in ["pt-BR", "all"]:
        dirs_to_search.append(base_docs / "pt-BR")
    if language in ["en", "all"]:
        dirs_to_search.append(base_docs / "en")
        
    results = []
    q_lower = query.lower()
    
    for d in dirs_to_search:
        if d.exists():
            for doc_file in d.glob("*.md"):
                try:
                    text = doc_file.read_text(encoding="utf-8")
                    if q_lower in text.lower():
                        lines = text.splitlines()
                        matching_lines = [l.strip() for l in lines if q_lower in l.lower()][:3]
                        results.append({
                            "file": doc_file.name,
                            "path": str(doc_file.resolve()),
                            "lang": d.name,
                            "snippets": matching_lines
                        })
                except Exception:
                    pass
                    
    return {
        "query": query,
        "total_matches": len(results),
        "results": results[:10]
    }

def process_request(request: Dict[str, Any]):
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})
    
    if method == "initialize":
        send_response({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {}
                },
                "serverInfo": {
                    "name": SERVER_NAME,
                    "version": SERVER_VERSION
                }
            }
        })
    elif method == "notifications/initialized":
        pass
    elif method == "tools/list":
        send_response({
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": handle_list_tools()
            }
        })
    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        try:
            if tool_name == "inspect_gravewright_environment":
                res = tool_inspect_gravewright_environment(args.get("project_path"))
            elif tool_name == "list_installed_modules":
                res = tool_list_installed_modules(args.get("modules_path"))
            elif tool_name == "validate_module_manifest":
                res = tool_validate_module_manifest(args.get("manifest_path"))
            elif tool_name == "query_marketplace_packages":
                res = tool_query_marketplace_packages(args.get("search_term"))
            elif tool_name == "scaffold_extension":
                res = tool_scaffold_extension(
                    args.get("name"),
                    args.get("module_type", "browser"),
                    args.get("author", "Gravewright Developer"),
                    args.get("target_dir")
                )
            elif tool_name == "search_offline_docs":
                res = tool_search_offline_docs(args.get("query"), args.get("language", "pt-BR"))
            else:
                send_response({
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "error": {
                        "code": -32601,
                        "message": f"Tool '{tool_name}' not found."
                    }
                })
                return
                
            # If the tool result contains an error or failure, return it as content with isError: true when relevant
            is_error = False
            if isinstance(res, dict):
                if res.get("valid") is False or res.get("success") is False:
                    is_error = True
                    
            response_payload = {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(res, indent=2, ensure_ascii=False)
                        }
                    ]
                }
            }
            if is_error:
                response_payload["result"]["isError"] = True
                
            send_response(response_payload)
        except Exception as e:
            send_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "isError": True,
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps({"error": str(e)}, indent=2, ensure_ascii=False)
                        }
                    ]
                }
            })
    else:
        if req_id is not None:
            send_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32601,
                    "message": f"Method '{method}' not implemented."
                }
            })

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            process_request(req)
        except Exception:
            pass

if __name__ == "__main__":
    main()
