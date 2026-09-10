# Sistemas Genéricos, Regras Customizadas e Nacionais para Foundry VTT 🌐🛠️
> *Base de Conhecimento — Master of Foundry VTT by GM Charles Corrêa*

---

## 1. GURPS 4th Edition (gurps / GURPS 4e Game Aid)
- **Repositório:** [https://github.com/crnormand/gurps](https://github.com/crnormand/gurps)
- **Arquitetura & Especificidades:**
  - Sistema universal detalhado com rolagens 3d6 Roll-Under (<= Nível Efetivo).
  - Importador direto de fichas geradas no GCS (GURPS Character Sheet) e GCA (GURPS Character Assistant).
  - Suporte completo a cálculo de manobras de combate tático, penalidades por localização de acerto, choque por ferimento, recuo (Rcl) de armas de fogo e regras de fadiga.
- **Armadilhas Comuns:**
  - Não edite valores derivados de atributos ou vantagens manualmente na ficha sem verificar se o arquivo XML/JSON do GCS foi reimportado, pois a reimportação sobrescreverá dados manuais soltos.

---

## 2. Savage Worlds Adventure Edition (swade & swade pt-br)
- **Repositórios:**
  - Pinnacle Oficial: [https://gitlab.com/peginc/swade](https://gitlab.com/peginc/swade)
  - FVTT Brasil Tradução: [https://gitlab.com/fvtt-brasil/swade](https://gitlab.com/fvtt-brasil/swade)
- **Arquitetura & Especificidades:**
  - Motor baseado em Tipos de Dados (d4 a d12) com dados que Explodem (*Aces* / `x`).
  - Rolagem de Carta Selvagem (Wild Die 1d6) mantendo o maior resultado contra o Número Alvo (TN padrão 4). Cada 4 pontos acima do TN gera uma Ampliação (*Raise*).
  - Suporte nativo a Baralho de Iniciativa de Ação (Action Cards deck com Jokers).
- **Armadilhas Comuns:**
  - O cálculo de iniciativa usa baralhos de cartas e não dados. Ao disparar combate programaticamente, utilize os métodos da API do SWADE (`combat.startCombat()` ou `combat.dealCards()`).

---

## 3. Custom System Builder & Simple Worldbuilding
- **Repositórios:**
  - Custom System Builder (CSB): [https://gitlab.com/custom-system-builder/custom-system-builder](https://gitlab.com/custom-system-builder/custom-system-builder)
  - Simple Worldbuilding (Oficial Foundry): [https://github.com/foundryvtt/worldbuilding](https://github.com/foundryvtt/worldbuilding)
- **Arquitetura & Especificidades:**
  - **CSB:** Permite criar fichas completas, fórmulas matemáticas e botões de rolagem com interface visual drag-and-drop sem programar código JavaScript.
  - **Simple Worldbuilding:** Sistema template oficial do Foundry para criação rápida de mundos e prototipação de atributos chave-valor simples.

---

## 4. Sistemas Nacionais Brasileiros: 3D&T e ABEA
- **Repositórios:**
  - 3D&T Alpha: [https://github.com/ederfialho/tresdetalpha](https://github.com/ederfialho/tresdetalpha)
  - 3D&T Victory / Vitória: [https://github.com/mclemente/fvtt-tresdetv](https://github.com/mclemente/fvtt-tresdetv)
  - A Bandeira do Elefante e da Arara (ABEA): [https://github.com/rafarvns/abea-foundryvtt-system](https://github.com/rafarvns/abea-foundryvtt-system)
- **Especificidades:**
  - **3D&T Alpha:** 1d6 + Características (F, H, R, A, PdF) com Críticos (resultado 6 dobrando o valor da característica).
  - **3D&T Victory:** Sistema moderno com dados de 6 faces (2d6 ou 3d6 com vantagens) comparados a Dificuldades fixas e testes de perícia com poderes.
  - **ABEA:** Baseado em dados de três cores (3d6) com regras históricas e mágicas inspiradas no folclore e período colonial brasileiro.

---

## 5. The Witcher TRPG (TheWitcherTRPG & Deathmarch)
- **Repositórios:**
  - Sistema Oficial: [https://github.com/witchertrpg-foundryvtt/TheWitcherTRPG](https://github.com/witchertrpg-foundryvtt/TheWitcherTRPG)
  - Deathmarch Witcher TRPG: [https://github.com/papajarv/Deathmarch-Witcher-TRPG](https://github.com/papajarv/Deathmarch-Witcher-TRPG)
- **Especificidades:**
  - 1d10 Explodindo em 10 e Subtraindo em 1 + Estatística + Perícia.
  - Tabelas de ferimentos críticos graves, membros decepados, alquimia e resistência à toxicidade por poções/mutagênicos.

---

## 6. Shadow of the Demon Lord & Shadow of the Weird Wizard
- **Repositórios:**
  - Shadow of the Demon Lord: [https://github.com/Xacus/demonlord](https://github.com/Xacus/demonlord)
  - Shadow of the Weird Wizard: [https://github.com/Savantford/foundry-weirdwizard](https://github.com/Savantford/foundry-weirdwizard)
- **Especificidades:**
  - Motor 1d20 + Dádivas e Maldições (*Boons and Banes* em dados d6 que se cancelam 1 a 1, mantendo o maior d6 resultante).
  - Dano por Loucura, Corrupção e caminhos de afinidade mágica (Tradições).

---

## 7. Ars Magica 5ª Edição (arm5e) & The One Ring 2e (tor2e)
- **Repositórios:**
  - Ars Magica 5E: [https://github.com/Xzotl42/arm5e](https://github.com/Xzotl42/arm5e)
  - The One Ring 2E: [https://gitlab.com/herve.darritchon/foundryvtt-tor2e](https://gitlab.com/herve.darritchon/foundryvtt-tor2e)
- **Especificidades:**
  - **Ars Magica:** Sistema hermético de magia verbal baseado em Verbo + Substantivo (Técnica + Forma) com dados de Estresse e cálculo de Vis mágica.
  - **The One Ring 2E:** Dado de Proeza (d12 com a Runa de Gandalf e o Olho de Sauron) somado a Dados de Sucesso (d6 com símbolos Tengwar de maestria).

---

## 8. TinyD6 (foundry-tinyd6)
- **Repositório:** [https://gitlab.com/architech99/foundry-tinyd6](https://gitlab.com/architech99/foundry-tinyd6)
- **Especificidades:**
  - Sistema minimalista (Tiny Dungeon, Tiny Frontiers, Tiny Wastelands): rolar 2d6 padrão (3d6 com Vantagem, 1d6 com Desvantagem). Qualquer `5` ou `6` representa um Sucesso completo.
