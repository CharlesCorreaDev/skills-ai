# Cheatsheet / Guia Rápido - Docker Master

## 🧹 Limpeza e Manutenção do Sistema

| Ação | Comando | Descrição |
|---|---|---|
| **Limpeza Geral** | `docker system prune -a --volumes` | Remove **tudo** que não está sendo usado no momento (imagens, contêineres parados, redes, volumes órfãos). Cuidado: Destrutivo. |
| **Limpeza Leve** | `docker system prune` | Remove apenas contêineres parados e imagens dangling (sem tag/camada órfã). |
| **Ver Espaço** | `docker system df` | Mostra exatamente onde o espaço do Docker está sendo utilizado. |

## 🐋 Comandos Diários de Contêiner

```bash
# Iniciar stack (Compose V2)
docker compose up -d

# Derrubar stack e remover volumes atrelados
docker compose down -v

# Ver logs em tempo real
docker logs -f <container_id_ou_nome>

# Entrar no shell do contêiner rodando (Linux/sh)
docker exec -it <container_id_ou_nome> sh

# Inspecionar detalhes técnicos
docker inspect <container_id_ou_nome>
```

## 🏗️ Construção de Imagens Avançada

```bash
# BuildKit (Garante uso do novo motor de build, mais rápido)
DOCKER_BUILDKIT=1 docker build -t meu_app:latest .

# Build forçando ignorar o cache local
docker build --no-cache -t meu_app:latest .
```

## 🔌 Troubleshooting Básico
- Se um container iniciar e parar logo em seguida, remova o `-d` do compose (`docker compose up`) ou use `docker logs` para ler a falha imediata.
- No Windows (WSL2), se houver lentidão de leitura/escrita, garanta que os arquivos fonte não estão no File System montado do Windows (`/mnt/c`), mas sim no file system nativo do WSL (`/home/user/`).

## 🛡️ Segurança e Vulnerabilidades (Docker Scout)

```bash
# Analisar vulnerabilidades locais da imagem (CVEs)
docker scout cves minha_imagem:latest

# Obter recomendações para corrigir vulnerabilidades (ex: mudar imagem base)
docker scout recommendations minha_imagem:latest

# Analisar impacto se eu atualizar a imagem base
docker scout update minha_imagem:latest
```

## 🚀 Publicando Imagens no Docker Hub

Para enviar sua imagem customizada para o mundo (ou para seu time):

```bash
# 1. Autenticar no Docker Hub (via CLI)
docker login -u seu_usuario

# 2. Fazer o Build já com a Tag do seu repositório
docker build -t seu_usuario/nome_da_imagem:v1.0 .

# 3. (Opcional) Adicionar Tag em uma imagem já existente
docker tag minha_imagem_local seu_usuario/nome_da_imagem:latest

# 4. Enviar a imagem para o Docker Hub
docker push seu_usuario/nome_da_imagem:v1.0
docker push seu_usuario/nome_da_imagem:latest
```
