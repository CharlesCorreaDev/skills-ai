---
name: escritor-pro
description: Referência arquitetural e suíte de escrita criativa, worldbuilding em 6 camadas, geração de enigmas e quebra-cabeças instigantes, estruturação de cenas, roteiros, romances e campanhas de RPG com orquestração de sub-agentes especializados. Garante correção gramatical estrita conforme MEC, ABL e Novo Acordo Ortográfico, pontuação canônica de diálogos PT-BR com travessão em (\u2014), expurgo de AI slop e copywriting persuasivo. Utilize quando o usuário desejar criar um mundo, conceber enigmas desafiadores para leitores ou jogadores de RPG, escrever capítulos ou contos, revisar gramática sem achismos, estruturar campanhas ou converter ideias em narrativas imersivas.
---

# Escritor Pro — Arquitetura de Escrita Criativa, Worldbuilding & Revisão PT-BR

O **Escritor Pro** é uma suíte orquestradora e referência arquitetural de escrita em Português Brasileiro (PT-BR). Ele divide o processo criativo em **8 Sub-agentes Virtuais Especializados**, operando sobre um **Núcleo Canônico Único (Single Source of Truth)** com três lentes de saída: **Modo Literário**, **Modo RPG / Campanha** e **Modo Transmídia**.

---

## 1. Mapa de Roteamento dos 8 Sub-agentes Especializados

Quando uma solicitação é recebida, o **Showrunner / Orquestrador Mestre** roteia a tarefa para os especialistas correspondentes:

```
[Usuário] ──> [1. Showrunner / Orquestrador]
                    │
                    ├──> [2. Worldbuilder] ─────────> 6 Camadas, Iceberg 10/90, Leis de Sanderson
                    ├──> [3. Dramaturgo] ───────────> Cena & Sequela, Dan Harmon, Save the Cat
                    ├──> [4. Prosador Literário] ───> Prosa Visceral, Show Don't Tell, Vozes BR
                    ├──> [5. Consultor de RPG] ─────> Rumores 2V/1F, Relógios, Foundry VTT
                    └──> [6. Copywriter] ───────────> AIDA, PAS, Headlines, Matriz 1 para 7
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
         [7. Filólogo ABL/MEC] ──> [8. Auditor Anti-Slop] ──> Entrega Final Validada
```

Consulte `references/arquitetura-subagentes.md` para os perfis completos de cada sub-agente.

---

## 2. Worldbuilding em 6 Camadas Progressivas (A Cura da Paralisia)

Para evitar a "doença do worldbuilder", o universo é construído das regras macro até o cheiro da rua, ativando a **Regra do Iceberg Narrativo (10/90)**:

1. **Camada 1: O DNA do Mundo**: Premissa em uma frase, metafísica, leis de poder/tecnologia e seus **custos dolorosos** (Leis de Sanderson).
2. **Camada 2: O Divino e o Folclore**: Entidades ativas, superstições do povo, lendas locais e tabus invioláveis.
3. **Camada 3: Geografia e Recursos**: Biomas opressores, barreiras naturais e recursos escassos que motivam conflitos.
4. **Camada 4: História Viva e Cicatrizes**: A última grande guerra/cataclismo, ruínas operadas sem compreensão e ódios herdados.
5. **Camada 5: Geopolítica e Facções**: Tríade de cada facção (*o que quer*, *o que teme*, *o que controla*) e cotidiando popular.
6. **Camada 6: O Nível da Rua**: Arquitetura, iluminação, segregação urbana, marcos locais e os **cheiros e sons dominantes**.

### O Filtro Sensorial Obrigatório (Regra 3 + 1)
Toda descrição de local gerada pela skill deve incluir obrigatoriamente:
- **Pelo menos 3 sentidos físicos** (Visão + Som + Olfato/Tato).
- **Pelo menos 1 tensão social ou econômica visível** no cenário imediato.

Consulte `references/worldbuilding-6-camadas.md` para o manual detalhado.

---

## 3. O Núcleo Canônico e as Três Lentes de Saída

O universo é armazenado em arquivos Markdown canônicos na pasta do projeto (`mundo/lugares.md`, `mundo/faccoes.md`, `mundo/personagens.md`). O que se altera é a **lente de saída**:

### Lente A: Modo Literário (`--modo livro`)
- Prosa refinada em Português Brasileiro, rica em subtexto e ritmo dramático.
- **Proibição Absoluta**: Nenhuma menção a termos de jogo, rolagens de dados, DCs ou estatísticas numéricas.

### Lente B: Modo Campanha / RPG (`--modo rpg`)
- Formatação acionável para Mestres (SWADE, Year Zero, D&D, Tormenta20, Foundry VTT).
- **Estrutura Obrigatória**:
  - **3 Rumores de Esquina**: 2 verdadeiros e 1 falso/distorcido.
  - **Relógios de Ameaça (Progress Clocks)**: 4 a 8 segmentos de contagem regressiva.
  - **3 Ganchos Imediatos**: Contratante, complicação e recompensa prometida.
  - **Segredos & Pistas**: Elementos fragmentados para investigação na mesa.

### Lente C: Modo Híbrido / Transmídia (`--modo ambos`)
- Texto de ambientação em prosa (read-aloud para abertura de sessão ou capítulo) seguido de apêndice recolhido com bastidores, fichas e ganchos.

Consulte `references/lentes-de-saida.md` para exemplos práticos.

---

## 4. Gramática Normativa e Correção Estrita (MEC / ABL / VOLP)

O **Filólogo & Corretor Normativo** opera sob o lema **Zero Achismo**. Toda intervenção baseia-se no VOLP, no Novo Acordo Ortográfico e nas lições consagradas de Bechara e Celso Cunha.

### 4.1 A Pontuação Canônica de Diálogos PT-BR
- **Caractere de Diálogo**: Usa-se exclusivamente o travessão em (`—`, Unicode `\u2014`), seguido de espaço. Jamais usar hífen `-` ou traço médio `–`.
- **Verbo Dicendi (Declarativo)**: Não leva ponto antes do travessão. O verbo inicia com letra minúscula.
  - ✅ `— Vamos recuar antes da noite — sussurrou o batedor.`
  - ❌ `— Vamos recuar antes da noite. — Sussurrou o batedor.`
- **Verbo de Ação (Não-Dicendi)**: A fala encerra com ponto final (ou `?`, `!`, `...`), o travessão abre o comentário do narrador e a oração inicia com letra **MAIÚSCULA**.
  - ✅ `— Não há mais água nos cantis. — O sargento jogou a bolsa vazia na poeira.`
  - ❌ `— Não há mais água nos cantis — O sargento jogou a bolsa vazia.`
- **Interrupção e Retomada**:
  - Com verbo dicendi: `— Se partirmos agora — advertiu ela —, alcançaremos o comboio.`
  - Com ação: `— Se partirmos agora... — Ela afivelou a couraça de couro. — Alcançaremos o comboio.`

### 4.2 Novo Acordo Ortográfico e Regência
- Sem acento em ditongos abertos paroxítonos (*ideia, jiboia, heroico*), mas mantido em oxítonos (*herói, constrói*).
- Queda do acento em hiatos *ee/oo* (*veem, leem, voo, enjoo*).
- Queda do trema em vocábulos da língua portuguesa (*tranquilo, cinquenta*).
- Regência verbal culta: *assistir ao espetáculo*, *visar ao poder*, *aspirar ao título*, *preferir a paz à guerra* (sem "do que"), *implicar prejuízo* (sem "em").

Consulte `references/gramatica-normativa-abl-mec.md` para tabelas completas.

---

## 5. Arquitetura de Cena e Enredo

- **Cena de Ação (Bickham/Swain)**: Objetivo Claro ➔ Conflito Crescente ➔ Desastre (*Não / Sim, mas / Não, e além do mais*).
- **Sequela Emocional**: Reação Fisiológica Visceral ➔ Dilema Doloroso ➔ Decisão Crítica.
- **Estruturas Dominadas**: Story Circle (Dan Harmon), Save the Cat (15 beats), Curva Fichteana e Kishōtenketsu.

Consulte `references/estrutura-de-cenas-e-enredo.md` e `references/generos-literarios.md`.

---

## 6. Copywriting, Headlines e Matriz 1 para 7

Transforme qualquer trecho de história ou cenário em divulgação de alta conversão:
- **Frameworks**: AIDA, PAS, BAB, 4Ps, QUEST.
- **Fórmula dos 4Us para Headlines**: Útil, Urgente, Único e Ultra-específico.
- **Logline em 25 Palavras**: `[Protagonista] + [Incidente Incitante] + [Objetivo] + [Antagonista] + [Altíssimo Risco]`.
- **Reaproveitamento 1 ➔ 7**: 1 capítulo se desdobra em artigo para blog, carrossel de 5 slides, 3 pílulas de lore, post de bastidores, roteiro para vídeo curto, gancho de RPG e enquete comunitária.

Consulte `references/copywriting-e-conteudo.md`.

---

## 7. Enigmas, Quebra-Cabeças e Desafios Mentais (Puzzles & Riddles)

Para criar mistérios, templos e desafios que façam leitores e jogadores de RPG pensarem profundamente sem frustração:
- **A Regra das Três Pistas**: Nunca dependa de uma pista única. Distribua 3 pistas independentes (óbvia, investigativa e sensorial).
- **Princípio do Fail Forward**: O erro dos personagens/jogadores nunca paralisa a história; gera uma complicação dinâmica imediata (o teto desce, o alarme toca, a água sobe).
- **Cinco Tipos de Enigmas Dominados**:
  1. *Linguísticos & Criptográficos* (Charadas poéticas em redondilha, cifras de deslocamento histórico, anagramas de deuses).
  2. *Mecânicos & Físicos* (Balanças de pesos e valores sagrados, vasos comunicantes de fluidos, engrenagens estelares).
  3. *Lógicos & Dedutivos* (Matrizes de exclusão, guardiões mentirosos e sinceros, o enigma do banquete envenenado).
  4. *Sensoriais & Sinestésicos* (Espectros de chamas alquímicas, harmonia de sinos de cristal, projeção de sombras no solstício).
  5. *Morais & Sacrifícios* (O custo das Leis de Sanderson aplicado a portas sagradas que exigem sangue, memória ou relíquias).

Consulte `references/enigmas-e-quebra-cabecas.md`.

---

## 8. Anti-Slop e Humanização Textual

Expurgo sumário de clichês e marcadores estatísticos de IA:
- Proibidas expressões vazias como: *"turbilhão de emoções"*, *"dança de sombras"*, *"testamento da resiliência"*, *"pouco sabia ele"*, *"farol de esperança"*, *"olhos faiscando"*, *"tempo parecia congelado"*, *"em suma"*.
- Aplicação contínua da técnica de **Show, Don't Tell**: substituir rótulos mentais abstratos por reações autonômicas, tensão muscular, cheiros e ações concretas.

Consulte `references/anti-slop-e-humanizacao.md`.

---

## 9. Integração com o Ecossistema de Skills

| Cenário de Uso | Skill Integrada | Como Utilizar |
| :--- | :--- | :--- |
| **Entrevista Investigativa Cirúrgica** | `grill-me` | Ao iniciar uma história ou mundo, faz 3 a 5 perguntas objetivas com opções recomendadas para destravar a premissa. |
| **Usuário Neurodivergente (TDAH/Autismo)** | `not-today-adhd` | Respostas em micro-blocos, ritmo passo-a-passo, linguagem direta sem sobrecarga cognitiva ou paralisia de escolha. |
| **Persistência de Memória do Projeto** | `second-brain-plus` | Salva a Bíblia do mundo, fichas de personagens e decisões canônicas em `.second-brain/` ou pasta do projeto. |
| **Leitura e Conversão de Documentos** | `book-formatter` / `docs-for-markdown` | Ingestão e conversão de PDFs, manuscritos antigos ou regras para Markdown legível por agentes. |
| **Criação de Prompts de Ilustração** | `image-to-prompt` | Engenharia reversa ou elaboração de prompts artísticos para capas e concept arts do universo. |
| **Descontaminação e Purga de Slop** | `humanizer-plus` | Remoção de caracteres de largura zero, despadronização de parágrafos sintéticos e de-watermarking. |
| **Integração com Ferramentas Externas** | `mcp-builder` | Construção de bridges MCP para dicionários, APIs lexicais ou ferramentas de escrita. |

---

## 10. Scripts Utilitários Disponíveis

Os scripts auxiliares estão localizados na pasta `scripts/`:

- **Analisador de Estilo, Diálogos e Anti-Slop**:
  ```bash
  python scripts/analisador_estilo.py caminho/do/capitulo.md
  python scripts/analisador_estilo.py --texto "— Venha depressa. — disse ele com um turbilhão de emoções."
  ```
- **Consulta Léxica, Regência Verbal e Vocabulário Normativo**:
  ```bash
  python scripts/consulta_lexico.py assistir --regencia
  python scripts/consulta_lexico.py ideia --acordo
  ```
- **Validador de Bíblia Canônica (Regra 3+1 e Metadados)**:
  ```bash
  python scripts/validador_biblia.py mundo/
  ```
