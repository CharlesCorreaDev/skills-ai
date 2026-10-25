# Guia de Bootstrap Prefixado e UI/UX Responsiva para Foundry VTT 🎨

## 1. Princípio Fundamental: Prefixo Obrigatório em TODAS as Classes
No Foundry VTT, múltiplos módulos, sistemas e a própria interface do Core (`ApplicationV2`, menus de configuração, sidebar) compartilham o mesmo DOM global.
> [!CRITICAL]
> **NUNCA injete classes puras do Bootstrap (como `.btn`, `.btn-primary`, `.card`, `.modal`, `.row`, `.col-12`) diretamente no Foundry VTT.** Isso quebra a interface do Core e colide com outros módulos.
> **TODAS as classes e variáveis do Bootstrap DEVEM receber o prefixo exclusivo do sistema ou módulo.**

### Exemplos de Nomenclatura com Prefixo:
- Se o sistema for **Year Zero Engine** (`year-zero-engine` / `yze`):
  - `.btn` ➔ `.yze-btn`
  - `.btn-primary` ➔ `.yze-btn-primary`
  - `.card` ➔ `.yze-card`
  - `.row` ➔ `.yze-row`
  - `.col-md-6` ➔ `.yze-col-md-6`
  - `.table` ➔ `.yze-table`
  - `.form-control` ➔ `.yze-form-control`
- Se for um módulo de armadilhas customizado (`dungeon-traps` / `dt`):
  - `.btn-danger` ➔ `.dt-btn-danger`
  - `.badge` ➔ `.dt-badge`

---

## 2. Gate Obrigatório: Solicitação da Paleta de Cores ao Usuário
Antes de desenvolver qualquer folha de personagem, diálogo, menu ou HUD:
1. **O Agente DEVE pedir ao usuário:**
   - **3 cores principais:** Cor Primária (base), Cor Secundária (apoio) e Cor de Fundo / Superfície.
   - **3 cores de destaque (accent):** Tons harmônicos ou contrastantes para botões de ação, alertas/danos, e estados ativos/sucessos.
2. **Customização via Sass / SCSS:**
   Utilize Sass para definir as variáveis do tema com o prefixo do projeto:
   ```scss
   // Exemplo: assets/styles/yze-variables.scss
   $yze-prefix: "yze-";

   $yze-primary: #8b0000;    // Ex: Vermelho escuro pós-apocalíptico
   $yze-secondary: #2b2b2b;  // Chumbo / metal desgastado
   $yze-background: #121214; // Fundo escuro imersivo
   
   $yze-accent-1: #e28743;   // Destaque âmbar (sucessos)
   $yze-accent-2: #c0392b;   // Destaque dano/trauma
   $yze-accent-3: #27ae60;   // Destaque cura/suprimento

   // Mapeamento para variáveis CSS escopadas
   .yze-app {
     --#{$yze-prefix}primary: #{$yze-primary};
     --#{$yze-prefix}secondary: #{$yze-secondary};
     --#{$yze-prefix}bg: #{$yze-background};
     --#{$yze-prefix}accent-1: #{$yze-accent-1};
     --#{$yze-prefix}accent-2: #{$yze-accent-2};
     --#{$yze-prefix}accent-3: #{$yze-accent-3};
   }
   ```

---

## 3. Compilação e Geração de CSS com Prefixo
Para compilar o Bootstrap com prefixo customizado, use Sass e a diretiva `$prefix`:
```scss
// custom-bootstrap.scss
$prefix: "yze-"; // Altera automaticamente o prefixo do Bootstrap 5.3+

@import "bootstrap/scss/functions";
@import "bootstrap/scss/variables";
@import "bootstrap/scss/variables-dark";
@import "bootstrap/scss/maps";
@import "bootstrap/scss/mixins";
@import "bootstrap/scss/utilities";

// Seletor raiz para isolamento
.yze-sheet {
  @import "bootstrap/scss/root";
  @import "bootstrap/scss/reboot";
  @import "bootstrap/scss/type";
  @import "bootstrap/scss/containers";
  @import "bootstrap/scss/grid";
  @import "bootstrap/scss/tables";
  @import "bootstrap/scss/forms";
  @import "bootstrap/scss/buttons";
  @import "bootstrap/scss/transitions";
  @import "bootstrap/scss/dropdown";
  @import "bootstrap/scss/button-group";
  @import "bootstrap/scss/nav";
  @import "bootstrap/scss/navbar";
  @import "bootstrap/scss/card";
  @import "bootstrap/scss/badge";
  @import "bootstrap/scss/alert";
  @import "bootstrap/scss/progress";
  @import "bootstrap/scss/close";
  @import "bootstrap/scss/toasts";
  @import "bootstrap/scss/modal";
  @import "bootstrap/scss/tooltip";
  @import "bootstrap/scss/popover";
  @import "bootstrap/scss/utilities/api";
}
```

---

## 4. Plugins e Componentes Recomendados para Foundry VTT
Estes plugins testados e validados melhoram a ergonomia de fichas e diálogos:

| Categoria | Plugin | Link | Uso Recomendado em Foundry |
|---|---|---|---|
| **Layout & Altura** | `jquery-match-height` | [liabru/jquery-match-height](https://github.com/liabru/jquery-match-height) | Alinhamento de cards de armas, magias e inventário em grid. |
| **Diálogos Modernos** | `use-bootstrap-dialog` | [use-bootstrap/use-bootstrap-dialog](https://github.com/use-bootstrap/use-bootstrap-dialog) | Modais de confirmação, testes de atributo e rolagem customizada. |
| **Progresso Circular** | `jquery-bs-circle-progress`| [ThomasDev-de/jquery-bs-circle-progress](https://github.com/ThomasDev-de/jquery-bs-circle-progress) | Círculos de HP, Mana, Sobrecarga, Stress e Estamina. |
| **Wizards & Criação** | `bootstrap-form-wizard` | [xonipatino/bootstrap-form-wizard](https://github.com/xonipatino/bootstrap-form-wizard) | Assistentes passo-a-passo de criação de personagem ou sessão zero. |
| **Notificações** | `bootstrap5-notify` / `toast`| [chrisgo/bootstrap5-toast](https://github.com/chrisgo/bootstrap5-toast) | Notificações visuais de iniciativa, danos e itens adquiridos. |
| **Selects & Tags** | `dselect` / `bootstrap-select`| [jarstone/dselect](https://github.com/jarstone/dselect) | Seleção de perícias, talentos e filtros com busca integrada. |
| **Abas Verticais** | `bootstrap-5-vertical-tabs` | [tromgy/bootstrap-5-vertical-tabs](https://github.com/tromgy/bootstrap-5-vertical-tabs) | Navegação lateral em fichas complexas (Bio, Stats, Inventário, Magias). |
| **Tabelas de Dados** | `bootstrap-table` | [wenzhixin/bootstrap-table](https://github.com/wenzhixin/bootstrap-table) | Listagens dinâmicas de equipamentos com ordenação e paginação. |
| **Árvore Hierárquica**| `bs5treeview` | [nhmvienna/bs5treeview](https://github.com/nhmvienna/bs5treeview) | Árvores genealógicas, facções, compêndios e hierarquia de talentos. |
| **Avatares** | `bootstrap-avatar` | [ghoststead/bootstrap-avatar](https://github.com/ghoststead/bootstrap-avatar) | Retratos circulares de personagens e tokens na ficha. |

---

## 5. Recursos de Design e Templates para Inspiração
- **Documentação Oficial:** [Bootstrap Docs](https://getbootstrap.com/docs/6.0/)
- **Templates e UI Kits:**
  - [UIdeck App Templates](https://uideck.com/app-templates?filter=bootstrap)
  - [BootstrapMade Free Templates](https://bootstrapmade.com/)
  - [ThemeWagon Bootstrap 5 Themes](https://themewagon.com/theme-price/free/?swoof=1&pa_frameworks=bootstrap-5)
  - [Bootstrap 5 Design Resources](https://github.com/jqueryscript/Bootstrap-5-Design-Resources)
