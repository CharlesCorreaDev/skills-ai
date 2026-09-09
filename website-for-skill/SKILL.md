---
name: website-for-skill
description: End-to-end orchestration pipeline that crawls live websites, API documentation, and technical portals and compiles them into structured, token-efficient AI skills (SKILL.md, on-demand chapters, cheatsheet, glossary, patterns). Use when the user wants to transform a website or online API reference into an installable agent skill via Antigravity, Claude Code, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA, or Ollama.
---

# Website for Skill 🌐➡️🧠

---

## 🇺🇸 English

### 📌 Objective & Orchestration Model
**Website for Skill** is the high-level orchestration pipeline that integrates `docs-for-markdown` and `website-for-markdown` to automatically convert live websites, developer documentation, and web portals into **fully structured, production-ready AI Skills**.

Instead of manual scraping and editing, it runs an automated pipeline that produces a complete skill folder ready to be registered in your AI coding agent.

### 🏗️ Generated Skill Structure
- `SKILL.md`: Master bilingual index and domain mental model.
- `cheatsheet.md`: Immediate commands, CRUD patterns, and quick reference tables.
- `glossary.md`: Canonical dictionary of technical terms and entities.
- `patterns.md`: Best practices, architectural patterns, and lifecycle guidelines.
- `chapters/`: Segmented on-demand chapters (~15KB to 40KB each) loaded only when needed.

### 🔄 Orchestration Workflow
1. **Dependency Check:** Verifies Playwright, Python extraction libraries, and engine binaries (`check_env.py`).
2. **Web Ingestion:** Fetches pages via Playwright or Firecrawl crawler.
3. **Skill Compilation:** Analyzes headings and content chunks, building modular chapters and synthesized reference files (`SKILL.md`, `cheatsheet.md`, `glossary.md`, `patterns.md`).
4. **Deployment:** Places the generated skill in the workspace or global agent path (`~/.agents/skills/<skill-name>/`).

### 🛠️ CLI Usage
```bash
# Check environment
python Scripts/check_env.py

# Build skill from single documentation URL
python Scripts/build_skill.py "https://foundryvtt.com/api/v12/" "foundryvtt-api-v12" [output_dir]

# Build skill with recursive crawling (requires FIRECRAWL_API_KEY)
python Scripts/build_skill.py "https://docs.example.com" "example-skill" [output_dir] --crawl
```

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (pandoc, libreoffice, tesseract), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---

## 🇧🇷 Português (Brasil)

### 📌 Objetivo & Modelo de Orquestração
O **Website for Skill** é o orquestrador de alto nível que integra as capacidades de `docs-for-markdown` e `website-for-markdown` para converter automaticamente websites ao vivo, documentações de desenvolvedores e portais técnicos em **Skills Modulares Prontas para Agentes de IA**.

Em vez de raspar e estruturar arquivos manualmente, ele executa um pipeline automatizado que gera uma pasta de skill completa pronta para ser registrada no seu agente de codificação de IA.

### 🏗️ Estrutura da Skill Gerada
- `SKILL.md`: Índice mestre bilíngue e modelo mental do domínio.
- `cheatsheet.md`: Comandos imediatos, operações CRUD e tabelas de referência rápida.
- `glossary.md`: Dicionário canônico de termos técnicos e entidades.
- `patterns.md`: Boas práticas, padrões de arquitetura e regras de ciclo de vida.
- `chapters/`: Capítulos segmentados carregados sob demanda (~15KB a 40KB) apenas quando requisitados.

### 🔄 Fluxo de Orquestração
1. **Verificação de Ambiente:** Valida o Playwright, bibliotecas de extração Python e binários do sistema (`check_env.py`).
2. **Ingestão Web:** Captura as páginas via Playwright ou pelo rastreador recursivo do Firecrawl.
3. **Compilação da Skill:** Analisa títulos e blocos de conteúdo, gerando os capítulos modulares e os arquivos sintetizados (`SKILL.md`, `cheatsheet.md`, `glossary.md`, `patterns.md`).
4. **Entrega/Instalação:** Salva a skill no projeto ou na pasta global de skills do agente (`~/.agents/skills/<nome-da-skill>/`).

### 🛠️ Uso via CLI
```bash
# Verificar ambiente
python Scripts/check_env.py

# Gerar skill a partir de uma URL única de documentação
python Scripts/build_skill.py "https://foundryvtt.com/api/v12/" "foundryvtt-api-v12" [diretorio_saida]

# Gerar skill com varredura recursiva de domínio (requer FIRECRAWL_API_KEY)
python Scripts/build_skill.py "https://docs.exemplo.com" "exemplo-skill" [diretorio_saida] --crawl
```

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro (dependências ausentes, permissões, ferramentas de SO, encoding de caracteres) e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente conforme seu propósito.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir a instalação de binários de sistema (pandoc, libreoffice, tesseract), pacotes globais ou configuração de chaves de API, o agente DEVE explicar o diagnóstico com clareza e solicitar a permissão explícita do desenvolvedor/operador antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar detalhadamente o que foi instalado e configurado para resolver o problema e executar imediatamente um teste de validação (ou solicitar ao operador os dados/arquivos necessários para testar a skill).
