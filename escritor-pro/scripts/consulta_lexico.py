#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consulta Léxica, Regência Verbal e Vocabulário Normativo PT-BR
Parte integrante da skill Escritor Pro.
"""

import sys
import json
import argparse
import urllib.request
import urllib.error
import urllib.parse

# Base de Dados Offline de Regência Verbal Canônica (MEC / ABL / Celso Pedro Luft)
REGENCIA_CANONICA = {
    "assistir": {
        "sentidos": [
            {
                "acepcao": "Presenciar, ver",
                "transitividade": "Transitivo Indireto (preposição 'a')",
                "exemplo_correto": "Assistimos ao cerco da cidade imperial.",
                "erro_comum": "Assistimos o cerco da cidade imperial."
            },
            {
                "acepcao": "Prestar assistência, socorrer",
                "transitividade": "Transitivo Direto",
                "exemplo_correto": "A curandeira assistiu o soldado ferido.",
                "erro_comum": "A curandeira assistiu ao soldado ferido."
            },
            {
                "acepcao": "Caber, pertencer (direito)",
                "transitividade": "Transitivo Indireto (preposição 'a')",
                "exemplo_correto": "Assiste ao réu o direito de defesa."
            }
        ]
    },
    "aspirar": {
        "sentidos": [
            {
                "acepcao": "Almejar, pretender",
                "transitividade": "Transitivo Indireto (preposição 'a')",
                "exemplo_correto": "O cavaleiro aspirava ao título de lorde.",
                "erro_comum": "O cavaleiro aspirava o título de lorde."
            },
            {
                "acepcao": "Inalar, sorver",
                "transitividade": "Transitivo Direto",
                "exemplo_correto": "Aspirou o perfume acre da pólvora queimada."
            }
        ]
    },
    "visar": {
        "sentidos": [
            {
                "acepcao": "Ter por objetivo, almejar",
                "transitividade": "Transitivo Indireto (preposição 'a')",
                "exemplo_correto": "A conspiração visava ao trono da dinastia.",
                "erro_comum": "A conspiração visava o trono da dinastia."
            },
            {
                "acepcao": "Mirar arma / passar visto",
                "transitividade": "Transitivo Direto",
                "exemplo_correto": "O atirador visou o alvo a duzentos passos."
            }
        ]
    },
    "preferir": {
        "sentidos": [
            {
                "acepcao": "Dar primazia a algo em relação a outro",
                "transitividade": "Bitransitivo (Transitivo Direto e Indireto com preposição 'a')",
                "exemplo_correto": "Preferia a espada curta à lança de cavalaria.",
                "erro_comum": "Preferia a espada mais do que a lança / Preferia a espada do que a lança."
            }
        ]
    },
    "obedecer": {
        "sentidos": [
            {
                "acepcao": "Cumprir ordens",
                "transitividade": "Transitivo Indireto (preposição 'a')",
                "exemplo_correto": "Os sentinelas obedeciam às leis da cidadela.",
                "erro_comum": "Os sentinelas obedeciam as leis da cidadela."
            }
        ]
    },
    "implicar": {
        "sentidos": [
            {
                "acepcao": "Acarretar, ter como consequência",
                "transitividade": "Transitivo Direto (sem preposição)",
                "exemplo_correto": "A quebra do tratado implicará nova guerra.",
                "erro_comum": "A quebra do tratado implicará em nova guerra."
            },
            {
                "acepcao": "Comprometer, envolver em crime",
                "transitividade": "Transitivo Direto e Indireto (em)",
                "exemplo_correto": "Implicaram o chanceler na conspiração."
            }
        ]
    },
    "esquecer": {
        "sentidos": [
            {
                "acepcao": "Forma Não-Pronominal",
                "transitividade": "Transitivo Direto",
                "exemplo_correto": "Ele esqueceu a senha dos portões."
            },
            {
                "acepcao": "Forma Pronominal (esquecer-se)",
                "transitividade": "Transitivo Indireto (preposição 'de')",
                "exemplo_correto": "Ele se esqueceu da senha dos portões."
            }
        ]
    }
}

# Base de Vocabulário do Novo Acordo Ortográfico
ACORDO_ORTOGRAFICO = {
    "ideia": "Sem acento (ditongo aberto 'ei' em paroxítona). Antes da reforma: idéia.",
    "jiboia": "Sem acento (ditongo aberto 'oi' em paroxítona). Antes da reforma: jibóia.",
    "heroico": "Sem acento (ditongo aberto 'oi' em paroxítona). Antes da reforma: heróico.",
    "herói": "Com acento (oxítona terminada em ditongo aberto). Permanece acentuada.",
    "voo": "Sem acento circunflexo (hiato 'oo'). Antes da reforma: vôo.",
    "enjoo": "Sem acento circunflexo (hiato 'oo'). Antes da reforma: enjôo.",
    "leem": "Sem acento circunflexo (hiato 'ee'). Antes da reforma: lêem.",
    "veem": "Sem acento circunflexo (hiato 'ee'). Antes da reforma: vêem.",
    "anti-inflamatório": "Com hífen (vogais iguais se separam).",
    "autoestrada": "Sem hífen (vogais diferentes se unem).",
    "microssistema": "Sem hífen, dobra-se o 's' (vogal + r/s).",
    "antirreflexo": "Sem hífen, dobra-se o 'r' (vogal + r/s).",
    "paraquedas": "Sem hífen e sem acento (aglutinação consagrada).",
    "guarda-chuva": "Com hífen (composto por justaposição com perda de sentido isolado).",
    "pôde": "Com acento diferencial (pretérito perfeito). Presente: pode.",
    "pôr": "Com acento diferencial (verbo). Preposição: por."
}

def consultar_regencia(verbo: str):
    v = verbo.lower().strip()
    if v in REGENCIA_CANONICA:
        dados = REGENCIA_CANONICA[v]
        print(f"\n📚 REGÊNCIA VERBAL CANÔNICA: '{v.upper()}'")
        print("=" * 60)
        for i, s in enumerate(dados["sentidos"], 1):
            print(f"[{i}] Sentido: {s['acepcao']}")
            print(f"    • Classificação: {s['transitividade']}")
            print(f"    • ✅ Correto:     {s['exemplo_correto']}")
            if "erro_comum" in s:
                print(f"    • ❌ Erro Comum:  {s['erro_comum']}")
            print()
    else:
        print(f"Verbo '{verbo}' não listado na tabela local de regências críticas.")
        print("Dica: Verbos usuais podem ser consultados nos manuais de Rocha Lima ou Bechara.")

def consultar_acordo(palavra: str):
    p = palavra.lower().strip()
    if p in ACORDO_ORTOGRAFICO:
        print(f"\n📖 NOVO ACORDO ORTOGRÁFICO (ABL/VOLP): '{p}'")
        print("=" * 60)
        print(f"Regra: {ACORDO_ORTOGRAFICO[p]}")
    else:
        print(f"Palavra '{palavra}' não possui caso especial listado na memória rápida.")

def consultar_dicionario_api(palavra: str):
    """Consulta segura à API pública do Dicio / Dicionário Aberto com fallback"""
    url = f"https://api.dicionario-aberto.net/word/{urllib.parse.quote(palavra)}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "EscritorPro/1.0 (Skill Assistente de Escrita; Python)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                if data and isinstance(data, list) and len(data) > 0:
                    xml_entry = data[0].get("xml", "")
                    # Limpeza rudimentar de tags XML
                    clean_def = re.sub(r"<[^>]+>", " ", xml_entry).strip()
                    clean_def = re.sub(r"\s+", " ", clean_def)
                    print(f"\n📖 DICIONÁRIO ABERTO: '{palavra}'")
                    print("=" * 60)
                    print(clean_def[:600] + ("..." if len(clean_def) > 600 else ""))
                    return
        print(f"Nenhuma definição encontrada na API pública para '{palavra}'.")
    except Exception as e:
        print(f"Consulta remota indisponível ou palavra não encontrada ({e}).")

def main():
    parser = argparse.ArgumentParser(description="Consulta Léxica, Regência e Ortografia PT-BR")
    parser.add_argument("termo", nargs="?", help="Palavra ou verbo a consultar")
    parser.add_argument("--regencia", "-r", action="store_true", help="Focar em regência verbal")
    parser.add_argument("--acordo", "-a", action="store_true", help="Checar regra do Novo Acordo Ortográfico")
    parser.add_argument("--online", "-o", action="store_true", help="Tentar buscar definição em dicionário online")

    args = parser.parse_args()

    if not args.termo:
        parser.print_help()
        sys.exit(1)

    t = args.termo.lower().strip()
    
    if args.regencia:
        consultar_regencia(t)
    elif args.acordo:
        consultar_acordo(t)
    elif args.online:
        consultar_dicionario_api(t)
    else:
        # Modo inteligente: checa onde encaixa
        matched = False
        if t in REGENCIA_CANONICA:
            consultar_regencia(t)
            matched = True
        if t in ACORDO_ORTOGRAFICO:
            consultar_acordo(t)
            matched = True
        if not matched:
            print(f"Termo '{t}' não encontrado nas bases de regras prioritárias.")
            print("Tentando dicionário aberto...")
            consultar_dicionario_api(t)

if __name__ == "__main__":
    main()
