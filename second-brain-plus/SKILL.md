---
name: second-brain-plus
description: Persistent memory, context management, and second brain orchestration suite for AI agents via Notion API, GitHub CLI (gh), GitLab CLI (glab), and local structured files. Orquestra 7 subagentes cobrindo Contexto/Memoria, Specs/PRs/SSD/Handoff, Ingestao P.A.R.A. 2.0, ADRs Imutaveis, Integracao Notion API, Versionamento Git gh/glab e Ergonomia Cognitiva TDAH. Sincroniza automaticamente conhecimentos do projeto, logs episodicos e decisoes de arquitetura para eliminar amnesia e alucinacoes.
---

# Second Brain Plus 🧠⚡💾
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Suíte Federada de 7 Subagentes de Memória Persistente (v0.2.0-beta)**

---

## 🏛️ Topologia dos 7 Subagentes Especializados

Para erradicar a amnésia e registrar 100% das decisões, especificações, PRs e handoffs do projeto em memória persistente:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor / User]) --> Showrunner[1. Orquestrador de Contexto & Memória]
    Showrunner --> SpecHandoff[2. Specs, PRs, SSD & Handoff]
    Showrunner --> Ingestor[3. Ingestor & Triador P.A.R.A. 2.0]
    SpecHandoff --> AdrArchitect[4. Arquiteto de Decisões & ADRs Imutáveis]
    Ingestor & AdrArchitect --> NotionBridge[5. Integração Notion API]
    SpecHandoff & AdrArchitect --> GitSync[6. Versionamento Git gh/glab]
    NotionBridge & GitSync --> NeuroSync[7. Auditor de Saúde & Ergonomia TDAH]
    NeuroSync --> OutputFinal([Memória Sincronizada, Consistente & Blindada])
`

---

## ⌨️ Comandos de Barra Canônicos (/second-brain)

| Comando | Descrição / Finalidade |
|---|---|
| /second-brain install | Executa wizard interativo e provisiona o cofre PARA e bancos do Notion. |
| /second-brain save memory <fato> | Salva fato ou aprendizado atômico na memória persistente. |
| /second-brain adr <título> | Registra uma Decisão de Arquitetura (ADR) imutável anti-alucinação. |
| /second-brain spec <título> | Registra uma Especificação Técnica (Tech Spec / SSD) formal do projeto. |
| /second-brain pr <título> | Gera e persiste a descrição atômica de PR e critérios de aceitação. |
| /second-brain handoff <título> | Estrutura o guia de handoff e homologação do projeto. |
| /second-brain sync | Dispara sincronização bidirecional imediata (Notion, Git, claude-mem). |
| /second-brain status | Exibe telemetria, integridade de notas e conectividade com a API. |
| /second-brain git-sync | Comita e envia alterações do cofre para o repositório remoto Git. |
| /second-brain focus / tdah | Ativa visão de tarefa única e formatação neurodivergente (not-today-adhd). |

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Auto-Sync Obrigatório:** Sempre que uma nota, decisão, spec ou PR for alterada, execute python second-brain-plus/scripts/auto_sync.py --now.
2. **Memória de Ciclo de Vida (Specs/SSD/PRs/Handoff):** Registre decisões e alterações de arquitetura em .second-brain/ para consulta de futuras sessões de IA.
3. **5 Camadas de Memória:** Respeite a hierarquia: Memória de Trabalho (RAM/Caveman), Episódica (claude-mem), Semântica (graphify), Procedural (Skills) e Decisória (ADRs/Specs).
4. **SemVer 2.0.0 (PT-BR) & Padrão Bilíngue:** Releases e documentações estritamente em EN e PT-BR.
5. **Grill-then-Persist:** Alinhe decisões complexas com o usuário antes de gravá-las como ADR/Spec definitiva.

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Arquitetura dos 7 Subagentes](references/arquitetura-subagentes-second-brain.md): Perfis e responsabilidades de cada especialista.
- [Guia Completo em Português](references/guide-ptbr.md): Arquitetura detalhada das 5 camadas, sinergias e comandos de terminal.
- [Full Documentation Guide (English)](references/guide-en.md): In-depth 5-layer memory model, Notion developer ecosystem and CLI options.
- [Blueprint do Notion](templates/notion/second_brain_blueprint.json): Especificação JSON dos 7 bancos de dados relacionais.
