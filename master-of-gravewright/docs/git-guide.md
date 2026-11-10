# Guia de Controle de Versão Git para Módulos e Sistemas Gravewright VTT

O desenvolvimento de módulos, temas, sistemas de RPG e pacotes de tradução para o **Gravewright VTT** segue o modelo canônico de repositórios Git, versionamento semântico (SemVer) e lançamentos com tags assinadas no GitHub.

---

## 🛠️ Skills Recomendadas para Git & GitHub
- **Git Workflows & Best Practices:** `git-pr-workflows` / `openclaw-github-repo-commander`.
- **Auditoria Pré-Push:** `codebase-audit-pre-push`.
- **Instalação via npx skills:**
  ```bash
  npx skills@latest add github
  ```

---

## 📦 Padrões de Repositório para Módulos Gravewright

Um repositório de módulo ou extensão do Gravewright deve possuir a seguinte organização na raiz:

```
meu-modulo-gravewright/
├── manifest.json              # Metadados obrigatórios do pacote
├── index.js                   # Entrypoint JavaScript (se módulo de browser)
├── style.css                  # Estilos com namespace CSS isolado
├── README.md                  # Documentação bilíngue de instalação e uso
├── CHANGELOG.md               # Histórico detalhado de alterações
├── LICENSE                    # Licença do módulo (MIT / Apache 2.0 / etc)
└── .gitignore                 # Arquivos ignorados
```

### Arquivo `.gitignore` Recomendado:
```gitignore
# Python / Django
__pycache__/
*.py[cod]
*$py.class
*.sqlite3
db.sqlite3
/data/
/media/
.env

# Astral uv
.venv/
uv.lock

# Node.js
node_modules/
dist/

# OS / IDE
.DS_Store
Thumbs.db
.vscode/
.idea/
```

---

## 🏷️ Fluxo de Versionamento e Releases no GitHub

1. Atualize a versão no `manifest.json`:
   ```json
   {
     "version": "0.2.0"
   }
   ```
2. Commit e criação de tag no formato `v<versao>`:
   ```bash
   git add .
   git commit -m "feat: adicionar suporte a clocks de investigação"
   git tag -a v0.2.0 -m "Release v0.2.0: Suporte a Clocks"
   git push origin main --tags
   ```
3. Gere o arquivo ZIP de distribuição para o Marketplace do Gravewright:
   ```bash
   git archive -o meu-modulo-v0.2.0.zip HEAD
   ```
