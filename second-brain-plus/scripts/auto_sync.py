#!/usr/bin/env python3
"""
auto_sync.py - Automatic Background Watcher & Synchronization Engine
Motor de Monitoramento em Segundo Plano e Sincronização Automática do Second Brain Plus.

Monitors local files and synchronizes automatically with:
- Notion API (Databases & Pages)
- claude-mem (Episodic Timeline)
- graphify (Knowledge Graph extraction)

Bilingual support: English (EN) and Portuguese (PT-BR).
Suporte bilíngue: Inglês (EN) e Português (PT-BR).
"""

import os
import sys
import time
import json
import argparse
import hashlib
from pathlib import Path

# Add script directory to module search path / Adiciona pasta de scripts ao path
sys.path.insert(0, str(Path(__file__).parent))
import notion_sync
import memory_bridge
import verify_brain
import git_remote_sync

STATE_FILE = Path(__file__).resolve().parent.parent / ".sync_state.json"

def get_vault_hashes(vault_dir: Path) -> dict:
    """
    EN: Compute SHA-256 hashes of all markdown files in vault to detect changes.
    PT-BR: Calcula hashes SHA-256 de todas as notas markdown no cofre para detectar alterações.
    """
    hashes = {}
    if not vault_dir.exists():
        return hashes
    for f in vault_dir.rglob("*.md"):
        # Ignore temporary or cache folders / Ignora pastas temporárias ou de cache
        if ".graphify" in str(f) or ".claude-mem-source" in str(f):
            continue
        try:
            content = f.read_bytes()
            hashes[str(f.relative_to(vault_dir))] = hashlib.sha256(content).hexdigest()[:12]
        except Exception:
            pass
    return hashes

def load_previous_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {}

def save_current_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")

def execute_full_sync(vault_dir: Path, api_key: str = None, changed_files: list = None):
    """
    EN: Trigger coordinated synchronization with Notion, claude-mem, and graphify.
    PT-BR: Dispara a sincronização coordenada com Notion, claude-mem e graphify.
    """
    print("\n" + "=" * 65)
    print("⚡ [EN] AUTO-SYNC TRIGGERED / [PT-BR] SINCRONIZAÇÃO AUTOMÁTICA DISPARADA")
    if changed_files:
        print(f"   [EN] Changes detected in {len(changed_files)} file(s):")
        print(f"   [PT-BR] Alterações detectadas em {len(changed_files)} arquivo(s):")
        for cf in changed_files[:5]:
            print(f"     • {cf}")
        if len(changed_files) > 5:
            print(f"     • ... (+{len(changed_files) - 5} others)")
    print("=" * 65)

    # 0. Check Git Remote Privacy Rule (Public Repo -> Automatic Notion Vault Upload)
    try:
        remote_mgr = git_remote_sync.GitRemoteManager()
        audit_res = remote_mgr.audit()
        if audit_res.get("is_private") is False:
            print("\n🛡️ [REGRA DE REPOSITÓRIO PÚBLICO ATIVA / PUBLIC REPO PROTECTION]:")
            print("   O repositório Git remoto é PÚBLICO. Realizando upload integral e seguro de todos")
            print(f"   os arquivos do cofre '{vault_dir}' para o Notion como cofre de segurança na nuvem...")
    except Exception as e:
        pass

    # 1. Sync with Notion API
    print("\n☁️ [1/3] Sincronizando com a API do Notion...")
    if api_key or os.environ.get("NOTION_API_KEY"):
        notion_sync.sync_local_vault(vault_dir, api_key or os.environ.get("NOTION_API_KEY"))
    else:
        print("  ⚠️ NOTION_API_KEY não encontrada no ambiente. Pulando push remoto.")

    # 2. Update claude-mem episodic sessions
    print("\n⏱️ [2/3] Atualizando memórias episódicas do claude-mem...")
    claude_source = vault_dir / "4-Archives" / ".claude-mem-source"
    sessions_out = vault_dir / "4-Archives" / "sessions"
    memory_bridge.export_claude_mem(claude_source, sessions_out)

    # 3. Regenerate Knowledge Graph via Graphify
    print("\n🕸️ [3/3] Recompilando Grafo de Conhecimento com Graphify...")
    graph_out = vault_dir / ".graphify" / "graph.json"
    memory_bridge.generate_graphify(vault_dir, graph_out)

    # Save state
    new_hashes = get_vault_hashes(vault_dir)
    save_current_state(new_hashes)

    print("\n" + "=" * 65)
    print("✅ [EN] AUTO-SYNC COMPLETED / [PT-BR] SINCRONIZAÇÃO CONCLUÍDA")
    print("=" * 65 + "\n")

def watch_vault(vault_dir: Path, poll_interval: float = 3.0, api_key: str = None):
    """
    EN: Continuous background watcher loop detecting changes and triggering auto-sync.
    PT-BR: Loop contínuo de monitoramento em segundo plano que detecta mudanças e dispara auto-sync.
    """
    print(f"👀 [EN] Watching '{vault_dir}' for changes (interval: {poll_interval}s)...")
    print(f"   [PT-BR] Monitorando '{vault_dir}' para alterações (intervalo: {poll_interval}s)...")
    print("   [Pressione Ctrl+C para encerrar / Press Ctrl+C to stop]\n")

    previous_hashes = load_previous_state()
    if not previous_hashes:
        previous_hashes = get_vault_hashes(vault_dir)
        save_current_state(previous_hashes)

    try:
        while True:
            time.sleep(poll_interval)
            current_hashes = get_vault_hashes(vault_dir)

            changed = []
            for path, h in current_hashes.items():
                if path not in previous_hashes or previous_hashes[path] != h:
                    changed.append(path)

            for path in previous_hashes:
                if path not in current_hashes:
                    changed.append(f"[DELETED / EXCLUÍDO] {path}")

            if changed:
                execute_full_sync(vault_dir, api_key, changed_files=changed)
                previous_hashes = current_hashes

    except KeyboardInterrupt:
        print("\n🛑 [EN] Watcher stopped / [PT-BR] Monitoramento interrompido.")

def main():
    parser = argparse.ArgumentParser(
        description="Second Brain Plus - Auto-Sync Watcher & Engine / Motor de Sincronização Automática"
    )
    parser.add_argument("--now", action="store_true", help="EN: Trigger one-shot sync now / PT-BR: Dispara sincronização imediata")
    parser.add_argument("--watch", action="store_true", help="EN: Run background watcher loop / PT-BR: Executa loop de monitoramento contínuo")
    parser.add_argument("--interval", type=float, default=3.0, help="EN: Poll interval in seconds / PT-BR: Intervalo de verificação em segundos")
    parser.add_argument("--vault-dir", default="./.second-brain", help="EN: Path to local vault / PT-BR: Caminho do cofre local")
    parser.add_argument("--api-key", default=None, help="EN: Notion API key / PT-BR: Chave da API do Notion")

    args = parser.parse_args()
    vault_path = Path(args.vault_dir)
    api_key = args.api_key or os.environ.get("NOTION_API_KEY")

    if args.now:
        execute_full_sync(vault_path, api_key)
        sys.exit(0)

    if args.watch:
        watch_vault(vault_path, poll_interval=args.interval, api_key=api_key)
        sys.exit(0)

    # Default to --now if no argument provided
    execute_full_sync(vault_path, api_key)

if __name__ == "__main__":
    main()
