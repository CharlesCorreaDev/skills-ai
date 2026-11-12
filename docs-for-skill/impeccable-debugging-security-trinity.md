# Impeccable Design, Systematic Debugging & Trail of Bits Security Trinity in Skill Generation 🏛️🛡️🔬
# Tríade Canônica na Engenharia e Geração de Skills via Docs for Skill

> **Finalidade na Skill `docs-for-skill`:**  
> Este documento define os **Padrões Canônicos de Síntese, Validação e Extração** aplicados pelo motor do `docs-for-skill` (`structure_skill.py`) ao ingerir manuais técnicos, livros de regras, especificações de design, arquitetura e documentações de software, compilando-os em skills de IA de alta fidelidade sem ruído ("anti-slop"), com depuração sistemática e segurança em profundidade.

---

## 🎨 1. Impeccable Synthesis (Síntese Impecável & Eliminação de AI Slop nos Capítulos)

Ao ingerir e estruturar documentos densos (PDFs, DOCX, Manuais, Livros de Regras e Design Systems):

### 🚫 Anti-Patterns de Extração Proibidos pelo Motor:
1. **Prolixidade & Introduções Genéricas ("AI Slop"):**
   - O pipeline elimina sumários repetitivos, preâmbulos bajuladores ou divagações de modelo. Cada capítulo em `chapters/` deve iniciar diretamente com definições conceituais canônicas ou tabelas normativas.
2. **Aninhamento Visual Indevido & Fragmentação:**
   - Evita subseções desnecessárias de 4º e 5º nível (`####`, `#####`). O motor agrupa conceitos logicamente em blocos limpos, com uso equilibrado de espaçamento, listas e tabelas sintéticas.
3. **Preservação de Escala & Tipografia Conceitual:**
   - Termos canônicos de UI, Design Systems, diagramação e regras devem ser compilados com formatação consistente (ex: código em monospaço, classes CSS identificadas, títulos claros).
4. **Resumos de Alta Densidade de Informação:**
   - Prioriza a relação token/conhecimento: maximiza o valor de cada token para que os agentes de IA não sofram de atenção difusa (*lost in the middle*).

---

## 🔬 2. Systematic Ingestion & Debugging (Validação Sistemática de Integridade do Conhecimento)

Ao processar documentos com equações, tabelas de dados, árvores de decisão ou trechos de código:

### 🛑 Regra de Ouro: Proibido Alucinar Dados ou Parâmetros
O pipeline de extração do `docs-for-skill` nunca "adivinha" fórmulas quebradas ou colunas faltantes.

### O Ciclo em 4 Etapas na Geração de Skills:
1. **Inspeção de Layout e Extração:**
   - Detecta quebras de colunas, hifenização rompida, tabelas complexas com células mescladas e blocos de código com caracteres corrompidos.
2. **Hipótese e Isolamento de Ruído:**
   - Se um trecho de texto estiver ambíguo ou corrompido no PDF/documento original, o compilador isola a seção e sinaliza a incerteza em vez de inventar números ou regras inexistentes.
3. **Validação Estrutural dos Arquivos de Saída:**
   - O compilador verifica automaticamente a existência e integridade dos arquivos gerados:
     - `SKILL.md`: Mapa mental bilíngue (EN/PT) e roteamento de capítulos.
     - `cheatsheet.md`: Tabelas de consulta rápida.
     - `glossary.md`: Dicionário canônico de entidades e termos.
     - `patterns.md`: Padrões arquiteturais e fluxos de decisão.
4. **Verificação Sintática e Markdown Lint:**
   - Confirmação de que links internos entre capítulos, âncoras e blocos de código estão sintaticamente perfeitos.

---

## 🛡️ 3. Trail of Bits Security & Safe Artifact Ingestion (Segurança na Extração e Execução)

Ao compilar documentos que contêm código de exemplo, especificações de APIs, esquemas de bancos de dados ou scripts executáveis:

### Diretrizes de Blindagem na Geração da Skill:
1. **Sanitização de Payloads e Comandos Extraídos:**
   - Scripts gerados ou extraídos de manuais são blindados contra comandos destrutivos sem confirmação (`rm -rf`, `shell=True` sem escape, queries SQL cruas sem parametrização).
2. **Classificação de Riscos e Avisos Explícitos (Alerts):**
   - Ao detectar trechos documentais sobre configurações de rede, credenciais, autenticação ou infraestrutura, o motor injeta automaticamente alertas visuais no padrão GitHub:
     > `> [!WARNING]` ou `> [!CAUTION]` para operações perigosas, prevenindo que agentes de IA executem comandos inseguros sugeridos por manuais legados.
3. **Prevenção de Injeção de Prompt no Conteúdo Ingerido:**
   - Tratamento de textos de terceiros para evitar que instruções maliciosas contidas em documentos ingeridos manipulem as instruções de sistema do agente executor.
4. **Verificação de Dependências e Ambientes Limpos:**
   - O script de validação de ambiente (`scripts/check_env.py`) checa a saúde dos binários locais (Pandoc, LibreOffice, Tesseract, bibliotecas Python) sem expor caminhos confidenciais ou variáveis de ambiente com credenciais.
