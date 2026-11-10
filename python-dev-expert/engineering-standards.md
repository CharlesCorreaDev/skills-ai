# Modern Python Engineering Standards & SOTA Patterns 🐍💎
# Padrões Canônicos de Engenharia Pythonica & Melhores Práticas da Comunidade

> *Módulo Integrado para `python-dev-expert`*  
> **Fontes & Referências SOTA Integradas:**
> - `rishapgandhi/python-skills` & `JoseVelazcoH/python-skills`: AI-SDLC rigoroso, tipagem total e `pydantic-settings`.
> - `mrKazzila/python-structured-logging-skill`: Logging estruturado em JSON com `structlog`.
> - `swoiow/python-pro-guide` & `MiniPrincipal/Coding-Agent-Skills`: Padrões de engenharia para agentes de IA e arquivos `AGENT.md`.
> - `Trail of Bits Security Skills`: Auditoria avançada com Semgrep e CodeQL.
> - `Test-Driven Development (TDD)`: Ciclo Red-Green-Refactor, Tracer Bullets e De-Sloppify.
> - `Systematic Debugging`: Hipótese científica, isolamento de reprodução e tracing.
> - `Impeccable & XLSX`: Rigor em planilhas (`pandas`/`openpyxl`) e anti-slop visual.
> - `Last30Days`: Validação temporal e pesquisa recente em fontes reais.

---

## 🇺🇸 English

### 1. Test-Driven Development (TDD) Protocol
1. **Red Phase:** Always write a failing test first that specifies the requirement or bug condition before touching business code.
2. **Green Phase:** Write the minimal possible implementation to make the test pass cleanly.
3. **Refactor & De-Sloppify:** Remove boilerplate, unnecessary prints, unused variables, and redundant type casts. Run test suite to ensure green bar is preserved.

### 2. Systematic Debugging Methodology
- **Rule 1: Never guess or patch randomly.** Formulate an explicit hypothesis based on stack traces and log state.
- **Rule 2: Minimal Reproducible Case:** Isolate the failing boundary into a standalone test function.
- **Rule 3: Scientific Verification:** Confirm the root cause by observing failure, applying the single targeted fix, and validating that edge cases pass.

### 3. Production Structured Logging (`structlog`)
Ditch unstructured `print()` or basic string logging in production. Use structured, machine-queryable JSON logs:

```python
import structlog

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.processors.JSONRenderer()
    ],
    wrapper_class=structlog.make_filtering_bound_logger(20), # INFO
    context_class=dict,
    logger_factory=structlog.PrintLoggerFactory(),
)

logger = structlog.get_logger()
# Usage:
logger.info("order_processed", order_id="ORD-9421", amount=1450.00, user_id=42)
```

### 4. Configuration & Environment Management (`pydantic-settings`)
Never use bare `os.environ.get()` scattered across code. Centralize strongly-typed environment variables:

```python
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field, SecretStr

class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    app_name: str = "MinhaApp"
    environment: str = Field(default="production", pattern="^(development|staging|production)$")
    database_url: SecretStr
    debug: bool = False

settings = AppSettings()
```

### 5. High-Performance Spreadsheet Handling (`xlsx` / `openpyxl` / `pandas`)
- For read-only high-volume data: use `openpyxl.load_workbook(..., read_only=True)`.
- For analytical data pipelines: use vectorized `pandas` or `polars`.

---

## 🇧🇷 Português (Brasil)

### 1. Protocolo de Desenvolvimento Guiado por Testes (TDD)
- **Ciclo Red-Green-Refactor:** Toda nova funcionalidade ou correção de bug DEVE começar com um teste que falha no `pytest`.
- **Vertical Slicing (Tracer Bullets):** Crie testes ponta a ponta reais sem excesso de mocks artificiais que mascarem o comportamento do sistema.
- **De-Sloppify:** Limpeza automática de comentários óbvios, logs descartáveis e blocos de código mortos após os testes passarem.

### 2. Depuração Sistemática (Systematic Debugging)
- **Proibição de Tentativa e Erro Cega:** O agente nunca deve chutar correções aleatórias.
- **Passo 1:** Analisar o traceback completo e identificar a fronteira exata da falha.
- **Passo 2:** Isolar em um caso mínimo de reprodução.
- **Passo 3:** Criar a hipótese de causa raiz, aplicar a correção cirúrgica e provar a resolução com teste de regressão.

### 3. Logging Estruturado em Produção (`structlog`)
Substitua `print()` por logs JSON estruturados com carimbo de data/hora ISO, níveis semânticos e contexto acoplado para observability (Datadog, CloudWatch, Grafana Loki).

### 4. Auditoria de Segurança com Semgrep e CodeQL (Trail of Bits Standard)
- Utilize regras estáticas do Semgrep para detectar vulnerabilidades OWASP Top 10 antes do commit.
- Integre verificação com `pip-audit` e `bandit` em todo pipeline CI/CD.

