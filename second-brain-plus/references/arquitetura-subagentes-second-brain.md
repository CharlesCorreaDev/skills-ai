# Arquitetura dos 7 Subagentes Especializados — Second Brain Plus 🧠⚡💾
## 7 Specialized Subagents Architecture — Second Brain Plus 🧠⚡💾

A suíte **Second Brain Plus** opera para garantir que o Segundo Cérebro seja uma Fonte Única da Verdade (SSOT) livre de esquecimento, desordem de notas e dessincronização entre nuvem e terminal, agora com agente dedicado à governança de PRs, Specs, SSD e Handoff de projetos.

The **Second Brain Plus** suite operates to ensure the Second Brain serves as an immutable Single Source of Truth (SSOT), immune to context amnesia, note sprawl, and desynchronization between cloud and terminal environments, now featuring a dedicated specialist for PR, Spec, SSD, and Handoff lifecycle memory.

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor / User]) --> Showrunner[1. Orquestrador de Contexto & Memória]
    
    Showrunner --> SpecHandoff[2. Engenheiro de Specs, PRs, SSD & Handoff]
    Showrunner --> Ingestor[3. Ingestor & Triador P.A.R.A. 2.0]
    
    SpecHandoff --> AdrArchitect[4. Arquiteto de Decisões & ADRs Imutáveis]
    
    Ingestor & AdrArchitect --> NotionBridge[5. Engenheiro de Integração Notion API]
    SpecHandoff & AdrArchitect --> GitSync[6. Guardião de Versionamento Git gh/glab]
    
    NotionBridge & GitSync --> NeuroSync[7. Auditor de Saúde, Integridade & Ergonomia TDAH]
    NeuroSync --> OutputFinal([Memória Sincronizada, Consistente & Blindada])
`

---

## 🇧🇷 Português (Brasil) — Papéis e Responsabilidades dos 7 Subagentes

1. **Orquestrador de Contexto & Memória (Showrunner):**
   - Coordena o ciclo de vida da memória do agente, supervisionando o fluxo entre as 5 camadas (Working, Episodic, Semantic, Procedural, Decisional).
2. **Engenheiro de Specs, PRs, SSD & Handoff (Memória de Ciclo de Vida do Projeto):**
   - **Missão:** Centraliza, estrutura e versiona formalmente todas as especificações técnicas (Specs/RFCs), diagramas de sequência de sistema (SSD - System Sequence Diagrams), descrições atômicas de Pull Requests (PRs) e guias de Handoff para o desenvolvedor ou cliente.
   - **Persistência Canônica:** Salva automaticamente em .second-brain/specs/, .second-brain/prs/ e .second-brain/handoffs/, sincronizando com a base de dados do Notion e memória episódica do projeto.
3. **Ingestor & Triador P.A.R.A. 2.0:**
   - Classifica automaticamente notas, ideias, snippets e recursos nas 4 categorias de Tiago Forte: Projetos, Áreas, Recursos e Arquivos.
4. **Arquiteto de Decisões & ADRs Imutáveis:**
   - Formaliza registros imutáveis de decisões técnicas (Architecture Decision Records) para impedir que a IA mude escolhas arquiteturais consolidadas ou altere bibliotecas sem justificativa.
5. **Engenheiro de Integração Notion API:**
   - Mantém as 7 bases de dados relacionais do Notion sincronizadas com o cofre local Markdown via API oficial e webhooks.
6. **Guardião de Versionamento Git (gh / glab):**
   - Garante auditoria contínua de repositórios remotos (GitHub/GitLab), controle estrito de privacidade (público/privado) e commits atômicos do cofre conforme [SemVer 2.0.0 PT-BR](https://semver.org/lang/pt-BR/).
7. **Auditor de Saúde, Integridade & Ergonomia TDAH:**
   - Monitora integridade de hashes de arquivos, nós semânticos (graphify) e formata respostas atômicas com bionic bolding e Orbit OS para neurodivergência (
ot-today-adhd).

---

## 🇺🇸 English — Roles and Responsibilities of the 7 Subagents

1. **Context & Memory Orchestrator (Showrunner):**
   - Oversees the agent's memory lifecycle across 5 distinct layers (Working, Episodic, Semantic, Procedural, Decisional).
2. **Specs, PRs, SSD & Handoff Engineer (Project Lifecycle Memory):**
   - **Mission:** Centralizes, structures, and formally versions all Technical Specifications (Specs/RFCs), System Sequence Diagrams (SSD), atomic Pull Request (PR) bodies, and Handoff manuals for developers and clients.
   - **Canonical Storage:** Persists records inside .second-brain/specs/, .second-brain/prs/, and .second-brain/handoffs/, synchronizing to Notion databases and project episodic memory.
3. **P.A.R.A. 2.0 Ingestor & Classifier:**
   - Routes incoming project knowledge, snippets, and resources into Tiago Forte's Projects, Areas, Resources, and Archives.
4. **Decisions & Immutable ADRs Architect:**
   - Authors immutable Architecture Decision Records (ADRs) to lock in foundational technical choices and prevent agent amnesia or accidental rewrites.
5. **Notion API Integration Engineer:**
   - Synchronizes local Markdown vaults with the 7 relational Notion databases via official APIs and webhooks.
6. **Git Versioning Guardian (gh / glab):**
   - Automates bidirectional Git backups (GitHub/GitLab), audits repository visibility (public/private), and enforces clean commits adhering to [SemVer 2.0.0](https://semver.org/).
7. **Health, Integrity & ADHD Ergonomics Auditor:**
   - Tracks file hash integrity, knowledge graph edges (graphify), and formats outputs with bionic bolding for neurodivergent focus (
ot-today-adhd).
