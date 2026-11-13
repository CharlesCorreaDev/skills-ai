#!/usr/bin/env python3
"""
build_notion_dashboard.py - Transforms Notion page into Second Brain All-in-One 2026 Layout
Constrói o layout visual completo do Second Brain All-in-One Productivity System 2026 no Notion.
"""

import os
import json
import urllib.request
import urllib.error
from pathlib import Path

def build_dashboard():
    token = os.environ.get("NOTION_API_KEY")
    page_id = os.environ.get("NOTION_PARENT_PAGE_ID", "417ec870-8531-80b7-9384-cfbd68dd0711")

    headers = {
        "Authorization": f"Bearer {token}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }

    print("🧠 Atualizando capa e ícone da página...")
    page_update = {
        "icon": {"type": "emoji", "emoji": "🧠"},
        "cover": {
            "type": "external",
            "external": {"url": "https://images.unsplash.com/photo-1507842229451-7f01be7ff60b?auto=format&fit=crop&w=2000&q=80"}
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
            print("  ✓ Capa e ícone atualizados com sucesso!")
    except urllib.error.HTTPError as e:
        print(f"  ⚠️ Erro na atualização da página: {e.code}")

    print("🎨 Construindo blocos visuais do Second Brain All-in-One 2026...")
    blocks = [
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "SECOND BRAIN ALL-IN-ONE PRODUCTIVITY SYSTEM 2026\n"},
                        "annotations": {"bold": True}
                    },
                    {
                        "type": "text",
                        "text": {"content": "Central de Produtividade P.A.R.A. 2.0 • Memória Persistente de IA • Anti-Alucinação"}
                    }
                ],
                "icon": {"emoji": "🧠"},
                "color": "gray_background"
            }
        },
        {
            "object": "block",
            "type": "quote",
            "quote": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "Sua mente é para ter ideias, não para guardá-las. — David Allen & Tiago Forte"},
                        "annotations": {"italic": True}
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "divider",
            "divider": {}
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "🧭 Central de Navegação P.A.R.A. 2.0"}
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "🚀 1. PROJETOS (Projects): "},
                        "annotations": {"bold": True}
                    },
                    {
                        "type": "text",
                        "text": {"content": "Metas ativas e sprints com prazo de entrega imediato.\n"}
                    },
                    {
                        "type": "text",
                        "text": {"content": "🎯 2. ÁREAS (Areas): "},
                        "annotations": {"bold": True}
                    },
                    {
                        "type": "text",
                        "text": {"content": "Padrões de engenharia, arquiteturas e responsabilidades contínuas.\n"}
                    },
                    {
                        "type": "text",
                        "text": {"content": "📚 3. RECURSOS (Resources): "},
                        "annotations": {"bold": True}
                    },
                    {
                        "type": "text",
                        "text": {"content": "Documentações de APIs, referências, prompts e grafo de conhecimento.\n"}
                    },
                    {
                        "type": "text",
                        "text": {"content": "📦 4. ARQUIVOS (Archives): "},
                        "annotations": {"bold": True}
                    },
                    {
                        "type": "text",
                        "text": {"content": "Logs de sessões concluídas, ADRs inativos e histórico de aprendizado."}
                    }
                ],
                "icon": {"emoji": "🗺️"},
                "color": "blue_background"
            }
        },
        {
            "object": "block",
            "type": "divider",
            "divider": {}
        },
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "⚡ MODO FOCO ATÔMICO (Orbit OS / TDAH):\n"},
                        "annotations": {"bold": True}
                    },
                    {
                        "type": "text",
                        "text": {"content": "Execute apenas 1 micro-tarefa por vez (5 a 10 min) para eliminar a paralisia de decisão. Use os comandos /second-brain focus ou /second-brain tdah no seu chat de IA."}
                    }
                ],
                "icon": {"emoji": "🎯"},
                "color": "orange_background"
            }
        },
        {
            "object": "block",
            "type": "divider",
            "divider": {}
        },
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "📊 Bancos de Dados Relacionais & Memória Persistente"}
                    }
                ]
            }
        }
    ]

    req_blocks = urllib.request.Request(
        f"https://api.notion.com/v1/blocks/{page_id}/children",
        data=json.dumps({"children": blocks}).encode("utf-8"),
        headers=headers,
        method="PATCH"
    )
    try:
        with urllib.request.urlopen(req_blocks) as resp:
            print("  ✓ Blocos visuais adicionados com sucesso ao Notion!")
            return True
    except urllib.error.HTTPError as e:
        print(f"  ⚠️ Erro ao adicionar blocos: {e.code} - {e.read().decode('utf-8')}")
        return False

if __name__ == "__main__":
    build_dashboard()
