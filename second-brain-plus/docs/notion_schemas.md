# Notion API Configuration Guide 📑⚡
# Guia de Configuração da API do Notion

> **Second Brain Plus Technical Specification / Especificação Técnica do Second Brain Plus**  
> *Bilingual Documentation: English (EN) and Portuguese (PT-BR) / Documentação Bilíngue: Inglês e Português*

---

## 🇺🇸 English

### 1. Creating the Notion Integration
1. Visit the Notion developers portal: [https://www.notion.com/my-integrations](https://www.notion.com/my-integrations).
2. Click **"+ New integration"**.
3. Name your integration (e.g., `Second Brain Plus AI Agent`).
4. Select the target Workspace.
5. In **Capabilities**, ensure the following permissions are granted:
   - Read content
   - Update content
   - Insert content
6. Copy the **Internal Integration Secret** (`ntn_...`).
7. Export it as an environment variable: `NOTION_API_KEY`.

### 2. Sharing Pages with the Integration
Notion uses explicit per-page access grants:
1. Open your master Second Brain page in Notion.
2. Click the top-right menu (`...`).
3. Select **"Connections"** -> **"Add connection"**.
4. Choose `Second Brain Plus AI Agent`.
5. All sub-pages and databases created within this root page will now inherit access.

### 3. Core Database Schemas
The suite provides 4 relational databases:
- **Projects & Sprints:** Tracks milestones, deadlines, priorities, and active task states.
- **Decisions & ADRs:** Houses immutable Architectural Decision Records.
- **Session Logs & Memories:** Stores episodic timelines from coding sessions.
- **Resources & Knowledge Graph:** Catalogs reference documentation and semantic nodes.

---

## 🇧🇷 Português

### 1. Criando a Integração no Notion
1. Acesse o portal de desenvolvedores do Notion: [https://www.notion.com/my-integrations](https://www.notion.com/my-integrations).
2. Clique em **"+ New integration"**.
3. Atribua um nome (ex: `Second Brain Plus AI Agent`).
4. Selecione o Workspace de destino.
5. Em **Capabilities**, garanta que estão ativas:
   - Read content (Ler conteúdo)
   - Update content (Atualizar conteúdo)
   - Insert content (Inserir conteúdo)
6. Copie o **Internal Integration Secret** (`ntn_...`).
7. Configure-o na variável de ambiente: `NOTION_API_KEY`.

### 2. Compartilhando Páginas com a Integração
O Notion adota controle explícito de acesso por página:
1. Abra a página principal do seu Segundo Cérebro no Notion.
2. Clique no menu de reticências no canto superior direito (`...`).
3. Escolha **"Connections"** (Conexões) -> **"Add connection"**.
4. Selecione a integração `Second Brain Plus AI Agent`.
5. Todas as subpáginas e bancos de dados criados nesta página terão acesso concedido.

### 3. Esquemas dos 4 Bancos Centrais
- **Projects & Sprints:** Rastreia marcos, prazos, prioridades e status atômico de tarefas.
- **Decisions & ADRs:** Armazena decisões arquiteturais definitivas (anti-alucinação).
- **Session Logs & Memories:** Registra memórias episódicas geradas ao final de cada sessão.
- **Resources & Knowledge Graph:** Indexa documentações, manuais e nós do grafo de conhecimento.
