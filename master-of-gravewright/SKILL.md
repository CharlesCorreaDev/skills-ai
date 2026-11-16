---
name: master-of-gravewright
description: Suíte de Engenharia Reversa, Desenvolvimento de Sistemas, Módulos, Extensões, Itens, Compêndios e Diagnóstico Especializado para Gravewright VTT por GM Charles Corrêa.
---

# Master of Gravewright ⚔️🎲
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Suíte Multiagente para Gravewright VTT (0.5.0-beta)**

---

## 🏛️ Topologia dos 7 Subagentes Especializados

Para erradicar incompatibilidades e garantir alto desempenho no motor ECS do Gravewright, a suíte opera em pipeline coordenado:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Orquestrador Gravewright]
    Showrunner --> EcsArchitect[2. Arquiteto de Sistemas & Entidades ECS]
    EcsArchitect --> CanvasGpuDev[3. Especialista em Canvas WebGPU/WebGL]
    EcsArchitect --> RuleMechanic[4. Engenheiro de Regras de RPG & Compêndios]
    CanvasGpuDev & RuleMechanic --> NetSyncDev[5. Engenheiro de Sockets & Sincronização]
    CanvasGpuDev & RuleMechanic --> QATester[6. Engenheiro de QA & Testes de Integração]
    NetSyncDev & QATester --> SupremeAuditor[7. Auditor Geral de Performance & Segurança]
    SupremeAuditor --> OutputFinal([Extensão ou Sistema Gravewright Pronto])
`

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Arquitetura ECS em 1º Lugar:** Respeite o desacoplamento estrito entre Entidades, Componentes de dados puros e Sistemas de lógica.
2. **Governança de WebGPU/Canvas:** Otimize draw calls e utilize texturas compactadas para garantir 60 FPS estáveis.
3. **Portão de Auditoria de Sockets:** Garanta validação de autorização em todas as mensagens transmitidas via WebSocket.
4. **Fidelidade de Regras:** Compêndios e atributos devem refletir com precisão matemática o sistema de RPG selecionado.

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Arquitetura dos 7 Subagentes](references/arquitetura-subagentes-gravewright.md): Perfis e responsabilidades de cada especialista.
- [Contratos de API](contracts/): Especificações de schemas e contratos de eventos.
- [Templates de Desenvolvimento](templates/): Scaffolding inicial para módulos e extensões.
- [Documentação Técnica](docs/): Guias aprofundados sobre o ecossistema Gravewright.
