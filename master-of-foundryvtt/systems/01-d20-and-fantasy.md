# Sistemas de Fantasia Heroica, D20 e Duality Dice para Foundry VTT ⚔️🧙‍♂️
> *Base de Conhecimento — Master of Foundry VTT by GM Charles Corrêa*

---

## 1. Dungeons & Dragons 5th Edition (dnd5e)
- **Repositórios:**
  - Sistema Oficial: [https://github.com/foundryvtt/dnd5e](https://github.com/foundryvtt/dnd5e)
  - Módulo de Tradução PT-BR (FVTT Brasil): [https://gitlab.com/fvtt-brasil/dnd5e/-/tree/master](https://gitlab.com/fvtt-brasil/dnd5e/-/tree/master)
- **Arquitetura & Especificidades:**
  - Utiliza arquitetura orientada a `TypeDataModel` (v3.0+) e `Activity` system para itens e magias.
  - Implementa pipelines ricos de `dnd5e.preRollAbilityTest`, `dnd5e.rollAttack`, `dnd5e.rollDamage` e `dnd5e.useItem`.
  - Altamente extensível via `CONFIG.DND5E`.
- **Armadilhas Comuns:**
  - A partir da versão 3.0+, métodos legados como `item.roll()` foram refatorados para o sistema de Activities (`item.system.activities`). Tentar disparar consumo direto de spell slots pelo método antigo causará erro.
  - Modificações em dados de atores devem usar `system.abilities.<hab>.value` e não schemas antigos da v1/v2.

---

## 2. Pathfinder 2nd Edition (pf2e)
- **Repositório:** [https://github.com/foundryvtt/pf2e](https://github.com/foundryvtt/pf2e)
- **Arquitetura & Especificidades:**
  - Considerado o sistema com maior grau de automação e fidelidade no Foundry VTT.
  - Utiliza **Rule Elements (REs)** extensivos armazenados nos dados dos itens em vez de Active Effects tradicionais.
  - Código estritamente em TypeScript com compilação rígida.
- **Armadilhas Comuns:**
  - **Não utilize Active Effects tradicionais** para alterar atributos como AC, Saves ou Ataques. Use Rule Elements (`FlatModifier`, `RollOption`, `AdjustModifier`).
  - O pipeline de cálculo estatístico de atores é recalculado deterministicamente através do `ActorPF2e#prepareDerivedData` e `RuleElements`.

---

## 3. Daggerheart (daggerheart)
- **Repositório:** [https://github.com/Foundryborne/daggerheart](https://github.com/Foundryborne/daggerheart)
- **Arquitetura & Mecânica Central (Duality Dice System):**
  - Desenvolvido pela Darrington Press (Critical Role / Spenser Starke).
  - **Não é PbtA**, mas um sistema de fantasia heroica com motor de **2d12 Duality Dice**:
    - **1 Dado da Esperança (*Hope Die*)** + **1 Dado do Medo (*Fear Die*)**.
    - O total (Hope + Fear + Modificador) determina o sucesso contra a Dificuldade (Difficulty / Target DC).
    - O dado individual mais alto determina o resultado narrativo:
      - **Sucesso com Esperança (*Success with Hope*):** Sucesso no teste e o jogador ganha 1 Ponto de Esperança (*Hope*).
      - **Sucesso com Medo (*Success with Fear*):** Sucesso no teste, mas o Mestre ganha 1 Ponto de Medo (*Fear*) ou ocorre uma complicação.
      - **Falha com Esperança (*Failure with Hope*):** Falha no teste, mas o jogador ganha 1 Ponto de Esperança.
      - **Falha com Medo (*Failure with Fear*):** Falha no teste e o Mestre ganha 1 Ponto de Medo ou faz um movimento de Mestre forte.
      - **Acerto Crítico (*Critical Success*):** Quando ambos os dados d12 caem no mesmo número (pares), gerando sucesso automático crítico e recuperando Esperança/Stress.
  - Utiliza arquitetura de Cartas de Domínio (*Domain Cards*), Slots de Armadura e Fichas de Personagem divididas em Classes/Subclasses.

---

## 4. Tormenta 20 (Tormenta20)
- **Repositório:** [https://gitlab.com/vizael/Tormenta20](https://gitlab.com/vizael/Tormenta20)
- **Arquitetura & Especificidades:**
  - Desenvolvido especificamente para as regras de Tormenta 20 (Editora Jambô).
  - Suporta cálculo automático de PV, PM, Defesa, Bônus de Treinamento e Perícias.
  - Fórmulas de rolagens com integração direta a macros de poderes e magias.
- **Armadilhas Comuns:**
  - Gerenciamento de PM temporários e custos de aprimoramento de magias possuem lógica customizada de diálogo. Ao disparar rolagens via macro, chame as funções do sistema registradas em `game.tormenta20` para manter consistência no consumo de recursos.

---

## 5. Old Dragon 2ª Edição (olddragon2e-foundryvtt)
- **Repositório:** [https://github.com/olddragoneditora/olddragon2e-foundryvtt](https://github.com/olddragoneditora/olddragon2e-foundryvtt)
- **Arquitetura & Especificidades:**
  - Sistema brasileiro Old School (Buró Jogos / Moostache).
  - Focado em agilidade, fichas clássicas e regras OSR (testes de Atributo sob o valor, Jogadas de Proteção, BA/BD).
- **Armadilhas Comuns:**
  - Mecânica de rolagem D20 Roll-Under (rolar abaixo do valor do atributo para sucesso) em testes de atributos e Roll-Over em Jogadas de Proteção/Ataque.

---

## 6. D&D 3.5e (D35E)
- **Repositório:** [https://gitlab.com/dragonshorn/D35E](https://gitlab.com/dragonshorn/D35E)
- **Arquitetura & Especificidades:**
  - Sistema completo para Dungeons & Dragons 3.5 com suporte a cálculo detalhado de BAB, modificadores de tamanho, resistências e tabelas de progressão de classe clássicas.
- **Armadilhas Comuns:**
  - Complexidade alta de bônus acumulativos (Stacking Rules: Enhancement, Morale, Luck, Insight, Competence). O sistema possui motor próprio para filtrar bônus não cumulativos.

---

## 7. Draw Steel (MCDM RPG)
- **Repositório:** [https://github.com/MetaMorphic-Digital/draw-steel](https://github.com/MetaMorphic-Digital/draw-steel)
- **Arquitetura & Especificidades:**
  - Sistema tático heroico projetado pela MCDM (Matt Colville).
  - Não utiliza jogadas de acerto tradicionais (ataques sempre causam efeito/dano em tiers 1, 2 ou 3 baseados no Power Roll 2d10).
- **Armadilhas Comuns:**
  - Sistema de dados de características e Heroic Resources (Victories, Stamina, Malice) segue ciclo de combate específico por rodada.

---

## 8. Advanced Roleplay System (Rolemaster / ARS)
- **Repositório:** [https://gitlab.com/foundryprojects/systems/advanced-roleplay-system](https://gitlab.com/foundryprojects/systems/advanced-roleplay-system)
- **Arquitetura & Especificidades:**
  - Sistema modular com suporte a tabelas críticas complexas, d100 open-ended (rolagens abertas) e cálculos percentuais detalhados.
