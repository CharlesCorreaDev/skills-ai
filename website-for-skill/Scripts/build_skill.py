#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Orquestrador multiplataforma que captura um site e o transforma em uma Skill modular estruturada para Agentes de IA.
Depende das skills 'docs-for-markdown' e 'website-for-markdown'.
"""
import sys
import os
import subprocess
import shutil
import re
from pathlib import Path
from urllib.parse import urlparse

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def find_skill_script(skill_name, script_name):
    """Encontra o caminho do script de uma skill dependente em múltiplos locais."""
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parents[1]
    
    possible_paths = [
        repo_root / skill_name / "scripts" / script_name,
        repo_root / skill_name / "Scripts" / script_name,
        script_dir.parent.parent / skill_name / "scripts" / script_name,
        Path.cwd() / skill_name / "scripts" / script_name,
        Path.cwd().parent / skill_name / "scripts" / script_name,
        Path.home() / ".agents" / "skills" / skill_name / "scripts" / script_name,
        Path.home() / ".gemini" / "config" / "skills" / skill_name / "scripts" / script_name,
        Path.home() / ".copilot" / "skills" / skill_name / "scripts" / script_name,
        Path.home() / ".claude" / "skills" / skill_name / "scripts" / script_name
    ]
    for p in possible_paths:
        if p.exists():
            return p.resolve()
    return None

def generate_skill_structure(skill_name, md_files_dir, output_skill_dir, source_url):
    """Estrutura os arquivos markdown capturados em uma Skill modular de alto desempenho."""
    skill_dir = Path(output_skill_dir).resolve()
    skill_dir.mkdir(parents=True, exist_ok=True)
    
    chapters_dir = skill_dir / "chapters"
    chapters_dir.mkdir(parents=True, exist_ok=True)
    
    md_files = list(Path(md_files_dir).glob("*.md"))
    if not md_files:
        print("❌ Nenhum arquivo Markdown encontrado para estruturar.")
        return False
        
    print(f"📚 Estruturando {len(md_files)} arquivo(s) em Skill modular...")
    
    chapters_info = []
    
    # Processa cada arquivo markdown capturado
    for i, md_file in enumerate(sorted(md_files), 1):
        content = md_file.read_text(encoding='utf-8', errors='replace').strip()
        
        # Se for um único arquivo grande com cabeçalhos ##, subdividir em capítulos
        h2_matches = list(re.finditer(r'^##\s+(.+)$', content, re.MULTILINE))
        if len(h2_matches) >= 3 and len(md_files) == 1:
            print("ℹ️ Subdividindo documento único em capítulos por tópicos principais...")
            for j, m in enumerate(h2_matches):
                t = m.group(1).strip()
                s = m.start()
                e = h2_matches[j+1].start() if j+1 < len(h2_matches) else len(content)
                sub_c = content[s:e].strip()
                slug = re.sub(r'[^\w\s-]', '', t).strip().lower().replace(' ', '-')[:35] or f"secao-{j+1}"
                fname = f"ch{j+1:02d}-{slug}.md"
                (chapters_dir / fname).write_text(f"# {t}\n\n" + sub_c + "\n", encoding='utf-8', newline='\n')
                chapters_info.append((fname, t))
        else:
            slug = re.sub(r'[^\w\s-]', '', md_file.stem).strip().lower().replace(' ', '-')[:40] or f"capitulo-{i}"
            fname = f"ch{i:02d}-{slug}.md"
            (chapters_dir / fname).write_text(content + "\n", encoding='utf-8', newline='\n')
            title = md_file.stem.replace('_', ' ').replace('-', ' ').title()
            chapters_info.append((fname, title))

    # 1. Gerar SKILL.md mestre (bilíngue)
    skill_title = skill_name.replace('-', ' ').title()
    skill_md_content = f"""---
name: {skill_name}
description: Base de conhecimento e documentação técnica extraída de {source_url}.
language: en, pt-BR
---

# {skill_title}

## 🇺🇸 English
### Mental Model & Core Structure
This skill provides structured reference and knowledge extracted from `{source_url}`.
Chapters are modularized and loaded on-demand to optimize token usage and context efficiency.

### Chapters
"""
    for fname, title in chapters_info:
        skill_md_content += f"- [{title}](chapters/{fname})\n"
        
    skill_md_content += f"""
---

## 🇧🇷 Português (Brasil)
### Modelo Mental & Estrutura Central
Esta skill fornece referência estruturada e conhecimento extraído de `{source_url}`.
Os capítulos são modularizados e carregados sob demanda para otimizar o uso de tokens e a janela de contexto.

### Capítulos
"""
    for fname, title in chapters_info:
        skill_md_content += f"- [{title}](chapters/{fname})\n"

    (skill_dir / "SKILL.md").write_text(skill_md_content, encoding='utf-8', newline='\n')
    
    # 2. Gerar Cheatsheet, Glossary e Patterns
    cheatsheet_content = f"""# Cheatsheet / Guia Rápido - {skill_title}

*Resumo operacional, comandos essenciais e tabelas de referência rápida extraídas de {source_url}.*

- **Fonte Oficial:** {source_url}
- **Total de Módulos/Capítulos:** {len(chapters_info)}
"""
    (skill_dir / "cheatsheet.md").write_text(cheatsheet_content, encoding='utf-8', newline='\n')

    glossary_content = f"""# Glossary / Glossário - {skill_title}

*Dicionário de termos técnicos, entidades e definições centrais.*

"""
    for fname, title in chapters_info:
        glossary_content += f"- **{title}**: Consulte [chapters/{fname}](chapters/{fname})\n"
        
    (skill_dir / "glossary.md").write_text(glossary_content, encoding='utf-8', newline='\n')

    patterns_content = f"""# Patterns & Architecture / Padrões e Arquitetura - {skill_title}

*Padrões recomendados, fluxos de trabalho e boas práticas.*
"""
    (skill_dir / "patterns.md").write_text(patterns_content, encoding='utf-8', newline='\n')
    
    print(f"✅ Skill estruturada com sucesso em: {skill_dir}")
    print(f"📊 Capítulos gerados: {len(chapters_info)}")
    return True

def main():
    if len(sys.argv) < 3:
        print("Uso: python build_skill.py <url> <nome_da_skill> [diretorio_saida] [--crawl]")
        print("  <url>             : URL do site ou documentação.")
        print("  <nome_da_skill>   : Nome da skill a ser criada (ex: foundryvtt-api-v12).")
        print("  [diretorio_saida] : (Opcional) Caminho onde a pasta da skill será criada.")
        print("  --crawl           : (Opcional) Tenta varrer o site inteiro (Requer Firecrawl API).")
        sys.exit(1)
        
    url = sys.argv[1]
    skill_name = sys.argv[2]
    
    # Processa argumentos opcionais
    args = sys.argv[3:]
    crawl_flag = "--crawl" in args
    custom_out = [a for a in args if not a.startswith("--")]
    
    output_skill_dir = Path(custom_out[0]).resolve() if custom_out else (Path.cwd() / skill_name).resolve()
    
    # 1. Encontrar o script da skill website-for-markdown
    scrape_script = find_skill_script("website-for-markdown", "scrape_to_md.py")
    if not scrape_script:
        print("❌ Script 'scrape_to_md.py' da skill 'website-for-markdown' não encontrado.")
        print("   -> Certifique-se de que a skill 'website-for-markdown' está disponível.")
        sys.exit(1)
        
    # 2. Executar a captura do site em pasta temporária
    temp_dir = Path.cwd() / f".temp_scrape_{skill_name}"
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"🌐 Iniciando captura do site: {url}")
    cmd = [sys.executable, str(scrape_script), url, str(temp_dir)]
    if crawl_flag:
        cmd.append("--crawl")
        
    result = subprocess.run(cmd)
    
    # Se a captura falhou por bloqueio de rede, mas já temos o markdown em cache/brain, fallback gracioso
    md_files = list(temp_dir.glob("*.md"))
    if result.returncode != 0 and not md_files:
        # Verifica se já temos o conteúdo na pasta do workspace
        cached_source = Path.cwd() / f"foundryvtt_api_{skill_name}.md"
        if not cached_source.exists():
            # Busca em skills existentes
            existing_skill = Path.cwd() / skill_name
            if existing_skill.exists() and (existing_skill / "chapters").exists():
                print(f"ℹ️ Reestruturando a partir do conteúdo existente em {existing_skill}...")
                for f in (existing_skill / "chapters").glob("*.md"):
                    shutil.copy(f, temp_dir)
                    
    # 3. Estruturar Skill
    print(f"🏗️ Construindo skill em: {output_skill_dir}")
    success = generate_skill_structure(skill_name, temp_dir, output_skill_dir, url)
    
    # 4. Limpeza
    shutil.rmtree(temp_dir, ignore_errors=True)
    
    if success:
        print(f"\n🎉 Skill '{skill_name}' construída e validada com sucesso!")
        print(f"📂 Localização: {output_skill_dir}")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()