# Book Formatter / Diagramador de Livros 📕➡️📄

> **Book Formatting & RPG Book Diagramming**  
> *Formatação de Livros e Diagramação de Livros de RPG*

---

## 🇺🇸 English

### 📌 Overview

**Book Formatter** is an AI agent toolchain designed to install any required document-reading tools and to format/diagram books, delivering:

- A **TXT** file with the texts,
- A **Markdown** file,
- A **PDF** duly diagramed/formatted.

Its core use case is **RPG books** — especially old materials from the **World of Darkness** (e.g., *Vampire: The Masquerade*) — where the final goal is a Portuguese translation with the diagramming/layout of the original as faithful as possible (same images, columns, fonts, titles, indents, paragraphs and page count).

The methodology follows a strict pipeline: **Analyze → Extract → Translate → Review → Diagram → Audit**, using a paid AI that can work directly with files and produce DOCX and PDF.

### 🔄 The 8 Workflow Phases

1. **FAÇA A IA ANALISAR O PDF ORIGINAL** — technical report on pages, margins, columns, spacing, indents, alignments, headers/footers, images, ornaments, borders, fonts.
2. **DESCUBRA E UTILIZE AS FONTES CORRETAS** — identify fonts, sizes and variations; handle unavailable fonts.
3. **EXTRAIA O TEXTO ANTES DE TRADUZIR** — extract text respecting column reading order, paragraphs, lists, tables, character sheets; generate editable DOCX.
4. **ENSENE A IA SOBRE O VOCABULÁRIO DO RPG** — bilingual glossary, consistent terminology, alternatives on divergences.
5. **TRADUZA EM PEQUENOS LOTES** — ~10–20 pages or one chapter per batch; preserve everything; no summaries/adaptations.
6. **VERIFIQUE A TRADUÇÃO ANTES DE DIAGRAMAR** — page-by-page, paragraph-by-paragraph comparison; report what was checked/corrected.
7. **AGORA SIM, COMECE A DIAGRAMAÇÃO!** — use original PDF as absolute layout reference and translated DOCX as content source; reproduce layout faithfully; work in small batches (5–10 test pages first).
8. **EXIJA UMA AUDITORIA FINAL** — visual and structural comparison per page; correct problems before delivering.

### 🧰 Installation

```bash
python scripts/check_env.py
pip install markitdown markitdown-ocr pdfminer.six pdfplumber pypdf pypdfium2 Pillow pytesseract \
            python-docx mammoth openpyxl pandas xlrd odfpy ebooklib beautifulsoup4 html2text striprtf

# Motores SOTA de IA para PDFs complexos de RPG:
pip install docling marker-pdf unstructured nougat-ocr
```

### 🧠 Motores Avançados de Layout & Utilitários (Docling, Marker, Stirling-PDF, Nougat)
Para livros de RPG com diagramações densas (colunas múltiplas, tabelas de monstros/magias e caixas laterais), a skill integra:
- **Docling (IBM/DS4SD):** Análise multimodal de layout e reconstrução de tabelas com `TableFormer`.
- **Marker (Datalab):** Extração ultrarrápida para Markdown preservando fórmulas e cabeçalhos.
- **Unstructured:** Particionamento inteligente de documentos para tradução em lotes.
- **Nougat (Meta AI):** OCR neural visual-to-text para scans antigos e fontes góticas.
- **Stirling-PDF:** Canivete suíço para dividir capítulos, extrair imagens em alta resolução e reparar PDFs.
- **Nano-PDF & PDFtoGPT:** Edição cirúrgica preservando background e auditoria RAG anti-alucinação.

### 🛠️ Usage

```bash
# Check environment & update dependencies
python scripts/check_env.py
python scripts/check_env.py --upgrade

# Check for skill updates (and optionally auto-upgrade via Git)
python scripts/check_update.py
python scripts/check_update.py --upgrade

# Convert document to TXT / Markdown
python scripts/convert_to_txt_md.py "caminho/do/documento.pdf" "saida"

# Segment rulebook into atomic rules for AI, RAG & MCP
python scripts/export_rules_for_ai.py "caminho/do/livro_traduzido.md" "saida_rag" "nome_sistema"
```

### 🧠 Segmentação de Regras para IA, RAG e MCP
A skill gera automaticamente:
- `<sistema>_rag_chunks.jsonl` com metadados para bancos vetoriais (ChromaDB, Pinecone, FAISS).
- `<sistema>_training_dataset.jsonl` para fine-tuning de modelos LLM.
- `categories/<topico>.md` para servir regras modulares sob demanda via Servidores MCP.

### 📖 Aprendizado Contínuo & Criação Automática de Glossários
Sempre que um livro de RPG for processado:
1. O agente compila termos de regras, magias, atributos e cenários.
2. Salva em memória e no diretório `glossarys/glossary-<sistema>.md`.
3. A comunicação ao usuário e o envio da contribuição ao desenvolvedor são **formalizados obrigatoriamente via GitHub Issue** (`gh issue create --repo CharlesCorreaDev/skills-ai`).

### 🔄 Monitor de Versão e Manutenção de Dependências
- `python scripts/check_update.py --upgrade`: atualiza a skill e glossários para a versão mais recente do GitHub.
- `python scripts/check_env.py --upgrade`: mantém todos os pacotes Python de IA e PDF na última versão estável.

### 📖 RPG & Gamers Glossary

The skill includes the **RPG & Gamers Glossary** (`glossarys/glossary.md`) with terms from community sources, used during the **Translate** phase for consistent terminology (clans, Disciplines, Attributes, Abilities, Backgrounds, Virtues, powers).

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral

O **Book Formatter** (Diagramador de Livros) é uma suíte de ferramentas para Agentes de IA que instala qualquer ferramenta necessária para leitura de documentos (PDF com ou sem OCR, TXT, DOCX, DOC, CSV/TSV, XLSX/XLS, HTML, EPUB, imagens com OCR) e executa a diagramação de livros, entregando:

- Um arquivo **`.txt`** com os textos,
- Um arquivo **`.md`** (Markdown),
- Um **`.pdf`** devidamente diagramado/formatado.

O caso de uso principal é **livros de RPG** — especialmente materiais antigos do **Mundo das Trevas** (ex.: *Vampiro: A Idade das Trevas*) — onde o objetivo final é uma tradução em português com a diagramação do original o mais fiel possível.

### 🎯 Protocolo Obrigatório Pré-Execução: Code Mode, Grill-Me & Karpathy
Antes de qualquer alteração, extração ou diagramação:
1. **Instalação Obrigatória das Skills:** Instalar e usar `grill-me` (interrogação e alinhamento do autor) e `andrej-karpathy-skills` (engenharia limpa e sem suposições).
   ```bash
   npx skills@latest add mattpocock/skills --skill=grill-me
   npx skills@latest add multica-ai/andrej-karpathy-skills
   ```
2. **Entrevista Obrigatória com Grill-Me:** Interrogar o autor sobre sistema de RPG, lote inicial de teste (5-10 páginas), termos consagrados e fontes.
3. **Protocolo Andrej Karpathy:** Não assumir nada, mudanças cirúrgicas, manter o código mínimo e simples, definir metas e verificar.
4. **Code Mode & Etapas:** Executar toda tarefa em Code Mode por etapas determinísticas, nunca em um único passo cego.

### 📜 Regras Rigorosas do Tradutor & Diagramador de RPG
A skill segue 5 mandamentos obrigatórios de tradução e diagramação profissional de RPG:
1. **Fidelidade Integral:** Tradução completa de 100% dos textos; proibido resumir, simplificar, omitir ou inventar dados.
2. **Preservação da Página Original:** A página original serve como base direta. Não recriar páginas do zero; ilustrações, bordas, molduras e ornamentos permanecem intactos.
3. **Inviolabilidade Numérica de Regras:** Fórmulas de dados (`1d8`), modificadores (`+2`), requisitos, ações e CDs são intocáveis.
4. **Controle de Qualidade Pré-Entrega:** Checklist visual e estrutural parágrafo por parágrafo contra o original.
5. **Formato de Entrega Fiel:** Entrega de páginas preservando dimensões, proporção e arte original.

### 🔄 Os 8 Fluxos de Trabalho

1. **FAÇA A IA ANALISAR O PDF ORIGINAL**
2. **DESCUBRA E UTILIZE AS FONTES CORRETAS**
3. **EXTRAIA O TEXTO ANTES DE TRADUZIR**
4. **ENSENE A IA SOBRE O VOCABULÁRIO DO RPG**
5. **TRADUZA EM PEQUENOS LOTES**
6. **VERIFIQUE A TRADUÇÃO ANTES DE DIAGRAMAR**
7. **AGORA SIM, COMECE A DIAGRAMAÇÃO!**
8. **EXIJA UMA AUDITORIA FINAL**

### 📖 Dicionário de RPG e Gamers

A skill conta com o **Dicionário de Termos de RPG e Gamers** (`glossarys/glossary.md`), alimentado pelas fontes indicadas, utilizado na fase de **Tradução** para manter a consistência terminológica.

---

## 📁 Structure

- [SKILL.md](SKILL.md) — Main skill definition, workflows, protocols.
- [README.md](README.md) — This file.
- [cheatsheet.md](cheatsheet.md) — Quick reference of formats, commands and phase prompts.
- [glossarys/glossary.md](glossarys/glossary.md) — RPG & Gamers terminology dictionary.
- [glossarys/glossary-scifi.md](glossarys/glossary-scifi.md) — Science Fiction, Cyberpunk, Space Opera, Military Sci-Fi & Psionics terminology dictionary.
- [glossarys/glossary-horror.md](glossarys/glossary-horror.md) — Cosmic Horror, Lovecraftian Mythos, Survival Horror & Gothic Horror terminology dictionary.
- [glossarys/glossary-savage-worlds.md](glossarys/glossary-savage-worlds.md) — Savage Worlds Adventure Edition (SWADE) terminology dictionary.
- [glossarys/glossary-year-zero.md](glossarys/glossary-year-zero.md) — Year Zero Engine (YZE) terminology dictionary.
- [glossarys/glossary-world-of-darkness.md](glossarys/glossary-world-of-darkness.md) — World of Darkness / Mundo das Trevas (all franchises) terminology dictionary.
- [glossarys/glossary-pathfinder-2e.md](glossarys/glossary-pathfinder-2e.md) — Pathfinder 2nd Edition / PF2e terminology dictionary.
- [VERSION](VERSION) — Semantic version.
- [CHANGELOG.md](CHANGELOG.md) — Release history.
- [scripts/](scripts/) — Environment checker and TXT/Markdown converter.
