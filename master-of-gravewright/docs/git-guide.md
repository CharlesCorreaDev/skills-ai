# Guia de Controle de Versão Git e Empacotamento para Gravewright VTT

O desenvolvimento de módulos, sistemas de RPG e extensões para o **Gravewright VTT** segue o modelo de repositórios Git, versionamento semântico (`X.Y.Z`) e empacotamento em formato ZIP para instalação e distribuição.

---

## 📦 1. Estrutura Canônica de um Módulo

No repositório e **na raiz do pacote ZIP**, os arquivos devem estar sem pastas intermediárias envoltórias. O `manifest.json` precisa estar na raiz do ZIP.

```text
meu-modulo/
├── manifest.json              # Manifesto oficial (obrigatório na raiz)
├── main.js                    # Entrypoint ESM (se módulo de browser/sistema)
├── styles.css                 # Estilos isolados carregados via styles.use()
├── README.md                  # Documentação de uso
├── CHANGELOG.md               # Histórico de alterações
├── LICENSE.txt                # Arquivo de licença COM EXTENSÃO (.txt ou .md)
└── .gitignore                 # Arquivos ignorados pelo Git
```

> [!WARNING]
> **Requisitos do Validador de ZIP do Gravewright (`gravewright/modules/services/packages.py`):**
> 1. **`manifest.json` na raiz:** O arquivo `manifest.json` precisa estar diretamente na raiz do ZIP, não dentro de um subdiretório raiz.
> 2. **Extensões de arquivos permitidas:** Arquivos sem extensão (como `LICENSE` sem sufixo) são **rejeitados**. Use sempre `LICENSE.txt` ou `LICENSE.md`.
> 3. **Arquivos ocultos:** Não inclua arquivos ocultos como `.gitignore`, `.DS_Store` ou pastas `.git/` dentro do ZIP de release.
> 4. **Tamanho máximo:** O arquivo ZIP não pode ultrapassar 50 MB, nem conter mais de 500 arquivos ou 100 MB descompactados.

---

## ⚙️ 2. Arquivo `.gitignore` Recomendado

```gitignore
# Python / Django
__pycache__/
*.py[cod]
*$py.class
*.sqlite3
/data/
/media/
.env

# Astral uv
.venv/
uv.lock

# Node.js
node_modules/
dist/

# Releases e temporários
*.zip
.DS_Store
Thumbs.db
.vscode/
.idea/
```

---

## 🏷️ 3. Versionamento Semântico no `manifest.json`

A versão no `manifest.json` deve seguir estritamente o formato numérico semântico `X.Y.Z` (sem sufixos como `-beta` ou `+build`).

```json
{
  "id": "charles.meu-modulo",
  "name": "Meu Módulo",
  "version": "0.2.0",
  "sdk": {
    "requires": ">=1.0.0 <2.0.0",
    "tested": "1.0.0"
  },
  "entry": "main.js",
  "description": "Descrição funcional do módulo.",
  "author": "Charles Corrêa",
  "license": "MIT"
}
```

---

## 📦 4. Como Gerar o ZIP Válido de Distribuição

Não utilize `git archive HEAD` diretamente se ele incluir arquivos sem extensão (como `LICENSE`) ou arquivos ocultos que o instalador do Gravewright possa rejeitar.

### Comando Python Recomendado (Multiplataforma):
Execute este script na raiz do seu módulo para gerar o ZIP perfeito e aceito pelo instalador:

```bash
python -c "
import zipfile, os
from pathlib import Path

# Extensões permitidas pelo validador do Gravewright
ALLOWED_EXTS = {'.js', '.mjs', '.css', '.json', '.txt', '.md', '.png', '.jpg', '.jpeg', '.webp', '.svg', '.py', '.po', '.mo'}
mod_dir = Path('.')
zip_name = 'meu-modulo-0.2.0.zip'

with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as z:
    for f in mod_dir.rglob('*'):
        if f.is_file() and not f.name.startswith('.') and f.suffix.lower() in ALLOWED_EXTS:
            rel = f.relative_to(mod_dir)
            if not any(part.startswith('.') for part in rel.parts):
                z.write(f, rel)
print(f'Pacote gerado com sucesso: {zip_name}')
"
```

No PowerShell ou terminal Unix:
```bash
# Ou utilizando zip excluindo dotfiles e garantindo LICENSE.txt:
zip -r meu-modulo-0.2.0.zip . -x ".*" -x "__pycache__/*" -x "*.zip"
```

### Criação de Tag Git:
```bash
git add .
git commit -m "feat: release v0.2.0 do módulo"
git tag -a v0.2.0 -m "Release v0.2.0"
git push origin main --tags
```
