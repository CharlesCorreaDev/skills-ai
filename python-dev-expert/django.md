# Django 6.1 Reference

## 🌐 Arquitetura MVT (Model-View-Template)
O Django segue o padrão MVT, que é ligeiramente diferente do MVC tradicional.
- **Model**: Gerencia os dados e a lógica de negócios central (banco de dados via ORM).
- **View**: A lógica de controle. Processa a requisição HTTP e retorna a resposta HTTP.
- **Template**: A camada de apresentação (HTML/UI).

## 🚀 Novidades e Foco (Django 6.1)
*Nota: Versões recentes do Django ampliaram imensamente o suporte assíncrono.*
- **ORM Assíncrono Completo**: Métodos como `await Model.objects.aget(...)`, `afirst()`, `acount()` para queries sem bloquear o event loop.
- **Views Assíncronas**: Definição de views com `async def my_view(request):`.
- **Formulários e Validação**: Uso avançado do `ModelForm` com tipagem reforçada.
- **Segurança Nativa**: Proteções CSRF, Clickjacking e SQL Injection embutidas.

## 🛠️ Comandos Essenciais (Django Admin)
```bash
# Criar projeto
django-admin startproject meu_projeto .

# Criar app
python manage.py startapp meu_app

# Gerar migrações do banco de dados (após alterar models.py)
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Subir servidor de desenvolvimento
python manage.py runserver

# Criar superusuário (Admin)
python manage.py createsuperuser
```

## 🧩 Padrões Recomendados (Django)
1. **Fat Models, Skinny Views**: Mova a lógica de negócio pesada para métodos customizados no `Model` ou para o `ModelManager`, mantendo as views concisas.
2. **Class-Based Views (CBV)**: Use `ListView`, `DetailView`, etc., para padronizar e reduzir código repetitivo (Boilerplate).
3. **App Modularity**: Mantenha os apps (pastas criadas com `startapp`) focados em um único domínio funcional e de preferência desacoplados (pluggable).

---

## 🎨 Integração com Bootstrap UX/UI Plus
Para construir interfaces modernas, dashboards e painéis administrativos no Django:
- **Referência Canônica da Skill:** Adote os padrões definidos na skill [`bootstrap-ux-ui-plus`](../bootstrap-ux-ui-plus/SKILL.md) (arquiteturas Mazer e AdminKit, 18 Leis do UX, WCAG 2.2 AA e inclusão para daltônicos).
- **Tema Claro por Padrão:** Toda interface Django DEVE iniciar com `data-bs-theme="light"`. O tema escuro/noturno é estritamente opt-in sob pedido do usuário.
- **Paleta Padrão (#90271) & Fontes Google Sans:** Títulos em `Google Sans Flex`, texto em `Google Sans` e código em `Google Sans Code`, combinados com a paleta corporativa azul calibrada.
- **Crispy Forms com Bootstrap 5:** Use `crispy-bootstrap5` para renderizar formulários elegantes com mensagens de erro acessíveis (ícones + texto).
- Consulte o guia completo e templates prontos em [Guia Django + Bootstrap UX/UI Plus](django-bootstrap-guide.md).
