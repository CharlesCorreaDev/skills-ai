# Arquitetura dos 6 Subagentes Especializados — Second Brain Plus 🧠⚡💾
## 6 Specialized Subagents Architecture — Second Brain Plus 🧠⚡💾

A suíte **Second Brain Plus** opera para garantir que o Segundo Cérebro seja uma Fonte Única da Verdade (SSOT) livre de esquecimento, desordem de notas e dessincronização entre nuvem e terminal.

The **Second Brain Plus** suite operates to ensure the Second Brain serves as an immutable Single Source of Truth (SSOT), immune to context amnesia, note sprawl, and desynchronization between cloud and terminal environments.

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor / User]) --> Showrunner[1. Orquestrador de Contexto & Memória]
    Showrunner --> Ingestor[2. Ingestor & Triador P.A.R.A.]
    Showrunner --> AdrArchitect[3. Arquiteto de Decisões & ADRs]
    Ingestor --> NotionBridge[4. Engenheiro de Integração Notion API]
    AdrArchitect --> GitSync[5. Guardião de Versionamento Git gh/glab]
    NotionBridge & GitSync --> NeuroSync[6. Auditor de Saúde & Ergonomia TDAH]
    NeuroSync --> OutputFinal([Memória Sincronizada, Consistente & Blindada])
`

---

## 🇧🇷 Português (Brasil) — Papéis e Responsabilidades dos 6 Subagentes

1. **Orquestrador de Contexto & Memória (Showrunner):** Coordena o ciclo de vida da memória do agente, supervisionando o fluxo entre as 5 camadas (Working, Episodic, Semantic, Procedural, Decisional).
2. **Ingestor & Triador P.A.R.A.:** Classifica automaticamente notas, ideias e recursos em Projetos, Áreas, Recursos e Arquivos (P.A.R.A. 2.0 de Tiago Forte).
3. **Arquiteto de Decisões & ADRs:** Formaliza registros imutáveis de decisões técnicas (Architecture Decision Records) para impedir que a IA mude escolhas arquiteturais consolidadas.
4. **Engenheiro de Integração Notion API:** Mantém as 7 bases de dados relacionais do Notion sincronizadas com o cofre local Markdown via API oficial.
5. **Guardião de Versionamento Git (gh / glab):** Garante auditoria contínua de repositórios remotos (GitHub/GitLab), controle estrito de privacidade e commits atômicos do cofre conforme [SemVer 2.0.0 PT-BR](https://semver.org/lang/pt-BR/).
6. **Auditor de Saúde & Ergonomia TDAH:** Monitora integridade de hashes, nós semânticos (graphify) e formata respostas atômicas com bionic bolding e Orbit OS para neurodivergência.

---

## 🇺🇸 English — Roles and Responsibilities of the 6 Subagents

1. **Context & Memory Orchestrator (Showrunner):** Manages the memory lifecycle across 5 distinct layers (Working, Episodic, Semantic, Procedural, Decisional).
2. **P.A.R.A. Ingestor & Classifier:** Automatically routes incoming notes, ideas, and knowledge into Tiago Forte's Projects, Areas, Resources, and Archives.
3. **Decisions & ADRs Architect:** Authors immutable Architecture Decision Records (ADRs) to lock in design patterns and prevent agent amnesia.
4. **Notion API Integration Engineer:** Synchronizes local Markdown vaults with the 7 relational Notion databases via official APIs.
5. **Git Versioning Guardian (gh / glab):** Automates bidirectional Git backups (GitHub/GitLab), audits visibility (public/private), and enforces clean commits.
6. **Health & ADHD Ergonomics Auditor:** Tracks hash integrity, knowledge graph edges (graphify), and formats outputs with bionic bolding for neurodivergent focus.
