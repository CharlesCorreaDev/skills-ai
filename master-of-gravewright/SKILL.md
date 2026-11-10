---
name: master-of-gravewright
description: Suíte de Engenharia Reversa, Desenvolvimento de Sistemas, Módulos, Extensões, Itens, Compêndios e Diagnóstico de Ambiente para o Gravewright VTT (Virtual Tabletop Open-Source em Python/Django).
---

# Master of Gravewright VTT ⚔️🎲

> **Versão:** `0.1.0-beta`  
> **Status:** Beta  
> **Compatibilidade:** Gravewright v0.3.0 a v0.4.x+  
> **Arquitetura Base:** Python 3.12+, Astral `uv`, Django 5.x/6.x, Jinja2, Django Channels (WebSockets), JavaScript ESModules e HTML5 Canvas.

---

## 🎯 Visão Geral / Overview

A skill **`master-of-gravewright`** é a inteligência técnica definitiva para desenvolvedores, Mestres e criadores de conteúdo que desejam construir **módulos**, **extensões**, **sistemas de RPG**, **compêndios de regras**, **fichas de personagens**, **clocks**, **mapas universais (UVTT)** e automações para o **[Gravewright VTT](https://gravewright.com/)** — o Virtual Tabletop open-source brasileiro desenvolvido em Python/Django.

### 🌟 O que é o Gravewright VTT?
Desenvolvido por **Rodrigo Tristão Porfírio** ([rtristaoporfirio@outlook.com](mailto:rtristaoporfirio@outlook.com)), o Gravewright é uma plataforma VTT moderna que centraliza o controle do mundo no servidor (regras estritas em Django/Python), enquanto entrega interfaces reativas e leves no navegador do jogador através de WebSockets e Jinja2.

---

## 🛠️ Mandatos de Instalação e Ambiente (OBRIGATÓRIO)

### 1. Diagnóstico Ativo do Ambiente Local
Quando esta skill for ativada ou o usuário solicitar setup do ambiente:
1. O agente **DEVE executar o diagnóstico automatizado**:
   ```bash
   python master-of-gravewright/scripts/setup_dev_env.py --check
   ```
2. O agente deve inspecionar e guiar o desenvolvedor na instalação do ferramental necessário:
   - **Python 3.12+**: Interpretador obrigatório.
   - **Astral `uv`**: Gerenciador de pacotes ultrarrápido padrão do Gravewright (`uv sync`, `uv run`).
   - **Git**: Controle de versão.
   - **Ruff**: Linter e formatador de código Python via Astral (`uv add --dev ruff`).

### 2. Instalação Obrigatória de Skills Companheiras
> [!IMPORTANT]
> O agente **DEVE instalar e utilizar as seguintes skills parceiras** para suportar o desenvolvimento no ecossistema Gravewright:
> 
> 1. **`python-dev-expert` (`v0.4.0-beta`):**
>    - Para toda a programação no backend Django, ORM, models, services, migrations e testes.
>    - Comando: `npx skills@latest add CharlesCorreaDev/skills-ai --skill=python-dev-expert`
> 2. **`bootstrap-ux-ui-plus` (`v0.3.0-beta`):**
>    - Para estilização e ergonomia de interfaces web e painéis do GM em Jinja2/HTML5 com acessibilidade WCAG 2.2 AA.
>    - Comando: `npx skills@latest add CharlesCorreaDev/skills-ai --skill=bootstrap-ux-ui-plus`
> 4. **`microsoft/postgres-skills` (PostgreSQL & Database Engineering):**
   - Para modelagem relacional avançada, índices JSONB em itens/fichas, connection pooling e deploy de alta escala com PostgreSQL.
   - Comando: `npx skills@latest add microsoft/postgres-skills`
   - Consulte o guia completo em [Guia de Banco de Dados: SQLite e PostgreSQL](docs/database-guide.md).
5. **Git Workflows & Version Control (`git-pr-workflows` / `github`):**
   - Para governança de repositórios de módulos, tags de release e empacotamento para o Marketplace.
   - Comando: `npx skills@latest add github`
   - Consulte o guia completo em [Guia de Versionamento Git](docs/git-guide.md).
5. **`cloudflare/security-audit-skill` & `NVIDIA/auto-ontology`:**
>    - Auditoria de segurança de permissões do GM vs Jogadores e proibição absoluta de inventar métricas/regras inexistentes.
>    - Comando: `npx skills@latest add cloudflare/security-audit-skill` e `npx skills@latest add NVIDIA/auto-ontology`

---

## 🏛️ Arquitetura e Engenharia Reversa do Gravewright

O Gravewright separa com rigor a responsabilidade entre cliente e servidor:

```
┌─────────────────────────────────────────────────────────────┐
│                 Gravewright VTT Architecture                │
├──────────────────────────────┬──────────────────────────────┤
│       BACKEND (Python)       │      FRONTEND (Browser)      │
├──────────────────────────────┼──────────────────────────────┤
│ • Django 5.x/6.x Core        │ • Jinja2 Template Shell     │
│ • Domain services.py         │ • Native JS ESModules        │
│   (Regras, Auth, Persistência│ • HTML5 Canvas (Tokens/Grid) │
│ • Django Channels            │ • WebSockets (Realtime Sync) │
│   (WebSockets por Campanha)  │ • Isolated Namespaced CSS    │
│ • SQLite (Dev) / Postgres    │ • Audio & Clocks WebAPIs     │
└──────────────────────────────┴──────────────────────────────┘
```

### Regras de Ouro da Arquitetura:
1. **Regra de Serviços (`services.py`):** Toda lógica de validação de regras de RPG, autorização de GM e persistência deve residir em arquivos de serviço (`services.py`). Views e WebSockets apenas traduzem requisições para os services.
2. **Dois Tipos de Módulos Oficiais:**
   - **Browser Modules:** Pacotes ZIP contendo arquivos JavaScript/CSS puros que alteram ou estendem a interface do tabuleiro. Ativados pelo GM na campanha.
   - **Django App Modules:** Aplicativos Django completos que adicionam novas tabelas, modelos de dados ou APIs no servidor. Ativados no servidor pelo administrador.

---

## 🚀 Como Criar Módulos e Extensões do Zero

Use o script scaffolder integrado:

```bash
# 1. Criar um módulo de navegador (Frontend JS/CSS):
python master-of-gravewright/scripts/setup_dev_env.py --create-module "meu-modulo" --type browser --author "Charles Corrêa"

# 2. Criar uma extensão com backend Django:
python master-of-gravewright/scripts/setup_dev_env.py --create-module "meu-sistema" --type django --author "Charles Corrêa"
```

### Estrutura do `manifest.json` Canônico:
```json
{
  "id": "meu-modulo",
  "title": "Meu Super Módulo",
  "version": "0.1.0",
  "description": "Extensão para customização do tabuleiro e regras no Gravewright VTT.",
  "author": "Charles Corrêa",
  "license": "MIT",
  "compatibility": {
    "minimum": "0.3.0",
    "verified": "0.3.4"
  },
  "scripts": ["index.js"],
  "styles": ["style.css"]
}
```

---

## 📚 Documentação Técnica Integrada (Offline em EN e pt-BR)

A skill possui cópia integral offline dos manuais oficiais em [`docs/en/`](docs/en/) e [`docs/pt-BR/`](docs/pt-BR/):
- **Guias de Engenharia:** [Guia de Banco de Dados: SQLite & PostgreSQL](docs/database-guide.md) • [Guia de Versionamento Git](docs/git-guide.md)
- **Arquitetura & Código:** [Architecture](docs/pt-BR/architecture.md) • [Code Map](docs/pt-BR/code-map.md) • [API](docs/pt-BR/api.md) • [Development](docs/pt-BR/development.md)
- **Módulos & Frontend:** [Modules Guide](docs/pt-BR/modules.md) • [Frontend](docs/pt-BR/frontend.md) • [Ethical Porting](docs/pt-BR/ethical-module-porting.md)
- **Sistemas de Jogo & Recursos:** [Campaign Management](docs/pt-BR/campaign-management.md) • [Journals](docs/pt-BR/journals.md) • [Clocks](docs/pt-BR/clocks.md) • [Clues](docs/pt-BR/clues.md) • [Mindmaps](docs/pt-BR/mindmaps.md) • [Map Builder](docs/pt-BR/map-builder.md) • [PDF System](docs/pt-BR/pdf-system.md) • [Universal VTT (UVTT)](docs/pt-BR/universal-vtt.md)
- **Runners & Deployment:** [Getting Started](docs/pt-BR/getting-started.md) • [Windows Runner](docs/pt-BR/windows-runner.md) • [Linux Runner](docs/pt-BR/linux-runner.md) • [macOS Runner](docs/pt-BR/macos-runner.md) • [Deployment](docs/pt-BR/deployment.md) • [Testing](docs/pt-BR/testing.md)

---

## 🛡️ Auditoria de Segurança Obrigatória (Cloudflare Security Audit) & Anti-Alucinação (NVIDIA Auto-Ontology)
> [!IMPORTANT]
> **Toda criação de código, arquitetura, automação, configuração ou resposta DEVE seguir as seguintes diretrizes:**
> 1. **Cloudflare Security Audit (`cloudflare/security-audit-skill`):**
>    - Instalação: `npx skills@latest add cloudflare/security-audit-skill`
>    - Sempre que algo for desenvolvido, execute uma auditoria adversarial em 6 fases (Mapeamento de superfícies, Caça por cobertura, Validação cética de falso-positivo, Saída estruturada, Verificação de sinks e Relatório com correção imediata).
>    - Se forem detectadas vulnerabilidades, falhas de autorização, injeções ou vazamentos de dados, **o agente DEVE realizar as correções imediatamente**.
> 2. **NVIDIA Auto-Ontology (`NVIDIA/auto-ontology`):**
>    - Instalação: `npx skills@latest add NVIDIA/auto-ontology` (ou `pip install auto-ontology`)
>    - **PROIBIDO INVENTAR NÚMEROS INEXISTENTES:** O agente JAMAIS deve alucinar estatísticas, portas arbitrárias, contagens fictícias, colunas inexistentes ou esquemas falsos. Se um número ou parâmetro não for conhecido com certeza matemática ou documental, declare incerteza e consulte as fontes reais.
> - Consulte o guia canônico completo em [`docs-for-skill/security-audit-and-auto-ontology.md`](../docs-for-skill/security-audit-and-auto-ontology.md).

---

## 📁 Estrutura da Skill

```
master-of-gravewright/
├── SKILL.md                          # Diretrizes e mandatos mestres para a IA
├── README.md                         # Visão geral completa bilíngue (EN / PT-BR)
├── VERSION                           # Versão semântica atual (0.1.0-beta)
├── CHANGELOG.md                      # Histórico detalhado de versões
├── scripts/
│   └── setup_dev_env.py              # Diagnóstico de ferramentas e scaffolder de módulos
├── mcp/                              # Servidor MCP Nativo Oficial (master-of-gravewright-mcp)
│   ├── gravewright_mcp_server.py     # Core do Servidor MCP em Python (JSON-RPC 2.0 stdio)
│   └── README.md                     # Guia de configuração e ferramentas MCP
├── docs/                             # Manuais oficiais offline do Gravewright
│   ├── en/                           # 25 guias técnicos em inglês
│   └── pt-BR/                        # 25 guias técnicos em português brasileiro
└── templates/                        # Templates de módulos e extensões
```

