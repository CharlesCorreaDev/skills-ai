#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de verificação de ambiente multiplataforma (Windows, Linux, macOS)
para a Skill 'docs-for-markdown'.
"""

import sys
import os
import platform
import shutil
import importlib.util

# Garantir saída UTF-8 em todos os sistemas operacionais e consoles
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def get_os_info():
    system = platform.system()
    if system == "Windows":
        return "Windows", "winget / choco / pip"
    elif system == "Darwin":
        return "macOS", "brew / pip3"
    elif system == "Linux":
        return "Linux", "apt / dnf / pacman / pip3"
    return system, "pip"

def check_package(package_name, display_name=None):
    display = display_name or package_name
    spec = importlib.util.find_spec(package_name)
    is_installed = spec is not None
    if is_installed:
        print(f"  ✅ {display} está instalado.")
    else:
        print(f"  ❌ {display} NÃO está instalado.")
    return is_installed

def check_system_tool(tool_name, os_install_hints):
    current_os = platform.system()
    found = shutil.which(tool_name) is not None
    
    if found:
        print(f"  ✅ Ferramenta de sistema '{tool_name}' encontrada no PATH.")
        return True
    else:
        print(f"  ⚠️ Ferramenta de sistema '{tool_name}' NÃO encontrada.")
        hint = os_install_hints.get(current_os, os_install_hints.get("default", ""))
        if hint:
            print(f"     -> Sugestão de instalação ({current_os}): {hint}")
        return False

def main():
    os_name, mgr_info = get_os_info()
    print("=========================================================")
    print(f"🔍 Verificação de Ambiente: Docs For Markdown")
    print(f"💻 Sistema Operacional : {os_name} ({platform.platform()})")
    print(f"🐍 Python              : {sys.version.split()[0]} ({sys.executable})")
    print("=========================================================\n")
    
    # 1. Checagem de versão do Python
    if sys.version_info < (3, 10):
        print("❌ ATENÇÃO: Python 3.10 ou superior é recomendado.")
        print(f"   Versão detectada: {sys.version.split()[0]}")
    else:
        print(f"✅ Versão do Python compatível ({sys.version_info.major}.{sys.version_info.minor})")

    # 2. Dependências Python
    print("\n📦 Verificando Pacotes Python:")
    pip_cmd = "pip" if os_name == "Windows" else "python3 -m pip"
    
    missing_pkgs = []
    
    pkgs = [
        ("markitdown", "markitdown (Motor principal)", f"{pip_cmd} install markitdown"),
        ("docx", "python-docx (Suporte Word .docx)", f"{pip_cmd} install python-docx"),
        ("openpyxl", "openpyxl (Suporte Excel .xlsx)", f"{pip_cmd} install openpyxl"),
        ("pdfminer", "pdfminer.six (Suporte PDF)", f"{pip_cmd} install pdfminer.six"),
        ("pdfplumber", "pdfplumber (Extração avançada de tabelas PDF)", f"{pip_cmd} install pdfplumber"),
        ("PIL", "Pillow (Suporte Imagens e EXIF)", f"{pip_cmd} install Pillow"),
        ("pptx", "python-pptx (Suporte PowerPoint .pptx)", f"{pip_cmd} install python-pptx"),
        ("markitdown_ocr", "markitdown-ocr (Opcional - OCR avançado)", f"{pip_cmd} install markitdown-ocr"),
    ]

    for pkg_import, name, install_cmd in pkgs:
        if not check_package(pkg_import, name):
            if pkg_import != "markitdown_ocr": # markitdown_ocr é opcional
                missing_pkgs.append(install_cmd)

    # 3. Ferramentas do Sistema (OCR / Pandoc)
    print("\n🛠️ Verificando Ferramentas de Sistema (Opcionais / Fallback):")
    
    tesseract_hints = {
        "Windows": "winget install UB-Mannheim.TesseractOCR  ou  choco install tesseract",
        "Darwin": "brew install tesseract",
        "Linux": "sudo apt-get install tesseract-ocr  (Ubuntu/Debian) | sudo dnf install tesseract (Fedora)",
        "default": "Instale o binário do Tesseract OCR para o seu sistema."
    }
    
    pandoc_hints = {
        "Windows": "winget install JohnMacFarlane.Pandoc  ou  choco install pandoc",
        "Darwin": "brew install pandoc",
        "Linux": "sudo apt-get install pandoc  (Ubuntu/Debian) | sudo dnf install pandoc (Fedora)",
        "default": "Instale o binário do Pandoc para o seu sistema."
    }

    check_system_tool("tesseract", tesseract_hints)
    check_system_tool("pandoc", pandoc_hints)

    # 4. Resumo e Instruções
    print("\n---------------------------------------------------------")
    if missing_pkgs:
        print("⚠️ Para instalar todos os pacotes Python recomendados de uma vez:")
        print(f"👉 {pip_cmd} install markitdown pdfplumber pdfminer.six python-docx openpyxl Pillow python-pptx")
    else:
        print("🎉 Todas as bibliotecas Python essenciais estão instaladas e prontas!")
    print("---------------------------------------------------------")

if __name__ == "__main__":
    main()
