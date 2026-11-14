#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisador de Estilo, Anti-Slop e Pontuação de Diálogos PT-BR
Parte integrante da skill Escritor Pro.
"""

import sys
import os
import re
import argparse
from pathlib import Path

# Lista negra de AI Slop e clichês sintéticos comuns
AI_SLOP_PATTERNS = [
    (r"\bturbilh[ãa]o de emo[çc][õo]es\b", "turbilhão de emoções (clichê de IA)"),
    (r"\bdan[çc]a (?:perigosa |mortal )?de sombras\b", "dança de sombras (clichê de IA)"),
    (r"\btestamento (?:da|de) resili[êe]ncia\b", "testamento de resiliência (clichê de IA)"),
    (r"\bpouco sabia ele\b", "pouco sabia ele (foreshadowing artificial)"),
    (r"\bfarol de esperan[çc]a\b", "farol de esperança (clichê de IA)"),
    (r"\bolhos faiscando\b", "olhos faiscando (clichê de IA)"),
    (r"\bo tempo parecia ter (?:parado|congelado)\b", "tempo congelado/parado (clichê de IA)"),
    (r"\btens[ãa]o palp[áa]vel\b", "tensão palpável (clichê de IA)"),
    (r"\bum lembrete sombrio\b", "lembrete sombrio (moralização sintética)"),
    (r"\bem suma,\b", "'em suma,' (conclusão acadêmica em ficção)"),
    (r"\bem [úu]ltima an[áa]lise,\b", "'em última análise,' (conclusão acadêmica em ficção)"),
    (r"\bum misto de emo[çc][õo]es\b", "misto de emoções (vaguidão emocional)"),
    (r"\bcalafrio na espinha\b", "calafrio na espinha (clichê físico gasto)"),
    (r"\bo cora[çc][ãa]o quase saltou pela boca\b", "coração saltou pela boca (clichê gasto)"),
]

# Léxicos sensoriais para checagem da Regra 3+1
SENSORY_LEXICON = {
    "visao": [
        "luz", "sombra", "brilho", "cor", "escuro", "vermelho", "azul", "dourado",
        "palha", "cinzento", "nevoa", "fumaca", "vislumbre", "silhueta", "claridade",
        "fosco", "lamparina", "chama", "fuligem", "olhar", "enxergar", "reflexo"
    ],
    "audicao": [
        "som", "ruido", "eco", "sussurro", "grito", "estalo", "baque", "rangido",
        "silencio", "passos", "zumbido", "guincho", "estrondo", "clamor", "farfalhar",
        "resfolego", "chiado", "bater", "tilintar", "rugido"
    ],
    "olfato_tato": [
        "cheiro", "odor", "frio", "calor", "suor", "umido", "seco", "aspero",
        "macio", "ardor", "queimado", "podre", "salobra", "enxofre", "ferro",
        "vento", "lama", "poeira", "calafrio", "pegajoso", "gelado", "morno"
    ]
}

# Verbos de percepção em excesso
PERCEPTION_VERBS = [
    r"\bele sentiu\b", r"\bela sentiu\b",
    r"\bele viu\b", r"\bela viu\b",
    r"\bele ouviu\b", r"\bela ouviu\b",
    r"\bele percebeu\b", r"\bela percebeu\b",
    r"\bele notou\b", r"\bela notou\b",
]

def analyze_text(text: str) -> dict:
    lines = text.splitlines()
    words = re.findall(r"\b\w+\b", text, re.IGNORECASE)
    word_count = len(words)
    
    # 1. Checagem de Diálogos e Travessões
    dialogue_issues = []
    dialogue_count = 0
    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped:
            continue
        
        # Início com hífen ou traço médio em vez de travessão em
        if stripped.startswith("- ") or stripped.startswith("– "):
            dialogue_issues.append((idx, "Linha inicia com hífen '-' ou traço '–' em vez do travessão oficial '—' (\\u2014)"))
        elif stripped.startswith("—") and not stripped.startswith("— "):
            dialogue_issues.append((idx, "Travessão inicial '—' deve ser seguido de espaço"))
            
        if stripped.startswith("—") or stripped.startswith("- ") or stripped.startswith("– "):
            dialogue_count += 1
            # Checar fala terminada com ponto antes de verbo dicendi
            # Ex: — Olá. — disse ele. (Errado)
            m = re.search(r"—\s*([^—]+?)\.\s*—\s*([a-zà-ú]+)", stripped)
            if m:
                verbo = m.group(2)
                dicendi = ["disse", "falou", "respondeu", "perguntou", "sussurrou", "gritou", "retrucou", "indagou", "murmurou"]
                if verbo in dicendi:
                    dialogue_issues.append((idx, f"Ponto final indevido antes de verbo dicendi '{verbo}'. Use vírgula: '— Fala, — {verbo}.'"))

    # 2. Checagem de AI Slop
    slop_findings = []
    for pattern, label in AI_SLOP_PATTERNS:
        matches = re.finditer(pattern, text, re.IGNORECASE)
        for m in matches:
            slop_findings.append({
                "trecho": m.group(0),
                "motivo": label,
                "pos": m.start()
            })

    # 3. Verbos de Percepção (Filter Words)
    perception_findings = []
    for p_pat in PERCEPTION_VERBS:
        matches = re.finditer(p_pat, text, re.IGNORECASE)
        for m in matches:
            perception_findings.append(m.group(0))

    # 4. Densidade Sensorial
    lower_text = text.lower()
    sensory_hits = {
        "visao": sum(lower_text.count(k) for k in SENSORY_LEXICON["visao"]),
        "audicao": sum(lower_text.count(k) for k in SENSORY_LEXICON["audicao"]),
        "olfato_tato": sum(lower_text.count(k) for k in SENSORY_LEXICON["olfato_tato"]),
    }

    return {
        "word_count": word_count,
        "line_count": len(lines),
        "dialogue_count": dialogue_count,
        "dialogue_issues": dialogue_issues,
        "slop_findings": slop_findings,
        "perception_findings": perception_findings,
        "sensory_hits": sensory_hits,
        "reading_time_min": round(word_count / 200, 1)
    }

def print_report(res: dict):
    print("=" * 60)
    print("  RELATÓRIO DE ESTILO E QUALIDADE TEXTUAL - ESCRITOR PRO")
    print("=" * 60)
    print(f"Total de Palavras: {res['word_count']}")
    print(f"Total de Linhas:   {res['line_count']}")
    print(f"Tempo de Leitura:  ~{res['reading_time_min']} min (base: 200 ppm)")
    print(f"Falas de Diálogo:  {res['dialogue_count']}")
    print("-" * 60)
    
    # Sensorial
    print("DENSIDADE SENSORIAL (REGRA 3+1):")
    v = res["sensory_hits"]
    print(f"  • Visão:       {v['visao']} menções")
    print(f"  • Audição:     {v['audicao']} menções")
    print(f"  • Olfato/Tato: {v['olfato_tato']} menções")
    atende_sensorial = all(count > 0 for count in v.values())
    if atende_sensorial:
        print("  ✅ Estimulação multissensorial equilibrada presente!")
    else:
        print("  ⚠️ Atenção: ao menos um sentido vital está ausente ou pouco explorado.")
    print("-" * 60)
    
    # Diálogos
    if res["dialogue_issues"]:
        print(f"🚨 PROBLEMAS DE PONTUAÇÃO DE DIÁLOGO ({len(res['dialogue_issues'])}):")
        for line_num, msg in res["dialogue_issues"][:10]:
            print(f"  [Linha {line_num}]: {msg}")
        if len(res["dialogue_issues"]) > 10:
            print(f"  ... e mais {len(res['dialogue_issues']) - 10} avisos.")
    else:
        print("✅ Pontuação de diálogos em conformidade com as normas ABL!")
    print("-" * 60)

    # Slop
    if res["slop_findings"]:
        print(f"⚠️ CLICHÊS SINTÉTICOS / AI SLOP ENCONTRADOS ({len(res['slop_findings'])}):")
        for s in res["slop_findings"][:10]:
            print(f"  • '{s['trecho']}' ➔ {s['motivo']}")
    else:
        print("✅ Texto limpo de clichês estatísticos e AI slop!")
    print("-" * 60)

    # Verbos de Percepção
    if res["perception_findings"]:
        print(f"ℹ️ Verbos de Percepção excessivos encontrados: {len(res['perception_findings'])}")
        print(f"   Amostra: {', '.join(res['perception_findings'][:8])}")
        print("   Dica: Transforme em 'Show, Don't Tell' direto eliminando 'ele sentiu / ela viu'.")
    else:
        print("✅ Excelente imersão direta sem verbos de percepção frouxos.")
    print("=" * 60)

def main():
    parser = argparse.ArgumentParser(description="Analisador de Estilo Literário e Anti-Slop PT-BR")
    parser.add_argument("arquivo", nargs="?", help="Caminho do arquivo de texto ou Markdown para analisar")
    parser.add_argument("--texto", "-t", help="Texto direto entre aspas para análise rápida")
    
    args = parser.parse_args()
    
    if args.texto:
        text = args.texto
    elif args.arquivo:
        p = Path(args.arquivo)
        if not p.exists():
            print(f"Erro: Arquivo '{args.arquivo}' não encontrado.")
            sys.exit(1)
        text = p.read_text(encoding="utf-8")
    else:
        # Lê de stdin se fornecido via pipe
        if not sys.stdin.isatty():
            text = sys.stdin.read()
        else:
            parser.print_help()
            sys.exit(1)
            
    results = analyze_text(text)
    print_report(results)

if __name__ == "__main__":
    main()
