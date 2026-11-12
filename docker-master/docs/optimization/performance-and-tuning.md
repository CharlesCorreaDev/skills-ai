# Guia Mestre de Otimização e Performance para Docker, Kiri e Podman ⚡🚀

> **Objetivo:** Fornecer o manual definitivo de técnicas, comandos, parâmetros de kernel, flags de compilação e configurações de runtime para extrair velocidade máxima, mínimo consumo de memória e I/O instantâneo em qualquer engine de contêineres.

---

## 🏎️ 1. Otimização de I/O de Disco & Bind Mounts (O Gargalo Nº 1)

O maior motivo de lentidão em contêineres no Windows e macOS é a tradução de chamadas de sistema entre o filesystem do host (NTFS / APFS) e o Linux do contêiner.

### 🪟 No Windows (WSL2):
1. **Regra Absoluta do Filesystem Nativo:**
   - ❌ **Lento:** Montar volumes a partir de drives do Windows (`/mnt/c/Projetos/...`).
   - ✅ **Rápido (até 10x mais veloz):** Manter o projeto dentro da partição nativa do WSL2 (ex: `\\wsl$\Ubuntu\home\<user>\projetos\...` ou `/home/<user>/...`).
2. **Ajuste Fino do `.wslconfig` (`%USERPROFILE%\.wslconfig`):**
   ```ini
   [wsl2]
   memory=4GB                 # Impede que o WSL2 devore toda a RAM
   processors=4               # Limita núcleos de CPU
   swap=2GB                   # Define paginação controlada
   pageReporting=true         # Devolve memória liberada de volta para o Windows
   nestedVirtualization=false # Desliga virtualização aninhada se não usar KVM
   ```

### 🍏 No macOS:
1. **VirtioFS Obrigatório:**
   - Certifique-se de que o backend de compartilhamento de arquivos seja **VirtioFS** (em vez do gRPC FUSE legado). O Kiri já traz aceleração nativa via Virtio; no Docker Desktop, selecione em *Settings > Resources > File Sharing*.
2. **Flags de Consistência (`:cached` e `:delegated`):**
   - Em bind mounts volumosos no `docker-compose.yml`:
     ```yaml
     volumes:
       - ./:/app:cached          # O contêiner pode atrasar sincronização para o host
       - ./node_modules:/app/node_modules # Volume anônimo isolado para não cruzar I/O
     ```

---

## 🧠 2. Otimização de Memória e Garbage Collection de Imagens

### ⚡ No Kiri (Recuperação Instantânea):
```bash
# Forçar recuperação imediata de memória retida para o SO:
kiri memory reclaim

# Definir teto máximo estrito:
kiri settings set memory.limit=4GB
```

### 🦭 No Podman (Modo Rootless e Limpeza):
```bash
# Limpar imagens órfãs e volumes não referenciados sem confirmação:
podman system prune --all --volumes --force

# Executar contêiner com limite estrito de memória e swap:
podman run -d --memory="512m" --memory-swap="1g" --cpus="1.5" meu-app
```

### 🐳 No Docker Desktop / Engine:
```bash
# Configurar limites automáticos de log no daemon (/etc/docker/daemon.json ou Settings > Docker Engine):
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "features": {
    "buildkit": true
  }
}
```

---

## 🛠️ 3. Otimização de Compilação (BuildKit & Caching Avançado)

1. **Uso de `.dockerignore` Rigoroso:**
   - Nunca envie `.git`, arquivos de log, `node_modules` ou arquivos temporários para o contexto de build:
     ```text
     .git
     .gitignore
     node_modules
     vendor
     *.log
     dist
     .env
     ```
2. **Mount de Cache durante a Instalação de Pacotes:**
   - Evita baixar pacotes repetidamente em cada build:
     ```dockerfile
     # Para Node.js / NPM:
     RUN --mount=type=cache,target=/root/.npm npm ci

     # Para PHP / Composer:
     RUN --mount=type=cache,target=/tmp/cache composer install --no-dev

     # Para Python / Pip:
     RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
     ```

---

## 🩺 4. Comandos de Diagnóstico e Inspeção de Gargalos

```bash
# 1. Estatísticas de consumo em tempo real de todos os contêineres:
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"
# Ou no Podman:
podman stats --no-stream

# 2. Inspecionar processos internos sem entrar no contêiner:
docker top <container_id>
podman top <container_id>

# 3. Descobrir quais arquivos mudaram dentro da camada do contêiner (Copy-on-Write diff):
docker diff <container_id>
podman diff <container_id>
```

