# Changelog - Code Mode Builder ⚡💻🧩

All notable changes to the `code-mode-builder` skill will be documented in this file.  
*Todas as alterações notáveis na skill `code-mode-builder` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.2.0-beta] - 2026-11-13

### Added / Adicionado
- **Integração com `GoogleChrome/modern-web-guidance` e WebMCP:**
  - Padrões de arquitetura para **WebMCP no Navegador** combinados com Code Mode (sandbox de execução de scripts de página e inspeção DOM direta).
  - Uso de `modern-web-guidance legacy-scan <path>` nos repositórios-alvo de sandboxes web para auditar e assegurar código moderno sem APIs legadas ou vulnerabilidades de injeção.

---

## [0.1.0-beta] - 2026-11-13

### Added / Adicionado
- **Lançamento Inicial da Skill (`v0.1.0-beta`):**
  - Engenharia e orquestração de **Code Mode** (*Programmatic Tool Calling / CodeAct*) baseada nos estudos de Anthropic, Cloudflare, UTCP, Apple e Thoughtworks.
  - Padrões de Gateway MCP de 2 ferramentas (`search` + `execute`) para reduzir o overhead de contexto em até 95%.
  - Padrões de sandbox seguro (V8 Isolates, QuickJS WASM, Docker, Rust Rhai) com timeout, quotas de memória e Gate Pattern de isolamento de credenciais.
  - Scripts de diagnóstico de ambiente e scaffolding inicial em Python e Node.js.
  - Documentação mestra bilíngue em `SKILL.md` e `README.md`.

