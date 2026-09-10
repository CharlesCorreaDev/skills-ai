# Foundry VTT RPG Systems Knowledge Base 🎲📚
> **Comprehensive System Architecture & Development Directory**  
> *Base de Conhecimento de Sistemas de RPG para Foundry VTT por GM Charles Corrêa*

---

## 🇺🇸 English

### 📌 Overview & Architecture Directory

This knowledge base catalogs the technical architectures, official repositories, `Hooks`, `DataModel` peculiarities, roll evaluation pipelines, and developer pitfalls for **over 60 of the most popular RPG systems** in the Foundry Virtual Tabletop ecosystem.

Its purpose is to guide developers, module creators, and AI Agents in avoiding runtime conflicts, data migration errors, and license/policy infringements.

---

### 📂 System Guides by Category

| Category | Guide File | Major Systems Covered |
| :--- | :--- | :--- |
| **01. Heroic Fantasy, D20 & Duality Dice** | [`01-d20-and-fantasy.md`](01-d20-and-fantasy.md) | D&D 5e (Official + PT-BR), D&D 3.5e, Pathfinder 2e (Rule Elements), Daggerheart (2d12 Hope & Fear), Tormenta 20, Old Dragon 2e, Draw Steel (MCDM), Advanced Roleplay System (Rolemaster). |
| **02. Storyteller & World of Darkness** | [`02-storyteller-and-world-of-darkness.md`](02-storyteller-and-world-of-darkness.md) | WoD20 (Vampire, Werewolf, Mage), Vampire V5, WoD5E, WoD6E, Changeling 5E, KULT: Divinity Lost. |
| **03. Investigation & Cosmic Horror** | [`03-investigative-and-horror.md`](03-investigative-and-horror.md) | Call of Cthulhu 7e, Delta Green, GUMSHOE, Cthulhu Dark, Arkham Horror RPG. |
| **04. Year Zero Engine (Free League)** | [`04-year-zero-engine.md`](04-year-zero-engine.md) | Year Zero Roller, Alien RPG, Blade Runner, Vaesen, Twilight: 2000, Forbidden Lands, Coriolis (TGD, Overhaul, YZE), Mutant: Year Zero, Dragonbane, The Walking Dead Universe (TWDU). |
| **05. Sci-Fi, Cyberpunk & Pulp** | [`05-pulp-scifi-and-cyberpunk.md`](05-pulp-scifi-and-cyberpunk.md) | Cyberpunk RED Core, Cyberpunk 2020, Shadowrun 5e/6e, CBR+PNK, Invincible RPG, Triangle Agency, Cosmere RPG, Warhammer 40k: Wrath & Glory. |
| **06. Narrative, PbtA & FitD** | [`06-narrative-and-pbta-fitd.md`](06-narrative-and-pbta-fitd.md) | Blades in the Dark, PbtA Generic, City of Mist, Fate Core/Accelerated, Perils & Princesses (*Perigos & Princesas*). |
| **07. Generic & Rules-Light Systems** | [`07-generic-and-rules-light.md`](07-generic-and-rules-light.md) | GURPS 4e Game Aid, Savage Worlds (SWADE Official + PT-BR), Custom System Builder (CSB), Simple Worldbuilding, TinyD6, 3D&T Alpha, 3D&T Victory, ABEA, Ars Magica 5e, The Witcher TRPG, Shadow of the Demon Lord / Weird Wizard. |

---

### 🔍 Dynamic Discovery of Unlisted Systems

If a developer or user requests support for an RPG system that is **not** currently listed in this knowledge base:
1. The AI Agent **MUST consult the official Foundry VTT Systems Directory**: [**https://foundryvtt.com/packages/systems**](https://foundryvtt.com/packages/systems).
2. Locate the package identifier (`id`), supported core versions (`compatibility`), manifest URL (`manifest`), and source code repository (GitHub, GitLab, etc.).
3. Inspect `system.json` and the system's schema/templates to understand the actor/item data models before generating code or scripts.

---

### ⚠️ Common Pitfalls & Best Practices

1. **Avoid Direct Method Overwriting:** Never replace class methods (`Actor.prototype.prepareDerivedData` or `Item.prototype.roll`) directly. Always use the `libWrapper` library to ensure compatibility with other modules.
2. **Respect System DataModels:** Modern systems (v10+) use `TypeDataModel`. Do not inject undeclared properties directly into `system`; use module flags (`flags.<module-id>.<field>`) instead.
3. **Internationalization (i18n):** Never hardcode strings in UI templates or JavaScript logic. Always use `game.i18n.localize("KEY.PATH")` or `{{localize 'KEY.PATH'}}`.
4. **System-Specific Effect Pipelines:** Check whether the system uses standard Foundry `ActiveEffect` objects or custom modifier pipelines (e.g., PF2e Rule Elements).

---
---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral & Índice dos Sistemas

Esta base de conhecimento cataloga a arquitetura técnica, repositórios oficiais, ganchos (`Hooks`), particularidades de `DataModel`, tratamento de rolagens e armadilhas comuns para **mais de 60 dos sistemas mais populares** do ecossistema Foundry Virtual Tabletop.

Seu propósito é orientar desenvolvedores, criadores de módulos e Agentes de IA a evitar conflitos de execução, erros de migração de esquemas e violações de termos de licença.

---

### 📂 Guias de Sistemas por Categoria

| Categoria | Arquivo do Guia | Principais Sistemas Cobertos |
| :--- | :--- | :--- |
| **01. Fantasia Heroica, D20 & Duality Dice** | [`01-d20-and-fantasy.md`](01-d20-and-fantasy.md) | D&D 5e (Oficial + PT-BR), D&D 3.5e, Pathfinder 2e (Rule Elements), Daggerheart (2d12 Hope & Fear), Tormenta 20, Old Dragon 2e, Draw Steel (MCDM), Advanced Roleplay System (Rolemaster). |
| **02. Storyteller & Mundo das Trevas** | [`02-storyteller-and-world-of-darkness.md`](02-storyteller-and-world-of-darkness.md) | WoD20 (Vampiro, Lobisomem, Mago), Vampiro V5, WoD5E, WoD6E, Changeling 5E, KULT: Divinity Lost. |
| **03. Investigação & Horror Cósmico** | [`03-investigative-and-horror.md`](03-investigative-and-horror.md) | Call of Cthulhu 7e, Delta Green, GUMSHOE, Cthulhu Dark, Arkham Horror RPG. |
| **04. Year Zero Engine (Fria Ligan)** | [`04-year-zero-engine.md`](04-year-zero-engine.md) | Year Zero Roller, Alien RPG, Blade Runner, Vaesen, Twilight: 2000, Forbidden Lands, Coriolis (TGD, Overhaul, YZE), Mutant: Year Zero, Dragonbane, The Walking Dead Universe (TWDU). |
| **05. Sci-Fi, Cyberpunk & Pulp** | [`05-pulp-scifi-and-cyberpunk.md`](05-pulp-scifi-and-cyberpunk.md) | Cyberpunk RED Core, Cyberpunk 2020, Shadowrun 5e/6e, CBR+PNK, Invincible RPG, Triangle Agency, Cosmere RPG, Warhammer 40k: Wrath & Glory. |
| **06. Narrativos, PbtA & FitD** | [`06-narrative-and-pbta-fitd.md`](06-narrative-and-pbta-fitd.md) | Blades in the Dark, PbtA Genérico, City of Mist, Fate Core/Accelerated, Perigos & Princesas (*Perils & Princesses*). |
| **07. Genéricos & Regras Customizadas** | [`07-generic-and-rules-light.md`](07-generic-and-rules-light.md) | GURPS 4e Game Aid, Savage Worlds (SWADE Oficial + PT-BR), Custom System Builder (CSB), Simple Worldbuilding, TinyD6, 3D&T Alpha, 3D&T Victory, ABEA, Ars Magica 5e, The Witcher TRPG, Shadow of the Demon Lord / Weird Wizard. |

---

### 🔍 Descoberta Dinâmica de Sistemas Não Catalogados

Caso o desenvolvedor ou usuário solicite suporte ou desenvolvimento para um sistema de RPG que **não** conste nesta base de conhecimento:
1. O Agente de IA **DEVE OBRIGATORIAMENTE consultar o Diretório Oficial de Sistemas do Foundry VTT**: [**https://foundryvtt.com/packages/systems**](https://foundryvtt.com/packages/systems).
2. Localizar o identificador do pacote (`id`), versões suportadas do Foundry (`compatibility`), link do manifesto (`manifest`) e o repositório oficial de código-fonte (GitHub, GitLab, etc.).
3. Inspecionar o `system.json` e os esquemas/templates do sistema para entender a árvore de dados antes de escrever código ou macros.

---

### ⚠️ Armadilhas Comuns e Boas Práticas

1. **Evitar Sobrescrita Direta de Métodos:** Nunca substitua métodos de classe (`Actor.prototype.prepareDerivedData` ou `Item.prototype.roll`) com atribuição direta. Utilize sempre a biblioteca `libWrapper` para garantir compatibilidade com múltiplos módulos.
2. **Respeitar os DataModels do Sistema:** Em versões modernas do Foundry (v10+), sistemas utilizam `TypeDataModel`. Não tente injetar campos diretamente em `system` sem declarar um schema; use `flags.<seu-modulo>.<campo>`.
3. **Internacionalização (i18n):** Nunca utilize textos fixos diretamente no código JavaScript ou templates HTML. Use sempre `game.i18n.localize("CHAVE.CAMPO")` ou `{{localize 'CHAVE.CAMPO'}}`.
4. **Active Effects Específicos do Sistema:** Verifique se o sistema suporta Active Effects padrão do Foundry ou se implementa um pipeline proprietário de modificadores (ex: Rule Elements do PF2e).
