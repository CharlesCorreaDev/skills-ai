# Changelog - Python Dev Expert 🐍

All notable changes to the `python-dev-expert` skill will be documented in this file.  
*Todas as alterações notáveis na skill `python-dev-expert` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.4.0-beta] - 2026-11-09

### Added / Adicionado
- **Linter e Formatador Ultrarrápido Ruff (uff-guide.md):** Adoção oficial do Ruff (Astral) como linter e formatador primário (uff check --fix . e uff format .), substituindo Flake8, Black e isort.
- **Auditoria Adversarial Cloudflare & Anti-Alucinação NVIDIA:** Diretrizes obrigatórias de segurança via cloudflare/security-audit-skill e blindagem contra números inexistentes com NVIDIA/auto-ontology.

---

## [0.3.0-beta] - 2026-11-09

### Added / Adicionado
- **Documentação Offline Completa do Python (pt-br 3.15) e Django (6.1):**
  - Mais de 1.200 arquivos `.md` integrados localmente (`python-docs/` e `django-docs/`) com índices mestres para eliminar consumo desnecessário de tokens e chamadas web.
- **Blindagem Contra Vulnerabilidades Recentes (2024–2026) em `security-cves.md`:**
  - Código defensivo contra `CVE-2026-19445` (SSL Use-After-Free), `CVE-2026-4519` (Injeção de comandos em `webbrowser`), `CVE-2024-9287` (RCE em `venv`), `CVE-2024-11168` (SSRF em `urllib`), `CVE-2024-6232` (ReDoS/Tar Slip) e Pillow RCE (`CVE-2026-112900`).
- **Prioridade Absoluta do PDF Oxide (`pdf-oxide-guide.md`):**
  - Mandato de uso do `PDF Oxide` (`pip install pdf-oxide`) como **1º Lugar Obrigatório** para leitura e metadados de PDFs em Python (~0.8ms).
- **Integração com Bootstrap UX/UI Plus e Django (`django-bootstrap-guide.md`):**
  - Instalação obrigatória da skill companheira `bootstrap-ux-ui-plus`, templates base Mazer/AdminKit, tema claro por padrão, paleta #90271 e formulários acessíveis para daltônicos com `crispy-bootstrap5`.
- **Padrões Canônicos de Engenharia SOTA (`engineering-standards.md`):**
  - Test-Driven Development (TDD) com ciclo Red-Green-Refactor, Systematic Debugging em 4 etapas, logging estruturado em JSON com `structlog`, gestão tipada de ambiente com `pydantic-settings` e auditoria Trail of Bits (Semgrep/CodeQL).
- **Novo `README.md` Oficial da Skill:**
  - Guia completo bilíngue documentando todos os pilares técnicos e módulos da skill.

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
  - Diretrizes para Python 3.8 até 3.16, validação automática da versão no host, Django 6.1, FastAPI e boas práticas de tipagem.
  - Arquivo `VERSION` para governança de versão e detecção por agentes.
