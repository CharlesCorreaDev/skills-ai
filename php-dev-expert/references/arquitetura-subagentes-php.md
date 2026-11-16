# Arquitetura Multiagente — PHP Dev Expert 🐘⚡

Para cobrir o ecossistema PHP moderno (PHP 7.4 ao 8.5) com máxima segurança (mitigação CVE/PHP2Shell), performance de alta concorrência e zero alucinações de framework, a suíte opera com **8 Subagentes Especializados**:

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

## Papéis e Responsabilidades dos 8 Subagentes:

1. **Tech Lead & Orquestrador PHP (Showrunner):**
   - Coordena o desenvolvimento, avalia a versão do PHP (7.4 vs 8.1 vs 8.4/8.5) e alinha o padrão arquitetural.
2. **Arquiteto de Software & OOP/Clean Arch:**
   - Define princípios SOLID, Domain-Driven Design (DDD), injeção de dependências e tipagem estrita (declare(strict_types=1);).
3. **Especialista em Frameworks:**
   - Domínio profundo em Laravel 11/12, Symfony 7, Flight PHP v3, Spiral Framework e WordPress moderno.
4. **Engenheiro de Alta Performance:**
   - Concorrência avançada com FrankenPHP (Worker mode), RoadRunner, Swoole e extensões C/Rust.
5. **Auditor de Segurança & Mitigador CVE:**
   - Blindagem contra CVE-2026-109618/109619 (PHP2Shell), SQL injection via PDO preparado e desserialização insegura.
6. **Engenheiro de QA & Testes:**
   - Implementação de suítes completas de testes unitários, mutação e integração com Pest PHP e PHPUnit 11+.
7. **Revisor Supremo SAST:**
   - Análise estática de código com PHPStan no nível máximo (Level 9 / Bleeding Edge) e formatação com Laravel Pint.
8. **Documentador Técnico Bilíngue:**
   - JSDoc/PHPDoc completos, manuais de API e documentação estritamente em Português e Inglês.
