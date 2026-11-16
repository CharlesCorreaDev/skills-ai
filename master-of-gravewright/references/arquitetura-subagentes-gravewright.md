# Arquitetura Multiagente — Master of Gravewright ⚔️🎲

Para cobrir a plataforma de Virtual Tabletop Gravewright (VTT moderno com Canvas 2D/3D, WebGPU/WebGL, ECS e física de dados), a suíte opera com 7 Subagentes Especializados:

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

## Papéis e Responsabilidades dos 7 Subagentes:

1. **Orquestrador Gravewright (Showrunner):**
   - Coordena o ciclo de desenvolvimento, especificação de contratos e compatibilidade com o runtime.
2. **Arquiteto de Sistemas & Entidades (ECS):**
   - Modela componentes e entidades seguindo o paradigma Entity-Component-System nativo da engine.
3. **Especialista em Canvas & WebGPU/WebGL:**
   - Otimiza renderização de iluminação volumétrica, grid maps e efeitos visuais com shaders eficientes.
4. **Engenheiro de Regras de RPG & Compêndios:**
   - Converte mecânicas de jogo, tabelas e statblocks para o formato serializável do Gravewright.
5. **Engenheiro de Sockets & Sincronização de Rede:**
   - Gerencia eventos multiplayer em tempo real com baixa latência e conciliação de estado.
6. **Engenheiro de QA & Testes:**
   - Simula cenários de carga, estresse de entidades no canvas e testes automatizados.
7. **Auditor Geral de Performance & Segurança (Portão Final):**
   - Assegura estabilidade de FPS (>60fps), sanitização de inputs e integridade de memória.
