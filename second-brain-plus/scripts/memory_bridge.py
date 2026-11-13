#!/usr/bin/env python3
"""
memory_bridge.py - Multi-Agent Memory Bridge for Second Brain Plus
Ponte de Memória Multi-Agente para o Second Brain Plus.

Integrates with:
- claude-mem: Episodic session log ingestion.
- graphify: Lightweight Knowledge Graph generator (nodes & edges).
- caveman: Hyper-dense context compression.
- grill-me: Pre-decision inquiry distillation into formal ADRs.

Bilingual support: English (EN) and Portuguese (PT-BR).
Suporte bilíngue: Inglês (EN) e Português (PT-BR).
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path

def compress_caveman(text: str) -> tuple[str, float]:
    """
    EN: Compress text using Caveman dialect, removing conversational filler and conversational fluff.
    PT-BR: Comprime o texto utilizando o dialeto Caveman, removendo conectivos conversacionais supérfluos.
    """
    lines = text.strip().split("\n")
    compressed_lines = []
    
    stop_phrases = [
        r"você poderia", r"gostaria de saber", r"nesta sessão nós",
        r"vamos começar com", r"por favor", r"com certeza", r"espero que ajude",
        r"could you please", r"in this session we", r"let's proceed with",
        r"i would like to", r"feel free to"
    ]
    
    for line in lines:
        line_clean = line.strip()
        if not line_clean:
            continue
        for p in stop_phrases:
            line_clean = re.sub(p, "", line_clean, flags=re.IGNORECASE)
        line_clean = re.sub(r"\s+", " ", line_clean).strip()
        if line_clean:
            compressed_lines.append(line_clean)
            
    compressed_text = "\n".join(compressed_lines)
    orig_len = max(len(text), 1)
    new_len = len(compressed_text)
    compression_ratio = round((1 - (new_len / orig_len)) * 100, 1)
    return compressed_text, max(0.0, compression_ratio)

def export_claude_mem(claude_dir: Path, output_dir: Path):
    """
    EN: Read claude-mem episodic sessions and export as standardized Markdown logs.
    PT-BR: Lê as sessões episódicas do claude-mem e exporta como logs estruturados em Markdown.
    """
    print(f"🔍 [EN] Scanning claude-mem in '{claude_dir}' / [PT-BR] Buscando sessões do claude-mem em '{claude_dir}'...")
    if not claude_dir.exists():
        print(f"⚠️ [EN] Path not found. Creating mock sample. / [PT-BR] Caminho não encontrado. Criando exemplo de teste.")
        claude_dir.mkdir(parents=True, exist_ok=True)
        sample = claude_dir / "sample_session.json"
        sample.write_text(json.dumps({
            "session_id": "sess-20261113-001",
            "date": "2026-11-13",
            "summary": "Second Brain Plus setup and Notion API synchronization.",
            "commands": ["python notion_sync.py", "git status"],
            "observations": ["Notion API returned HTTP 200", "Local vault synchronized"]
        }, indent=2), encoding="utf-8")
        
    session_files = list(claude_dir.glob("*.json"))
    output_dir.mkdir(parents=True, exist_ok=True)
    
    converted = 0
    for sf in session_files:
        try:
            data = json.loads(sf.read_text(encoding="utf-8"))
            sid = data.get("session_id", sf.stem)
            date = data.get("date", "2026-11-13")
            summary = data.get("summary", "No summary provided / Sem resumo disponível.")
            obs = data.get("observations", [])
            
            md_content = f"""---
id: "{sid}"
title: "Claude Session: {sid}"
type: "session-log"
date: "{date}"
agent: "Claude Code"
source: "claude-mem"
---

# ⏱️ Claude-Mem Session: {sid}

## 🎯 Summary / Resumo
{summary}

## 🔍 Observations / Observações
""" + "\n".join(f"- {o}" for o in obs) + "\n"
            
            out_file = output_dir / f"{sid}.md"
            out_file.write_text(md_content, encoding="utf-8")
            converted += 1
            print(f"  ✓ [EN] Exported / [PT-BR] Exportado: {out_file.name}")
        except Exception as e:
            print(f"  ❌ [EN] Failed parsing / [PT-BR] Falha ao processar {sf.name}: {e}")
            
    print(f"✅ [EN] Successfully converted {converted} session(s). / [PT-BR] Convertida(s) com sucesso {converted} sessão(ões).")

def generate_graphify(vault_dir: Path, graph_output: Path):
    """
    EN: Extract knowledge graph nodes and edges from Markdown links and ADR references.
    PT-BR: Extrai nós e arestas de grafo de conhecimento a partir de links Markdown e menções a ADRs.
    """
    print(f"🕸️ [EN] Generating Graphify knowledge graph from '{vault_dir}' / [PT-BR] Gerando grafo de conhecimento do Graphify em '{vault_dir}'...")
    if not vault_dir.exists():
        print(f"❌ [EN] Directory does not exist / [PT-BR] Diretório não existe: {vault_dir}")
        return
        
    nodes = []
    edges = []
    
    md_files = list(vault_dir.rglob("*.md"))
    file_map = {f.stem.lower(): f for f in md_files}
    
    for f in md_files:
        content = f.read_text(encoding="utf-8", errors="ignore")
        node_id = f.stem
        id_m = re.search(r'^id:\s*["\']?([^"\']+)["\']?', content, re.MULTILINE)
        label = id_m.group(1) if id_m else node_id
        
        type_m = re.search(r'^type:\s*["\']?([^"\']+)["\']?', content, re.MULTILINE)
        node_type = type_m.group(1) if type_m else "note"
        
        nodes.append({"id": label, "file": str(f.name), "type": node_type})
        
        # Markdown links / Links em Markdown
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for link_text, link_target in links:
            target_stem = Path(link_target).stem.lower()
            if target_stem in file_map:
                edges.append({
                    "source": label,
                    "target": target_stem,
                    "relation": "references"
                })
                
        # ADR references / Referências a ADRs
        adrs = re.findall(r'\b(ADR-\d+)\b', content)
        for adr in set(adrs):
            if adr != label:
                edges.append({
                    "source": label,
                    "target": adr,
                    "relation": "governed_by_adr"
                })
                
    graph_data = {
        "generator": "Second Brain Plus - Graphify Bridge",
        "nodes_count": len(nodes),
        "edges_count": len(edges),
        "nodes": nodes,
        "edges": edges
    }
    
    graph_output.parent.mkdir(parents=True, exist_ok=True)
    graph_output.write_text(json.dumps(graph_data, indent=2), encoding="utf-8")
    print(f"✅ [EN] Graph generated: {len(nodes)} nodes, {len(edges)} edges saved to '{graph_output}' / [PT-BR] Grafo gerado: {len(nodes)} nós e {len(edges)} arestas.")

def distill_grill_session(input_text_or_path: str, output_path: str = None) -> str:
    """
    EN: Distill an interactive grill-me inquiry conversation into an Architecture Decision Record (ADR).
    PT-BR: Destila o inquérito de alinhamento do grill-me em um Architecture Decision Record (ADR) formal.
    """
    raw_text = Path(input_text_or_path).read_text(encoding="utf-8") if os.path.exists(input_text_or_path) else input_text_or_path
    
    adr_id = "ADR-GRILL-001"
    title_match = re.search(r'(?:título|decisão|assunto|subject|topic):\s*(.+)', raw_text, re.IGNORECASE)
    title = title_match.group(1).strip() if title_match else "Decisão Alinhada via Grill-Me / Decision Aligned via Grill-Me"
    
    adr_content = f"""---
id: "{adr_id}"
title: "{title}"
type: "adr"
status: "accepted"
decided_at: "2026-11-13"
source: "grill-me interview session / sessão de inquérito grill-me"
decided_by: "Author & AI Agent / Autor & Agente de IA"
impacted_modules: ["core"]
---

# 🏛️ {adr_id}: {title}

## 📋 Context & Alignment / Contexto Alinhado no Inquérito (Grill-Me)
[EN] This architectural decision was distilled from an interactive inquiry session, eliminating hidden assumptions.
[PT-BR] Esta decisão arquitetural foi destilada após sessão de inquérito dialético com o autor, eliminando premissas ocultas.

## ⚖️ Evaluated Alternatives / Alternativas Examinadas
- [EN] Options analyzed during the questioning rounds / [PT-BR] Opções analisadas durante as rodadas de perguntas da entrevista.

## 🎯 Approved Decision / Decisão Aprovada
{title}

## 🛡️ Technical Rationale / Racional Técnico
- [EN] Documented immediately upon frontier closure / [PT-BR] Registrado diretamente após o fechamento da fronteira de perguntas.
- [EN] Scope delimited and confirmed / [PT-BR] O escopo foi delimitado e confirmado.

## 📝 Raw Synthesis / Transcrição Sintetizada
```text
{raw_text[:800]}...
```
"""
    if output_path:
        out_p = Path(output_path)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(adr_content, encoding="utf-8")
        print(f"✅ [EN] Grill-me session distilled into ADR at '{output_path}' / [PT-BR] Sessão grill-me destilada em ADR em '{output_path}'.")
    return adr_content

def main():
    parser = argparse.ArgumentParser(
        description="Second Brain Plus - Multi-Agent Memory Bridge / Ponte de Memória Multi-Agente"
    )
    parser.add_argument("--export-claude-mem", action="store_true", help="EN: Sync claude-mem sessions / PT-BR: Sincroniza sessões do claude-mem")
    parser.add_argument("--claude-dir", default=os.path.expanduser("~/.claude-mem"), help="EN: Path to claude-mem / PT-BR: Caminho do claude-mem")
    parser.add_argument("--generate-graphify", action="store_true", help="EN: Extract knowledge graph / PT-BR: Extrai grafo de conhecimento")
    parser.add_argument("--vault-dir", default="./.second-brain", help="EN: Path to vault / PT-BR: Caminho do cofre")
    parser.add_argument("--graph-output", default="./.second-brain/.graphify/graph.json", help="EN: Graph output JSON / PT-BR: Arquivo JSON de saída do grafo")
    parser.add_argument("--compress-caveman", help="EN: Compress text using Caveman / PT-BR: Comprime texto com dialeto Caveman")
    parser.add_argument("--grill-distill", help="EN: Distill grill-me text to ADR / PT-BR: Destila transcrição de grill-me em ADR")
    parser.add_argument("--out", default="./.second-brain/3-Resources/adrs/ADR-GRILL-001.md", help="EN: Output ADR path / PT-BR: Caminho de saída do ADR")

    args = parser.parse_args()

    if args.export_claude_mem:
        out_dir = Path(args.vault_dir) / "4-Archives" / "sessions"
        export_claude_mem(Path(args.claude_dir), out_dir)
        sys.exit(0)

    if args.generate_graphify:
        generate_graphify(Path(args.vault_dir), Path(args.graph_output))
        sys.exit(0)

    if args.compress_caveman:
        target = args.compress_caveman
        text = Path(target).read_text(encoding="utf-8") if os.path.exists(target) else target
        comp, ratio = compress_caveman(text)
        print(f"🗜️ [EN] Caveman Compressed ({ratio}% saved) / [PT-BR] Comprimido ({ratio}% economizado):\n{comp}")
        sys.exit(0)

    if args.grill_distill:
        distill_grill_session(args.grill_distill, args.out)
        sys.exit(0)

    parser.print_help()

if __name__ == "__main__":
    main()
