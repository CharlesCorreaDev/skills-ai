#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Multi-platform environment & hardware budget check for 'website-for-markdown'.
Verificação de ambiente e orçamento de hardware multiplataforma para a Skill 'website-for-markdown'.
"""
import importlib.util
import os
import platform
import subprocess
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Import hardware profiler from scrape_to_md / Importa o perfilador de hardware do scrape_to_md
sys.path.insert(0, str(Path(__file__).resolve().parent))
from scrape_to_md import detect_hardware_budget


def check_package(pkg, display):
    spec = importlib.util.find_spec(pkg)
    if spec:
        print(f"  ✅ {display}")
        return True
    print(f"  ❌ {display} NÃO instalado.")
    return False


def main():
    budget = detect_hardware_budget()

    print("=================================================================")
    print("🔍 Verificação de Ambiente & Hardware: Website For Markdown")
    print(f"💻 OS: {platform.system()} | 🐍 Python: {sys.version.split()[0]}")
    print("=================================================================\n")

    print("🖥️ Diagnóstico da Máquina Operante (Auto-Tuning Eco):")
    print(f"  ├─ Processador : {budget['cpu_model']}")
    print(f"  ├─ Núcleos CPU : {budget['cpu_cores']} lógicos")
    print(f"  ├─ Memória RAM : {budget['avail_ram_gb']} GB livres de {budget['total_ram_gb']} GB ({budget['ram_used_percent']}% em uso)")
    print(f"  ├─ Perfil Eco  : {budget['tier']}")
    print(f"  └─ Limite Auto : {budget['workers']} worker(s) | Lote: {budget['batch_size']} págs | Pausa: {budget['delay_ms']}ms\n")

    print("📦 Dependências Base (Conversão HTML -> Markdown):")
    check_package("bs4", "beautifulsoup4 (Limpeza cirúrgica de DOM e extração de links)")
    check_package("markdownify", "markdownify (Conversor HTML -> Markdown de baixo uso de RAM)")
    check_package("markitdown", "markitdown (Conversor universal fallback)")

    print("\n🎭 Modo Local (Playwright - Para Sites com JS / SPAs):")
    if check_package("playwright", "playwright (Automação de Navegador Headless)"):
        print("  ℹ️ Playwright instalado (configurado com limite de memória JS e reúso de contexto).")
    else:
        print("  ⚠️ playwright não instalado. Instale com: pip install playwright && python -m playwright install chromium")

    print("\n🌐 Modo Nuvem Opcional (Firecrawl API):")
    if check_package("firecrawl", "firecrawl-py (SDK Opcional do Firecrawl)"):
        if os.environ.get("FIRECRAWL_API_KEY"):
            print("  ✅ FIRECRAWL_API_KEY encontrada no ambiente.")
        else:
            print("  ℹ️ FIRECRAWL_API_KEY não definida (o crawler local gratuito será utilizado automaticamente).")

    print("\n✅ Verificação concluída.")


if __name__ == "__main__":
    main()
