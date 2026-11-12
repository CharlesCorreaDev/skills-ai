# Como Criar, Otimizar e Publicar Imagens no Kiri e Podman 📦⚡

> **Objetivo:** Guia completo de ponta a ponta ensinando a construir imagens de sistemas operacionais, serviços de backend, bancos de dados e aplicações web no **Kiri** e **Podman**, aplicando multi-stage builds, boas práticas de segurança (rootless/distroless), auditoria de camadas com **Dive** e publicação nos principais registros de contêineres (**Docker Hub**, **GitHub Packages - GHCR** e **Quay.io**).

---

## 🏗️ 1. Padrões de Criação de Imagens (Dockerfile / Containerfile)

Tanto o Kiri quanto o Podman seguem as especificações da **OCI (Open Container Initiative)**. No Kiri utiliza-se `Dockerfile`, enquanto no Podman você pode usar tanto `Dockerfile` quanto `Containerfile` (nome canônico do ecossistema Podman/Buildah).

---

### 🌟 Exemplo 1: Aplicação Node.js / TypeScript com Multi-Stage Build

```dockerfile
# ==========================================
# Estágio 1: Build & Compilação
# ==========================================
FROM node:22-alpine AS builder

WORKDIR /app

# Aproveitamento agressivo do cache de camadas
COPY package*.json tsconfig.json ./
RUN npm ci

COPY src ./src
RUN npm run build && npm prune --production

# ==========================================
# Estágio 2: Imagem Final de Produção (Ultraleve)
# ==========================================
FROM node:22-alpine AS runner

WORKDIR /app
ENV NODE_ENV=production

# Segurança Rootless: Não rodar como root
USER node

COPY --chown=node:node --from=builder /app/package*.json ./
COPY --chown=node:node --from=builder /app/node_modules ./node_modules
COPY --chown=node:node --from=builder /app/dist ./dist

EXPOSE 3000

CMD ["node", "dist/index.js"]
```

---

### 🌟 Exemplo 2: API em PHP 8.4 com Nginx / FrankenPHP

```dockerfile
FROM dunglas/frankenphp:latest-alpine

ENV SERVER_NAME=":80"
WORKDIR /app

# Instalação de extensões do PHP
RUN install-php-extensions \
    pdo_mysql \
    pdo_pgsql \
    redis \
    opcache \
    intl

COPY composer.json composer.lock ./
RUN composer install --no-dev --optimize-autoloader --no-scripts

COPY . /app

# Permissões seguras
RUN chown -R www-data:www-data /app/storage /app/bootstrap/cache 2>/dev/null || true
```

---

## ⚡ 2. Construindo Imagens no Kiri

Como o Kiri atende à Docker Engine API nativamente com suporte a **BuildKit**, o processo de compilação utiliza o comando `docker build`:

### Compilação Padrão:
```bash
# 1. Certifique-se de que o contexto do Kiri está ativo:
docker context use kiri

# 2. Construir a imagem localmente com tag:
docker build -t meu-usuario/minha-app:1.0.0 .

# 3. Construir com múltiplos estágios e sem cache (para release limpo):
docker build --no-cache -t meu-usuario/minha-app:latest .
```

### Build Multi-Arquitetura (Intel x86_64 e Apple Silicon ARM64):
```bash
# O Kiri suporta emulação rápida para compilar imagens multiplataforma:
docker buildx build --platform linux/amd64,linux/arm64 -t meu-usuario/minha-app:1.0.0 .
```

---

## 🦭 3. Construindo Imagens no Podman

No Podman, a criação de imagens é executada através da ferramenta nativa `podman build` (baseada na tecnologia `Buildah`), dispensando totalmente daemons de root:

### Compilação Padrão:
```bash
# Usando Dockerfile ou Containerfile:
podman build -t meu-usuario/minha-app:1.0.0 -f Containerfile .

# Ou com Dockerfile comum:
podman build -t meu-usuario/minha-app:1.0.0 .
```

### Build Multi-Arquitetura no Podman:
```bash
podman build --platform linux/amd64,linux/arm64 --manifest meu-usuario/minha-app:1.0.0 .
```

---

## 🔍 4. Auditoria de Camadas com o Dive antes de Publicar

Antes de publicar qualquer imagem na internet ou em ambiente de produção corporativo, utilize o **Dive** para checar se você não esqueceu dependências temporárias ou lixo dentro das camadas:

```bash
# No Kiri (Docker):
dive meu-usuario/minha-app:1.0.0

# No Podman:
# Exportar a imagem para o Dive analisar ou via pipe:
podman save meu-usuario/minha-app:1.0.0 | dive docker-archive:/dev/stdin
```

**Meta de Qualidade:** O score de eficiência (`Image efficiency`) reportado pelo Dive deve ser de **98% a 100%**, com 0 bytes de desperdício em arquivos apagados tardiamente.

---

## 🚀 5. Como Publicar Imagens nos Registros (Registries)

### 🔹 Opção A: Docker Hub (`docker.io`)

#### 1. Autenticação:
- **No Kiri (Docker CLI):**
  ```bash
  docker login
  # Digite seu usuário e token de acesso pessoal (PAT)
  ```
- **No Podman:**
  ```bash
  podman login docker.io
  # As credenciais são salvas de forma segura em ~/.config/containers/auth.json
  ```

#### 2. Taguear e Publicar:
- **No Kiri:**
  ```bash
  docker tag meu-app:1.0.0 docker.io/meu-usuario/meu-app:1.0.0
  docker tag meu-app:1.0.0 docker.io/meu-usuario/meu-app:latest
  docker push docker.io/meu-usuario/meu-app:1.0.0
  docker push docker.io/meu-usuario/meu-app:latest
  ```
- **No Podman:**
  ```bash
  podman tag meu-app:1.0.0 docker.io/meu-usuario/meu-app:1.0.0
  podman push docker.io/meu-usuario/meu-app:1.0.0
  ```

---

### 🔹 Opção B: GitHub Packages / GitHub Container Registry (`ghcr.io`)
Ideal para repositórios no GitHub, com integração direta ao GitHub Actions e controle de permissões por organização.

#### 1. Autenticação via GitHub CLI (`gh`) ou Token:
```bash
# Autenticação automática usando o GitHub CLI:
gh auth token | docker login ghcr.io -u SEU_USUARIO_GITHUB --password-stdin
# Ou com Podman:
gh auth token | podman login ghcr.io -u SEU_USUARIO_GITHUB --password-stdin
```

#### 2. Taguear e Publicar no GHCR:
```bash
# No Kiri / Docker:
docker tag meu-app:1.0.0 ghcr.io/seu-usuario-ou-org/meu-app:1.0.0
docker push ghcr.io/seu-usuario-ou-org/meu-app:1.0.0

# No Podman:
podman tag meu-app:1.0.0 ghcr.io/seu-usuario-ou-org/meu-app:1.0.0
podman push ghcr.io/seu-usuario-ou-org/meu-app:1.0.0
```

---

### 🔹 Opção C: Quay.io (Registro Oficial mantido pela Red Hat)
Muito utilizado em ecossistemas de Kubernetes corporativos e projetos Open Source.

```bash
# Login no Quay:
podman login quay.io

# Taguear e Publicar:
podman tag meu-app:1.0.0 quay.io/meu-usuario/meu-app:1.0.0
podman push quay.io/meu-usuario/meu-app:1.0.0
```

---

## 🤖 6. Automação de Publicação via GitHub Actions (CI/CD)

Crie um arquivo `.github/workflows/publish-container.yml` no seu repositório:

```yaml
name: Build and Publish Container Image

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  build-and-push:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      packages: write

    steps:
      - name: Checkout Código
        uses: actions/checkout@v4

      - name: Setup QEMU (Multi-arquitetura)
        uses: docker/setup-qemu-action@v3

      - name: Setup Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login no GitHub Container Registry (GHCR)
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extrair Metadados (Tags e Labels)
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}

      - name: Build e Push Multi-Arch
        uses: docker/build-push-action@v5
        with:
          context: .
          platforms: linux/amd64,linux/arm64
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

