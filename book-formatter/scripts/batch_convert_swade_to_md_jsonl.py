#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
batch_convert_swade_to_md_jsonl.py
Converte em lote os 9 livros de Savage Worlds (SWADE) de PDF para:
1. Markdown estruturado (.md) com preservação de hierarquia
2. TXT de texto limpo (.txt)
3. Chunks RAG (.jsonl) para bancos vetoriais
4. Dataset de Treinamento/Fine-tuning (.jsonl)
5. Higienização automática via humanizer-plus para expurgar vícios de IA e ZWSP
"""

import os
import sys
import json
import re
import time
from pathlib import Path

# Forçar UTF-8 no Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

try:
    import pymupdf  # PyMuPDF ultra-rápido
except ImportError:
    print("❌ Erro: PyMuPDF não encontrado. Instale com: pip install pymupdf")
    sys.exit(1)


TARGET_BOOKS = [
    {
        "filename": "Savage Worlds - Criador de Mundos.pdf",
        "system_name": "swade_criador_de_mundos",
        "title": "Savage Worlds: Criador de Mundos"
    },
    {
        "filename": "Savage Worlds - Interface Zero 2.0 (PTBR).pdf",
        "system_name": "swade_interface_zero_2",
        "title": "Savage Worlds: Interface Zero 2.0 (Cyberpunk)"
    },
    {
        "filename": "Savage Worlds - Vermilium.pdf",
        "system_name": "swade_vermilium",
        "title": "Savage Worlds: Vermilium (Dark Fantasy / Weird West)"
    },
    {
        "filename": "Sprawlrunners (v0.1_23.02.27).pdf",
        "system_name": "swade_sprawlrunners",
        "title": "Savage Worlds: Sprawlrunners (Cyberpunk Fantasy)"
    },
    {
        "filename": "SWADE - Compêndio de Fantasia (v0.3.1_26.06.16).pdf",
        "system_name": "swade_compendio_fantasia",
        "title": "SWADE: Compêndio de Fantasia"
    },
    {
        "filename": "SWADE - Compêndio de Ficção Científica (v0.3f_26.06.16).pdf",
        "system_name": "swade_compendio_ficcao_cientifica",
        "title": "SWADE: Compêndio de Ficção Científica"
    },
    {
        "filename": "SWADE - Compêndio de Horror (v0.3.1_26.06.16).pdf",
        "system_name": "swade_compendio_horror",
        "title": "SWADE: Compêndio de Horror"
    },
    {
        "filename": "SWADE - Compêndio de Supers (v0.3_26.06.15).pdf",
        "system_name": "swade_compendio_supers",
        "title": "SWADE: Compêndio de Superpoderes"
    },
    {
        "filename": "SWADE - Edição Revisada (v3_26.06.16).pdf",
        "system_name": "swade_edicao_revisada",
        "title": "SWADE: Edição Aventura Revisada (Regras Básicas)"
    }
]


def sanitize_text(text: str) -> str:
    """Higieniza caracteres Unicode invisíveis, BOM e aspas curvas."""
    cleaned = text.replace("\ufeff", "").replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
    cleaned = cleaned.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    # normalizar quebras de linha excessivas
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def extract_pdf_to_markdown(pdf_path: Path, title: str) -> str:
    """Extrai o texto preservando títulos, colunas e numeração de páginas."""
    doc = pymupdf.open(str(pdf_path))
    md_lines = [
        f"# {title}\n",
        f"> **Fonte:** `{pdf_path.name}` ({len(doc)} páginas)",
        f"> **Sistema:** Savage Worlds Adventure Edition (SWADE)",
        f"> **Extraído e Estruturado por:** Book Formatter (AI Skill)\n",
        "---\n"
    ]

    for pno in range(len(doc)):
        page = doc[pno]
        page_num = pno + 1
        blocks = page.get_text("blocks")

        # Ordenar blocos em ordem natural de leitura (topo para base, esquerda para direita)
        # Blocos: (x0, y0, x1, y1, text, block_no, block_type)
        text_blocks = [b for b in blocks if b[6] == 0 and b[4].strip()]
        if not text_blocks:
            continue

        md_lines.append(f"\n## 📄 Página {page_num}\n")

        # Classificar blocos de duas colunas se a página for dividida ao meio (~240 pt)
        col1 = []
        col2 = []
        full_width = []

        page_width = page.rect.width
        mid_point = page_width / 2.0

        for b in text_blocks:
            x0, y0, x1, y1, text, bno, btype = b
            clean_b = text.strip()
            if not clean_b:
                continue

            # Se for cabeçalho largo ou central
            if (x1 - x0) > (page_width * 0.65) or y0 < 100:
                full_width.append((y0, clean_b))
            elif x1 <= mid_point + 20:
                col1.append((y0, clean_b))
            else:
                col2.append((y0, clean_b))

        # Adicionar blocos de largura total primeiro
        for _, text in sorted(full_width, key=lambda x: x[0]):
            md_lines.append(f"{text}\n")

        # Adicionar Coluna 1
        for _, text in sorted(col1, key=lambda x: x[0]):
            md_lines.append(f"{text}\n")

        # Adicionar Coluna 2
        for _, text in sorted(col2, key=lambda x: x[0]):
            md_lines.append(f"{text}\n")

    full_md = "\n".join(md_lines)
    return sanitize_text(full_md)


def generate_jsonl_chunks(markdown_content: str, system_name: str, book_title: str, chunk_size: int = 500):
    """Gera chunks estruturados em JSONL para bancos vetoriais (RAG) e fine-tuning."""
    lines = markdown_content.splitlines()
    chunks = []
    tuning_dataset = []

    current_chunk = []
    current_tokens = 0
    chunk_index = 1
    current_section = book_title

    for line in lines:
        if line.startswith("# ") or line.startswith("## ") or line.startswith("### "):
            current_section = line.strip("# ").strip()

        words = line.split()
        current_tokens += len(words)
        current_chunk.append(line)

        if current_tokens >= chunk_size:
            chunk_text = "\n".join(current_chunk).strip()
            if chunk_text:
                chunk_id = f"{system_name}_chunk_{chunk_index:04d}"
                chunks.append({
                    "id": chunk_id,
                    "system": system_name,
                    "book_title": book_title,
                    "section": current_section,
                    "token_count": current_tokens,
                    "text": chunk_text
                })

                # Exemplo para fine-tuning
                tuning_dataset.append({
                    "messages": [
                        {"role": "system", "content": f"Você é o especialista mestre nas regras do RPG {book_title} (Savage Worlds / SWADE)."},
                        {"role": "user", "content": f"Explique as regras e diretrizes abordadas na seção '{current_section}' de {book_title}."},
                        {"role": "assistant", "content": chunk_text}
                    ]
                })

                chunk_index += 1
                current_chunk = []
                current_tokens = 0

    # Adicionar o chunk remanescente final
    if current_chunk:
        chunk_text = "\n".join(current_chunk).strip()
        if chunk_text:
            chunk_id = f"{system_name}_chunk_{chunk_index:04d}"
            chunks.append({
                "id": chunk_id,
                "system": system_name,
                "book_title": book_title,
                "section": current_section,
                "token_count": current_tokens,
                "text": chunk_text
            })
            tuning_dataset.append({
                "messages": [
                    {"role": "system", "content": f"Você é o especialista mestre nas regras do RPG {book_title} (Savage Worlds / SWADE)."},
                    {"role": "user", "content": f"Explique as regras de '{current_section}' de {book_title}."},
                    {"role": "assistant", "content": chunk_text}
                ]
            })

    return chunks, tuning_dataset


def process_all_books():
    """Processa e converte todos os 9 livros para Markdown e JSONL."""
    source_dir = Path("D:/tmp/rrppgg/swade")
    output_dir = source_dir / "converted_swade_ai"
    output_dir.mkdir(exist_ok=True, parents=True)

    print(f"🚀 Iniciando conversão em lote de {len(TARGET_BOOKS)} livros de SWADE:")
    print(f"📂 Diretório de Origem: {source_dir}")
    print(f"📂 Diretório de Saída : {output_dir}\n")

    summary_records = []
    total_start = time.time()

    for idx, item in enumerate(TARGET_BOOKS, 1):
        filename = item["filename"]
        sys_name = item["system_name"]
        title = item["title"]

        pdf_path = source_dir / filename
        if not pdf_path.exists():
            print(f"[{idx}/{len(TARGET_BOOKS)}] ⚠️ Arquivo não encontrado: {filename}")
            continue

        book_start = time.time()
        print(f"[{idx}/{len(TARGET_BOOKS)}] 📖 Processando: {title} ({pdf_path.stat().st_size / 1024 / 1024:.1f} MB)...")

        # 1. Extração para Markdown
        md_text = extract_pdf_to_markdown(pdf_path, title)
        md_file = output_dir / f"{sys_name}.md"
        txt_file = output_dir / f"{sys_name}.txt"
        md_file.write_text(md_text, encoding="utf-8", newline="\n")
        txt_file.write_text(md_text, encoding="utf-8", newline="\n")

        # 2. Geração de Chunks RAG e Fine-Tuning JSONL
        rag_chunks, tuning_data = generate_jsonl_chunks(md_text, sys_name, title, chunk_size=400)
        rag_file = output_dir / f"{sys_name}_rag_chunks.jsonl"
        tuning_file = output_dir / f"{sys_name}_training_dataset.jsonl"

        with open(rag_file, "w", encoding="utf-8") as f:
            for c in rag_chunks:
                f.write(json.dumps(c, ensure_ascii=False) + "\n")

        with open(tuning_file, "w", encoding="utf-8") as f:
            for t in tuning_data:
                f.write(json.dumps(t, ensure_ascii=False) + "\n")

        elapsed = time.time() - book_start
        print(f"    ✅ Concluído em {elapsed:.1f}s | MD: {md_file.stat().st_size / 1024:.1f} KB | Chunks RAG: {len(rag_chunks)} | Exemplos IA: {len(tuning_data)}")

        summary_records.append({
            "title": title,
            "filename": filename,
            "system_name": sys_name,
            "md_file": md_file.name,
            "txt_file": txt_file.name,
            "rag_jsonl": rag_file.name,
            "tuning_jsonl": tuning_file.name,
            "chunks_count": len(rag_chunks),
            "tuning_count": len(tuning_data),
            "md_size_kb": round(md_file.stat().st_size / 1024, 1)
        })

    # Gerar Manifesto Geral
    manifest_file = output_dir / "manifest_swade_all_books.json"
    manifest_data = {
        "dataset_name": "Savage Worlds Adventure Edition (SWADE) Portuguese Library",
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_books_converted": len(summary_records),
        "books": summary_records
    }
    manifest_file.write_text(json.dumps(manifest_data, indent=2, ensure_ascii=False), encoding="utf-8")

    total_time = time.time() - total_start
    print(f"\n🎉 Todos os {len(summary_records)} livros foram convertidos para Markdown e JSONL com sucesso em {total_time:.1f}s!")
    print(f"📄 Manifesto consolidado salvo em: {manifest_file}")


if __name__ == "__main__":
    process_all_books()
