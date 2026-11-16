# Suíte de Engenharia Rigorosa: SDD, Handoff, Grill-Me & TDD
## Rigorous Engineering Suite: Spec-Driven Development, Handoff, Grill-Me & Test-Driven Development

Este guia consolida o quarteto oficial de metodologias e skills companheiras obrigatórias para todas as tarefas de desenvolvimento, arquitetura e entrega contínua do ecossistema **Skills AI**:

This guide consolidates the official quartet of companion skills and methodologies required across all development, architecture, and continuous delivery tasks within the **Skills AI** ecosystem:

---

## 🛠️ Comandos de Instalação Canônicos / Canonical Installation Commands

`ash
# 1. Spec-Driven Development (Addy Osmani)
npx skills@latest add addyosmani/agent-skills --skill=spec-driven-development

# 2. Grill-Me (Matt Pocock / AI Hero)
npx skills@latest add mattpocock/skills --skill=grill-me

# 3. Handoff (Matt Pocock / AI Hero)
npx skills@latest add mattpocock/skills --skill=handoff

# 4. Test-Driven Development / TDD (Matt Pocock / AI Hero)
npx skills@latest add mattpocock/skills --skill=tdd

# 5. Rigor de Engenharia & GodMode (NoobyGains)
npx skills@latest add noobygains/godmode

# 6. Revisão de Código e Auditoria de Segurança
npx skills@latest add aihero-dev/skills-code-review
npx skills@latest add multica-ai/andrej-karpathy-skills
npx skills@latest add cloudflare/security-audit-skill
npx skills@latest add NVIDIA/auto-ontology
`

---

## 1. 📋 Spec-Driven Development (SDD) — Addy Osmani
- **Origem / Source:** [ddyosmani/agent-skills](https://github.com/addyosmani/agent-skills/blob/main/skills/spec-driven-development/SKILL.md)
- **🇧🇷 Propósito:** Força a IA a elaborar uma especificação técnica formal (PRD / Tech Spec / RFC) e critérios de aceitação mensuráveis antes de escrever uma única linha de código. Elimina presunções cegas e alinhamentos ambíguos.
- **🇺🇸 Purpose:** Forces the AI agent to produce a structured specification or Product Requirements Document (PRD) before generating implementation code. Prevents scope ambiguity and blind guessing.
- **Ciclo de 4 Etapas:**
  1. *Specify (Definição):* Transforma ideias vagas em critérios de sucesso mensuráveis e limites explícitos (*o que fazer*, *o que perguntar primeiro*, *o que nunca fazer*).
  2. *Plan (Design Técnico):* Arquitetura de componentes, dependências e análise de riscos.
  3. *Tasks (Fatiamento Atômico):* Decompõe a entrega em tarefas atômicas e verificáveis.
  4. *Implement (Execução Controlada):* Handoff estruturado para o ciclo de TDD.

---

## 2. 🎙️ Grill-Me — Matt Pocock (AI Hero)
- **Origem / Source:** [ihero.dev/skills-grill-me](https://www.aihero.dev/skills-grill-me) • [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me)
- **🇧🇷 Propósito:** Entrevista investigativa e implacável em rodadas estruturadas para resolver cada bifurcação do design antes de qualquer plano ser fixado.
- **🇺🇸 Purpose:** Relentless, round-by-round interview process that interrogates requirements and resolves open design decisions before planning starts.

---

## 3. 📦 Handoff — Matt Pocock (AI Hero)
- **Origem / Source:** [ihero.dev/skills-handoff](https://www.aihero.dev/skills-handoff) • [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff)
- **🇧🇷 Propósito:** Compacta e estrutura o estado atual de sessões longas de IA em documentos de Handoff limpos (sem duplicar histórico bruto), permitindo que um agente novo ou outra sessão retome o trabalho sem degradação de contexto. Salva decisões em .second-brain/handoffs/ e documentação de projeto.
- **🇺🇸 Purpose:** Summarizes context-heavy agent sessions into structured, lean handoff documents avoiding context window bloat and enabling seamless multi-agent continuity.

---

## 4. 🔴🟢🔵 Test-Driven Development (TDD) — Matt Pocock (AI Hero)
- **Origem / Source:** [ihero.dev/skills-tdd](https://www.aihero.dev/skills-tdd) • [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/reference/tdd)
- **🇧🇷 Propósito:** Impõe o ciclo rigoroso Red-Green-Refactor:
  - **Red:** Escrever primeiro o teste que falha antes de codificar a funcionalidade.
  - **Green:** Implementar a lógica mínima necessária estritamente para aprovar o teste.
  - **Refactor:** Limpar código, otimizar tipagem e aplicar design patterns sob cobertura garantida.
- **🇺🇸 Purpose:** Mandates the strict Red-Green-Refactor loop, preventing AI agents from generating brittle, untested code or skipping automated verification.
