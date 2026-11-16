---
name: second-brain-plus
description: Persistent memory, context management, and second brain orchestration suite for AI agents via Notion API, GitHub CLI (gh), GitLab CLI (glab), and local structured files. Synchronizes project knowledge, episodic session logs, and architectural decisions automatically with claude-mem, graphify, caveman, headroom, and context7 to eliminate agent amnesia and prevent hallucinations. Enforces automatic background synchronization, supports private or public remote repositories with proactive security auditing, and provides slash commands (/second-brain install, /second-brain save memory, /second-brain adr, /second-brain sync, /second-brain status, /second-brain git-status, /second-brain git-sync, /second-brain focus, /second-brain tdah). Integrates with grill-me for pre-decision alignment, karpathy-guidelines for engineering rigor, impeccable for craft design, and activates not-today-adhd for neurodivergent cognitive accessibility. Use when building or managing persistent AI memory, setting up Notion and Git remotes as a Single Source of Truth, synchronizing local markdown vaults with remote knowledge bases, or designing anti-hallucination context architectures for autonomous agents.
---

# Second Brain Plus 🧠⚡💾
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Status: Beta (0.1.0-beta)**

---

## 📌 Visão Geral & Modelo Mental / Overview

O **Second Brain Plus** resolve a amnésia contextual, desperdício de tokens e alucinações de agentes de IA através de uma infraestrutura em 3 camadas (Single Source of Truth - SSOT):
1. **Cofre Markdown Local (.second-brain/):** Estrutura P.A.R.A. 2.0 (Projetos, Áreas, Recursos, Arquivos).
2. **Notion Central Hub:** Dashboard relacional com 7 bancos mestres via API oficial do Notion.
3. **Repositórios Remotos Git (GitHub / GitLab):** Backup seguro, versionado e imutável.

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
| /second-brain focus / 	dah | Ativa visão de tarefa única e formatação com bionic reading (
ot-today-adhd). |

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Auto-Sync Obrigatório:** Sempre que uma nota, decisão ou tarefa for alterada, execute python second-brain-plus/scripts/auto_sync.py --now.
2. **5 Camadas de Memória:** Respeite a hierarquia: Memória de Trabalho (RAM/Caveman), Episódica (claude-mem), Semântica (graphify), Procedural (Skills) e Decisória (ADRs).
3. **Grill-then-Persist:** Alinhe decisões complexas com o usuário antes de gravá-las como ADR definitiva.

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Guia Completo em Português](references/guide-ptbr.md): Arquitetura detalhada das 5 camadas, sinergias e comandos de terminal.
- [Full Documentation Guide (English)](references/guide-en.md): In-depth 5-layer memory model, Notion developer ecosystem and CLI options.
- [Blueprint do Notion](templates/notion/second_brain_blueprint.json): Especificação JSON dos 7 bancos de dados relacionais.
