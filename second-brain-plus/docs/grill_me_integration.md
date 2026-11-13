# Grill-Me & Second Brain Plus Integration Guide 🎙️🧠
# Guia de Integração: Grill-Me & Second Brain Plus

> **The "Grill-then-Persist" Cycle / O Ciclo "Grill-then-Persist"**  
> *Bilingual Technical Documentation: English (EN) and Portuguese (PT-BR) / Documentação Técnica Bilíngue*

---

## 🇺🇸 English

### 1. The Missing Link: Why Combine `grill-me` with `second-brain-plus`?
The `grill-me` skill (created by Matt Pocock) conducts an exhaustive dialectical interview to test loose ideas and settle ambiguity. By design, `grill-me` is **stateless**: it writes no files and leaves no artifacts behind.

**Second Brain Plus provides stateful closure to `grill-me`:**
The mental effort spent during the inquiry is captured immediately by:
1. Synthesizing the inquiry into an **Architecture Decision Record (ADR)**.
2. Persisting the agreed-upon trade-offs into the local Markdown vault and the **Notion Decisions Database**.
3. Creating relational edges in the **Graphify** knowledge graph.

### 2. Operational Workflow
```
[Raw Idea] ──► 1. Inquiry (/grill-me) ──► 2. Frontier Closes ──► 3. Distill to ADR (Second Brain Plus)
```

---

## 🇧🇷 Português

### 1. O Elo Faltante: Por que unir `grill-me` com `second-brain-plus`?
A skill `grill-me` (criada por Matt Pocock) conduz uma entrevista dialética profunda para eliminar ambiguidades antes de começar a codificar. Por padrão, o `grill-me` é **sem estado (stateless)**: não salva arquivos e não deixa rastros.

**O Second Brain Plus adiciona persistência ao `grill-me`:**
Todo o alinhamento da entrevista é aproveitado imediatamente:
1. O script `memory_bridge.py --grill-distill` sintetiza a conversa em um **Architecture Decision Record (ADR)** formal.
2. Registra no cofre local e no **Banco de Decisões do Notion** para evitar futuras contradições.
3. Cria conexões no grafo de conhecimento do **Graphify**.

### 2. Sinergia com o Modo Neurodivergente (`not-today-adhd`)
Quando o perfil neurodivergente estiver ativo, o `grill-me` opera com perguntas atômicas:
- 1 pergunta por rodada com opções estruturadas.
- Sem sobrecarga de texto ou perguntas abertas confusas.
