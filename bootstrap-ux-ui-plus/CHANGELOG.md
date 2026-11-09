# Changelog - Bootstrap UX/UI Plus 🎨⚡

All notable changes to the `bootstrap-ux-ui-plus` skill will be documented in this file.  
*Todas as alterações notáveis na skill `bootstrap-ux-ui-plus` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0-beta] - 2026-11-08

### Added / Adicionado
- **Lançamento Inicial da Skill (`bootstrap-ux-ui-plus` v0.1.0-beta):**
  - **Mapeamento Prático das 18 Leis do UX (`laws/laws-of-ux-bootstrap.md`):**
    - Tradução detalhada de todas as 18 Leis Canônicas do UX (Hick, Fitts, Jakob, Proximidade, Semelhança, Região Comum, Conectividade Uniforme, Miller, Doherty, Von Restorff, Posição Serial, Pico-Fim, Zeigarnik, Prägnanz, Tesler, Postel, Parkinson, Occam & Pareto) em componentes e utilitários do Bootstrap (v5.3 & v6.0).
  - **10 Heurísticas de Usabilidade de Jakob Nielsen (`heuristics/nielsen-heuristics-bootstrap.md`):**
    - Aplicação prática de visibilidade de status, prevenção de erros, saídas de emergência (Undo) e design minimalista no framework.
  - **Diretrizes de Acessibilidade & WCAG 2.2 AA (`accessibility/a11y-wcag-guidelines.md`):**
    - Padrões de conformidade baseados em AccessLint com atributos ARIA mandatórios, preservação de anéis de foco (`.focus-ring`), contraste sutil e alvos de toque mobile.
  - **Template Completo de Dashboard Administrativo (`templates/admin-dashboard-template.html`):**
    - Painel corporativo com navegação lateral (Sidebar), barra superior de busca, cards de métricas (Chunking), tabela responsiva e alternador dinâmico de tema claro/escuro.
  - **Padrões Canônicos de Dashboards Mazer & AdminKit (`patterns/mazer-and-adminkit-standards.md`):**
    - Estruturação baseada em [zuramai/mazer](https://github.com/zuramai/mazer) (`#app > #sidebar + #main`) e [adminkit/adminkit](https://github.com/adminkit/adminkit) (`.wrapper > .sidebar + .main`) com zero dependência de jQuery e Vanilla JS nativo.
  - **Motor CLI de Auditoria e Validação (`scripts/audit_ux_bootstrap.mjs`):**
    - Linter automatizado para verificar inconformidades de acessibilidade e usabilidade em arquivos HTML, PHP, JSX e templates.
  - **Documentação Arquitetural e de Consulta:**
    - `cheatsheet.md`: Tabela rápida relacionando Leis de UX a classes do Bootstrap.
    - `glossary.md`: Glossário técnico com termos de HCI, psicologia cognitiva e Bootstrap.
    - `patterns.md`: Padrões de implementação para PHP (Blade), React (Next.js/TSX), Python (Django/Jinja2) e Node.js.
    - `README.md` e `SKILL.md` bilíngues (Inglês e Português).
