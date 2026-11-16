# Arquitetura dos 11 Subagentes Especializados — Python Dev Expert
## 11 Specialized Subagents Architecture — Python Dev Expert

A suíte Python Dev Expert opera sob o padrão de Engenharia Federada em Linha de Montagem, integrando o ecossistema Python moderno com Astral uv, Ruff, tipagem estrita Mypy, frameworks assíncronos, pipelines de IA com pdf-oxide e suítes completas de testes.

The Python Dev Expert suite operates under a federated assembly line engineering model, integrating the modern Python ecosystem with Astral uv, Ruff, strict Mypy typing, asynchronous frameworks, AI pipelines with pdf-oxide, and comprehensive test suites.

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor / User]) --> Showrunner[1. Tech Lead & Orquestrador Python]
    Showrunner --> SpecArchitect[2. Specs & Arquitetura Assíncrona]
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

## 🇧🇷 Português (Brasil) — Papéis e Responsabilidades dos 11 Subagentes

1. **Tech Lead & Orquestrador Python (Showrunner):** Entrevista o usuário via grill-me, delimita versões do runtime (3.12 a 3.16+) e governa o pipeline.
2. **Engenheiro de Specs, PRs, SSD & Handoff (Arquitetura Assíncrona):** Modela Tech Specs/RFCs, diagramas de sequência (SSD), documentação de PRs e guias de handoff salvos em memória perene, além de  Modela schemas Pydantic v2, design patterns assíncronos (asyncio) e fluxos de dados.
3. **Mestre em Tooling Moderno (Astral uv & Ruff):** Substitui ferramentas lentas pelo ecossistema Astral (uv para pacotes ultravelozes e ruff para linting instantâneo).
4. **Especialista em Frameworks Web:** Domínio em FastAPI de alta performance, Django 6+ robusto e microserviços Flask.
5. **Engenheiro de Dados, LLM & IA:** Ingestão ultraveloz com pdf_oxide em Rust, RAG com embeddings, LangChain e scripts PyTorch.
6. **Desenvolvedor de Scripts CLI & Automação:** Ferramentas de terminal ergonômicas utilizando Typer, Rich e Click com feedback em tempo real.
7. **Auditor de Tipagem Estrita (Mypy strict):** Exige type hints completos em todas as assinaturas, Generic Types e validação strict.
8. **Engenheiro de QA & Testes Automatizados:** Testes unitários com pytest, fixtures assíncronas e testes baseados em propriedades com hypothesis.
9. **Auditor SAST & Segurança de Pacotes:** Auditoria de vulnerabilidades com bandit e varredura de dependências com pip-audit.
10. **Guardião de Versões & SemVer 2.0.0:** Controle rigoroso de releases de pacotes PyPI e versionamento semântico conforme SemVer 2.0.0 PT-BR (https://semver.org/lang/pt-BR/).
11. **Redator Técnico & Documentador Bilíngue:** Gera docstrings nos formatos Google/NumPy, documentação Sphinx/MkDocs e manuais em EN e PT-BR.

---

## 🇺🇸 English — Roles and Responsibilities of the 11 Subagents

1. **Tech Lead & Python Orchestrator (Showrunner):** Directs specifications via grill-me, sets runtime versions (3.12 through 3.16+), and aligns architectural integrity.
2. **Specs, PRs, SSD & Handoff Engineer (Async Architecture):** Authors Tech Specs, System Sequence Diagrams (SSD), PR bodies, and handoff guides stored in persistent memory, along with  Defines Pydantic v2 data models, asynchronous execution pipelines, and clean API contracts.
3. **Modern Tooling Master (Astral uv & Ruff):** Replaces legacy tooling with the ultra-fast Astral toolchain (uv package management and ruff linting/formatting).
4. **Web Frameworks Specialist:** Expert engineering across high-performance FastAPI, production-ready Django 6+, and lightweight Flask microservices.
5. **Data, LLM & AI Systems Engineer:** Rust-powered pdf_oxide document extraction, LangChain RAG pipelines, and PyTorch deep learning workflows.
6. **CLI Automation Developer:** Authors ergonomic terminal tools and developer utilities using Typer, Rich, and Click with real-time feedback.
7. **Strict Typing Auditor (Mypy strict):** Enforces 100% type annotations, Generics, and strict typing with zero type inference escapes.
8. **QA & Automated Testing Engineer:** Comprehensive testing suites using pytest, asynchronous fixtures, and property-based testing with hypothesis.
9. **SAST Auditor & Package Security Guard:** Automated static security scans with bandit and supply-chain dependency audits with pip-audit.
10. **SemVer 2.0.0 & Release Guardian:** Manages PyPI packaging and strict SemVer versioning adhering to semver.org.
11. **Bilingual Technical Writer (EN / PT-BR):** Produces Google/NumPy docstrings, Sphinx/MkDocs technical docs, and bilingual user guides.
