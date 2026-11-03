#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
diagramar_e_traduzir_5_paginas.py
Script oficial da skill book-formatter para diagramação e tradução de 5 páginas.
Fidelidade visual absoluta:
- Zero caixas brancas/opacas: streams de texto originais limpos (BT...ET)
- Backgrounds, texturas, pergaminhos e relâmpagos 100% preservados
- Tipografia original autêntica (PopulationZeroBB e Palatino Linotype)
- Alinhamento milimétrico baseado nos vetores e coordenadas originais do livro
- Organização em pastas: fonts/, images/, comparativos/ e traduzidos/
"""

import sys
from pathlib import Path
from PIL import Image
import pymupdf as fitz
import re

# Configuração de encoding para console Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE_DIR = Path(r"D:\tmp\rrppgg\swade\pra traduzir\necessary_evil_invasion_projeto")
FONTS_DIR = BASE_DIR / "fonts"
IMAGES_DIR = BASE_DIR / "images"
COMPARATIVOS_DIR = BASE_DIR / "comparativos"
TRADUZIDOS_DIR = BASE_DIR / "traduzidos"

# Garantir existência dos diretórios
FONTS_DIR.mkdir(parents=True, exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)
COMPARATIVOS_DIR.mkdir(parents=True, exist_ok=True)
TRADUZIDOS_DIR.mkdir(parents=True, exist_ok=True)

INPUT_PDF = Path(r"D:\tmp\rrppgg\swade\pra traduzir\necessary-evil-swade-invasion (Original).pdf")
OUTPUT_PDF = TRADUZIDOS_DIR / "necessary-evil-swade-invasion-5-paginas-traduzido.pdf"
OUTPUT_MD = TRADUZIDOS_DIR / "necessary-evil-swade-invasion-5-paginas-traduzido.md"
OUTPUT_TXT = TRADUZIDOS_DIR / "necessary-evil-swade-invasion-5-paginas-traduzido.txt"

# Fontes limpas
FONT_POP = str(FONTS_DIR / "PopulationZeroBB_clean.otf")
FONT_PALA = r"C:\Windows\Fonts\pala.ttf"
FONT_PALA_BOLD = r"C:\Windows\Fonts\palab.ttf"
FONT_PALA_IT = r"C:\Windows\Fonts\palai.ttf"

BRAIN_DIR = Path(r"C:\Users\SkyTeamPOA-CharlesCo\.gemini\antigravity\brain\d4f7539e-bad3-4122-8492-3dd4dca9fcc0")


def clean_pdf_stream_text(doc, pno, keep_filter=None):
    """Remove blocos BT...ET de texto diretamente do content stream do PDF."""
    page = doc[pno]
    cxrefs = page.get_contents()
    for cx in cxrefs:
        stream = doc.xref_stream(cx)
        if keep_filter:
            clean = re.sub(rb"BT\s.*?\sET", keep_filter, stream, flags=re.DOTALL)
        else:
            clean = re.sub(rb"BT\s.*?\sET", b"", stream, flags=re.DOTALL)
        doc.update_stream(cx, clean)


def draw_pop_zero(page, pos, text, fontsize=60.0):
    """Renderiza título em PopulationZeroBB com duplo passe (stroke preto + fill branco)."""
    x, y = pos
    page.insert_text((x, y), text, fontname="PopZero", fontfile=FONT_POP, fontsize=fontsize, render_mode=1, color=(0, 0, 0))
    page.insert_text((x, y), text, fontname="PopZero", fontfile=FONT_POP, fontsize=fontsize, render_mode=0, color=(1, 1, 1))


def build_translation():
    print(f"📖 Lendo PDF de Origem: {INPUT_PDF.name}")
    src_doc = fitz.open(str(INPUT_PDF))
    out_doc = fitz.open()

    # Copiar o lote exato de 5 páginas
    for pno in range(5):
        out_doc.insert_pdf(src_doc, from_page=pno, to_page=pno)

    print("⚡ Limpando streams de texto originais (sem desenhar caixas opacas)...")

    # -------------------------------------------------------------
    # PÁGINA 1: Capa (Preservação 100% da arte)
    # -------------------------------------------------------------
    print("  -> Página 1: Capa Original Preservada 100%")

    # -------------------------------------------------------------
    # PÁGINA 2: Folha de Guarda
    # -------------------------------------------------------------
    print("  -> Página 2: Folha de Guarda em Palatino Italic")
    clean_pdf_stream_text(out_doc, 1)
    out_doc[1].insert_text(
        (105.0, 325.0),
        "Esta pagina foi inserida para facilitar a impressao frente e verso.",
        fontname="PalatinoIt",
        fontfile=FONT_PALA_IT,
        fontsize=10.0,
        color=(0.4, 0.4, 0.4)
    )

    # -------------------------------------------------------------
    # PÁGINA 3: Créditos
    # -------------------------------------------------------------
    print("  -> Página 3: Créditos com Palatino Linotype original")
    # Manter INVASION, logos e disclaimer inferior do PEG
    def keep_p3_filter(m):
        bt = m.group(0)
        if b"Clint Black" in bt or b"493.5807" in bt:
            return b""
        return bt

    clean_pdf_stream_text(out_doc, 2, keep_filter=keep_p3_filter)

    p3_creditos = [
        (115.0, 230.0, "Autoria: Clint Black, Shane Lacy Hensley e Scott Pyle"),
        (135.0, 242.0, "Atualizacoes para SWADE: Clint Black e Darrell Hayhurst"),
        (48.0, 256.0, "Ilustracoes Internas: Bad Moon Studio, Storn Cook, David Corsi, James Denton, Robin Elliott,"),
        (55.0, 268.0, "Bien Flores, Gil Formosa, Allen Geneta, Ani Ghosh, Jason Juta, Saga Mackenzie, Aaron J Riley,"),
        (50.0, 280.0, "Martin Sickree, Vincenzo Siriani, Unique Soparie, Dimitar Spasov, Talisman Studios, Cheyenne Wright"),
        (145.0, 294.0, "Capa: Bad Moon Studio | Edicao Adicional: Piotr Korys,"),
        (110.0, 306.0, "Randy Mosiondz, Shane Lacy Hensley, Zeke Sparkes, Chris Toh e Matt Cutter"),
        (80.0, 320.0, "Heroismo de Ultima Hora: Dave Blewer, Butch Curry, Joel Kinstle, Dennis Mohr, Brent Wolke"),
        (75.0, 334.0, "Marketing e Logistica: Jodi Black, Chris Landauer e Christine Lapp | Producao: Darrell Hayhurst, Simon Lucas"),
        (55.0, 375.0, "Dedicatoria de Clint: Aos meus pais, que me ensinaram a amar. Ao meu irmao Gary, que me ensinou a"),
        (50.0, 387.0, "compartilhar o que voce ama. A Kay Reid, que me ensinou que eu amo escrever. A Trinity e Bethany, a quem"),
        (130.0, 399.0, "amo incondicionalmente. E a minha Musa, agora e para sempre."),
        (65.0, 420.0, "Dedicatoria de Shane: A minha prima Liz, que lutou contra o mal verdadeiro. Voce faz muita falta."),
        (110.0, 432.0, "O mundo ficou muito mais escuro sem o seu sorriso caloroso constante."),
        (45.0, 455.0, "Testadores: Ben Ansaldo, Adam Black, Jodi Black, Mark Francis, Sharon Francis, Marguerite Frey, Zachary Kennedy,"),
        (100.0, 467.0, "Frank Chrisley, Rich Miller, Kyle Gallagher, Skipper Beale, Christopher Landauer."),
    ]
    for x, y, txt in p3_creditos:
        font = FONT_PALA_IT if "Dedicatoria" in txt or y > 360 else FONT_PALA
        out_doc[2].insert_text((x, y), txt, fontname="Palatino", fontfile=font, fontsize=8.5, color=(0, 0, 0))

    # -------------------------------------------------------------
    # PÁGINA 4: Sumário (TABLE OF CONTENTS)
    # -------------------------------------------------------------
    print("  -> Página 4: Sumário completo em PopulationZeroBB e Palatino")
    clean_pdf_stream_text(out_doc, 3)

    # Título SUMARIO em PopZero duplo
    draw_pop_zero(out_doc[3], (150.0, 84.3), "SUMARIO", fontsize=60.0)

    toc_items = [
        # Coluna 1
        ("PopZero", 13.0, 36.0, 117.9, "CAPITULO UM: UM MAL NECESSARIO ............................ 3"),
        ("Pala", 10.0, 46.0, 129.9, "Omega . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5"),
        ("Pala", 10.0, 46.0, 141.9, "Star City . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5"),
        ("PopZero", 13.0, 36.0, 162.0, "CAPITULO DOIS: CRIANDO VILOES .............................. 13"),
        ("Pala", 10.0, 46.0, 174.0, "Ancestralidades Necessarias . . . . . . . . . . . . . . . . . . . . . . . . . . 14"),
        ("Pala", 10.0, 46.0, 186.0, "Complicacoes Alteradas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15"),
        ("Pala", 10.0, 46.0, 198.0, "Novas Complicacoes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15"),
        ("Pala", 10.0, 46.0, 210.0, "Regras de Cenario . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15"),
        ("PopZero", 16.0, 36.0, 233.7, "SECAO DO MESTRE"),
        ("PopZero", 13.0, 36.0, 253.8, "CAPITULO TRES: UM MUNDO DE MALDADE ................... 18"),
        ("Pala", 10.0, 46.0, 265.8, "O Inicio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18"),
        ("Pala", 10.0, 46.0, 277.8, "Os V’sori . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19"),
        ("Pala", 10.0, 46.0, 289.8, "Por Tras da Mascara . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21"),
        ("Pala", 10.0, 46.0, 301.8, "Atlantida . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21"),
        ("PopZero", 13.0, 36.0, 321.9, "CAPITULO QUATRO: SEGREDOS DE STAR CITY .............. 24"),
        ("Pala", 10.0, 46.0, 333.9, "Guia Geografico de Star City . . . . . . . . . . . . . . . . . . . . . . . . . . 25"),
        ("PopZero", 13.0, 36.0, 354.0, "CAPITULO CINCO: AVENTURAS .................................... 38"),
        ("Pala", 10.0, 46.0, 366.0, "Gerador de Aventuras . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38"),
        ("Pala", 10.0, 46.0, 378.0, "Resumo dos Pontos de Enredo . . . . . . . . . . . . . . . . . . . . . . . . 38"),
        ("Pala", 10.0, 46.0, 390.0, "Episodio 1: Fuga da Prisao! . . . . . . . . . . . . . . . . . . . . . . . . . . . 43"),
        ("Pala", 10.0, 46.0, 402.0, "Episodio 2: Os Irregulares Subterraneos . . . . . . . . . . . . . . . . . 46"),
        ("Pala", 10.0, 46.0, 414.0, "Episodio 3: A Primeira Familia . . . . . . . . . . . . . . . . . . . . . . . . 49"),
        ("Pala", 10.0, 46.0, 426.0, "Episodio 4: O Enforcado . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51"),
        ("Pala", 10.0, 46.0, 438.0, "Episodio 5: Mesticos . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53"),
        ("Pala", 10.0, 46.0, 450.0, "Episodio 6: Saqueadores do Templo Perdido . . . . . . . . . . . . . . 55"),
        ("Pala", 10.0, 46.0, 462.0, "Episodio 7: Vira-Casaca . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57"),
        ("Pala", 10.0, 46.0, 474.0, "Episodio 8: Assalto ao Satelite 15! . . . . . . . . . . . . . . . . . . . . . 59"),
        ("Pala", 10.0, 46.0, 486.0, "Episodio 9: Um Vilao os Liderara! . . . . . . . . . . . . . . . . . . . . . . 61"),
        ("Pala", 10.0, 46.0, 498.0, "Episodio 10: Retorno do Forasteiro . . . . . . . . . . . . . . . . . . . . . 63"),
        ("Pala", 10.0, 46.0, 510.0, "Episodio 11: A Contingencia Omega! . . . . . . . . . . . . . . . . . . . . 66"),
        ("PopZero", 13.0, 36.0, 530.1, "CAPITULO SEIS: CONTOS SELVAGENS ........................... 68"),
        ("Pala", 10.0, 46.0, 542.1, "Culto dos Deuses Espaciais . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68"),
        ("Pala", 10.0, 46.0, 554.1, "Cuidado com o Adormecido . . . . . . . . . . . . . . . . . . . . . . . . . . . 69"),
        # Coluna 2
        ("Pala", 10.0, 254.5, 114.8, "O Retorno do Monolito! . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70"),
        ("Pala", 10.0, 254.5, 126.8, "Problemas na Base Hidro 11 . . . . . . . . . . . . . . . . . . . . . . . . . 72"),
        ("Pala", 10.0, 254.5, 138.8, "Vendetta . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74"),
        ("Pala", 10.0, 254.5, 150.8, "O Legado do Coronel Clone . . . . . . . . . . . . . . . . . . . . . . . . . . 76"),
        ("Pala", 10.0, 254.5, 162.8, "Puxando a Tomada . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78"),
        ("Pala", 10.0, 254.5, 174.8, "Fogo dos Ceus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80"),
        ("Pala", 10.0, 254.5, 186.8, "Culto de Sangue . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 82"),
        ("Pala", 10.0, 254.5, 198.8, "Destruicao Robotica . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85"),
        ("Pala", 10.0, 254.5, 210.8, "Meia-Noite no Jardim do Dr. Devolucao . . . . . . . . . . . . . . . . . 87"),
        ("Pala", 10.0, 254.5, 222.8, "Sangria Alienigena . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89"),
        ("Pala", 10.0, 254.5, 234.8, "Vidas Paralelas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91"),
        ("Pala", 10.0, 254.5, 246.8, "Um Dia na Vida de um Heroi . . . . . . . . . . . . . . . . . . . . . . . . . 92"),
        ("Pala", 10.0, 254.5, 258.8, "A Camara . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 94"),
        ("Pala", 10.0, 254.5, 270.8, "Os Caes de Guerra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97"),
        ("Pala", 10.0, 254.5, 282.8, "O Resgate . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 98"),
        ("Pala", 10.0, 254.5, 294.8, "O Inimigo do Meu Inimigo . . . . . . . . . . . . . . . . . . . . . . . . . . . 99"),
        ("Pala", 10.0, 254.5, 306.8, "Espreitador em Star City . . . . . . . . . . . . . . . . . . . . . . . . . . . 100"),
        ("Pala", 10.0, 254.5, 318.8, "Terror em Tarrytown . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103"),
        ("Pala", 10.0, 254.5, 330.8, "O Retorno de 4-Star e Lucky . . . . . . . . . . . . . . . . . . . . . . . . 105"),
        ("Pala", 10.0, 254.5, 342.8, "O Opositor Alienigena . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 107"),
        ("Pala", 10.0, 254.5, 354.8, "Cacando os Cacadores . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 108"),
        ("Pala", 10.0, 254.5, 366.8, "A Cruz Vermelha . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109"),
        ("Pala", 10.0, 254.5, 378.8, "O Cofre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111"),
        ("PopZero", 13.0, 244.5, 410.9, "CAPITULO SETE: GALERIA DE VILOES ......................... 113"),
        ("Pala", 10.0, 254.5, 422.9, "A Maquina de Guerra V’sori . . . . . . . . . . . . . . . . . . . . . . . . . 113"),
        ("Pala", 10.0, 254.5, 434.9, "O Povo de Star City . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122"),
        ("PopZero", 13.0, 244.5, 455.0, "INDICE REMISSIVO ..................................................... 128"),
    ]

    for ftype, sz, x, y, txt in toc_items:
        if ftype == "PopZero":
            out_doc[3].insert_text((x, y), txt, fontname="PopZero", fontfile=FONT_POP, fontsize=sz, color=(0, 0, 0))
        else:
            out_doc[3].insert_text((x, y), txt, fontname="Palatino", fontfile=FONT_PALA, fontsize=sz, color=(0, 0, 0))

    # -------------------------------------------------------------
    # PÁGINA 5: Capítulo Um (A NECESSARY EVIL)
    # -------------------------------------------------------------
    print("  -> Página 5: Capítulo Um com fidelidade tipográfica absoluta")
    clean_pdf_stream_text(out_doc, 4)

    # Título principal do Capítulo Um em PopZero duplo
    draw_pop_zero(out_doc[4], (115.2, 98.1), "CAPITULO UM: ", fontsize=60.0)
    draw_pop_zero(out_doc[4], (80.1, 158.1), "UM MAL NECESSARIO", fontsize=60.0)

    # Subtítulos em PopZero duplo
    draw_pop_zero(out_doc[4], (84.3, 317.5), "PREPARANDO O CENARIO", fontsize=18.0)
    draw_pop_zero(out_doc[4], (106.1, 614.8), "OS V’SORI", fontsize=18.0)
    draw_pop_zero(out_doc[4], (244.5, 538.3), "TRAICAO", fontsize=16.0)

    # Número da página no rodapé
    out_doc[4].insert_text((442.5, 709.4), "3", fontname="PopZero", fontfile=FONT_POP, fontsize=8.0, color=(0, 0, 0))

    # Linhas de texto correspondendo perfeitamente ao grid original
    p5_lines = [
        # Coluna 1 - Topo
        (36.0, 181.6, "Em Necessary Evil, um bando de alienigenas atraiu os"),
        (36.0, 193.6, "super-herois do mundo para uma armadilha astuta e"),
        (36.0, 205.6, "matou ou aprisionou a vasta maioria deles."),
        (36.0, 217.6, "Os personagens dos jogadores sao os unicos seres"),
        (36.0, 229.6, "aprimorados que restaram para salvar o planeta — superviloes!"),
        (36.0, 241.6, "Como a politica dos novos soberanos alienigenas e matar"),
        (36.0, 253.6, "qualquer um que manifeste poderes paranormais, a"),
        (36.0, 265.6, "unica opcao aberta para tais individuos e lutar ou fugir!"),
        (36.0, 277.6, "Voce pode adivinhar qual opcao a maioria dos viloes"),
        (36.0, 289.6, "escolhe…"),

        # Coluna 1 - Meio
        (36.0, 329.5, "Naturalmente, tudo comecou em 1 de janeiro de 2001."),
        (36.0, 341.5, "As primeiras naves surgiram sobre todas as grandes"),
        (36.0, 353.5, "cidades do planeta. Nao houve preludio e nenhuma"),
        (36.0, 365.5, "exigencia. Os alienigenas simplesmente atacaram. Eles"),
        (36.0, 377.5, "eram uma raca anfibia feroz que combinava os aspectos"),
        (36.0, 389.5, "mais crueis de tubaroes e crocodilos com uma agressao"),
        (36.0, 401.5, "nao superada por nenhuma especie. Eram o verdadeiro"),
        (36.0, 413.5, "pesadelo da humanidade. As pessoas logo os"),
        (36.0, 425.5, "chamavam de Guelras."),
        (40.5, 439.3, "Nova York virou zona de guerra, Toquio foi"),
        (36.0, 451.3, "bombardeada e ate a lendaria Atlantida afundada"),
        (36.0, 463.3, "foi destruida e o seu governante — o soberano"),
        (36.0, 475.3, "Aquariano — foi assassinado."),
        (40.5, 489.1, "Os super-herois da Terra lutaram bravamente e"),
        (36.0, 501.1, "contra-atacaram de imediato. Os guelras eram aterradores,"),
        (36.0, 513.1, "mas ninguem duvidava de que os herois venceriam no"),
        (36.0, 525.1, "final. Afinal, invasores alienigenas ja haviam tentado"),
        (36.0, 537.1, "atacar a Terra tres vezes antes, e os protetores"),
        (36.0, 549.1, "sempre emergiram triunfantes em todas as batalhas."),
        (40.5, 562.9, "Mas os guelras possuiam tecnologia alienigena superior"),
        (36.0, 574.9, "e uma sede de sangue selvagem, causando perdas pesadas."),
        (36.0, 586.9, "A Terra comecou a temer pelo seu destino."),
        (36.0, 626.8, "Entao veio a virada da mare que as pessoas tanto"),
        (36.0, 638.8, "esperavam nessas guerras epicas de super-herois."),
        (36.0, 650.8, "Forcas de vanguarda de uma nova raca surgiram em"),
        (36.0, 662.8, "orbita terrestre — os V’sori. Afirmaram ser aliados"),
        (36.0, 674.8, "ha muito perdidos de Atlantida e defensores da paz"),
        (36.0, 686.8, "que cruzaram galaxias para proteger o nosso mundo."),

        # Coluna 2
        (244.5, 181.6, "em busca de seus companheiros de armas ao longo de"),
        (244.5, 193.6, "seculos. Durante a jornada, tornaram-se guardioes"),
        (244.5, 205.6, "reconhecidos de toda a galaxia."),
        (249.0, 219.4, "Os V’sori declararam que os Guelras — ou k’tharen —"),
        (244.5, 231.4, "eram mercenarios sanguinarios que devastavam mundos,"),
        (244.5, 243.4, "mas que os V’sori ja os haviam combatido no passado"),
        (244.5, 255.4, "e ajudariam a Terra a derrota-los de uma vez por todas."),
        (249.0, 281.2, "O maior heroi do planeta, o Campeao da Forca Alfa,"),
        (244.5, 293.2, "voou ao espaco para recebe-los. Retornou com um apelo"),
        (244.5, 305.2, "emocionado convocando a humanidade a resistir com"),
        (244.5, 317.2, "coragem mais um pouco. O povo resistiu, com extremo"),
        (244.5, 329.2, "sacrificio em sangue e determinacao heroica."),
        (249.0, 355.0, "Quando a frota V’sori chegou em massa, a armada"),
        (244.5, 367.0, "k’tharen levantou voo. As naves travaram um duelo"),
        (244.5, 379.0, "titanico nos ceus, e os V’sori sairam vitoriosos,"),
        (244.5, 391.0, "transmitindo para o planeta as imagens dos guelras"),
        (244.5, 403.0, "em fuga desesperada atraves do espaco profundo."),
        (249.0, 416.8, "A humanidade celebrou seus salvadores e recebeu"),
        (244.5, 428.8, "os nobres protetores alienigenas de bracos abertos."),
        (244.5, 440.8, "Jovens dancavam nas ruas, celebrando uma nova era"),
        (244.5, 452.8, "de paz universal e fraternidade. Os poucos jornalistas"),
        (244.5, 464.8, "e analistas ceticos foram vaiados e censurados."),
        (244.5, 476.8, "Governos fragilizados chegaram a entregar as chaves"),
        (244.5, 488.8, "simbolicas de suas proprias capitais aos novos aliados."),
        (244.5, 550.3, "E claro que era exatamente isso o que os alienigenas"),
        (244.5, 562.3, "planejaram desde o inicio. Em todas as metropoles,"),
        (244.5, 574.3, "herois e lideres mundiais se uniram para saudar os"),
        (244.5, 586.3, "visitantes estelares. Multidoes aplaudiam quando as"),
        (244.5, 598.3, "naves V’sori pairavam imponentes no horizonte."),
        (244.5, 610.3, "Super-herois, ajudantes, presidentes e astros da midia"),
        (244.5, 622.3, "compareceram em massa a essas cerimonias gloriosas."),
        (244.5, 634.3, "O povo da Terra aplaudia em lagrimas assistindo aos"),
        (244.5, 646.3, "seus maiores icones saudando os novos salvadores."),
        (249.0, 672.1, "Os aplausos viraram gritos de pavor e horror quando as"),
        (244.5, 684.1, "naves V’sori abriram fogo sobre todos os reunidos…"),
    ]

    for x, y, txt in p5_lines:
        out_doc[4].insert_text((x, y), txt, fontname="Palatino", fontfile=FONT_PALA, fontsize=10.0, color=(0, 0, 0))

    # Salvar PDF em traduzidos/
    out_doc.save(str(OUTPUT_PDF), garbage=4, deflate=True)
    print(f"\n🎉 PDF traduzido salvo em: {OUTPUT_PDF}")

    # Gerar comparativos lado a lado para as 5 páginas
    for pno in range(5):
        orig_img_path = IMAGES_DIR / f"pagina_original_{pno+1}.jpg"
        pix_orig = src_doc[pno].get_pixmap(dpi=150)
        pix_orig.save(orig_img_path)

        trans_img_path = IMAGES_DIR / f"pagina_traduzida_{pno+1}.jpg"
        pix_trans = out_doc[pno].get_pixmap(dpi=150)
        pix_trans.save(trans_img_path)

        im_o = Image.open(orig_img_path)
        im_t = Image.open(trans_path_img := trans_img_path)

        w = im_o.width + im_t.width
        h = max(im_o.height, im_t.height)
        comp = Image.new("RGB", (w, h), (255, 255, 255))
        comp.paste(im_o, (0, 0))
        comp.paste(im_t, (im_o.width, 0))

        comp_path = COMPARATIVOS_DIR / f"comparativo_lado_a_lado_pagina_{pno+1}.jpg"
        comp.save(comp_path, quality=92)

        # Copiar para o diretório de artefatos do chat
        brain_path = BRAIN_DIR / f"comparativo_lado_a_lado_pagina_{pno+1}.jpg"
        comp.save(brain_path, quality=92)
        print(f"  -> Comparativo lado a lado gerado: {comp_path.name}")

    # Gerar Markdown em traduzidos/
    md_content = """# NECESSARY EVIL: INVASÃO (SWADE)
## Edição em Português Brasileiro — Lote de Teste (5 Primeiras Páginas)
> **Fonte Original:** `necessary-evil-swade-invasion (Original).pdf`  
> **Sistema:** Savage Worlds Edição Aventura (SWADE)  
> **Traduzido e Diagramado por:** Book Formatter (AI Skill)  

---

## 📄 Página 1: Capa
**NECESSARY EVIL: INVASÃO**  
*Um Cenário de Supervilões para Savage Worlds Edição Aventura*  
Pinnacle Entertainment Group (PEG)  

---

## 📄 Página 2: Folha de Guarda
*Esta página foi inserida propositalmente para facilitar a impressão frente e verso.*

---

## 📄 Página 3: Créditos e Dedicatórias

**NECESSARY EVIL: INVASÃO**

- **Autoria:** Clint Black, Shane Lacy Hensley e Scott Pyle  
- **Atualizações para SWADE:** Clint Black e Darrell Hayhurst  
- **Ilustrações Internas:** Bad Moon Studio, Storn Cook, David Corsi, James Denton, Robin Elliott, Bien Flores, Gil Formosa, Allen Geneta, Ani Ghosh, Jason Juta, Saga Mackenzie, Aaron J Riley, Martin Sickree, Vincenzo Siriani, Unique Soparie, Dimitar Spasov, Talisman Studios, Cheyenne Wright  
- **Capa:** Bad Moon Studio  
- **Material Adicional e Edição:** Piotr Korys, Randy Mosiondz, Shane Lacy Hensley, Zeke Sparkes, Chris Toh e Matt Cutter  
- **Heroísmo de Última Hora:** Dave Blewer, Butch Curry, Joel Kinstle, Dennis Mohr, Brent Wolke  
- **Marketing e Logística:** Jodi Black, Chris Landauer e Christine Lapp  
- **Produção:** Darrell Hayhurst, Simon Lucas, Jessica Rogers e Donald Schepis  

---

## 📄 Página 4: Sumário (Table of Contents)

**SUMÁRIO**

### Coluna 1
- **CAPÍTULO UM: UM MAL NECESSÁRIO** — 3
  - Ômega — 5
  - Star City — 5
- **CAPÍTULO DOIS: CRIANDO VILÕES** — 13
  - Ancestralidades Necessárias — 14
  - Complicações Alteradas — 15
  - Novas Complicações — 15
  - Regras de Cenário — 15
- **SEÇÃO DO MESTRE**
- **CAPÍTULO TRÊS: UM MUNDO DE MALDADE** — 18
  - O Início — 18
  - Os V’sori — 19
  - Por Trás da Máscara — 21
  - Atlântida — 21
- **CAPÍTULO QUATRO: SEGREDOS DE STAR CITY** — 24
  - Guia Geográfico de Star City — 25
- **CAPÍTULO CINCO: AVENTURAS** — 38
  - Gerador de Aventuras — 38
  - Resumo dos Pontos de Enredo — 38
  - Episódio 1: Fuga da Prisão! — 43
  - Episódio 2: Os Irregulares Subterrâneos — 46
  - Episódio 3: A Primeira Família — 49
  - Episódio 4: O Enforcado — 51
  - Episódio 5: Mestiços — 53
  - Episódio 6: Saqueadores do Templo Perdido — 55
  - Episódio 7: Vira-Casaca — 57
  - Episódio 8: Assalto ao Satélite 15! — 59
  - Episódio 9: Um Vilão os Liderará! — 61
  - Episódio 10: Retorno do Forasteiro — 63
  - Episódio 11: A Contingência Ômega! — 66
- **CAPÍTULO SEIS: CONTOS SELVAGENS** — 68
  - Culto dos Deuses Espaciais — 68
  - Cuidado com o Adormecido — 69

### Coluna 2
- O Retorno do Monólito! — 70
- Problemas na Base Hidro 11 — 72
- Vendetta — 74
- O Legado do Coronel Clone — 76
- Puxando a Tomada — 78
- Fogo dos Céus — 80
- Culto de Sangue — 82
- Destruição Robótica — 85
- Meia-Noite no Jardim do Dr. Devolução — 87
- Sangria Alienígena — 89
- Vidas Paralelas — 91
- Um Dia na Vida de um Herói — 92
- A Câmara — 94
- Os Cães de Guerra — 97
- O Resgate — 98
- O Inimigo do Meu Inimigo — 99
- Espreitador em Star City — 100
- Terror em Tarrytown — 103
- O Retorno de 4-Star e Lucky — 105
- O Opositor Alienígena — 107
- Caçando os Caçadores — 108
- A Cruz Vermelha — 109
- O Cofre — 111
- **CAPÍTULO SETE: GALERIA DE VILÕES** — 113
  - A Máquina de Guerra V’sori — 113
  - O Povo de Star City — 122
- **ÍNDICE REMISSIVO** — 128

---

## 📄 Página 5: Capítulo Um — Um Mal Necessário

### Banner Superior
**CAPÍTULO UM: UM MAL NECESSÁRIO**

### Coluna 1
Em *Necessary Evil*, um bando de alienígenas atraiu os super-heróis do mundo para uma armadilha astuta e matou ou aprisionou a vasta maioria deles. Os personagens dos jogadores são os únicos seres aprimorados que restaram para salvar o planeta — supervilões!

Como a política dos novos soberanos alienígenas é matar qualquer um que manifeste poderes paranormais, a única opção aberta para tais indivíduos é lutar ou fugir! Você pode adivinhar qual opção a maioria dos vilões escolhe…

#### PREPARANDO O CENÁRIO
Naturalmente, tudo começou em 1º de janeiro de 2001. As primeiras naves surgiram sobre todas as grandes cidades do planeta. Não houve prelúdio e nenhuma exigência. Os alienígenas simplesmente atacaram. Eles eram uma raça anfíbia feroz que combinava os aspectos mais cruéis de tubarões e crocodilos com uma agressão não superada por nenhuma espécie. Eram o verdadeiro pesadelo da humanidade. As pessoas logo os chamavam de "Guelras".

Nova York virou zona de guerra, Tóquio foi bombardeada e até a lendária Atlântida afundada foi destruída e o seu governante — o soberano Aquariano — foi assassinado.

Os super-heróis da Terra lutaram bravamente e contra-atacaram de imediato. Os guelras eram aterradores, mas ninguém duvidava de que os heróis venceriam no final. Afinal, invasores alienígenas já haviam tentado atacar a Terra três vezes antes, e os protetores sempre emergiram triunfantes em todas as batalhas.

Mas os guelras possuíam tecnologia alienígena superior e uma sede de sangue selvagem, causando perdas pesadas. A Terra começou a temer pelo seu destino.

#### OS V’SORI
Então veio a virada da maré que as pessoas tanto esperavam nessas guerras épicas de super-heróis. Forças de vanguarda de uma nova raça surgiram em órbita terrestre — os V’sori. Afirmaram ser aliados há muito perdidos de Atlântida e defensores da paz que cruzaram galáxias para proteger o nosso mundo.

### Coluna 2
...em busca de seus companheiros de armas ao longo de séculos. Durante a jornada, tornaram-se guardiões reconhecidos de toda a galáxia.

Os V’sori declararam que os Guelras — ou k’tharen — eram mercenários sanguinários que devastavam mundos, mas que os V’sori já os haviam combatido no passado e ajudariam a Terra a derrotá-los de uma vez por todas.

O maior herói do planeta, o Campeão da Força Alfa, voou ao espaço para recebê-los. Retornou com um apelo emocionado convocando a humanidade a resistir com coragem mais um pouco. O povo resistiu, com extremo sacrifício em sangue e determinação heroica.

Quando a frota V’sori chegou em massa, a armada k’tharen levantou voo. As naves travaram um duelo titânico nos céus, e os V’sori saíram vitoriosos, transmitindo para o planeta as imagens dos guelras em fuga desesperada através do espaço profundo.

A humanidade celebrou seus salvadores e recebeu os nobres protetores alienígenas de braços abertos. Jovens dançavam nas ruas, celebrando uma nova era de paz universal e fraternidade. Os poucos jornalistas e analistas céticos foram vaiados e censurados. Governos fragilizados chegaram a entregar as chaves simbólicas de suas próprias capitais aos novos aliados.

#### TRAIÇÃO
É claro que era exatamente isso o que os alienígenas planejaram desde o início. Em todas as metrópoles, heróis e líderes mundiais se uniram para saudar os visitantes estelares. Multidões aplaudiam quando as naves V’sori pairavam imponentes no horizonte. Super-heróis, ajudantes, presidentes e astros da mídia compareceram em massa a essas cerimônias gloriosas. O povo da Terra aplaudia em lágrimas assistindo aos seus maiores ícones saudando os novos salvadores.

Os aplausos viraram gritos de pavor e horror quando as naves V’sori abriram fogo sobre todos os reunidos…
"""
    OUTPUT_MD.write_text(md_content, encoding="utf-8")
    OUTPUT_TXT.write_text(md_content, encoding="utf-8")
    print(f"📄 Arquivos Markdown e TXT salvos em: {TRADUZIDOS_DIR}")


if __name__ == "__main__":
    build_translation()
