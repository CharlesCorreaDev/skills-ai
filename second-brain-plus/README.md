# Second Brain Plus 🧠⚡💾

> **Persistent Memory, Context Optimization & AI Second Brain Suite**  
> **Suíte de Memória Persistente, Otimização de Contexto e Segundo Cérebro para Agentes de IA**  
> *Automatic real-time synchronization across Notion API, Local Markdown Vault, claude-mem, and graphify with dedicated slash commands.*

---

## ⌨️ Comandos de Barra Dedicados / Dedicated Slash Commands

| Comando / Command | Finalidade / Purpose |
|---|---|
| **`/second-brain install`** | Instalação interativa e criação dos bancos no Notion / Setup & scaffolding |
| **`/second-brain save memory <texto>`** | Salva fatos, aprendizados ou regras na memória persistente e auto-sincroniza |
| **`/second-brain adr <título>`** | Registra uma decisão arquitetural formal anti-alucinação |
| **`/second-brain sync`** | Dispara sincronização imediata (Notion + claude-mem + graphify) |
| **`/second-brain status`** | Exibe painel de métricas do cofre e status da API |
| **`/second-brain focus`** | Alterna para o painel de foco atômico para neurodivergentes (Orbit OS) |
| **`/second-brain tdah`** | Ativa o modo TDAH com formatação biônica, 1 micro-ação por vez e Body Doubling |

---

## 🇺🇸 English Summary

Large Language Models (LLMs) and autonomous coding assistants excel at problem-solving, but suffer from critical shortcomings:
1. **Context Window Amnesia:** Losing past architectural choices when sessions reset or turn limits are reached.
2. **Hallucination of Stale APIs:** Confidently writing obsolete syntax for rapidly evolving libraries.
3. **Conversational Fluff & Token Drain:** Inefficient prompts wasting context space and degrading attention.

**Second Brain Plus** integrates a multi-tiered ecosystem that guarantees:
- **Single Source of Truth (SSOT):** Synchronized between Notion and local Git-tracked Markdown vaults.
- **Automatic Event-Driven Sync (`auto_sync.py`):** Automatically pushes changes to Notion, claude-mem, and graphify whenever files are modified.
- **Dedicated Slash Commands (`cli.py`):** Save memories, register ADRs, and check health seamlessly.
- **5-Layer Memory:** Working, Episodic, Semantic, Procedural, and Knowledge Graph.
- **Pre-Decision Alignment:** Leveraging `grill-me` to surface hidden assumptions and `karpathy-guidelines` for engineering rigor.
- **Token Efficiency:** Compressing payloads via `headroom` and enforcing ASD-STE100 controlled dialect with `caveman`.
- **Live Versioned Docs:** Pulling fresh library documentation on-demand using Upstash `context7`.
- **Neurodivergent Ergonomics:** Automatic cognitive accommodation via `not-today-adhd`.
- **Design Craft:** Eliminating generic AI slop using Paul Bakaus' `impeccable` guidelines.

---

## 🇧🇷 Sumário em Português

O **Second Brain Plus** resolve esses gargalos integrando:
- **Comandos de Barra Rápidos:** Salve memórias com `/second-brain save memory ...`, registre decisões com `/second-brain adr ...` ou verifique o sistema com `/second-brain status`.
- **Sincronização Automática em Tempo Real (`auto_sync.py`):** Disparada automaticamente sempre que o agente ou o desenvolvedor altera um arquivo, mantendo Notion, claude-mem e graphify em uníssono.
- **Única Fonte da Verdade (SSOT):** Notion (dashboard visual e colaborativo) + Repositório Local Git (`.second-brain/`).
- **Memória em 5 Camadas:** Working (Trabalho), Episódica (Sessões), Semântica (ADRs e Regras), Procedural (Runbooks) e Grafo de Conhecimento.
- **Alinhamento Pré-Decisão:** Uso do `grill-me` para inquérito dialético antes de assumir premissas e `karpathy-guidelines` para rigor e minimalismo.
- **Otimização de Contexto:** `headroom` para compressão de JSON e tool outputs locais e `caveman` para comunicação concisa sem perda semântica.
- **Documentação em Tempo Real:** Ingestão de bibliotecas atualizadas via Upstash `context7`.
- **Ergonomia Neurodivergente:** Modo de baixa carga cognitiva via `not-today-adhd` (Orbit OS / Brain Reset OS).
- **Design Craft:** Eliminação de "AI slop" visual com `impeccable`.

---

## 📦 Exemplos de Uso via Linha de Comando

```bash
# Salvar memória persistente
python second-brain-plus/scripts/cli.py save memory "PostgreSQL local porta 5433"

# Registrar ADR
python second-brain-plus/scripts/cli.py adr "Adoção de DuckDB" --rationale "Analytics local veloz"

# Disparar sincronização manual imediata
python second-brain-plus/scripts/cli.py sync

# Monitoramento contínuo em segundo plano
python second-brain-plus/scripts/auto_sync.py --watch

# Ver métricas e status
python second-brain-plus/scripts/cli.py status
```
