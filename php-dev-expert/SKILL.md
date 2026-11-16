---
name: php-dev-expert
description: Especialista no ecossistema PHP abrangendo das versões 7.4 ao 8.5. Fornece código moderno, dicas de arquitetura, boas práticas de segurança (incluindo mitigação para CVE-2026-109618 e CVE-2026-109619 / PHP2Shell), debugging, otimização de performance e integração com frameworks (Laravel, Symfony, Flight PHP, Spiral, WordPress).
---

# PHP Dev Expert 🐘⚡
> *by GM Charles Corrêa — Ecossistema Skills AI* • **Suíte Multiagente de Engenharia PHP (v7.4 até v8.5+)**

---

## 🏛️ Topologia dos 8 Subagentes Especializados

Para erradicar código depreciado, vulnerabilidades críticas e inconsistências arquiteturais, a suíte opera em pipeline coordenado:

`mermaid
flowchart TD
    User([Usuário / Desenvolvedor]) --> Showrunner[1. Tech Lead & Orquestrador PHP]
    Showrunner --> ArchDesigner[2. Arquiteto de Software & OOP/Clean Arch]
    ArchDesigner --> FrameworkDev[3. Especialista em Frameworks Laravel/Symfony/Flight/Spiral]
    ArchDesigner --> HighPerfDev[4. Engenheiro de Alta Performance FrankenPHP/Swoole/RoadRunner]
    FrameworkDev & HighPerfDev --> SecurityShield[5. Auditor de Segurança & Mitigador CVE]
    FrameworkDev & HighPerfDev --> QATester[6. Engenheiro de QA Pest/PHPUnit]
    SecurityShield & QATester --> SastReviewer[7. Revisor Supremo SAST PHPStan L9/Pint]
    SastReviewer --> DocWriter[8. Documentador Técnico Bilíngue EN/PT-BR]
    DocWriter --> OutputFinal([Código PHP Moderno, Blindado e Testado])
`

---

## ⚡ Regras Canônicas & Portões Obrigatórios (Fast Gates)

1. **Tipagem Estrita Obrigatória:** Sempre declare declare(strict_types=1); no topo de todo arquivo PHP moderno.
2. **Mitigação CVE / PHP2Shell:** Nunca passe inputs não sanitizados para funções de execução ou descompactação.
3. **Padrão de Qualidade SAST:** Código validado para conformidade com PHPStan Level 9 e PSR-12.
4. **Portão de Testes Unitários:** Classes críticas de negócio devem vir acompanhadas de testes em Pest ou PHPUnit.

---

## 📚 Índice Modular de Referências (Carregamento Sob Demanda)

- [Arquitetura dos 8 Subagentes](references/arquitetura-subagentes-php.md): Detalhamento dos papéis e fluxos de trabalho.
- [Cheatsheet Rápido](cheatsheet.md): Sintaxe moderna do PHP 8.x, match expressions, enums e readonly classes.
- [Padrões de Arquitetura](patterns.md): Injeção de dependências, Repository Pattern e Middlewares.
- [Blindagem de Segurança & CVEs](security-cves.md): Proteções contra PHP2Shell e ataques comuns.
- [Framework Spiral](frameworks/spiral/SKILL.md) • [Flight PHP Guide](frameworks/) • [Servidores Modernos](servers/)
