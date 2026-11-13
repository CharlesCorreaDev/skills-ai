# Guia de Banco de Dados do Gravewright VTT (Database Guide)

O **Gravewright VTT** utiliza intencionalmente o **SQLite 3** como seu mecanismo de banco de dados exclusivo (`data/gravewright.sqlite3`). 

Diferente de sistemas web corporativos genéricos, o Gravewright foi desenhado para rodar localmente com baixa latência, simplicidade operacional e portabilidade total de campanhas, operando com transações `IMMEDIATE` controladas pelo Django ORM.

> [!IMPORTANT]
> **Atenção:** O Gravewright **não** utiliza PostgreSQL, `DATABASE_URL` nem `dj_database_url`. Todo o gerenciamento de persistência do core e de extensões é baseado em SQLite no caminho `data/gravewright.sqlite3`.

---

## 💾 1. Arquitetura de Persistência no SQLite

- **Localização padrão:** `data/gravewright.sqlite3`.
- **Modo de transação:** Operações transacionais são configuradas com `BEGIN IMMEDIATE` para evitar conflitos de gravação concorrente em ambiente assíncrono/WebSockets.
- **Isolamento de Estado:**
  - O estado do jogo, atores, cenas, itens e logs residem no SQLite.
  - Dados customizados de módulos de navegador são armazenados via API de storage do cliente (`api.actors.saveSheet(...)` ou storage de tabela/usuário com controle de revisão optimista `expectedRevision`).
  - Módulos de servidor (Django apps) podem definir seus próprios models e tabelas no SQLite.

---

## 📦 2. Migrações em Módulos e Extensões Django

Quando você cria um módulo do tipo `django` (declarado no `manifest.json` sob o bloco `"django": { "apps": [...] }`), o Gravewright carrega o app dinamicamente.

### Estrutura de Diretórios Recomendada:
```text
meu-modulo/
├── manifest.json
├── LICENSE.txt
└── meu_modulo_server/
    ├── __init__.py
    ├── apps.py
    ├── models.py
    ├── services.py
    └── migrations/
        └── __init__.py
```

### Regras para Migrações de Extensões:
1. Toda pasta de app Django criada para extensões deve conter o subdiretório `migrations/` com um arquivo `__init__.py` vazio.
2. Ao adicionar ou alterar models na extensão, execute a criação de migrações direcionada para o label do app:
   ```bash
   uv run python manage.py makemigrations meu_modulo_server
   ```
3. Para aplicar migrações:
   ```bash
   uv run python manage.py migrate
   ```

---

## 🛡️ 3. Boas Práticas de Concorrência e Transações

- **Não bloqueie a thread assíncrona:** Operações de banco de dados devem ser delegadas aos serviços (`services.py`) e transacionadas de forma atômica (`transaction.atomic()`).
- **Resolução de Conflitos:** Ao atualizar dados de atores e fichas pelo runtime do navegador, sempre capture possíveis conflitos (`conflict`), leia a revisão atual do documento (`expectedRevision`) e faça o merge antes de reenviar. Nunca sobrescreva cegamente dados de outros participantes da mesa.
