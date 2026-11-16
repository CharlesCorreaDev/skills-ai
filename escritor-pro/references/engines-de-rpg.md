# Enciclopédia Arquitetural de Engines & Motores de RPG
## Parte Integrante da Skill Escritor Pro — Consultoria de RPG & Game Design

Esta referência reúne a catalogação estruturada, mecânicas-base, curvas matemáticas, fórmulas de resolução e documentações oficiais de dezenas de motores de RPG de mesa mundiais, independentes e nacionais, além de um mapeamento aprofundado de **Afrofantasia, Afrofuturismo e RPGs Afro-Urbanos**.

Utilize quando o usuário desejar conceber um jogo novo, adaptar um cenário canônico para um sistema específico, balancear encontros ou escolher o motor ideal para sua proposta narrativa.

---

## Índice Temático dos Motores

1. [Motores de Dado Único & Dados de Dualidade](#1-motores-de-dado-único--dados-de-dualidade)
2. [Motores d12 Específicos & Minimalistas (d12 RPG, d12GO!)](#2-motores-d12-específicos--minimalistas)
3. [Motores de Parada de Dados (Dice Pool)](#3-motores-de-parada-de-dados-dice-pool)
4. [Motores de Dados Escalonados (Step Dice) & Curva de Sino](#4-motores-de-dados-escalonados-step-dice--curva-de-sino)
5. [Motores Percentuais (d100) & OSR Clássico](#5-motores-percentuais-d100--osr-clássico)
6. [Motores Narrativos, PbtA, FitD & Sem Dados (Diceless)](#6-motores-narrativos-pbta-fitd--sem-dados-diceless)
7. [Motores Táticos, Mechas & Grid](#7-motores-táticos-mechas--grid)
8. [Motores Investigativos, Horror & Tensão Psicológica](#8-motores-investigativos-horror--tensão-psicológica)
9. [Sistemas Autorais de Newton Rocha / Tio Nitro (NitroDungeon)](#9-sistemas-autorais-de-newton-rocha--tio-nitro-nitrodungeon)
10. [Motores Brasileiros Históricos & Contemporâneos](#10-motores-brasileiros-históricos--contemporâneos)
11. [Sistemas & Cenários de Afrofantasia, Afrofuturismo e Afro-Urbano](#11-sistemas--cenários-de-afrofantasia-afrofuturismo-e-afro-urbano)
12. [Motores Japoneses, JRPG & Anime](#12-motores-japoneses-jrpg--anime)
13. [Tabela Comparativa Rápida de Resolução](#13-tabela-comparativa-rápida-de-resolução)

---

## 1. Motores de Dado Único & Dados de Dualidade

### Caltrop Core (d4 System)
- **Criador / Editora:** Lex Kim Bobrow (Titanomachy RPG, 2021 / v1.2 em 2023)
- **Proposta:** Engine minimalista de 11 páginas projetada para hacks rápidos usando exclusivamente dados de 4 faces.
- **Mecânica Base:** Pool de $d4$ igual ao atributo (1 a 3) ou gasto de fichas. Lê-se apenas o maior resultado:
  - `4`: Sucesso total.
  - `3`: Sucesso parcial (com custo/complicação).
  - `1–2`: Falha.
- **Link Oficial:** [Caltrop Core SRD (CC-BY 4.0)](https://caltropcore.com/)

### d20 System (D&D 3e / 3.5 / 5e / OGL)
- **Criadores / Editora:** Jonathan Tweet, Monte Cook, Skip Williams / Wizards of the Coast (2000)
- **Proposta:** Padrão clássico de fantasia heroica, progressão por classes, talentos, níveis e pontos de vida crescentes.
- **Mecânica Base:** Rolagem ascendente (roll-over):
  $$\text{Resultado} = 1d20 + \text{Modificador de Atributo} + \text{Bônus de Perícia/Proficiência} \ge \text{Classe de Dificuldade (CD)}$$
- **Links Oficiais:** [Hypertext d20 SRD (v3.5)](https://www.d20srd.org/) | [D&D 5e SRD v5.2.1 (CC-BY 4.0)](https://www.dndbeyond.com/srd)

### Daggerheart (Dual d12 / Duality Dice)
- **Criadores / Editora:** Spenser Starke e Rowan Hall / Darrington Press (2025 / SRD 2.0 em 2026)
- **Proposta:** Fantasia heroica cinematográfica focada em drama colaborativo e fluxo de recursos narrativos entre Mestre e Jogadores.
- **Mecânica Base:** Rola-se $2d12$ (um Dado de Esperança e um Dado de Medo) + Modificador vs. Dificuldade:
  - Soma atinge a CD: Sucesso.
  - Dado de Esperança maior: Jogador ganha 1 recurso de Esperança.
  - Dado de Medo maior: Mestre ganha 1 ficha de Medo para ativar perigos e reações de adversários.
- **Link Oficial:** [Daggerheart SRD Oficial](https://www.daggerheart.com/srd/)

### Cypher System
- **Criador / Editora:** Monte Cook / Monte Cook Games (2013 em Numenera / 2015 genérico)
- **Proposta:** Exploração, ficção científica/fantasia e consumo de artefatos de uso único (Cyphers). 100% voltado aos jogadores (player-facing).
- **Mecânica Base:** O Mestre define a Dificuldade de 1 a 10. O número-alvo é sempre $\text{Dificuldade} \times 3$ no $1d20$. Os atributos (Potência, Velocidade, Intelecto) são reservas de esforço gastas antes da rolagem para reduzir a dificuldade da tarefa.
- **Link Oficial:** [Cypher System Rules Primer](https://www.montecookgames.com/cypher-system-rules-primer/)

### Quest RPG
- **Criador / Editora:** T.C. Sottek / The Adventure Guild (2020)
- **Proposta:** Acessibilidade total sem modificadores matemáticos na ficha.
- **Mecânica Base:** $1d20$ puro sem bônus:
  - `20`: Triunfo.
  - `11–19`: Sucesso pleno.
  - `6–10`: Escolha Difícil (sucesso com custo).
  - `2–5`: Falha.
  - `1`: Catástrofe.
- **Link Oficial:** [Quest RPG Creator Resource (CC-BY 4.0)](https://www.adventure.game/resources)

---

## 2. Motores d12 Específicos & Minimalistas

### d12 RPG (Basic Edition)
- **Criador / Editora:** d12 Studios (2022)
- **Proposta:** Alternativa tática de fantasia medieval completa construída integralmente em torno do dado de 12 faces ($d12$), dispensando o d20 tradicional.
- **Mecânica Base:** Resolução baseada em $1d12$ + perícia/atributo contra a dificuldade ou defesa ativa do oponente. Apresenta sistema híbrido de compra de atributos por pontos e progressão por classes, onde a armadura e o posicionamento reduzem danos de forma granular em vez de apenas ditar a chance de acerto.
- **Link Oficial:** [d12 RPG Basic Edition no DriveThruRPG](https://www.drivethrurpg.com/en/product/407886/d12-rpg-basic-edition)

### d12GO!
- **Criador / Editora:** Brad Zimmerman / Squadeth Games (#KiwiRPG, 2022+)
- **Proposta:** Sistema universal ultrarrápido (rules-lite) desenhado para one-shots, sessões descompromissadas e adaptação fluida de qualquer cenário (alta fantasia, zumbis, ficção científica).
- **Mecânica Base:** Utiliza um único $d12$ para a maioria dos testes de atributo e tarefas, com faixas de sucesso claras, fichas de 1 página e rápida geração de adversários.
- **Link Oficial:** [d12GO! na itch.io (Squadeth Games)](https://squadethgames.itch.io/d12go)

---

## 3. Motores de Parada de Dados (Dice Pool)

### D6 System / OpenD6
- **Criadores / Editora:** Sandy Petersen, Lynn Willis, Greg Stafford (1986); Greg Costikyan (Star Wars WEG, 1987); West End Games / Comunidade OpenD6
- **Mecânica Base:** Parada de $d6$ somada contra Número-Alvo. Um dos dados é o **Dado Selvagem (Wild Die)**: `6` explode somando; `1` anula o maior dado da rolagem ou impõe complicações.
- **Link Oficial:** [Portal Oficial OpenD6](https://opend6.net/) | [OpenD6 SRD (OGL)](https://opend6.net/srd)

### Year Zero Engine (YZE)
- **Criador / Editora:** Tomas Härenstam / Free League Publishing (2014 em Mutant: Year Zero / SRD 2023)
- **Proposta:** Sobrevivência implacável, horror e escassez (Alien RPG, Vaesen, Blade Runner, Forbidden Lands).
- **Mecânica Base:**
  - *Dice Pool Padrão:* Soma-se $d6$ de Atributo + Perícia + Equipamento. Apenas resultados `6` contam como sucesso. Pode-se Forçar a Rolagem (Push), mas cada `1` em dados de atributo causa trauma físico/mental ou danifica itens.
  - *Step Dice:* Escala de dados ($d6$ a $d12$) onde $6+$ = 1 sucesso e $10+$ = 2 sucessos.
- **Link Oficial:** [Year Zero Engine SRD (PDF)](https://freeleaguepublishing.com/wp-content/uploads/2023/11/YZE-Standard-Reference-Document.pdf)

### Forged in the Dark (FitD)
- **Criador / Editora:** John Harper / One Seven Design (2017 em Blades in the Dark)
- **Proposta:** Golpes criminosos, estresse, facções e ciclos de missão e folga (downtime).
- **Mecânica Base:** Pool de $d6$ lendo o maior resultado: `6` = sucesso pleno (crítico em duplo 6); `4–5` = sucesso parcial com consequência; `1–3` = falha. O Mestre define **Posição** (Controlada, Arriscada, Desesperada) e **Efeito** (Limitado, Padrão, Ótimo).
- **Link Oficial:** [Blades in the Dark Licensing / SRD](https://bladesinthedark.com/licensing)

### 2d20 System
- **Criadores / Editora:** Jay Little e Nathan Dowdell / Modiphius Entertainment (2015 em Mutant Chronicles / SRD 2022)
- **Proposta:** Ação cinematográfica com gestão de recursos táticos (Conan, Dune, Star Trek Adventures, Fallout).
- **Mecânica Base:** Roll-under: Rola-se de $2d20$ a $5d20$. Cada dado $\le \text{Atributo} + \text{Perícia}$ gera 1 sucesso (rolar $\le \text{Perícia}$ pura gera 2 sucessos). Sucessos excedentes geram pontos de **Ímpeto (Momentum)** para a reserva compartilhada do grupo.
- **Link Oficial:** [2d20 World Builders SRD](https://modiphius.net/pages/2d20worldbuilders)

### Storyteller / Storytelling System (World of Darkness / V5)
- **Criadores / Editora:** Mark Rein-Hagen, Tom Dowd / White Wolf (1991) / Paradox Interactive
- **Mecânica Base:** Parada de $d10$ igual a $\text{Atributo} + \text{Habilidade}$. No V5, sucesso é obtido em $6+$ no dado (pares de 10 geram críticos). Parte da parada é substituída por **Dados de Fome**: `1` ou `10` neles desencadeia compulsões bestiais.
- **Link Oficial:** [World of Darkness Dark Pack](https://www.paradoxinteractive.com/games/world-of-darkness/community/dark-pack-agreement)

### Genesys / Narrative Dice System (NDS)
- **Criador / Editora:** Jay Little / Fantasy Flight Games / Edge Studio (2012 em Star Wars RPG / 2017 genérico)
- **Proposta:** Separação matemática entre sucesso na tarefa e consequências circunstanciais.
- **Mecânica Base:** Dados customizados com símbolos opostos que se anulam: Sucesso vs. Falha; Vantagem vs. Ameaça; Triunfo vs. Desespero. É possível falhar na tarefa mas gerar vantagens colaterais, ou ter sucesso com graves ameaças.
- **Link Oficial:** [Genesys Foundry](https://www.edge-studio.net/shares/genesys/)

### One-Roll Engine (ORE)
- **Criador / Editora:** Greg Stolze / Arc Dream Publishing (2001 em Godlike / Wild Talents / Reign)
- **Mecânica Base:** Rola-se até $10d10$ procurando conjuntos de números iguais (Matches). A **Largura** (Width: quantos dados iguais saíram) determina a velocidade e dano; a **Altura** (Height: o valor da face de 1 a 10) define a qualidade e localização do golpe.
- **Link Oficial:** [Arc Dream Publishing ORE](https://arcdream.com/home/wild-talents/)

### Outgunned (Director's Cut)
- **Criadores / Editora:** Riccardo Sirignano, Simone Formicola / Two Little Mice (2023)
- **Mecânica Base:** Pool de $d6$ estilo Yahtzee. Busca-se combinações de faces iguais: Par = Sucesso Básico; Trinca = Crítico; Quadra = Extremo; Quina = Impossível.
- **Link Oficial:** [Two Little Mice Outgunned](https://twolittlemice.net/outgunned/)

---

## 4. Motores de Dados Escalonados (Step Dice) & Curva de Sino

### Savage Worlds (SWADE)
- **Criador / Editora:** Shane Lacy Hensley / Pinnacle Entertainment Group (2003 / SWADE 2018)
- **Proposta:** Ação rápida ("Fast! Furious! Fun!"), combate com cartas de baralho e alta letalidade.
- **Mecânica Base:** Atributos e perícias em dados escalonados ($d4$ a $d12$). Protagonistas rolam o dado do atributo junto com o Dado Selvagem ($1d6$), ficando com o maior. O alvo padrão é $4$. Todos os dados explodem (Ace) na face máxima. A cada 4 pontos acima do alvo gera-se uma Ampliação (Raise).
- **Link Oficial:** [Pinnacle Entertainment Group — SWADE](https://peginc.com/savage-settings/savage-worlds/)

### GURPS (3d6 Bell Curve)
- **Criador / Editora:** Steve Jackson / Steve Jackson Games (1986 / 4ª Edição em 2004)
- **Proposta:** Padrão-ouro da simulação modular e compra por pontos sem classes ou níveis.
- **Mecânica Base:** Roll-under em curva de sino: $3d6 \le \text{Nível Efetivo da Perícia}$. Resultados 10 e 11 representam a mediana estatística; extremos (3–4 críticos / 17–18 falhas críticas) são raros e controlados.
- **Link Oficial:** [GURPS Lite (Grátis)](https://www.sjgames.com/gurps/lite/)

### Cortex Prime
- **Criadores / Editora:** Jamie Chambers, Cam Banks / Dire Wolf Digital (2004 / 2020)
- **Proposta:** Toolkit modular para compor regras personalizadas (Tales of Xadia, Marvel Heroic).
- **Mecânica Base:** Monta-se uma parada com dados escalonados ($d4$ a $d12$) de diferentes características da cena, rola-se todos e soma-se os dois maiores para bater a dificuldade. Escolhe-se um terceiro dado como Dado de Efeito (Effect Die) para ditar a magnitude do impacto.
- **Link Oficial:** [Cortex Prime Official](https://www.cortexrpg.com/)

### AGE System (Adventure Game Engine)
- **Criador / Editora:** Chris Pramas / Green Ronin Publishing (2009 em Dragon Age / 2015 Fantasy AGE)
- **Mecânica Base:** $3d6$ + modificador vs. Número-Alvo. Um dos dados tem cor diferente: o **Dado de Façanha (Stunt Die)**. Se o teste tiver sucesso e houver números iguais em quaisquer dois dados, o jogador ganha Pontos de Façanha iguais ao valor do Stunt Die para gastar em manobras imediatas.
- **Link Oficial:** [Green Ronin AGE](https://greenroninstore.com/pages/age-creators-alliance)

### Breathless (Step-Down Exhaustion)
- **Criador / Editora:** René-Pier Deshaies-Gélinas / Fari RPGs (2022)
- **Proposta:** Tensão de sobrevivência onde recursos e fôlego decaem a cada esforço.
- **Mecânica Base:** Perícias começam em dados altos ($d10, d8, d6, d4$). Ao usar uma perícia, rola-se o dado ($5+$ pleno, $3–4$ custo, $1–2$ falha); após a rolagem, o dado da perícia **cai um degrau** até o grupo conseguir descansar (avançando o relógio de perigo).
- **Link Oficial:** [Breathless SRD (CC-BY 4.0)](https://fari-rpgs.itch.io/breathless-srd)

---

## 5. Motores Percentuais (d100) & OSR Clássico

### Basic Roleplaying (BRP) / Call of Cthulhu / Mythras
- **Criadores / Editora:** Greg Stafford, Lynn Willis / Chaosium (1980 / SRD ORC em 2023)
- **Mecânica Base:** Roll-under percentual: $1d100 \le \text{Valor da Perícia (01\% a 100\%)}$. Sucesso Especial/Crítico em $\le 1/5$ da perícia; Falha Crítica em $96–00$.
- **Link Oficial:** [Chaosium BRP SRD (ORC License)](https://www.chaosium.com/brp-system-reference-document/)

### Mothership 1e (Panic Engine)
- **Criador / Editora:** Sean McCoy / Tuesday Knight Games (2018 / 1e em 2024)
- **Proposta:** Horror espacial e paranoia industrial (estilo Alien, Dead Space).
- **Mecânica Base:** $1d100$ roll-under com críticos em números duplos (11, 22, 33). Falhas acumulam Estresse ($2$ a $20$). Testes de Pânico usam $1d20$ buscando tirar acima do Estresse acumulado; falhar ativa a Tabela de Pânico ($1d20 + \text{Estresse}$).
- **Link Oficial:** [Mothership Third-Party License](https://www.tuesdayknightgames.com/pages/mothership-rpg)

### Old-School Essentials (OSE) & Shadowdark
- **Criadores / Editora:** Gavin Norman / Necrotic Gnome (2019) | Kelsey Dionne / The Arcane Library (2023)
- **Proposta:** Exploração de masmorras com alta letalidade, escassez de luz e foco nas decisões do jogador.
- **Mecânica Base:**
  - *Shadowdark:* $1d20 + \text{modificador} \ge \text{CD}$. Tochas duram exatamente 1 hora em tempo real na mesa.
  - *OSE:* Retroclone de D&D B/X (1981) com turnos de exploração de 10 minutos e testes de reação/moral em $2d6$.
- **Links Oficiais:** [OSE SRD](https://oldschoolessentials.necroticgnome.com/srd/) | [Shadowdark RPG](https://www.thearcanelibrary.com/pages/shadowdark-rpg-third-party-license)

### Into the Odd / Cairn (NSR Auto-Hit)
- **Criadores / Editora:** Chris McDowall (2014) / Yochai Gal (2020)
- **Proposta:** Letalidade instantânea e ausência de rolagem de acerto em combate.
- **Mecânica Base:** Apenas 3 atributos (Força, Destreza, Vontade) em $1d20$ roll-under. Em combate, os ataques acertam automaticamente: rola-se direto o dado de dano da arma, subtraindo primeiro da Proteção e depois da Força.
- **Link Oficial:** [Cairn SRD (CC-BY-SA 4.0)](https://cairnrpg.com/)

---

## 6. Motores Narrativos, PbtA, FitD & Sem Dados (Diceless)

### Powered by the Apocalypse (PbtA)
- **Criadores / Editora:** Vincent Baker e Meguey Baker / Lumpley Games (2010 em Apocalypse World)
- **Mecânica Base:** Rola-se apenas quando um Movimento narrativo é ativado: $2d6 + \text{Atributo}$ (-1 a +3):
  - `10+`: Sucesso pleno.
  - `7–9`: Sucesso parcial com custo, escolha difícil ou complicação.
  - `6-`: Falha (o Mestre realiza um Movimento duro).
- **Link Oficial:** [Apocalypse World PbtA Policy](http://apocalypse-world.com/pbta/policy)

### Fate Core / Fate Accelerated
- **Criadores / Editora:** Fred Hicks e Rob Donoghue / Evil Hat Productions (2003 / 2013)
- **Mecânica Base:** Rola-se $4dF$ (quatro dados Fate com faces +, -, branco, variando de -4 a +4) + Perícia contra escada de dificuldade. A economia de mesa gira em torno dos Aspectos (verdades conceituais) invocados ou forçados com Pontos de Destino.
- **Link Oficial:** [Fate SRD (CC-BY 3.0 / OGL)](https://fate-srd.com/)

### Ironsworn / Starforged
- **Criador / Editora:** Shawn Tomkin / Tomkin Press (2018 / 2022)
- **Proposta:** Padrão mundial para RPG solo, cooperativo sem mestre e guiado.
- **Mecânica Base:** Rola-se $1d6$ (Dado de Ação) + Atributo contra dois $d10$ independentes (Dados de Desafio):
  - Supera ambos os $d10$: Sucesso Total (Strong Hit).
  - Supera apenas um $d10$: Sucesso Parcial (Weak Hit com custo).
  - Não supera nenhum: Falha (Miss).
  - Pares nos $d10$ ativam reviravoltas narrativas extremas.
- **Link Oficial:** [Ironsworn Licensing (CC-BY 4.0)](https://www.ironswornrpg.com/licensing)

### Belonging Outside Belonging (Diceless / Token Economy)
- **Criadores / Editora:** Avery Alder e Benjamin Rosenbaum / Buried Without Ceremony (2018 em Dream Askew)
- **Mecânica Base:** Economia de fichas: Movimentos Fracos concedem 1 ficha; Movimentos Regulares são gratuitos; Movimentos Fortes custam 1 ficha.
- **Link Oficial:** [Belonging Outside Belonging SRD](https://buriedwithoutceremony.com/belonging)

### Dread (Torre de Blocos Jenga)
- **Criadores / Editora:** Epidiah Ravachol, Nathaniel Barmore / The Impossible Dream (2005)
- **Mecânica Base:** Ações arriscadas exigem puxar blocos de uma torre de madeira no centro da mesa. Se a torre cair, o personagem morre ou é retirado tragicamente da história.
- **Link Oficial:** [The Impossible Dream — Dread](https://www.tiltingatwindmills.net/games/dread/)

---

## 7. Motores Táticos, Mechas & Grid

### Lancer / ICON
- **Criadores / Editora:** Tom Parkinson-Morgan e Miguel Lopez / Massif Press (2019 / 2021)
- **Proposta:** Combate tático profundo de mechas em grid hexagonal com gestão de calor (*Heat*) e regras narrativas leves fora do combate.
- **Link Oficial:** [Massif Press Lancer Core](https://massif-press.itch.io/corebook-pdf-free)

### Draw Steel / MCDM RPG
- **Criadores / Editora:** Matt Colville, James Introcaso / MCDM Productions (2025)
- **Proposta:** Combate heroico dinâmico em grid onde ataques nunca erram. Rola-se a Rolagem de Poder ($2d10$ + Característica) para medir patamares de dano (Tier 1 a 3).
- **Link Oficial:** [MCDM Productions](https://www.mcdmproductions.com/)

### Pathfinder 2e Remaster
- **Criadores / Editora:** Jason Bulmahn, Logan Bonner / Paizo (2019 / Remaster ORC 2023)
- **Mecânica Base:** Economia de 3 Ações por turno + 4 Graus de Sucesso (superar por 10+ ou falhar por 10+ altera o patamar de crítico).
- **Link Oficial:** [Archives of Nethys PF2e SRD](https://2e.aonprd.com/)

---

## 8. Motores Investigativos, Horror & Tensão Psicológica

### GUMSHOE System
- **Criador / Editora:** Robin D. Laws / Pelgrane Press (2007 em The Esoterrorists / Trail of Cthulhu)
- **Proposta:** Fim da estagnação por falha em testes de investigação. Perícias Investigativas **não rolam dados** — ter a perícia e visitar a cena garante a pista central automaticamente. O $1d6$ só é rolado para ações gerais (combate, fuga) gastando pontos da reserva.
- **Link Oficial:** [GUMSHOE SRD (CC-BY 3.0)](https://pelgranepress.com/2013/10/24/the-gumshoe-system-reference-document/)

### Spire / Heart: The City Beneath (Resistance System)
- **Criadores / Editora:** Grant Howitt, Christopher Taylor / Rowan, Rook and Decard (2018 / 2020)
- **Mecânica Base:** Pool de $d10$ (lê o maior). Sucessos com custo geram Estresse distribuído em 5 Resistências (Sangue, Mente, Eco, Fortuna, Suprimentos). O Mestre testa $1d12$ contra o estresse para gerar Consequências permanentes.
- **Link Oficial:** [Resistance Toolbox SRD (CC-BY 4.0)](https://rowanrookanddecard.com/product/the-resistance-toolbox/)

---

## 9. Sistemas Autorais de Newton Rocha / Tio Nitro (NitroDungeon)

Conjunto de sistemas gratuitos e abertos desenvolvidos por **Newton "Tio Nitro" Rocha**, amplamente difundidos na comunidade brasileira de RPG para jogos rápidos, narrativistas e solo:

### 2d6World
- **Criador:** Newton Rocha (Tio Nitro / NitroDungeon)
- **Proposta:** Adaptação livre, aberta e modular da filosofia PbtA (*Powered by the Apocalypse*) e *Dungeon World* em Português Brasileiro, desenhada para ser adaptada facilmente a qualquer gênero ficcional.
- **Mecânica Base:** $2d6 + \text{modificador de atributo}$ (-2 a +3) com faixas canônicas narrativas: 10+ sucesso total; 7–9 sucesso parcial com escolha difícil; 6- falha com movimento do Mestre.
- **Link Oficial:** [2d6World no NitroDungeon](https://newtonrocha.wordpress.com/2d6world/)

### Pocket 2d6World
- **Criador:** Newton Rocha
- **Proposta:** Versão de bolso, ultracompacta e minimalista do 2d6World, condensando fichas, movimentos básicos e regras em pouquíssimas páginas para jogos improvisados.
- **Link Oficial:** [Pocket 2d6World no NitroDungeon](https://newtonrocha.wordpress.com/pocket-2d6world-sistema-de-regras-de-rpg-minimalista-narrativista-e-customizavel/)

### Sistema 2d6 (2d6 Nitro)
- **Criador:** Newton Rocha
- **Proposta:** Sistema genérico baseado em 2d6 clássico para campanhas de fantasia, horror e ficção científica com regras tradicionais de atributos e perícias sem depender estritamente da estrutura de *Playbooks*.
- **Link Oficial:** [Sistema de RPG 2d6 no NitroDungeon](https://newtonrocha.wordpress.com/sistema-de-rpg-2d6/)

### 2d6Solo
- **Criador:** Newton Rocha
- **Proposta:** Motor de regras e oráculo narrativo voltado exclusivamente para jogar RPG sem Mestre utilizando apenas dois dados de seis faces ($2d6$).
- **Mecânica Base:** Tabelas de oráculo de "Sim/Não", geradores de eventos, faixas de probabilidade e catalisadores narrativos para conduzir histórias solo ou em modo cooperativo.
- **Link Oficial:** [2d6Solo no NitroDungeon](https://newtonrocha.wordpress.com/2d6solo/)

### Sistema 2d10Solo
- **Criador:** Newton Rocha
- **Proposta:** Evolução do oráculo solo do autor utilizando dois dados de dez faces ($2d10$), oferecendo uma curva probabilística mais detalhada e ampla (escala percentual/decimal) para responder perguntas e criar reviravoltas na ausência de um Narrador.
- **Link Oficial:** [Sistema 2d10Solo no NitroDungeon](https://newtonrocha.wordpress.com/sistema-2d10solo-2d10solo-regras-customizaveis-para-jogos-de-rpg-sem-mestre-download-gratuito-nitrogames-rpgsolo-sistemaderpg/)

### Coleção Sistemas do Tio Nitro (Hub Central)
- Reúne os motores *2d6World, Pocket 2d6World, 2d10Solo, 2d6Solo, Sistema 2d6 e Old Dragon Turbo*.
- **Link Oficial:** [Hub dos Sistemas do Tio Nitro](https://newtonrocha.wordpress.com/sistemas-de-rpg-do-tio-nitro-2d6world-pocket-2d6world-2d10solo-2d6solo-sistema-2d6-old-dragon-turbo/)

---

## 10. Motores Brasileiros Históricos & Contemporâneos

### Tormenta20 (T20)
- **Criadores / Editora:** Marcelo Cassaro, Guilherme Dei Svaldi, Leonel Caldela, J.M. Trevisan / Jambô Editora (2020 / Edição Jogo do Ano 2022)
- **Mecânica Base:** $1d20$ + Perícia $\ge$ CD. Unificação de todos os poderes e magias através da reserva de **Pontos de Mana (PM)** para todas as classes.
- **Link Oficial:** [Jambô Editora — Tormenta20](https://jamboeditora.com.br/categoria/rpg/tormenta20/)

### 3DeT Victory
- **Criadores / Editora:** Marcelo Cassaro, Guilherme Dei Svaldi, Bruno Schlatter / Jambô Editora (1998 / 2023)
- **Proposta:** Ação estilo mangá, games e tokusatsu.
- **Mecânica Base:** 3 Atributos (Poder, Habilidade, Resistência) somados a uma parada de $1d6$ a $3d6$ contra uma Meta. Resultados 6 dobram o valor do atributo na rolagem.
- **Link Oficial:** [3DeT Victory](https://jamboeditora.com.br/categoria/rpg/3det/)

### Old Dragon 2ª Edição (OD2)
- **Criadores / Editora:** Antonio Sá Neto, Fabiano Neme / Buró Brasil (2010 / 2023)
- **Proposta:** O principal retroclone clássico OSR brasileiro.
- **Mecânica Base:** Ataques ascendentes ($1d20 + \text{BA} \ge \text{CA}$), testes de atributo descendentes ($1d20 \le \text{Atributo}$) e Jogadas de Proteção por classe.
- **Link Oficial:** [Old Dragon Online SRD](https://olddragon.com.br/livros/srd)

### Tagmar (Tagmar 1, 2 e 3)
- **Criadores:** Marcelo Rodrigues, Ygor Moraes e comunidade / GSA (1991) / Projeto Tagmar
- **Proposta:** O primeiro RPG de mesa publicado no Brasil.
- **Mecânica Base:** $1d20$ cruzado com a clássica **Tabela de Resolução** colorida por patamares de perícia, determinando qualidade e gravidade do dano.
- **Link Oficial:** [Projeto Tagmar Oficial](https://www.tagmar.com.br/)

### Daemon System
- **Criador / Editora:** Marcelo Del Debbio / Daemon Editora (1995 em Arkanun e Trevas)
- **Mecânica Base:** Atributos numéricos com perícias percentuais ($1d100 \le \text{Perícia}$). Combates utilizam a fórmula de confronto: $50\% + (\text{Ataque} - \text{Defesa})$.
- **Link Oficial:** [Daemon Editora](https://www.daemon.com.br/)

### Espadas Afiadas & Feitiços Sinistros (EA&FS)
- **Criador / Editora:** Diogo Nogueira / Old Skull Publishing (2016)
- **Mecânica Base:** $1d20$ roll-under ($\le \text{Atributo}$). Uso inovador do **Dado de Uso (Usage Die)** para gerenciar recursos e munições ($d12 \rightarrow d4$).
- **Link Oficial:** [Old Skull Publishing](https://oldskull-publishing.com/)

### Skyfall RPG
- **Criador / Editora:** Pedro Coimbra / CapyCat Games (2024)
- **Proposta:** Fantasia trágica e melancolia com motor d20 híbrido, Dados de Ênfase e Pontos de Catarse.
- **Link Oficial:** [CapyCat Games](https://www.capycat.games/)

### Sistema Dharma (Edição Revisada e Ampliada)
- **Criador:** Bruno Moraes Alves (Bruno "More Eyes" / MoreEyesVerso)
- **Proposta:** Sistema universal brasileiro independente publicado sob Open Game License (OGL), desenhado para adaptar desde fantasia medieval clássica e horror até cyberpunk, pós-apocalíptico, steampunk e cenários de alta potência (*overpower*).
- **Mecânica Base:** 
  - Estruturado em **quatro atributos fundamentais**: *Corpo (BD)* (vigor e força física), *Movimento (MV)* (agilidade e reflexos), *Mente (MN)* (intelecto e raciocínio) e *Espírito (SP)* (força de vontade e intuição).
  - Utiliza uma pool poliédrica diversificada ($d4, d6, d8, d10, d12, d20$) com dinâmicas de Vitalidade, Resistência, trunfos/contratempos e mecânicas morais e filosóficas de *Dharma* e *Karma*.
- **Link Oficial:** [Dharma RPG — Edição Revisada (Site Oficial)](https://www.brunomoraesalves.com.br/dharma-edicao-revisada) | [Dharma Fastplays Gratuitos](https://www.brunomoraesalves.com.br/dharma-fastplays)

### Ecossistema MoreEyesVerso (Bruno Moraes Alves)
Coleção de motores independentes e adaptações shonen/ação desenvolvidas pelo autor:

#### 1. Sistema Edhen 3 (Edhen 3ª Edição — Shonen d20)
- **Proposta:** Desenvolvido originalmente para emular combates cinematográficos e escalas titânicas de poder no universo de *Dragon Ball Z*, servindo de alicerce histórico e laboratório de mecânicas para o posterior desenvolvimento do Sistema Dharma.
- **Mecânica Base:** Utiliza o chassi $1d20$ adaptado para lutas acrobáticas, ki/energia, escalonamento monumental de atributos e regras específicas de transformações e treinos intensivos.
- **Links Oficiais:** 
  - [Edhen 3: Guia de Regras Básicas](https://www.brunomoraesalves.com.br/edhen-3-guia-regras-basicas)
  - [Edhen 3: Guia de Transformações](https://www.brunomoraesalves.com.br/edhen-3-guia-transformacoes)
  - [Edhen 3: Guia de Treinamentos](https://www.brunomoraesalves.com.br/edhen-3-guia-treinamentos)

#### 2. Sistema SAGE (2d10 Engine)
- **Proposta:** Motor clássico autoral do autor centrado na curva probabilística de dois dados de dez faces ($2d10$), focado em emulação de anime épico e cosmos.
- **Mecânica Base:** Resolução em $2d10$ + modificadores contra dificuldade, com subsistemas dedicados à energia cósmica, queima de cosmo e golpes especiais.
- **Links Oficiais:**
  - [SAGE: Livro Básico](https://www.brunomoraesalves.com.br/sage-basico)
  - [SAGE: Saint Seiya (Cavaleiros do Zodíaco)](https://www.brunomoraesalves.com.br/sage-saint-seiya)

#### 3. Sistema StoryFighter (Jogos de Luta & Ação)
- **Proposta:** Motor dinâmico criado em 2012 dedicado a emular jogos de luta (*fighting games* estilo Street Fighter e anime brawlers).
- **Mecânica Base:** Gestão de combos, iniciativas rápidas, super-barras e golpes característicos por arquétipos de lutadores.
- **Links Oficiais:**
  - [StoryFighter: Módulo Básico](https://www.brunomoraesalves.com.br/storyfighter-basico)
  - [StoryFighter: Suplemento Cavaleiros de Ouro](https://www.brunomoraesalves.com.br/storyfighter-cavs-ouro)

---

## 11. Sistemas & Cenários de Afrofantasia, Afrofuturismo e Afro-Urbano

Mapeamento de sistemas autorais e cenários focados em cosmovisões africanas, espiritualidade de matriz iorubá/banto, periferias, negritude e estética afrofuturista:

### 1. Kalymba RPG
- **Criador / Editora:** Daniel Pirraça (2021)
- **Subgênero:** Afrofantasia Épica Ancestral
- **Proposta:** Ambientado no vasto continente mítico de *Aiyê*, afasta-se radicalmente do medievalismo europeu tradicional. O mundo é governado pela energia cósmica do *Axé*, com presença viva de Orixás, magias orais ("mandingas"), guerreiros ancestrais e criaturas do folclore africano.
- **Mecânica Base:** Sistema autoral baseado em $2d6 + \text{bônus}$, sem classes rígidas de personagem; o protagonista é customizado através de históricos, dádivas ancestrais e conexões espirituais.

### 2. Mojubá RPG
- **Criadores:** Lucas Conti e Lucas Sampaio (2023)
- **Subgênero:** Afrofuturismo & Cyberpunk Afro-Urbano
- **Proposta:** Ambientado em uma metrópole futurista inspirada no Rio de Janeiro, Salvador e Lagos. Os personagens são "Crias" — jovens dotados de poderes herdados de seus Orixás de cabeça que combatem corporações predatórias e espíritos corrompidos (*Kiumbas*).
- **Mecânica Base:** Resolução em $2d6$ somados aos quatro atributos fundamentais: *Ipá* (Força física), *Ori* (Inteligência/Equilíbrio mental), *Ginga* (Destreza e malemolência) e *Gana* (Força de vontade e ímpeto).

### 3. O Último Ancestral RPG
- **Criador:** Alê Santos (baseado no romance homônimo premiado)
- **Subgênero:** Afrofuturismo Cyberpunk & Fantasia Periférica
- **Proposta:** Ambientado na cidade segregada de Nagast, dominada pela elite dos tecnocratas e pelos deuses cibernéticos. Retrata a luta dos "Mos primates" e favelados que resgatam o poder dos Ancestrais e a magia dos Orixás para quebrar as correntes da opressão sistêmica.

### 4. Odú RPG
- **Criadores:** Coletivo Odú RPG (Brasil)
- **Subgênero:** Misticismo Tradicional dos Orixás & Cosmologia Iorubá
- **Proposta & Inovação:** Substitui completamente os dados poliédricos ocidentais pelo **Jogo de Búzios tradicional (Mergindilogum)**. Cada lançamento de 16 búzios lê os búzios abertos e fechados para determinar o *Odú* regente da ação, consultando mensagens oraculares e intervenções divinas na cena.

### 5. Malandros: Tales from the streets of Rio
- **Criador:** Tom McGenery (2016)
- **Subgênero:** Drama Histórico Afro-Urbano
- **Proposta:** Ambientado no Rio de Janeiro de 1889, logo após a Abolição da Escravidão. Explora a boêmia, a capoeira marginalizada, os sambistas, malandros, prostitutas e imigrantes que lutavam pela sobrevivência nas ruas da então capital imperial/republicana.
- **Mecânica Base:** Baseado no motor *DramaSystem* (de Robin D. Laws), focado em diálogos, demandas emocionais e conflitos interpessoais sem combate convencional.

### 6. The Wagadu Chronicles
- **Criador:** Twin Drums (Allan Cudicio)
- **Subgênero:** Afrofantasia Primordial
- **Proposta:** Cenário transmídia (suplemento de RPG 5e e MMORPG) fortemente ancorado em tradições da África Ocidental e Oriental (como povos Iorubá e Maasai). Elimina o conceito eurocêntrico de "raças" de fantasia em favor de Linhagens Ancestrais, com grande profundidade de totens, espíritos e tabus culturais.

### 7. Swordsfall
- **Criador:** Brandon Dixon
- **Subgênero:** Afropunk Sci-Fantasy
- **Proposta:** Ambientado no mundo vibrante de Tikor, une arquitetura pré-colonial africana a roupas de alta-costura, neon, implantes cibernéticos e tecnologia movida a espíritos ancestrais.
- **Mecânica Base:** Focado em regras narrativas com dados temáticos e criação de conflitos cinematográficos anti-coloniais.

### 8. Spears of the Dawn
- **Criador:** Kevin Crawford (Sine Nomine Publishing, 2013)
- **Subgênero:** Sword & Sorcery Africano (OSR)
- **Proposta:** Cenário completo nas terras de Baharna inspirado em reinos africanos antigos (Mali, Songai, Grande Zimbábue). Mecânica OSR d20 clássica com classes como o Griot (bardo orador), Marabout (sábio espiritual) e Nganga (feiteceiro xamânico).

### 9. Into the Mother Lands
- **Criadores:** Tanya DePass (Cypheroftyr), B. Dave Walters e equipe BIPOC (2021)
- **Subgênero:** Sci-Fi Espacial Afrofuturista
- **Proposta:** Odisseia interestelar no planeta Musalia onde expedições humanas de matriz africana prosperaram sem colonialismo ou escravidão, focando em ciência ancestral, comunidades prósperas e exploração alienígena.

---

## 12. Motores Japoneses, JRPG & Anime

### Sword World 2.0 / 2.5
- **Criadores / Editora:** Kei Kitazawa e Group SNE (1989 / 2018)
- **Proposta:** O RPG mais popular do Japão, clássico da fantasia de Lodoss.
- **Mecânica Base:** $2d6$ + bônus. Duplo 1 é falha com concessão de XP imediato; duplo 6 é sucesso automático. Dano gerado através da **Tabela de Potência (Power Table)** da arma específica.
- **Link Oficial:** [Group SNE Sword World](https://www.groupsne.co.jp/products/sw/index.html)

### Fabula Ultima (TTJRPG)
- **Criador / Editora:** Emanuele Galletto / Need Games! (2022)
- **Proposta:** Emulação de clássicos de console como Final Fantasy e Octopath Traveler.
- **Mecânica Base:** Combina dois atributos em dados escalonados (ex: DES $d8$ + AST $d10$). O maior dado define o dano base (High Roll); pares iguais de 6+ geram críticos.
- **Link Oficial:** [Need Games Fabula Ultima](https://www.needgames.it/fabula-ultima-en/)

---

## 13. Tabela Comparativa Rápida de Resolução

| Engine / Família | Tipo de Rolagem | Resolução Central | Foco de Experiência |
| :--- | :--- | :--- | :--- |
| **d20 Clássico / T20** | $1d20 + \text{mod}$ | Roll-over ($\ge \text{CD}$) | Fantasia heroica, progressão tática |
| **Daggerheart** | $2d12$ (Dualidade) | Roll-over + Esperança vs. Medo | Drama narrativo heroico e economia de mesa |
| **d12 RPG / d12GO!** | $1d12$ puro ou $+ \text{mod}$ | Roll-over / Faixas de sucesso | Tática independente e one-shots rápidas |
| **YZE (Year Zero)** | Pool de $d6$ / Step | Contagem de 6s com Push | Sobrevivência, escassez e horror |
| **OpenD6** | Pool de $d6$ + Wild Die | Soma dos dados vs. CD | Ação cinematográfica e space opera |
| **Forged in the Dark** | Pool de $d6$ | Maior dado ($6$ pleno, $4–5$ parcial) | Golpes criminosos, estresse e facções |
| **PbtA (2d6) / 2d6World**| $2d6 + \text{mod}$ | Faixas fixas ($10+, 7–9, 6-$) | Emulação narrativa de gêneros |
| **2d6Solo / 2d10Solo** | $2d6$ ou $2d10$ | Tabelas de oráculo e perguntas | RPG sem mestre e jogo solitário |
| **BRP / Call of Cthulhu**| $1d100$ | Roll-under ($\le \text{Perícia}$) | Realismo, letalidade e investigação |
| **GURPS** | $3d6$ somados | Roll-under em curva de sino | Simulação universal modular |
| **Savage Worlds** | Step Dice + $1d6$ | Maior dado $\ge 4$ com explosão | Ação ágil, cartas e combate pulp |
| **Kalymba (Afrofantasia)**| $2d6 + \text{mod}$ | Roll-over em mundo mítico | Fantasia africana ancestral com Axé |
| **Dharma RPG (Universal)**| Poliédricos ($d4$–$d20$) | Atributos BD, MV, MN, SP + OGL | Universalidade, tática e Dharma/Karma |
| **Mojubá (Afro-Urbano)** | $2d6 + \text{Atributo}$ | Ipá, Ori, Ginga e Gana | Afrofuturismo urbano e Orixás |
| **Odú RPG** | 16 Búzios | Abertos vs. Fechados (Odús) | Divinação e espiritualidade iorubá |
| **GUMSHOE** | Automático / $1d6$ | Pistas sem rolagem / reservas | Investigação sem travamentos |
| **Cairn / Into the Odd**| $1d20$ + Auto-Hit | Roll-under fora de combate / Dano direto | Letalidade NSR ágil |
| **Ironsworn** | $1d6$ vs. $2d10$ | Comparar Ação contra Desafios | Solo, cooperativo sem mestre e juramentos |
