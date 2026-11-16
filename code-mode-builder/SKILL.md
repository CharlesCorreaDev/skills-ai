---
name: code-mode-builder
description: Architect, builder, and orchestrator of Code Mode (Programmatic Tool Calling and Code Execution) systems for AI Agents. Condenses hundreds of MCP/API tools into 2-3 primitives (search, describe, execute) with up to 90% token reduction and 1-turn multi-step batching. Orquestra 10 subagentes cobrindo Specs/PRs/SSD/Handoff CodeAct, Compressao de APIs, Sandboxing WASM/VM, Gate Pattern de Seguranca, Runtimes TS/Python, Benchmarks, QA e Documentacao Bilingue.
---

# Code Mode Builder ⚡💻🧩
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Suíte Federada de 10 Subagentes para Code Mode (v0.2.0-beta)**

---

## 🏛️ Topologia dos 10 Subagentes Especializados

Para erradicar loops repetitivos de ferramentas JSON, desperdício de tokens e lentidão de chamadas atômicas:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Showrunner & Orquestrador CodeAct]
    Showrunner --> SpecHandoff[2. Specs, PRs, SSD & Handoff Primitivas CodeAct]
    SpecArchitect --> ApiCompressor[3. Compressao de APIs & Tipos .d.ts]
    ApiCompressor --> SandboxEngineer[4. Sandboxing WASM/QuickJS/Node VM]
    SandboxEngineer --> SecurityGatekeeper[5. Blindador & Gate Pattern]
    SandboxEngineer --> MultiLangRuntime[6. Runtimes TS/JS/Python/Rhai]
    SecurityGatekeeper & MultiLangRuntime --> TokenBenchmarker[7. Eficiencia de Tokens & Latencia]
    TokenBenchmarker --> QATester[8. QA & Resiliencia/Timeouts]
    QATester --> ReleaseGatekeeper[9. Guardiao SemVer 2.0.0]
    ReleaseGatekeeper --> TechnicalWriter[10. Documentador Bilingue EN/PT-BR]
    TechnicalWriter --> SpecArchitect
    SpecArchitect --> OutputFinal([Harness Code Mode Testado e Homologado])
`

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Pensamento Code-First:** Agrupe operações e paginações em scripts em lote em vez de disparar chamadas atômicas sucessivas.
2. **Gate Pattern de Segurança Obrigatório:** O script no sandbox NUNCA acessa segredos brutos; a autenticação reside estritamente no host.
3. **Fail-Safe com isError: true:** Capture stdout, stderr e tracebacks limpos para permitir autocorreção em um único turno.
4. **SemVer 2.0.0 (PT-BR) & Padrão Bilíngue:** Releases e documentações estritamente em EN e PT-BR.
5. **Portão de Sandboxing & Quotas:** Todo runtime deve impor limites de memória (ex: 256MB), timeout (15-30s) e saída máxima.

---

## 🔗 Protocolo de Skills Companheiras
`ash
npx skills@latest add noobygains/godmode
npx skills@latest add addyosmani/agent-skills --skill=spec-driven-development
npx skills@latest add mattpocock/skills --skill=grill-me
npx skills@latest add mattpocock/skills --skill=handoff
npx skills@latest add mattpocock/skills --skill=tdd
npx skills@latest add aihero-dev/skills-code-review
npx skills@latest add multica-ai/andrej-karpathy-skills
npx skills@latest add cloudflare/security-audit-skill
npx skills@latest add NVIDIA/auto-ontology
`

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Arquitetura dos 10 Subagentes](references/arquitetura-subagentes-code-mode.md): Perfis e responsabilidades de cada especialista.
- [Guia Canônico de Arquitetura Code Mode](references/guia-arquitetura-code-mode.md): Padrões de implementação Gateway MCP, In-Process VM e WASM.
- [Templates de Scaffolding](templates/): Boilerplates para Node.js VM, QuickJS e Python.
- [Scripts de Execução e Benchmarks](scripts/): Utilitários de teste e medição de tokens.
