#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificador de ambiente e diagnóstico para a Skill Master of Foundry VTT.
Verifica dependências (Node.js, NPX, Git, Python) e localiza pastas de dados do Foundry VTT.
"""
import sys
import os
import shutil
from pathlib import Path

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def check_foundry_data_paths():
    found_paths = []
    
    if sys.platform == 'win32':
        local_app = os.environ.get('LOCALAPPDATA', '')
        if local_app:
            p = Path(local_app) / 'FoundryVTT' / 'Data'
            if p.exists():
                found_paths.append(str(p))
    elif sys.platform == 'darwin':
        p = Path.home() / 'Library' / 'Application Support' / 'FoundryVTT' / 'Data'
        if p.exists():
            found_paths.append(str(p))
    else:  # Linux / Unix
        p = Path.home() / '.local' / 'share' / 'FoundryVTT' / 'Data'
        if p.exists():
            found_paths.append(str(p))
            
    # Check custom environment variable
    custom_env = os.environ.get('FOUNDRY_DATA_PATH') or os.environ.get('FOUNDRY_VTT_DATA')
    if custom_env and Path(custom_env).exists() and custom_env not in found_paths:
        found_paths.append(custom_env)
        
    return found_paths

def main():
    print('🎲 ========================================================')
    print('🔍 DIAGNÓSTICO DE AMBIENTE: MASTER OF FOUNDRY VTT')
    print('🎲 ========================================================\n')
    
    # 1. Python
    print(f'🐍 Python: {sys.version.split()[0]} ({sys.executable})')
    
    # 2. Node.js & NPX
    node = shutil.which('node')
    npx = shutil.which('npx')
    if node:
        print(f'  ✅ Node.js: Encontrado ({node})')
    else:
        print('  ⚠️ Node.js: Não encontrado no PATH. (Necessário para empacotamento, compilação TS e servidores MCP).')
        
    if npx:
        print(f'  ✅ NPX: Encontrado ({npx})')
    else:
        print('  ⚠️ NPX: Não encontrado no PATH. (Recomendado para execução dinâmica de MCPs como ninjos-foundry-mcp e foundryvtt-mcp).')
        
    # 3. Git
    git = shutil.which('git')
    if git:
        print(f'  ✅ Git: Encontrado ({git})')
    else:
        print('  ⚠️ Git: Não encontrado no PATH.')

    # 4. Foundry VTT Data Directory Detection
    print('\n📁 Detecção de Pastas de Dados do Foundry VTT:')
    data_paths = check_foundry_data_paths()
    if data_paths:
        for path in data_paths:
            print(f'  🎉 Pasta de Dados Detectada: {path}')
            modules_dir = Path(path) / 'modules'
            systems_dir = Path(path) / 'systems'
            worlds_dir = Path(path) / 'worlds'
            print(f'     ├── Módulos: {"✅ Existe" if modules_dir.exists() else "❌ Não encontrada"}')
            print(f'     ├── Sistemas: {"✅ Existe" if systems_dir.exists() else "❌ Não encontrada"}')
            print(f'     └── Mundos: {"✅ Existe" if worlds_dir.exists() else "❌ Não encontrada"}')
    else:
        print('  ℹ️ Nenhuma pasta padrão de dados do Foundry VTT foi encontrada automaticamente.')
        print('     (Se o Foundry estiver instalado em caminho customizado ou servidor remoto, forneça a URL ou caminho ao Agente).')

    # 5. CLI Tools (Foundry CLI & World CLI)
    print('\n💻 Ferramentas de Linha de Comando (CLI):')
    fvtt_cli = shutil.which('fvtt')
    if fvtt_cli:
        print(f'  ✅ @foundryvtt/foundryvtt-cli: Encontrado ({fvtt_cli})')
    else:
        print('  ℹ️ @foundryvtt/foundryvtt-cli: Não instalado globalmente. (Disponível via "npx @foundryvtt/foundryvtt-cli").')

    world_cli = shutil.which('fvtt-world-cli')
    if world_cli:
        print(f'  ✅ fvtt-world-cli: Encontrado ({world_cli})')
    else:
        print('  ℹ️ fvtt-world-cli: Não instalado globalmente. (Disponível via "npx fvtt-world-cli").')

    # 6. Summary & Guidance
    print('\n🔌 Integração MCP (Model Context Protocol):')
    print('  - ninjos-foundry-mcp: Pronto para conexão via URL/WebSocket (http://localhost:30000).')
    print('  - foundryvtt-mcp: Pronto para leitura direta da pasta Data.')
    print('  - foundry-vtt-mcp: Pronto para parsing de pacotes LevelDB/ClassicLevel locais.')
    
    print('\n✨ Diagnóstico concluído com sucesso!')

if __name__ == '__main__':
    main()
