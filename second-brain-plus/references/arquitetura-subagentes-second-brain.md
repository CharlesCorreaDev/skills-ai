# Arquitetura Multiagente — Second Brain Plus 🧠⚡💾

Para garantir que o Segundo Cérebro seja uma Fonte Única da Verdade (SSOT) livre de esquecimento, desordem de notas e dessincronização entre nuvem e terminal, a suíte opera com **6 Subagentes Especializados**:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Orquestrador de Contexto & Memória]
    Showrunner --> Ingestor[2. Ingestor & Triador P.A.R.A.]
    Showrunner --> AdrArchitect[3. Arquiteto de Decisões & ADRs]
    Ingestor --> NotionBridge[4. Engenheiro de Integração Notion API]
    AdrArchitect --> GitSync[5. Guardião de Versionamento Git gh/glab]
    NotionBridge & GitSync --> NeuroSync[6. Auditor de Saúde & Ergonomia TDAH]
    NeuroSync --> OutputFinal([Memória Sincronizada, Consistente & Blindada])
`

## Papéis e Responsabilidades dos 6 Subagentes:

1. **Orquestrador de Contexto & Memória (Showrunner):**
   - Coordena o ciclo de vida da memória do agente, supervisionando o fluxo entre as 5 camadas (Working, Episodic, Semantic, Procedural, Decisional).
2. **Ingestor & Triador P.A.R.A.:**
   - Classifica automaticamente notas, ideias e recursos em Projetos, Áreas, Recursos e Arquivos (P.A.R.A. 2.0 de Tiago Forte).
3. **Arquiteto de Decisões & ADRs:**
   - Formaliza registros imutáveis de decisões técnicas (Architecture Decision Records) para impedir que a IA mude escolhas arquiteturais consolidadas.
4. **Engenheiro de Integração Notion API:**
   - Mantém as 7 bases de dados relacionais do Notion sincronizadas com o cofre local Markdown via API oficial.
5. **Guardião de Versionamento Git (gh / glab):**
   - Garante auditoria contínua de repositórios remotos (GitHub/GitLab), controle estrito de privacidade (public/private) e commits atômicos do cofre.
6. **Auditor de Saúde & Ergonomia TDAH:**
   - Monitora integridade de hashes, nós semânticos (graphify) e formata respostas atômicas com bionic bolding e Orbit OS para neurodivergência.
