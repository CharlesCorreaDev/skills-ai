---
name: master-of-gravewright
description: Suíte de Engenharia Reversa, Desenvolvimento de Sistemas, Módulos, Extensões, Itens, Compêndios e Diagnóstico de Ambiente para o Gravewright VTT (Virtual Tabletop Open-Source em Python/Django).
---

# Master of Gravewright VTT ⚔️🎲

> **Versão:** `0.4.0-beta`  
> **Status:** Beta  
> **Compatibilidade:** Gravewright v0.3.0 a v0.4.x+  
> **Arquitetura Base:** Python 3.14+, Astral `uv`, Django 6.1, Jinja2, Datastar, PixiJS, Django Channels (WebSockets), JavaScript ESModules e SQLite.

---

## 🎯 Visão Geral / Overview

A skill **`master-of-gravewright`** é a inteligência técnica definitiva para desenvolvedores, Mestres e criadores de conteúdo que desejam construir **módulos**, **extensões**, **sistemas de RPG**, **compêndios de regras**, **fichas de personagens**, **clocks**, **mapas universais (UVTT)** e automações para o **[Gravewright VTT](https://gravewright.com/)** — o Virtual Tabletop open-source brasileiro desenvolvido em Python/Django por **Rodrigo Tristão Porfírio**.

---

## 🛠️ Mandatos de Instalação e Ambiente

### 1. Diagnóstico Ativo do Ambiente Local
Quando esta skill for ativada ou o usuário solicitar setup do ambiente:
1. O agente **DEVE executar o diagnóstico automatizado**:
   ```bash
   python master-of-gravewright/scripts/setup_dev_env.py --check
   ```
2. Ferramental canônico do Gravewright:
   - **Python 3.14+**: Interpretador com tipagem avançada e performance assíncrona.
   - **Astral `uv`**: Gerenciador de pacotes e ambientes virtuais ultrarrápido (`uv sync`, `uv run`).
   - **Django 6.1**: Backend de orquestração e ORM com SQLite (`data/gravewright.sqlite3`).
   - **Datastar + PixiJS**: Reatividade hiperleve e canvas 2D de alta performance.
   - **Ruff**: Linter e formatador de código Python via Astral (`uv add --dev ruff`).

### 2. Instalação Recomendada de Skills Companheiras
Para enriquecer a experiência de engenharia de software no ecossistema Gravewright:

1. **`python-dev-expert` (`v0.4.0-beta`):**
   - Para programação backend Django, ORM, models, services, migrations e testes.
   - Instalação: `npx skills@latest add CharlesCorreaDev/skills-ai --skill=python-dev-expert`
2. **`bootstrap-ux-ui-plus` (`v0.3.0-beta`):**
   - Para estilização e ergonomia de interfaces web e painéis do GM em Jinja2/HTML5 com acessibilidade WCAG 2.2 AA.
   - Instalação: `npx skills@latest add CharlesCorreaDev/skills-ai --skill=bootstrap-ux-ui-plus`
3. **Git Workflows & Version Control (`git-pr-workflows` / `github`):**
   - Para governança de repositórios de módulos, tags de release e empacotamento para o Marketplace.
   - Instalação: `npx skills@latest add github`
   - Consulte [Guia de Versionamento Git e Empacotamento](docs/git-guide.md).
4. **`cloudflare/security-audit-skill` & `NVIDIA/auto-ontology`:**
   - Auditoria de segurança de permissões do GM vs Jogadores e ancoragem ontológica sem inventar métricas/regras inexistentes.
   - Instalação: `npx skills@latest add cloudflare/security-audit-skill` e `npx skills@latest add NVIDIA/auto-ontology`

---

## 📜 Manifesto Oficial (`manifest.json`) - Regras do Schema 2020-12

Todo pacote instalado no Gravewright é validado rigorosamente contra o schema JSON Schema 2020-12 (`contracts/schemas/manifest.json`) com `additionalProperties: false`.

### Regras Mandatórias:
- **Campos Obrigatórios Gerais:** `id`, `name`, `version`, `sdk`, `description`, `author`, `license`.
- **`id`:** Deve casar com o regex `^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)+$` (ex: `autor.modulo` ou `charles.meu-modulo`).
- **`version`:** Exatamente semver numérico `X.Y.Z` (sem sufixos como `-beta`).
- **`sdk`:** Objeto `{ "requires": ">=1.0.0 <2.0.0", "tested": "1.0.0" }`. Faixa de compatibilidade sem operadores `^`, `~`, `*` ou `||`.
- **`entry`:** Obrigatório para módulos client/browser e sistemas; **proibido** em extensões com bloco `django`.
- **CSS:** Não é declarado no manifest. É carregado dinamicamente via `styles.use("styles.css")`.
- **Proibidos no manifest:** `title`, `compatibility`, `scripts`, `styles`, `django_app`.

### Manifesto Mínimo de Módulo Browser:
```json
{
  "id": "charles.meu-modulo",
  "name": "Meu Módulo",
  "version": "0.1.0",
  "sdk": { "requires": ">=1.0.0 <2.0.0", "tested": "1.0.0" },
  "entry": "main.js",
  "description": "Descrição curta do módulo.",
  "author": "Charles Corrêa",
  "license": "MIT"
}
```

### Manifesto de Pacote de Sistema:
```json
{
  "id": "charles.meu-sistema",
  "name": "Meu Sistema de RPG",
  "version": "0.1.0",
  "sdk": { "requires": ">=1.0.0 <2.0.0", "tested": "1.0.0" },
  "entry": "main.js",
  "description": "Sistema completo para Gravewright VTT.",
  "author": "Charles Corrêa",
  "license": "MIT",
  "system": {
    "actorTypes": [
      { "id": "character", "label": "Personagem" },
      { "id": "monster", "label": "Criatura" }
    ],
    "itemTypes": [
      { "id": "weapon", "label": "Arma", "icon": "Sword" },
      { "id": "spell", "label": "Magia", "icon": "Sparkles" }
    ],
    "combat": {
      "formula": "1d20 + @combat.initiative",
      "manualInput": "number"
    }
  }
}
```

---

## 🔄 Ciclo de Vida do Runtime JS (`start / register / stop`)

O arquivo entry (ex: `main.js`) é importado como ES Module e **DEVE** exportar como default as funções de ciclo de vida:

```javascript
export default {
  start({ styles }) {
    // Carrega estilos isolados
    styles.use("styles.css");
  },

  register({ register }) {
    // Superfícies suportadas: actor.directory, actor.sheet, token.sheet, item.directory,
    // item.sheet, journal.sheet, scene.directory, scene.controls, scene.overlay,
    // chat.log, combat.tracker, preferences, table.interface.
    register("actor.directory", async ({ root, api, signal }) => {
      const label = root.ownerDocument.createElement("p");
      label.className = "meu-modulo-contador";
      root.append(label);

      const render = (actors) => {
        if (!signal.aborted) label.textContent = `Atores visíveis: ${actors.length}`;
      };

      render(await api.actors.list());
      api.events.on("actors.changed", (snapshot) => render(snapshot.actors));
    });

    // Ficha de sistema:
    register("actor.sheet", {
      mode: "replace",
      types: ["character"],
      mount: async ({ root, api, entityId, signal }) => {
        const sheet = await api.actors.sheet(entityId);
        // Renderiza ficha e persiste com api.actors.saveSheet(entityId, patch, { expectedRevision })
      }
    });
  },

  stop() {
    // O host descarta estilos, raízes montadas e handles de API automaticamente
  }
};
```

---

## 🐍 Extensões Django (`django.apps`)

Para extensões que registram APIs ou models no backend:
- Declaradas sob `"django": { "apps": ["pacote_server.apps.PacoteServerConfig"], "requirements": [] }`.
- Sem bloco `entry`, `system` ou `locales`.
- A inicialização ocorre dentro de `ready()` da `AppConfig`, registrando operações com `api.systems.register_api`. O core do Gravewright **NUNCA** deve ser modificado.

---

## 🚀 Como Criar Módulos e Extensões com Scaffolding

```bash
# 1. Módulo de Navegador:
python master-of-gravewright/scripts/setup_dev_env.py --create-module "charles.meu-modulo" --type browser --author "Charles Corrêa"

# 2. Extensão Django:
python master-of-gravewright/scripts/setup_dev_env.py --create-module "charles.meu-sistema" --type django --author "Charles Corrêa"
```

---

## 🌐 Modern Web Guidance & WebMCP no Gravewright VTT

O cliente do Gravewright VTT roda em navegadores modernos via ES Modules nativos, Datastar e PixiJS. O agente DEVE seguir o padrão **[GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)**:
- **Instalação:** `npx modern-web-guidance@latest install` ou globalmente `npm install -g modern-web-guidance`.
- **Auditoria de Superfícies (`actor.sheet`, `item.sheet`, `scene.overlay`):**
  - Execute `modern-web-guidance legacy-scan <diretório-do-modulo>` para evitar seletores ou eventos DOM obsoletos.
  - Utilize CSS Container Queries para fichas de atores responsivas que funcionam tanto em janelas desacopladas quanto em overlays de cena.
  - Adote o padrão **WebMCP** (`agentic-javascript-tools` do Chrome) para registrar e expor ferramentas de automação do VTT diretamente aos agentes de IA no navegador.

---

## 📚 Documentação Técnica Integrada (Offline em EN e pt-BR)

- **Engenharia & Arquitetura:** [Guia de Engenharia Reversa Cross-VTT](docs/reverse-engineering-cross-vtt.md) • [Guia de Banco de Dados: SQLite](docs/database-guide.md) • [Guia de Versionamento Git e Empacotamento](docs/git-guide.md) • [Aviso Legal de Licença Upstream](docs/NOTICE.md)
- **Guias Oficiais Upstream:** Manuais offline em [`docs/en/`](docs/en/) e [`docs/pt-BR/`](docs/pt-BR/) espelhando a arquitetura e APIs do Gravewright VTT sob licença GPL-3.0-only.
