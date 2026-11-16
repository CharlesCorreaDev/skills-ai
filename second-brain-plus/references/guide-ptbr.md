## 🇧🇷 Português (PT-BR)

### 📌 Visão Geral, Filosofia & Princípio da SSOT

O **Second Brain Plus** resolve as três maiores limitações dos Large Language Models e agentes autônomos de código: **amnésia de contexto, desperdício de tokens e alucinação**.

Quando agentes trocam de sessão ou atingem o limite da janela de contexto, esquecem decisões de arquitetura anteriores, portas de rede, soluções de contorno e aprendizados obtidos.

> *"Se as anotações técnicas e regras de projeto estiverem dispersas entre chats temporários, arquivos de notas soltas e cabeças de desenvolvedores, o agente de IA alucinará com 100% de certeza."*

O **Second Brain Plus** estabelece uma infraestrutura sincronizada de camada tripla:
1. **Cofre Local em Markdown (`.second-brain/`):** Arquivos estruturados versionados no Git, com latência zero e leitura imediata offline, organizados segundo a metodologia P.A.R.A. 2.0 de Tiago Forte (Projetos, Áreas, Recursos, Arquivos).
2. **Hub Central no Notion:** Dashboard interativo com bancos de dados relacionais para acompanhamento humano em Kanban, tabelas e consultas estruturadas via Notion API.
3. **Repositórios Remotos Git Multi-Plataforma (GitHub / GitLab):** Backup criptográfico, versionado e imutável do código e decisões com controle de visibilidade privada ou pública.
4. **Template Padrão Canônico & Blueprint:** [Second Brain All-in-One Productivity System 2026](https://www.notion.com/pt/templates/second-brain-all-in-one-productivity-system-2026) adotado e adaptado para Engenharia de Software e Agentes de IA, versionado em `templates/notion/second_brain_blueprint.json` com 7 Bancos Mestres (Projetos, Tarefas, Notas/ADRs, Recursos, Áreas Dev, Rotina Operacional Dev, Diário de Sessões de IA).

---

### ⌨️ Comandos de Barra Dedicados (`/second-brain`)

A skill responde a comandos de barra amigáveis no chat da IDE e no terminal:

| Comando de Barra | Ação & Papel no Sistema |
| :--- | :--- |
| **`/second-brain install`** | Executa o assistente guiado de instalação, cria as pastas PARA, aplica o blueprint Dev & IA 2026 e constrói os 7 bancos relacionais mestres no Notion via API. |
| **`/second-brain save memory <fato>`** | Salva instantaneamente qualquer fato, regra ou aprendizado na memória persistente e auto-sincroniza. |
| **`/second-brain adr <título>`** | Registra formalmente uma Decisão de Arquitetura (ADR) inviolável contra alucinações. |
| **`/second-brain sync`** | Dispara a sincronização bidirecional imediata entre cofre local, Notion API, claude-mem e graphify. |
| **`/second-brain status`** | Exibe painel de saúde: notas ativas, nós do grafo, integridade de hashes e conectividade com a API. |
| **`/second-brain git-status`** | Audita a sincronização com GitHub (`gh`) e GitLab (`glab`), privacidade e verificações ("Precisa de algo a mais?"). |
| **`/second-brain git-sync`** | Commita e envia (push) todas as alterações do segundo cérebro para o remote Git configurado. |
| **`/second-brain task <título>`** | Agenda uma tarefa com data/horário, prioridade e 4 micro-passos atômicos (5-10 min cada). |
| **`/second-brain tasks`** | Exibe painel com todas as tarefas ativas, agendadas e pendentes no cofre e Notion. |
| **`/second-brain do <id>`** | Executa autonomamente uma tarefa: cumpre micro-passos, valida DoD, marca como concluída e arquiva log. |
| **`/second-brain focus`** | Alterna para o painel de foco único do modo neurodivergente (Orbit OS / TDAH - 1 tarefa por vez). |
| **`/second-brain tdah`** | Ativa o modo TDAH com formatação biônica, linhas curtas de 45-65 caracteres e Body Doubling contra paralisia. |

---

### 🔄 Regra Obrigatória de Sincronização Automática Contínua

> 🚨 **REGRA DE OURO DA AUTO-SINCRONIZAÇÃO:**  
> Sempre que o agente de IA realizar uma alteração, criar uma nova nota ou detectar que qualquer arquivo foi modificado:
> 1. O agente **DEVE DISPARAR A SINCRONIZAÇÃO AUTOMÁTICA IMEDIATA**:
>    ```bash
>    python second-brain-plus/scripts/auto_sync.py --now
>    ```
> 2. Este comando coordena:
>    - **Notion API / CLI:** Envia propriedades atualizadas, hashes e conteúdo de ADRs para os bancos na nuvem.
>    - **`claude-mem`:** Atualiza a linha do tempo episódica e o histórico de observações.
>    - **`graphify`:** Reconstrói as conexões da AST e as arestas do grafo de conhecimento (`.graphify/graph.json`).
> 3. Opcionalmente, o usuário pode manter o observador contínuo aberto em segundo plano:
>    ```bash
>    python second-brain-plus/scripts/auto_sync.py --watch
>    ```

---

### 🏛️ Arquitetura de Memória em 5 Camadas

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ARQUITETURA DE MEMÓRIA EM 5 CAMADAS                      │
├──────────────────────────────┬──────────────────────────────┬───────────────┤
│ Camada                       │ Finalidade                   │ Persistência  │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 1. Memória de Trabalho (RAM) │ Estado do turno ativo,       │ RAM da Sessão │
│                              │ compactado via Caveman       │ (Headroom)    │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 2. Memória Episódica (Logs)  │ Linha do tempo de sessões e  │ claude-mem /  │
│                              │ histórico de observações     │ Notion Logs   │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 3. Memória Semântica (Fatos) │ Regras de negócio, ADRs e    │ Cofre Local / │
│                              │ docs ao vivo via Context7    │ Notion Docs   │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 4. Memória Procedural (Como) │ Como executar: runbooks e    │ SKILL.md /    │
│                              │ as 4 Leis de Karpathy        │ Scripts CLI   │
├──────────────────────────────┼──────────────────────────────┼───────────────┤
│ 5. Grafo de Conhecimento     │ Relações entre entidades e   │ graphify /    │
│                              │ links sintáticos de código   │ Triplas RDF   │
└──────────────────────────────┴──────────────────────────────┴───────────────┘
```

---

### 🎙️ Sinergia "Grill-then-Persist" (`grill-me` + `second-brain-plus`)

Antes de iniciar a implementação de código complexo ou decisões de arquitetura, o agente aciona o `grill-me` para conduzir uma entrevista dialética profunda, eliminando premissas ocultas e pontos cegos. O consenso resultante é **automaticamente destilado em um ADR formal** em `.second-brain/adr/` e enviado ao Notion.

---

### 🔬 Disciplina de Engenharia Karpathy (`karpathy-guidelines`)

O agente segue rigorosamente as 4 Leis de Engenharia de Andrej Karpathy:
1. **Pense Antes de Codificar:** Verifique APIs, inspecione restrições e projete o fluxo de dados primeiro.
2. **Simplicidade Primeiro:** Escreva a menor quantidade viável de código que resolve o problema central; evite abstrações prematuras.
3. **Precisão Cirúrgica:** Altere apenas o estritamente necessário; preserve os padrões do código existente.
4. **Execução Orientada a Metas:** Valide cada hipótese com verificações reproduzíveis e testes.

---

### ⚡ Adaptação Neurodivergente (`not-today-adhd` & Orbit OS)

Quando o modo TDAH está ativo (`/second-brain tdah` ou `/second-brain focus`):
- Oculta listas longas e muralhas de texto.
- Exibe **somente 1 micro-tarefa ativa por vez (com duração de 5 a 10 minutos)**.
- Adota formatação biônica, linhas curtas de 45-65 caracteres e checagens amigáveis de Body Doubling para combater a paralisia de tarefa.

---

### 🌐 Ecossistema Oficial Notion Developer & AI Agents

A skill integra toda a infraestrutura oficial da Notion para agentes de IA:
1. **Notion CLI (`ntn` / https://ntn.dev):**
   - Comandos de alta performance: `ntn whoami`, `ntn pages get <id>`, `ntn databases query <id>`, `ntn workers deploy`.
2. **Notion Workers (`@notionhq/workers`):**
   - Funções serverless edge com gatilhos de criação de página (`onPageCreated`) e alteração de propriedades (`onPropertyChanged`).
3. **Notion MCP (Model Context Protocol) & Notion Skills:**
   - Protocolo universal para agentes de IA realizarem buscas híbridas e gravação atômica em páginas (`notion_search`, `notion_read_page`, `notion_append_block_children`).
4. **Notion Agent & Data APIs:**
   - Manipulação nativa da árvore de blocos (parágrafos, cabeçalhos, toggles, callouts, tabelas) e APIs corporativas de Admin (Audit Logs e SCIM).
   - Consulte o guia completo em [docs/notion_developer_suite.md](docs/notion_developer_suite.md).
5. **Blueprint Padrão Oficial 2026 para Devs & IA:**
   - Versionado nativamente em `templates/notion/second_brain_blueprint.json`.
   - Inclui os 7 Bancos Mestres (Projetos, Tarefas, Notas/ADRs, Recursos, Áreas Dev, Rotina Operacional Dev, Diário de Sessões de IA).
   - Provisionamento instantâneo em qualquer novo projeto via `build_notion_dashboard.py` e preenchimento automático das memórias daquele projeto via `setup_and_sync.py`.

---

### 🐙🦊 Sincronização Remota Multi-Plataforma Git (GitHub `gh` e GitLab `glab`)

O Second Brain Plus oferece backup criptográfico e imutável via Git no **GitHub** e no **GitLab**:
1. **GitHub CLI (`gh` / https://cli.github.com/):**
   - Integração nativa com `gh auth status`, `gh repo view` e `gh repo create`.
2. **GitLab CLI (`glab` / https://docs.gitlab.com/cli/):**
   - Suporte completo com `glab auth status`, `glab repo view` e `glab repo create`.
3. **Gestão de Visibilidade (Privado vs. Público):**
   - Padrão **Privado** para salvaguardar anotações confidenciais, regras de negócio e ADRs internos.
   - Suporte a **Jardins Digitais Públicos** para documentações abertas e bibliotecas comunitárias.
4. **Diagnóstico Proativo ("Precisa de Algo a Mais?"):**
   - O motor audita o `.gitignore` contra vazamento de segredos, alerta sobre repositórios públicos acidentais, valida commits pendentes (*ahead/behind*) e recomenda workflows de CI/CD para backup automatizado.
   - Consulte o guia técnico em [docs/git_remote_sync_guide.md](docs/git_remote_sync_guide.md).

---

### ⚙️ Exemplos de Execução via Linha de Comando

```bash
# Salvar memória técnica atômica
python second-brain-plus/scripts/cli.py save memory "PostgreSQL 16 de produção roda na porta 5433"

# Registrar Decisão de Arquitetura (ADR) imutável
python second-brain-plus/scripts/cli.py adr "Adoção do Redis para Cache" --rationale "Garantir respostas < 5ms"

# Ver telemetria e saúde do segundo cérebro
python second-brain-plus/scripts/cli.py status

# Executar auditoria proativa do Git remoto (GitHub/GitLab e checagem de privacidade)
python second-brain-plus/scripts/cli.py git-status

# Enviar alterações do cofre para o repositório remoto
python second-brain-plus/scripts/cli.py git-sync

# Disparar sincronização manual imediata
python second-brain-plus/scripts/cli.py sync
```
