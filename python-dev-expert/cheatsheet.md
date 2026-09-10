# Cheatsheet / Guia Rápido - Python Developer Expert

## 🐍 Evolução e Features (Python 3.x)

| Feature | Versão de Origem | Exemplo / Descrição |
|---|---|---|
| **F-Strings** | 3.6 | `f"Hello {name}"` |
| **Data Classes** | 3.7 | `@dataclass class User: ...` |
| **Walrus Operator** | 3.8 | `if (n := len(a)) > 10:` |
| **Positional-Only Args**| 3.8 | `def f(a, /, b):` |
| **Union Type Hinting** | 3.10 | `def foo(v: int \| str):` (substitui `Union[int, str]`) |
| **Pattern Matching** | 3.10 | `match status: case 200: ...` |
| **Melhoria em Erros** | 3.11 | Mensagens de erro muito mais detalhadas e apontamentos precisos de sintaxe |
| **`ExceptionGroup`** | 3.11 | Agrupamento de múltiplas exceções para fluxos assíncronos |
| **Type Parameter Sintaxe**| 3.12 | `def max[T](args: Iterable[T]) -> T:` |

## 🛠️ Comandos CLI Úteis

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual (Windows)
.\venv\Scripts\activate

# Ativar ambiente virtual (Linux/Mac)
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Exportar dependências
pip freeze > requirements.txt

# Executar módulo como script
python -m http.server 8000
```

## 🔒 Boas Práticas (Checklist)
1. **Ambientes Isolados**: NUNCA instale pacotes globalmente. Sempre use `venv`, `poetry` ou `conda`.
2. **Dependências**: Fixe as versões no `requirements.txt` ou `pyproject.toml` para reprodutibilidade.
3. **Type Hinting**: Utilize `mypy` no seu CI/CD para pegar erros silenciosos.
4. **Secrets**: Use variáveis de ambiente (ex: `.env` com a lib `python-dotenv`) e NUNCA commite chaves de API.
