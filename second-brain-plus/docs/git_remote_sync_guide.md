# Git Remote Synchronization & Multi-Platform Integration 🐙🦊
> *GitHub CLI (`gh`), GitLab CLI (`glab`), Private vs. Public Vault Architecture & CI Automations*  
> **Status:** Official 2026 Reference | **Compatible with:** Antigravity, Claude Code, Cursor, Codex, Copilot CLI

---

## 🇺🇸 English

### 1. Architectural Philosophy: The Dual-Backup Model

While the **Notion API Hub** serves as the collaborative, relational, and visual dashboard for human interaction, **Git Remote Repositories** (GitHub and GitLab) serve as the **cryptographic, version-controlled, immutable code & decision backup**.

```
┌────────────────────────────────────────────────────────────────────────┐
│                        AI AGENT RUNTIME & LOCAL                        │
│   Local Markdown Vault (.second-brain/) + Git Commits (git add/commit) │
└──────────────────┬─────────────────────────────────┬───────────────────┘
                   │                                 │
                   ▼                                 ▼
   ┌───────────────────────────────┐ ┌─────────────────────────────────┐
   │       NOTION CLOUD HUB        │ │      GIT REMOTE REPOSITORIES    │
   │  (Notion API / CLI / Workers) │ │  GitHub (gh) & GitLab (glab)    │
   │  - Visual Kanban & Mobile     │ │  - Immutable Commit History     │
   │  - Relational Database Views  │ │  - Branch Versioning & Tags     │
   │  - Zero-Latency Blocks        │ │  - CI/CD Auditing & Scanners    │
   └───────────────────────────────┘ └─────────────────────────────────┘
```

---

### 2. Supported Git Command-Line Interfaces (CLIs)

#### A. GitHub CLI (`gh` / https://cli.github.com/)
- **Installation:**
  - Windows: `winget install GitHub.cli`
  - macOS: `brew install gh`
  - Linux: `sudo apt install gh`
- **Authentication & Diagnostics:**
  ```bash
  gh auth login
  gh auth status
  ```
- **Managing Second Brain Repositories:**
  ```bash
  # Check current repository metadata
  gh repo view --json isPrivate,nameWithOwner,defaultBranchRef

  # Create a dedicated PRIVATE repository for the second-brain vault
  gh repo create my-second-brain-vault --private --source=.second-brain --push
  ```

#### B. GitLab CLI (`glab` / https://docs.gitlab.com/cli/)
- **Installation:**
  - Windows: `winget install GLab.GLab`
  - macOS: `brew install glab`
  - Linux: `sudo apt install glab`
- **Authentication & Diagnostics:**
  ```bash
  glab auth login
  glab auth status
  ```
- **Managing Second Brain Repositories:**
  ```bash
  # Check repository status
  glab repo view

  # Create a dedicated PRIVATE repository on GitLab
  glab repo create my-second-brain-vault --private
  ```

---

### 3. Repository Visibility: Private vs. Public Strategy

| Strategy | Recommended When | Pros & Considerations |
| :--- | :--- | :--- |
| **🔒 Private Repository (Recommended)** | Default for personal or enterprise knowledge. | Completely protects confidential tokens, proprietary ADRs, internal passwords, and personal reflection logs from public indexing. |
| **🌍 Public Repository (Digital Garden)** | Open-source libraries, public cheatsheets, community ADRs. | Allows sharing public knowledge bases and documentation gardens with the world. **Never commit `.env` or credentials!** |
| **⚡ Hybrid Submodule Model** | The codebase is Public, but the Second Brain notes are Private. | Keep the root code repo Public, while `.second-brain/` is a linked Git Submodule pointing to a **Private** repository. |

---

### 4. Proactive Diagnostics: "Does It Need Anything Else?"

When running `python second-brain-plus/scripts/git_remote_sync.py --audit`, the engine checks:

1. **CLI Installation & Keyring Authentication:**
   - Detects whether `gh` or `glab` is active and token scopes are sufficient (`repo`, `workflow`).
2. **Repository Visibility Guard:**
   - Warns immediately if sensitive vaults are stored in a **Public** repository.
3. **Secret Scrubbing & `.gitignore` Integrity:**
   - Verifies that `.env`, `credentials.json`, and private tokens are explicitly ignored to avoid GitHub Push Protection rejections.
4. **Branch Synchronization Health:**
   - Calculates exact commit counts: `ahead` (local changes needing `git push`) and `behind` (remote changes needing `git pull`).
5. **Continuous Integration (CI/CD) Automations:**
   - Recommends deploying automated workflows (`.github/workflows/second-brain-sync.yml` or `.gitlab-ci.yml`) for scheduled backup, integrity checks, and link validation.

---

### 5. Automated CI/CD Workflows

#### GitHub Actions Workflow (`.github/workflows/second-brain-sync.yml`)
Runs an automated health audit and sync check on every push:
```yaml
name: Second Brain CI & Audit

on:
  push:
    paths:
      - '.second-brain/**'
      - 'second-brain-plus/**'
  schedule:
    - cron: '0 3 * * *' # Nightly at 03:00 UTC

jobs:
  audit-and-verify:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - name: Verify Brain Integrity
        run: python second-brain-plus/scripts/verify_brain.py
      - name: Remote Sync Audit
        run: python second-brain-plus/scripts/git_remote_sync.py --audit
```

---

## 🇧🇷 Português (PT-BR)

### 1. Filosofia Arquitetural: O Modelo de Backup Duplo

Enquanto o **Notion Central Hub** fornece a interface colaborativa, relacional e visual para interação diária, os **Repositórios Remotos Git** (GitHub e GitLab) operam como a **garantia criptográfica, imutável e versionada de todo o histórico de decisões e código**.

### 2. Ferramentas Suportadas (CLIs)

- **GitHub CLI (`gh`):**
  - Autenticação e diagnóstico: `gh auth status`
  - Inspeção: `gh repo view`
  - Criação de cofre privado: `gh repo create meu-segundo-cerebro --private --source=.second-brain --push`
- **GitLab CLI (`glab`):**
  - Autenticação e diagnóstico: `glab auth status`
  - Criação de cofre privado: `glab repo create meu-segundo-cerebro --private`

### 3. Estratégia de Visibilidade: Privado vs. Público

- **🔒 Repositório Privado (Padrão Recomendado):** Impede que regras confidenciais, notas internas e arquiteturas proprietárias vazem na internet.
- **🌍 Repositório Público (Jardim Digital):** Ideal para documentação open-source e artigos abertos à comunidade.
- **⚡ Modelo Híbrido (Submódulo):** Repositório de código público com a pasta `.second-brain/` configurada como submódulo Git apontando para um repositório privado.

### 4. Diagnóstico Proativo: "Precisa de Algo a Mais?"

Ao executar `/second-brain git-status` ou `python second-brain-plus/scripts/git_remote_sync.py --audit`:
1. Verifica instalação e autenticação das ferramentas `gh` e `glab`.
2. Alerta sobre repositórios públicos com dados sensíveis.
3. Checa integridade do `.gitignore` para barrar arquivos `.env` e chaves de API.
4. Informa a contagem de commits à frente (*ahead*) e atrás (*behind*) do servidor.
5. Recomenda a adoção de workflows de CI/CD para automação noturna de integridade.
