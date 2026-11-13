#!/usr/bin/env python3
"""
notion_sync.py - Notion API Synchronization Utility for Second Brain Plus
Utilitário de Sincronização da API do Notion para o Second Brain Plus.

Bilingual support: English (EN) and Portuguese (PT-BR).
Suporte bilíngue: Inglês (EN) e Português (PT-BR).
"""

import os
import sys
import re
import json
import argparse
import hashlib
from pathlib import Path
import urllib.request
import urllib.error

# Notion API Configuration / Configuração da API do Notion
NOTION_API_VERSION = "2022-06-28"
NOTION_API_BASE = "https://api.notion.com/v1"

def load_env_file():
    """
    EN: Auto-load .env file if present in workspace root.
    PT-BR: Carrega automaticamente o arquivo .env se presente na raiz do workspace.
    """
    env_path = Path(__file__).resolve().parent.parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

load_env_file()

def extract_notion_id(raw_input: str) -> str:
    """
    EN: Extract clean Notion UUID from either a raw ID or full Notion URL.
    PT-BR: Extrai o UUID limpo do Notion a partir de um ID puro ou URL completa do Notion.
    """
    if not raw_input:
        return ""
    # Remove dashes if already an ID
    clean = raw_input.strip().split("?")[0].split("#")[0]
    match = re.search(r'([a-f0-9]{32}|[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12})', clean)
    if match:
        raw_id = match.group(1).replace("-", "")
        # Format as standard 8-4-4-4-12 UUID
        return f"{raw_id[:8]}-{raw_id[8:12]}-{raw_id[12:16]}-{raw_id[16:20]}-{raw_id[20:]}"
    return raw_input

def get_notion_headers(api_key: str) -> dict:
    """
    EN: Build standard HTTP headers for Notion API requests.
    PT-BR: Constrói os cabeçalhos HTTP padrão para requisições à API do Notion.
    """
    return {
        "Authorization": f"Bearer {api_key}",
        "Notion-Version": NOTION_API_VERSION,
        "Content-Type": "application/json"
    }

def notion_request(endpoint: str, api_key: str, method: str = "GET", data: dict = None) -> dict:
    """
    EN: Execute a native HTTP request against Notion API without heavy 3rd-party dependencies.
    PT-BR: Executa uma requisição HTTP nativa contra a API do Notion sem dependências pesadas externas.
    """
    url = f"{NOTION_API_BASE}/{endpoint.lstrip('/')}"
    headers = get_notion_headers(api_key)
    body = json.dumps(data).encode("utf-8") if data else None
    
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode("utf-8")
            return json.loads(res_body)
    except urllib.error.HTTPError as e:
        error_content = e.read().decode("utf-8")
        try:
            err_json = json.loads(error_content)
            msg = err_json.get("message", error_content)
        except Exception:
            msg = error_content
        return {"error": True, "status": e.code, "message": msg}
    except Exception as e:
        return {"error": True, "status": 500, "message": str(e)}

def check_authentication(api_key: str) -> bool:
    """
    EN: Test integration credentials by querying the current bot/user info.
    PT-BR: Testa as credenciais da integração consultando as informações do bot/usuário atual.
    """
    print("🔍 [EN] Testing Notion API authentication... / [PT-BR] Testando autenticação da API do Notion...")
    result = notion_request("/users/me", api_key)
    if result.get("error"):
        print(f"❌ [EN] Authentication failed / [PT-BR] Falha na autenticação: {result.get('message')} (HTTP {result.get('status')})")
        return False
    bot_name = result.get("name", "Unknown Integration")
    bot_id = result.get("id", "N/A")
    print(f"✅ [EN] Authenticated as '{bot_name}' (ID: {bot_id}) / [PT-BR] Autenticado com sucesso como '{bot_name}'")
    return True

def list_pages(api_key: str) -> list:
    """
    EN: List all Notion pages shared with the current integration.
    PT-BR: Lista todas as páginas do Notion compartilhadas com a integração atual.
    """
    print("📋 [EN] Querying accessible Notion pages... / [PT-BR] Consultando páginas acessíveis no Notion...")
    query_payload = {
        "filter": {"value": "page", "property": "object"}
    }
    result = notion_request("/search", api_key, method="POST", data=query_payload)
    if result.get("error"):
        print(f"❌ [EN] Failed to list pages / [PT-BR] Falha ao listar páginas: {result.get('message')}")
        return []
    
    pages = result.get("results", [])
    print(f"📄 [EN] Found {len(pages)} page(s) / [PT-BR] Encontrada(s) {len(pages)} página(s):")
    for p in pages:
        props = p.get("properties", {})
        # Find title property
        title = "Untitled"
        for _, prop_val in props.items():
            if prop_val.get("type") == "title":
                title_objs = prop_val.get("title", [])
                title = "".join(t.get("plain_text", "") for t in title_objs) or "Untitled"
                break
        print(f"  • [{p.get('id')}] {title}")
    return pages

def list_databases(api_key: str) -> list:
    """
    EN: List all Notion databases shared with the current integration.
    PT-BR: Lista todos os bancos de dados do Notion compartilhados com a integração atual.
    """
    print("📋 [EN] Querying accessible Notion databases... / [PT-BR] Consultando bancos de dados acessíveis no Notion...")
    query_payload = {
        "filter": {"value": "database", "property": "object"}
    }
    result = notion_request("/search", api_key, method="POST", data=query_payload)
    if result.get("error"):
        print(f"❌ [EN] Failed to list databases / [PT-BR] Falha ao listar bancos de dados: {result.get('message')}")
        return []
    
    databases = result.get("results", [])
    print(f"📊 [EN] Found {len(databases)} database(s) / [PT-BR] Encontrado(s) {len(databases)} banco(s) de dados:")
    for db in databases:
        title_objs = db.get("title", [])
        title = "".join(t.get("plain_text", "") for t in title_objs) or "Untitled"
        print(f"  • [{db.get('id')}] {title}")
    return databases

def create_databases_on_page(parent_page_id: str, api_key: str) -> dict:
    """
    EN: Create all 4 Second Brain databases inside a parent page.
    PT-BR: Cria todos os 4 bancos de dados do Segundo Cérebro dentro de uma página-mãe.
    """
    formatted_parent = extract_notion_id(parent_page_id)
    print(f"🏗️ [EN] Creating Second Brain databases inside page '{formatted_parent}'...")
    print(f"   [PT-BR] Criando bancos de dados do Segundo Cérebro na página '{formatted_parent}'...")

    schema_file = Path(__file__).resolve().parent.parent / "templates" / "notion" / "databases_schema.json"
    if not schema_file.exists():
        print(f"❌ Schema template missing at {schema_file}")
        return {}

    schemas = json.loads(schema_file.read_text(encoding="utf-8")).get("databases", {})
    created_dbs = {}

    for key, spec in schemas.items():
        title_text = spec.get("title", f"Second Brain - {key.capitalize()}")
        payload = {
            "parent": {"type": "page_id", "page_id": formatted_parent},
            "title": [{"type": "text", "text": {"content": title_text}}],
            "properties": spec.get("properties", {})
        }
        res = notion_request("/databases", api_key, method="POST", data=payload)
        if res.get("error"):
            print(f"  ❌ Falha ao criar banco '{title_text}': {res.get('message')}")
        else:
            db_id = res.get("id")
            created_dbs[key] = db_id
            print(f"  ✅ Banco criado com sucesso: '{title_text}' (ID: {db_id})")

    return created_dbs

def calculate_checksum(file_path: Path) -> str:
    """
    EN: Compute short SHA-256 hash for file drift detection.
    PT-BR: Calcula hash SHA-256 curto para detecção de alterações em arquivos.
    """
    content = file_path.read_bytes()
    return hashlib.sha256(content).hexdigest()[:8]

def parse_frontmatter(content: str) -> tuple[dict, str]:
    """
    EN: Parse YAML frontmatter and body from Markdown text.
    PT-BR: Extrai o frontmatter YAML e o corpo do texto Markdown.
    """
    fm = {}
    body = content
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if match:
        fm_text = match.group(1)
        body = match.group(2)
        for line in fm_text.splitlines():
            line = line.strip()
            if line and not line.startswith("#") and ":" in line:
                k, v = line.split(":", 1)
                clean_v = v.strip().strip('"\'')
                if clean_v.lower() == "true":
                    clean_v = True
                elif clean_v.lower() == "false":
                    clean_v = False
                fm[k.strip()] = clean_v
    return fm, body

def normalize_notion_code_lang(lang: str) -> str:
    """Normalize markdown code block language to Notion-accepted language enum."""
    raw = (lang or "").lower().strip()
    mapping = {
        "text": "plain text",
        "txt": "plain text",
        "": "plain text",
        "sh": "shell",
        "zsh": "shell",
        "py": "python",
        "js": "javascript",
        "ts": "typescript",
        "yml": "yaml",
        "rb": "ruby",
        "rs": "rust",
        "ps1": "powershell"
    }
    if raw in mapping:
        return mapping[raw]
    
    valid_langs = {
        "abap", "arduino", "bash", "basic", "c", "clojure", "coffeescript", "cpp", "c++", "c#",
        "css", "dart", "diff", "docker", "elixir", "elm", "erlang", "flow", "fortran", "f#",
        "gherkin", "glsl", "go", "graphql", "groovy", "haskell", "html", "java", "javascript",
        "json", "julia", "kotlin", "latex", "less", "lisp", "livescript", "lua", "makefile",
        "markdown", "markup", "matlab", "mermaid", "nix", "objective-c", "ocaml", "pascal", "perl",
        "php", "plain text", "powershell", "prolog", "protobuf", "python", "r", "reason", "ruby",
        "rust", "sass", "scala", "scheme", "scss", "shell", "sql", "swift", "toml", "typescript",
        "vb.net", "verilog", "vhdl", "visual basic", "webassembly", "xml", "yaml"
    }
    return raw if raw in valid_langs else "plain text"

def markdown_to_notion_blocks(md_text: str) -> list:
    """
    EN: Convert raw markdown text into Notion block objects.
    PT-BR: Converte texto Markdown puro em objetos de blocos do Notion.
    """
    blocks = []
    lines = md_text.splitlines()
    in_code = False
    code_lang = "plain text"
    code_lines = []

    for line in lines:
        stripped = line.strip()
        if not stripped and not in_code:
            continue

        if stripped.startswith("```"):
            if in_code:
                content = "\n".join(code_lines)[:2000]
                blocks.append({
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [{"type": "text", "text": {"content": content}}],
                        "language": normalize_notion_code_lang(code_lang)
                    }
                })
                in_code = False
                code_lines = []
            else:
                in_code = True
                lang = stripped[3:].strip()
                code_lang = normalize_notion_code_lang(lang)
                code_lines = []
            continue

        if in_code:
            code_lines.append(line)
            continue

        if stripped == "---":
            blocks.append({"object": "block", "type": "divider", "divider": {}})
        elif stripped.startswith("### "):
            blocks.append({
                "object": "block",
                "type": "heading_3",
                "heading_3": {"rich_text": [{"type": "text", "text": {"content": stripped[4:][:2000]}}]}
            })
        elif stripped.startswith("## "):
            blocks.append({
                "object": "block",
                "type": "heading_2",
                "heading_2": {"rich_text": [{"type": "text", "text": {"content": stripped[3:][:2000]}}]}
            })
        elif stripped.startswith("# "):
            blocks.append({
                "object": "block",
                "type": "heading_1",
                "heading_1": {"rich_text": [{"type": "text", "text": {"content": stripped[2:][:2000]}}]}
            })
        elif stripped.startswith("- [ ] ") or stripped.startswith("- [x] "):
            checked = stripped.startswith("- [x] ")
            blocks.append({
                "object": "block",
                "type": "to_do",
                "to_do": {
                    "rich_text": [{"type": "text", "text": {"content": stripped[6:][:2000]}}],
                    "checked": checked
                }
            })
        elif stripped.startswith("- ") or stripped.startswith("* "):
            blocks.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": stripped[2:][:2000]}}]}
            })
        elif stripped.startswith("> "):
            blocks.append({
                "object": "block",
                "type": "quote",
                "quote": {"rich_text": [{"type": "text", "text": {"content": stripped[2:][:2000]}}]}
            })
        else:
            blocks.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": stripped[:2000]}}]}
            })

    return blocks[:100]

def push_note_to_notion(file_path: Path, api_key: str) -> bool:
    """
    EN: Push a local markdown note to its corresponding Notion database.
    PT-BR: Envia uma nota Markdown local para o banco de dados correspondente no Notion.
    """
    content = file_path.read_text(encoding="utf-8", errors="ignore")
    fm, body = parse_frontmatter(content)
    note_type = fm.get("type", "").lower()
    title = fm.get("title", file_path.stem)
    rel_path = str(file_path.name)
    checksum = calculate_checksum(file_path)

    # Infer type from folder structure if missing in frontmatter
    if not note_type:
        parent_name = file_path.parent.name.lower()
        grandparent_name = file_path.parent.parent.name.lower()
        if "project" in parent_name or "project" in grandparent_name:
            note_type = "project"
        elif "adr" in parent_name or "adr" in grandparent_name:
            note_type = "adr"
        elif "session" in parent_name or "session" in grandparent_name:
            note_type = "session-log"
        elif "resource" in parent_name or "resource" in grandparent_name:
            note_type = "resource"
        else:
            note_type = "resource"

    db_map = {
        "project": os.environ.get("NOTION_DB_PROJECTS"),
        "adr": os.environ.get("NOTION_DB_ADRS"),
        "session-log": os.environ.get("NOTION_DB_MEMORIES"),
        "resource": os.environ.get("NOTION_DB_RESOURCES"),
        "adhd-focus": os.environ.get("NOTION_DB_PROJECTS")
    }

    target_db = db_map.get(note_type)
    if not target_db:
        return False

    # Build properties payload based on database schema
    properties = {}
    if note_type in ["project", "adhd-focus"]:
        properties = {
            "Name": {"title": [{"text": {"content": str(title)}}]},
            "Status": {"select": {"name": "Active / Sprint" if fm.get("status") == "active" else "Backlog"}},
            "Priority": {"select": {"name": "P1 - High" if fm.get("priority") == "P1" else "P2 - Medium"}},
            "FocusMode_ADHD": {"checkbox": bool(fm.get("adhd_mode_enabled", False))},
            "LastSyncHash": {"rich_text": [{"text": {"content": checksum}}]},
            "LocalPath": {"rich_text": [{"text": {"content": rel_path}}]}
        }
    elif note_type == "adr":
        properties = {
            "Title": {"title": [{"text": {"content": str(title)}}]},
            "ID": {"rich_text": [{"text": {"content": str(fm.get("id", "ADR-001"))}}]},
            "Status": {"select": {"name": "Accepted" if fm.get("status") == "accepted" else "Proposed"}},
            "DecidedBy": {"rich_text": [{"text": {"content": str(fm.get("decided_by", "AI & Dev"))}}]},
            "Rationale": {"rich_text": [{"text": {"content": body[:200].strip()}}]},
            "LocalPath": {"rich_text": [{"text": {"content": rel_path}}]}
        }
    elif note_type == "session-log":
        properties = {
            "SessionTitle": {"title": [{"text": {"content": str(title)}}]},
            "Agent": {"select": {"name": "Antigravity"}},
            "Summary": {"rich_text": [{"text": {"content": body[:200].strip()}}]},
            "NeurodivergentMode": {"checkbox": bool(fm.get("neurodivergent_mode", False))},
            "LocalPath": {"rich_text": [{"text": {"content": rel_path}}]}
        }
    elif note_type == "resource":
        properties = {
            "ResourceName": {"title": [{"text": {"content": str(title)}}]},
            "Category": {"select": {"name": "Architecture"}},
            "LocalPath": {"rich_text": [{"text": {"content": rel_path}}]}
        }

    # Convert markdown body into Notion block children
    children_blocks = markdown_to_notion_blocks(body)

    payload = {
        "parent": {"database_id": target_db},
        "properties": properties,
        "children": children_blocks
    }

    res = notion_request("/pages", api_key, method="POST", data=payload)
    if res.get("error"):
        print(f"    ⚠️ Erro ao sincronizar '{file_path.name}': {res.get('message')}")
        return False
    else:
        page_id = res.get("id")
        print(f"    ☁️ Sincronizado no Notion -> {title} (Page ID: {page_id})")
        return True

def sync_local_vault(vault_dir: Path, api_key: str = None):
    """
    EN: Scan, verify, and push markdown notes to Notion databases.
    PT-BR: Varre, verifica e envia notas Markdown para os bancos do Notion.
    """
    print(f"🔄 [EN] Scanning vault at '{vault_dir}' / [PT-BR] Varrendo cofre em '{vault_dir}'...")
    if not vault_dir.exists():
        print(f"❌ [EN] Vault path does not exist / [PT-BR] Caminho do cofre não existe: {vault_dir}")
        return
    
    md_files = list(vault_dir.rglob("*.md"))
    print(f"📄 [EN] Found {len(md_files)} Markdown document(s) / [PT-BR] Encontrado(s) {len(md_files)} documento(s) Markdown.")
    
    synced_count = 0
    pushed_count = 0
    for f in md_files:
        checksum = calculate_checksum(f)
        rel_path = f.relative_to(vault_dir)
        synced_count += 1
        print(f"  ✓ {rel_path} (Hash: {checksum})")
        if api_key and os.environ.get("NOTION_DB_PROJECTS"):
            if push_note_to_notion(f, api_key):
                pushed_count += 1
    
    print(f"✅ [EN] Sync complete: {synced_count} note(s) scanned, {pushed_count} pushed to Notion.")
    print(f"   [PT-BR] Sincronização concluída: {synced_count} nota(s) verificada(s), {pushed_count} enviada(s) para o Notion.")

def main():
    parser = argparse.ArgumentParser(
        description="Second Brain Plus - Notion Sync Utility / Utilitário de Sincronização do Notion"
    )
    parser.add_argument("--check-auth", action="store_true", help="EN: Validate Notion token / PT-BR: Valida token da API do Notion")
    parser.add_argument("--list-pages", action="store_true", help="EN: List accessible Notion pages / PT-BR: Lista páginas acessíveis no Notion")
    parser.add_argument("--list-databases", action="store_true", help="EN: List accessible Notion databases / PT-BR: Lista bancos acessíveis no Notion")
    parser.add_argument("--create-databases", help="EN: Parent page ID or URL to scaffold databases / PT-BR: ID ou URL da página mãe para criar bancos")
    parser.add_argument("--sync-local", action="store_true", help="EN: Scan and verify local vault / PT-BR: Varre e verifica o cofre local")
    parser.add_argument("--vault-dir", default="./.second-brain", help="EN: Path to local vault / PT-BR: Caminho do cofre local")
    parser.add_argument("--api-key", default=None, help="EN: Notion API key / PT-BR: Chave da API do Notion")

    args = parser.parse_args()
    api_key = args.api_key or os.environ.get("NOTION_API_KEY")

    if args.check_auth:
        if not api_key:
            print("❌ [EN] NOTION_API_KEY not provided / [PT-BR] NOTION_API_KEY não informada.")
            sys.exit(1)
        success = check_authentication(api_key)
        sys.exit(0 if success else 1)

    if args.list_databases:
        if not api_key:
            print("❌ [EN] NOTION_API_KEY not provided / [PT-BR] NOTION_API_KEY não informada.")
            sys.exit(1)
        list_databases(api_key)
        sys.exit(0)

    if args.list_pages:
        if not api_key:
            print("❌ [EN] NOTION_API_KEY not provided / [PT-BR] NOTION_API_KEY não informada.")
            sys.exit(1)
        list_pages(api_key)
        sys.exit(0)

    if args.create_databases:
        if not api_key:
            print("❌ [EN] NOTION_API_KEY not provided / [PT-BR] NOTION_API_KEY não informada.")
            sys.exit(1)
        create_databases_on_page(args.create_databases, api_key)
        sys.exit(0)

    if args.sync_local:
        sync_local_vault(Path(args.vault_dir), api_key)
        sys.exit(0)

    parser.print_help()

if __name__ == "__main__":
    main()
