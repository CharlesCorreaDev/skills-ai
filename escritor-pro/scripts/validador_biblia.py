#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validador da Bíblia de Worldbuilding e Entidades Canônicas
Parte integrante da skill Escritor Pro.
"""

import sys
import os
import re
import argparse
from pathlib import Path

def validate_entity_file(filepath: Path) -> dict:
    content = filepath.read_text(encoding="utf-8")
    issues = []
    warnings = []
    
    # 1. Checagem de Frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not fm_match:
        issues.append("Arquivo não possui YAML frontmatter inicial (---).")
    else:
        fm_text = fm_match.group(1)
        if not re.search(r"^tipo:\s*.+", fm_text, re.MULTILINE):
            issues.append("Frontmatter ausente de 'tipo:' (ex: lugar, faccao, personagem, etc.).")
        if not re.search(r"^nome:\s*.+", fm_text, re.MULTILINE):
            issues.append("Frontmatter ausente de 'nome:'.")
        if not re.search(r"^camada:\s*[1-6]", fm_text, re.MULTILINE):
            warnings.append("Frontmatter ausente de 'camada:' (de 1 a 6 conforme metodologia).")

    # 2. Checagem do Filtro Sensorial (Regra 3+1)
    # Deve conter menção a sentidos e tensão social
    sensory_fields = ["visual", "sonor", "olfat", "t[áa]til"]
    found_sensory = 0
    for s in sensory_fields:
        if re.search(s, content, re.IGNORECASE):
            found_sensory += 1
            
    if found_sensory < 2:
        warnings.append("Filtro Sensorial incompleto: inclua detalhes de visão, som e olfato/tato.")

    if not re.search(r"tens[ãa]o social", content, re.IGNORECASE) and not re.search(r"conflito", content, re.IGNORECASE):
        warnings.append("Falta explicitar a 'Tensão Social' ou 'Conflito' ativo na entidade.")

    # 3. Quem lucra / Quem sangra
    has_lucro = bool(re.search(r"lucra|beneficia|privil[ée]gio", content, re.IGNORECASE))
    has_sangue = bool(re.search(r"sangra|oprimid|v[íi]tima", content, re.IGNORECASE))
    if not (has_lucro and has_sangue):
        warnings.append("Considere definir explicitamente 'Quem lucra aqui' e 'Quem sangra aqui'.")

    return {
        "file": filepath.name,
        "path": str(filepath),
        "issues": issues,
        "warnings": warnings,
        "valid": len(issues) == 0
    }

def main():
    parser = argparse.ArgumentParser(description="Validador de Entidades e Bíblia de Worldbuilding")
    parser.add_argument("diretorio", nargs="?", default="mundo", help="Diretório de lore/mundo a validar (padrão: mundo)")
    args = parser.parse_args()

    target_dir = Path(args.diretorio)
    if not target_dir.exists():
        print(f"Diretório '{args.diretorio}' não existe. Nada a validar.")
        sys.exit(0)

    md_files = list(target_dir.glob("**/*.md"))
    if not md_files:
        print(f"Nenhum arquivo .md encontrado em '{args.diretorio}'.")
        sys.exit(0)

    print("=" * 65)
    print(f"  VALIDAÇÃO DA BÍBLIA DE WORLDBUILDING: {target_dir}")
    print("=" * 65)

    all_valid = True
    for f in md_files:
        res = validate_entity_file(f)
        status = "✅ OK" if res["valid"] and not res["warnings"] else ("⚠️ AVISOS" if res["valid"] else "❌ INVÁLIDO")
        print(f"\n[{status}] {res['file']}")
        for iss in res["issues"]:
            print(f"   🔴 ERRO: {iss}")
            all_valid = False
        for w in res["warnings"]:
            print(f"   🟡 ALERTA: {w}")

    print("\n" + "=" * 65)
    if all_valid:
        print("🎉 Todos os arquivos avaliados cumprem as diretrizes canônicas!")
    else:
        print("⚠️ Alguns arquivos requerem correções de conformidade estrutural.")
    print("=" * 65)

if __name__ == "__main__":
    main()
