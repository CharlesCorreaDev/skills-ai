#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consulta Léxica Multilíngue (PT-BR, EN, ES), Regência, Falsos Cognatos e Emoções
Parte integrante da skill Escritor Pro.
"""

import sys
import os
import re
import json
import argparse
import urllib.request
import urllib.error
import urllib.parse
from pathlib import Path

# Base de Dados de Falsos Cognatos Críticos (Inglês ➔ PT-BR)
FALSOS_COGNATOS_EN = {
    "eventually": {
        "falso_amigo": "eventualmente",
        "sentido_real": "Ao final, por fim, com o tempo, mais cedo ou mais tarde",
        "exemplo_correto": "After three days of siege, the gates eventually opened (Ao final, os portões se abriram).",
        "alerta": "'Eventualmente' em português significa apenas 'às vezes' ou 'por acaso', não 'ao final'."
    },
    "pretend": {
        "falso_amigo": "pretender",
        "sentido_real": "Fingir, simular, aparentar",
        "exemplo_correto": "The spy pretended to be a merchant (O espião fingiu ser um mercador).",
        "alerta": "'Pretender' em português é 'to intend' (ter a intenção de)."
    },
    "intend": {
        "falso_amigo": "entender",
        "sentido_real": "Pretender, ter a intenção de, planejar",
        "exemplo_correto": "I intend to march at dawn (Pretendo marchar ao amanhecer)."
    },
    "actually": {
        "falso_amigo": "atualmente",
        "sentido_real": "Na verdade, na realidade, de fato",
        "exemplo_correto": "He actually knew the secret password (Na verdade, ele sabia a contra-senha)."
    },
    "currently": {
        "falso_amigo": "correntemente",
        "sentido_real": "Atualmente, nos dias de hoje, no momento presente",
        "exemplo_correto": "Currently, the king is away (Atualmente, o rei está ausente)."
    },
    "grip": {
        "falso_amigo": "gripe",
        "sentido_real": "Empunhadura, pegada firme, garra",
        "exemplo_correto": "He tightened his grip on the hilt (Ele apertou a empunhadura da espada)."
    },
    "novel": {
        "falso_amigo": "novela de TV",
        "sentido_real": "Romance literário",
        "exemplo_correto": "He wrote a fantasy novel (Ele escreveu um romance de fantasia)."
    },
    "fabric": {
        "falso_amigo": "fábrica",
        "sentido_real": "Tecido, pano, estofo",
        "exemplo_correto": "Silk is a delicate fabric (A seda é um tecido delicado)."
    },
    "hazard": {
        "falso_amigo": "azar",
        "sentido_real": "Perigo iminente, risco grave",
        "exemplo_correto": "Fire is a hazard in wooden ships (O fogo é um perigo em navios de madeira)."
    },
    "realize": {
        "falso_amigo": "realizar (concretizar)",
        "sentido_real": "Dar-se conta de, perceber, notar",
        "exemplo_correto": "She realized she was alone (Ela deu-se conta de que estava sozinha)."
    }
}

# Base de Dados de Falsos Cognatos Críticos (Espanhol ➔ PT-BR)
FALSOS_COGNATOS_ES = {
    "exquisito": {
        "falso_amigo": "esquisito (estranho)",
        "sentido_real": "Delicioso, requintado, saboroso, refinado",
        "exemplo_correto": "Un vino exquisito (Um vinho refinado/delicioso)."
    },
    "raro": {
        "falso_amigo": "apenas escasso",
        "sentido_real": "Estranho, bizarro, excêntrico, invulgar",
        "exemplo_correto": "Tiene un comportamiento raro (Tem um comportamento bizarro/estranho)."
    },
    "largo": {
        "falso_amigo": "largo (espaçoso)",
        "sentido_real": "Comprido, longo no comprimento",
        "exemplo_correto": "Un camino largo (Um caminho comprido/longo. 'Largo' em espanhol é 'ancho')."
    },
    "espalda": {
        "falso_amigo": "espada",
        "sentido_real": "Costas, dorso",
        "exemplo_correto": "Le clavó un puñal por la espalda (Cravou-lhe um punhal pelas costas)."
    },
    "cena": {
        "falso_amigo": "cena (de teatro/filme)",
        "sentido_real": "Jantar, ceia",
        "exemplo_correto": "La cena está servida (O jantar está servido. 'Cena' de teatro é 'escena')."
    },
    "polvo": {
        "falso_amigo": "polvo (molusco)",
        "sentido_real": "Pó, poeira",
        "exemplo_correto": "El camino lleno de polvo (O caminho cheio de poeira. O molusco é 'pulpo')."
    },
    "borrar": {
        "falso_amigo": "borrar (sujar)",
        "sentido_real": "Apagar, eliminar, rasurar",
        "exemplo_correto": "Borrar las huellas (Apagar as pegadas/rastros)."
    },
    "todavia": {
        "falso_amigo": "todavia (contudo, mas)",
        "sentido_real": "Ainda, até este momento",
        "exemplo_correto": "Todavía no ha llegado (Ainda não chegou)."
    }
}

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
                "exemplo_correto": "O plano visava à queda do tirano.",
                "erro_comum": "O plano visava a queda do tirano (sem crase se feminino)."
            },
            {
                "acepcao": "Mirar arma ou alvo",
                "transitividade": "Transitivo Direto",
                "exemplo_correto": "O arqueiro visou o centro do elmo inimigo."
            },
            {
                "acepcao": "Apor visto / rubricar documento",
                "transitividade": "Transitivo Direto",
                "exemplo_correto": "O magistrado visou os decretos de execução."
            }
        ]
    },
    "implicar": {
        "sentidos": [
            {
                "acepcao": "Acarretar, ter como consequência",
                "transitividade": "Transitivo Direto (NÃO admite preposição 'em')",
                "exemplo_correto": "A quebra da trégua implicará guerra total.",
                "erro_comum": "A quebra da trégua implicará em guerra total."
            },
            {
                "acepcao": "Antipatizar, implicar com alguém",
                "transitividade": "Transitivo Indireto (preposição 'com')",
                "exemplo_correto": "O capitão implicava com os recrutas novatos."
            }
        ]
    },
    "preferir": {
        "sentidos": [
            {
                "acepcao": "Querer antes, ter primazia",
                "transitividade": "Transitivo Direto e Indireto (rege preposição 'a', NUNCA 'do que')",
                "exemplo_correto": "Preferia a morte honrosa à rendição vergonhosa.",
                "erro_comum": "Preferia a morte do que a rendição / Preferia mais a morte..."
            }
        ]
    },
    "esquecer": {
        "sentidos": [
            {
                "acepcao": "Sem pronome reflexivo (não-pronominal)",
                "transitividade": "Transitivo Direto (sem preposição)",
                "exemplo_correto": "Ele esqueceu a chave da masmorra.",
                "erro_comum": "Ele esqueceu da chave."
            },
            {
                "acepcao": "Com pronome reflexivo (esquecer-se)",
                "transitividade": "Transitivo Indireto (rege preposição 'de')",
                "exemplo_correto": "Ele se esqueceu da chave da masmorra."
            }
        ]
    },
    "lembrar": {
        "sentidos": [
            {
                "acepcao": "Sem pronome reflexivo (não-pronominal)",
                "transitividade": "Transitivo Direto (sem preposição)",
                "exemplo_correto": "Lembrei os rostos dos traidores.",
                "erro_comum": "Lembrei dos rostos."
            },
            {
                "acepcao": "Com pronome reflexivo (lembrar-se)",
                "transitividade": "Transitivo Indireto (rege preposição 'de')",
                "exemplo_correto": "Lembrei-me dos rostos dos traidores."
            }
        ]
    },
    "obedecer": {
        "sentidos": [
            {
                "acepcao": "Cumprir ordem, submeter-se",
                "transitividade": "Transitivo Indireto (exige preposição 'a')",
                "exemplo_correto": "A tropa obedeceu aos comandos do general.",
                "erro_comum": "A tropa obedeceu os comandos do general."
            }
        ]
    },
    "desobedecer": {
        "sentidos": [
            {
                "acepcao": "Não cumprir ordem",
                "transitividade": "Transitivo Indireto (exige preposição 'a')",
                "exemplo_correto": "Desobedeceu às leis do reino.",
                "erro_comum": "Desobedeceu as leis do reino."
            }
        ]
    },
    "proceder": {
        "sentidos": [
            {
                "acepcao": "Realizar, dar início",
                "transitividade": "Transitivo Indireto (exige preposição 'a')",
                "exemplo_correto": "O inquisidor procedeu à leitura da sentença.",
                "erro_comum": "Procedeu a leitura (sem crase)."
            },
            {
                "acepcao": "Originar-se, descender",
                "transitividade": "Transitivo Indireto (exige preposição 'de')",
                "exemplo_correto": "Sua linhagem procede de reis antigos."
            },
            {
                "acepcao": "Ter fundamento ou lógica",
                "transitividade": "Intransitivo",
                "exemplo_correto": "Os temores do sentinela procedem."
            }
        ]
    }
}

# Casos Críticos do Novo Acordo Ortográfico
ACORDO_ORTOGRAFICO = {
    "ideia": "Sem acento (ditongo aberto 'ei' em palavra paroxítona).",
    "jiboia": "Sem acento (ditongo aberto 'oi' em palavra paroxítona).",
    "heroico": "Sem acento (ditongo aberto 'oi' em palavra paroxítona).",
    "paranoia": "Sem acento (ditongo aberto 'oi' em palavra paroxítona).",
    "coreia": "Sem acento (ditongo aberto 'ei' em palavra paroxítona).",
    "heroi": "Grafia com acento: 'herói' (ditongo aberto em oxítona mantém o acento).",
    "constroi": "Grafia com acento: 'constrói' (ditongo aberto em oxítona mantém o acento).",
    "voo": "Sem acento (hiato 'oo' perdeu o circunflexo).",
    "enjoo": "Sem acento (hiato 'oo' perdeu o circunflexo).",
    "veem": "Sem acento (hiato 'ee' da 3ª pessoa do plural do verbo ver perdeu o circunflexo).",
    "leem": "Sem acento (hiato 'ee' do verbo ler perdeu o circunflexo).",
    "creem": "Sem acento (hiato 'ee' do verbo crer perdeu o circunflexo).",
    "deem": "Sem acento (hiato 'ee' do verbo dar perdeu o circunflexo).",
    "para": "Sem acento circunflexo diferencial no verbo parar.",
    "pelo": "Sem acento circunflexo diferencial em substantivo (pêlo caiu).",
    "tranquilo": "Sem trema (abolido na língua portuguesa).",
    "cinquenta": "Sem trema.",
    "linguiça": "Sem trema.",
    "para-raios": "Com hífen.",
    "anti-inflamatorio": "Com hífen: 'anti-inflamatório'.",
    "antirreligioso": "Sem hífen e dobra 'r': 'antirreligioso'.",
    "minissaia": "Sem hífen e dobra 's': 'minissaia'.",
    "autoestima": "Junto sem hífen: 'autoestima'.",
    "infraestrutura": "Junto sem hífen: 'infraestrutura'."
}

# Base de Dados do Emotion Thesaurus
THESAURUS_EMOCOES = {
    "raiva": {
        "sinonimos": ["fúria", "ira", "ódio", "cólera", "indignação"],
        "autonomicas": ["sangue pulsando nas têmporas", "visão em túnel", "rubor no pescoço e orelhas", "boca seca"],
        "musculares": ["maxilar travado até doer os molares", "punhos cerrados com unhas cravadas", "ombros projetados à frente"],
        "micro_acoes": ["falar entredentes", "bater ou apertar objetos até estalar", "engolir em seco"],
        "show_dont_tell": "O sangue latejou atrás dos olhos. Ele cravou as unhas nas palmas até a ponta dos dedos embranquecer, as mandíbulas cerradas com força."
    },
    "medo": {
        "sinonimos": ["pânico", "terror", "pavor", "apreensão", "temor"],
        "autonomicas": ["pele arrepiada", "suor frio descendo pelas costas", "nó súbito no estômago (náusea)", "pupilas dilatadas"],
        "musculares": ["ombros encolhidos", "recuo involuntário de meio passo", "ar preso no peito", "tremores nos joelhos"],
        "micro_acoes": ["olhos varrendo saídas de emergência", "umedecer lábios rachados", "cruzar braços sobre o abdômen"],
        "show_dont_tell": "O ar travou no peito. Um filete de suor gelado desceu entre suas omoplatas enquanto os joelhos vacilavam sob o peso do corpo."
    },
    "tristeza": {
        "sinonimos": ["luto", "pesar", "dor", "desolação", "melancolia"],
        "autonomicas": ["vazio oco na boca do estômago", "peso de chumbo nos membros", "ardor ocular", "respiração pontuada por suspiros"],
        "musculares": ["perda de tônus (ombros caídos)", "cabeça pendente", "passos arrastados", "movimentos lentos"],
        "micro_acoes": ["acariciar objeto de quem partiu", "olhar fixo no vazio sem registrar estímulos", "voz monossilábica e rouca"],
        "show_dont_tell": "Os pés arrastavam-se pela lama como se as botas estivessem cheias de cascalho. Ele girava a medalha amassada entre o polegar e o indicador."
    },
    "vergonha": {
        "sinonimos": ["humilhação", "constrangimento", "acanhamento", "vexame"],
        "autonomicas": ["calor súbito subindo pelo tórax", "orelhas incandescentes", "suor na testa"],
        "musculares": ["postura encolhida tentando sumir", "queixo grudado ao peito", "braços colados ao tronco"],
        "micro_acoes": ["pigarrear sem motivo", "ajeitar roupa já alinhada", "olhar fixo em manchas no chão"],
        "show_dont_tell": "O calor subiu pelas bochechas até abrasar a ponta das orelhas. Ela recolheu os cotovelos contra as costelas, baixando o olhar."
    },
    "culpa": {
        "sinonimos": ["remorso", "pesar", "arrependimento"],
        "autonomicas": ["peso físico sobre o peito", "nó na garganta", "ardor sem lágrimas", "estômago revirado"],
        "musculares": ["olhar esquivo", "ombros caídos", "mãos escondidas nos bolsos"],
        "micro_acoes": ["coçar a nuca repetidamente", "roer cantos das unhas", "falar em sussurros monótonos"],
        "show_dont_tell": "Ele não suportou encarar a mesa. Um peso opressor assentou-se sobre suas clavículas, e sua mão subiu para a nuca, coçando uma pele que já ardia vermelha."
    },
    "atracao": {
        "sinonimos": ["desejo", "paixão", "tensão sexual", "encanto"],
        "autonomicas": ["frequência cardíaca elevada", "pupilas dilatadas", "respiração superficial", "boca entreaberta"],
        "musculares": ["corpo inclinado na direção do outro", "maxilar relaxado", "postura magnética"],
        "micro_acoes": ["passar a língua nos lábios secos", "ajeitar o cabelo expondo o pescoço", "sustentação prolongada de olhar"],
        "show_dont_tell": "Quando ele estendeu o cantil, o olhar dela demorou-se na curva suada do seu pescoço. Ela umedeceu os lábios antes de segurar o couro."
    },
    "arrogancia": {
        "sinonimos": ["desprezo", "altivez", "soberba", "desdém"],
        "autonomicas": ["respiração nasal lenta e insolente", "relaxamento deliberado do semblante"],
        "musculares": ["queixo erguido", "olhar de cima para baixo", "coluna displicentemente recostada"],
        "micro_acoes": ["canto da boca repuxado em esgar unilateral", "afastar fiapo invisível da roupa", "ignorar falas"],
        "show_dont_tell": "O emissário recostou-se no espaldar almofadado, erguendo uma sobrancelha displicente enquanto afastava uma partícula imaginária da manga de veludo."
    },
    "ansiedade": {
        "sinonimos": ["insegurança", "nervosismo", "inquietação", "aflição"],
        "autonomicas": ["mãos úmidas e frias", "palpitações irregulares", "falta de ar", "amargor na boca"],
        "musculares": ["pernas inquietas batendo no chão", "ombros tensionados junto às orelhas", "dedos irrequietos"],
        "micro_acoes": ["estalar juntas dos dedos", "morder interior da bochecha", "checar maçaneta a cada trinta segundos"],
        "show_dont_tell": "A ponta de sua bota batia ritmicamente contra o assoalho de tábuas. Ele esfregou as palmas suadas nas calças de feltro, puxando a gola sufocante."
    }
}

def consultar_falso_cognato(termo: str):
    t = termo.lower().strip()
    if t in FALSOS_COGNATOS_EN:
        f = FALSOS_COGNATOS_EN[t]
        print(f"\n⚠️ FALSO COGNATO CRÍTICO (INGLÊS ➔ PT-BR): '{t.upper()}'")
        print("=" * 65)
        print(f"❌ Não confunda com:  '{f['falso_amigo']}'")
        print(f"✅ Sentido Real:      {f['sentido_real']}")
        print(f"📖 Exemplo Correto:   {f['exemplo_correto']}")
        if "alerta" in f:
            print(f"💡 Alerta:            {f['alerta']}")
        return True
    elif t in FALSOS_COGNATOS_ES:
        f = FALSOS_COGNATOS_ES[t]
        print(f"\n⚠️ FALSO COGNATO CRÍTICO (ESPANHOL ➔ PT-BR): '{t.upper()}'")
        print("=" * 65)
        print(f"❌ Não confunda com:  '{f['falso_amigo']}'")
        print(f"✅ Sentido Real:      {f['sentido_real']}")
        print(f"📖 Exemplo Correto:   {f['exemplo_correto']}")
        return True
    return False

def consultar_dicionario_ingles(palavra: str):
    """Consulta à API pública do Free Dictionary (Inglês)"""
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{urllib.parse.quote(palavra)}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "EscritorPro/1.0 (Skill Assistente de Escrita; Python)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                if data and isinstance(data, list) and len(data) > 0:
                    entry = data[0]
                    word = entry.get("word", palavra)
                    phonetic = entry.get("phonetic", "")
                    print(f"\n🇬🇧 DICTIONARY (ENGLISH): '{word.upper()}' {phonetic}")
                    print("=" * 65)
                    meanings = entry.get("meanings", [])
                    for m in meanings[:3]:
                        part = m.get("partOfSpeech", "")
                        print(f"[{part.upper()}]")
                        for d in m.get("definitions", [])[:2]:
                            print(f"  • {d.get('definition', '')}")
                            if "example" in d:
                                print(f"    Ex: \"{d.get('example')}\"")
                    return
        print(f"No definition found in English dictionary for '{palavra}'.")
    except Exception as e:
        print(f"Online English dictionary unavailable or word not found ({e}).")

def consultar_dicionario_espanhol(palavra: str):
    """Consulta à API pública do Wiktionary / Dicionário em Espanhol com fallback inteligente"""
    url = f"https://es.wiktionary.org/api/rest_v1/page/definition/{urllib.parse.quote(palavra)}"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "EscritorPro/1.0 (Skill Assistente de Escrita; Python)"}
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            if response.status == 200:
                data = json.loads(response.read().decode("utf-8"))
                if data and "es" in data:
                    print(f"\n🇪🇸 DICCIONARIO (ESPAÑOL): '{palavra.upper()}'")
                    print("=" * 65)
                    for item in data["es"][:2]:
                        pos = item.get("partOfSpeech", "")
                        print(f"[{pos.upper()}]")
                        for d in item.get("definitions", [])[:2]:
                            clean = re.sub(r"<[^>]+>", "", d.get("definition", "")).strip()
                            print(f"  • {clean}")
                    return
        print(f"No se encontró definición en español para '{palavra}'.")
    except Exception as e:
        print(f"Diccionario en español no disponible o palabra no encontrada ({e}).")

def consultar_regencia(verbo: str):
    v = verbo.lower().strip()
    if v in REGENCIA_CANONICA:
        dados = REGENCIA_CANONICA[v]
        print(f"\n📚 REGÊNCIA VERBAL CANÔNICA: '{v.upper()}'")
        print("=" * 60)
        for idx, s in enumerate(dados["sentidos"], 1):
            print(f"[{idx}] Acepação:      {s['acepcao']}")
            print(f"    • Transitividade: {s['transitividade']}")
            print(f"    • ✅ Exemplo:     {s['exemplo_correto']}")
            if "erro_comum" in s:
                print(f"    • ❌ Erro Comum:  {s['erro_comum']}")
            print()
    else:
        print(f"Verbo '{verbo}' não listado na tabela local de regências críticas.")

def consultar_acordo(palavra: str):
    p = palavra.lower().strip()
    if p in ACORDO_ORTOGRAFICO:
        print(f"\n📖 NOVO ACORDO ORTOGRÁFICO (ABL/VOLP): '{p}'")
        print("=" * 60)
        print(f"Regra: {ACORDO_ORTOGRAFICO[p]}")
    else:
        print(f"Palavra '{palavra}' não possui caso especial listado na memória rápida.")

def consultar_emocao(termo: str):
    t = termo.lower().strip()
    encontrado = None
    nome_chave = ""
    for chave, dados in THESAURUS_EMOCOES.items():
        if chave == t or t in dados["sinonimos"]:
            encontrado = dados
            nome_chave = chave
            break
            
    if encontrado:
        print(f"\n🧠 THE EMOTION THESAURUS (SHOW, DON'T TELL): '{nome_chave.upper()}'")
        print("=" * 65)
        print(f"Sinônimos / Tons afins: {', '.join(encontrado['sinonimos'])}")
        print("\n⚡ REAÇÕES AUTONÔMICAS (INVOLUNTÁRIAS DO CORPO):")
        for r in encontrado["autonomicas"]:
            print(f"  • {r}")
        print("\n💪 TENSÃO MUSCULAR & POSTURA:")
        for m in encontrado["musculares"]:
            print(f"  • {m}")
        print("\n👀 MICRO-AÇÕES & TIQUES:")
        for a in encontrado["micro_acoes"]:
            print(f"  • {a}")
        print("\n✨ MODELO DE TRANSFORMAÇÃO 'SHOW, DON'T TELL':")
        print(f"  {encontrado['show_dont_tell']}")
        print("=" * 65)
    else:
        print(f"Emoção '{termo}' não encontrada diretamente no banco rápido.")
        print(f"Emoções disponíveis: {', '.join(THESAURUS_EMOCOES.keys())}")

def consultar_dicionario_api(palavra: str):
    """Consulta segura à API pública do Dicio / Dicionário Aberto (PT-BR)"""
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
                    clean_def = re.sub(r"<[^>]+>", " ", xml_entry).strip()
                    clean_def = re.sub(r"\s+", " ", clean_def)
                    print(f"\n📖 DICIONÁRIO ABERTO (PT-BR): '{palavra}'")
                    print("=" * 60)
                    print(clean_def[:600] + ("..." if len(clean_def) > 600 else ""))
                    return
        print(f"Nenhuma definição encontrada na API pública para '{palavra}'.")
    except Exception as e:
        print(f"Consulta remota indisponível ou palavra não encontrada ({e}).")

def main():
    parser = argparse.ArgumentParser(description="Consulta Léxica Multilíngue (PT, EN, ES), Regência, Falsos Cognatos e Emoções")
    parser.add_argument("termo", nargs="?", help="Palavra, termo, verbo ou emoção a consultar")
    parser.add_argument("--en", action="store_true", help="Consultar dicionário de Inglês")
    parser.add_argument("--es", action="store_true", help="Consultar dicionário de Espanhol")
    parser.add_argument("--cognato", "-c", action="store_true", help="Verificar se é falso cognato (EN/ES ➔ PT)")
    parser.add_argument("--regencia", "-r", action="store_true", help="Focar em regência verbal")
    parser.add_argument("--acordo", "-a", action="store_true", help="Checar regra do Novo Acordo Ortográfico")
    parser.add_argument("--emocao", "-e", action="store_true", help="Consultar reações corporais do Emotion Thesaurus")
    parser.add_argument("--online", "-o", action="store_true", help="Buscar definição em dicionário online PT-BR")

    args = parser.parse_args()

    if not args.termo:
        parser.print_help()
        sys.exit(1)

    t = args.termo.lower().strip()
    
    if args.en:
        consultar_falso_cognato(t)
        consultar_dicionario_ingles(t)
    elif args.es:
        consultar_falso_cognato(t)
        consultar_dicionario_espanhol(t)
    elif args.cognato:
        if not consultar_falso_cognato(t):
            print(f"Termo '{t}' não catalogado nos falsos amigos críticos rápidos.")
    elif args.emocao:
        consultar_emocao(t)
    elif args.regencia:
        consultar_regencia(t)
    elif args.acordo:
        consultar_acordo(t)
    elif args.online:
        consultar_dicionario_api(t)
    else:
        # Modo inteligente de resolução
        # 1. Checa se é falso cognato
        if consultar_falso_cognato(t):
            return
        # 2. Checa se é emoção
        matched_emocao = False
        for k, v in THESAURUS_EMOCOES.items():
            if k == t or t in v["sinonimos"]:
                consultar_emocao(t)
                matched_emocao = True
                break
        if matched_emocao:
            return
        # 3. Checa regência
        if t in REGENCIA_CANONICA:
            consultar_regencia(t)
            return
        # 4. Checa acordo
        if t in ACORDO_ORTOGRAFICO:
            consultar_acordo(t)
            return
        # 5. Fallback dicionário PT-BR
        consultar_dicionario_api(t)

if __name__ == "__main__":
    main()
