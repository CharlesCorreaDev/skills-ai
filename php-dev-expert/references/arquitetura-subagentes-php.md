# Arquitetura dos 11 Subagentes Especializados — PHP Dev Expert 🐘⚡
## Suíte de Engenharia, Performance e Segurança para PHP (v7.4 até v8.5+) — by GM Charles Corrêa

A suíte **PHP Dev Expert** opera sob o padrão de **Engenharia Federada em Linha de Montagem**, garantindo código moderno, estritamente tipado, imune a CVEs (PHP2Shell), de alta concorrência e com cobertura de testes:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Tech Lead & Orquestrador PHP]
    
    Showrunner --> SpecArchitect[2. Engenheiro de Specs & Clean Architecture/DDD]
    
    SpecArchitect --> FrameworkDev[3. Especialista em Frameworks Laravel/Symfony/Flight/Spiral]
    SpecArchitect --> HighPerfDev[4. Engenheiro de Alta Performance FrankenPHP/Swoole/RoadRunner]
    SpecArchitect --> LegacyModernizer[5. Especialista em Migração & Modernização v7.4 a v8.5]
    
    FrameworkDev & HighPerfDev & LegacyModernizer --> SecurityShield[6. Auditor de Segurança & Mitigador CVE/PHP2Shell]
    FrameworkDev & HighPerfDev & LegacyModernizer --> QATester[7. Engenheiro de QA & Testes Pest/PHPUnit]
    
    SecurityShield & QATester --> SastAuditor[8. Auditor Supremo SAST PHPStan L9/Pint]
    
    SastAuditor --> DevopsDatabase[9. Especialista em Banco de Dados & CI/CD Docker/MySQL/PostgreSQL]
    
    DevopsDatabase --> VersionRelease[10. Guardião de Versões & SemVer 2.0.0]
    
    VersionRelease --> TechnicalWriter[11. Redator Técnico & Documentador Bilíngue EN/PT-BR]
    
    TechnicalWriter --> SpecArchitect
    SpecArchitect --> OutputFinal([Código PHP Moderno, Blindado, Testado e Homologado])
`

---

## 🏛️ Papéis e Responsabilidades dos 11 Subagentes

1. **Tech Lead & Orquestrador PHP (Showrunner):** Entrevista o desenvolvedor via grill-me, define versões de runtime (7.4 a 8.5) e gerencia os ciclos dos subagentes.
2. **Engenheiro de Specs & Clean Architecture (DDD/SOLID):** Modela diagramas, contratos de interfaces, DTOs imutáveis e regras de negócio desacopladas.
3. **Especialista em Frameworks:** Implementações canônicas para Laravel 11/12, Symfony 7, Flight PHP v3, Spiral Framework e WordPress moderno.
4. **Engenheiro de Alta Performance (Worker Mode & Async):** Concorrência extrema com FrankenPHP (100% Go runtime), RoadRunner, Swoole e caching Redis.
5. **Especialista em Migração & Modernização:** Converte código PHP legado (7.4, 8.0) para sintaxe idiomática moderna 8.3/8.4/8.5 (match, enums, property promotion, readonly).
6. **Auditor de Segurança & Mitigador CVE:** Blindagem estrita contra CVE-2026-109618/109619 (PHP2Shell), SQL injection via PDO e upload seguro.
7. **Engenheiro de QA & Testes Automatizados:** Testes unitários, mutação e feature tests utilizando Pest PHP e PHPUnit 11+.
8. **Auditor Supremo SAST (Portão Obrigatório):** Análise estática profunda com PHPStan Level 9 (ou Bleeding Edge) e conformidade PSR-12 via Laravel Pint.
9. **Especialista em Banco de Dados & CI/CD:** Migrations seguras, otimização de índices em MySQL/PostgreSQL e workflows GitHub Actions.
10. **Guardião de Versões & SemVer 2.0.0:** Controle rigoroso de releases de bibliotecas e pacotes Composer.
11. **Redator Técnico & Documentador Bilíngue:** Gera PHPDoc completo, especificações OpenAPI e manuais técnicos em Português e Inglês.
