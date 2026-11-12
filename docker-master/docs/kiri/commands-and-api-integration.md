# Guia Completo de Comandos do Kiri & Substituição da API do Docker ⚡

> **Objetivo:** Documentar todos os comandos da CLI do Kiri e fornecer o passo a passo exato para substituir o Docker Desktop de forma 100% transparente através do socket e da API nativa do Docker.

---

## 🔌 1. Como Fazer o Kiri Substituir o Docker (Docker API Socket Hijack)

O Kiri implementa um servidor de API compatível com as especificações da Docker Engine API (v1.40+). Isso significa que qualquer ferramenta que converse com o Docker (`docker`, `docker compose`, VS Code Dev Containers, Testcontainers, DBeaver, plugins do JetBrains) funciona imediatamente com o Kiri.

### 📍 Localização do Socket
- **macOS / Linux:** `/var/run/docker.sock` ou `~/.kiri/run/docker.sock`
- **Windows:** Named Pipe `\\.\pipe\docker_engine` (e montado dentro do WSL2 em `/var/run/docker.sock`)

---

### ⚙️ Passo a Passo para Ativar a API do Docker no Kiri

#### Passo 1: Parar e Desativar o Docker Desktop
Para evitar conflito de portas e de socket:
- **macOS:** 
  ```bash
  killall "Docker Desktop" 2>/dev/null
  ```
- **Windows:**
  ```powershell
  Stop-Process -Name "Docker Desktop" -ErrorAction SilentlyContinue
  ```

#### Passo 2: Vincular o Kiri ao Socket Padrão do Docker
Abra o Kiri e nas configurações (ou via CLI):
```bash
# Definir o Kiri como o contexto ativo do Docker:
docker context create kiri --docker "host=unix:///var/run/docker.sock" 2>/dev/null || true
docker context use kiri
```
No Windows (PowerShell):
```powershell
docker context create kiri --docker "host=npipe:////./pipe/docker_engine"
docker context use kiri
```

#### Passo 3: Exportar a Variável de Ambiente DOCKER_HOST (Garante 100% de Compatibilidade)
Se alguma ferramenta antiga não respeitar o contexto do Docker:
- **Linux / macOS (`~/.bashrc` ou `~/.zshrc`):**
  ```bash
  export DOCKER_HOST="unix:///var/run/docker.sock"
  ```
- **Windows (PowerShell / Variáveis de Ambiente):**
  ```powershell
  [System.Environment]::SetEnvironmentVariable('DOCKER_HOST', 'npipe:////./pipe/docker_engine', 'User')
  ```

#### Passo 4: Testar a Conexão
```bash
docker version
# Verifique se o Server Version indica Kiri / Containerd Runtime
docker info
```

---

## 💻 2. Referência Completa de Comandos da CLI do Kiri (`kiri`)

O Kiri fornece a ferramenta de linha de comando `kiri` para gerenciar a máquina virtual, recursos de hardware, domínios e serviços:

### 🚀 Gerenciamento do Runtime & Máquina Virtual
```bash
kiri start             # Inicia a engine e os serviços de background do Kiri
kiri stop              # Para a máquina virtual e encerra os contêineres graciosamente
kiri restart           # Reinicia a engine do Kiri
kiri status            # Exibe o status da VM, uso de RAM, CPU e processos ativos
kiri info              # Exibe versões, diretórios de dados e configurações do host
```

### 🧠 Controle de Memória e Recursos de Hardware
```bash
kiri memory            # Exibe estatísticas de consumo de RAM e páginas recuperadas
kiri memory reclaim    # Força a devolução imediata de memória não utilizada para o SO
kiri cpu               # Exibe consumo de núcleos e limites de processamento
kiri settings set memory.limit=4GB   # Define teto de memória alocável
kiri settings set cpu.cores=4        # Define contagem de núcleos disponíveis
```

### 🌐 Gerenciamento de Domínios Locais & HTTPS
```bash
kiri domains list      # Lista todos os domínios .kiri ativos associados a contêineres
kiri domains add <nome> <porta>  # Mapeia um domínio manual (ex: api.kiri -> 3000)
kiri https trust       # Instala e confia na Autoridade Certificadora (CA) raiz do Kiri no sistema
kiri https status      # Verifica o status dos certificados TLS locais
```

### 📁 Compartilhamento de Arquivos e Volumes
```bash
kiri share list        # Lista pastas do host montadas na VM
kiri share add <caminho-local>  # Adiciona uma nova pasta compartilhada com aceleração VirtIO
kiri share remove <caminho>     # Remove uma pasta compartilhada
```

### 🔄 Sincronização e Migração com Docker
```bash
kiri docker enable-socket    # Garante que o Kiri responda em /var/run/docker.sock
kiri docker disable-socket   # Libera o socket do Docker
kiri docker prune            # Limpeza rápida de imagens, volumes e builders em cache
```

---

## 🛠️ 3. Comandos Docker que Rodam Nativamente no Kiri

Como o Kiri atende à API Docker, todos os comandos canônicos funcionam sem alteração:

```bash
# Execução e Gerenciamento
docker run -d --name web -p 80:80 nginx:alpine
docker ps -a
docker logs -f web
docker exec -it web sh
docker restart web
docker stop web && docker rm web

# Docker Compose
docker compose up -d
docker compose down
docker compose logs -f
docker compose build --no-cache

# Gerenciamento de Recursos
docker system df
docker system prune -af --volumes
```

