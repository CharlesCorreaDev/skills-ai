# Arquitetura dos 10 Subagentes Especializados — MCP Builder 🔌🛠️
## Gerador, Blindador e Orquestrador Universal de Servidores MCP — by GM Charles Corrêa

A suíte **MCP Builder** opera em linha de montagem com especialistas dedicados para erradicar prompt injection, vazamento de chaves de API, tipos fracos e incompatibilidade de IDEs:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Showrunner & Orquestrador MCP]
    
    Showrunner --> SpecHandoff[2. Engenheiro de Specs & OpenAPI/MCP]
    
    SpecHandoff --> ProtocolDev[3. Engenheiro de Protocolo JSON-RPC 2.0 & Stdio/SSE]
    
    ProtocolDev --> PolyglotDev[4. Desenvolvedor Poliglota TS/PHP/Python/Go/Rust]
    
    PolyglotDev --> SecurityShield[5. Blindador contra Prompt Injection & Secrets]
    PolyglotDev --> TypingSastAuditor[6. Auditor de Tipagem Estrita & SAST L9/Mypy]
    
    SecurityShield & TypingSastAuditor --> IdeTester[7. Engenheiro de Conectividade Multi-IDE Claude/Cursor/Antigravity]
    
    IdeTester --> QABenchmarker[8. Engenheiro de QA, Stress Test & Latência]
    
    QABenchmarker --> ReleaseGatekeeper[9. Guardião de Versões & SemVer 2.0.0]
    
    ReleaseGatekeeper --> TechnicalWriter[10. Redator Técnico & Documentador Bilíngue EN/PT-BR]
    
    TechnicalWriter --> SpecHandoff
    SpecHandoff --> OutputFinal([Servidor MCP Seguro, Blindado, Testado e Homologado])
`

---

## 🏛️ Papéis e Responsabilidades dos 10 Subagentes

1. **Showrunner & Orquestrador MCP:** Entrevista o desenvolvedor, delimita fontes de dados (APIs, DBs, arquivos) e orquestra o pipeline.
2. **Engenheiro de Specs & OpenAPI/MCP:** Modela schemas JSON Schema estritos, nomeação de tools sem ambiguidade e descrições semânticas para LLMs.
3. **Engenheiro de Protocolo JSON-RPC 2.0 (Stdio & SSE):** Implementa o ciclo de transporte, tratamento assíncrono de mensagens e multiplexação.
4. **Desenvolvedor Poliglota (TS, PHP 8.4+, Python 3.12+, Go, Rust):** Implementa os handlers nativos de ferramentas e recursos com alta velocidade.
5. **Blindador de Segurança (Security Shield):** Contenção contra Prompt Injection indireto, validação de inputs e proteção de variáveis de ambiente.
6. **Auditor de Tipagem Estrita & SAST:** Valida estaticamente TypeScript strict, PHPStan Level 9, Mypy strict e auditoria Bandit.
7. **Engenheiro de Conectividade Multi-IDE:** Valida integração e gera arquivos de configuração para Claude Desktop, Antigravity, Cursor e VS Code.
8. **Engenheiro de QA, Stress Test & Latência:** Executa benchmarks de tempo de resposta (<50ms em stdio), concorrência e resiliência a timeouts.
9. **Guardião de Versões & SemVer 2.0.0:** Controla a semântica de versionamento de tools e backward compatibility.
10. **Redator Técnico & Documentador Bilíngue:** Gera READMEs de instalação, documentação de tools e exemplos de prompts em EN e PT-BR.
