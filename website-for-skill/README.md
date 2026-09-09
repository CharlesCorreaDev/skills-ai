# Website for Skill 🌐➡️🧠

> **AI Skill Orchestrator: Turn Websites & API Docs into Structured Modular AI Skills**  
> *Orquestrador de Skills para IA: Transforme Websites e Documentações de API em Skills Modulares*

---

## 🇺🇸 English

### 📌 Overview
**Website for Skill** is the high-level orchestration skill that integrates `docs-for-markdown` and `website-for-markdown` to automatically convert live websites, developer documentations, and web portals into **fully structured, production-ready AI Skills**.

It automatically generates:
- `SKILL.md`: Master bilingual index and domain mental model.
- `cheatsheet.md`: Immediate commands, CRUD patterns, and quick reference tables.
- `glossary.md`: Key terminology and entity dictionary.
- `patterns.md`: Coding practices, architecture patterns, and lifecycle guidelines.
- `chapters/`: Segmented on-demand chapters optimized for LLM context windows.

---

### 🚀 Usage

#### 1. Verify Environment
```bash
python Scripts/check_env.py
```

#### 2. Build a Modular Skill from a Website
```bash
# Single page or documentation root
python Scripts/build_skill.py "https://example.com/docs" "my-new-skill" [optional_output_dir]

# Full domain recursive crawl (Requires FIRECRAWL_API_KEY)
python Scripts/build_skill.py "https://docs.example.com" "my-new-skill" [optional_output_dir] --crawl
```

---
---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral
O **Website for Skill** é o orquestrador de alto nível que integra as capacidades de `docs-for-markdown` e `website-for-markdown` para converter automaticamente websites, documentações de APIs e portais web em **Skills Modulares Prontas para Agentes de IA**.

A skill gera automaticamente:
- `SKILL.md`: Índice mestre bilíngue (EN / PT-BR) e modelo mental do domínio.
- `cheatsheet.md`: Comandos imediatos, operações CRUD e tabelas de referência rápida.
- `glossary.md`: Dicionário canônico de termos técnicos e entidades.
- `patterns.md`: Boas práticas, padrões de arquitetura e regras de ciclo de vida.
- `chapters/`: Capítulos segmentados e carregados sob demanda (~15KB a 40KB) para máxima eficiência de tokens.

---

### 🚀 Modo de Uso

#### 1. Verificação do Ambiente
```bash
python Scripts/check_env.py
```

#### 2. Gerar uma Nova Skill a Partir de uma URL
```bash
# Página única ou documentação base
python Scripts/build_skill.py "https://exemplo.com/docs" "nome-da-skill" [diretorio_saida]

# Varredura recursiva de domínio inteiro (Requer FIRECRAWL_API_KEY)
python Scripts/build_skill.py "https://docs.exemplo.com" "nome-da-skill" [diretorio_saida] --crawl
```

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (pandoc, libreoffice, tesseract), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro (dependências ausentes, permissões, ferramentas de SO, encoding de caracteres) e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente conforme seu propósito.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir a instalação de binários de sistema (pandoc, libreoffice, tesseract), pacotes globais ou configuração de chaves de API, o agente DEVE explicar o diagnóstico com clareza e solicitar a permissão explícita do desenvolvedor/operador antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar detalhadamente o que foi instalado e configurado para resolver o problema e executar imediatamente um teste de validação (ou solicitar ao operador os dados/arquivos necessários para testar a skill).

---

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)

