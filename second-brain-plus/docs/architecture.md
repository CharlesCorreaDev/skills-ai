# Persistent Memory Architecture for AI Agents 🧠📐
# Arquitetura de Memória Persistente para Agentes de IA

> **Second Brain Plus Technical Specification / Especificação Técnica do Second Brain Plus**  
> *Bilingual Documentation: English (EN) and Portuguese (PT-BR) / Documentação Bilíngue: Inglês e Português*

---

## 🇺🇸 English

### 1. The Context Amnesia Problem in LLMs
Modern Large Language Models (LLMs) operate as stateless predictors. In multi-turn coding sessions:
1. **Context Drift:** As context windows fill up, "lost-in-the-middle" degrades attention.
2. **Session Reset:** Every fresh agent invocation starts with tabula rasa amnesia.
3. **Decision Hallucination:** Agents invent non-existent architectures instead of adhering to previously approved decisions.

### 2. The 5-Layer Memory Hierarchy
Second Brain Plus structures agent memory into 5 distinct operational tiers:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. WORKING MEMORY (Active Turn)                                             │
│    • In-memory prompt context, compressed via Caveman (-70% token overhead).│
├─────────────────────────────────────────────────────────────────────────────┤
│ 2. EPISODIC MEMORY (Session Timeline)                                       │
│    • Chronological logs, command history captured via claude-mem & Notion.  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3. SEMANTIC MEMORY (Factual Knowledge Base)                                 │
│    • Immutable rules, schemas, and Architecture Decision Records (ADRs).    │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4. PROCEDURAL MEMORY (Execution Runbooks)                                   │
│    • Build recipes, test routines, and Karpathy engineering guidelines.     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 5. KNOWLEDGE GRAPH (Relational Causality)                                   │
│    • Entity relationships and cross-file dependencies via Graphify.         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3. Memory Ecosystem Comparison Matrix

| Project / Library | Primary Memory Model | Core Advantage | Second Brain Plus Integration |
|---|---|---|---|
| **`claude-mem`** | Episodic / Chronological | Zero-friction session tracking | Ingests into `.second-brain/4-Archives/` and Notion |
| **`graphify`** | Knowledge Graph (KG) | Zero-database lightweight AST graph | Builds `.graphify/graph.json` connecting notes and ADRs |
| **`caveman`** | Context Compression | Ultra-dense keyword dialect | Drastically cuts working memory token footprint |
| **`grill-me`** | Inquiry / Alignment | Eliminates hidden assumptions | Distills inquiry output directly into permanent ADRs |
| **`karpathy-guidelines`** | Engineering Rigor | Surgical edits & empirical proof | Enforces verification before task completion |
| **`not-today-adhd`** | Cognitive Ergonomics | Low-overload visual presentation | Simplifies tasks into atomic single actions |
| **`mem0`** | Vector + Temporal Graph | Adaptive user preference scoring | REST synchronization capability |
| **`superlocalmemory`** | 100% Offline Vector DB | Complete privacy and sovereignty | Recommended for sensitive enterprise repositories |

---

## 🇧🇷 Português

### 1. O Problema da Amnésia e Alucinação em Agentes de IA
Modelos fundacionais não possuem estado contínuo entre invocações. Quando um agente autônomo opera em projetos complexos, depara-se com dois gargalos:
1. **Context Drift:** Degradação de atenção à medida que a janela de tokens cresce.
2. **Amnésia entre Sessões:** Ao iniciar nova sessão, o histórico de decisões passadas desaparece.
3. **Alucinação de Decisões:** O agente inventa dados técnicos que contrariam escolhas prévias.

### 2. A Hierarquia em 5 Camadas de Memória
O Second Brain Plus organiza a retenção de dados do agente em 5 camadas complementares:
1. **Working Memory (Memória de Trabalho):** Contexto da rodada atual, comprimido via Caveman para economia drástica de tokens.
2. **Episodic Memory (Memória Episódica):** Diário cronológico de sessões registrado via claude-mem e espelhado no Notion.
3. **Semantic Memory (Memória Semântica):** Fatos, schemas, regras de negócio e ADRs estruturados como Única Fonte da Verdade (SSOT).
4. **Procedural Memory (Memória Procedural):** Runbooks de execução guiados pelas diretrizes de simplicidade de Andrej Karpathy.
5. **Knowledge Graph (Grafo de Conhecimento):** Nós e arestas extraídos pelo Graphify para mapear dependências cruzadas entre código e notas.

### 3. Protocolo de Verificação Anti-Alucinação
1. **Pre-turn Retrieval:** Consulta mandatória ao repositório local e ao Notion antes de qualquer afirmação técnica.
2. **Grounding Estrito:** Citação obrigatória do ID do documento de referência (`Conforme ADR-001...`).
3. **Inquérito / Grill-me:** Se a informação não constar documentada, o agente não presume silenciosamente: aciona o alinhamento e registra formalmente a nova decisão.
