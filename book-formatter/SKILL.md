---
name: book-formatter
description: Book formatting and RPG book diagramming suite for AI agents. Installs any required document-reading toolchain (PDF with or without OCR, TXT, DOCX, DOC, CSV/TSV, XLSX/XLS, HTML, EPUB, images OCR) and orchestrates book diagramming delivering a TXT with the texts, a Markdown and a duly diagrammed PDF preserving the original layout. Built for paid AI workflows (ChatGPT + Adobe WORK plugin) to analyze, extract, translate in small batches, review and diagram RPG books (World of Darkness, Vampire: The Masquerade) with faithful typography, columns, margins, fonts, images, borders and ornaments. Use when the user wants to format, translate or diagram an RPG book into Portuguese via AI with TXT, Markdown and PDF deliverables via Antigravity, Claude Code, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA, or Ollama.
---

# Book Formatter / Diagramador de Livros 📕➡️📄
> *by GM Charles Corrêa* • **Suíte Multiagente de Diagramação de Livros & RPG (v0.8.0-beta)**

---

## 🏛️ Topologia dos 8 Subagentes Especializados

Para erradicar omissões e garantir fidelidade tipográfica e visual idêntica ao original, a suíte opera em pipeline federado:

`mermaid
flowchart TD
    User([Usuário / Autor / GM]) --> Showrunner[1. Orquestrador de Diagramação]
    Showrunner --> Extractor[2. Engenheiro de Ingestão & PDF Oxide]
    Extractor --> Typographer[3. Analista Tipográfico & Fontes]
    Typographer --> RpgAnalyst[4. Especialista em Regras & Glossário RPG]
    RpgAnalyst --> BatchTranslator[5. Tradutor em Lotes de 5 Páginas]
    BatchTranslator --> Reviewer[6. Revisor Semântico & Mecânico]
    Reviewer --> Diagrammer[7. Diagramador & Compositor de PDF/MD]
    Diagrammer --> Auditor[8. Auditor de Qualidade & Fidelidade Visual]
    Auditor --> OutputFinal([Pacote Entregue: TXT, MD e PDF Diagramado])
`

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **PDF Oxide em 1º Lugar:** Para qualquer extração/leitura de PDF, use pdf_oxide (Rust/Python/Node). Demais ferramentas (docling, marker-pdf) são fallback.
2. **Tradução em Lotes de 5 Páginas:** Nunca traduza o livro inteiro de uma vez; opere em micro-lotes para evitar alucinações e perda de termos.
3. **Glossário & Consistência:** Mantenha glossário bilíngue estrito (ver glossarys/) para mecânicas e termos de RPG.
4. **Preservação Visual de Página:** Mesma quantidade de páginas, fluxo de colunas e fidelidade às fontes originais do livro.
5. **Portão de Auditoria Visual:** O Auditor compara página a página antes da homologação final.

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Arquitetura dos 8 Subagentes](references/arquitetura-subagentes-book-formatter.md): Perfis e fluxo de trabalho de cada agente.
- [Guia Completo de Diagramação (Português)](references/book-formatter-guide-ptbr.md): As 8 fases obrigatórias de diagramação, protocolos Karpathy e regras de tradução.
- [Complete Diagramming Guide (English)](references/book-formatter-guide-en.md): Full extraction matrix, SOTA AI engines, format matrix and quality checklists.
- [Guia do Motor PDF Oxide](pdf-oxide-guide.md): Instalação e uso de pdf-oxide para alta velocidade em Rust/Python/Node.
- [Cheatsheet Rápido](cheatsheet.md): Comandos e atalhos rápidos de conversão.
- [Design Systems](design-systems/): Paletas, fontes, ornamentos e tipografia para WoD, Fantasia e Sci-Fi.
- [Neurodiversidade](neurodiversity/): Diretrizes para acessibilidade visual, dislexia e contraste confortável.
- [Glossários de RPG](glossarys/): Dicionários de termos técnicos para World of Darkness e sistemas D20.
