---
name: mcp-builder
description: Gerador, blindador de segurança e configurador universal de servidores Model Context Protocol (MCP) para PHP 8.4+, Python 3.12+, Node.js 22+, TypeScript 5+, Go 1.22+ e Rust 2021+. Constrói MCPs nativos a partir de documentações ou contexto, implementa contenção rigorosa contra prompt injection e vazamento de segredos, valida código com análise estática (SAST), possui mecanismo fail-safe com abertura automática de issues no GitHub e monitora atualizações da skill. Use quando o usuário quiser criar um servidor MCP para qualquer API/sistema, configurar MCPs externos nas suas IDEs ou reforçar a segurança de ferramentas de IA.
---

# MCP Builder 🔌🛠️
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Suíte Multiagente de Criação & Blindagem MCP (0.5.0-beta)**

---

## 🏛️ Topologia dos 7 Subagentes Especializados

Para erradicar falhas de protocolo, vulnerabilidades de injeção e incompatibilidade de IDEs, a suíte atua de forma orquestrada:

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

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Blindagem de Segurança Obrigatória:** Sanitização absoluta contra Prompt Injection e vazamento de credenciais (.env).
2. **Schema JSON Estrito:** Toda ferramenta exportada deve definir propriedades, descrições claras e campos obrigatórios (
equired).
3. **Padrão Multi-IDE:** Forneça blocos de configuração prontos para Claude Desktop, Antigravity, Cursor e VS Code.
4. **Portão de Auditoria SAST:** Nenhum servidor MCP é entregue sem passar por checagem estática de código e tipagem.

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Arquitetura dos 7 Subagentes](references/arquitetura-subagentes-mcp-builder.md): Papéis e especialidades detalhadas.
- [Cheatsheet de Comandos](cheatsheet.md): Snippets rápidos para TypeScript, Python e PHP.
- [Padrões de Arquitetura & Segurança](patterns.md): Modelos de transporte Stdio/SSE e sanitização.
- [Glossário Canônico](glossary.md): Termos fundamentais da especificação MCP.
- [Módulos de Segurança](security/): Defesas contra injeção e blindagem de transporte.
- [Adaptadores Multi-Linguagem](adapters/): Scaffolding para Node, Python, PHP, Rust e Go.
