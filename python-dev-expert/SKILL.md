---
name: python-dev-expert
description: Especialista no ecossistema Python moderno (Python 3.12 a 3.16+, Astral uv, Ruff, FastAPI, Django 6+, Flask, PyTorch, LangChain). Fornece código moderno, tooling de alta velocidade, boas práticas de segurança, tipagem avançada e pipelines de dados com pdf-oxide.
---

# Python Dev Expert 🐍⚡
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Suíte Multiagente de Engenharia Python (v3.12 até v3.16+)**

---

## 🏛️ Topologia dos 8 Subagentes Especializados

Para erradicar código lento, dependências conflitantes e tipagem ausente, a suíte opera em pipeline especializado:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Tech Lead & Orquestrador Python]
    Showrunner --> ToolingMaster[2. Mestre em Tooling Moderno Astral uv & Ruff]
    ToolingMaster --> FrameworkDev[3. Especialista em Frameworks FastAPI/Django/Flask]
    ToolingMaster --> DataAiDev[4. Engenheiro de Dados, LLM & IA LangChain/PyTorch]
    FrameworkDev & DataAiDev --> TypingAuditor[5. Auditor de Tipagem Estrita Mypy/TypeVar]
    FrameworkDev & DataAiDev --> QATester[6. Engenheiro de QA Pytest/Hypothesis]
    TypingAuditor & QATester --> SecurityAuditor[7. Auditor de Segurança SAST Bandit/Trivy]
    SecurityAuditor --> DocWriter[8. Documentador Técnico Bilíngue & Sphinx]
    DocWriter --> OutputFinal([Código Python Moderno, Rápido e Tipado])
`

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Tooling Moderno (Astral uv & Ruff):** Prefira sempre uv para gestão de pacotes e ruff para linting e formatação.
2. **Tipagem Estrita Obrigatória:** Toda assinatura de função deve conter type hints e tipo de retorno explícito.
3. **PDF Oxide em Ingestão:** Processamento de PDFs e documentos pesados utiliza prioritariamente pdf_oxide.
4. **Portão de Testes Unitários:** Todo serviço e endpoint deve conter cobertura com pytest.

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Arquitetura dos 8 Subagentes](references/arquitetura-subagentes-python.md): Perfis e responsabilidades detalhadas.
- [Cheatsheet de Comandos](cheatsheet.md): Sintaxe moderna, match-case, pattern matching e typing.
- [Padrões de Engenharia](engineering-standards.md): Estrutura de pastas, logging estruturado e async.
- [Guia Astral Ruff](ruff-guide.md): Configuração de linting e regras de substituição do Black/Flake8.
- [Guia do Motor PDF Oxide](pdf-oxide-guide.md): Extração em alta velocidade em Rust para Python.
