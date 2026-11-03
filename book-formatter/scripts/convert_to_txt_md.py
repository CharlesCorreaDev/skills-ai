#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de conversão de documentos para TXT / Markdown multiplataforma (Windows, Linux, macOS)
usando Microsoft MarkItDown — motor principal da Skill 'book-formatter'.
"""

import sys
import os
from pathlib import Path
from markitdown import MarkItDown

# Garantir UTF-8 nas saídas de console (Windows, Linux, macOS)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def convert_document(input_path: str, output_base_path: str = None) -> bool:
    input_file = Path(input_path).resolve()

    if not input_file.exists():
        print(f"❌ Erro: Arquivo não encontrado: '{input_file}'")
        return False

    print(f"🔄 Convertendo documento: '{input_file.name}' ({input_file.parent})")

    try:
        md = MarkItDown()
        result = md.convert(str(input_file))
        markdown_content = result.text_content if hasattr(result, 'text_content') else getattr(result, 'markdown', str(result))

        # Salvar Markdown
        if output_base_path:
            base = Path(output_base_path).resolve()
            base.parent.mkdir(parents=True, exist_ok=True)
            md_file = base.with_suffix('.md')
            md_file.write_text(markdown_content, encoding='utf-8', newline='\n')
            txt_file = base.with_suffix('.txt')
            txt_file.write_text(markdown_content, encoding='utf-8', newline='\n')
            print(f"✅ Conversão concluída com sucesso!")
            print(f"📄 Arquivos salvos em: {md_file} e {txt_file}")
        else:
            print("\n--- Conteúdo Markdown Gerado ---")
            print(markdown_content)
            print("--------------------------------")

        return True
    except Exception as e:
        print(f"❌ Erro durante a conversão: {e}")
        print("💡 Dica: Execute 'python scripts/check_env.py' para diagnosticar dependências ausentes.")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python convert_to_txt_md.py <caminho_do_arquivo> [caminho_de_saida_base]")
        sys.exit(1)

    in_arg = sys.argv[1]
    out_arg = sys.argv[2] if len(sys.argv) > 2 else None

    success = convert_document(in_arg, out_arg)
    sys.exit(0 if success else 1)
