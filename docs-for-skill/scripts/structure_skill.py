#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script multiplataforma (Windows, Linux, macOS) para estruturar documentos (PDF, DOCX, MD, etc.)
em uma Skill modular de alto desempenho para Agentes de IA.
"""

import sys
import os
import re
import platform
from pathlib import Path

# Garantir UTF-8 no console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def slugify(text: str) -> str:
    """Converte um título em um nome de arquivo seguro e limpo."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text[:40].strip('-') or "secao"

def convert_to_markdown_if_needed(input_path: Path) -> str:
    """Lê o arquivo se for .md, ou converte usando MarkItDown se for outro formato."""
    if input_path.suffix.lower() in [".md", ".markdown", ".txt"]:
        return input_path.read_text(encoding='utf-8', errors='replace')
    
    print(f"🔄 Extraindo conteúdo de '{input_path.name}' com MarkItDown...")
    try:
        from markitdown import MarkItDown
        md = MarkItDown()
        result = md.convert(str(input_path))
        return result.text_content if hasattr(result, 'text_content') else getattr(result, 'markdown', str(result))
    except Exception as e:
        print(f"❌ Erro ao converter documento: {e}")
        raise

def find_chapter_splits(content: str):
    """Encontra os pontos de divisão de capítulos com heurísticas inteligentes."""
    # 1. Cabeçalhos Markdown explícitos (# ou ## ou ###)
    md_heading_pattern = re.compile(r'^(#{1,3})\s+(.+)$', re.MULTILINE)
    matches = list(md_heading_pattern.finditer(content))
    if len(matches) >= 3:
        return [(m.start(), m.group(2).strip()) for m in matches]

    # 2. Divisores de Capítulos/Partes numerados (ex: Capítulo 1, Capítulo II, Parte 3)
    cap_pattern = re.compile(r'^\s*(?:Cap[ií]tulo|Chapter|Parte|Seção|Section)\s+(\d+|[IVXLCDM]+)[\s:\.\-–—]*(.*)$', re.MULTILINE | re.IGNORECASE)
    matches = list(cap_pattern.finditer(content))
    if len(matches) >= 3:
        splits = []
        for m in matches:
            num = m.group(1).strip()
            rest = m.group(2).strip()
            title = f"{m.group(0).split()[0].title()} {num}" + (f" - {rest}" if rest else "")
            splits.append((m.start(), title))
        return splits

    # 3. Títulos em linhas curtas isoladas com letras maiúsculas ou tópicos estruturais
    topic_pattern = re.compile(r'^(?:[0-9]+\.\s+)?([A-ZÁÀÂÃÉÈÊÍÓÔÕÚÇ][A-Za-zÁÀÂÃÉÈÊÍÓÔÕÚÇ0-9\s\-_/]{3,50})$', re.MULTILINE)
    matches = list(topic_pattern.finditer(content))
    valid_topics = []
    for m in matches:
        line = m.group(1).strip()
        # Ignora linhas numéricas simples, páginas soltas ou frases longas
        if len(line.split()) <= 6 and not line.isdigit() and len(line) >= 4:
            valid_topics.append((m.start(), line))
            
    if len(valid_topics) >= 5:
        # Filtrar tópicos que estejam muito próximos (< 500 caracteres) para evitar microfragmentação
        filtered = []
        last_pos = -1000
        for pos, title in valid_topics:
            if pos - last_pos >= 1500:
                filtered.append((pos, title))
                last_pos = pos
        if len(filtered) >= 3:
            return filtered

    return []

def split_large_chunks(content: str, max_chunk_size: int = 35000):
    """Subdivide blocos de texto muito grandes para otimização de tokens."""
    paragraphs = content.split("\n\n")
    chunks = []
    current_chunk = []
    current_size = 0
    
    for p in paragraphs:
        current_chunk.append(p)
        current_size += len(p)
        if current_size >= max_chunk_size:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = []
            current_size = 0
            
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))
    return chunks

def structure_skill(input_path_str: str, skill_name: str, target_dir: str = None) -> bool:
    input_file = Path(input_path_str).resolve()
    if not input_file.exists():
        print(f"❌ Arquivo não encontrado: {input_file}")
        return False

    print(f"🚀 Iniciando estruturação da Skill '{skill_name}' a partir de: '{input_file.name}'")
    
    try:
        content = convert_to_markdown_if_needed(input_file)
    except Exception as e:
        print(f"❌ Falha no processamento do documento: {e}")
        return False

    if not content or not content.strip():
        print("❌ O documento está vazio ou não possui texto extraível.")
        return False

    out_dir = Path(target_dir).resolve() if target_dir else Path(skill_name).resolve()
    chapters_dir = out_dir / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)

    splits = find_chapter_splits(content)
    chapters_info = []

    if splits:
        for i, (start_idx, title) in enumerate(splits):
            end_idx = splits[i+1][0] if i + 1 < len(splits) else len(content)
            chunk = content[start_idx:end_idx].strip()
            
            if not chunk or len(chunk) < 50:
                continue
            
            # Se o bloco for muito longo (> 45KB), subdividir para manter tokens equilibrados
            if len(chunk) > 45000:
                sub_chunks = split_large_chunks(chunk, max_chunk_size=35000)
                for sub_i, sub_c in enumerate(sub_chunks):
                    sub_title = f"{title} (Parte {sub_i+1})" if len(sub_chunks) > 1 else title
                    slug = slugify(sub_title)
                    filename = f"ch{len(chapters_info)+1:02d}-{slug}.md"
                    filepath = chapters_dir / filename
                    
                    if not sub_c.startswith("#"):
                        sub_c = f"# {sub_title}\n\n{sub_c}"
                    filepath.write_text(sub_c + "\n", encoding='utf-8', newline='\n')
                    chapters_info.append((filename, sub_title))
                    print(f"  📄 Capítulo: {filename} - {sub_title}")
            else:
                slug = slugify(title)
                filename = f"ch{len(chapters_info)+1:02d}-{slug}.md"
                filepath = chapters_dir / filename
                
                if not chunk.startswith("#"):
                    chunk = f"# {title}\n\n{chunk}"
                filepath.write_text(chunk + "\n", encoding='utf-8', newline='\n')
                chapters_info.append((filename, title))
                print(f"  📄 Capítulo: {filename} - {title}")
    else:
        # Divisão por tamanho inteligente
        print("ℹ️ Segmentando documento em capítulos modulares equilibrados...")
        sub_chunks = split_large_chunks(content, max_chunk_size=30000)
        for i, sub_c in enumerate(sub_chunks):
            title = f"Capítulo {i+1}"
            slug = f"capitulo-{i+1:02d}"
            filename = f"ch{i+1:02d}-{slug}.md"
            filepath = chapters_dir / filename
            
            filepath.write_text(f"# {title}\n\n" + sub_c + "\n", encoding='utf-8', newline='\n')
            chapters_info.append((filename, title))
            print(f"  📄 Capítulo: {filename}")

    # Gerar SKILL.md modular
    skill_md_content = f"""---
name: {skill_name}
description: Conhecimento estruturado e modularizado a partir de {input_file.name}.
language: en, pt-BR
---

# {skill_name}

## 🇺🇸 English
### Mental Model & Index
This skill contains structured knowledge extracted from `{input_file.name}`.
Chapters are modularized and loaded on-demand to optimize token usage and context window efficiency.

### Chapters
"""
    for fname, title in chapters_info:
        skill_md_content += f"- [{title}](chapters/{fname})\n"
        
    skill_md_content += f"""
---

## 🇧🇷 Português (Brasil)
### Modelo Mental & Índice
Esta skill contém conhecimento estruturado extraído de `{input_file.name}`.
Os capítulos são modularizados e carregados sob demanda para otimizar o consumo de tokens e a janela de contexto.

### Capítulos
"""
    for fname, title in chapters_info:
        skill_md_content += f"- [{title}](chapters/{fname})\n"

    (out_dir / "SKILL.md").write_text(skill_md_content, encoding='utf-8', newline='\n')
    
    # Criar Placeholders para Agente de IA enriquecer
    (out_dir / "glossary.md").write_text(f"# Glossary / Glossário - {skill_name}\n\n*Definições chave e termos técnicos extraídos dos capítulos.*\n", encoding='utf-8', newline='\n')
    (out_dir / "patterns.md").write_text(f"# Patterns & Rules / Padrões e Regras - {skill_name}\n\n*Mecânicas, fluxos de decisão e padrões operacionais.*\n", encoding='utf-8', newline='\n')
    (out_dir / "cheatsheet.md").write_text(f"# Quick Reference / Guia Rápido - {skill_name}\n\n*Resumo essencial para consulta rápida.*\n", encoding='utf-8', newline='\n')

    print(f"\n✅ Skill '{skill_name}' estruturada com sucesso!")
    print(f"📂 Diretório: {out_dir}")
    print(f"📊 Capítulos modulares gerados: {len(chapters_info)}")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python structure_skill.py <caminho_do_documento> <nome_da_skill> [diretorio_saida]")
        sys.exit(1)
        
    in_file = sys.argv[1]
    name = sys.argv[2]
    out_path = sys.argv[3] if len(sys.argv) > 3 else None
    
    success = structure_skill(in_file, name, out_path)
    sys.exit(0 if success else 1)