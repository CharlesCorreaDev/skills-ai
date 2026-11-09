# Bootstrap UX/UI Plus 🎨⚡

> **Cognitive UX Laws, Nielsen Usability Heuristics & WCAG 2.2 AA for Bootstrap (v5.3 & v6.0)**  
> *Engenharia Cognitiva de Usabilidade, Leis de UX e Acessibilidade para Bootstrap por GM Charles Corrêa*  
> **Status: Beta (v0.1.0-beta)**

---

## 🇺🇸 English

### 📌 Overview
**Bootstrap UX/UI Plus** bridges the scientific laws of human-computer interaction (HCI), Jakob Nielsen's usability principles, and accessibility standards (WCAG 2.2 AA) directly into **Bootstrap (v5.3 & v6.0)** front-end development. 

Whether building corporate administrative panels, SaaS dashboards, or high-conversion landing pages, this skill provides production-grade components, layouts, and automation tools across **HTML, PHP, Node.js, React, Python/Django, and Java**.

### 🌟 Core Highlights
- **The 18 Essential Laws of UX:** Concrete implementation of all 18 laws (Hick, Fitts, Jakob, Proximity, Similarity, Common Region, Uniform Connectedness, Miller, Doherty Threshold, Von Restorff, Serial Position, Peak-End, Zeigarnik, Prägnanz, Tesler, Postel, Parkinson, Occam's Razor & Pareto).
- **Nielsen's 10 Heuristics:** Actionable guidance for system feedback, user freedom (Undo), error recovery, and clean typography.
- **AccessLint & WCAG 2.2 AA:** Zero-compromise accessibility with keyboard focus rings (`.focus-ring`), ARIA labels, and touch targets (44px+).
- **Mazer & AdminKit Architectures:** Production-ready dashboard structures modeled directly after [zuramai/mazer](https://github.com/zuramai/mazer) and [adminkit/adminkit](https://github.com/adminkit/adminkit).
- **Dark Mode Ready:** Built-in dynamic theme management using Bootstrap 5.3+ `data-bs-theme="auto"`.
- **Integrated Audit Engine:** Run `node scripts/audit_ux_bootstrap.mjs <file>` to automatically lint and detect accessibility/UX violations.

### 🚀 Quick Start
```bash
# Run UX & Accessibility linter on any HTML/PHP/JSX file:
node bootstrap-ux-ui-plus/scripts/audit_ux_bootstrap.mjs path/to/your-page.html
```

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral
O **Bootstrap UX/UI Plus** une as leis da psicologia cognitiva (Laws of UX), as heurísticas consagradas de Jakob Nielsen e as diretrizes internacionais de acessibilidade (WCAG 2.2 AA) ao poder do **Bootstrap (v5.3 e v6.0)**.

Projetada para desenvolvedores e arquitetos de software criarem interfaces elegantes, intuitivas e acessíveis para portais, dashboards analíticos e sistemas de gestão em **HTML, PHP, Node.js, React, Python/Django e Java**.

### 🌟 Destaques Principais
- **As 18 Leis Canônicas do UX:** Aplicação prática de todas as 18 leis (Hick, Fitts, Jakob, Proximidade, Semelhança, Região Comum, Conectividade Uniforme, Miller, Limiar de Doherty <400ms, Von Restorff, Posição Serial, Pico-Fim, Zeigarnik, Prägnanz, Tesler, Postel, Parkinson, Navalha de Occam e Pareto 80/20).
- **10 Heurísticas de Nielsen:** Componentes com feedback imediato de status, proteção contra erros destrutivos com modais de confirmação e linguagem humana.
- **Acessibilidade WCAG 2.2 Nível AA:** Navegação completa por teclado com `.focus-ring`, rótulos ARIA em botões de ação e contraste de cores aprimorado com tokens sutis (`.bg-*-subtle`).
- **Arquiteturas de Referência Mazer & AdminKit:** Estruturas canônicas completas para painéis e administrações espelhadas em [zuramai/mazer](https://github.com/zuramai/mazer) e [adminkit/adminkit](https://github.com/adminkit/adminkit).
- **Suporte Nativo a Modo Escuro:** Gerenciamento dinâmico de tema com o seletor `data-bs-theme`.
- **Auditor de Qualidade Integrado:** Script CLI nativo para validar templates e páginas antes da entrega.

### 🚀 Exemplo de Uso do Auditor CLI
```bash
# Executar a auditoria de UX e Acessibilidade em um template:
node bootstrap-ux-ui-plus/scripts/audit_ux_bootstrap.mjs bootstrap-ux-ui-plus/templates/admin-dashboard-template.html
```

---

## 📁 Estrutura de Arquivos / Folder Structure

```
bootstrap-ux-ui-plus/
├── SKILL.md                          # Diretrizes e mandatos mestres para agentes de IA
├── README.md                         # Visão geral completa bilíngue (EN / PT-BR)
├── VERSION                           # Versão semântica atual (0.1.0-beta)
├── CHANGELOG.md                      # Histórico detalhado de versões
├── cheatsheet.md                     # Guia rápido de classes e Leis de UX
├── glossary.md                       # Dicionário de termos técnicos de UX e UI
├── patterns.md                       # Padrões de arquitetura multi-linguagem
├── laws/
│   └── laws-of-ux-bootstrap.md       # Tradução técnica das Leis do UX para Bootstrap
├── heuristics/
│   └── nielsen-heuristics-bootstrap.md # 10 Heurísticas de Nielsen aplicadas
├── accessibility/
│   └── a11y-wcag-guidelines.md       # Diretrizes WCAG 2.2 AA & AccessLint
├── templates/
│   └── admin-dashboard-template.html # Dashboard administrativo completo responsivo
└── scripts/
    └── audit_ux_bootstrap.mjs        # Motor CLI de auditoria e validação de código
```

---

## 👨‍💻 Autor / Author
**GM Charles Corrêa**  
- 🌐 Website: [charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 GitHub: [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ Skills AI: [github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)
