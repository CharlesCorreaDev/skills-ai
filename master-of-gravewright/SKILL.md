---
name: master-of-gravewright
description: Suíte de Engenharia Reversa, Desenvolvimento de Sistemas, Módulos, Extensões, Itens, Compêndios e Diagnóstico Especializado para Gravewright VTT por GM Charles Corrêa. Orquestra 12 subagentes especializados cobrindo Specs, PRs, SSD & Handoff SemVer, Scaffolding, regras de RPG, backend ECS/Django, UI reativa, Canvas WebGPU/WebGL, Sockets em tempo real, Bridge Cross-VTT, QA automatizado, auditoria SAST e documentação técnica bilíngue (EN/PT-BR).
---

# Master of Gravewright ⚔️🎲
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Suíte Federada de 12 Subagentes para Gravewright VTT (0.6.0-beta)**

---

## 🏛️ Topologia dos 12 Subagentes Especializados

Para erradicar alucinações de engine, falhas de sincronização e perda de performance no canvas, a suíte opera em pipeline federado:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Showrunner & Orquestrador Gravewright]
    Showrunner --> SpecHandoff[2. Specs, PRs, SSD & Handoff SemVer]
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
    SpecHandoff --> OutputFinal([Pacote Validado, Testado e Homologado])
`

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Arquitetura ECS Desacoplada:** Entidades são IDs, Componentes são dados puros e Sistemas contêm toda a lógica de execução.
2. **WebGPU/Canvas a 60 FPS:** Proibido gargalos de renderização; otimize draw calls e utilize texturas compactadas.
3. **Bridge Cross-VTT Precisa:** Conversões de Foundry ou Roll20 devem validar paridade de atributos e grids.
4. **SemVer 2.0.0 (PT-BR) & Padrão Bilíngue:** Releases e documentações obrigatoriamente bilíngues (EN/PT-BR).
5. **Portão de Auditoria Supremo:** O Auditor Geral (SAST) valida segurança e estabilidade antes da homologação.

---

## 🔗 Protocolo de Skills Companheiras
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
- [Arquitetura dos 12 Subagentes](references/arquitetura-subagentes-gravewright.md): Perfis, entregáveis e fluxos detalhados.
- [Contratos de API & Schemas](contracts/): Especificações de eventos e serialização de dados.
- [Templates de Desenvolvimento](templates/): Scaffolding moderno de módulos e extensões.
- [Documentação Técnica da Engine](docs/): Guias aprofundados sobre a engine Gravewright.
