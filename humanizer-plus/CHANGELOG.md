# Changelog - Humanizer Plus 🧠🛡️✨

All notable changes to the `humanizer-plus` skill will be documented in this file.  
*Todas as alterações notáveis na skill `humanizer-plus` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-10-25

### Added / Adicionado
- **Lançamento Inicial da Skill Humanizer Plus:**
  - Arquitetura de saneamento em Duas Camadas:
    - **Camada A (Saneamento Físico & Determinístico):** Purgagem de caracteres invisíveis (zero-width spaces `U+200B`, `U+FEFF`, `U+200C`, `U+200D`, marcas direcionais), normalização de aspas tipográficas (`“ ”`) para aspas retas ASCII, remoção de metadados de contêineres e tags C2PA.
    - **Camada B (Dispersão Estatística & Humanização Textual):** Quebra de viés n-gram (SynthID) via reestruturação oracional e dispersão sintática; eliminação de 26 vícios de IA adaptados do WikiProject AI Cleanup para PT-BR e EN; preservação de fatos e variáveis técnicas.
  - **Tabela de Substituições Idiomáticas:** Dicionário de conversão de expressões corporativas/artificiais em linguagem direta e humana.
  - **Diretrizes para Código-Fonte:** Regras para desmarcação de scripts e macros (early returns, remoção de comentários acadêmicos óbvios e cabeçalhos de IA).
  - **Scripts Utilitários Nativos:**
    - `scripts/sanitize.js`: Script Node.js de varredura e limpeza recursiva em lote.
    - `scripts/sanitize.py`: Script Python alternativo.
  - **Matriz de Avaliação (50 Pontos):** Rubrica de scoring cobrindo Diretividade, Ritmo, Confiança no Leitor, Autenticidade e Densidade.
