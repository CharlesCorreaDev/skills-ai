#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de conversão de documentos para Markdown multiplataforma (Windows, Linux, macOS)
usando Microsoft MarkItDown.
"""

import sys
import os
from pathlib import Path
from markitdown import MarkItDown

# Garantir UTF-8 nas saídas de console (Windows, Linux, macOS)
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def convert_document(input_path: str, output_path: str = None) -> bool:
    input_file = Path(input_path).resolve()
    
    if not input_file.exists():
        print(f"❌ Erro: Arquivo não encontrado: '{input_file}'")
        return False

    print(f"🔄 Convertendo documento: '{input_file.name}' ({input_file.parent})")
    
    try:
        md = MarkItDown()
        result = md.convert(str(input_file))
        markdown_content = result.text_content if hasattr(result, 'text_content') else getattr(result, 'markdown', str(result))
        
        if output_path:
            out_file = Path(output_path).resolve()
            out_file.parent.mkdir(parents=True, exist_ok=True)
            out_file.write_text(markdown_content, encoding='utf-8', newline='\n')
            print(f"✅ Conversão concluída com sucesso!")
            print(f"📄 Arquivo salvo em: {out_file}")
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
        print("Uso: python convert_to_md.py <caminho_do_arquivo> [caminho_de_saida.md]")
        sys.exit(1)
        
    in_arg = sys.argv[1]
    out_arg = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = convert_document(in_arg, out_arg)
    sys.exit(0 if success else 1)