# Arquitetura Multiagente — Book Formatter 📕➡️📄

Para garantir diagramações impecáveis, traduções fiéis sem alucinação e preservação total de colunas, fontes e ornamentos visuais, a suíte opera com **8 Subagentes Especializados**:

`mermaid
flowchart TD
    User([Usuário / Autor / GM]) --> Showrunner[1. Orquestrador de Diagramação]
    Showrunner --> Extractor[2. Engenheiro de Ingestão & PDF Oxide]
    Extractor --> Typographer[3. Analista Tipográfico & Fontes]
    Typographer --> RpgAnalyst[4. Especialista em Regras & Glossário RPG]
    RpgAnalyst --> BatchTranslator[5. Tradutor em Lotes de 5 Páginas]
    BatchTranslator --> Reviewer[6. Revisor Semântico & Mecânico]
    Reviewer --> Diagrammer[7. Diagramador & Compositor de PDF/MD]
    Diagrammer --> Auditor[8. Auditor de Qualidade & Fidelidade Visual]
    Auditor --> OutputFinal([Pacote Entregue: TXT, MD e PDF Diagramado])
`

## Papéis e Responsabilidades dos 8 Subagentes:

1. **Orquestrador de Diagramação (Showrunner):**
   - Coordena o pipeline de 8 fases, define metas de páginas e orquestra handoffs entre extração, tradução e diagramação.
2. **Engenheiro de Ingestão & PDF Oxide:**
   - Executa extração ultrarrápida via pdf_oxide (ou OCR docling/
ougat em scans antigos). Garante extração limpa sem quebra de fluxo.
3. **Analista Tipográfico & Fontes:**
   - Inspeciona fontes originais do livro (serifas, góticas, títulos, caixas de texto), mapeia substitutas idênticas e define pesos/entrelinhas.
4. **Especialista em Regras & Glossário RPG:**
   - Ingesta os glossários canônicos (World of Darkness, D20, etc.) em glossarys/ e assegura coerência estrita de termos de jogo e atributos.
5. **Tradutor em Lotes de 5 Páginas:**
   - Realiza a tradução em micro-lotes rigorosos (5 a 10 páginas por vez), impedindo estouro de contexto, omissão de parágrafos ou alucinações.
6. **Revisor Semântico & Mecânico:**
   - Compara o texto em português com o original em inglês linha a linha, checando integridade matemática, tabelas e fórmulas de dados.
7. **Diagramador & Compositor de PDF/MD:**
   - Recria o layout no padrão original: duas colunas, caixas de citação decoradas, capitulares, bordas de página e ilustrações nas exatas posições.
8. **Auditor de Qualidade & Fidelidade Visual (Portão Final):**
   - Compara página por página do PDF gerado com o PDF original, garantindo a mesma paginação (page count), índice remissivo e entrega impecável.
