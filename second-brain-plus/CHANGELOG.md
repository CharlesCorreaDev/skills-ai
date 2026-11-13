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
  - `/second-brain focus`: Exibição do painel de foco atômico neurodivergente (Orbit OS).
- **Motor de Sincronização Automática em Tempo Real (`auto_sync.py`):**
  - Suporte a modo `--now` (disparo pontual) e `--watch` (monitoramento contínuo em segundo plano).
- **Lançamento Inicial em Versão Beta** com documentação e código 100% bilíngue (Português PT-BR e Inglês EN).
- **Arquitetura de Memória Persistente em 5 Camadas:**
  - *Working Memory*, *Episodic Memory*, *Semantic Memory*, *Procedural Memory*, *Knowledge Graph*.
- **Integração com Notion API oficial (v2022-06-28):**
  - Criação automática dos 4 bancos relacionais via API e sincronização bidirecional.
- **Ecossistema Integrado:**
  - `claude-mem`, `graphify`, `caveman`, `headroom`, `context7`, `grill-me`, `karpathy-guidelines`, `impeccable`, `not-today-adhd`.
