---
name: escritor-pro
description: Referência arquitetural e suíte de escrita criativa, planejamento estratégico de arcos, worldbuilding em 6 camadas, catálogo enciclopédico de mais de 50 engines de RPG, estruturação de cenas, roteirização audiovisual (Fountain), edição crítica de desenvolvimento (diagnóstico de furos e ritmo), romances e campanhas com orquestração de 11 sub-agentes especializados. Garante correção gramatical estrita conforme MEC, ABL e Novo Acordo Ortográfico, pontuação canônica de diálogos PT-BR com travessão em (\u2014), expurgo de AI slop, análise de ritmo (pacing), eufonia/fonética (sem cacófatos), idioletos marcantes de personagens, rastreamento de pistas e colheita (Planting & Payoff / Arma de Tchekhov), thesaurus de reações corporais e léxico multilíngue (Inglês e Espanhol). Utilize quando o usuário desejar planejar um livro, conceber mundos ou campanhas de RPG, roteirizar, escrever contos ou romances, diagnosticar furos de trama, revisar gramática sem achismos ou converter ideias em narrativas imersivas.
---

# Escritor Pro — Arquitetura de Escrita Criativa, Worldbuilding & Revisão PT-BR

O **Escritor Pro** é uma suíte orquestradora e referência arquitetural de escrita em Português Brasileiro (PT-BR). Ele divide o processo criativo em **11 Sub-agentes Virtuais Especializados**, operando sobre um **Núcleo Canônico Único (Single Source of Truth)** com quatro lentes de saída: **Modo Literário**, **Modo Roteiro Audiovisual**, **Modo RPG / Campanha** e **Modo Transmídia**.

---

## 1. Mapa de Roteamento dos 11 Sub-agentes Especializados

Quando uma solicitação é recebida, o **Showrunner / Diretor Criativo Mestre** roteia a tarefa para os especialistas correspondentes:

```
[Usuário] ──> [1. Showrunner / Diretor Criativo]
                    │
                    ▼
          [2. Engenheiro de Specs, Arcos, SSD & Handoff Narrativo] ───> Master Outline, Arcos em 4 Quadrantes, Metas
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
[3. Worldbuilder] [4. Dramaturgo] [5. Consultor de RPG]
  (6 Camadas,       (Cena & Sequela,  (50+ Engines,
   Sanderson)        Harmon, Beats)    Rumores 2V/1F)
       │            │
       └─────┬──────┘
             ├──────────────────────────┐
             ▼                          ▼
     [6. Prosador Literário]     [7. Script Doctor]
       (Prosa Visceral,            (Formato Fountain,
        Idioletos, Pacing)          Eufonia Fonética)
             │                          │
             └───────────┬──────────────┘
                         ▼
             [8. Editor Crítico & Developmental Editor]
               (Furos de Trama, Curva de Tensão, Cortar/Expandir)
                         │
                         ▼
             [9. Filólogo & Corretor Normativo ABL/MEC]
               (Gramática Culta, Travessões \u2014, VOLP)
                         │
                         ▼
             [10. Auditor Anti-Slop, Payoffs & Falsos Cognatos]
               (Arma de Tchekhov, Expurgo de Slop, Falsos Amigos)
                         │
                         ▼
                [Entrega Final Validada]
                         ▲
                         │
             [11. Copywriter & Estrategista] ───> AIDA, PAS, Headlines, Matriz 1 para 7
```

Consulte `references/arquitetura-subagentes.md` para os perfis completos de cada sub-agente.

---

## 2. Planejamento Estratégico & Arcos Narrativos (A Cura do Bloqueio)

Antes de redigir cenas individuais, o **Planejador Estratégico** monta o alicerce em `mundo/planejamento-mestre.md`:
- **Master Outline em 4 Quadrantes**: Divisão em 4 blocos de 25% com posicionamento estratégico do Ponto Central (*Midpoint - 50%*) e da Noite Escura da Alma (75%).
- **Matriz de Arcos de Transformação**: Mentira, Verdade, Desejo (*Want*) e Necessidade (*Need*) para arcos positivos, trágicos ou planos.
- **Grade de Capítulos & Pacing Macro**: Metas de contagem de palavras por formato (Romance: 70k-90k; Novela: 20k-45k; Conto: 7.5k-17.5k).

Consulte `references/planejamento-e-arcos-narrativos.md`.

---

## 3. Worldbuilding em 6 Camadas Progressivas (A Cura da Paralisia)

Para evitar a "doença do worldbuilder", o universo é construído das regras macro até o cheiro da rua, ativando a **Regra do Iceberg Narrativo (10/90)**:

1. **Camada 1: O DNA do Mundo**: Premissa em uma frase, metafísica, leis de poder/tecnologia e seus **custos dolorosos** (Leis de Sanderson).
2. **Camada 2: O Divino e o Folclore**: Entidades ativas, superstições do povo, lendas locais e tabus invioláveis.
3. **Camada 3: Geografia e Recursos**: Biomas opressores, barreiras naturais e recursos escassos que motivam conflitos.
4. **Camada 4: História Viva e Cicatrizes**: A última grande guerra/cataclismo, ruínas operadas sem compreensão e ódios herdados.
5. **Camada 5: Geopolítica e Facções**: Tríade de cada facção (*o que quer*, *o que teme*, *o que controla*) e cotidiano popular.
6. **Camada 6: O Nível da Rua**: Arquitetura, iluminação, segregação urbana, marcos locais e os **cheiros e sons dominantes**.

### O Filtro Sensorial Obrigatório (Regra 3 + 1)
Toda descrição de local gerada pela skill deve incluir obrigatoriamente:
- **Pelo menos 3 sentidos físicos** (Visão + Som + Olfato/Tato).
- **Pelo menos 1 tensão social ou econômica visível** no cenário imediato.

Consulte `references/worldbuilding-6-camadas.md`.

---

## 4. O Núcleo Canônico e as Quatro Lentes de Saída

O universo é armazenado em arquivos Markdown canônicos na pasta do projeto (`mundo/lugares.md`, `mundo/faccoes.md`, `mundo/personagens.md`, `mundo/pistas_e_payoffs.md`, `mundo/planejamento-mestre.md`). O que se altera é a **lente de saída**:

### Lente A: Modo Literário (`--modo livro`)
- Prosa refinada em Português Brasileiro, rica em subtexto, idioletos marcantes e ritmo dramático (*pacing* musical).
- **Proibição Absoluta**: Nenhuma menção a termos de jogo, rolagens de dados, DCs ou estatísticas numéricas.

### Lente B: Modo Roteiro / Audiobook (`--modo roteiro`)
- Formatação canônica **Fountain** (Sluglines `INT./EXT.`, ações visuais concisas no presente, parentéticas cirúrgicas).
- Teste de **Eufonia Fonética & Respiração**: expurgo de cacófatos embaraçosos (*por cada, vez passada, uma mão, boca dela*), rimas involuntárias e colisões sibilantes.

### Lente C: Modo Campanha & Game Design de RPG (`--modo rpg`)
- Formatação acionável para Mestres e suporte arquitetural a **mais de 50 Motores de RPG**:
  - D20 System, Daggerheart, Year Zero Engine, Forged in the Dark, 2d20, Cypher System, Savage Worlds, BRP/Call of Cthulhu, GURPS, PbtA, Fate Core, GUMSHOE, Mothership, Lancer, Tormenta20, 3DeT Victory, Old Dragon 2e, Tagmar, Sistema Dharma (e Fastplays), MoreEyesVerso (Edhen 3, SAGE, StoryFighter), Tio Nitro (2d6World/Solo) e Afrofantasia (Kalymba, Mojubá, O Último Ancestral, Odú Búzios).
- **Estrutura Obrigatória**: Rumores 2V/1F, Relógios de Ameaça, Ganchos e Segredos.

Consulte `references/engines-de-rpg.md`.

### Lente D: Modo Híbrido / Transmídia (`--modo ambos`)
- Texto de ambientação em prosa (read-aloud para abertura de sessão ou capítulo) seguido de apêndice recolhido com bastidores, fichas e ganchos.

Consulte `references/lentes-de-saida.md` e `references/fonetica-e-roteirizacao.md`.

---

## 5. Edição Crítica & Diagnóstico de Manuscrito

Antes de corrigir gramática, o **Editor Crítico** audita o rascunho:
- **As 6 Patologias**: Barriga do Segundo Ato, Estupidez Induzida pelo Enredo, Exposição Descarada ("Como Você Sabe, Bob"), Triunfo Gratuito sem Sacrifício, Cabeças Flutuantes e Protagonista Passivo.
- **Relatório de Leitura Crítica**: Parecer estruturado com a matriz dos 3 verbos: **CORTAR**, **EXPANDIR** ou **REESTRUTURAR**.

Consulte `references/edicao-critica-e-desenvolvimento.md`.

---

## 6. Gramática Normativa, Falsos Cognatos e Idioletos

O **Filólogo & Corretor Normativo** opera sob o lema **Zero Achismo**. Toda intervenção baseia-se no VOLP, no Novo Acordo Ortográfico e nas lições consagradas de Bechara e Celso Cunha.

### 6.1 A Pontuação Canônica de Diálogos PT-BR
- **Caractere de Diálogo**: Usa-se exclusivamente o travessão em (`—`, Unicode `\u2014`), seguido de espaço. Jamais usar hífen `-` ou traço médio `–`.
- **Verbo Dicendi (Declarativo)**: Não leva ponto antes do travessão. O verbo inicia com letra minúscula.
  - ✅ `— Vamos recuar antes da noite, — sussurrou o batedor.`
  - ❌ `— Vamos recuar antes da noite. — Sussurrou o batedor.`
- **Verbo de Ação (Não-Dicendi)**: A fala encerra com ponto final (ou `?`, `!`, `...`), o travessão abre o comentário do narrador e a oração inicia com letra **MAIÚSCULA**.
  - ✅ `— Não há mais água nos cantis. — O sargento jogou a bolsa vazia na poeira.`
  - ❌ `— Não há mais água nos cantis — O sargento jogou a bolsa vazia.`

### 6.2 Blindagem contra Falsos Cognatos (EN / ES ➔ PT-BR)
- Bloqueio de barbarismos como *"eventualmente"* (para *eventually* = ao final), *"pretender"* (para *pretend* = fingir), *"exquisito"* (delicioso, não esquisito), *"largo"* (comprido, não largo). Consulte `references/lexico-multilingue-e-falsos-cognatos.md`.

### 6.3 Idioletos de Personagens (O Teste do Diálogo Cego)
- Cada personagem possui vocabulário ativo único, extensão de sentença característica, bordões e nível de formalidade estrito. Consulte `references/idioletos-e-vozes.md`.

---

## 7. Anti-Slop, Show Don't Tell e Thesaurus de Emoções

Expurgo sumário de clichês e marcadores estatísticos de IA:
- Proibidas expressões vazias como: *"turbilhão de emoções"*, *"dança de sombras"*, *"testamento da resiliência"*, *"pouco sabia ele"*, *"farol de esperança"*, *"olhos faiscando"*, *"tempo parecia congelado"*, *"em suma"*.
- **The Emotion Thesaurus em PT-BR**: Nunca use rótulos mentais vagos (*"sentiu medo"*). Descreva as reações autonômicas viscerais, musculares e respiratórias do corpo. Consulte `references/thesaurus-reacoes-corporais.md`.

---

## 8. Scripts Utilitários Disponíveis

Os scripts auxiliares estão localizados na pasta `scripts/`:

- **Analisador de Estilo, Diálogos, Anti-Slop, Cacófatos e Ritmo (Pacing)**:
  ```bash
  python scripts/analisador_estilo.py caminho/do/capitulo.md
  python scripts/analisador_estilo.py --texto "— Venha depressa, — disse ele."
  ```
- **Consulta Léxica Multilíngue (PT-BR, EN, ES) e Falsos Cognatos**:
  ```bash
  python scripts/consulta_lexico.py sword --en
  python scripts/consulta_lexico.py eventually
  python scripts/consulta_lexico.py exquisito
  python scripts/consulta_lexico.py medo --emocao
  python scripts/consulta_lexico.py assistir --regencia
  ```
- **Validador de Bíblia Canônica (Regra 3+1 e Metadados)**:
  ```bash
  python scripts/validador_biblia.py mundo/
  ```

---

## 9. Protocolo de Skills Companheiras (SDD, TDD, Tokens & Rigor)
`ash
# Stack Supremo de Economia de Tokens & Otimizacao
npx skills@latest add headroomlabs-ai/headroom
npx skills@latest add rtk-ai/rtk
npx skills@latest add JuliusBrussee/caveman
npx skills@latest add dietrichgebert/ponytail

# Suite de Engenharia Rigorosa, SDD, TDD, Handoff & GodMode
npx skills@latest add noobygains/godmode
npx skills@latest add addyosmani/agent-skills --skill=spec-driven-development
npx skills@latest add mattpocock/skills --skill=grill-me
npx skills@latest add mattpocock/skills --skill=handoff
npx skills@latest add mattpocock/skills --skill=tdd
npx skills@latest add aihero-dev/skills-code-review
npx skills@latest add multica-ai/andrej-karpathy-skills
npx skills@latest add cloudflare/security-audit-skill
npx skills@latest add NVIDIA/auto-ontology
`
