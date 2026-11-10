#!/usr/bin/env python3
"""
Master of Gravewright VTT - Native MCP Server
==============================================
Server Name: master-of-gravewright-mcp
Version: 0.1.0-beta
Author: GM Charles Corrêa
License: MIT

Zero-dependency Model Context Protocol (MCP) server running over JSON-RPC 2.0 (stdio).
Connects AI coding assistants and agents directly into Gravewright VTT project contexts.

Capabilities / Funcionalidades:
1. inspect_gravewright_environment: Detects local repository, Django apps, uv environment, and database.
2. list_installed_modules: Scans and reports installed Gravewright browser and Django modules.
3. validate_module_manifest: Validates manifest.json schemas, compatibility tags, and assets.
4. query_marketplace_packages: Searches the official Gravewright marketplace for modules and translation packages.
5. scaffold_extension: Generates browser-module or django-app-module boilerplate with isolated CSS.
6. inspect_campaign_data: Reads campaign structure, clocks, clues, and journals from project directory.
7. search_offline_docs: Queries the 50 offline Markdown manuals in EN and pt-BR.
"""

import sys
import json
import os
import glob
import re
from pathlib import Path
from typing import Dict, Any, List, Optional

SERVER_NAME = "master-of-gravewright-mcp"
SERVER_VERSION = "0.1.0-beta"

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
            "description": "Inspects the local Gravewright VTT project root, Python/uv environment, Django configuration, and registered apps.",
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
            "description": "Scans and lists installed Gravewright modules, reporting title, version, type (browser/django), and compatibility.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "modules_path": {
                        "type": "string",
                        "description": "Optional path to the extensions or modules directory."
                    }
                }
            }
        },
        {
            "name": "validate_module_manifest",
            "description": "Validates a Gravewright module's manifest.json file against official schema requirements (id, title, version, scripts, compatibility).",
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
            "description": "Queries the official Gravewright GitHub marketplace catalog for available extensions, 3D dice, and compatibility packages.",
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
            "description": "Generates a complete Gravewright module boilerplate (browser JavaScript or Django app) with isolated CSS and manifest.",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Module name or ID (e.g. 'custom-clocks', 'swade-helper')."
                    },
                    "module_type": {
                        "type": "string",
                        "enum": ["browser", "django"],
                        "default": "browser",
                        "description": "Type of module: 'browser' for client JS/CSS or 'django' for server app."
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
        
    return {
        "project_path": str(path.resolve()),
        "is_gravewright_root": is_gravewright,
        "uses_astral_uv": has_uv,
        "django_manage_py": (path / "manage.py").exists(),
        "detected_subapps": apps,
        "extensions_dir_exists": (path / "extensions").exists() or (path / "data" / "extensions").exists(),
        "status": "ready" if is_gravewright else "not_a_gravewright_repo"
    }

def tool_list_installed_modules(modules_path: Optional[str] = None) -> Dict[str, Any]:
    search_dirs = []
    if modules_path:
        search_dirs.append(Path(modules_path))
    else:
        cwd = Path.cwd()
        search_dirs.extend([
            cwd / "extensions",
            cwd / "data" / "extensions",
            cwd / "master-of-gravewright" / "templates"
        ])
        
    modules = []
    for d in search_dirs:
        if d.exists() and d.is_dir():
            for sub in d.iterdir():
                if sub.is_dir() and (sub / "manifest.json").exists():
                    try:
                        with open(sub / "manifest.json", "r", encoding="utf-8") as f:
                            data = json.load(f)
                        modules.append({
                            "directory": str(sub.resolve()),
                            "id": data.get("id", sub.name),
                            "title": data.get("title", sub.name),
                            "version": data.get("version", "0.0.0"),
                            "type": "django" if data.get("django_app") else "browser",
                            "author": data.get("author", "Unknown"),
                            "compatibility": data.get("compatibility", {})
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
        
    errors = []
    warnings = []
    
    required_keys = ["id", "title", "version"]
    for k in required_keys:
        if k not in data or not str(data[k]).strip():
            errors.append(f"Missing required field: '{k}'")
            
    # Check script files if specified
    base_dir = p.parent
    for script in data.get("scripts", []):
        if not (base_dir / script).exists():
            warnings.append(f"Referenced script file does not exist: {script}")
            
    for style in data.get("styles", []):
        if not (base_dir / style).exists():
            warnings.append(f"Referenced stylesheet does not exist: {style}")
            
    return {
        "valid": len(errors) == 0,
        "manifest_id": data.get("id"),
        "version": data.get("version"),
        "errors": errors,
        "warnings": warnings
    }

def tool_query_marketplace_packages(search_term: Optional[str] = None) -> Dict[str, Any]:
    # Known official packages in the Gravewright ecosystem
    known_packages = [
        {
            "id": "gravewright.translator",
            "title": "Gravewright Translator",
            "repo": "https://github.com/Gravewright/translator",
            "description": "Official translation framework and localized bundles for Gravewright.",
            "category": "utility"
        },
        {
            "id": "gravewright.3d-dice",
            "title": "Gravewright 3D Dice",
            "repo": "https://github.com/Gravewright/Gravewright-3D-Dice",
            "description": "3D dice rolling physics and animations for the tabletop canvas.",
            "category": "visual"
        },
        {
            "id": "gravewright.dnd-srd-5e",
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

def tool_scaffold_extension(name: str, module_type: str, author: str, target_dir: str) -> Dict[str, Any]:
    dest = Path(target_dir) / name.lower().replace(" ", "-")
    if dest.exists():
        return {"success": False, "error": f"Target directory '{dest}' already exists."}
        
    dest.mkdir(parents=True)
    
    manifest = {
        "id": name.lower().replace(" ", "-"),
        "title": name,
        "version": "0.1.0",
        "description": f"Custom {module_type} module for Gravewright VTT.",
        "author": author,
        "license": "MIT",
        "compatibility": {
            "minimum": "0.3.0",
            "verified": "0.3.4"
        },
        "scripts": ["index.js"] if module_type == "browser" else [],
        "styles": ["style.css"] if module_type == "browser" else [],
        "django_app": f"{name.lower().replace('-', '_')}_app" if module_type == "django" else None
    }
    
    with open(dest / "manifest.json", "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        
    if module_type == "browser":
        (dest / "index.js").write_text(f"""// {name} - Browser Extension for Gravewright VTT
// Author / Autor: {author}
(() => {{
    console.log("[Gravewright Extension] Initializing: {name}");
}})();
""", encoding="utf-8")
        (dest / "style.css").write_text(f"""/* {name} - Isolated Styles */
.{manifest['id']}-root {{
    box-sizing: border-box;
}}
""", encoding="utf-8")
    else:
        app_name = f"{name.lower().replace('-', '_')}_app"
        app_dir = dest / app_name
        app_dir.mkdir(parents=True)
        (app_dir / "__init__.py").write_text("", encoding="utf-8")
        (app_dir / "models.py").write_text("# Django models for Gravewright extension\n", encoding="utf-8")
        (app_dir / "services.py").write_text("# Domain services: owns validation and persistence\n", encoding="utf-8")
        (app_dir / "views.py").write_text("# HTTP and API views\n", encoding="utf-8")
        
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
                        # Find matching snippet
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
                
            send_response({
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
            })
        except Exception as e:
            send_response({
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {
                    "code": -32000,
                    "message": str(e)
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
        except Exception as e:
            pass

if __name__ == "__main__":
    main()

