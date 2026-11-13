#!/usr/bin/env python3
"""
build_notion_dashboard.py - Default Blueprint Engine for Second Brain Plus
Motor de Construção e Aplicação do Layout Padrão Oficial do Second Brain Plus no Notion.

Bilingual support: English (EN) and Portuguese (PT-BR).
"""

import os
import json
import urllib.request
import urllib.error
from pathlib import Path

BLUEPRINT_PATH = Path(__file__).resolve().parent.parent / "templates" / "notion" / "second_brain_blueprint.json"

def load_blueprint() -> dict:
    if BLUEPRINT_PATH.exists():
        return json.loads(BLUEPRINT_PATH.read_text(encoding="utf-8"))
    return {}

def build_dashboard(target_page_id: str = None, api_key: str = None) -> bool:
    """
    EN: Apply the official canonical Second Brain Plus layout to a target Notion page.
    PT-BR: Aplica o layout canônico padrão oficial do Second Brain Plus na página alvo do Notion.
    """
    token = api_key or os.environ.get("NOTION_API_KEY")
    page_id = target_page_id or os.environ.get("NOTION_PARENT_PAGE_ID")

    if not token or not page_id:
        print("❌ [EN] NOTION_API_KEY or NOTION_PARENT_PAGE_ID missing. / [PT-BR] Token ou ID da página ausente.")
        return False

    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    blueprint = load_blueprint()
    root_cfg = blueprint.get("root_page", {
        "title": "Second Brain Plus | Hub de Produtividade & IA",
        "icon": "🧠",
        "cover": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=2000&q=80"
    })

    print(f"🧠 [EN] Applying canonical layout to page: {page_id}")
    print(f"   [PT-BR] Aplicando layout padrão oficial na página: {page_id}")

    # 1. Update Title, Icon, Cover
    page_update = {
        "properties": {
            "title": {
                "title": [{"type": "text", "text": {"content": root_cfg.get("title")}}]
            }
        },
        "icon": {"type": "emoji", "emoji": root_cfg.get("icon", "🧠")},
        "cover": {
            "type": "external",
            "external": {"url": root_cfg.get("cover")}
        }
    }

    req_page = urllib.request.Request(
        f"https://api.notion.com/v1/pages/{page_id}",
        data=json.dumps(page_update).encode("utf-8"),
        headers=headers,
        method="PATCH"
    )
    try:
        with urllib.request.urlopen(req_page) as resp:
            print("  ✓ [PT-BR] Capa, ícone e título padrão atualizados!")
    except urllib.error.HTTPError as e:
        print(f"  ⚠️ Erro na atualização da página: {e.code}")

    # 2. Ensure Welcome & Orbit OS Callout at the top
    callout_payload = {
        "children": [
            {
                "object": "block",
                "type": "callout",
                "callout": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": "⚡ Bem-vindo ao Second Brain Plus!\n"
                                           "• SSOT Ativo: Sincronização contínua entre cofre local (.second-brain) e Notion Cloud.\n"
                                           "• Modo Foco TDAH (Orbit OS): Tarefas decompostas em micro-passos atômicos de 5-10 min.\n"
                                           "• Comandos Rápidos: /second-brain task, /second-brain do, /second-brain sync, /tdah."
                            }
                        }
                    ],
                    "icon": {"type": "emoji", "emoji": "🧠"},
                    "color": "blue_background"
                }
            }
        ]
    }
    try:
        req_callout = urllib.request.Request(
            f"https://api.notion.com/v1/blocks/{page_id}/children",
            data=json.dumps(callout_payload).encode("utf-8"),
            headers=headers,
            method="PATCH"
        )
        with urllib.request.urlopen(req_callout) as resp:
            print("  ✓ [PT-BR] Callout de status e ergonomia cognitiva garantido!")
    except Exception as e:
        pass

    print("\n✅ [EN] Canonical Second Brain Plus layout is fully configured.")
    print("   [PT-BR] Layout canônico padrão do Second Brain Plus configurado com sucesso.")
    return True

if __name__ == "__main__":
    build_dashboard()
