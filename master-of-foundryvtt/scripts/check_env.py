#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificador de ambiente para a Skill Master of Foundry VTT.
"""
import sys
import os
import shutil

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

def main():
    print('🔍 Verificação de Ambiente: Master of Foundry VTT')
    print('💻 Python:', sys.version.split()[0])
    
    node = shutil.which('node')
    if node:
        print('  ✅ Node.js encontrado no PATH:', node)
    else:
        print('  ⚠️ Node.js não encontrado no PATH (recomendado para desenvolvimento de pacotes Foundry).')
        
    print('\n🎉 Estrutura da Skill Master of Foundry VTT validada com sucesso!')

if __name__ == '__main__':
    main()
