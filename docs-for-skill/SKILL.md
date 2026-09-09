---
name: docs-for-skill
description: Ingests documents (PDF, DOCX, XLSX, PPTX, ODT, ODS, HTML, EPUB) and transforms them into modular, high-performance agent skills with master index, mental models, on-demand chapters, cheatsheets, glossaries, and architectural patterns. Use when the user wants to convert a document into an actionable AI skill via Antigravity, Claude Code, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA, or Ollama, build a token-efficient knowledge base, or extract structured frameworks from complex manuals.
---

# Docs for Skill 🚀

---

## 🇺🇸 English

### 📌 Overview & Philosophy
**Docs for Skill** transforms heavy, monolithic documents (technical manuals, RPG rulebooks, laws, engineering specifications, company handbooks) into **modular, high-performance AI Skills**.

Instead of dumping an entire document into an AI agent's context window—which wastes thousands of tokens and causes attention degradation—**Docs for Skill** compiles the source material into an actionable, on-demand micro-knowledge repository.

### 🏗️ Architecture of a Generated Skill

```text
my-generated-skill/
├── SKILL.md             # Master bilingual index (EN / PT-BR) & Domain Mental Model
├── cheatsheet.md        # Quick reference tables, formulas, immediate rules & commands
├── glossary.md          # Canonical dictionary of technical terms, entities & definitions
├── patterns.md          # Architecture rules, decision flows, best practices & mechanics
└── chapters/            # Cleaned, balanced chapters loaded on-demand (~15KB to 40KB each)
    ├── ch01-introduction.md
    ├── ch02-core-mechanics.md
    └── ...
```

### 🔄 Ingestion & Extraction Pipeline

1. **Ingest & Extract:** Employs `docs-for-markdown` for layout-aware conversion (OCR, column ordering, table handling).
2. **Text Sanitization:** Strips recurring headers/footers, repairs hyphenation, and fixes character encodings (UTF-8).
3. **Semantic Modularization:** Detects natural sections and headings (`#`, `##`), balancing chapters into optimal token chunks.
4. **Synthesis of Fast-Path References:**
   - `cheatsheet.md`: Synthesizes syntax, calculations, and cheat sheets for rapid recall.
   - `glossary.md`: Catalogs core terminology, classes, and lore definitions.
   - `patterns.md`: Formulates architecture rules and anti-patterns.
5. **Master Index (`SKILL.md`):** Generates domain mental model and on-demand navigation map.

### 🛠️ CLI Usage
```bash
# Check environment dependencies
python scripts/check_env.py

# Ingest document and generate skill
python scripts/structure_skill.py "path/to/manual.pdf" "my-new-skill" [optional_output_dir]
```

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (pandoc, libreoffice, tesseract), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral & Filosofia
O **Docs for Skill** transforma documentos densos e volumosos (manuais técnicos, livros de regras de RPG, legislações, especificações de engenharia, manuais de processos) em **Skills Modulares de Alta Performance para Agentes de IA**.

Em vez de despejar um arquivo inteiro na janela de contexto de um LLM—o que desperdiça milhares de tokens e provoca alucinações por sobrecarga—o **Docs for Skill** compila o material em um repositório micro-modular de conhecimento carregado sob demanda.

### 🏗️ Arquitetura de uma Skill Gerada

```text
minha-skill/
├── SKILL.md             # Índice mestre bilíngue (EN / PT-BR) + Modelo Mental do Domínio
├── cheatsheet.md        # Resumo rápido de fórmulas, tabelas, comandos e regras imediatas
├── glossary.md          # Dicionário canônico de termos técnicos, entidades e definições
├── patterns.md          # Padrões de arquitetura, mecânicas, fluxos de decisão e boas práticas
└── chapters/            # Capítulos modulares carregados sob demanda (~15KB a 40KB por arquivo)
    ├── ch01-introducao.md
    ├── ch02-regras-basicas.md
    └── ...
```

### 🔄 Pipeline de Ingestão e Extração

1. **Ingestão & Extração:** Utiliza o motor do `docs-for-markdown` para conversão preservando layout (OCR, ordenação de colunas, tabelas).
2. **Sanitização Textual:** Remove cabeçalhos/rodapés repetitivos, reconecta palavras hifenizadas e normaliza para UTF-8.
3. **Modularização Semântica:** Identifica seções naturais e títulos (`#`, `##`), balanceando capítulos em blocos ideais de tokens.
4. **Síntese de Arquivos de Acesso Rápido:**
   - `cheatsheet.md`: Sintetiza tabelas de cálculo, comandos e atalhos para resposta imediata.
   - `glossary.md`: Dicionário estruturado de terminologias e entidades.
   - `patterns.md`: Regras arquiteturais, boas práticas e antipadrões.
5. **Índice Mestre (`SKILL.md`):** Constrói o modelo mental e o mapa de navegação sob demanda.

### 🛠️ Uso via CLI
```bash
# Verificar dependências do ambiente
python scripts/check_env.py

# Ingerir documento e estruturar skill
python scripts/structure_skill.py "caminho/para/manual.pdf" "minha-nova-skill" [diretorio_saida_opcional]
```

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro (dependências ausentes, permissões, ferramentas de SO, encoding de caracteres) e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente conforme seu propósito.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir a instalação de binários de sistema (pandoc, libreoffice, tesseract), pacotes globais ou configuração de chaves de API, o agente DEVE explicar o diagnóstico com clareza e solicitar a permissão explícita do desenvolvedor/operador antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar detalhadamente o que foi instalado e configurado para resolver o problema e executar imediatamente um teste de validação (ou solicitar ao operador os dados/arquivos necessários para testar a skill).
