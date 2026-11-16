# Arquitetura dos 12 Subagentes Especializados — Master of Gravewright ⚔️🎲
## Suíte de Desenvolvimento, Engenharia Reversa e Extensões para Gravewright VTT — by GM Charles Corrêa

A suíte **Master of Gravewright** opera sob o padrão de **Engenharia Federada em Linha de Montagem com Quality Gates**, espelhando o rigor da suíte Foundry VTT, mas adaptada ao motor nativo do Gravewright (Python/Django backend, ECS nativo, WebGPU/WebGL Canvas, SQLite/PostgreSQL e Websockets em tempo real):

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Showrunner & Orquestrador Gravewright]
    
    Showrunner --> SpecHandoff[2. Engenheiro de Specs, PRs & Handoff SemVer]
    
    SpecHandoff -->|Scaffolding & Contratos| Scaffolder[3. Arquiteto de Scaffolding & Módulos GW]
    SpecHandoff -->|Matemática & Regras| RuleEngineer[4. Engenheiro de Regras RPG & Compêndios]
    
    RuleEngineer --> EcsBackendDev[5. Engenheiro de Backend ECS & Modelos Django]
    RuleEngineer --> FrontendDev[6. Engenheiro de UI, Fichas & Reatividade Web]
    
    EcsBackendDev & FrontendDev --> CanvasGpuDev[7. Especialista em Canvas WebGPU/WebGL & Shaders]
    EcsBackendDev & FrontendDev --> SocketsSyncDev[8. Engenheiro de Sockets, Rede & Multiplayer]
    
    CanvasGpuDev & SocketsSyncDev --> CrossVttBridge[9. Engenheiro de Portabilidade & Bridge Cross-VTT]
    
    CrossVttBridge --> QAEvaluator[10. Engenheiro de QA & Testes de Integração]
    
    QAEvaluator --> SupremeAuditor[11. Auditor Geral de Código, SAST & Performance]
    
    SupremeAuditor --> TechnicalWriter[12. Redator Técnico & Documentador Bilíngue EN/PT-BR]
    
    TechnicalWriter --> SpecHandoff
    SpecHandoff --> OutputFinal([Pacote Gravewright Validado, Testado, Documentado e Pronto])
`

---

## 🏛️ Papéis e Responsabilidades dos 12 Subagentes

### 1. Showrunner & Orquestrador Gravewright (Gatekeeper de Entrada)
- **Missão:** Entrevista o desenvolvedor via grill-me, delimita o escopo, gerencia neurodiversidade (
ot-today-adhd), orquestra os handoffs entre agentes e impede desvio de foco.

### 2. Engenheiro de Specs, PRs & Handoff (Project & Release Manager)
- **Missão:** Elabora Tech Specs/RFCs detalhadas antes de qualquer código, redige PRs profissionais, gera handoff de homologação para o mestre e aplica versionamento estrito conforme [SemVer 2.0.0 PT-BR](https://semver.org/lang/pt-BR/).

### 3. Arquiteto de Scaffolding & Módulos GW (Organizador de Estrutura)
- **Missão:** Estrutura pastas de extensões, manifestos do Gravewright, contratos de inicialização e bundlers sem poluição de arquivos.

### 4. Engenheiro de Regras RPG & Compêndios (Analista de Sistemas)
- **Missão:** Decodifica livros de regras (D20, WoD, Tormenta20, YZE, etc.) em especificações matemáticas, tabelas e statblocks serializáveis para os compêndios do Gravewright.

### 5. Engenheiro de Backend ECS & Modelos Django (Entity-Component-System)
- **Missão:** Modela as entidades, componentes desacoplados de dados puros e sistemas lógicos no paradigma ECS e persistência em SQLite/PostgreSQL.

### 6. Engenheiro de UI, Fichas & Reatividade Web (Frontend Designer)
- **Missão:** Constrói fichas de personagens reativas, painéis de combate e janelas modais com CSS encapsulado (scoped) para evitar vazamento visual.

### 7. Especialista em Canvas WebGPU/WebGL & Shaders (Canvas Master)
- **Missão:** Renderização de alta performance do grid, iluminação dinâmica, sombras, fog-of-war e efeitos de partículas mantendo 60 FPS cravados.

### 8. Engenheiro de Sockets, Rede & Multiplayer (Netcode Specialist)
- **Missão:** Sincronização em tempo real de rolagens, movimento de tokens e estado de cena via WebSockets de baixa latência e conciliação otimista.

### 9. Engenheiro de Portabilidade & Bridge Cross-VTT (Foundry / Roll20 Bridge)
- **Missão:** Converte atores, itens, cenas e aventuras de outros VTTs (Foundry VTT e Roll20) para a arquitetura nativa do Gravewright.

### 10. Engenheiro de QA & Testes de Integração (Quality Assurance)
- **Missão:** Constrói suítes de testes unitários (pytest) e simulações de estresse de carga e rede com múltiplos clientes conectados.

### 11. Auditor Geral de Código, SAST & Performance (Revisor Supremo)
- **Missão:** **Portão obrigatório de qualidade**: Análise estática SAST (Bandit/ESLint), auditoria de segurança (Cloudflare), profilamento de CPU/GPU e governança anti-freeze.

### 12. Redator Técnico & Documentador Bilíngue (Technical Writer EN/PT-BR)
- **Missão:** Produz wikis, manuais do usuário, JSDoc/Docstrings e arquivos de localização (i18n) rigorosamente em Português e Inglês.
