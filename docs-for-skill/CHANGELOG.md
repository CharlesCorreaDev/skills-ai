# Changelog - Docs for Skill 🧩

All notable changes to the `docs-for-skill` skill will be documented in this file.  
*Todas as alterações notáveis na skill `docs-for-skill` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.4.0-beta] - 2026-11-13

### Added / Adicionado
- **Defesa Contra Tool Poisoning (OWASP MCP Top 10) & Protocolo Agent Postmortem:**
  - Inclusão do princípio de não-confiança em descrições de ferramentas e inputs de APIs externas para prevenir ataques de *Confused Deputy* e injeções de prompt indiretas.
  - Implementação do protocolo de aprendizado contínuo com registro obrigatório de postmortems em falhas de compilação ou de lógica (`memory/learnings.md`).

---

## [0.3.0-beta] - 2026-11-09

### Added / Adicionado
- **Auditoria Adversarial Cloudflare & Anti-Alucinação NVIDIA:** Diretrizes obrigatórias de segurança via cloudflare/security-audit-skill e blindagem contra números inexistentes com NVIDIA/auto-ontology (security-audit-and-auto-ontology.md).

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
  - Pipeline de estruturação e particionamento de documentos Markdown em skills modulares (capítulos, cheatsheet, glossary, patterns).
  - Arquivo `VERSION` para governança de versão e detecção por agentes.
