#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificação de ambiente multiplataforma para a Skill 'website-for-markdown'.
"""
import sys
import os
import platform
import shutil
import importlib.util
import subprocess

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def check_package(pkg, display):
    spec = importlib.util.find_spec(pkg)
    if spec:
        print(f"  ✅ {display}")
        return True
    print(f"  ❌ {display} NÃO instalado.")
    return False

def main():
    print("=========================================================")
    print("🔍 Verificação de Ambiente: Website For Markdown")
    print(f"💻 OS: {platform.system()} | 🐍 Python: {sys.version.split()[0]}")
    print("=========================================================\n")
    
    # 1. Verificar MarkItDown (Herança)
    print("📦 Dependências Base (Herança da Docs For Markdown):")
    check_package("markitdown", "markitdown (Conversor HTML -> Markdown)")
    
    # 2. Verificar Firecrawl (Modo Premium/API)
    print("\n🌐 Modo Premium (Firecrawl API - Recomendado para Crawling):")
    if check_package("firecrawl", "firecrawl-py (SDK do Firecrawl)"):
        api_key = os.environ.get("FIRECRAWL_API_KEY")
        if api_key:
            print(f"  ✅ FIRECRAWL_API_KEY encontrada no ambiente.")
        else:
            print(f"  ⚠️ FIRECRAWL_API_KEY NÃO encontrada.")
            print(f"     -> O script usará o modo local (Playwright). Para varrer sites inteiros,")
            print(f"     -> obtenha uma chave em https://firecrawl.dev e exporte: export FIRECRAWL_API_KEY=sua_chave")
    else:
        print(f"  ⚠️ firecrawl-py não instalado. O script usará o modo local (Playwright).")
        print(f"     -> Instale com: pip install firecrawl-py")

    # 3. Verificar Playwright (Modo Local/Grátis)
    print("\n🎭 Modo Local (Playwright - Fallback para Sites com JS):")
    if check_package("playwright", "playwright (Automação de Navegador)"):
        # Verifica se os browsers estão instalados
        try:
            # Tenta importar e verificar o estado do chromium de forma simples
            result = subprocess.run([sys.executable, "-m", "playwright", "install", "--dry-run"], 
                                    capture_output=True, text=True, timeout=10)
            # Se o playwright está instalado, verificamos se o binário do chromium existe na pasta de cache
            # Uma forma mais direta é tentar rodar um script mínimo, mas para o check_env, 
            # vamos apenas alertar o usuário para garantir a instalação.
            print(f"  ℹ️ Playwright instalado. Certifique-se de que os browsers estão baixados:")
            print(f"     -> Rode: python -m playwright install chromium")
        except Exception:
            pass
    else:
        print(f"  ⚠️ playwright não instalado. Sites com JavaScript não serão capturados corretamente.")
        print(f"     -> Instale com: pip install playwright && python -m playwright install chromium")

    print("\n✅ Verificação concluída.")

if __name__ == "__main__":
    main()