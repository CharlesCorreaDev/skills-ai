# Arquitetura dos 11 Subagentes Especializados — PHP Dev Expert 🐘⚡
## 11 Specialized Subagents Architecture — PHP Dev Expert 🐘⚡

A suíte **PHP Dev Expert** opera sob o padrão de Engenharia Federada em Linha de Montagem, garantindo código moderno, estritamente tipado, imune a CVEs (PHP2Shell), de alta concorrência e com cobertura de testes.

The **PHP Dev Expert** suite operates under a federated assembly line engineering model, ensuring modern, strictly typed, CVE-hardened (PHP2Shell mitigation), high-concurrency code with robust test coverage.

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor / User]) --> Showrunner[1. Tech Lead & Orquestrador PHP]
    Showrunner --> SpecArchitect[2. Specs & Clean Architecture/DDD]
    SpecArchitect --> FrameworkDev[3. Frameworks Laravel/Symfony/Flight/Spiral]
    SpecArchitect --> HighPerfDev[4. Alta Performance FrankenPHP/RoadRunner]
    SpecArchitect --> LegacyModernizer[5. Modernização Legada v7.4 a v8.5]
    FrameworkDev & HighPerfDev & LegacyModernizer --> SecurityShield[6. Mitigador CVE & PHP2Shell]
    FrameworkDev & HighPerfDev & LegacyModernizer --> QATester[7. QA & Testes Pest/PHPUnit]
    SecurityShield & QATester --> SastAuditor[8. Auditor SAST PHPStan L9/Pint]
    SastAuditor --> DevopsDatabase[9. Banco de Dados & CI/CD]
    DevopsDatabase --> VersionRelease[10. Guardião SemVer 2.0.0]
    VersionRelease --> TechnicalWriter[11. Documentador Bilíngue EN/PT-BR]
    TechnicalWriter --> SpecArchitect
    SpecArchitect --> OutputFinal([Código PHP Moderno, Blindado e Testado])
`

---

## 🇧🇷 Português (Brasil) — Papéis e Responsabilidades dos 11 Subagentes

1. **Tech Lead & Orquestrador PHP (Showrunner):** Entrevista o desenvolvedor via grill-me, define versões de runtime (7.4 a 8.5) e gerencia os ciclos dos subagentes.
2. **Engenheiro de Specs & Clean Architecture (DDD/SOLID):** Modela diagramas, contratos de interfaces, DTOs imutáveis e regras de negócio desacopladas.
3. **Especialista em Frameworks:** Implementações canônicas para Laravel 11/12, Symfony 7, Flight PHP v3, Spiral Framework e WordPress moderno.
4. **Engenheiro de Alta Performance (Worker Mode & Async):** Concorrência extrema com FrankenPHP (100% Go runtime), RoadRunner, Swoole e caching Redis.
5. **Especialista em Migração & Modernização:** Converte código PHP legado (7.4, 8.0) para sintaxe idiomática moderna 8.3/8.4/8.5 (match, enums, property promotion, readonly).
6. **Auditor de Segurança & Mitigador CVE:** Blindagem estrita contra CVE-2026-109618/109619 (PHP2Shell), SQL injection via PDO e upload seguro.
7. **Engenheiro de QA & Testes Automatizados:** Testes unitários, mutação e feature tests utilizando Pest PHP e PHPUnit 11+.
8. **Auditor Supremo SAST (Portão Obrigatório):** Análise estática profunda com PHPStan Level 9 (ou Bleeding Edge) e conformidade PSR-12 via Laravel Pint.
9. **Especialista em Banco de Dados & CI/CD:** Migrations seguras, otimização de índices em MySQL/PostgreSQL e workflows GitHub Actions.
10. **Guardião de Versões & SemVer 2.0.0:** Controle rigoroso de releases de bibliotecas e pacotes Composer conforme [SemVer 2.0.0 PT-BR](https://semver.org/lang/pt-BR/).
11. **Redator Técnico & Documentador Bilíngue:** Gera PHPDoc completo, especificações OpenAPI e manuais técnicos em Português e Inglês.

---

## 🇺🇸 English — Roles and Responsibilities of the 11 Subagents

1. **Tech Lead & PHP Orchestrator (Showrunner):** Gathers specifications via grill-me, selects target runtime versions (7.4 through 8.5), and coordinates subagents.
2. **Specs & Clean Architecture Engineer (DDD/SOLID):** Authors architectural RFCs, strict interface contracts, immutable DTOs, and decoupled domain logic.
3. **Modern Frameworks Specialist:** Canonical designs across Laravel 11/12, Symfony 7, Flight PHP v3, Spiral Framework, and modern WordPress.
4. **High-Performance Concurrency Engineer:** Powers high-throughput deployments with FrankenPHP (Go worker mode), RoadRunner, Swoole, and Redis caching.
5. **Legacy Modernization Specialist:** Refactors legacy codebases (7.4, 8.0) to idiomatic PHP 8.3/8.4/8.5 features (enums, match expressions, readonly classes).
6. **Security Auditor & CVE Mitigator:** Deep hardening against CVE-2026-109618/109619 (PHP2Shell), SQL injection, deserialization, and upload vulnerabilities.
7. **QA & Automated Testing Engineer:** Comprehensive unit, feature, and mutation testing using Pest PHP and PHPUnit 11+.
8. **Supreme SAST Auditor (Mandatory Quality Gate):** Strict static analysis with PHPStan Level 9 / Bleeding Edge and PSR-12 formatting via Laravel Pint.
9. **Database & DevOps Specialist:** Safe migrations, PostgreSQL/MySQL indexing strategies, and automated GitHub Actions CI/CD pipelines.
10. **SemVer 2.0.0 & Composer Release Guardian:** Manages SemVer releases and Composer library dependencies per [semver.org](https://semver.org/).
11. **Bilingual Technical Writer (EN / PT-BR):** Produces exhaustive PHPDoc, OpenAPI specs, and user manuals in both English and Brazilian Portuguese.
