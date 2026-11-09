# Leis Fundamentais do UX para Bootstrap / Fundamental Laws of UX for Bootstrap 🧠📐

Este guia traduz as leis clássicas e psicológicas do UX (Laws of UX, Hick, Fitts, Jakob, Zeigarnik, Miller, etc.) em padrões acionáveis de componentes, grids e utilitários do **Bootstrap (v5.3 e v6.0)**.

---

## 1. Lei de Hick (Hick's Law) ⏳
> *O tempo que leva para tomar uma decisão aumenta logaritmicamente com o número e a complexidade das escolhas.*  
> *The time it takes to make a decision increases with the number and complexity of choices: $T = b \cdot \log_2(n + 1)$*

### 🎯 Aplicação no Bootstrap:
- **Redução de Carga Cognitiva:**
  - Em vez de um formulário longo com 20 campos visíveis, use **Progressive Disclosure** (acordeões `accordion`, abas `nav-tabs` ou wizards passo-a-passo).
  - Em menus dropdown (`dropdown-menu`), limite a 5 a 7 opções principais. Se houver mais, agrupe com `dropdown-header` e `dropdown-divider`.
  - Destaque a **Ação Primária** com `.btn-primary` e utilize `.btn-outline-secondary` ou `.btn-link` para ações secundárias ou de cancelamento.

### 💻 Exemplo Bootstrap:
```html
<!-- Ruim: 4 botões com o mesmo peso visual gerando paralisia de escolha -->
<!-- Bom: Ação primária destacada e opções secundárias agrupadas -->
<div class="d-flex align-items-center gap-2">
  <button type="submit" class="btn btn-primary px-4 fw-semibold">
    Salvar e Continuar
  </button>
  <button type="button" class="btn btn-outline-secondary">
    Salvar Rascunho
  </button>
  <button type="button" class="btn btn-link text-muted ms-auto">
    Cancelar
  </button>
</div>
```

---

## 2. Lei de Fitts (Fitts's Law) 🎯
> *O tempo necessário para alcançar um alvo é uma função da distância até o alvo e do tamanho dele.*  
> *The time to acquire a target is a function of the distance to and size of the target.*

### 🎯 Aplicação no Bootstrap:
- **Área de Toque Confortável (Touch Targets):**
  - Alvos interativos em mobile devem ter no mínimo **44x44px** ou **48x48px**.
  - No Bootstrap, use botões maiores para ações chave: `.btn-lg`, padding vertical `.py-2` ou `.py-3`, e utilitários de clique expandido `.stretched-link` em cards inteiros.
- **Posicionamento Próximo ao Cursor / Polegar:**
  - Em interfaces mobile, coloque botões críticos na zona inferior (bottom bar fixa com `.fixed-bottom`).
  - Em formulários, use rótulos clicáveis associados ao `id` do input (`<label for="...">`) e `.form-check-label` com área de clique ampla.

### 💻 Exemplo Bootstrap:
```html
<!-- Card inteiro clicável através de .stretched-link -->
<div class="card shadow-sm h-100 position-relative border-0 rounded-3">
  <div class="card-body p-4">
    <div class="badge bg-primary-subtle text-primary mb-2">Relatório</div>
    <h5 class="card-title fw-bold">Performance de Vendas</h5>
    <p class="card-text text-secondary">Acesse o comparativo mensal completo.</p>
    <a href="/relatorios/vendas" class="stretched-link text-decoration-none fw-medium">
      Ver detalhes &rarr;
    </a>
  </div>
</div>
```

---

## 3. Lei de Jakob (Jakob's Law) 🔄
> *Os usuários passam a maior parte do tempo em outros sites. Isso significa que eles preferem que seu site funcione da mesma maneira que todos os outros que já conhecem.*  
> *Users spend most of their time on other sites. This means they prefer your site to work the same way as all the other sites they already know.*

### 🎯 Aplicação no Bootstrap:
- **Convenções Familiares:**
  - O logotipo da marca fica no canto superior esquerdo da barra de navegação (`.navbar-brand`) e leva para a Home.
  - A busca fica no topo central ou à direita.
  - O avatar do perfil/usuário fica na extremidade direita do cabeçalho.
  - Ícones padronizados: lupa para pesquisa, sino para notificações, engrenagem para configurações, lixeira para exclusão.
  - Não tente reinventar controles nativos (como caixas de seleção, dropdowns e paginação). Utilize `.navbar`, `.form-select`, `.pagination` e `.breadcrumb`.

---

## 4. Efeito Zeigarnik (Zeigarnik Effect) ⏳
> *As pessoas se lembram de tarefas incompletas ou interrompidas com mais facilidade do que de tarefas concluídas.*  
> *People remember uncompleted or interrupted tasks better than completed tasks.*

### 🎯 Aplicação no Bootstrap:
- **Barras de Progresso e Indicadores de Conclusão:**
  - Em dashboards e fluxos de onboarding, utilize barras de progresso do Bootstrap (`.progress` e `.progress-bar`) com indicação de porcentagem (ex: "Perfil 70% completo").
  - Em wizards, use etapas numeradas para instigar o usuário a concluir a jornada.

### 💻 Exemplo Bootstrap:
```html
<div class="card border-0 shadow-sm p-4 rounded-3">
  <div class="d-flex justify-content-between align-items-center mb-2">
    <span class="fw-semibold">Configuração da Conta</span>
    <span class="badge bg-success-subtle text-success">3 de 4 etapas</span>
  </div>
  <div class="progress" style="height: 8px;">
    <div class="progress-bar bg-success" role="progressbar" style="width: 75%;" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100"></div>
  </div>
  <small class="text-muted mt-2">Falta apenas confirmar seu número de telefone!</small>
</div>
```

---

## 5. Lei de Miller (Miller's Law) 🔢
> *A pessoa média consegue manter apenas cerca de 7 (mais ou menos 2) itens em sua memória de trabalho.*  
> *The average person can only keep 7 (plus or minus 2) items in their working memory.*

### 🎯 Aplicação no Bootstrap:
- **Chunking (Agrupamento de Dados):**
  - Divida tabelas longas em grupos claros ou use `.card` particionados com títulos descritivos.
  - Formatação de dados: números de telefone, CPF, cartões de crédito divididos visualmente em blocos legíveis.
  - Filtros de busca: agrupar filtros relacionados em seções recolhíveis (`collapse`).

---

## 6. Efeito da Posição Serial (Serial Position Effect) 📊
> *Os usuários têm uma propensão a se lembrar melhor do primeiro e do último item em uma série.*  
> *Users have a penchant to best remember the first and last items in a series.*

### 🎯 Aplicação no Bootstrap:
- Na navegação (`.nav` ou `.navbar`), posicione o item mais crítico no início (primeiro item) e a ação de conversão principal no final (extrema direita).
- Em tabelas de planos e preços (`pricing cards`), posicione o plano mais popular no centro ou com destaque visual (`scale` ou borda destacada `.border-primary .shadow`).
