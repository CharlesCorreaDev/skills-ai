# Guia de Banco de Dados para Gravewright VTT: SQLite (Dev) & PostgreSQL (Prod)

O **Gravewright VTT** utiliza o **Django ORM** para gerenciar todo o ciclo de vida dos dados de campanha, fichas, itens, rolagens, clocks e anotações.
- **Ambiente Local / Desenvolvimento:** SQLite 3 (configuração padrão `db.sqlite3` gerenciada automaticamente pelo Django).
- **Ambiente de Produção / Multi-Tabelas:** PostgreSQL 16+ com suporte a conexões simultâneas, transações ACID rigorosas e WebSockets de alta concorrência via Django Channels.

---

## 🛠️ Skills Recomendadas para Banco de Dados
- **PostgreSQL:** [`microsoft/postgres-skills`](https://github.com/microsoft/postgres-skills) (`npx skills@latest add microsoft/postgres-skills`).
  - Boas práticas para índices em JSONB, tuning de conexões e pool com PgBouncer.
- **Python & Django ORM:** [`python-dev-expert`](../python-dev-expert/SKILL.md) (`v0.4.0-beta`).
  - Criação de `models.py`, `migrations`, `services.py` e validação com `pydantic`.

---

## 💾 1. Desenvolvimento com SQLite (Padrão)

No arquivo de configuração do Gravewright (`config/settings.py` ou `.env`):

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'data' / 'db.sqlite3',
    }
}
```

### Comandos Essenciais de Migração:
```bash
# Executar migrações pendentes
uv run python manage.py migrate

# Criar novas migrações após alterar models em um módulo Django
uv run python manage.py makemigrations meu_modulo_app
```

---

## 🐘 2. Produção com PostgreSQL

Para servidores com múltiplos Mestres e centenas de jogadores conectados simultaneamente via WebSockets:

```ini
# No arquivo .env do Gravewright:
DATABASE_URL=postgres://gravewright_user:senha_segura@localhost:5432/gravewright_db
```

Configuração no `settings.py`:
```python
import os
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///' + str(BASE_DIR / 'data' / 'db.sqlite3'),
        conn_max_age=600,
        ssl_require=False
    )
}
```

### Instalação do Driver no Ambiente:
```bash
uv add psycopg2-binary
# ou
uv add "psycopg[binary]"
```
