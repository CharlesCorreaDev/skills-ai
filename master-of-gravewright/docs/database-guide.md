# Guia de Banco de Dados e Gerenciamento SQLite para Gravewright VTT

O **Gravewright VTT** utiliza o **SQLite 3** como seu motor de persistência exclusivo (`data/gravewright.sqlite3`).

Este guia absorve as melhores práticas da comunidade de engenharia de software e segurança em SQLite ([SecureSkills SQLite](https://github.com/SecureSkills-io/sqlite-skill), [Claude SQLite Database Expert](https://github.com/martinholovsky/claude-skills-generator/tree/main/skills/sqlite) e padrões de conformidade), estabelecendo os **mecanismos canônicos de leitura, consulta, backup e mutação de dados com autorização prévia e auditabilidade**.

---

## 🔒 1. Princípio Sagrado: Permissão do Usuário e Operações Atômicas

> [!CAUTION]
> **Aviso de Integridade:** Modificações diretas no banco de dados SQLite (`data/gravewright.sqlite3`) ignorando o Django ORM ou serviços de aplicação podem corromper o estado das mesas, desconectar sessões ativas ou gerar conflitos de revisão.
> 
> **Regras Obrigatórias para Agentes de IA:**
> 1. **Autorização Explícita Prévia:** O agente NUNCA deve executar comandos de alteração (`UPDATE`, `DELETE`, `DROP`, `INSERT`) no banco de dados sem antes:
>    - Apresentar ao usuário o SQL exato que será executado e a justificativa clara da alteração.
>    - Solicitar a aprovação expressa do usuário no chat.
> 2. **Backup Automático Pré-Mutação:** Antes de aplicar qualquer `UPDATE` ou migração estrutural, crie uma cópia pontual do banco (ex: `data/gravewright.sqlite3.backup-<TIMESTAMP>`).
> 3. **Modo Somente Leitura por Padrão:** Consultas de diagnóstico (`SELECT`, contagens, inspeção de tabelas, busca de schemas) podem ser executadas para responder a dúvidas e planejar soluções.

---

## 🗄️ 2. Topologia do Banco de Dados (`data/gravewright.sqlite3`)

O banco do Gravewright gerencia 86+ tabelas integradas aos domínios da aplicação:

| Prefixo da Tabela | Domínio do Jogo / Aplicação | Exemplos de Dados Armazenados |
|---|---|---|
| `gravewright_actors_*` | **Atores & Fichas** | Personagens, NPCs, monstros, atributos, fichas JSON e pastas |
| `gravewright_items_*` | **Itens & Equipamentos** | Armas, magias, talentos, armaduras e inventário |
| `gravewright_campaigns_*` | **Campanhas** | Mesas ativas, permissões de jogadores e configurações |
| `gravewright_maps_*` | **Mapas & Cenas** | Mapas UVTT (`.dd2vtt`), paredes, iluminação e grid |
| `gravewright_tokens_*` | **Tokens** | Posições (x, y), elevação, visibilidade e condições |
| `gravewright_combat_*` | **Combate** | Ordem de iniciativa, rodadas e turnos ativos |
| `gravewright_journals_*` | **Diários** | Handouts, notas de sessão e diários do mestre |
| `gravewright_administration_*` | **Administração** | Snapshots de backup, logs de auditoria e host settings |

---

## 🛠️ 3. Ferramentas Integradas na Skill (`scripts/manage_sqlite.py`)

A skill `master-of-gravewright` fornece um utilitário seguro com saída JSON estruturada para leitura e administração:

### A. Listar Tabelas do Banco:
```bash
python master-of-gravewright/scripts/manage_sqlite.py --tables --json
```

### B. Inspecionar o Schema de uma Tabela:
```bash
python master-of-gravewright/scripts/manage_sqlite.py --schema gravewright_actors_actor --json
```

### C. Executar Consulta Segura Somente-Leitura (SELECT):
```bash
python master-of-gravewright/scripts/manage_sqlite.py --query "SELECT id, name, type FROM gravewright_actors_actor LIMIT 10;" --json
```

### D. Criar Backup Instantâneo:
```bash
python master-of-gravewright/scripts/manage_sqlite.py --backup
```

---

## 🛡️ 4. Padrões de Segurança e Robustez (SQLite Best Practices)

1. **Prevenção Total contra SQL Injection:**
   - NUNCA concatene strings de inputs do usuário em queries (`f"WHERE name = '{user_input}'"`).
   - Use SEMPRE queries parametrizadas com placeholders (`WHERE name = ?`, `(user_input,)`).

2. **Concorrência e Modo WAL (Write-Ahead Logging):**
   - O Gravewright opera com `PRAGMA journal_mode = WAL;` e `PRAGMA synchronous = NORMAL;`, permitindo que múltiplos leitores acessem o banco simultaneamente sem travar a escrita assíncrona dos WebSockets.
   - Toda transação de escrita deve usar `BEGIN IMMEDIATE` para evitar deadlocks de gravação.

3. **Chaves Estrangeiras (`Foreign Keys`):**
   - Ao inspecionar ou executar rotinas SQL puras, assegure a integridade relacional com `PRAGMA foreign_keys = ON;`.

4. **Manutenção e Desfragmentação Segura:**
   - Execute `PRAGMA optimize;` e analise `PRAGMA freelist_count;` antes de sugerir `VACUUM`. O `VACUUM` só deve ser rodado com a instância parada ou em períodos de inatividade.
