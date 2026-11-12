# Docker Master 🐳⚡

> **Especialista em Engenharia de Infraestrutura, Runtimes de Contêineres de Alto Desempenho, Alternativas Leves ao Docker Desktop (com preferência para Kiri e Podman), Otimização com Dive e Orquestração Multiplataforma.**

[![Versão](https://img.shields.io/badge/version-0.4.0--beta-brightgreen.svg)](VERSION)
[![Licença](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-Beta-orange.svg)]()

---

## 🎯 Visão Geral & Filosofia

O **Docker Master** atua como um Engenheiro DevOps especializado em ambientes de contêineres modernos, seguros e altamente eficientes. 

### 💡 Diretriz de Eficiência Energética e Recursos (Anti-Bloatware)
O **Docker Desktop tradicional consome muitos recursos de máquina** (uso pesado de memória RAM persistente, I/O virtualizado lento em binds e alto consumo de bateria em notebooks).

Por essa razão, o Docker Master:
1. **Dá preferência e recomenda o [Kiri (Runkiri)](https://docs.runkiri.com/)**: Runtime ultra-leve, boot instantâneo, devolução dinâmica de memória RAM para o SO e 100% compatível com a CLI do Docker e Docker Compose.
2. **Orienta o uso do [Podman](https://podman.io/)**: Execução rootless por padrão, sem daemon central e com suporte nativo a Pods no padrão Kubernetes.
3. **Aplica o [Dive](https://github.com/wagoodman/dive)**: Inspeção cirúrgica de camadas para caçar espaço desperdiçado e garantir eficiência máxima em builds de imagens.

---

## 📦 Estrutura da Skill

```text
docker-master/
├── SKILL.md                          # Diretrizes completas, regras de SO e protocolos de agente
├── README.md                         # Visão geral, comparativos e guia de início rápido
├── CHANGELOG.md                      # Histórico de alterações e versões
├── VERSION                           # Versão semântica atual da skill
├── runtimes-and-alternatives.md      # Guia aprofundado: Kiri vs Docker Desktop vs Podman vs Dive
├── docs/
│   ├── optimization/
│   │   └── performance-and-tuning.md # Ajustes finos de I/O, WSL2, VirtioFS e memória
│   ├── kubernetes/
│   │   └── kubernetes-local-and-cloud-guide.md # Local (Kind, K3s) e Nuvem (Azure, GCP, AWS, OCI, DO, Hostinger, Cloudflare)
│   ├── docker/README.md              # Documentação oficial do Docker Desktop & Engine
│   ├── companion-tools.md            # Lazydocker, Trivy, Hadolint, SlimToolkit, Testcontainers
│   ├── building-and-publishing-images.md # Guia completo de build, multi-arch e publicação
│   ├── kiri/README.md                # Manual e documentação completa do Kiri
│   └── podman/README.md              # Manual e documentação completa do Podman
├── templates/
│   └── compose/docker-compose-stacks.yml # Stacks completas prontas (PHP 8.4, Node 22, Postgres 17)
├── scripts/
│   └── check_env.py                  # Inspeciona SO, hardware e runtime ativo localmente
├── cheatsheet.md                     # Comandos rápidos de limpeza, compose, scout e debug
├── patterns.md                       # Padrões multi-stage, caching, volumes e rootless
├── ecosystem.md                      # Docker Hub, Build Cloud, Scout e CI/CD
└── glossary.md                       # Termos técnicos essenciais (Daemon, OCI, WSL2, Binds)
```

---

## ⚡ Comparativo Rápido de Runtimes

| Recurso / Métrica | Docker Desktop | Kiri (Preferencial) ⚡ | Podman 🦭 |
| :--- | :--- | :--- | :--- |
| **Consumo de Memória em Idle** | Alto (~2GB a 4GB+) | **Mínimo (~200MB a 500MB)** | Baixo (sem daemon em background) |
| **Recuperação de RAM (Dynamic Memory)** | Lenta / Limitada | **Imediata e Automática** | Por processo individual |
| **Compatibilidade com Docker / Compose** | Nativo | **100% Drop-in replacement** | Via wrapper / podman-compose |
| **Segurança Rootless** | Configuração adicional | Sim | **Nativo por padrão** |
| **Domínios Locais & HTTPS Automáticos** | Não (manual) | **Sim (domínios `.kiri` e TLS nativos)** | Não (manual) |
| **Licenciamento Comercial** | Pago em médias/grandes empresas | Aberto / Flexível | Gratuito e Open Source |

---

## 🚀 Como Começar

### 1. Migrando para o Kiri (Recomendado)
Acesse a [documentação do Kiri](https://docs.runkiri.com/) e instale o runtime para a sua plataforma (macOS / Windows / Linux). 
Uma vez iniciado, você continuará usando os mesmos comandos no terminal:
```bash
# Seus comandos Docker continuam funcionando exatamente iguais:
docker version
docker compose up -d
```

### 2. Inspecionando o Tamanho de Imagens com o Dive
Identifique arquivos temporários não apagados nas camadas intermediárias:
```bash
dive <sua-imagem>:<tag>
```

### 3. Usando Podman para Ambientes Rootless
```bash
alias docker=podman
podman run -d -p 8080:80 nginx:alpine
```

---

## 📚 Documentação Complementar

- [Runtimes & Alternativas](runtimes-and-alternatives.md): Análise detalhada de benchmarks, memória, configuração e migração.
- [Cheatsheet](cheatsheet.md): Tabela de comandos essenciais para o dia a dia.
- [Patterns & Arquitetura](patterns.md): Práticas de multi-stage builds e segurança.
- [Ecosistema Docker](ecosystem.md): Docker Scout, Docker Build Cloud e Hub.
- [Glossário](glossary.md): Definições sobre Daemons, WSL2, Containerd e Mounts.

