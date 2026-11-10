# Changelog - SMS Legal Suite & MCP 📱⚡

Todas as alterações notáveis na skill e ferramentas do **SMS Legal** serão documentadas neste arquivo.

O formato é baseado no [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e adere ao [Semantic Versioning](https://semver.org/lang/pt-BR/).

---

## [1.1.0] - 2026-11-09

### Added / Adicionado
- **Auditoria Adversarial Cloudflare & Anti-Alucinação NVIDIA:** Diretrizes obrigatórias de segurança via cloudflare/security-audit-skill e blindagem contra números/tarifas inexistentes com NVIDIA/auto-ontology.

---

## [1.0.0] - 2026-11-04

### Adicionado / Added
- **Skill Principal (`SKILL.md`):**
  - Registro de diretrizes obrigatórias para agentes de IA (higienização de telefones DDI 55 + DDD + 9 dígitos, URL Encoding compulsório, gestão de credenciais e limite de 1.000 números por lote).
  - Espelhamento automático para o diretório `.agents/skills/sms-legal/SKILL.md`.
- **Servidor MCP Nativo Unificado (`mcp/`):**
  - Implementação em Node.js (`mcp/sms_legal_mcp_server.js`) sem dependências externas via JSON-RPC 2.0 stdio.
  - Implementação em Python 3 (`mcp/sms_legal_mcp_server.py`) com módulo nativo `urllib`.
  - Manual detalhado de integração (`mcp/README.md`) para Antigravity IDE, Claude Desktop e Cursor.
  - Ferramentas expostas: `sms_enviar_texto`, `sms_enviar_lote`, `sms_agendar`, `sms_consultar_status`, `sms_consultar_creditos`, `sms_consultar_respostas`, `sms_consultar_numero`, `sms_enviar_voz` e `sms_enviar_audio`.
- **SDKs Nativos de Integração (`integrations/`):**
  - **PHP** (`integrations/SmsLegalClient.php`): Classe compatível com PHP 7.4 a 8.5+, cURL nativo e tipagem estrita.
  - **Python** (`integrations/sms_legal_client.py`): Classe compatível com Python 3.8+, sem bibliotecas de terceiros.
  - **Node.js** (`integrations/sms_legal_client.js`): Módulo assíncrono nativo com Promises e https.
- **Documentação de Engenharia e Arquitetura:**
  - `cheatsheet.md`: Tabela rápida de endpoints, métodos e mapeamento completo de códigos de erro (`000` a `011`).
  - `patterns.md`: Padrões de arquitetura (BFF, filas com workers assíncronos, proteção contra bloqueio de URLs e rate-limit de lotes).
  - `glossary.md`: Glossário técnico com termos do ecossistema SMS Gateway (DDI+DDD, IdSMS, TTS, Portabilidade, Reply).
  - `README.md`: Apresentação completa e bilíngue da suite.

