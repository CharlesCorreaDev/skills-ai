# Arquitetura Multiagente — MCP Builder 🔌🛠️

Para gerar, blindar e auditar servidores Model Context Protocol (MCP) com total segurança e zero alucinações de API, a suíte opera com **7 Subagentes Especializados**:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Orquestrador de Protocolo MCP]
    Showrunner --> ProtocolArchitect[2. Arquiteto de Ferramentas & Recursos]
    ProtocolArchitect --> PolyglotDev[3. Desenvolvedor Poliglota TS/PHP/Python/Go/Rust]
    PolyglotDev --> SecurityShield[4. Blindador de Segurança & Prompt Injection]
    PolyglotDev --> SastAuditor[5. Auditor SAST & Validador de Tipos]
    SecurityShield & SastAuditor --> IntegrationVerifier[6. Verificador de IDEs Claude/Cursor/Antigravity]
    IntegrationVerifier --> ReleaseSigner[7. Publicador SemVer & Guardião de Versões]
    ReleaseSigner --> OutputFinal([Servidor MCP Seguro, Testado e Homologado])
`

## Papéis e Responsabilidades dos 7 Subagentes:

1. **Orquestrador de Protocolo MCP (Showrunner):**
   - Coordena o pipeline do MCP Builder, mapeando contratos JSON-RPC 2.0 e orquestrando o scaffolding.
2. **Arquiteto de Ferramentas, Recursos & Prompts:**
   - Define a especificação OpenAPI/MCP, nomeação semântica de tools, schemas JSON Schema estritos e descrições claras para as LLMs.
3. **Desenvolvedor Poliglota (TypeScript, PHP 8.4+, Python 3.12+, Go, Rust):**
   - Implementa o servidor utilizando SDKs nativos oficiais ou stdio/SSE robustos com tratamento assíncrono de exceções.
4. **Blindador de Segurança (Security Shield):**
   - Protege contra Prompt Injection indireto, validação estrita de inputs, path traversal e vazamento de variáveis de ambiente (.env).
5. **Auditor SAST & Validador de Tipos:**
   - Executa análise estática de segurança (SAST) e valida conformidade estrita de tipagem (TypeScript strict, PHPStan L9, Mypy).
6. **Verificador de Integração com IDEs:**
   - Gera e testa as configurações de conexão (claude_desktop_config.json, .gemini/settings.json, .cursor/mcp.json).
7. **Publicador SemVer & Guardião de Versões:**
   - Valida conformance do manifesto, controle de versão SemVer 2.0.0 e monitoramento de atualizações do protocolo.
