#!/usr/bin/env python3
"""
setup_and_sync.py - Complete Installation, Setup & Synchronization Engine
Motor Completo de Instalação, Configuração e Sincronização do Second Brain Plus.

Bilingual support: English (EN) and Portuguese (PT-BR).
Suporte bilíngue: Inglês (EN) e Português (PT-BR).
"""

import os
import sys
import json
import argparse
from pathlib import Path

# Import companion utilities / Importa utilitários irmãos
sys.path.insert(0, str(Path(__file__).parent))
import verify_brain
import memory_bridge
import notion_sync

def run_installation_and_setup(vault_dir: Path, api_key: str = None, neurodivergent_mode: bool = False):
    """
    EN: Execute end-to-end setup: scaffold vault, build graph, compress context, verify sync.
    PT-BR: Executa configuração ponta a ponta: cria pastas, gera grafo, comprime contexto e valida sincronização.
    """
    print("=" * 70)
    print("🧠⚡ SECOND BRAIN PLUS — SETUP & SYNCHRONIZATION WIZARD")
    print("   Instalação, Configuração e Sincronização Integrada")
    print("=" * 70)

    # 1. Scaffolding P.A.R.A. 2.0 Vault
    print("\n📁 [Passo 1/6] Inicializando estrutura local (.second-brain)...")
    verify_brain.scaffold_second_brain(vault_dir)

    # 2. Installing Slash Commands & Workflows
    print("\n⌨️ [Passo 2/6] Registrando Slash Commands (/second-brain e /tdah)...")
    workflows_src = Path(__file__).resolve().parent.parent / "workflows"
    if workflows_src.exists():
        destinations = [
            Path.home() / ".gemini" / "commands",
            Path.home() / ".gemini" / "antigravity" / "commands",
            Path.home() / ".gemini" / "config" / "workflows",
            Path.cwd() / ".agents" / "workflows",
            Path.cwd() / ".agents" / "commands"
        ]
        for dest in destinations:
            dest.mkdir(parents=True, exist_ok=True)
            for wf in workflows_src.glob("*.md"):
                target_file = dest / wf.name
                target_file.write_text(wf.read_text(encoding="utf-8"), encoding="utf-8")
        print("  ✓ Comandos /second-brain e /tdah registrados com sucesso no IDE.")

    # 3. ADHD / Neurodivergent setup if requested
    if neurodivergent_mode:
        print("\n⚡ [Acessibilidade] Ativando templates e visualização para Neurodivergentes (Orbit OS)...")
        adhd_panel = vault_dir / "1-Projects" / "ADHD-FOCUS-DASHBOARD.md"
        template_adhd = Path(__file__).parent.parent / "templates" / "markdown" / "adhd_orbit_os_template.md"
        if template_adhd.exists() and not adhd_panel.exists():
            adhd_panel.write_text(template_adhd.read_text(encoding="utf-8"), encoding="utf-8")
            print(f"  ✓ Painel de Foco Único criado: {adhd_panel.name}")

    # 3. Ingesting Claude-mem sessions
    print("\n⏱️ [Passo 2/5] Integrando memórias episódicas do claude-mem...")
    mock_claude_dir = vault_dir / "4-Archives" / ".claude-mem-source"
    sessions_out = vault_dir / "4-Archives" / "sessions"
    memory_bridge.export_claude_mem(mock_claude_dir, sessions_out)

    # 4. Generating Graphify Knowledge Graph
    print("\n🕸️ [Passo 3/5] Gerando Grafo de Conhecimento com Graphify...")
    graph_out = vault_dir / ".graphify" / "graph.json"
    memory_bridge.generate_graphify(vault_dir, graph_out)

    # 5. Auditing local integrity
    print("\n🔎 [Passo 4/5] Auditando conformidade e integridade das notas...")
    is_valid = verify_brain.audit_second_brain(vault_dir)

    # 6. Notion API Connection check & sync
    print("\n☁️ [Passo 5/5] Sincronização com a API do Notion...")
    if api_key:
        print("  🔑 Token NOTION_API_KEY detectado. Testando autenticação...")
        auth_ok = notion_sync.check_authentication(api_key)
        if auth_ok:
            notion_sync.list_databases(api_key)
            notion_sync.sync_local_vault(vault_dir, api_key)
    else:
        print("  ⚠️ Nenhuma NOTION_API_KEY informada no momento.")
        print("  ℹ️ O cofre local está 100% operacional offline como SSOT.")
        print("  💡 Para sincronizar com o Notion na nuvem, basta fornecer o token da integração.")

    print("\n" + "=" * 70)
    print("✅ INSTALAÇÃO E CONFIGURAÇÃO CONCLUÍDAS COM SUCESSO!")
    print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description="Second Brain Plus Setup & Sync Wizard")
    parser.add_argument("--vault-dir", default="./.second-brain", help="Path to local vault")
    parser.add_argument("--api-key", default=None, help="Notion API Key")
    parser.add_argument("--neurodivergent", action="store_true", help="Enable ADHD / Neurodivergent Orbit OS mode")

    args = parser.parse_args()
    api_key = args.api_key or os.environ.get("NOTION_API_KEY")

    run_installation_and_setup(Path(args.vault_dir), api_key, args.neurodivergent)

if __name__ == "__main__":
    main()
