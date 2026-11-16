---
name: book-formatter
description: Book formatting and RPG book diagramming suite for AI agents. Installs any required document-reading toolchain (PDF with or without OCR, TXT, DOCX, DOC, CSV/TSV, XLSX/XLS, HTML, EPUB, images OCR) and orchestrates book diagramming delivering a TXT with the texts, a Markdown and a duly diagrammed PDF preserving the original layout. Built for paid AI workflows (ChatGPT + Adobe WORK plugin) to analyze, extract, translate in small batches, review and diagram RPG books (World of Darkness, Vampire: The Masquerade) with faithful typography, columns, margins, fonts, images, borders and ornaments. Use when the user wants to format, translate or diagram an RPG book into Portuguese via AI with TXT, Markdown and PDF deliverables via Antigravity, Claude Code, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA, or Ollama.
---

# Book Formatter / Diagramador de Livros 📕➡️📄
> *by GM Charles Corrêa* • **Versão v0.8.0-beta**

---

## 📌 Visão Geral & Modelo Mental / Overview

O **Book Formatter** é uma suíte multiplataforma para extração, tradução e diagramação de livros e manuais de RPG (World of Darkness, D&D, Tormenta20, etc.), garantindo fidelidade tipográfica e visual:
1. **.txt**: Texto extraído e traduzido.
2. **.md**: Versão em Markdown estruturado.
3. **.pdf**: PDF diagramado fiel ao layout original (colunas, fontes, imagens e ornamentos).

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **PDF Oxide em 1º Lugar:** Para qualquer extração/leitura de PDF, use pdf_oxide (Rust/Python/Node). Demais ferramentas (docling, marker-pdf) são fallback.
2. **Tradução em Lotes Pequenos:** Nunca traduza o livro inteiro de uma vez; opere em lotes de 5 a 10 páginas para evitar alucinações e perda de termos.
3. **Glossário & Consistência:** Mantenha glossário bilíngue estrito (ver glossarys/) para mecânicas e termos de RPG.
4. **Preservação Visual de Página:** Mesma quantidade de páginas, fluxo de colunas e fidelidade às fontes originais do livro.

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

### 📖 Manuais Canônicos Completos
- [Guia Completo de Diagramação (Português)](references/book-formatter-guide-ptbr.md): As 8 fases obrigatórias de diagramação, protocolos Karpathy e regras de tradução.
- [Complete Diagramming Guide (English)](references/book-formatter-guide-en.md): Full extraction matrix, SOTA AI engines, format matrix and quality checklists.
- [Guia do Motor PDF Oxide](pdf-oxide-guide.md): Instalação e uso de pdf-oxide para alta velocidade em Rust/Python/Node.
- [Cheatsheet Rápido](cheatsheet.md): Comandos e atalhos rápidos de conversão.

### 🎨 Design Systems & Neurodiversidade
- [Design Systems](design-systems/): Paletas, fontes, ornamentos e tipografia para WoD, Fantasia e Sci-Fi.
- [Neurodiversidade](neurodiversity/): Diretrizes para acessibilidade visual, dislexia e contraste confortável.
- [Glossários de RPG](glossarys/): Dicionários de termos técnicos para World of Darkness e sistemas D20.
