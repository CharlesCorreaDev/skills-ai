# Cheatsheet: Bootstrap UX/UI Plus ⚡🎨

Guia rápido de referência para implementar as Leis de UX e padrões do Bootstrap (v5.3 e v6.0) em qualquer linguagem (HTML, PHP, Node.js, React, Python, Django, Java).

---

## 1. Mapeamento Rápido: Leis de UX vs Classes Bootstrap

| Lei de UX | Problema Humano | Solução Bootstrap | Classes e Utilitários |
|---|---|---|---|
| **Lei de Hick** | Paralisia por excesso de opções | Destaque da ação primária, progressive disclosure | `.btn-primary` (primária) vs `.btn-outline-secondary`, `.accordion`, `.collapse`, `.nav-tabs` |
| **Lei de Fitts** | Dificuldade de clicar em telas touch/mouse | Alvos de toque grandes (44px+), cards clicáveis | `.btn-lg`, `.py-2`, `.py-3`, `.stretched-link`, `.form-check-label` |
| **Lei de Jakob** | Desconforto com layouts não convencionais | Navegação e layouts familiares com busca no topo | `.navbar`, `.navbar-brand`, `.breadcrumb`, `.pagination`, `.dropdown-menu` |
| **Efeito Zeigarnik** | Abandono de cadastros e tarefas longas | Indicadores visuais de tarefas em andamento | `.progress`, `.progress-bar`, `.badge bg-success-subtle` |
| **Lei de Miller** | Sobrecarga de memória de trabalho (7±2 itens) | Agrupamento em blocos digeríveis (Chunking) | `.card`, `.shadow-sm`, `.border-0`, `.row .g-3`, `.list-group` |
| **Efeito Posição Serial** | Esquecimento de itens intermediários | Ações críticas nos extremos (primeiro e último) | Primeiro item da navbar e botão de conversão à extrema direita |

---

## 2. Padrões de Cor e Contraste Sutil (Bootstrap 5.3 & 6.0)

Substitua alertas e badges pesados pelas novas variáveis com alto contraste e elegância:

```html
<!-- Sucesso Sutil -->
<span class="badge bg-success-subtle text-success-emphasis border border-success-subtle rounded-pill px-3 py-2">
  Ativo
</span>

<!-- Alerta de Atenção Sutil -->
<span class="badge bg-warning-subtle text-warning-emphasis border border-warning-subtle rounded-pill px-3 py-2">
  Pendente
</span>

<!-- Erro Crítico Sutil -->
<span class="badge bg-danger-subtle text-danger-emphasis border border-danger-subtle rounded-pill px-3 py-2">
  Cancelado
</span>
```

---

## 3. Checklist Rápido de Acessibilidade (WCAG 2.2 AA)
- [ ] Todo botão que contém apenas ícone possui `aria-label="Descrição da ação"`.
- [ ] Todos os campos de formulário têm `<label for="idDoCampo">` associado.
- [ ] Modais contêm `role="dialog"`, `aria-modal="true"` e `aria-labelledby="tituloModal"`.
- [ ] Anéis de foco (`.focus-ring`) estão preservados em todos os elementos interativos.
- [ ] Imagens contêm atributo `alt="..."` descritivo.
