# Documentação Completa do Podman (Pod Manager) 🦭

> **Fonte Oficial:** [podman.io](https://podman.io/)  
> **Documentação Canônica:** [docs.podman.io](https://docs.podman.io/)  
> **Repositório GitHub:** [github.com/containers/podman](https://github.com/containers/podman)  
> **Comunidade & Tutoriais:** [podman.io/community](https://podman.io/community)

---

## 📖 1. O que é o Podman e por que ele é diferente?

O **Podman** é uma engine de contêineres padrão OCI (Open Container Initiative) de código aberto, mantida pela Red Hat e pela comunidade Linux, projetada para desenvolvimento, execução e gerenciamento de contêineres e pods.

### 🌟 As Três Grandes Diferenças em relação ao Docker:
1. **Daemonless Architecture (Arquitetura Sem Daemon Central):**
   - O Docker depende do processo `dockerd` rodando continuamente em segundo plano com privilégios elevados. Se o daemon cair, todos os contêineres podem ser afetados.
   - O Podman cria os contêineres como **processos filhos diretos** via `conmon` (Container Monitor) e `crun`/`runc`. Não há daemon único consumindo recursos continuamente.
2. **Rootless por Padrão (Sem Privilégios de Administrador):**
   - No Docker, acessar o socket dá ao usuário direitos equivalentes a root na máquina.
   - No Podman, qualquer usuário sem privilégios pode construir, rodar e gerenciar contêineres isolados usando User Namespaces do Linux (`subuid` e `subgid`), tornando o ambiente muito mais seguro contra invasões e escapes de contêiner.
3. **Conceito Nativo de Pods (Padrão Kubernetes):**
   - O Podman permite agrupar contêineres em **Pods** que compartilham o mesmo namespace de rede e volumes locais, simulando exatamente o comportamento de um cluster Kubernetes.

---

## 🚀 2. Instalação do Podman

### Linux (Ubuntu, Debian, Fedora, Arch)
```bash
# Ubuntu 22.04+ / Debian:
sudo apt-get update && sudo apt-get install -y podman

# Fedora / RHEL:
sudo dnf install -y podman
```

### macOS
```bash
brew install podman
# Iniciar a máquina virtual leve do Podman no Mac:
podman machine init --now
```

### Windows (WSL2)
```bash
# Via Winget:
winget install RedHat.Podman
# Ou através do instalador do Podman Desktop: https://podman-desktop.io/
```

---

## 🛠️ 3. Transição Suave e Equivalência com Docker

A sintaxe da CLI do Podman é intencionalmente 100% compatível com a do Docker:

```bash
# Configurar alias direto:
alias docker=podman

# Operações básicas idênticas:
podman pull alpine:latest
podman run -d --name meu-app -p 8080:80 nginx:alpine
podman ps -a
podman logs -f meu-app
podman exec -it meu-app sh
podman stop meu-app && podman rm meu-app
```

---

## 🧩 4. Orquestração Local com Podman Compose

Existem duas formas suportadas de rodar arquivos `docker-compose.yml` com Podman:

### 1. `podman compose` (Plugin Nativo Moderno)
```bash
podman compose up -d
podman compose down
```

### 2. `podman-compose` (Utilitário Python)
```bash
pip install podman-compose
podman-compose up -d
```

---

## ☸️ 5. Criação de Pods e Integração com Kubernetes

Uma das maiores forças do Podman é a facilidade de mover contêineres do ambiente de desenvolvimento direto para a nuvem/Kubernetes:

### Criando um Pod com múltiplos contêineres:
```bash
# 1. Criar o Pod compartilhando a porta 8080:
podman pod create --name web-pod -p 8080:80

# 2. Adicionar contêineres dentro do mesmo Pod:
podman run -d --pod web-pod --name web-front nginx:alpine
podman run -d --pod web-pod --name web-back meu-backend:latest
```

### Gerando Manifestos Kubernetes (`podman generate kube`):
```bash
# Converte o Pod em execução diretamente em um arquivo YAML padrão do Kubernetes:
podman generate kube web-pod > k8s-deployment.yaml
```

### Executando Manifestos Kubernetes Localmente (`podman play kube`):
```bash
# Roda qualquer manifesto do Kubernetes diretamente no Podman sem precisar subir Minikube ou Kind!
podman play kube k8s-deployment.yaml
```

---

## ⏸️ 6. Checkpoint e Restore (CRIU)

O Podman permite salvar o estado exato da memória de um contêiner em execução para o disco e restaurá-lo mais tarde, permitindo migração de processos ou cold-start instantâneo de aplicações pesadas:

```bash
# Congelar o estado do contêiner e salvar a memória:
podman container checkpoint meu-app --export /tmp/meu-app-dump.tar.gz

# Restaurar o contêiner exatamente de onde parou:
podman container restore --import /tmp/meu-app-dump.tar.gz
```

---

## 📊 7. Python SDK: Podman-py

Para automações DevOps e scripts em Python, o Podman disponibiliza a biblioteca oficial `podman-py`:
- Documentação: [podman-py.readthedocs.io](https://podman-py.readthedocs.io/)
- Instalação: `pip install podman`
- Permite gerenciar contêineres, pods, imagens e redes de forma programática com tipagem e suporte assíncrono.

---

## 📚 Guias Complementares
- [Comandos Completos da CLI e Integração com a API do Docker](commands-and-api-integration.md) - Manual passo a passo para emular a API do Docker com Podman (`podman.sock`), aliases e tabela de comandos de Pods, imagens, volumes e redes.

