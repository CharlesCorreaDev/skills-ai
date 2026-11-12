# Ecossistema de Ferramentas Complementares de Contêineres 🛠️⚡

> **Objetivo:** Integrar as ferramentas mais consagradas e modernas da comunidade Open Source para serem usadas em conjunto com **Docker, Kiri e Podman**, elevando a produtividade, a segurança, o monitoramento e a observabilidade do desenvolvedor.

---

## 🧭 1. Navegação de Terminal e Gestão Interativa (TUI)

### 🐙 **Lazydocker** ([github.com/jesseduffield/lazydocker](https://github.com/jesseduffield/lazydocker))
- **O que é:** Uma interface de terminal (TUI) completa e ultra-rápida escrita em Go para gerenciar contêineres, imagens, volumes e redes com atalhos de teclado.
- **Por que usar:** Elimina a necessidade de abrir interfaces gráficas pesadas como Docker Desktop ou Portainer. Você visualiza gráficos de CPU/RAM em tempo real, navega pelos logs de múltiplos contêineres e reinicia serviços com uma única tecla.
- **Como usar no Kiri/Podman:**
  ```bash
  # Instalação rápida:
  # macOS: brew install lazydocker
  # Windows: scoop install lazydocker / winget install jesseduffield.lazydocker
  # Linux: script curl oficial
  lazydocker
  ```

### 🚢 **Oxker** ([github.com/mrjackwills/oxker](https://github.com/mrjackwills/oxker))
- **O que é:** Um TUI alternativo construído em **Rust**, focado em latência zero e consumo irrisório de CPU/RAM para monitorar contêineres.

---

## 🛡️ 2. Varredura de Vulnerabilidades & Segurança (SAST / CVE Scan)

### 🔒 **Trivy** ([github.com/aquasecurity/trivy](https://github.com/aquasecurity/trivy))
- **O que é:** O scanner de vulnerabilidades (CVEs), segredos vazados e misconfigurations mais popular e rápido do mundo, mantido pela Aqua Security.
- **Por que usar:** Analisa a imagem antes de fazer o push para o Docker Hub ou GHCR, garantindo que você não está enviando pacotes do Linux ou bibliotecas do Node/Python/PHP com brechas críticas conhecidas.
- **Comandos essenciais:**
  ```bash
  # Varrer uma imagem local por vulnerabilidades críticas:
  trivy image --severity HIGH,CRITICAL meu-app:1.0.0

  # Varrer o Dockerfile em busca de más práticas de segurança:
  trivy config ./Dockerfile
  ```

### 🔬 **Hadolint** ([github.com/hadolint/hadolint](https://github.com/hadolint/hadolint))
- **O que é:** Um linter rigoroso e inteligente para `Dockerfile` que analisa sintaxe e enforça as melhores práticas da documentação do Docker.
- **Comando:**
  ```bash
  hadolint Dockerfile
  ```

---

## ⚡ 3. Atualização e Automação de Contêineres

### 🔄 **Watchtower** ([github.com/containrrr/watchtower](https://github.com/containrrr/watchtower))
- **O que é:** Um contêiner que monitora automaticamente seus outros contêineres em execução e os atualiza de forma autônoma sempre que uma nova versão da imagem for publicada no registro.
- **Exemplo de uso com Kiri / Podman:**
  ```bash
  docker run -d \
    --name watchtower \
    -v /var/run/docker.sock:/var/run/docker.sock \
    containrrr/watchtower --interval 3600
  ```

---

## 🧹 4. Limpeza e Diagnóstico Avançado

### 🔍 **Dive** ([github.com/wagoodman/dive](https://github.com/wagoodman/dive))
- **O que é:** Análise de camadas, cálculo de score de eficiência e identificação de arquivos mortos em imagens OCI.
- **Uso:** `dive meu-app:latest`

### 🩺 **Docker-Slim / SlimToolkit** ([github.com/slimtoolkit/slim](https://github.com/slimtoolkit/slim))
- **O que é:** Uma ferramenta que analisa dinamicamente uma aplicação e reduz drasticamente o tamanho da imagem final (às vezes em até **30x**), removendo executáveis e bibliotecas do SO que nunca são chamadas pela sua aplicação.
- **Comando:**
  ```bash
  slim build --target meu-app:latest --tag meu-app:slim
  ```

---

## 🚀 5. Testes Automatizados com Contêineres Reais

### 🧪 **Testcontainers** ([testcontainers.com](https://testcontainers.com/))
- **O que é:** Biblioteca para Java, Node.js, Python, Go e PHP que inicializa bancos de dados reais (Postgres, MySQL, Redis, RabbitMQ) dentro de contêineres durante a execução da suíte de testes unitários/integração e os destrói no final.
- **Compatibilidade:** Funciona 100% com o Kiri e Podman via o socket padrão!

---

## 📊 Matriz de Ferramentas Recomendadas

| Ferramenta | Categoria | Tecnologia | Objetivo Principal |
| :--- | :--- | :--- | :--- |
| **Lazydocker** | TUI / Gerenciamento | Go | Dashboard interativo no terminal sem precisar de Docker Desktop |
| **Trivy** | Segurança / CVEs | Go | Detectar brechas de segurança e segredos vazados em imagens |
| **Hadolint** | Linting de Dockerfile | Haskell | Enforçar boas práticas de Dockerfile antes do build |
| **Dive** | Otimização de Imagens | Go | Caçar espaço desperdiçado entre camadas |
| **Watchtower** | Automação / CD | Go | Atualizar contêineres automaticamente quando a imagem muda |
| **Testcontainers** | Qualidade de Software | Multi-linguagem | Subir bancos reais em contêineres efêmeros durante testes |

