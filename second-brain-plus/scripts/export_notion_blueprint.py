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

root_page_id = "45fec870-8531-8321-a294-8163f5dc870c"
output_dir = Path(__file__).resolve().parent.parent / "templates" / "notion"
output_dir.mkdir(parents=True, exist_ok=True)
blueprint_file = output_dir / "second_brain_blueprint.json"

def get_block(block_id):
    url = f"https://api.notion.com/v1/blocks/{block_id}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

def get_children(block_id):
    url = f"https://api.notion.com/v1/blocks/{block_id}/children?page_size=100"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8")).get("results", [])

def get_database(db_id):
    url = f"https://api.notion.com/v1/databases/{db_id}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))

print(f"📦 Exportando Blueprint do Second Brain Plus a partir da página: {root_page_id}...")

blueprint = {
    "version": "1.0.0",
    "exported_at": "2026-11-13T17:35:00Z",
    "root_page": {
        "title": "Second Brain Plus | Hub de Produtividade & IA",
        "icon": "🧠",
        "cover": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=2000&q=80"
    },
    "databases": {},
    "subpages": {},
    "layout_blocks": []
}

# 1. Export Master Databases from Backend
master_dbs = {
    "projects": "eb4ec870-8531-822f-be6c-018002a6a3ce",
    "tasks": "741ec870-8531-8318-8583-81f96fcab4cd",
    "notes": "622ec870-8531-8354-881f-0139fadeeea0",
    "resources": "5f3ec870-8531-83b6-acd3-818f1b8e0675",
    "areas": "090ec870-8531-832d-a6f2-8107c51cafc1",
    "habits": "0faec870-8531-82b5-9f61-81fc662947aa",
    "journal": "1efec870-8531-8284-8153-01d5be01e3df"
}

for db_alias, db_id in master_dbs.items():
    try:
        db_data = get_database(db_id)
        title = "".join([t.get("plain_text", "") for t in db_data.get("title", [])])
        blueprint["databases"][db_alias] = {
            "title": title,
            "properties": db_data.get("properties", {})
        }
        print(f"  ✓ Banco mestre exportado: {title} ({db_alias})")
    except Exception as e:
        print(f"  ⚠️ Erro ao exportar banco {db_alias}: {e}")

# 2. Export Subpages Metadata
subpages = {
    "projects_tasks": "78bec870-8531-830d-bb36-8121b4c81947",
    "resources_notes": "3fcec870-8531-82e0-81af-0120258fbec4",
    "areas": "82dec870-8531-82ee-b7f6-01b9cf90acad",
    "habits": "a87ec870-8531-822a-909a-81d3fbbb6ed0",
    "journal": "6ceec870-8531-82a1-b39f-8171707743cb"
}

for sp_alias, sp_id in subpages.items():
    try:
        url = f"https://api.notion.com/v1/pages/{sp_id}"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as resp:
            sp_data = json.loads(resp.read().decode("utf-8"))
            sp_title = ""
            for pk, pv in sp_data.get("properties", {}).items():
                if pv.get("type") == "title":
                    sp_title = "".join([x.get("plain_text", "") for x in pv.get("title", [])])
            cover_obj = sp_data.get("cover") or {}
            cover_url = cover_obj.get("external", {}).get("url", "")
            icon_obj = sp_data.get("icon") or {}
            icon_val = icon_obj.get("emoji") or icon_obj.get("icon", {}).get("name", "📄")
            blueprint["subpages"][sp_alias] = {
                "title": sp_title,
                "icon": icon_val,
                "cover": cover_url
            }
            print(f"  ✓ Subpágina exportada: {sp_title} ({sp_alias})")
    except Exception as e:
        print(f"  ⚠️ Erro na subpágina {sp_alias}: {e}")

# Save JSON Blueprint
blueprint_file.write_text(json.dumps(blueprint, indent=2, ensure_ascii=False), encoding="utf-8")
print(f"\n✅ Blueprint exportado com sucesso em: {blueprint_file}")
