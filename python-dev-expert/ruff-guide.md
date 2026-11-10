# Ruff - Linter e Formatador Python de Alta Performance (Astral)

O **Ruff** (`docs.astral.sh/ruff`) é o linter e formatador de código Python mais rápido do mundo, desenvolvido em Rust pela **Astral**. Ele substitui de 10 a 100x mais rápido um conjunto enorme de ferramentas tradicionais em Python:
- **Flake8** (e dezenas de plugins como flake8-bugbear, flake8-comprehensions, etc.)
- **Black** (formatação determinística com estilo canônico)
- **isort** (organização automática de imports)
- **pydocstyle** (padronização de docstrings)
- **pyupgrade** (modernização de sintaxe legada para Python 3.10+)
- **autoflake** (remoção de variáveis e imports não utilizados)

---

## ⚡ Instalação e Execução

### 1. Instalação:
```bash
# Via uv (recomendado)
uv add --dev ruff

# Ou via pip / pipx / poetry
pip install ruff
```

### 2. Linting com Auto-Fix:
```bash
# Executar análise estática em todo o projeto
ruff check .

# Corrigir automaticamente todas as violações auto-reparáveis
ruff check --fix .

# Modo contínuo (Watch Mode para desenvolvimento)
ruff check --watch .
```

### 3. Formatação Canônica (Drop-in replacement do Black):
```bash
# Formatar todos os arquivos Python
ruff format .

# Checar se os arquivos estão formatados (ideal para CI/CD e pre-commit)
ruff format --check .
```

---

## ⚙️ Configuração Canônica em Projetos (`pyproject.toml`)

```toml
[tool.ruff]
target-version = "py312"
line-length = 88
indent-width = 4

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # Pyflakes (erros de sintaxe e variáveis não utilizadas)
    "I",      # isort (organização de imports)
    "B",      # flake8-bugbear (bugs comuns e anti-patterns)
    "C4",     # flake8-comprehensions
    "UP",     # pyupgrade (modernização de sintaxe Python)
    "S",      # flake8-bandit (análise de segurança SAST)
    "BLE",    # flake8-blind-except (proíbe 'except Exception:' genérico)
    "RUF",    # Regras exclusivas do Ruff
]
ignore = [
    "E501",   # Line length (delegado ao formatador)
]

[tool.ruff.lint.isort]
combine-as-imports = true
known-first-party = ["meu_app"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
```
