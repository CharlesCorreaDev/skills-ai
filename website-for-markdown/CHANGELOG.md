# Changelog - Website for Markdown 🌐

All notable changes to the `website-for-markdown` skill will be documented in this file.  
*Todas as alterações notáveis na skill `website-for-markdown` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.3.0-beta] - 2026-10-28

### Added / Adicionado
- **Motor Nativo de Crawling Recursivo Local (`--crawl` sem depender de Firecrawl API):**
  - Rastreamento recursivo em largura (BFS) seguindo automaticamente todos os links internos do mesmo prefixo de caminho (`get_scope_prefix`), impedindo vazamento para outros idiomas ou domínios externos (ex: mantém estritamente dentro de `https://www.php.net/manual/pt_BR/`).
  - Modo **HTTP Multi-Thread Rápido (`--fast` / `--engine http` com `--workers`)** com fallback automático para Playwright Headless Chromium (reutilizando o mesmo contexto de navegador em toda a fila).
  - **Limpeza Cirúrgica de DOM & Reescrita de Links Internos:** Isola o container principal (`#layout-content`, `article`, `main`), remove menus, rodapés e notas de usuários (`#usernotes`, `.contribute`) e reescreve todos os `<a href="...">` internos (`.php`/`.html`) para apontarem diretamente para os arquivos `.md` locais salvos.
  - **Controle de Limites, Filtros Regex e Retomada (Resume Cache):** Adicionados `--max-pages` (`0` = ilimitado), `--max-depth`, `--include`, `--exclude`, `--selector`, `--no-resume` e geração automática de `_INDEX.md` e `crawl_manifest.json`.
  - **Perfilador Automático de Hardware e Controle Eco Adaptativo (`detect_hardware_budget` & `guard_memory_pressure`):** Inspeção em tempo real do modelo de CPU, núcleos lógicos, RAM total e RAM livre da máquina operante; ajuste automático conservador de threads (~15-20% da CPU), redução de prioridade do processo no SO (`BELOW_NORMAL_PRIORITY_CLASS` / `nice(10)`), streaming direto de disco em micro-lotes (sem carregar pacotes inteiros na RAM), coleta de lixo ativa (`gc.collect()`) e pausa preventiva se o uso de RAM ultrapassar `--max-ram-percent` (padrão 78%).

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
  - Motor de raspagem web híbrido (Firecrawl + Playwright/Chromium) para extração limpa de documentações e SPAs em Markdown.
  - Arquivo `VERSION` para governança de versão e detecção por agentes.
