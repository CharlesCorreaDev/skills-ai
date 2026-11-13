#!/usr/bin/env python3
"""
apply_full_dashboard.py - Apply complete Second Brain Plus visual layout to Notion page
Aplica o layout visual completo do Second Brain Plus na página de Desenvolvimento do Foundry VTT.
"""

import os
import json
import urllib.request
import urllib.error
from pathlib import Path

def load_env_credentials():
    token = os.environ.get("NOTION_API_KEY")
    page_id = os.environ.get("NOTION_PARENT_PAGE_ID")
    
    # Try local .env or .env_local
    for env_name in [".env", ".env_local"]:
        p = Path.cwd() / env_name
        if p.exists():
            for line in p.read_text(encoding="utf-8").splitlines():
                if "=" in line and not line.startswith("#"):
                    k, v = line.split("=", 1)
                    if k.strip() == "NOTION_API_KEY" and not token:
                        token = v.strip()
                    elif k.strip() == "NOTION_PARENT_PAGE_ID" and not page_id:
                        page_id = v.strip()
    return token, page_id

token, page_id = load_env_credentials()

headers = {
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def patch_endpoint(endpoint, payload):
    url = f"https://api.notion.com/v1/{endpoint.lstrip('/')}"
    req = urllib.request.Request(url, headers=headers, data=json.dumps(payload).encode("utf-8"), method="PATCH")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def apply_styling():
    print("🎨 1. Atualizando Ícone, Capa e Título da Página...")
    page_props = {
        "properties": {
            "title": {
                "title": [{"type": "text", "text": {"content": "Desenvolvimento Foundry VTT | Second Brain"}}]
            }
        },
        "icon": {"type": "emoji", "emoji": "🎲"},
        "cover": {
            "type": "external",
            "external": {
                "url": "https://images.unsplash.com/photo-1610890716171-6b1bb98ffd09?auto=format&fit=crop&w=2000&q=80"
            }
        }
    }
    patch_endpoint(f"pages/{page_id}", page_props)
    print("  ✓ Capa e ícone atualizados com sucesso!")

    # 1. Start Blocks (Header Callouts & Project Section Heading)
    print("🧠 2. Inserindo Callouts de Boas-Vindas e Painel TDAH no topo...")
    start_blocks = [
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "⚡ Desenvolvimento Foundry VTT — Second Brain Plus Hub\n"},
                        "annotations": {"bold": True}
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "• SSOT (Single Source of Truth): Sincronização automática contínua entre cofre local (.second-brain/), Graphify, claude-mem e Notion Cloud.\n"
                                       "• Metodologia P.A.R.A. 2.0: Projetos, Áreas de Responsabilidade, Recursos/ADRs e Arquivos.\n"
                                       "• Anti-Alucinação: Decisões de arquitetura (ADRs) persistentes e consultadas em todas as sessões de IA."
                        }
                    }
                ],
                "icon": {"type": "emoji", "emoji": "🧠"},
                "color": "blue_background"
            }
        },
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "🎯 Painel de Ações Rápidas & Foco Cognitivo\n"},
                        "annotations": {"bold": True}
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "• Agendar Tarefa: /second-brain task \"Nome da Tarefa\" --p1 (divide em 4 micro-passos de 5-10 min)\n"
                                       "• Registrar Decisão: /second-brain adr \"Título da Decisão Técnica\"\n"
                                       "• Salvar Fato/Regra: /second-brain save memory \"Fato permanente\"\n"
                                       "• Modo Foco Neurodivergente: /second-brain focus ou /tdah\n"
                                       "• Sincronizar Tudo: /second-brain sync"
                        }
                    }
                ],
                "icon": {"type": "emoji", "emoji": "⚡"},
                "color": "purple_background"
            }
        },
        {"object": "block", "type": "divider", "divider": {}},
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "🚀 Gestão de Projetos & Sprints (PARA: Projects)"},
                        "annotations": {"bold": True}
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "Central de planejamento de módulos, sistemas, pacotes e compêndios do Foundry VTT v14."},
                        "annotations": {"italic": True, "color": "gray"}
                    }
                ]
            }
        }
    ]
    patch_endpoint(f"blocks/{page_id}/children", {
        "children": start_blocks,
        "position": {"type": "start"}
    })
    print("  ✓ Topo do Dashboard estruturado com sucesso!")

    # 2. Section 2: Decisions & ADRs (after Projects DB: 417ec870-8531-8195-a083-f4de6a88b1ae)
    print("🛡️ 3. Formatando Seção de Decisões & ADRs...")
    adrs_blocks = [
        {"object": "block", "type": "divider", "divider": {}},
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "🛡️ Base de Decisões de Arquitetura & ADRs (Zero-Hallucination)"},
                        "annotations": {"bold": True}
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "Registro imutável de decisões técnicas e contratos de API para blindar o desenvolvimento contra amnésia."},
                        "annotations": {"italic": True, "color": "gray"}
                    }
                ]
            }
        }
    ]
    patch_endpoint(f"blocks/{page_id}/children", {
        "children": adrs_blocks,
        "after": "417ec870-8531-8195-a083-f4de6a88b1ae"
    })

    # 3. Section 3: Session Logs (after Decisions DB: 417ec870-8531-81f5-9726-de2c775ad2c8)
    print("⏱️ 4. Formatando Seção de Memórias Episódicas...")
    session_blocks = [
        {"object": "block", "type": "divider", "divider": {}},
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "⏱️ Sessões de IA & Memórias Episódicas (claude-mem)"},
                        "annotations": {"bold": True}
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "Linha do tempo contínua de sessões, marcos alcançados e decisões históricas gravadas pelo claude-mem."},
                        "annotations": {"italic": True, "color": "gray"}
                    }
                ]
            }
        }
    ]
    patch_endpoint(f"blocks/{page_id}/children", {
        "children": session_blocks,
        "after": "417ec870-8531-81f5-9726-de2c775ad2c8"
    })

    # 4. Section 4: Resources & Knowledge Graph (after Session Logs DB: 417ec870-8531-8149-903a-e0e07bd1fc06)
    print("📚 5. Formatando Seção de Recursos & Grafo de Conhecimento...")
    resources_blocks = [
        {"object": "block", "type": "divider", "divider": {}},
        {
            "object": "block",
            "type": "heading_2",
            "heading_2": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "📚 Recursos & Grafo de Conhecimento (Graphify & Context7)"},
                        "annotations": {"bold": True}
                    }
                ]
            }
        },
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "Documentação canônica de APIs v14 (ApplicationV2, DataModel), cheatsheets e grafo semântico de código."},
                        "annotations": {"italic": True, "color": "gray"}
                    }
                ]
            }
        }
    ]
    patch_endpoint(f"blocks/{page_id}/children", {
        "children": resources_blocks,
        "after": "417ec870-8531-8149-903a-e0e07bd1fc06"
    })

    # 5. Footer: Orbit OS Focus Guide (after Resources DB: 417ec870-8531-819c-8ab2-e25276c2b91a)
    print("🌱 6. Adicionando Guia de Foco e Ergonomia Cognitiva no rodapé...")
    footer_blocks = [
        {"object": "block", "type": "divider", "divider": {}},
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {"content": "🌱 Orbit OS — Ergonomia Cognitiva & Tolerância Zero a Bloqueios\n"},
                        "annotations": {"bold": True}
                    },
                    {
                        "type": "text",
                        "text": {
                            "content": "• Micro-Passos Atômicos: Cada tarefa é decomposta para eliminar a paralisia decisória e o sobrepeso cognitivo.\n"
                                       "• Duplicação de Corpo (Body Doubling): O agente de IA programa junto, testando e validando cada função em tempo real.\n"
                                       "• Modo Foco: Execute /second-brain focus para ativar a visualização de tarefa única atômica."
                        }
                    }
                ],
                "icon": {"type": "emoji", "emoji": "🎯"},
                "color": "green_background"
            }
        }
    ]
    patch_endpoint(f"blocks/{page_id}/children", {
        "children": footer_blocks,
        "after": "417ec870-8531-819c-8ab2-e25276c2b91a"
    })

    print("\n" + "=" * 65)
    print("✅ DASHBOARD DO SECOND BRAIN PLUS APLICADO COM SUCESSO NO NOTION!")
    print("=" * 65)

if __name__ == "__main__":
    apply_styling()
