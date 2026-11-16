# Arquitetura dos 6 Subagentes Especializados — Website for Skill 🌐➡️🧠
## 6 Specialized Subagents Architecture — Website for Skill 🌐➡️🧠

A suíte **Website for Skill** orquestra o rastreamento recursivo de portais de documentação ao vivo, síntese de páginas técnicas e compilação em skills de IA modulares sem estourar janelas de contexto.

The **Website for Skill** suite orchestrates the recursive crawling of live documentation portals, technical page synthesis, and compilation into modular AI skills without overflowing LLM context windows.

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor / User]) --> Showrunner[1. Orquestrador de Crawling & Compilação]
    Showrunner --> CrawlerEngineer[2. Engenheiro de Rastreamento HTTP/Playwright/Firecrawl]
    CrawlerEngineer --> ContentSanitizer[3. Sanitizador de Ruído HTML & Parser DOM]
    ContentSanitizer --> LinkRewriter[4. Especialista em Grafo & Links Internos .md]
    LinkRewriter --> SkillSynthesizer[5. Compilador de Skill SKILL.md/Cheatsheet/Glossary]
    SkillSynthesizer --> QualityAuditor[6. Auditor de Integridade & Token Efficiency]
    QualityAuditor --> OutputFinal([Skill Estruturada, Enxuta e Pronta para Uso])
`

---

## 🇧🇷 Português (Brasil) — Papéis e Responsabilidades dos 6 Subagentes

1. **Orquestrador de Crawling & Compilação (Showrunner):** Planeja o escopo de páginas, limites de profundidade e balanceamento de tópicos técnicos.
2. **Engenheiro de Rastreamento (Crawler Engineer):** Executa o download de páginas via crawler HTTP multithread local, Playwright Chromium headless ou Firecrawl.
3. **Sanitizador de Ruído & Parser DOM:** Remove menus, sidebars de navegação repetitivas, footers, scripts e banners de cookies, mantendo apenas o conteúdo técnico.
4. **Especialista em Grafo & Links Internos:** Reescreve links relativos de documentações web (.html/.php) para referências locais limpas em Markdown (.md).
5. **Compilador de Skill:** Gera a arquitetura padrão: SKILL.md conciso (<200 linhas), chapters/_INDEX.md, cheatsheet.md e glossary.md conforme [SemVer 2.0.0 PT-BR](https://semver.org/lang/pt-BR/).
6. **Auditor de Integridade & Eficiência de Tokens (Portão Final):** Valida balanceamento de capítulos (15KB a 40KB cada), ausência de links quebrados e conformance com o ecossistema.

---

## 🇺🇸 English — Roles and Responsibilities of the 6 Subagents

1. **Crawling & Compilation Orchestrator (Showrunner):** Outlines target domain boundaries, max crawl depth, and topic chunking budgets.
2. **Web Crawling Engineer:** Executes asynchronous page fetching via multithreaded HTTP crawler, headless Chromium (Playwright), or Firecrawl API.
3. **DOM Sanitizer & Noise Filter:** Purges navigation sidebars, repetitive headers, footers, tracking scripts, and cookie banners.
4. **Graph & Internal Link Rewriter:** Re-maps online relative hyperlinks (.html, .php) into clean local Markdown references (.md).
5. **Skill Compiler & Synthesizer:** Compiles the standard skill artifact: lean SKILL.md (<200 lines), chapters/_INDEX.md, cheatsheet.md, and glossary.md.
6. **Integrity & Token Efficiency Auditor (Mandatory Quality Gate):** Validates chapter chunk sizes (15KB to 40KB), zero dead links, and ecosystem compliance.
