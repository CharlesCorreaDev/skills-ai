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

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)

