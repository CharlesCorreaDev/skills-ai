---
name: second-brain-plus
description: Persistent memory, context management, and second brain orchestration suite for AI agents via Notion API, GitHub CLI (gh), GitLab CLI (glab), and local structured files. Synchronizes project knowledge, episodic session logs, and architectural decisions automatically with claude-mem, graphify, caveman, headroom, and context7 to eliminate agent amnesia and prevent hallucinations. Enforces automatic background synchronization, supports private or public remote repositories with proactive security auditing, and provides slash commands (/second-brain install, /second-brain save memory, /second-brain adr, /second-brain sync, /second-brain status, /second-brain git-status, /second-brain git-sync, /second-brain focus, /second-brain tdah). Integrates with grill-me for pre-decision alignment, karpathy-guidelines for engineering rigor, impeccable for craft design, and activates not-today-adhd for neurodivergent cognitive accessibility. Use when building or managing persistent AI memory, setting up Notion and Git remotes as a Single Source of Truth, synchronizing local markdown vaults with remote knowledge bases, or designing anti-hallucination context architectures for autonomous agents.
---

# Second Brain Plus 🧠⚡💾
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Suíte Multiagente de Memória Persistente (0.1.0-beta)**

---

## 🏛️ Topologia dos 6 Subagentes Especializados

Para erradicar amnésia e garantir coerência perfeita entre Markdown local, Notion e Git remoto, a suíte opera de forma federada:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Orquestrador de Contexto & Memória]
    Showrunner --> Ingestor[2. Ingestor & Triador P.A.R.A.]
    Showrunner --> AdrArchitect[3. Arquiteto de Decisões & ADRs]
    Ingestor --> NotionBridge[4. Engenheiro de Integração Notion API]
    AdrArchitect --> GitSync[5. Guardião de Versionamento Git gh/glab]
    NotionBridge & GitSync --> NeuroSync[6. Auditor de Saúde & Ergonomia TDAH]
    NeuroSync --> OutputFinal([Memória Sincronizada, Consistente & Blindada])
`

---

## ⌨️ Comandos de Barra Canônicos (/second-brain)

| Comando | Descrição / Finalidade |
|---|---|
| /second-brain install | Executa wizard interativo e provisiona o cofre PARA e bancos do Notion. |
| /second-brain save memory <fato> | Salva fato ou aprendizado atômico na memória persistente. |
| /second-brain adr <título> | Registra uma Decisão de Arquitetura (ADR) imutável anti-alucinação. |
| /second-brain sync | Dispara sincronização bidirecional imediata (Notion, Git, claude-mem). |
| /second-brain status | Exibe telemetria, integridade de notas e conectividade com a API. |
| /second-brain git-status | Audita sincronização remota via gh / glab e privacidade de repositórios. |
| /second-brain git-sync | Comita e envia alterações do cofre para o repositório remoto Git. |
| /second-brain focus / 	dah | Ativa visão de tarefa única e formatação neurodivergente (
ot-today-adhd). |

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Auto-Sync Obrigatório:** Sempre que uma nota, decisão ou tarefa for alterada, execute python second-brain-plus/scripts/auto_sync.py --now.
2. **5 Camadas de Memória:** Respeite a hierarquia: Memória de Trabalho (RAM/Caveman), Episódica (claude-mem), Semântica (graphify), Procedural (Skills) e Decisória (ADRs).
3. **Grill-then-Persist:** Alinhe decisões complexas com o usuário antes de gravá-las como ADR definitiva.

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Arquitetura dos 6 Subagentes](references/arquitetura-subagentes-second-brain.md): Papéis detalhados de cada especialista.
- [Guia Completo em Português](references/guide-ptbr.md): Arquitetura detalhada das 5 camadas, sinergias e comandos de terminal.
- [Full Documentation Guide (English)](references/guide-en.md): In-depth 5-layer memory model, Notion developer ecosystem and CLI options.
- [Blueprint do Notion](templates/notion/second_brain_blueprint.json): Especificação JSON dos 7 bancos de dados relacionais.
