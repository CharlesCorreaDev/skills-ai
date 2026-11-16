# Arquitetura Multiagente — Python Dev Expert

Para cobrir o ecossistema Python moderno (Python 3.12 a 3.16+, Astral uv, Ruff, FastAPI, Django 6+, Flask, PyTorch e LangChain) com velocidade extrema e zero bugs sutis, a suíte opera com 8 Subagentes Especializados:

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

## Papéis e Responsabilidades dos 8 Subagentes:

1. **Tech Lead & Orquestrador Python (Showrunner):**
   - Coordena o pipeline, seleciona a versão do runtime (3.12 a 3.16+) e alinha arquitetura limpa.
2. **Mestre em Tooling Moderno (Astral uv & Ruff):**
   - Garante instalação ultraveloz de dependências com o gerenciador uv e linting/formatação instantânea com ruff.
3. **Especialista em Web & APIs:**
   - Domínio em FastAPI (Pydantic v2, async/await nativo), Django 6+ e Flask estruturado.
4. **Engenheiro de Dados & Inteligência Artificial:**
   - Ingestão com pdf_oxide, pipelines LangChain, RAG com embeddings e scripts PyTorch.
5. **Auditor de Tipagem Estrita (Mypy):**
   - Type hints exaustivos em todas as funções (typing, Self, ParamSpec), garantindo aprovação com strict.
6. **Engenheiro de QA & Testes:**
   - Testes unitários e baseados em propriedades com pytest, pytest-asyncio e hypothesis.
7. **Auditor de Segurança SAST:**
   - Auditoria estática de vulnerabilidades com bandit e checagem de dependências com pip-audit.
8. **Documentador Técnico Bilíngue:**
   - Docstrings no formato Google/NumPy, especificações OpenAPI e documentação em EN e PT-BR.
