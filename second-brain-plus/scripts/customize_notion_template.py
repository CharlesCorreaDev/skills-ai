import os
import urllib.request
import json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("NOTION_API_KEY")
headers = {
    "Authorization": f"Bearer {token}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

page_id = "45fec870-8531-8321-a294-8163f5dc870c"

def notion_patch(endpoint, data):
    url = f"https://api.notion.com/v1/{endpoint.lstrip('/')}"
    req = urllib.request.Request(url, headers=headers, data=json.dumps(data).encode("utf-8"), method="PATCH")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def notion_post(endpoint, data):
    url = f"https://api.notion.com/v1/{endpoint.lstrip('/')}"
    req = urllib.request.Request(url, headers=headers, data=json.dumps(data).encode("utf-8"), method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

print("1. Atualizando Título e Capa da Página Principal...")
page_payload = {
    "properties": {
        "title": {
            "title": [{"type": "text", "text": {"content": "Second Brain Plus | Hub de Produtividade & IA"}}]
        }
    },
    "icon": {
        "type": "emoji",
        "emoji": "🧠"
    },
    "cover": {
        "type": "external",
        "external": {
            "url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=2000&q=80"
        }
    }
}
try:
    notion_patch(f"/pages/{page_id}", page_payload)
    print("   ✓ Página principal atualizada (Título, Capa e Ícone).")
except Exception as e:
    print(f"   ⚠️ Erro ao atualizar página: {e}")

print("\n2. Traduzindo Headings (Títulos das Seções)...")
headings_map = {
    "8abec870-8531-821a-8814-019bd66cfaa3": "⚡ Ações Rápidas",
    "746ec870-8531-83ed-b6f3-019f43ee32e2": "🧭 Módulos & Navegação",
    "eafec870-8531-8269-a3f9-0176a8c20b7e": "⚙️ Infraestrutura & Backend",
    "67cec870-8531-826a-b399-0189a90a9905": "📊 Resumo Financeiro",
    "883ec870-8531-8357-aa5b-81b35f0a0c70": "🌐 Áreas de Responsabilidade (PARA)",
    "d23ec870-8531-83cb-9c2b-01b1d7565c6d": "🚀 Gestão de Projetos & Sprints",
    "ec7ec870-8531-82fc-99c2-01bd232b199a": "⚡ Tarefas a Fazer (Micro-Passos TDAH)",
    "df2ec870-8531-83e2-8026-01cbb71f0a97": "📚 Recursos & Conhecimento",
    "431ec870-8531-821c-859d-81fb21b572f3": "🔄 Rastreamento de Hábitos",
    "832ec870-8531-837d-a860-813b9018b41d": "📖 Diário & Sessões de IA",
    "472ec870-8531-8291-83df-819fa02d1828": "📝 Visão Geral de Notas & ADRs"
}

for b_id, title in headings_map.items():
    try:
        notion_patch(f"/blocks/{b_id}", {
            "heading_2": {
                "rich_text": [{"type": "text", "text": {"content": title}}]
            }
        })
        print(f"   ✓ Heading atualizado: {title}")
    except Exception as e:
        print(f"   ⚠️ Erro no heading {b_id}: {e}")

print("\n3. Traduzindo Subpáginas...")
pages_map = {
    "78bec870-8531-830d-bb36-8121b4c81947": ("📁 Projetos & Tarefas", "📁"),
    "3fcec870-8531-82e0-81af-0120258fbec4": ("📚 Recursos, ADRs & Notas", "📚"),
    "e71ec870-8531-83ac-a845-811effb3a14f": ("💰 Controle Financeiro", "💰"),
    "82dec870-8531-82ee-b7f6-01b9cf90acad": ("🌐 Áreas de Foco (PARA)", "🌐"),
    "a87ec870-8531-822a-909a-81d3fbbb6ed0": ("🔄 Hábitos Diários & Rotina", "🔄"),
    "6ceec870-8531-82a1-b39f-8171707743cb": ("📖 Diário de Bordo & Sessões", "📖")
}

for p_id, (p_title, p_icon) in pages_map.items():
    try:
        notion_patch(f"/pages/{p_id}", {
            "properties": {
                "title": {
                    "title": [{"type": "text", "text": {"content": p_title}}]
                }
            },
            "icon": {"type": "emoji", "emoji": p_icon}
        })
        print(f"   ✓ Subpágina atualizada: {p_title}")
    except Exception as e:
        print(f"   ⚠️ Erro na subpágina {p_id}: {e}")

print("\n4. Inserindo Callout de Boas-Vindas & Status TDAH...")
# Verificar se já existe callout no topo
callout_exists = False
url = f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=20"
req = urllib.request.Request(url, headers=headers)
with urllib.request.urlopen(req) as resp:
    existing_blocks = json.loads(resp.read().decode("utf-8")).get("results", [])
    for eb in existing_blocks:
        if eb.get("type") == "callout":
            callout_exists = True
            break

if not callout_exists:
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
        notion_patch(f"/blocks/{page_id}/children", callout_payload)
        print("   ✓ Callout de foco e status inserido com sucesso!")
    except Exception as e:
        print(f"   ⚠️ Erro ao inserir callout: {e}")
else:
    print("   ✓ Callout já presente.")
