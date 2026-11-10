# Django 6.1 & Bootstrap UX/UI Plus Integration Guide 🐍🎨
# Guia de Integração do Django com Bootstrap UX/UI Plus

> *Módulo Integrado para `python-dev-expert` e `bootstrap-ux-ui-plus`*  
> **Arquitetura de Referência:** Mazer & AdminKit Standards • Leis do UX • Acessibilidade WCAG 2.2 AA • Daltonismo  
> **Versões Alvo:** Django 5.x / 6.1+ • Bootstrap v5.3 & v6.0 • Python 3.10 a 3.16+

---

## 🇺🇸 English

### 1. Integration Objective
Bridge Django's robust Model-View-Template (MVT) architecture with the design and usability engineering provided by **`bootstrap-ux-ui-plus`**:
- **Light Theme by Default (`data-bs-theme="light"`):** Ensures maximum daylight readability and adheres to corporate dashboard standards.
- **Cognitive UX & 18 Laws of UX:** Layouts designed with Hick's Law, Fitts's Law (44px+ touch targets), Miller's Chunking (metric cards), and Doherty Threshold (<400ms loading feedback).
- **Inclusivity & Visual Accessibility:** Multi-channel status signaling (color + icon + text) preventing errors for colorblind users (Protanopia, Deuteranopia, Tritanopia, Achromatopsia).
- **Official Typography & Default Palette (#90271):** Seamless integration of Google Sans typography (`Google Sans Flex`, `Google Sans`, `Google Sans Code`) and balanced blues (`#869dcc`, `#5772ac`, `#3b5998`, `#224389`, `#14306b`).

### 2. Project Setup & Package Installation
```bash
pip install django django-crispy-forms crispy-bootstrap5
```

In `settings.py`:
```python
INSTALLED_APPS = [
    # Django apps...
    'crispy_forms',
    'crispy_bootstrap5',
    'meu_app',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
```

### 3. Canonical Base Template: `templates/base.html`
```html
{% load static %}
<!DOCTYPE html>
<html lang="pt-BR" data-bs-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}Django AdminPro{% endblock %}</title>

  <!-- Google Sans Official Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Google+Sans+Code:wght@400;600&family=Google+Sans+Flex:opsz,wght@9..144,400;500;600;700;800&family=Google+Sans:wght@400;500;700&display=swap" rel="stylesheet">

  <!-- Bootstrap 5.3 & Bootstrap Icons -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">

  <style>
    :root {
      /* Paleta Corporativa #90271 */
      --ux-primary: #224389;
      --ux-primary-hover: #14306b;
      --bs-primary: #224389;
      --bs-primary-rgb: 34, 67, 137;

      --ux-font-headings: 'Google Sans Flex', -apple-system, sans-serif;
      --ux-font-body: 'Google Sans', -apple-system, sans-serif;
      --ux-font-mono: 'Google Sans Code', monospace;
      --sidebar-width: 260px;
    }
    body {
      font-family: var(--ux-font-body);
      background-color: var(--bs-body-bg);
      color: var(--bs-body-color);
      min-height: 100vh;
    }
    h1, h2, h3, h4, h5, h6, .h1, .h2, .h3, .h4, .navbar-brand {
      font-family: var(--ux-font-headings);
      font-weight: 700;
      color: var(--bs-heading-color, inherit);
    }
    .btn-touch-target {
      min-height: 44px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }
    .focus-ring-accessible:focus-visible {
      outline: 3px solid #f5a623 !important;
      outline-offset: 2px !important;
      box-shadow: 0 0 0 2px #14306b !important;
    }
    /* Dark Mode Luminance Adjustments (Strictly Opt-in) */
    [data-bs-theme="dark"] {
      --bs-primary: #869dcc;
      --bs-heading-color: #f8fafc;
    }
  </style>
  {% block extra_head %}{% endblock %}
</head>
<body class="d-flex">

  <!-- Sidebar Lateral Estilo Mazer / AdminKit -->
  <aside class="sidebar bg-body-tertiary d-flex flex-column p-3 position-sticky top-0" style="width: var(--sidebar-width); min-height: 100vh;" aria-label="Navegação Principal">
    <a href="{% url 'dashboard' %}" class="d-flex align-items-center mb-3 text-decoration-none text-body">
      <i class="bi bi-bootstrap-fill text-primary fs-3 me-2" aria-hidden="true"></i>
      <span class="fs-5 fw-bold">DjangoPro</span>
    </a>
    <hr class="text-secondary opacity-25">
    <ul class="nav nav-pills flex-column mb-auto gap-1">
      <li class="nav-item">
        <a href="{% url 'dashboard' %}" class="nav-link active d-flex align-items-center py-2" aria-current="page">
          <i class="bi bi-speedometer2 me-2 fs-5" aria-hidden="true"></i>
          Dashboard
        </a>
      </li>
      <li>
        <a href="{% url 'clientes_list' %}" class="nav-link text-body d-flex align-items-center py-2">
          <i class="bi bi-people me-2 fs-5" aria-hidden="true"></i>
          Clientes
        </a>
      </li>
    </ul>
    <hr class="text-secondary opacity-25">
    <!-- Perfil do Usuário Django -->
    <div class="dropdown">
      <a href="#" class="d-flex align-items-center text-body text-decoration-none dropdown-toggle p-2 rounded btn-touch-target" data-bs-toggle="dropdown">
        <div class="rounded-circle bg-primary text-white p-2 me-2"><i class="bi bi-person-fill"></i></div>
        <strong>{{ request.user.username|default:"Operador" }}</strong>
      </a>
      <ul class="dropdown-menu shadow border">
        <li><a class="dropdown-item" href="{% url 'admin:index' %}">Django Admin</a></li>
        <li><hr class="dropdown-divider"></li>
        <li><a class="dropdown-item text-danger" href="{% url 'logout' %}">Sair</a></li>
      </ul>
    </div>
  </aside>

  <!-- Área de Conteúdo -->
  <main class="flex-grow-1 d-flex flex-column">
    <header class="navbar navbar-expand bg-body border-bottom px-4 py-2 sticky-top">
      <div class="container-fluid p-0">
        <h2 class="h5 mb-0 fw-bold">{% block page_title %}Visão Geral{% endblock %}</h2>
        <div class="d-flex align-items-center gap-2 ms-auto">
          <!-- Acessibilidade / Alternador Noturno (Opcional) -->
          <button class="btn btn-outline-secondary border-0 btn-touch-target" id="btnThemeToggle" aria-label="Alternar Tema Noturno">
            <i class="bi bi-sun-fill" id="themeIcon"></i>
          </button>
        </div>
      </div>
    </header>

    <div class="p-4">
      <!-- Mensagens Flash do Django (Feedback Acessível) -->
      {% if messages %}
        {% for message in messages %}
          <div class="alert alert-{{ message.tags }} alert-dismissible fade show d-flex align-items-center gap-2 shadow-sm rounded-3" role="alert">
            <i class="bi {% if message.tags == 'success' %}bi-check-circle-fill text-success{% else %}bi-exclamation-triangle-fill text-danger{% endif %} fs-5" aria-hidden="true"></i>
            <div>{{ message }}</div>
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Fechar"></button>
          </div>
        {% endfor %}
      {% endif %}

      {% block content %}{% endblock %}
    </div>
  </main>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script>
    const btnToggle = document.getElementById('btnThemeToggle');
    const themeIcon = document.getElementById('themeIcon');
    btnToggle?.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-bs-theme') || 'light';
      const target = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-bs-theme', target);
      themeIcon.className = target === 'dark' ? 'bi bi-moon-stars-fill' : 'bi bi-sun-fill';
    });
  </script>
</body>
</html>
```

### 4. Formulários Elegantes e Acessíveis (`forms.py` com Crispy)
```python
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'status']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Mariana Silva'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'mariana@empresa.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(11) 99999-9999'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }
```

No template do formulário:
```html
{% extends 'base.html' %}
{% load crispy_forms_tags %}

{% block content %}
<div class="card border-0 shadow-sm rounded-3 p-4">
  <h3 class="h4 fw-bold mb-3">Cadastrar Novo Cliente</h3>
  <form method="post" novalidate>
    {% csrf_token %}
    {{ form|crispy }}
    <div class="d-flex gap-2 mt-4">
      <button type="submit" class="btn btn-primary btn-touch-target px-4 shadow-sm text-white">
        <i class="bi bi-check-lg me-2"></i>Salvar Registro
      </button>
      <a href="{% url 'clientes_list' %}" class="btn btn-outline-secondary btn-touch-target px-3">
        Cancelar
      </a>
    </div>
  </form>
</div>
{% endblock %}
```

---

## 🇧🇷 Português (Brasil)

### 📌 Princípios da Integração Django + Bootstrap UX/UI Plus
Ao construir aplicações web com Django utilizando esta skill:
1. **Tema Claro Obrigatório por Padrão:** Toda interface herda `data-bs-theme="light"`. O tema noturno só deve ser disponibilizado como opção secundária ativada a pedido do usuário.
2. **Paleta Padrão Calibrada (#90271):** Uso coerente dos tons azuis `#869dcc`, `#5772ac`, `#3b5998`, `#224389` e `#14306b`.
3. **Tipografia Google Sans:** Títulos em `Google Sans Flex`, texto corrido em `Google Sans` e snippets/código em `Google Sans Code`.
4. **Validação e Acessibilidade para Daltônicos:**
   - Mensagens de erro e formulários no Django **nunca dependem apenas de cores** (sempre acompanhadas de ícones `bi-exclamation-circle-fill` e texto explicativo).
   - Botões e campos interativos respeitam o alvo de toque de no mínimo 44px (Lei de Fitts).
5. **Auditoria Integrada:** Você pode rodar o auditor da skill diretamente sobre seus templates do Django:
   ```bash
   node ../bootstrap-ux-ui-plus/scripts/audit_ux_bootstrap.mjs templates/base.html
   ```

