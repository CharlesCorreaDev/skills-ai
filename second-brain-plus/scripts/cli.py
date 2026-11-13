#!/usr/bin/env python3
"""
cli.py - Unified Command Interface for Second Brain Plus (/second-brain)
Interface Unificada de Comandos para o Second Brain Plus (/second-brain).

Supports slash commands and CLI invocations:
- /second-brain install        : Interactive setup & database scaffolding
- /second-brain save memory    : Instantly store facts, notes, or learnings
- /second-brain adr            : Record an immutable Architecture Decision Record
- /second-brain sync           : Trigger one-shot multi-agent synchronization
- /second-brain status         : Display vault metrics and Notion sync health
- /second-brain focus          : Switch to ADHD/Neurodivergent atomic focus mode

Bilingual support: English (EN) and Portuguese (PT-BR).
Suporte bilíngue: Inglês (EN) e Português (PT-BR).
"""

import os
import sys
import re
import json
import argparse
import datetime
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent))
import auto_sync
import notion_sync
import memory_bridge
import verify_brain
import git_remote_sync

def get_vault_dir() -> Path:
    vault_str = os.environ.get("SECOND_BRAIN_DIR", "./.second-brain")
    return Path(vault_str)

def cmd_install(args):
    """
    EN: Install and scaffold Second Brain vault and Notion databases.
    PT-BR: Instala e inicializa o cofre do Segundo Cérebro e os bancos no Notion.
    """
    vault = get_vault_dir()
    api_key = os.environ.get("NOTION_API_KEY")
    page_id = os.environ.get("NOTION_PARENT_PAGE_ID")

    print("🚀 [EN] Running /second-brain install...")
    print("   [PT-BR] Executando /second-brain install...")
    
    verify_brain.scaffold_second_brain(vault)
    
    if api_key and page_id:
        print(f"☁️ [EN] Scaffolding databases on Notion page {page_id}...")
        print(f"   [PT-BR] Criando bancos de dados na página {page_id} do Notion...")
        notion_sync.create_databases_on_page(page_id, api_key)
        
    auto_sync.execute_full_sync(vault, api_key)
    print("✅ [EN] Installation completed! / [PT-BR] Instalação concluída com sucesso!")

def cmd_save_memory(memory_text: str):
    """
    EN: Save a custom fact, rule, or learning into episodic memory and auto-sync.
    PT-BR: Salva um fato, regra ou aprendizado na memória episódica e auto-sincroniza.
    """
    vault = get_vault_dir()
    sessions_dir = vault / "4-Archives" / "sessions"
    sessions_dir.mkdir(parents=True, exist_ok=True)
    
    today_str = datetime.date.today().isoformat()
    timestamp = datetime.datetime.now().strftime("%H%M%S")
    mem_id = f"MEM-{today_str}-{timestamp}"
    
    compressed_text, ratio = memory_bridge.compress_caveman(memory_text)
    
    note_content = f"""---
id: "{mem_id}"
title: "Memória Salva: {memory_text[:40]}..."
type: "session-log"
date: "{today_str}"
agent: "Human / AI Agent"
tokens_saved_caveman: {ratio}
source: "user /second-brain save memory"
---

# 🧠 Memória Persistente / Persistent Memory: {mem_id}

## 📝 Fato Registrado / Stored Fact
{memory_text}

## 🗜️ Resumo Comprimido (Caveman Dialect)
```text
{compressed_text}
```
"""
    note_file = sessions_dir / f"{mem_id}.md"
    note_file.write_text(note_content, encoding="utf-8")
    print(f"💾 [EN] Memory saved locally: {note_file.name}")
    print(f"   [PT-BR] Memória salva localmente: {note_file.name}")
    
    # Auto-sync immediately to Notion, claude-mem, and graphify
    auto_sync.execute_full_sync(vault, changed_files=[str(note_file.relative_to(vault))])

def cmd_save_adr(title: str, rationale: str = ""):
    """
    EN: Save an Architecture Decision Record (ADR) and auto-sync.
    PT-BR: Salva um Architecture Decision Record (ADR) e auto-sincroniza.
    """
    vault = get_vault_dir()
    adrs_dir = vault / "3-Resources" / "adrs"
    adrs_dir.mkdir(parents=True, exist_ok=True)
    
    count = len(list(adrs_dir.glob("ADR-*.md"))) + 1
    adr_id = f"ADR-{count:03d}"
    today_str = datetime.date.today().isoformat()
    
    content = f"""---
id: "{adr_id}"
title: "{title}"
type: "adr"
status: "accepted"
decided_at: "{today_str}"
decided_by: "Charles Corrêa & Antigravity"
impacted_modules: ["core"]
source: "user /second-brain adr"
---

# 🏛️ {adr_id}: {title}

## 📋 Contexto & Decisão / Context & Decision
{rationale or title}

## 🎯 Racional Técnico / Technical Rationale
- Decisão registrada formalmente pelo usuário para prevenção de alucinações.
- O agente de IA deve respeitar esta decisão em todas as gerações de código futuras.
"""
    adr_file = adrs_dir / f"{adr_id}-{title.lower().replace(' ', '-')[:30]}.md"
    adr_file.write_text(content, encoding="utf-8")
    print(f"🏛️ [EN] ADR recorded: {adr_file.name}")
    print(f"   [PT-BR] ADR registrado: {adr_file.name}")
    
    auto_sync.execute_full_sync(vault, changed_files=[str(adr_file.relative_to(vault))])

def cmd_status():
    """
    EN: Print summary of vault health, note count, and Notion sync.
    PT-BR: Exibe resumo de saúde do cofre, contagem de notas e sincronização do Notion.
    """
    vault = get_vault_dir()
    print("=" * 65)
    print("🧠 SECOND BRAIN PLUS — SYSTEM STATUS")
    print("=" * 65)
    
    if not vault.exists():
        print(f"❌ Cofre local não encontrado em '{vault}'. Execute /second-brain install.")
        return
        
    md_files = list(vault.rglob("*.md"))
    adrs = list((vault / "3-Resources" / "adrs").glob("*.md")) if (vault / "3-Resources" / "adrs").exists() else []
    sessions = list((vault / "4-Archives" / "sessions").glob("*.md")) if (vault / "4-Archives" / "sessions").exists() else []
    projects = list((vault / "1-Projects").glob("*.md")) if (vault / "1-Projects").exists() else []
    
    print(f"📁 Diretório Local: {vault}")
    print(f"📄 Total de Notas Markdown: {len(md_files)}")
    print(f"  • Projetos / Sprints: {len(projects)}")
    print(f"  • Decisões & ADRs: {len(adrs)}")
    print(f"  • Memórias & Sessões: {len(sessions)}")
    
    # Graphify status
    graph_file = vault / ".graphify" / "graph.json"
    if graph_file.exists():
        try:
            g_data = json.loads(graph_file.read_text(encoding="utf-8"))
            print(f"🕸️ Grafo de Conhecimento (Graphify): {g_data.get('nodes_count', 0)} nós, {g_data.get('edges_count', 0)} arestas")
        except Exception:
            pass
            
    # Notion status
    api_key = os.environ.get("NOTION_API_KEY")
    if api_key:
        print("☁️ Conexão Notion API: Configurada (Token ativo)")
    else:
        print("☁️ Conexão Notion API: Não configurada (Modo offline local)")
        
    print("=" * 65)

def cmd_tdah_focus():
    """
    EN: Display ADHD atomic focus panel with bionic formatting and low cognitive load.
    PT-BR: Exibe o painel de foco atômico para TDAH com formatação biônica e baixa carga cognitiva.
    """
    vault = get_vault_dir()
    adhd_file = vault / "1-Projects" / "ADHD-FOCUS-DASHBOARD.md"
    
    print("\n" + "=" * 65)
    print("⚡ [MODO TDAH / ADHD ACTIVE] — NOT TODAY, ADHD! 🧠🛡️")
    print("   Baixa Carga Cognitiva • Uma Micro-Ação Por Vez • Body Doubling")
    print("=" * 65 + "\n")
    
    if adhd_file.exists():
        content = adhd_file.read_text(encoding="utf-8")
        # Extract active action
        action_match = re.search(r'-\s*\[\s*\]\s*\*\*Ação Ativa[^*]*\*\*:\s*(.+)', content)
        active_action = action_match.group(1).strip() if action_match else "Continuar implementação da task atual"
        
        print("🎯 **SUA ÚNICA MICRO-AÇÃO AGORA (5-10 min):**")
        print(f"👉 **{active_action}**\n")
        print("🧭 **Matriz Eisenhower Enxuta:**")
        print("• 🔥 **Fazer AGORA:** Resolver foco único acima")
        print("• 📅 **Depois:** Itens secundários guardados no Notion")
        print("• 🛡️ **Ideia Paralela?** Anote no Estacionamento de Ideias e continue!\n")
        print("🤝 **Body Doubling:** Estou aqui com você. Quando terminar, me avise para marcarmos como feito!")
    else:
        print("⚠️ Painel de foco não encontrado. Criando modelo base...")
        template_adhd = Path(__file__).resolve().parent.parent / "templates" / "markdown" / "adhd_orbit_os_template.md"
        if template_adhd.exists():
            adhd_file.parent.mkdir(parents=True, exist_ok=True)
            adhd_file.write_text(template_adhd.read_text(encoding="utf-8"), encoding="utf-8")
            print("✅ Painel criado! Execute '/second-brain tdah' novamente.")
    print("=" * 65 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Second Brain Plus Command Interface (/second-brain)")
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # install
    subparsers.add_parser("install", help="Install & scaffold Second Brain local vault and Notion databases")

    # save memory
    p_save = subparsers.add_parser("save", help="Save knowledge or memories")
    p_save.add_argument("category", choices=["memory", "fact", "note"], help="Category of item to save")
    p_save.add_argument("text", nargs="+", help="Content to store in persistent memory")

    # adr
    p_adr = subparsers.add_parser("adr", help="Record an Architecture Decision Record")
    p_adr.add_argument("title", help="Title of the decision")
    p_adr.add_argument("--rationale", default="", help="Detailed explanation or context")

    # sync
    subparsers.add_parser("sync", help="Trigger immediate multi-agent synchronization")

    # status
    subparsers.add_parser("status", help="Show system and synchronization status")

    # focus / tdah / adhd
    subparsers.add_parser("focus", help="Display ADHD single-task atomic focus panel")
    subparsers.add_parser("tdah", help="Ativa modo TDAH com formatação biônica e foco atômico (Orbit OS)")
    subparsers.add_parser("adhd", help="Activate ADHD mode with bionic formatting and atomic focus (Orbit OS)")

    # git-status / git-sync
    subparsers.add_parser("git-status", help="Audit GitHub (gh) and GitLab (glab) remote synchronization status")
    p_git_sync = subparsers.add_parser("git-sync", help="Commit and push second brain changes to Git remote")
    p_git_sync.add_argument("--message", "-m", default="chore(brain): automated second-brain sync", help="Commit message")

    args = parser.parse_args()

    if args.command == "install":
        cmd_install(args)
    elif args.command == "save":
        cmd_save_memory(" ".join(args.text))
    elif args.command == "adr":
        cmd_save_adr(args.title, args.rationale)
    elif args.command == "sync":
        auto_sync.execute_full_sync(get_vault_dir())
    elif args.command == "status":
        cmd_status()
    elif args.command in ["focus", "tdah", "adhd"]:
        cmd_tdah_focus()
    elif args.command == "git-status":
        git_remote_sync.GitRemoteManager().print_audit_report()
    elif args.command == "git-sync":
        git_remote_sync.GitRemoteManager().sync_to_remote(args.message)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
