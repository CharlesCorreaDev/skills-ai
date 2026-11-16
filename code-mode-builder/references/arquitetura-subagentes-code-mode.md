# Arquitetura dos 10 Subagentes Especializados — Code Mode Builder ⚡💻🧩
## 10 Specialized Subagents Architecture — Code Mode Builder

A suíte **Code Mode Builder** opera em linha de montagem com 10 especialistas dedicados para substituir dumps massivos de ferramentas JSON por execução programática em lote (search, describe, xecute), reduzindo até 90% dos tokens com execução atômica em 1 turno.

The **Code Mode Builder** suite operates as an assembly line of 10 dedicated specialists to replace massive JSON tool dumps with programmatic batch execution (search, describe, xecute), saving up to 90% of tokens with 1-turn atomic execution.

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor / User]) --> Showrunner[1. Showrunner & Orquestrador CodeAct]
    
    Showrunner --> SpecHandoff[2. Engenheiro de Specs, PRs, SSD & Handoff Primitivas CodeAct]
    
    SpecArchitect --> ApiCompressor[3. Especialista em Compressão de APIs & Tipos .d.ts]
    
    ApiCompressor --> SandboxEngineer[4. Engenheiro de Sandboxing WASM/QuickJS/Node VM/Docker]
    
    SandboxEngineer --> SecurityGatekeeper[5. Blindador de Segurança & Gate Pattern Segredos Fora]
    SandboxEngineer --> MultiLangRuntime[6. Especialista em Runtimes TS/JS/Python/Rhai]
    
    SecurityGatekeeper & MultiLangRuntime --> TokenBenchmarker[7. Analista de Eficiência de Tokens & Latência]
    
    TokenBenchmarker --> QATester[8. Engenheiro de QA & Testes de Resiliência/Timeouts]
    
    QATester --> ReleaseGatekeeper[9. Guardião de Versões & SemVer 2.0.0]
    
    ReleaseGatekeeper --> TechnicalWriter[10. Redator Técnico & Documentador Bilíngue EN/PT-BR]
    
    TechnicalWriter --> SpecArchitect
    SpecArchitect --> OutputFinal([Harness Code Mode Seguro, Rápido, Testado e Homologado])
`

---

## 🇧🇷 Português (Brasil) — Papéis e Responsabilidades dos 10 Subagentes

1. **Showrunner & Orquestrador CodeAct:** Entrevista o usuário via grill-me, delimita fluxos repetitivos de chamadas de ferramentas e define a estratégia de sandboxing.
2. **Engenheiro de Specs, PRs, SSD & Handoff (Primitivas search/describe/xecute):** Formaliza Tech Specs de Code Mode, diagramas de sequência de sandbox (SSD), documentação de PRs e guias de handoff, além de  Modela o contrato canônico do gateway, condensando centenas de ferramentas em 2-3 primitivas leves.
3. **Especialista em Compressão de APIs & Tipos (.d.ts / Pydantic):** Gera definições de tipos compactas e expressivas para que a LLM compreenda o catálogo sem sobrecarga de tokens.
4. **Engenheiro de Sandboxing (WASM, QuickJS, Node VM, Docker):** Configura os isolamentos de execução em memória, cotas de CPU/RAM, limites de saída e timeouts rígidos.
5. **Blindador de Segurança & Gate Pattern:** Garante que chaves de API, credenciais e conexões ao host fiquem no host (*Gate*), nunca acessíveis pelo script executado.
6. **Especialista em Runtimes Multi-Linguagem:** Implementa harnesses para TypeScript/JavaScript, Python, Rhai (Rust) e Bash com captura estruturada de stdout/stderr.
7. **Analista de Eficiência de Tokens & Latência:** Mede reduções de tokens (-80% a -95%) e ganho de velocidade (1 turno em vez de 10-20 round-trips).
8. **Engenheiro de QA & Testes de Resiliência:** Simula scripts com loops infinitos, exaustão de memória e falhas parciais, validando respostas limpas com isError: true.
9. **Guardião de Versões & SemVer 2.0.0:** Controla a semântica de versionamento do harness e conformidade retrocompatível conforme [semver.org/lang/pt-BR/](https://semver.org/lang/pt-BR/).
10. **Redator Técnico & Documentador Bilíngue:** Produz documentação técnica, manuais de integração para agentes e exemplos práticos em Português e Inglês.

---

## 🇺🇸 English — Roles and Responsibilities of the 10 Subagents

1. **Showrunner & CodeAct Orchestrator:** Interviews the developer via grill-me, isolates repetitive JSON tool calls, and defines sandbox isolation strategy.
2. **Specs, PRs, SSD & Handoff Engineer (CodeAct Primitives):** Authors formal Code Mode Tech Specs, sandbox System Sequence Diagrams (SSD), PR definitions, and handoff guides, along with  Formulates canonical gateway contracts, condensing hundreds of API tools into 2-3 lightweight primitives.
3. **API Compression & Type Definitions Specialist (.d.ts / Pydantic):** Generates compact, strongly typed signatures enabling LLMs to understand catalogs without token overhead.
4. **Sandboxing Engineer (WASM, QuickJS, Node VM, Docker):** Provisions in-memory isolation, CPU/RAM quotas, execution timeouts, and output limits.
5. **Security Gatekeeper & Gate Pattern Architect:** Enforces that raw API credentials, secrets, and host connections remain on the host (*Gate*), inaccessible to the executed script.
6. **Multi-Language Runtime Specialist:** Implements execution harnesses for TypeScript/JavaScript, Python, Rhai (Rust), and Bash with structured stdout/stderr logging.
7. **Token Efficiency & Latency Benchmarker:** Measures token savings (-80% to -95%) and latency speedups (1-turn batching vs. 10-20 sequential round-trips).
8. **QA & Resilience Engineer:** Tests edge cases (infinite loops, memory exhaustion, partial failures) ensuring clean error handling with isError: true.
9. **Release Gatekeeper & SemVer 2.0.0 Guardian:** Manages SemVer releases and backwards compatibility according to [semver.org](https://semver.org/).
10. **Bilingual Technical Writer (EN / PT-BR):** Produces end-user guides, agent integration manuals, and runnable examples in both English and Brazilian Portuguese.
