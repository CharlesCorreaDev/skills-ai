# Guia Completo: Como Publicar Módulos e Sistemas no Foundry VTT 🚀📦
> *Passo a Passo Oficial para Hospedagem, GitHub Releases, Validação e Submissão no Diretório do FoundryVTT.com*  
> *Master of Foundry VTT by GM Charles Corrêa*

---

## 📌 Visão Geral do Ciclo de Publicação

Para que qualquer mestre ou jogador consiga instalar o seu módulo ou sistema através da interface do Foundry VTT (ou para que ele apareça no **Diretório Oficial de Pacotes em [foundryvtt.com/packages](https://foundryvtt.com/packages/)**), o pacote passa por **4 etapas obrigatórias**:

```
1. Estruturação do Manifesto (`module.json` ou `system.json`)
                         │
                         ▼
2. Repositório Git & Automação de Releases (GitHub / GitLab)
                         │
                         ▼
3. Validação Técnica com `@foundryvtt/foundryvtt-cli`
                         │
                         ▼
4. Submissão no Portal Oficial do Foundry VTT (`foundryvtt.com`)
```

---

## 📄 1. Requisitos do Manifesto (`module.json` / `system.json`)

Para ser aceito no diretório e funcionar via instalador remoto, o manifesto precisa conter as URLs públicas permanentes de distribuição:

```json
{
  "id": "meu-modulo-incrivel",
  "title": "Meu Módulo Incrível",
  "description": "Adiciona automações táticas e interface moderna para Foundry VTT.",
  "version": "1.0.0",
  "compatibility": {
    "minimum": "12",
    "verified": "12.331",
    "maximum": "14"
  },
  "authors": [
    {
      "name": "Charles Corrêa",
      "url": "https://github.com/CharlesCorreaDev",
      "discord": "charlescorrea"
    }
  ],
  "esmodules": ["scripts/main.mjs"],
  "styles": ["styles/module.css"],
  
  "url": "https://github.com/CharlesCorreaDev/meu-modulo-incrivel",
  "manifest": "https://github.com/CharlesCorreaDev/meu-modulo-incrivel/releases/latest/download/module.json",
  "download": "https://github.com/CharlesCorreaDev/meu-modulo-incrivel/releases/download/v1.0.0/module.zip",
  "readme": "https://raw.githubusercontent.com/CharlesCorreaDev/meu-modulo-incrivel/main/README.md",
  "license": "MIT"
}
```

### 🚨 As 3 URLs Sagradas do Manifesto:
1. **`url`**: Página inicial do projeto (ex: o repositório no GitHub).
2. **`manifest`**: **DEVE apontar sempre para a release mais recente** (`/releases/latest/download/module.json`). É esse link que o Foundry consulta para saber se saiu uma versão nova!
3. **`download`**: Link direto para baixar o arquivo `.zip` da versão específica descrita no campo `version`.

---

## 📦 2. Estrutura do Arquivo `.zip` de Distribuição

Um erro muito comum que impede a instalação é empacotar a pasta de forma errada no `.zip`:

### ❌ Formato Errado (Sem pasta raiz ou com caminhos absolutos):
```
module.zip
├── module.json
├── scripts/
└── styles/
```
*(Se descompactado direto na raiz de `Data/modules/`, ele espalha arquivos soltos e quebra o Foundry).*

### ✅ Formato Correto (Pasta com o ID exato como raiz do ZIP):
```
module.zip
└── meu-modulo-incrivel/
    ├── module.json
    ├── scripts/
    │   └── main.mjs
    ├── styles/
    │   └── module.css
    └── README.md
```

---

## 🛠️ 3. Empacotamento Automatizado com o CLI Oficial

Utilize o CLI oficial `@foundryvtt/foundryvtt-cli` (já disponível no ambiente) para validar e gerar o pacote:

```bash
# 1. Validar se o manifest cumpre todos os schemas exigidos pelo Foundry
fvtt package validate "meu-modulo-incrivel"

# 2. Empacotar compêndios (se houver fontes em YAML/JSON)
fvtt package pack "meu-modulo-incrivel"

# 3. Gerar o arquivo .zip pronto para distribuição
fvtt package release "meu-modulo-incrivel"
```

---

## 🤖 4. Automação de Releases via GitHub Actions (CI/CD)

Crie o arquivo `.github/workflows/release.yml` no seu repositório para que, a cada tag `v*` criada (ex: `git tag v1.0.0 && git push --tags`), o GitHub crie a release e anexe o `module.json` e o `module.zip` automaticamente:

```yaml
name: Release Creation

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Build Zip Package
        run: |
          mkdir -p package/meu-modulo-incrivel
          cp -r scripts styles assets module.json README.md package/meu-modulo-incrivel/
          cd package && zip -r ../module.zip meu-modulo-incrivel

      - name: Create GitHub Release
        uses: softprops/action-gh-release@v2
        with:
          files: |
            module.json
            module.zip
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

## 🌐 5. Como Submeter no Diretório Oficial do Foundry VTT

Depois que o repositório estiver público e a primeira release (`v1.0.0`) estiver funcionando via link de manifesto:

### Passo a Passo no Portal:
1. Acesse **[https://foundryvtt.com/](https://foundryvtt.com/)** e faça login com sua conta oficial de desenvolvedor/usuário.
2. No menu superior ou no seu painel de usuário, acesse a seção **"Package Submissions"** ou vá direto em:  
   👉 **[https://foundryvtt.com/packages/submit](https://foundryvtt.com/packages/submit)**
3. Preencha os campos solicitados:
   - **Package Type:** Selecione `Module` ou `System`.
   - **Manifest URL:** Cole a URL raw permanente do seu manifesto (ex: `https://github.com/CharlesCorreaDev/meu-modulo-incrivel/releases/latest/download/module.json`).
4. Clique em **"Validate & Submit"**:
   - O servidor do Foundry fará uma requisição `GET` imediata na sua URL de manifesto.
   - Ele verificará se o JSON é válido, se o link de download responde `HTTP 200` e se os campos obrigatórios estão preenchidos.
5. **Revisão e Aprovação:**
   - Pacotes novos passam por uma breve moderação pela equipe do Foundry VTT (geralmente 24 a 48 horas) para garantir que não violam a Política de Licença ou Propriedade Intelectual.
   - Uma vez aprovado, seu módulo aparecerá nas buscas do Foundry VTT para todos os usuários do mundo!

---

## 🔄 6. Como Atualizar seu Pacote no Futuro

Depois de aceito no diretório oficial, **você NUNCA mais precisa submeter o formulário no site**:
1. Incremente o campo `"version": "1.1.0"` no `module.json`.
2. Atualize o `"download"` para a nova release `v1.1.0/module.zip`.
3. Atualize a tag no Git (`git tag v1.1.0 && git push --tags`).
4. O GitHub Actions publicará os novos arquivos na release `latest`.
5. O Foundry VTT consulta a URL do `manifest` automaticamente a cada 24 horas e alertará todos os mestres que instalaram seu módulo de que uma atualização está disponível!
