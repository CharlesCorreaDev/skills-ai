# Arquitetura dos 10 Subagentes Especializados — Book Formatter 📕➡️📄
## Suíte de Formatação, Tradução em Lotes e Diagramação de Livros de RPG — by GM Charles Corrêa

A suíte **Book Formatter** opera sob o padrão de **Engenharia Federada em Linha de Montagem com Quality Gates**, espelhando o fluxo de uma editora profissional especializada em livros complexos de RPG (World of Darkness, Vampire: The Masquerade, D&D, Tormenta20):

`mermaid
flowchart TD
    User([Usuário / Autor / GM]) --> Showrunner[1. Showrunner & Diretor Editorial]
    
    Showrunner --> SpecHandoff[2. Engenheiro de Specs, Escopo & SemVer]
    
    SpecHandoff --> Extractor[3. Engenheiro de Ingestão & PDF Oxide/OCR]
    
    Extractor --> Typographer[4. Analista Tipográfico, Fontes & Margens]
    Extractor --> RpgAnalyst[5. Especialista em Regras & Glossário RPG]
    
    Typographer & RpgAnalyst --> BatchTranslator[6. Tradutor em Lotes Estritos de 5 Páginas]
    
    BatchTranslator --> SemanticReviewer[7. Revisor Semântico, Fórmulas & Fidedignidade]
    
    SemanticReviewer --> Diagrammer[8. Diagramador & Compositor de PDF/MD/EPUB]
    
    Diagrammer --> QualityAuditor[9. Auditor Geral de Fidelidade Visual & Comparador de Páginas]
    
    QualityAuditor --> TechnicalWriter[10. Redator Técnico & Documentador Bilíngue EN/PT-BR]
    
    TechnicalWriter --> SpecHandoff
    SpecHandoff --> OutputFinal([Pacote Entregue: TXT, MD e PDF Fielmente Diagramado])
`

---

## 🏛️ Papéis e Responsabilidades dos 10 Subagentes

1. **Showrunner & Diretor Editorial:** Entrevista o autor via grill-me, define o estilo editorial, metas de páginas e orquestra as fases da esteira.
2. **Engenheiro de Specs, Escopo & SemVer:** Mapeia a estrutura do livro (capítulos, apêndices), critérios de aceitação e versionamento de artefatos.
3. **Engenheiro de Ingestão & PDF Oxide:** Executa extração ultraveloz com pdf_oxide (Rust) ou OCR avançado (docling/
ougat em scans antigos) sem quebrar colunas.
4. **Analista Tipográfico, Fontes & Margens:** Mapeia fontes exatas (serifas, títulos góticos, capitulares), pesos, entrelinhas e caixas de texto decoradas.
5. **Especialista em Regras & Glossário RPG:** Ingesta glossários canônicos de sistemas (WoD, D20, YZE) e garante coerência mecânica e terminológica.
6. **Tradutor em Lotes Estritos de 5 Páginas:** Tradução progressiva em micro-lotes (5 a 10 páginas por vez), impedindo alucinações ou omissão de parágrafos.
7. **Revisor Semântico, Fórmulas & Fidedignidade:** Compara o texto traduzido contra o original em inglês linha por linha, validando tabelas e cálculos.
8. **Diagramador & Compositor de PDF/MD/EPUB:** Reconstrói o layout original (duas colunas, caixas de citação, ornamentos de borda e posicionamento de imagens).
9. **Auditor Geral de Fidelidade Visual (Portão Obrigatório):** Compara página por página do PDF gerado com o original, garantindo o mesmo número exato de páginas (page count).
10. **Redator Técnico & Documentador Bilíngue:** Produz documentação técnica do livro, glossários gerados e relatórios de conformidade em EN e PT-BR.
