#!/usr/bin/env python3
"""
verify_brain.py - Second Brain Integrity Auditor and Scaffolder
Auditor de Integridade e Inicializador de Estrutura do Second Brain Plus.

Bilingual support: English (EN) and Portuguese (PT-BR).
Suporte bilíngue: Inglês (EN) e Português (PT-BR).
"""

import os
import sys
import re
import argparse
from pathlib import Path

# Standard P.A.R.A. 2.0 folders / Pastas padrão do Método P.A.R.A. 2.0
DEFAULT_PARA_STRUCTURE = [
    "1-Projects",
    "2-Areas",
    "3-Resources/adrs",
    "3-Resources/cheatsheets",
    "4-Archives/sessions"
]

def scaffold_second_brain(vault_dir: Path):
    """
    EN: Initialize standard PARA 2.0 folder hierarchy and baseline templates.
    PT-BR: Inicializa a hierarquia de pastas do PARA 2.0 e templates de linha de base.
    """
    print(f"🚀 [EN] Initializing Second Brain PARA 2.0 at '{vault_dir}' / [PT-BR] Inicializando PARA 2.0 em '{vault_dir}'...")
    for sub in DEFAULT_PARA_STRUCTURE:
        folder = vault_dir / sub
        folder.mkdir(parents=True, exist_ok=True)
        print(f"  📁 [EN] Created / [PT-BR] Criado: {sub}")

    # EN: Create baseline project / PT-BR: Cria projeto inicial de exemplo
    sample_prj = vault_dir / "1-Projects" / "PRJ-001-init.md"
    if not sample_prj.exists():
        sample_prj.write_text("""---
id: "PRJ-001"
title: "Setup do Second Brain Plus / Second Brain Plus Setup"
type: "project"
status: "active"
priority: "P1"
deadline: "2026-12-31"
owner: "Charles Corrêa & Antigravity"
tags: ["setup", "memory", "ssot"]
adhd_mode_enabled: false
---

# 🚀 Projeto / Project: PRJ-001 Setup

> **[EN] Core Goal:** Establish persistent memory infrastructure with Notion API and local Git vault.  
> **[PT-BR] Objetivo Central:** Estabelecer infraestrutura de memória persistente com a API do Notion e cofre Git local.

## 🎯 Milestones / Marcos
- [x] [EN] Create local PARA folder structure / [PT-BR] Criar estrutura de pastas locais PARA
- [ ] [EN] Configure Notion Integration Secret / [PT-BR] Configurar token da API do Notion
- [ ] [EN] First bidirectional ADR and Project sync / [PT-BR] Primeira sincronização de ADRs e Projetos
""", encoding="utf-8")
        print(f"  📄 [EN] Sample project created / [PT-BR] Projeto de exemplo criado: {sample_prj.name}")

    # EN: Create baseline ADR / PT-BR: Cria ADR inicial de exemplo
    sample_adr = vault_dir / "3-Resources" / "adrs" / "ADR-001-ssot.md"
    if not sample_adr.exists():
        sample_adr.write_text("""---
id: "ADR-001"
title: "Notion and Local Markdown as SSOT / Notion e Markdown Local como SSOT"
type: "adr"
status: "accepted"
decided_at: "2026-11-13"
decided_by: "Charles Corrêa & Antigravity"
impacted_modules: ["all"]
---

# 🏛️ ADR-001: Notion & Local Markdown as SSOT

## 📋 Context / Contexto
[EN] Autonomous coding agents suffer from amnesia across sessions and invent decisions when restarted.
[PT-BR] Agentes de IA sofrem de amnésia entre sessões e inventam dados técnicos ao serem reinicializados.

## 🎯 Decision / Decisão
[EN] Adopt Notion as human-friendly cloud dashboard and Git-tracked Markdown (.second-brain) as Single Source of Truth.
[PT-BR] Adotar o Notion como dashboard em nuvem e arquivos Markdown locais (.second-brain) como Única Fonte da Verdade.
""", encoding="utf-8")
        print(f"  📄 [EN] Sample ADR created / [PT-BR] ADR de exemplo criado: {sample_adr.name}")

    print(f"✅ [EN] Second Brain scaffolded cleanly at '{vault_dir}'. / [PT-BR] Segundo Cérebro inicializado com sucesso em '{vault_dir}'.")

def audit_second_brain(vault_dir: Path) -> bool:
    """
    EN: Audit local vault files for mandatory frontmatter, types, and schema compliance.
    PT-BR: Audita arquivos do cofre local para conformidade de frontmatter obrigatório e tipos.
    """
    print(f"🔎 [EN] Auditing Second Brain at '{vault_dir}' / [PT-BR] Auditando Segundo Cérebro em '{vault_dir}'...")
    if not vault_dir.exists():
        print(f"❌ [EN] Directory does not exist / [PT-BR] Diretório não existe: {vault_dir}")
        return False

    md_files = list(vault_dir.rglob("*.md"))
    if not md_files:
        print(f"⚠️ [EN] No markdown files found / [PT-BR] Nenhum arquivo Markdown encontrado.")
        return True

    errors = 0
    warnings = 0

    for f in md_files:
        rel = f.relative_to(vault_dir)
        content = f.read_text(encoding="utf-8", errors="ignore")

        # Frontmatter validation / Validação de frontmatter
        fm = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not fm:
            print(f"  🔴 [ERROR / ERRO] Missing YAML frontmatter: {rel}")
            errors += 1
            continue

        fm_text = fm.group(1)
        if not re.search(r'^id:\s*.+$', fm_text, re.MULTILINE):
            print(f"  🔴 [ERROR / ERRO] Missing 'id' field: {rel}")
            errors += 1
        if not re.search(r'^type:\s*.+$', fm_text, re.MULTILINE):
            print(f"  🟡 [WARN / AVISO] Missing 'type' field: {rel}")
            warnings += 1

    print("\n--- [EN] Audit Summary / [PT-BR] Resumo da Auditoria ---")
    print(f"Total Notes / Total de Notas: {len(md_files)}")
    print(f"Critical Errors / Erros Críticos: {errors}")
    print(f"Warnings / Avisos: {warnings}")

    if errors == 0:
        print("✅ [EN] Second Brain vault is intact and compliant. / [PT-BR] Segundo Cérebro íntegro e em total conformidade.")
        return True
    else:
        print("❌ [EN] Issues detected that require attention. / [PT-BR] Detectadas pendências que precisam de atenção.")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Second Brain Auditor & Scaffolder / Auditor e Inicializador do Segundo Cérebro"
    )
    parser.add_argument("--scaffold", action="store_true", help="EN: Create PARA folders / PT-BR: Cria pastas do método PARA")
    parser.add_argument("--audit", action="store_true", help="EN: Audit vault integrity / PT-BR: Audita integridade do cofre")
    parser.add_argument("--vault-dir", default="./.second-brain", help="EN: Vault path / PT-BR: Caminho do cofre")

    args = parser.parse_args()
    vault_path = Path(args.vault_dir)

    if args.scaffold:
        scaffold_second_brain(vault_path)
        sys.exit(0)

    if args.audit:
        success = audit_second_brain(vault_path)
        sys.exit(0 if success else 1)

    parser.print_help()

if __name__ == "__main__":
    main()
