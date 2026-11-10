# PHP Developer Expert 🐘⚡

> **Senior Software Engineering, Modern Architecture, Framework Ecosystem, Critical Security (PHP2Shell), PDF Oxide & Web Servers for PHP (v7.4 to v8.5)**  
> *Engenharia de Software Sênior, Arquitetura Moderna, Ecossistema de Frameworks, Segurança Crítica, PDF Oxide e Servidores Web para PHP por GM Charles Corrêa*  
> **Status: Beta (v0.6.0-beta)**

---

## 🇺🇸 English

### 📌 Overview
**PHP Developer Expert** is an advanced AI agent skill and comprehensive technical knowledge base designed for senior software engineers and autonomous AI agents working with the PHP ecosystem across legacy (PHP 7.4) and modern versions (PHP 8.0, 8.1, 8.2, 8.3, 8.4, 8.5).

It integrates modern OOP, MVC/ADR architectures, comprehensive official documentation for **31+ platforms (CMS, LMS, CRM, E-Commerce)**, **10 major frameworks**, **6 web servers**, critical vulnerability shielding (**PHP2Shell / CVE-2026-109618 & CVE-2026-109619**), ultra-fast PDF reading with **PDF Oxide**, and refined interface motion via **Claude-Motion**.

### 🌟 Core Capabilities
1. **Mandatory Version Inquiry (Golden Rule):** The agent ALWAYS identifies or inquires the project's PHP version before generating code to guarantee strict compatibility.
2. **First-Choice PDF Engine (`PDF Oxide`):** Ultra-fast Rust-powered PDF extraction, metadata, and Markdown conversion via PHP FFI (`oxide/pdf-oxide`).
3. **Critical Security & PHP2Shell Defense:** Full mitigations for `CVE-2026-109618` and `CVE-2026-109619` across Docker containers (`php:*-fpm`, `php:*-apache`), legacy runtimes, and PHP-FPM socket configurations.
4. **Comprehensive Framework Docs:** Complete offline Markdown references for Laravel, Symfony, Yii, Spiral, CodeIgniter 4, FuelPHP, Slim 4, FlightPHP 3, and Fat-Free (F3).
5. **Web Server Mastery:** Hardening guides and official docs for Nginx, Caddy, Apache HTTP (2.2 & 2.4), LiteSpeed (LSWS/LSCache), and IIS.
6. **Platform Ecosystem (2,500+ Pages):** WordPress, Moodle 5.0, Joomla, OpenCart, Invoice Ninja, Roundcube, phpMyAdmin, and 24 other platforms.
7. **Modern POO & MVC Architecture:** Full video-course modular guides covering PSR-4, DI containers, ADR, repositories, DTOs, and test-driven design.
8. **Motion Design & UI Animation:** Integration with [Claude-Motion](https://github.com/whaleyxbt/claude-motion) for smooth, GPU-accelerated micro-interactions.

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral
A skill **PHP Developer Expert** é uma suíte completa de engenharia de software sênior para PHP, cobrindo com rigor técnico desde aplicações legadas estruturadas (PHP 7.4) até o ecossistema moderno de alta performance (PHP 8.5).

A skill reúne guias modulares de Orientação a Objetos, arquitetura MVC/ADR limpa, documentações completas de **10 frameworks**, **6 servidores web**, **31 plataformas e ferramentas (2.501 páginas)**, blindagem contra vulnerabilidades críticas (**PHP2Shell**), processamento de PDF de alta performance com **PDF Oxide** e animações refinadas com **Claude-Motion**.

### 🌟 Destaques Principais
- **Regra de Ouro (Versão Obrigatória):** A IA sempre pergunta ou verifica a versão exata do PHP do projeto para não sugerir sintaxes incompatíveis (ex: não sugerir Enums ou Attributes em projetos legados PHP 7.4).
- **Leitura de PDF com PDF Oxide em 1º Lugar:** Extração de texto e metadados ultrarrápida (~0.8ms) via FFI/Rust (`composer require oxide/pdf-oxide`), deixando bibliotecas legadas apenas como fallback.
- **Blindagem Contra PHP2Shell (`CVE-2026-109618` e `CVE-2026-109619`):** Regras de ouro para uploads seguros, proteção de `php.ini`, PHP-FPM e imagens Docker (`php:*-fpm`, `Dockerfile`).
- **Acervo Extensivo de Documentações em Markdown:**
  - **Frameworks:** Laravel, Symfony, Yii, Spiral, CodeIgniter, Slim, FlightPHP, FuelPHP, Fat-Free.
  - **Servidores:** Nginx, Caddy, Apache 2.4/2.2, LiteSpeed, IIS.
  - **Plataformas:** WordPress, Moodle, Invoice Ninja, Roundcube, phpMyAdmin, Matomo, OpenCart, etc.
- **Arquitetura POO & MVC Avançada:** Do Front Controller ao ADR, DTOs, Repository Pattern e Dependency Injection nativo.
- **Motion Design (Claude-Motion):** Criação de interfaces web e dashboards animados com aceleração por GPU e respeito a `prefers-reduced-motion`.

---

## 📁 Estrutura de Arquivos / Folder Structure

```
php-dev-expert/
├── SKILL.md                          # Diretrizes e mandatos mestres para a IA
├── README.md                         # Visão geral completa bilíngue (EN / PT-BR)
├── VERSION                           # Versão semântica atual (0.6.0-beta)
├── CHANGELOG.md                      # Histórico detalhado de versões
├── cheatsheet.md                     # Guia rápido de evolução e comandos PHP
├── glossary.md                       # Dicionário de termos técnicos essenciais
├── patterns.md                       # Padrões de arquitetura e design patterns
├── security-cves.md                  # Análise profunda e mitigação de PHP2Shell
├── php-docs/
│   ├── _INDEX.md                     # Índice geral do manual oficial do PHP
│   └── pdf-oxide-guide.md            # Guia oficial de leitura e metadados com PDF Oxide
├── OOP/                              # Curso modular de Programação Orientada a Objetos
├── MVC/                              # Guia modular completo de Arquitetura MVC/ADR
├── frameworks/                       # Documentações oficiais de 10 frameworks PHP
├── servers/                          # Documentações oficiais de 6 servidores web
├── bootstrap/                        # Documentações de Bootstrap (v3.4, v4.6, v5.3, v6.0)
└── cms/                              # Documentações de 31 plataformas PHP (2.501 páginas)
```

---

## 👨‍💻 Autor / Author
**GM Charles Corrêa**  
- 🌐 Website: [charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 GitHub: [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ Skills AI: [github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)
