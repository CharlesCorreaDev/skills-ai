# Guia Completo de Comandos do Podman & Substituição da API do Docker 🦭

> **Objetivo:** Documentar todos os comandos da CLI do Podman e fornecer o procedimento detalhado para emular a API do Docker, redirecionando o socket do Docker para o serviço do Podman (`podman.sock`).

---

## 🔌 1. Como Fazer o Podman Substituir o Docker (Docker API Emulation)

O Podman possui um serviço nativo (`podman system service`) que implementa a API REST do Docker v1.40+. Ele responde exatamente como o `dockerd`, permitindo que ferramentas como Docker Compose, Testcontainers, VS Code, CI e IntelliJ conversem com o Podman sem perceber a diferença.

---

### ⚙️ Passo a Passo para Ativar a API do Docker no Podman

#### 🐧 No Linux (Rootless via Systemd)
O Linux moderno já vem com o socket do Podman configurado via systemd para usuários comuns:

```bash
# 1. Habilitar e iniciar o socket do Podman para o seu usuário:
systemctl --user enable --now podman.socket

# 2. Verificar se o socket está ativo:
systemctl --user status podman.socket

# 3. Descobrir o caminho do socket:
# Geralmente fica em: /run/user/$UID/podman/podman.sock
echo "unix://$XDG_RUNTIME_DIR/podman/podman.sock"

# 4. Vincular ao Docker CLI:
export DOCKER_HOST="unix://$XDG_RUNTIME_DIR/podman/podman.sock"

# (Opcional) Criar link simbólico para ferramentas antigas que buscam /var/run/docker.sock:
sudo ln -sf "$XDG_RUNTIME_DIR/podman/podman.sock" /var/run/docker.sock
```

#### 🍏 No macOS (Podman Machine)
No macOS, o Podman roda dentro de uma máquina virtual leve:
```bash
# 1. Iniciar a máquina virtual do Podman:
podman machine start

# 2. Configurar o socket e o contexto Docker:
podman-mac-helper install
# Ou configurar o DOCKER_HOST manualmente:
export DOCKER_HOST="unix://$(podman machine inspect --format '{{.ConnectionInfo.PodmanSocket.Path}}')"

# 3. Testar:
docker version
```

#### 🪟 No Windows (WSL2 / Podman Desktop)
```powershell
# 1. Iniciar o serviço do Podman:
podman machine start

# 2. Definir a variável DOCKER_HOST no PowerShell:
$env:DOCKER_HOST = "npipe:////./pipe/docker_engine"
# Ou apontando para o socket WSL2 exportado pelo Podman Desktop.
```

#### 🔄 Configurar o Docker Context Oficial
Você pode registrar o Podman nativamente no Docker CLI:
```bash
docker context create podman --docker "host=unix://$XDG_RUNTIME_DIR/podman/podman.sock"
docker context use podman
```

---

## 💻 2. Referência Completa de Comandos da CLI do Podman (`podman`)

### 📦 1. Gerenciamento de Contêineres
| Comando | O que faz | Exemplo |
| :--- | :--- | :--- |
| `podman run` | Cria e inicia um contêiner | `podman run -d --name web -p 8080:80 nginx:alpine` |
| `podman ps` | Lista contêineres ativos | `podman ps -a` (todos os estados) |
| `podman stop` | Para um ou mais contêineres | `podman stop web` (ou `podman stop -a` para todos) |
| `podman start` | Inicia um contêiner parado | `podman start web` |
| `podman restart` | Reinicia um contêiner | `podman restart web` |
| `podman rm` | Remove um contêiner | `podman rm -f web` (força remoção) |
| `podman exec` | Executa comando dentro do contêiner | `podman exec -it web sh` |
| `podman logs` | Exibe logs do contêiner | `podman logs -f --tail 100 web` |
| `podman inspect` | Detalhes em JSON do contêiner | `podman inspect web` |
| `podman top` | Exibe processos rodando no contêiner | `podman top web` |
| `podman stats` | Uso de CPU, memória e rede em tempo real | `podman stats` |
| `podman port` | Mostra portas mapeadas | `podman port web` |

---

### ☸️ 2. Gerenciamento de Pods (Exclusivo do Podman!)
| Comando | O que faz | Exemplo |
| :--- | :--- | :--- |
| `podman pod create` | Cria um Pod compartilhado | `podman pod create --name meu-pod -p 3000:80` |
| `podman pod list` (`podman pod ps`) | Lista todos os Pods | `podman pod ps` |
| `podman pod start` / `stop` | Inicia ou para todos os contêineres do Pod | `podman pod stop meu-pod` |
| `podman pod rm` | Remove o Pod e todos os contêineres associados | `podman pod rm -f meu-pod` |
| `podman pod top` | Processos ativos dentro do Pod | `podman pod top meu-pod` |
| `podman generate kube` | Gera manifesto YAML do Kubernetes | `podman generate kube meu-pod > k8s.yaml` |
| `podman play kube` | Sobe manifestos do Kubernetes localmente | `podman play kube k8s.yaml` |
| `podman play kube --down` | Destrói a stack criada pelo manifesto | `podman play kube --down k8s.yaml` |

---

### 🖼️ 3. Gerenciamento de Imagens
| Comando | O que faz | Exemplo |
| :--- | :--- | :--- |
| `podman pull` | Baixa uma imagem do registro | `podman pull docker.io/library/node:20-alpine` |
| `podman images` | Lista imagens locais | `podman images` |
| `podman build` | Constrói imagem a partir de Containerfile | `podman build -t meu-app:1.0 .` |
| `podman rmi` | Remove uma imagem | `podman rmi meu-app:1.0` |
| `podman tag` | Adiciona uma nova tag | `podman tag meu-app:1.0 registry.empresa.com/app:1.0` |
| `podman push` | Envia imagem para o registro | `podman push registry.empresa.com/app:1.0` |
| `podman save` / `load` | Exporta/importa imagem em arquivo `.tar` | `podman save -o app.tar meu-app:1.0` |
| `podman history` | Exibe histórico de camadas da imagem | `podman history meu-app:1.0` |

---

### 🌐 4. Gerenciamento de Redes
| Comando | O que faz | Exemplo |
| :--- | :--- | :--- |
| `podman network create` | Cria uma rede isolada | `podman network create rede-interna` |
| `podman network ls` | Lista redes existentes | `podman network ls` |
| `podman network inspect` | Inspeciona configuração e subnets | `podman network inspect rede-interna` |
| `podman network connect` | Conecta contêiner a uma rede | `podman network connect rede-interna web` |
| `podman network disconnect` | Desconecta contêiner da rede | `podman network disconnect rede-interna web` |
| `podman network rm` | Remove rede não utilizada | `podman network rm rede-interna` |

---

### 💾 5. Gerenciamento de Volumes
| Comando | O que faz | Exemplo |
| :--- | :--- | :--- |
| `podman volume create` | Cria um volume persistente | `podman volume create dados-db` |
| `podman volume ls` | Lista volumes locais | `podman volume ls` |
| `podman volume inspect` | Caminho físico no disco | `podman volume inspect dados-db` |
| `podman volume rm` | Remove volume | `podman volume rm dados-db` |
| `podman volume prune` | Remove todos os volumes órfãos | `podman volume prune -f` |

---

### ⚙️ 6. Sistema, Limpeza e Máquina Virtual
| Comando | O que faz | Exemplo |
| :--- | :--- | :--- |
| `podman system df` | Espaço ocupado por contêineres, imagens e volumes | `podman system df` |
| `podman system prune` | Limpa contêineres parados e imagens sem uso | `podman system prune -a --volumes` |
| `podman system service` | Inicia o servidor da API compatível com Docker | `podman system service -t 0 tcp:127.0.0.1:8888` |
| `podman machine init` | Cria máquina virtual do Podman (Mac/Windows) | `podman machine init --cpus 4 --memory 4096` |
| `podman machine start` | Inicia a máquina virtual | `podman machine start` |
| `podman machine stop` | Desliga a máquina virtual | `podman machine stop` |
| `podman machine rm` | Remove a máquina virtual | `podman machine rm` |

---

## ⚡ 3. Atalho Universal de Aliases (`~/.bashrc` ou PowerShell)

Para substituir completamente o Docker sem precisar digitar `podman`:

### No Linux / macOS:
```bash
# Adicione ao ~/.bashrc ou ~/.zshrc:
alias docker="podman"
alias docker-compose="podman compose"

# Testar se funcionou:
docker ps
docker-compose up -d
```

### No Windows (PowerShell Profile):
```powershell
# Adicione ao $PROFILE:
function docker { podman $args }
function docker-compose { podman compose $args }
```

