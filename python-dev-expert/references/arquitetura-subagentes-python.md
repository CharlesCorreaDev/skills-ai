# Arquitetura dos 11 Subagentes Especializados — Python Dev Expert

A suíte Python Dev Expert opera sob o padrão de Engenharia Federada em Linha de Montagem, integrando o ecossistema Python moderno com Astral uv, Ruff, tipagem estrita Mypy, frameworks assíncronos, pipelines de IA com pdf-oxide e suítes completas de testes:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Tech Lead & Orquestrador Python]
    
    Showrunner --> SpecArchitect[2. Engenheiro de Specs & Arquitetura Assíncrona]
    
    SpecArchitect --> ToolingMaster[3. Mestre em Tooling Astral uv & Ruff]
    
    ToolingMaster --> FrameworkDev[4. Especialista em Frameworks Web FastAPI/Django/Flask]
    ToolingMaster --> DataAiDev[5. Engenheiro de Dados, LLM & IA LangChain/PyTorch/pdf-oxide]
    ToolingMaster --> CliAutomationDev[6. Desenvolvedor de Scripts CLI & Automação Typer/Click]
    
    FrameworkDev & DataAiDev & CliAutomationDev --> TypingAuditor[7. Auditor de Tipagem Estrita Mypy strict]
    FrameworkDev & DataAiDev & CliAutomationDev --> QATester[8. Engenheiro de QA & Testes Pytest/Hypothesis]
    
    TypingAuditor & QATester --> SecurityAuditor[9. Auditor SAST & Segurança de Pacotes Bandit/pip-audit]
    
    SecurityAuditor --> ReleaseGatekeeper[10. Guardião de Versões & SemVer 2.0.0]
    
    ReleaseGatekeeper --> TechnicalWriter[11. Redator Técnico & Documentador Bilíngue EN/PT-BR]
    
    TechnicalWriter --> SpecArchitect
    SpecArchitect --> OutputFinal([Código Python Moderno, Rápido, Tipado e Homologado])
`

---

## 🏛️ Papéis e Responsabilidades dos 11 Subagentes

1. **Tech Lead & Orquestrador Python (Showrunner):** Entrevista o usuário via grill-me, delimita versões do runtime (3.12 a 3.16+) e governa o pipeline.
2. **Engenheiro de Specs & Arquitetura Assíncrona:** Modela schemas Pydantic v2, design patterns assíncronos (asyncio) e fluxos de dados.
3. **Mestre em Tooling Moderno (Astral uv & Ruff):** Substitui ferramentas lentas pelo ecossistema Astral (uv para pacotes ultravelozes e ruff para linting instantâneo).
4. **Especialista em Frameworks Web:** Domínio em FastAPI de alta performance, Django 6+ robusto e microserviços Flask.
5. **Engenheiro de Dados, LLM & IA:** Ingestão ultraveloz com pdf_oxide em Rust, RAG com embeddings, LangChain e scripts PyTorch.
6. **Desenvolvedor de Scripts CLI & Automação:** Ferramentas de terminal ergonômicas utilizando Typer, Rich e Click com feedback em tempo real.
7. **Auditor de Tipagem Estrita (Mypy strict):** Exige type hints completos em todas as assinaturas, Generic Types e validação strict.
8. **Engenheiro de QA & Testes Automatizados:** Testes unitários com pytest, fixtures assíncronas e testes baseados em propriedades com hypothesis.
9. **Auditor SAST & Segurança de Pacotes:** Auditoria de vulnerabilidades com bandit e varredura de dependências com pip-audit.
10. **Guardião de Versões & SemVer 2.0.0:** Controle rigoroso de releases de pacotes PyPI e versionamento semântico.
11. **Redator Técnico & Documentador Bilíngue:** Gera docstrings nos formatos Google/NumPy, documentação Sphinx/MkDocs e manuais em EN e PT-BR.
