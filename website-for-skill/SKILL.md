---
name: website-for-skill
description: End-to-end orchestration pipeline that crawls live websites, API documentation, and technical portals and compiles them into structured, token-efficient AI skills (SKILL.md, chapters/_INDEX.md, cheatsheet, glossary, patterns) with preserved internal links.
---

# Website for Skill 🌐➡️🧠
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Suíte Multiagente de Compilação Web para Skills (0.5.0-beta)**

---

## 🏛️ Topologia dos 6 Subagentes Especializados

Para erradicar ruído web, links quebrados e desorganização de capítulos, a suíte atua de forma orquestrada:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Orquestrador de Crawling & Compilação]
    Showrunner --> CrawlerEngineer[2. Engenheiro de Rastreamento HTTP/Playwright/Firecrawl]
    CrawlerEngineer --> ContentSanitizer[3. Sanitizador de Ruído HTML & Parser DOM]
    ContentSanitizer --> LinkRewriter[4. Especialista em Grafo & Links Internos .md]
    LinkRewriter --> SkillSynthesizer[5. Compilador de Skill SKILL.md/Cheatsheet/Glossary]
    SkillSynthesizer --> QualityAuditor[6. Auditor de Integridade & Token Efficiency]
    QualityAuditor --> OutputFinal([Skill Estruturada, Enxuta e Pronta para Uso])
`

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Eficiência Máxima de Contexto:** O SKILL.md gerado deve atuar apenas como índice mestre sob demanda (< 200 linhas).
2. **Remoção Estrita de Ruído:** Banners, menus e footers de portais devem ser purgados antes da compilação em Markdown.
3. **Preservação de Links Internos:** Links para outras páginas da documentação devem apontar para os arquivos .md locais gerados.
4. **Portão de Auditoria de Capítulos:** Capítulos individuais mantidos entre 15KB e 40KB para carregamento otimizado.

---

## 🔗 Protocolo de Skills Companheiras (SDD, Handoff, TDD & Rigor)
`ash
# Stack Supremo de Economia de Tokens & Otimizacao
npx skills@latest add headroomlabs-ai/headroom
npx skills@latest add rtk-ai/rtk
npx skills@latest add JuliusBrussee/caveman
npx skills@latest add dietrichgebert/ponytail

# Suite de Engenharia Rigorosa, SDD, TDD, Handoff & GodMode
npx skills@latest add noobygains/godmode
npx skills@latest add addyosmani/agent-skills --skill=spec-driven-development
npx skills@latest add mattpocock/skills --skill=grill-me
npx skills@latest add mattpocock/skills --skill=handoff
npx skills@latest add mattpocock/skills --skill=tdd
npx skills@latest add aihero-dev/skills-code-review
npx skills@latest add multica-ai/andrej-karpathy-skills
npx skills@latest add cloudflare/security-audit-skill
npx skills@latest add NVIDIA/auto-ontology
`

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Metodologias SDD, Handoff, Grill-Me & TDD](references/sdd-handoff-grillme-tdd.md): Especificação rigorosa, alinhamento, TDD e handoff.
- [Arquitetura dos 6 Subagentes](references/arquitetura-subagentes-website-for-skill.md): Perfis e responsabilidades de cada especialista.
- [Scripts de Compilação](Scripts/): Automação de crawling e compilação estruturada.
- [Changelog de Versões](CHANGELOG.md): Histórico de melhorias da suíte.
