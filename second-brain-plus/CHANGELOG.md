# Changelog — Second Brain Plus 🧠⚡

Todas as mudanças notáveis nesta skill serão documentadas neste arquivo.
O formato segue o padrão de [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [0.1.0-beta] - 2026-11-13

### Adicionado / Added
- **Interface de Comandos de Barra Dedicados (`/second-brain`):**
  - `/second-brain install`: Assistente de configuração inicial e criação dos bancos no Notion.
  - `/second-brain save memory <texto>`: Armazena fatos, regras e aprendizados na memória persistente e auto-sincroniza.
  - `/second-brain adr <título>`: Registra decisões arquiteturais (ADR) instantaneamente.
  - `/second-brain sync`: Sincronização sob demanda (Notion + claude-mem + graphify).
  - `/second-brain status`: Painel de saúde, notas ativas, métricas do grafo e conexão.
  - `/second-brain git-status`: Auditoria de sincronização remota Git (GitHub `gh` e GitLab `glab`), visibilidade (privado/público) e diagnóstico ("Precisa de algo a mais?").
  - `/second-brain git-sync`: Commit e push de alterações para o repositório remoto configurado.
  - `/second-brain tdah`: Ativação de foco atômico (1 micro-ação por vez, baixa carga e Body Doubling).
  - `/second-brain focus`: Exibição do painel de foco atômico neurodivergente (Orbit OS).
- **Template Padrão Canônico do Notion:**
  - Adoção oficial do **[Second Brain All-in-One Productivity System 2026](https://www.notion.com/pt/templates/second-brain-all-in-one-productivity-system-2026)** como layout visual padrão, documentado em `docs/recommended_notion_templates.md`.
- **Motor de Sincronização Automática em Tempo Real (`auto_sync.py`):**
  - Suporte a modo `--now` (disparo pontual) e `--watch` (monitoramento contínuo em segundo plano).
- **Lançamento Inicial em Versão Beta** com documentação e código 100% bilíngue (Português PT-BR e Inglês EN).
- **Arquitetura de Memória Persistente em 5 Camadas:**
  - *Working Memory*, *Episodic Memory*, *Semantic Memory*, *Procedural Memory*, *Knowledge Graph*.
- **Integração com Notion API oficial (v2022-06-28):**
  - Criação automática dos 4 bancos relacionais via API e sincronização bidirecional.
- **Suporte Oficial ao Ecossistema Notion Developer:**
  - Suporte ao **Notion CLI (`ntn` / https://ntn.dev)** para inspeção de páginas e queries de terminal.
  - Modelos e guias para **Notion Workers (`@notionhq/workers`)** serverless edge triggers.
  - Integração com **Notion MCP (Model Context Protocol)** e Notion Skills para tool calling de agentes de IA.
  - Documentação completa da arquitetura de blocos (árvores de conteúdo) e APIs corporativas de Admin em `docs/notion_developer_suite.md`.
- **Integração com GitHub CLI (`gh`) e GitLab CLI (`glab`):**
  - Motor de sincronização remota multi-plataforma em `scripts/git_remote_sync.py`.
  - Suporte a repositórios privados e públicos com detecção automática de visibilidade via API.
  - Diagnóstico proativo ("Precisa de algo a mais?"): verificação de vazamento de segredos no `.gitignore`, divergência de branches (*ahead/behind*) e alerta de privacidade.
  - Templates de automação contínua de CI/CD para GitHub Actions (`templates/github/second-brain-sync.yml`) e GitLab CI (`templates/gitlab/.gitlab-ci.yml`).
  - Guia arquitetural completo em `docs/git_remote_sync_guide.md`.
- **Ecossistema Integrado:**
  - `claude-mem`, `graphify`, `caveman`, `headroom`, `context7`, `grill-me`, `karpathy-guidelines`, `impeccable`, `not-today-adhd`.
