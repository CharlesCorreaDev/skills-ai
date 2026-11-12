# Documentação Completa do Kiri (Runkiri) ⚡

> **Fonte Oficial:** [docs.runkiri.com](https://docs.runkiri.com/)  
> **Repositório:** [github.com/libracoder/kiri](https://github.com/libracoder/kiri)  
> **Comunidade / Reddit:** [r/BestGitHubRepos - Kiri](https://www.reddit.com/r/BestGitHubRepos/comments/1xplfp5/kiri_a_tiny_fast_container_runtime_for_macos/)

---

## 📖 1. Visão Geral e Filosofia (What is Kiri?)
O **Kiri** é um runtime de contêineres e máquinas virtuais ultraleve, rápido e eficiente, desenhado especificamente para substituir o Docker Desktop no macOS e Windows, reduzindo o desperdício de memória RAM e CPU a níveis mínimos.

### 🌟 Destaques de Arquitetura:
1. **Drop-in Replacement:** Substitui o Docker Desktop de forma totalmente transparente. Mantém o mesmo socket (`/var/run/docker.sock` ou named pipe no Windows), funcionando imediatamente com a CLI `docker`, `docker compose`, `testcontainers`, VS Code Remote Containers e ferramentas de CI locais.
2. **Dynamic Memory Reclamation (Recuperação Dinâmica de Memória):**
   - O Docker Desktop pré-aloca e retém gigabytes de RAM mesmo quando os contêineres terminam a execução.
   - O Kiri utiliza compactação de memória e retorno dinâmico de páginas para o sistema operacional hospedeiro. Em idle, consome entre **150MB e 400MB**, devolvendo a memória instantaneamente para o seu SO.
3. **Boot Sub-Segundo:** Inicialização quase instantânea da stack de virtualização.
4. **I/O de Disco de Alta Performance:** Montagem de volumes (Bind Mounts) otimizada para eliminar os gargalos clássicos de sistemas de arquivos sincronizados (ex: virtiofs acelerado).

---

## 🚀 2. Instalação e Configuração

### Instalação no macOS
```bash
# Via Homebrew (quando disponível) ou baixando o instalador DMG oficial:
# https://docs.runkiri.com/install/
```
- Suporte nativo completo para **Apple Silicon (M1/M2/M3/M4)** e **Intel**.
- Integração com a Menu Bar para monitoramento de CPU, memória e status dos serviços.

### Instalação no Windows
- Utiliza a infraestrutura moderna do WSL2 / Hyper-V com aceleração de hardware nativa.
- Baixe o instalador `.exe` em [docs.runkiri.com/install/](https://docs.runkiri.com/install/).
- Não requer licença corporativa paga para uso em equipes.

---

## 🌐 3. Recursos Avançados de Rede, Domínios e HTTPS

O Kiri resolve uma das maiores dores do desenvolvimento local: gerenciar portas e certificados SSL.

### 🔹 Domínios Automáticos `.kiri`
- Qualquer contêiner ou serviço exposto pode ser acessado diretamente por nome de domínio automático, sem necessidade de editar o arquivo `/etc/hosts`:
  - Exemplo: um contêiner nomeado `api-backend` fica disponível em `http://api-backend.kiri`.

### 🔹 Certificados HTTPS Locais Nativos
- Gera e confia automaticamente em certificados TLS locais para todos os domínios `.kiri`.
- Permite testar cookies `Secure`, HTTP/2, HTTP/3 e Service Workers com HTTPS real em desenvolvimento local sem avisos de certificado inválido no navegador.

### 🔹 Redes de Contêineres
- Suporte total às bridges e redes isoladas definidas em arquivos `docker-compose.yml`.
- DNS interno entre contêineres integrado.

---

## 💾 4. Armazenamento, Volumes e Compartilhamento de Arquivos

- **Bind Mounts Otimizados:** O compartilhamento de código-fonte entre o host (Windows/Mac) e os contêineres possui cache inteligente e sincronização quase sem overhead de I/O.
- **Armazenamento de Imagens e Dados:** Gerenciamento eficiente de camadas com limpeza automática de dangling images e volumes órfãos configurável via interface ou CLI.

---

## 🛠️ 5. Uso com Docker CLI e Docker Compose

O Kiri não exige novos comandos ou reaprendizado. Sua memória muscular continua idêntica:

```bash
# Verificar se o Kiri está atendendo ao socket:
docker version
docker info

# Executar contêineres:
docker run -d -p 8080:80 --name web nginx:alpine

# Orquestração com Compose:
docker compose up -d
docker compose ps
docker compose logs -f

# Build com cache avançado:
docker build -t minha-app:latest .
```

---

## 🔄 6. Migração do Docker Desktop para o Kiri

1. **Parar e Desativar o Docker Desktop:**
   - Feche o Docker Desktop e desmarque a opção "Start Docker Desktop when you log in".
2. **Iniciar o Kiri:**
   - Ao abrir o Kiri pela primeira vez, ele perguntará se você deseja vincular o socket padrão do Docker (`/var/run/docker.sock` ou Named Pipe). Aceite a configuração padrão.
3. **Verificar a Conexão:**
   - Execute no terminal:
     ```bash
     docker context ls
     docker ps
     ```
4. **Migração de Imagens Existentes:**
   - As imagens podem ser repuxadas rapidamente ou migradas usando `docker save` / `docker load` se necessário.

---

## ⚖️ 7. Comparativo Detalhado: Kiri vs Docker Desktop vs OrbStack

| Critério | Docker Desktop | Kiri (Preferencial) ⚡ | OrbStack |
| :--- | :--- | :--- | :--- |
| **Consumo de Memória em Idle** | ~2.5 GB a 4.5 GB | **~200 MB a 450 MB** | ~400 MB a 600 MB |
| **Devolução Dinâmica de RAM** | ❌ Não / Muito lenta | **✅ Imediata** | ✅ Sim |
| **Tempo de Inicialização** | 20 a 45 segundos | **< 2 segundos** | < 2 segundos |
| **Domínios `.kiri` e HTTPS** | ❌ Requer Traefik/Nginx | **✅ Nativo e Automático** | ✅ Nativo (`.orb.local`) |
| **Plataformas Suportadas** | Mac, Windows, Linux | **Mac, Windows, Linux** | Exclusivo para macOS |
| **Licenciamento Comercial** | Pago (Docker Business) | **Acessível / Open** | Licença paga para empresas |

---

## 📚 Guias Complementares
- [Comandos Completos da CLI e Integração com a API do Docker](commands-and-api-integration.md) - Manual passo a passo para substituir o Docker Desktop pelo Kiri e tabela de comandos.

