---
name: code-mode-builder
description: Architect, builder, and orchestrator of Code Mode (Programmatic Tool Calling and Code Execution) systems for AI Agents. Replaces token-heavy JSON tool dumps with sandboxed code execution (TypeScript/JavaScript, Python, Rhai, Bash), compressing hundreds of MCP/API tools into 2-3 primitives (search, describe, execute) with up to 90% token reduction and 1-turn multi-step batching. Use when designing Code Mode harnesses, building programmatic tool bridges, replacing repetitive MCP tool-calling loops with code actions, or configuring secure VM/WASM/Docker execution sandboxes.
---

# Code Mode Builder ⚡💻🧩
> *by GM Charles Corrêa — Ecossistema Skills AI*  
> **Status: Beta (v0.1.0-beta)**  
> **Conceito Central:** Programmatic Tool Calling & Code-as-Action (CodeAct)

---

## 🇺🇸 English

### 📌 Overview & Philosophy

**Code Mode Builder** is the definitive architecture suite and engineering guide for building, adopting, and orchestrating **Code Mode** (also known as *Programmatic Tool Calling* or *Code-as-Action / CodeAct*) in AI agents.

As established by **Anthropic** (*Code Execution with MCP*), **Cloudflare** (*Code Mode & Workers*), **Apple** (*CodeAct*), **Thoughtworks Radar**, and the **Universal Tool Calling Protocol (UTCP)**:
> *"LLMs excel at writing structured code, but degrade rapidly when forced into multi-turn sequential JSON tool-calling loops."*

Instead of flooding the agent's context window with dozens of tool schemas (costing 5,000 to 30,000+ tokens on every turn) and executing 10 to 20 round-trips for multi-step workflows, **Code Mode condenses the entire API/MCP catalog into 2 or 3 lightweight primitives (`search`, `describe`, `execute`)**. The agent writes a single sandboxed script that calls methods, filters datasets, and processes logic in-memory, returning only the final synthesized result into the conversation context.

---

### 📊 Benchmark Comparison: Traditional Tool Calling vs. Code Mode

| Metric / Cenário | Traditional JSON Tool Calling | Code Mode (Programmatic) | Ganho / Eficiência |
|---|---|---|:---:|
| **Context Overhead** | 50 a 300+ esquemas JSON por prompt | 2 a 3 ferramentas (`search` + `execute`) | **-80% a -95% tokens** |
| **Paging & Filtering (ex: 50 arquivos/registros)** | 50 round-trips LLM (Turnos repetitivos) | 1 script em lote (`map()`, `filter()`, `reduce()`) | **1 única rodada** |
| **Complex Workflows (8+ operações)** | 16 iterações sucessivas | 1 execução paralela (`Promise.all`) | **88% mais rápido** |
| **Custo de API em Produção** | Custos crescentes com re-ingestão de prompt | Resposta final sintetizada | **Até 5.7x mais econômico** |
| **Manipulação de Dados Intermediários** | Payload intermediário polui o contexto | Processado diretamente na memória do sandbox | **Zero poluição de contexto** |

---

### 🏗️ Os 3 Padrões Canônicos de Implementação do Code Mode

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       Arquiteturas de Code Mode Suportadas                  │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ 1. Code Mode Gateway MCP     │ 2. In-Process Sandbox        │ 3. Native CLI │
│    (Cloudflare / UTCP)       │    (Node VM / QuickJS WASM)  │    (Rhai Rust)│
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ • Servidor MCP com 2 ferramentas:│ • Script executado em VM     │ • Binário     │
│   `search` + `execute`.      │   isolada sem rede externa.  │   compilado.  │
│ • Expõe upstream tools como  │ • Suporte a TypeScript/JS    │ • Zero deps,  │
│   globais no script (`await  │   com tipos estritos (.d.ts).│   executa via │
│   github.get_pr()`).         │ • Timeout e quotas de RAM.   │   Bash host.  │
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

#### Padrão A: O Gateway MCP de 2 Ferramentas (`search` & `execute`)
1. **`search(query)`**: Busca semântica ou por palavra-chave no catálogo de ferramentas do servidor. Retorna apenas as assinaturas TypeScript/Python dos 2-3 métodos necessários para a tarefa imediata.
2. **`execute(code)`**: Recebe o código gerado pelo modelo, compila e executa em ambiente sandbox onde cada ferramenta upstream é acessível como uma função global assíncrona (`await database.query(...)`, `await slack.send(...)`).

#### Padrão B: Sandbox Embutido com Tipagem Estrita (TypeScript / Python)
- Injeta interfaces `.d.ts` ou classes tipadas (Pydantic / Dataclasses).
- O modelo aproveita a tipagem estrita para encadear operações (`Promise.all`, destructuring, transformações funcionais).

#### Padrão C: Sandboxing Físico e Limites de Segurança
- **Ambientes Recomendados:**
  - **QuickJS / WebAssembly:** Leve, zero-network por padrão, sem acesso a filesystem host.
  - **Node.js Isolates / V8 Contexts:** Isolamento de contexto sem bindings nativos.
  - **Docker / OCI Containers:** Para fluxos que exigem ferramentas de compilação ou execução de shell com isolamento de kernel.
- **Limites Obrigatórios:** Timeout rígido (ex: 15-30s), limite de memória (ex: 256MB/512MB), e quotas de saída (`max-output`).

---

## 🚨 Diretrizes Mandatórias para Agentes de IA

Quando esta skill estiver ativa ou o usuário pedir para aplicar Code Mode:

### 1. Pensamento "Code-First" (Código como Ação)
- Em vez de disparar ferramentas atômicas repetidas vezes (ex: listar pastas -> ler arquivo 1 -> ler arquivo 2 -> ler arquivo 3), o agente **DEVE gerar um script consolidado** que realiza a iteração em lote e processa os dados antes de retornar.
- Nunca retorne JSONs brutos gigantescos de 500 linhas para o contexto quando apenas uma agregação (soma, contagem, filtro booleano) é solicitada.

### 2. Tratamento de Credenciais Fora do Sandbox (The Gate Pattern)
- **O script NUNCA deve ter acesso a tokens, chaves de API ou segredos brutos.**
- As ferramentas registradas no sandbox invocam funções de host (*Gate*). O injetor de autenticação atua no host, fora do alcance da linguagem de script executada pelo modelo.

### 3. Fail-Safe com `isError: true` e Observabilidade
- O runtime de Code Mode deve capturar `stdout`, `stderr` e exceções não tratadas.
- Se o script falhar, retorne um diagnóstico limpo com `isError: true`, traceback estruturado e as linhas relevantes para que o agente possa corrigir a sintaxe em uma única iteração.

---

## 🛠️ Scaffolding & Scripts Disponíveis

A skill fornece um kit inicial de geração de servidores e harnesses Code Mode:

```bash
# 1. Gerar boilerplate de Servidor MCP Code Mode em TypeScript/Node.js:
python code-mode-builder/scripts/scaffold_code_mode.py --type ts-mcp --name "meu-code-gateway"

# 2. Gerar boilerplate em Python com Sandbox:
python code-mode-builder/scripts/scaffold_code_mode.py --type python-sandbox --name "py-codemode"

# 3. Diagnosticar ambiente de execução (Node.js, Python, QuickJS, uv):
python code-mode-builder/scripts/check_codemode_env.py
```

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral & Filosofia

O **Code Mode Builder** é a suíte de arquitetura para implementar **Code Mode** (Chamada Programática de Ferramentas / Code-as-Action) em agentes de inteligência artificial.

Em vez de sobrecarregar a janela de contexto com centenas de definições de ferramentas JSON estáticas e forçar o agente a fazer dezenas de turnos de requisições lentas, **o Code Mode fornece apenas 2 ferramentas (`search` e `execute`)**. O agente escreve um script que roda em sandbox seguro, orquestra múltiplos métodos em lote, filtra coleções na memória e devolve apenas o resultado final limpo.

### 🌟 Principais Vantagens
- **Economia Drástica de Tokens:** Redução de até 95% do overhead de esquemas no contexto.
- **Orquestração Paralela:** Uso natural de `Promise.all` ou concorrência assíncrona.
- **Segurança Reforçada:** O sandbox não expõe o sistema de arquivos do host nem chaves de API ao código dinâmico.

