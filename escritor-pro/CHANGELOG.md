# Changelog - Escritor Pro

Todas as mudanças notáveis nesta skill serão documentadas neste arquivo.
O formato é baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.0.0/),
e este projeto adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [0.1.0-beta.1] - 2026-11-14

### Adicionado
- **Arquitetura de Sub-agentes Especializados**: Orquestrador Mestre, Worldbuilder 6 Camadas, Dramaturgo de Cenas, Prosador Literário, Copywriter Estratégico, Consultor de RPG/Mesa, Filólogo & Corretor Normativo (MEC/ABL/VOLP) e Auditor de Continuidade & Anti-Slop.
- **Worldbuilding em 6 Camadas Progressivas**: Macro (Top-Down) a Micro (Bottom-Up) com DNA do mundo, cosmologia, folclore, ecologia/recursos, história viva, geopolítica e nível da rua.
- **Regra do Iceberg Narrativo (10/90)**: Modo Semente (5 perguntas cirúrgicas), Expansão Just-in-Time e Filtro Sensorial Obrigatório (3 sentidos + 1 tensão social).
- **Três Lentes de Saída (Single Source of Truth)**:
  - Modo Literário (`--modo livro`): prosa refinada sem metalinguagem, foco em subtexto e *show, don't tell*.
  - Modo Campanha / Mesa (`--modo rpg`): ganchos de aventura, 3 rumores (2 verdadeiros, 1 falso), relógios de facção/ameaça, segredos & pistas para RPGs (SWADE, Year Zero, D&D, Foundry VTT).
  - Modo Transmídia (`--modo ambos`): texto de ambientação/lore em prosa seguido de apêndice do mestre/autor recolhido.
- **Gramática Normativa e Estilo PT-BR Irrefutável**:
  - Alinhamento rigoroso às diretrizes do MEC, Academia Brasileira de Letras (ABL), Novo Acordo Ortográfico e VOLP.
  - Regras canônicas de pontuação de diálogo em Língua Portuguesa (uso correto de travessão `—` `\u2014`, verbos *dicendi* vs de ação, posicionamento de vírgula e ponto final).
  - Manual de vozes regionais autênticas do Brasil sem caricaturas pejorativas.
- **Copywriting, Headlines e Reaproveitamento**:
  - Frameworks de alta conversão (AIDA, PAS, BAB, 4Ps, QUEST, Star-Story-Solution).
  - Gerador de headlines de alto impacto psicológico.
  - Matriz de reaproveitamento de conteúdo multicanal.
- **Enigmas, Quebra-Cabeças e Desafios Mentais (`enigmas-e-quebra-cabecas.md`)**:
  - Implementação da Regra das Três Pistas (Justin Alexander) e princípio do *Fail Forward*.
  - 5 Categorias completas: Linguísticos/Criptográficos, Mecânicos/Físicos, Lógicos/Dedutivos, Sensoriais/Sinestésicos e Morais/Sacrifícios.
  - Handouts para jogadores e gabarito recolhido para o Mestre.
- **Filtro Anti-Slop e Humanização**:
  - Lista negra de clichês e marcadores estatísticos de IA.
  - Diretrizes de prosa visceral.
- **Scripts Auxiliares**:
  - `analisador_estilo.py`: verificação de travessões, densidade sensorial, slop de IA e métricas de prosa.
  - `consulta_lexico.py`: consulta léxica, sinônimos, regência e vocabulário semântico.
  - `validador_biblia.py`: validação estrutural de arquivos de lore e entidades em Markdown.
- **Integração Ecossistêmica**:
  - Suporte documentado a `grill-me`, `book-formatter`, `not-today-adhd`, `second-brain-plus`, `mcp-builder`, `website-for-markdown` e `humanizer-plus`.
