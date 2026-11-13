# Recommended Notion Templates Catalog 🏛️📋
# Catálogo de Modelos Recomendados do Notion

> **Canonical Default Template / Modelo Padrão Canônico:**  
> 🌟 **[Second Brain All-in-One Productivity System 2026](https://www.notion.com/pt/templates/second-brain-all-in-one-productivity-system-2026)**  
> *Bilingual Documentation: English (EN) and Portuguese (PT-BR) / Documentação Bilíngue*

---

## 🌟 Padrão Oficial do Sistema / Official Default Template

### 🥇 [Second Brain All-in-One Productivity System 2026](https://www.notion.com/pt/templates/second-brain-all-in-one-productivity-system-2026)
- **Definição:** Adotado como o **modelo padrão canônico** do `second-brain-plus`.
- **Por que é o padrão:**
  - Implementação completa do Método P.A.R.A. (Projects, Areas, Resources, Archives).
  - Visual moderno, limpo e profissional, sem poluição de propriedades desnecessárias.
  - Conexão nativa com os bancos de dados relacionais sincronizados pela nossa API.
  - Seções dedicadas para metas, revisões semanais, entregáveis de projetos e base de conhecimento.

---

## 🏆 Catálogo Completo por Caso de Uso / Complete Catalog by Use Case

### 1. Foco Neurodivergente e TDAH (Baixa Carga Cognitiva)
- **[Orbit OS — ADHD Second Brain](https://www.notion.com/templates/orbit-os-adhd-second-brain):** Criado para baixa sobrecarga visual, foco atômico em 1 micro-tarefa por vez e eliminação de ruídos.
- **[Brain Reset OS — Anti-Distraction Focus Tracking](https://www.notion.com/templates/brain-reset-os-anti-distraction-focus-tracking-system):** Layout minimalista para combater a paralisia de tarefas e proteger a memória de trabalho.
- **[Eisenhower Matrix Priority Planner](https://www.notion.com/templates/eisenhower-matrix-priority-planner):** Matriz de 4 quadrantes com foco no "Fazer Agora".

### 2. Sistemas P.A.R.A. 2.0 Alternativos
- **[Ultimate PARA Dashboard](https://www.notion.com/templates/ultimate-para-dashboard):** Dashboard relacional avançado conectando entregáveis, notas e sprints de tarefas.
- **[PARA Dashboard 224](https://www.notion.com/templates/para-dashboard-224):** Implementação limpa e de carregamento rápido.

### 3. Alinhamento de Agentes de IA e Decisões Técnicas
- **[Teach to AI How You Work (Lite)](https://www.notion.com/templates/teach-to-ai-how-you-work-lite):** Seções para documentar decisões de arquitetura (ADRs) e regras para LLMs.
- **[Knowledge 1o1](https://www.notion.com/templates/knowledge-1o1):** Base semântica Zettelkasten.

---

## 🔄 Como Conectar o Modelo Padrão no seu Workspace

1. Acesse o link oficial: [https://www.notion.com/pt/templates/second-brain-all-in-one-productivity-system-2026](https://www.notion.com/pt/templates/second-brain-all-in-one-productivity-system-2026).
2. Clique no botão **"Duplicar modelo"** (ou *"Duplicate template"*) selecionando o seu workspace **Inteligência Artificial**.
3. Na página duplicada, clique no menu de três pontos (`...`) no canto superior direito ➔ **"Connections" / "Conexões"** ➔ **"Add connection"** ➔ selecione **`Second-brain-plus`**.
4. Copie a URL da página e envie para o agente ou configure no seu `.env`:
   ```env
   NOTION_PARENT_PAGE_ID=<ID_DA_PAGINA_DUPLICADA>
   ```
5. Execute a sincronização automática:
   ```bash
   python second-brain-plus/scripts/notion_sync.py --sync-local
   ```
