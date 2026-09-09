#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de verificação de ambiente multiplataforma (Windows, Linux, macOS)
para a Skill 'image-to-prompt'.
"""

import sys
import os
import platform
import shutil
import importlib.util

# Garantir UTF-8 nas saídas de console
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
    print(f"🔍 Verificação de Ambiente: Image To Prompt")
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
    print("\n📦 Verificando Pacotes Python para Manipulação e Visão:")
    pip_cmd = "pip" if os_name == "Windows" else "python3 -m pip"
    
    missing_pkgs = []
    
    pkgs = [
        ("PIL", "Pillow (Inspeção de imagens, EXIF e cores)", f"{pip_cmd} install Pillow"),
    ]

    for pkg_import, name, install_cmd in pkgs:
        if not check_package(pkg_import, name):
            missing_pkgs.append(install_cmd)

    # 3. Resumo e Instruções
    print("\n---------------------------------------------------------")
    if missing_pkgs:
        print("⚠️ Para instalar os pacotes necessários:")
        print(f"👉 {pip_cmd} install Pillow")
    else:
        print("🎉 Todas as dependências essenciais estão instaladas e prontas!")
    print("---------------------------------------------------------")

if __name__ == "__main__":
    main()
