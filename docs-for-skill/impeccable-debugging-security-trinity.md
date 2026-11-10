# Impeccable Design, Systematic Debugging & Trail of Bits Security Trinity 🏛️🛡️🔬
# Tríade Canônica: Design Impecável, Depuração Sistemática e Segurança Trail of Bits

> *Módulo Canônico Integrado para as Skills:*  
> `book-formatter` • `bootstrap-ux-ui-plus` • `master-of-foundryvtt` • `php-dev-expert` • `python-dev-expert`  
> **Fontes & Referências SOTA:**  
> - **Impeccable** (Paul Bakaus / `pbakaus/impeccable`): Anti-slop visual, vocabulário tipográfico rigoroso e design intencional.  
> - **Systematic Debugging** (`systematic-debugging`): Hipótese científica, isolamento de falha e testes de regressão antes do patch.  
> - **Trail of Bits Security Skills** (`trail-of-bits-security-skills`): Análise estática profunda (Semgrep/CodeQL), sanitização de inputs e mitigação OWASP Top 10.

---

## 🎨 1. Impeccable Design (Paul Bakaus / Anti-Slop Visual)

Aplica-se ao desenvolvimento de interfaces em **Bootstrap**, diagramação de livros em **Book Formatter** e fichas/telas do **Foundry VTT**:

### 🚫 Anti-Patterns Visuais Proibidos (Eliminando "AI Slop"):
1. **Cards dentro de Cards Infinitos:** Proibido aninhar contêineres `.card` dentro de `.card` sem necessidade de agrupamento semântico. Use espaçamento (`gap`, `margin`) e divisores sutis em vez de bordas acumuladas.
2. **Gradientes Roxos/Azuis Genéricos:** Evite paletas clichês não intencionais. Utilize a paleta corporativa calibrada `#90271` ou paletas contextuais estritas do sistema/marca.
3. **Tipografia Monótona:** Títulos em `Google Sans Flex` com contraste claro de peso (`font-weight: 700`), corpo de texto em `Google Sans` (`line-height: 1.6`) e código em `Google Sans Code`.
4. **Espaçamento e Ritmo:** Use escala modular de 8px (Bootstrap `$spacer` de 0.25rem a 3rem) para consistência visual.

---

## 🔬 2. Systematic Debugging (Depuração Científica sem Tentativa e Erro)

Aplica-se a bugs, erros de execução, falhas de testes e exceções em **todas as skills**:

### 🛑 Regra Fundamental: Proibido "Chutar" Correções
Nunca proponha um patch ou altere código às cegas na esperança de que funcione.

### O Ciclo em 4 Etapas:
1. **Observar & Mapear (Trace):** Inspecione o stack trace completo, variáveis locais e o ponto exato da fronteira de falha.
2. **Formular Hipótese Causal:** Declare explicitamente qual é a causa raiz física (ex: `Null pointer`, `incompatibilidade de tipo`, `condição de corrida`).
3. **Isolamento Mínimo Reproduzível:** Escreva um teste automatizado ou script isolado que reproduza a falha com 100% de consistência.
4. **Correção Cirúrgica & Validação:** Aplique a menor alteração suficiente no local correto e confirme que o teste de reprodução agora passa e nenhum efeito colateral ocorreu.

---

## 🛡️ 3. Trail of Bits Security Skills (Blindagem de Código & SAST)

Aplica-se a código backend, APIs, scripts e integrações em **PHP, Python e JavaScript**:

### Princípios de Segurança em Profundidade:
1. **Sanitização de Fronteiras:** Todos os dados externos (inputs de usuário, arquivos enviados, parâmetros de URL, cabeçalhos HTTP, websockets) são tratados como hostis e validados por esquemas estritos (`pydantic` em Python, DTOs tipados em PHP, validação de schema em JS).
2. **Prevenção OWASP Top 10:**
   - **Injeções (SQL, Command, Path Traversal):** Consultas preparadas obrigatórias (PDO / Django ORM), proibição de `shell=True` ou chamadas cruas sem whitelist.
   - **Controle de Acesso Quebrado:** Checagem de permissões em nível de objeto e sessão antes de qualquer mutação.
   - **Falhas Criptográficas:** Uso de algoritmos modernos (`Argon2id`, `bcrypt`, AES-GCM) e segredos guardados fora do código.
3. **Auditoria SAST Pré-Commit:**
   - Python: `bandit`, `pip-audit`, regras personalizadas do `Semgrep`.
   - PHP: `psalm --taint-analysis`, `phpstan`, `composer audit`.
   - JS/Node: `npm audit`, `eslint-plugin-security`.

