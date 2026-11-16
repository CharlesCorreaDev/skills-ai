# Arquitetura dos 12 Subagentes Especializados — Master of Gravewright ⚔️🎲
## 12 Specialized Subagents Architecture — Master of Gravewright ⚔️🎲

A suíte **Master of Gravewright** opera sob o padrão de Engenharia Federada em Linha de Montagem com Quality Gates para o motor do Gravewright VTT (Python/Django, ECS nativo, WebGPU/WebGL Canvas, SQLite/PostgreSQL e WebSockets em tempo real).

The **Master of Gravewright** suite operates under a federated assembly line engineering model with Quality Gates for the Gravewright VTT engine (Python/Django, native ECS, WebGPU/WebGL Canvas, SQLite/PostgreSQL, and real-time WebSockets).

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor / User]) --> Showrunner[1. Showrunner & Orquestrador Gravewright]
    Showrunner --> SpecHandoff[2. Specs, PRs & Handoff SemVer]
    SpecHandoff --> Scaffolder[3. Scaffolding & Módulos GW]
    SpecHandoff --> RuleEngineer[4. Regras RPG & Compêndios]
    RuleEngineer --> EcsBackendDev[5. Backend ECS & Modelos Django]
    RuleEngineer --> FrontendDev[6. UI, Fichas & Reatividade Web]
    EcsBackendDev & FrontendDev --> CanvasGpuDev[7. Canvas WebGPU/WebGL & Shaders]
    EcsBackendDev & FrontendDev --> SocketsSyncDev[8. Sockets, Rede & Multiplayer]
    CanvasGpuDev & SocketsSyncDev --> CrossVttBridge[9. Portabilidade & Bridge Cross-VTT]
    CrossVttBridge --> QAEvaluator[10. QA & Testes de Integração]
    QAEvaluator --> SupremeAuditor[11. Auditor SAST & Portão de Qualidade]
    SupremeAuditor --> TechnicalWriter[12. Documentador Bilíngue EN/PT-BR]
    TechnicalWriter --> SpecHandoff
    SpecHandoff --> OutputFinal([Pacote Gravewright Validado, Testado e Homologado])
`

---

## 🇧🇷 Português (Brasil) — Papéis e Responsabilidades dos 12 Subagentes

1. **Showrunner & Orquestrador Gravewright:** Entrevista o desenvolvedor via grill-me, delimita o escopo, gerencia neurodiversidade (
ot-today-adhd), orquestra handoffs e impede desvio de foco.
2. **Engenheiro de Specs, PRs & Handoff:** Elabora Tech Specs/RFCs detalhadas antes de qualquer código, redige PRs profissionais, gera handoff de homologação e aplica versionamento estrito conforme [SemVer 2.0.0 PT-BR](https://semver.org/lang/pt-BR/).
3. **Arquiteto de Scaffolding & Módulos GW:** Estrutura pastas de extensões, manifestos do Gravewright, contratos de inicialização e bundlers.
4. **Engenheiro de Regras RPG & Compêndios:** Decodifica livros de regras (D20, WoD, Tormenta20, YZE) em especificações matemáticas, tabelas e statblocks serializáveis.
5. **Engenheiro de Backend ECS & Modelos Django:** Modela entidades, componentes desacoplados de dados puros e sistemas lógicos no paradigma ECS e persistência.
6. **Engenheiro de UI, Fichas & Reatividade Web:** Constrói fichas reativas, painéis de combate e modais com CSS encapsulado (scoped) para evitar vazamento visual.
7. **Especialista em Canvas WebGPU/WebGL & Shaders:** Renderização de alta performance do grid, iluminação dinâmica, sombras e fog-of-war a 60 FPS cravados.
8. **Engenheiro de Sockets, Rede & Multiplayer:** Sincronização em tempo real de rolagens, movimento de tokens e estado via WebSockets de baixa latência.
9. **Engenheiro de Portabilidade & Bridge Cross-VTT:** Converte atores, itens, cenas e aventuras de outros VTTs (Foundry VTT e Roll20) para o Gravewright.
10. **Engenheiro de QA & Testes de Integração:** Constrói suítes de testes unitários (pytest) e simulações de estresse de carga com múltiplos clientes.
11. **Auditor Geral de Código, SAST & Performance:** Portão obrigatório de qualidade: análise estática SAST (Bandit/ESLint), auditoria de segurança e governança anti-freeze.
12. **Redator Técnico & Documentador Bilíngue:** Produz wikis, manuais do usuário, JSDoc/Docstrings e arquivos de localização (i18n) rigorosamente em Português e Inglês.

---

## 🇺🇸 English — Roles and Responsibilities of the 12 Subagents

1. **Showrunner & Gravewright Orchestrator:** Interviews developers via grill-me, establishes scope bounds, supports neurodiversity (
ot-today-adhd), and oversees agent handoffs.
2. **Specs, PRs, SSD & Handoff Engineer:** Authors comprehensive Tech Specs/RFCs prior to code execution, drafts PRs, and enforces [SemVer 2.0.0](https://semver.org/).
3. **Scaffolding & GW Module Architect:** Structures extension folders, manifests, lifecycle bootloaders, and bundlers.
4. **RPG Rules & Compendium Engineer:** Transcribes tabletop rulebooks (D20, WoD, Tormenta20, YZE) into pure mathematical logic, tables, and serializable statblocks.
5. **ECS Backend & Django Models Engineer:** Architect of decoupled entities, pure data components, and execution systems under the ECS paradigm.
6. **UI, Sheets & Reactive Web Engineer:** Develops reactive character sheets, combat HUDs, and dialogs with scoped CSS isolation.
7. **WebGPU/WebGL Canvas & Shaders Specialist:** Delivers high-performance grid rendering, dynamic lighting, vision, and particle effects locked at 60 FPS.
8. **Sockets, Netcode & Multiplayer Engineer:** Handles real-time multiplayer synchronization, token movement, and roll dispatch over low-latency WebSockets.
9. **Portability & Cross-VTT Bridge Specialist:** Migrates actors, items, scenes, and compendiums from Foundry VTT and Roll20 into native Gravewright schemas.
10. **QA & Integration Testing Engineer:** Implements automated test suites (pytest), headless browser validations, and multi-client load simulations.
11. **Supreme Code Auditor, SAST & Performance Gatekeeper:** Mandatory Quality Gate enforcing SAST security (Bandit/ESLint), memory profiling, and anti-freeze governance.
12. **Bilingual Technical Writer (EN / PT-BR):** Delivers technical wikis, manuals, Docstrings, and localization assets (i18n) in English and Brazilian Portuguese.
