---
name: python-dev-expert
description: Especialista no ecossistema Python moderno (Python 3.12 a 3.16+, Astral uv, Ruff, FastAPI, Django 6+, Flask, PyTorch, LangChain). Orquestra 11 subagentes especializados cobrindo Specs, PRs, SSD & Handoff Assíncronas, Tooling Astral (uv/ruff), Frameworks Web, Dados/IA (pdf-oxide/LangChain), CLI Typer, Tipagem Estrita Mypy, QA com Pytest, Auditoria SAST Bandit, SemVer e Documentação Técnica Bilíngue (EN/PT-BR).
---

# Python Dev Expert 🐍⚡
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Suíte Federada de 11 Subagentes para Python (0.6.0-beta)**

---

## 🏛️ Topologia dos 11 Subagentes Especializados

Para erradicar código lento, dependências conflitantes e tipagem ausente:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Tech Lead & Orquestrador Python]
    Showrunner --> SpecArchitect[2. Specs, PRs, SSD & Handoff Arquitetura Assíncrona]
    SpecArchitect --> ToolingMaster[3. Tooling Astral uv & Ruff]
    ToolingMaster --> FrameworkDev[4. Frameworks FastAPI/Django/Flask]
    ToolingMaster --> DataAiDev[5. Dados, LLM & IA pdf-oxide/PyTorch]
    ToolingMaster --> CliAutomationDev[6. Scripts CLI & Automação Typer]
    FrameworkDev & DataAiDev & CliAutomationDev --> TypingAuditor[7. Tipagem Estrita Mypy strict]
    FrameworkDev & DataAiDev & CliAutomationDev --> QATester[8. QA & Testes Pytest/Hypothesis]
    TypingAuditor & QATester --> SecurityAuditor[9. Auditor SAST Bandit/pip-audit]
    SecurityAuditor --> ReleaseGatekeeper[10. Guardião SemVer 2.0.0]
    ReleaseGatekeeper --> TechnicalWriter[11. Documentador Bilíngue EN/PT-BR]
    TechnicalWriter --> SpecArchitect
    SpecArchitect --> OutputFinal([Código Python Moderno, Rápido e Tipado])
`

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Tooling Moderno (Astral uv & Ruff):** Prefira sempre uv para pacotes e ruff para linting e formatação.
2. **Tipagem Estrita Obrigatória:** Toda assinatura de função deve conter type hints e tipo de retorno explícito.
3. **PDF Oxide em Ingestão:** Processamento de PDFs e documentos pesados utiliza prioritariamente pdf_oxide.
4. **SemVer 2.0.0 (PT-BR) & Padrão Bilíngue:** Releases e documentações estritamente em EN e PT-BR.
5. **Portão de Testes Unitários:** Todo serviço e endpoint deve conter cobertura com pytest.

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Arquitetura dos 11 Subagentes](references/arquitetura-subagentes-python.md): Perfis e responsabilidades detalhadas.
- [Cheatsheet de Comandos](cheatsheet.md): Sintaxe moderna, match-case, pattern matching e typing.
- [Padrões de Engenharia](engineering-standards.md): Estrutura de pastas, logging estruturado e async.
- [Guia Astral Ruff](ruff-guide.md): Configuração de linting e regras de substituição do Black/Flake8.
- [Guia do Motor PDF Oxide](pdf-oxide-guide.md): Extração em alta velocidade em Rust para Python.
