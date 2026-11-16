# Arquitetura Multiagente — Website for Skill 🌐➡️🧠

Para orquestrar o rastreamento recursivo de portais de documentação ao vivo, síntese de páginas técnicas e compilação em skills de IA modulares sem estourar janelas de contexto, a suíte opera com 6 Subagentes Especializados:

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

## Papéis e Responsabilidades dos 6 Subagentes:

1. **Orquestrador de Crawling & Compilação (Showrunner):**
   - Planeja o escopo de páginas, limites de profundidade e balanceamento de tópicos técnicos.
2. **Engenheiro de Rastreamento (Crawler Engineer):**
   - Executa o download de páginas via crawler HTTP multithread local, Playwright Chromium headless ou Firecrawl.
3. **Sanitizador de Ruído & Parser DOM:**
   - Remove menus, sidebars de navegação repetitivas, footers, scripts e banners de cookies, mantendo apenas o conteúdo técnico.
4. **Especialista em Grafo & Links Internos:**
   - Reescreve links relativos de documentações web (.html/.php) para referências locais limpas em Markdown (.md).
5. **Compilador de Skill:**
   - Gera a arquitetura padrão: SKILL.md conciso (<200 linhas), chapters/_INDEX.md, cheatsheet.md e glossary.md.
6. **Auditor de Integridade & Eficiência de Tokens (Portão Final):**
   - Valida balanceamento de capítulos (15KB a 40KB cada), ausência de links quebrados e conformance com o ecossistema.
