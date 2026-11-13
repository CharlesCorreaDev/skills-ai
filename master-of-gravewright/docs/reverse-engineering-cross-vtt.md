# Guia de Engenharia Reversa e Adaptação Cross-VTT para Gravewright

Este guia estabelece o protocolo técnico e prático para realizar **engenharia reversa** em módulos, sistemas e automações de outros Virtual Tabletops (especialmente **Foundry VTT**, **Roll20** e **Fantasy Grounds**) e adaptá-los com fidelidade mecânica para a arquitetura de **pacotes e extensões do Gravewright VTT**.

> [!IMPORTANT]
> **Arquitetura de Extensão:** Todo sistema ou módulo de regras deve ser empacotado como uma **extensão isolada** (via pacote instalado com `manifest.json`), **NUNCA alterando os arquivos internos do core do Gravewright**. O core é estável e agnóstico a sistemas.

---

## 🛠️ Ferramental de Engenharia Reversa (REA) & Web Runtime Reversing
- **REA CLI & MCP:** Utilize ferramentas REA (`rea-agents`, Ghidra, Cutter) para inspecionar binários, scripts e pacotes de terceiros.
- **Estratégia para Web SPAs e Bundles ("Fight the Delivery, Not the Runtime"):**
  - Quando bundles JS forem minificados ou tiverem anti-debugging, intercepte no trânsito (`mitmproxy`) ou injete hooks pré-bootstrap via Playwright (`addInitScript`).
  - Utilize desobfuscação por AST (`webcrack`, `ast-grep`) para recuperar a árvore sintática antes de analisar lógicas complexas.
- **Inspecione Repositórios Oficiais:** Clone temporariamente o código-fonte original (`git clone --depth 1 <url>`) para inspecionar schemas de dados, hooks de eventos e lógica de cálculo.
- **Porte Ético Obrigatório:** Aplique rigorosamente as diretrizes em [`docs/pt-BR/ethical-module-porting.md`](pt-BR/ethical-module-porting.md). Extraia a mecânica e a lógica funcional; **NÃO copie textos proprietários, imagens protegidas ou marcas registradas**.
- **REA CLI & MCP:** Utilize ferramentas REA para inspecionar binários, scripts e pacotes de terceiros.
- **Inspecione Repositórios Oficiais:** Clone temporariamente o código-fonte original (`git clone --depth 1 <url>`) para inspecionar schemas de dados, hooks de eventos e lógica de cálculo.
- **Porte Ético Obrigatório:** Aplique rigorosamente as diretrizes em [`docs/pt-BR/ethical-module-porting.md`](pt-BR/ethical-module-porting.md). Extraia a mecânica e a lógica funcional; **NÃO copie textos proprietários, imagens protegidas ou marcas registradas**.

---

## 🔄 Matriz de Mapeamento Cross-VTT (Foundry VTT ➔ Gravewright VTT)

| Conceito no Foundry VTT | Arquitetura no Gravewright VTT | Como Adaptar Corretamente |
|---|---|---|
| **`Actor` / `TypeDataModel`** | **`system.actorTypes` no `manifest.json` + `api.actors.sheet`** | Declare os tipos no `manifest.json` sob `"system": { "actorTypes": [...] }`. A carga e gravação dos dados ocorrem via `api.actors.sheet(actorId)` e `api.actors.saveSheet(actorId, patch, { expectedRevision })`. |
| **`ActorSheet` / `ApplicationV2`** | **Superfície `actor.sheet` (ES Module `register`)** | Registre a ficha do sistema com `register("actor.sheet", { mode: "replace", types: ["character"], mount(ctx) {...} })`. Monte o DOM reativo com os dados do ator e escute eventos via `api.events.on(...)`. |
| **`Item` / `TypeDataModel`** | **`system.itemTypes` no `manifest.json` + `item.sheet`** | Declare os tipos sob `"system": { "itemTypes": [...] }`. Fichas de itens são registradas em `register("item.sheet", ...)`. |
| **`Token` / `TokenDocument`** | **`tokens` (Canvas PixiJS / WebSockets) & `token.sheet`** | Posição, visão, luz e elevação são renderizados no canvas e gerenciados pelo host. Extensões podem registrar superfícies `token.sheet`. |
| **`Scene` / `Grid` / `Tiles`** | **`maps` (Universal VTT / UVTT) & `scene.overlay`** | Importação de mapas com paredes e luz via UVTT (`.dd2vtt`). Renderizações visuais customizadas usam `register("scene.overlay", ...)`. |
| **`Combat` / `CombatTracker`** | **`system.combat` no `manifest.json` ou Provider no Servidor** | Declare a fórmula de iniciativa no `manifest.json` (`"combat": { "formula": "1d20 + @initiative" }`). Para lógicas avançadas de turnos e efeitos, registre um combat provider via app Django com `api.combat.register_provider`. |
| **`Hooks.on()` / `Hooks.callAll()`** | **`api.events.on(eventName, handler)` com `signal`** | Escute eventos reativos da mesa (ex: `actors.changed`, `combat.round`). Sempre passe `{ signal }` para desregistrar automaticamente ao fechar o componente. |
| **Lógica de Regras no Backend** | **`django.apps` + `api.systems.register_api`** | Operações complexas no servidor são registradas no `ready()` da `AppConfig` do seu pacote e invocadas no navegador com `api.system.call("meu-sistema.regra", params)`. |

---

## 🔬 Protocolo de Adaptação em 4 Fases

1. **Fase 1 — Desconstrução do Modelo de Dados (Data Model):**
   - Inspecione `template.json`, schemas `DataModel` ou structs do VTT de origem.
   - Identifique campos essenciais: atributos base, atributos derivados, listas de perícias e inventário.
   - Mapeie como esses campos serão organizados no JSON da ficha do Gravewright.

2. **Fase 2 — Definição do Pacote de Sistema no `manifest.json`:**
   - Crie o manifesto oficial com `sdk: { "requires": ">=1.0.0 <2.0.0", "tested": "1.0.0" }`.
   - Adicione o bloco `system` declarando `actorTypes`, `itemTypes` e `combat`:
   ```json
   {
     "id": "charles.tormenta20",
     "name": "Tormenta20",
     "version": "0.1.0",
     "sdk": { "requires": ">=1.0.0 <2.0.0", "tested": "1.0.0" },
     "entry": "main.js",
     "description": "Sistema de RPG Tormenta20 para Gravewright VTT.",
     "author": "Charles Corrêa",
     "license": "MIT",
     "system": {
       "actorTypes": [
         { "id": "character", "label": "Personagem" },
         { "id": "npc", "label": "Ameaça" }
       ],
       "itemTypes": [
         { "id": "equipment", "label": "Equipamento", "icon": "Backpack" },
         { "id": "power", "label": "Poder", "icon": "Sparkles" }
       ],
       "combat": {
         "formula": "1d20 + @iniciativa",
         "manualInput": "number"
       }
     }
   }
   ```

3. **Fase 3 — Implementação da Interface Reativa (`main.js`):**
   - Exporte o ciclo de vida oficial `export default { start, register, stop }`.
   - Registre o `actor.sheet` substituindo o layout padrão para os tipos declarados:
   ```javascript
   export default {
     start({ styles }) {
       styles.use("styles.css");
     },
     register({ register }) {
       register("actor.sheet", {
         mode: "replace",
         types: ["character"],
         mount: async ({ root, api, entityId, signal }) => {
           const sheetData = await api.actors.sheet(entityId);
           // Renderiza a ficha no root
         }
       });
     },
     stop() {}
   };
   ```

4. **Fase 4 — Persistência e Integridade de Dados:**
   - Ao gravar edições na ficha, utilize controle otimista de revisão com `expectedRevision`.
   - Caso receba um erro de `conflict`, faça o re-fetch dos dados mais recentes, faça o merge das alterações e reenvie. Nunca sobrescreva cegamente.
