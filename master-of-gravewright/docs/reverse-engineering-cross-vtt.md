# Guia de Engenharia Reversa e Adaptação Cross-VTT para Gravewright

Este guia estabelece o protocolo técnico e prático para realizar **engenharia reversa** em módulos, sistemas e automações de outros Virtual Tabletops (especialmente **Foundry VTT**, **Roll20** e **Fantasy Grounds**) e adaptá-los com fidelidade mecânica para a arquitetura do **Gravewright VTT**.

---

## 🛠️ Ferramental de Engenharia Reversa (REA)
- **REA CLI & MCP:** [`rea-agents`](https://github.com/morluto/rea) e [`inematds/rea-engenharia-reversa`](https://github.com/inematds/rea-engenharia-reversa).
- **Inspecione Repositórios Oficiais:** Clone temporariamente o código-fonte original (`git clone --depth 1 <url>`) para inspecionar schemas de dados, hooks de eventos e lógica de cálculo.
- **Porte Ético Obrigatório:** Aplique rigorosamente as diretrizes em [`docs/pt-BR/ethical-module-porting.md`](docs/pt-BR/ethical-module-porting.md). Extraia a lógica e o comportamento; **NÃO copie ativos de arte, textos proprietários ou trademarks sem autorização**.

---

## 🔄 Matriz de Mapeamento Cross-VTT (Foundry VTT ➔ Gravewright VTT)

| Conceito no Foundry VTT | Arquitetura no Gravewright VTT | Como Adaptar |
|---|---|---|
| **`Actor` / `TypeDataModel`** | **`actors` (Django Model + `services.py`)** | As propriedades de atributos, perícias e PVs viram campos ou dicionários no model `Actor` do Gravewright. |
| **`ActorSheet` / `ApplicationV2`** | **`actor.sheet` (Jinja2 + JS ESModules)** | A renderização reativa de ficha no Gravewright é feita através do template Jinja2 e eventos WebSocket. |
| **`Item` / `TypeDataModel`** | **`items` (Django Model + `item.sheet`)** | Armas, magias, armaduras e talentos viram itens canônicos associados ao ator via drag-and-drop. |
| **`Token` / `TokenDocument`** | **`tokens` (HTML5 Canvas + WebSockets)** | Posição (x, y), visão, luz e condições são sincronizados via Django Channels em tempo real. |
| **`Scene` / `Grid` / `Tiles`** | **`maps` (Universal VTT / UVTT)** | Importação de mapas com paredes e iluminação no formato Universal VTT (`.dd2vtt`, `.df2vtt`). |
| **`JournalEntry` / `JournalEntryPage`** | **`journals`** | Diários, handouts e notas secretas do Mestre (GM Exclusive por padrão). |
| **`Combat` / `CombatTracker`** | **`combat`** | Iniciativa e ordem de turnos orquestrados no servidor. |
| **`RollTable` / `Cards`** | **`cards` & `dice`** | Baralhos (compra, descarte, embaralhamento) e fórmulas de dados (`Roll` via backend seguro). |
| **`Hooks.on()` / `Hooks.callAll()`** | **`realtime` (Django Channels Events)** | O Gravewright despacha eventos orientados a domínio através de WebSockets para as mesas conectadas. |

---

## 🔬 Protocolo de Estudo em 4 Fases

1. **Fase 1 — Desconstrução do Modelo de Dados (Data Model):**
   - Inspecione arquivos `template.json`, schemas `DataModel` ou `models.py` da origem.
   - Identifique tipos primitivos (`integer`, `string`, `boolean`, `dictionary`).
   - Mapeie campos calculados (ex: modificador derivado de atributo) para serem gerados nos `services.py` do Gravewright.

2. **Fase 2 — Mapeamento do Fluxo de Eventos (Event Flow):**
   - Identifique quais ações dependem de validação do servidor (ex: gastar mana, sofrer dano, rolar ataque).
   - Transfira as validações para o backend Django (`services.py`), prevenindo trapaças ou estados dessincronizados entre jogadores.

3. **Fase 3 — Adaptação da Interface do Usuário (UI/UX):**
   - Utilize a skill `bootstrap-ux-ui-plus` para estruturar a ficha ou painel.
   - Aplique CSS isolado com namespace (ex: `.meu-modulo-container`) para não vazar estilos no canvas do Gravewright.

4. **Fase 4 — Blindagem de Segurança & Anti-Alucinação:**
   - Execute a auditoria em 6 fases com `cloudflare/security-audit-skill`.
   - Garanta que regras, dados e constantes estejam ancorados na ontologia real com `NVIDIA/auto-ontology`.
