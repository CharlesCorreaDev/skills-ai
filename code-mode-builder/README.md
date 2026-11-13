# Code Mode Builder ⚡💻🧩

> **Architect, Builder & Runtime Orchestrator for Programmatic Tool Calling & Code-as-Action in AI Agents**  
> *Arquiteto, Gerador e Orquestrador de Code Mode (Chamada Programática de Ferramentas) para Agentes de IA por GM Charles Corrêa*  
> **Status: Beta (v0.2.0-beta)**

---

## 🇺🇸 English

### 📌 What is Code Mode?
Code Mode replaces the conventional, token-expensive pattern of dumping dozens of JSON schemas into an LLM's context window. Instead, it exposes **two minimal primitives** (`search` and `execute`) and allows the model to write TypeScript, JavaScript, Python, or Rhai scripts executed inside an isolated sandbox.

### 🌟 Core Capabilities
1. **API/MCP Catalog Compression:** Turns 50–500 tool endpoints into just 2 tools, cutting prompt token overhead by 80% to 95%.
2. **In-Memory Multi-Step Batching:** Replaces 10–30 sequential LLM turns with a single script executing parallel calls (`Promise.all`), filtering lists, and calculating aggregations in-memory.
3. **Sandbox Architectures:** Templates and guides for QuickJS WASM, Node.js V8 Isolates, Python Restricted Execution, and Rust Rhai.
4. **The Gate Pattern:** Keeps API tokens, credentials, and network sockets strictly outside the sandbox.
5. **Fail-Safe Observability:** Full `stdout`/`stderr` logging and structured `isError: true` responses for instant self-healing.

---

## 🇧🇷 Português (Brasil)

### 📌 O que é Code Mode?
O Code Mode substitui o padrão tradicional de despejar dezenas de ferramentas JSON no prompt da IA. Ele fornece **duas ferramentas mínimas** (`search` e `execute`) permitindo que o modelo escreva scripts que executam em sandbox isolado com acesso ao catálogo completo de ferramentas.

### 🌟 Vantagens Principais
- **Economia de até 95% de tokens de contexto.**
- **Redução drástica de round-trips e latência:** tarefas que levariam 20 turnos de ida e volta ocorrem em 1 único turno.
- **Isolamento de Credenciais:** As chaves de API nunca entram no runtime do script; ficam isoladas no host (*Gate Pattern*).

---

## 📁 Estrutura de Arquivos / Directory Structure

```text
code-mode-builder/
├── SKILL.md                          # Diretrizes mestras e padrões de arquitetura
├── README.md                         # Visão geral completa bilíngue (EN / PT-BR)
├── VERSION                           # Versão semântica atual (0.2.0-beta)
├── CHANGELOG.md                      # Histórico de alterações
├── scripts/
│   ├── check_codemode_env.py         # Diagnóstico de runtimes (Node, Python, uv)
│   └── scaffold_code_mode.py         # Gerador de harnesses e gateways Code Mode
├── templates/                        # Templates canônicos (TypeScript, Python, MCP Gateway)
└── docs/                             # Manuais de sandbox, benchmarks e padrões
    ├── architecture-patterns.md      # Padrões Gateway, Isolate e In-Process
    └── benchmarks-and-case-studies.md # Análise de custo, latência e tokens
```

---

## 👨‍💻 Autor / Author
**GM Charles Corrêa**  
- 🌐 Website: [charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 GitHub: [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ Skills AI: [github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)

