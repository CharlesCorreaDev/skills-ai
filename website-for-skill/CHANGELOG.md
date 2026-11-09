# Changelog - Website for Skill 🚀

All notable changes to the `website-for-skill` skill will be documented in this file.  
*Todas as alterações notáveis na skill `website-for-skill` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.3.0-beta] - 2026-10-28

### Added / Adicionado
- **Suporte Completo a Crawling Recursivo Local e Portais de Grande Porte (`Scripts/build_skill.py`):**
  - Repasse completo dos parâmetros de crawling para `website-for-markdown` (`--crawl`, `--fast`, `--engine`, `--max-pages`, `--max-depth`, `--workers`, `--include`, `--exclude`, `--selector`, `--keep-raw`) e nova flag `--from-dir` para estruturar skills diretamente de pastas `.md` já baixadas.
  - **Preservação de Links Internos entre Capítulos:** Mantém os nomes semânticos originais dos arquivos em `chapters/` (ex: `chapters/index.md`, `chapters/security.intro.md`) para que todos os links relativos entre páginas funcionem nativamente.
  - **Agrupamento Inteligente por Categoria e Proteção de Context Window:** Gera `chapters/_INDEX.md` (evitando colisão case-insensitive com `index.md` no Windows/macOS) e resume automaticamente no `SKILL.md` por categorias quando o site possui mais de 40 páginas.
  - **Controle Adaptativo de Recursos (Baixo Consumo de CPU e RAM):** Redução automática da prioridade do processo no SO (`BELOW_NORMAL_PRIORITY_CLASS` / `nice(10)`), leitura parcial de cabeçalhos (512 bytes) em vez de carregar arquivos inteiros em memória, gravação de `_INDEX.md` em streaming direto para o disco e monitoramento contínuo de RAM com `gc.collect()` e pausas adaptativas (`--delay-ms`, `--max-ram-percent`).

---

## [0.2.0-beta] - 2026-10-25

### Added / Adicionado
- **Protocolo de Feedback Proativo e Abertura Autônoma de Issues no GitHub:** Geração de documentação técnica bilíngue (EN/PT) e abertura autônoma de issues via `gh issue create` perante bugs, ferramentas ausentes ou limitações no MCP.
- **Protocolo Obrigatório de Verificação e Revisão:** Validação sintática, execução de testes funcionais e integridade de caminhos antes de qualquer entrega.
- **Diretriz de Comentários Bilíngues de Código:** Comentários estritamente necessários devem ser escritos em Inglês e Português.

---

## [0.1.0-beta] - 2026-10-23

### Added / Adicionado
- **Lançamento Inicial da Skill (Beta):**
  - Pipeline autônomo que rastreia portais web e documentações de APIs, gerando skills completas e modulares.
  - Arquivo `VERSION` para governança de versão e detecção por agentes.
