# Base de Conhecimento de Sistemas de RPG para Foundry VTT 🎲📚
> *Criado por Mestre Charles Corrêa — Master of Foundry VTT*

---

## 📌 Visão Geral & Índice dos Sistemas

Esta base de conhecimento cataloga a arquitetura técnica, links oficiais de repositórios, ganchos (`Hooks`), peculiaridades de `DataModel`, tratamento de rolagens e pontos de atenção para mais de 60 dos sistemas mais populares da comunidade do Foundry Virtual Tabletop.

O objetivo é orientar o desenvolvedor e o Agente de IA para evitar conflitos de módulos, erros de migração de esquemas e violações de regras/licenças de terceiros.

---

## 📂 Guias por Categoria

| Categoria | Arquivo | Principais Sistemas Cobertos |
| :--- | :--- | :--- |
| **01. Fantasia Heroica, D20 & Duality Dice** | [`01-d20-and-fantasy.md`](01-d20-and-fantasy.md) | D&D 5e, D&D 3.5e, Pathfinder 2e, Daggerheart (2d12 Hope & Fear), Tormenta 20, Old Dragon 2e, Draw Steel (MCDM), Advanced Roleplay System. |
| **02. Storyteller & Mundo das Trevas** | [`02-storyteller-and-world-of-darkness.md`](02-storyteller-and-world-of-darkness.md) | WoD20, Vampire V5, WoD5E, WoD6E, Changeling 5E, KULT: Divinity Lost. |
| **03. Investigação & Horror Cósmico** | [`03-investigative-and-horror.md`](03-investigative-and-horror.md) | Call of Cthulhu 7e, Delta Green, GUMSHOE, Cthulhu Dark, Arkham Horror RPG. |
| **04. Year Zero Engine (Fria Ligan)** | [`04-year-zero-engine.md`](04-year-zero-engine.md) | Year Zero Roller, Alien RPG, Blade Runner, Vaesen, Twilight 2000, Forbidden Lands, Coriolis (TGD, Overhaul), Mutant Year Zero, Dragonbane, The Walking Dead Universe (TWDU). |
| **05. Sci-Fi, Cyberpunk & Pulp** | [`05-pulp-scifi-and-cyberpunk.md`](05-pulp-scifi-and-cyberpunk.md) | Cyberpunk RED, Cyberpunk 2020, Shadowrun 5e/6e, CBR+PNK, Invincible RPG, Triangle Agency, Cosmere RPG, Warhammer 40k Wrath & Glory. |
| **06. Narrativos, PbtA & FitD** | [`06-narrative-and-pbta-fitd.md`](06-narrative-and-pbta-fitd.md) | Blades in the Dark, PbtA Generic, City of Mist, Fate Core/Accelerated, Perils & Princesses. |
| **07. Genéricos & Regras Customizadas** | [`07-generic-and-rules-light.md`](07-generic-and-rules-light.md) | GURPS 4e Game Aid, Savage Worlds (SWADE & SWADE BR), Custom System Builder (CSB), Simple Worldbuilding, TinyD6, 3D&T Alpha, 3D&T Victory, ABEA, Ars Magica 5e, Shadow of the Demon Lord / Weird Wizard, The Witcher TRPG. |

---

## ⚠️ Armadilhas Comuns e Boas Práticas ao Desenvolver para Sistemas

1. **Evitar Sobrescrita Direta de Métodos:** Nunca substitua métodos de classe (`Actor.prototype.prepareDerivedData` ou `Item.prototype.roll`) com atribuição direta. Utilize sempre a biblioteca `libWrapper` para garantir compatibilidade com múltiplos módulos.
2. **Respeitar os DataModels do Sistema:** Em versões modernas do Foundry (v10+), sistemas como D&D 5e e PF2e utilizam `TypeDataModel`. Não tente injetar campos diretamente em `system` sem declarar um schema ou usar `flags.<seu-modulo>.<campo>`.
3. **Internacionalização (i18n):** Nunca utilize textos fixos diretamente no código JavaScript ou templates HTML. Use sempre `game.i18n.localize("CHAVE.CAMPO")` ou `{{localize 'CHAVE.CAMPO'}}`.
4. **Active Effects Específicos do Sistema:** Verifique se o sistema suporta Active Effects padrão do Foundry ou se implementa um pipeline proprietário de modificadores (ex: PF2e Rule Elements).
