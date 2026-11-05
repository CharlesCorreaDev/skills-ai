#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Not Today, ADHD! - Automated Ecosystem Downloader & Sync
Clona, baixa e atualiza repositórios de referência para ferramentas neurodivergentes/TDAH.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

ECOSYSTEM_REPOS = [
    {
        "name": "adhd",
        "author": "uditakhourii",
        "url": "https://github.com/uditakhourii/adhd.git",
        "desc": "Recursos de produtividade e quebra de paralisia de tarefa."
    },
    {
        "name": "i-have-adhd",
        "author": "ayghri",
        "url": "https://github.com/ayghri/i-have-adhd.git",
        "desc": "Estratégias diárias contra procrastinação e sobrecarga."
    },
    {
        "name": "awesome-adhd-tools",
        "author": "dicktracey909",
        "url": "https://github.com/dicktracey909/awesome-adhd-tools.git",
        "desc": "Coleção curada de ferramentas de suporte executivo."
    },
    {
        "name": "neurodivergent-memory",
        "author": "jmeyer1980",
        "url": "https://github.com/jmeyer1980/neurodivergent-memory.git",
        "desc": "Estratégias de preservação de memória de trabalho (Working Memory)."
    },
    {
        "name": "awesome-adhd",
        "author": "yutakobayashidev",
        "url": "https://github.com/yutakobayashidev/awesome-adhd.git",
        "desc": "Guia visual de ferramentas e extensões para TDAH."
    },
    {
        "name": "Loft-Hours",
        "author": "lazyfoxjumps",
        "url": "https://github.com/lazyfoxjumps/Loft-Hours.git",
        "desc": "Técnicas de micro-sessões de foco e ambientação sonora."
    },
    {
        "name": "adhd-copilot",
        "author": "zimai233",
        "url": "https://github.com/zimai233/adhd-copilot.git",
        "desc": "Assistente de decomposição atômica e body doubling."
    },
    {
        "name": "skill-engineering-tdah",
        "author": "murilonerdx",
        "url": "https://github.com/murilonerdx/skill-engineering-tdah.git",
        "desc": "Engenharia de software amigável para desenvolvedores com TDAH."
    },
    {
        "name": "adhd-classifier",
        "author": "lpassine",
        "url": "https://github.com/lpassine/adhd-classifier.git",
        "desc": "Classificação de padrões de dispersão vs hiperfoco."
    },
    {
        "name": "TDAH-REST-API",
        "author": "PedroLaRosa",
        "url": "https://github.com/PedroLaRosa/TDAH-REST-API.git",
        "desc": "APIs de rotina, medicação e timers contextuais."
    },
    {
        "name": "modo-tdah",
        "author": "rafamarchetti",
        "url": "https://github.com/rafamarchetti/modo-tdah.git",
        "desc": "Adaptação de tom e escrita em PT-BR para pessoas com TDAH."
    },
    {
        "name": "skill-tdah",
        "author": "lilian-barty",
        "url": "https://github.com/lilian-barty/skill-tdah.git",
        "desc": "Diretrizes práticas de comunicação livre de prolixidade."
    },
    {
        "name": "tdah-ia",
        "author": "saraivabr",
        "url": "https://github.com/saraivabr/tdah-ia.git",
        "desc": "Engenharia de prompts para IA acessível a neurodivergentes."
    }
]

def get_target_dir():
    # Diretório padrão: references/ecosystem dentro da skill not-today-adhd
    script_path = Path(__file__).resolve()
    skill_dir = script_path.parent.parent
    target_dir = skill_dir / "references" / "ecosystem"
    return target_dir

def sync_repos(target_dir):
    target_dir.mkdir(parents=True, exist_ok=True)
    print(f"🎯 Sincronizando ecossistema de referências TDAH em: {target_dir}\n")

    for repo in ECOSYSTEM_REPOS:
        repo_name = repo["name"]
        repo_url = repo["url"]
        repo_dest = target_dir / repo_name

        print(f"⚡ [{repo['author']}/{repo_name}]: {repo['desc']}")

        if repo_dest.exists() and (repo_dest / ".git").exists():
            print(f"   🔄 Atualizando repositório existente (git pull)...")
            try:
                subprocess.run(["git", "pull", "--depth=1"], cwd=str(repo_dest), check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print(f"   ✅ Atualizado com sucesso.")
            except Exception as e:
                print(f"   ⚠️ Aviso ao atualizar: {e}")
        else:
            print(f"   📥 Clonando (shallow clone)...")
            try:
                res = subprocess.run(["git", "clone", "--depth=1", repo_url, str(repo_dest)], check=False, capture_output=True, text=True)
                if res.returncode == 0:
                    print(f"   ✅ Clonado com sucesso.")
                else:
                    print(f"   ⚠️ Erro ou repositório privado/indisponível: {res.stderr.strip()}")
            except Exception as e:
                print(f"   ⚠️ Falha na execução do clone: {e}")

    print("\n🎉 Ecossistema sincronizado com sucesso!")

if __name__ == "__main__":
    dest = get_target_dir()
    sync_repos(dest)
