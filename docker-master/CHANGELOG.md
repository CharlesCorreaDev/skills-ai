# Changelog - Docker Master 🐳⚡

All notable changes to the `docker-master` skill will be documented in this file.  
*Todas as alterações notáveis na skill `docker-master` serão documentadas neste arquivo.*

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.4.0-beta] - 2026-11-12

### Added / Adicionado
- **Runtimes de Alto Desempenho e Alternativas ao Docker Desktop:**
  - Recomendação ativa e prioritária do **Kiri** (`docs.runkiri.com`) para boot instantâneo, devolução dinâmica de memória RAM e domínios `.kiri` com HTTPS nativo.
  - Integração do **Podman** (`podman.io`) para execução rootless e sem daemon de background.
  - Manual de substituição da Docker Engine API via socket hijacking (`/var/run/docker.sock` e Named Pipe).
- **Criação, Multi-Arch e Publicação de Imagens (`docs/building-and-publishing-images.md`):**
  - Multi-stage builds para Node.js 22 e PHP 8.4 FrankenPHP.
  - Auditoria de camadas com **Dive** (`github.com/wagoodman/dive`).
  - Publicação no Docker Hub, GitHub Packages (GHCR) e Quay.io, com pipeline GitHub Actions pronto para CI/CD.
- **Suíte de Ferramentas Complementares (`docs/companion-tools.md`):**
  - **Lazydocker** (TUI completa no terminal), **Trivy** (varredura de CVEs e segredos), **Hadolint** (linter de Dockerfile), **SlimToolkit** (redução extrema de imagem) e **Testcontainers** (bancos reais efêmeros em testes).
- **Manual de Otimização e Performance (`docs/optimization/performance-and-tuning.md`):**
  - Mitigação de lentidão de I/O de disco no WSL2 (regra do filesystem nativo do Linux vs NTFS).
  - Configuração do `.wslconfig` para limitar RAM do WSL2 e VirtioFS no macOS.
  - Mounts de cache para compiladores e gerenciadores de pacotes (`--mount=type=cache`).
- **Manual Mestre de Kubernetes Local & Multi-Cloud (`docs/kubernetes/kubernetes-local-and-cloud-guide.md`):**
  - **Local:** Kind (multi-node), K3s (ultraleve), Minikube e Podman Play Kube.
  - **Nuvens Públicas:** Azure AKS, Google GKE (Autopilot/Standard), AWS EKS e Oracle OKE (Tier Always Free ARM 24GB).
  - **VPS & Edge:** DigitalOcean DOKS, Hostinger VPS (K3s self-hosted) e Cloudflare Tunnel (`cloudflared`) com SSL gratuito e proteção WAF.
- **Automação & Stacks:**
  - Script detector de ambiente e runtime (`scripts/check_env.py`).
  - Templates de stacks prontas em Compose (`templates/compose/docker-compose-stacks.yml`).
  - Documentação oficial do Docker Engine e Docker Desktop com ajustes de performance (`docs/docker/README.md`).
  - `README.md` completo da skill com comparativos e início rápido.

---

## [0.3.0-beta] - 2026-11-09

### Added / Adicionado
- **Auditoria Adversarial Cloudflare & Anti-Alucinação NVIDIA:** Diretrizes obrigatórias de segurança via cloudflare/security-audit-skill e blindagem contra portas/métricas inexistentes com NVIDIA/auto-ontology.

---

## [0.2.0-beta] - 2026-10-25

### Added / Adicionado
- **Protocolo de Feedback Proativo e Abertura Autônoma de Issues no GitHub:** Geração de documentação técnica bilíngue (EN/PT) e abertura autônoma de issues via `gh issue create` perante bugs, ferramentas ausentes ou limitações no MCP.
- **Protocolo Obrigatório de Verificação e Revisão:** Validação sintática, execução de testes funcionais e integridade de caminhos antes de qualquer entrega.
- **Diretriz de Comentários Bilíngues de Código:** Comentários estritamente necessários devem ser escritos em Inglês e Português.

---

## [0.1.0-beta] - 2026-10-23

### Added / Adicionado
- **Lançamento Inicial da Skill (Beta):**
  - Implementação de regras de detecção de SO e adaptação dinâmica para Docker Compose V2.
  - Guias para multi-stage builds, cache agressivo, rootless containers e Docker Scout.
  - Arquivo `VERSION` para governança de versão e detecção por agentes.
