# Cloudflare Security Audit & NVIDIA Auto-Ontology Guidelines
## Diretrizes Universais de Auditoria de Segurança e Prevenção de Alucinação Numérica/Ontológica

Este documento estabelece o protocolo canônico e mandatório para **TODAS as skills do ecossistema Skills AI**, garantindo que:
1. Nenhuma skill produza código, arquitetura, automação ou regras com vulnerabilidades, vazamento de dados ou falhas de controle de acesso (via **Cloudflare Security Audit Skill**).
2. Nenhuma skill invente números, métricas, parâmetros inexistentes, alucinações de campos ou esquemas incoerentes (via **NVIDIA Auto-Ontology Framework**).

---

## 🛡️ Parte 1: Cloudflare Security Audit Skill (`cloudflare/security-audit-skill`)

- **Repositório:** [github.com/cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)
- **Propósito:** Transformar o agente de desenvolvimento em um auditor adversarial rigoroso em 6 fases, provando e testando cada hipótese de vulnerabilidade contra evidências no código-fonte.

### Instalação da Skill:
```bash
# Instalação via npx skills
npx skills@latest add cloudflare/security-audit-skill
```

### O Fluxo Mandatório em 6 Fases:
Sempre que uma nova funcionalidade, script, endpoint, componente ou migração for desenvolvida em qualquer skill (`php-dev-expert`, `python-dev-expert`, `master-of-foundryvtt`, `mcp-builder`, `bootstrap-ux-ui-plus`, `docker-master`, etc.):

1. **Reconhecimento & Mapeamento de Fronteiras:** Identificar superfícies de ataque, pontos de entrada (`$_GET`, `$_POST`, `sys.argv`, inputs de formulário, webhooks, rotas HTTP) e fronteiras de confiança (*trust boundaries*).
2. **Caça Baseada em Cobertura:** Dividir o código em unidades auditáveis (autenticação, autorização, manipulação de arquivos, chamadas de sistema, deserialização).
3. **Validação Adversarial (Prova de Falso-Positivo):** Tentar refutar a vulnerabilidade de forma cética antes de acusar um problema ou afirmar que o código é seguro.
4. **Saída Estruturada:** Registrar as vulnerabilidades encontradas no formato estruturado (CWE, OWASP Top 10, severidade CVSS e trecho exato de código).
5. **Verificação Independente de Registro:** Confirmar se o path de exploração é executável e se os dados do usuário atingem o ponto sensível (*sink*).
6. **Correção Imediata & Relatório Neutro:** Se qualquer falha for detectada, **a skill DEVE refatorar o código imediatamente** implementando validação estrita, prepared statements, escape contextual e sanitização de permissões.

---

## 🧠 Parte 2: NVIDIA Auto-Ontology (`NVIDIA/auto-ontology`)

- **Repositório:** [github.com/NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology)
- **Propósito:** Blindagem semântica contra alucinação de dados, invenção de números inexistentes, tabelas fictícias, colunas fantasmas ou métricas falsas em raciocínios de IA e bancos de dados.

### Instalação da Skill / Ferramenta:
```bash
# Instalação via npx skills ou pip
npx skills@latest add NVIDIA/auto-ontology
# ou como biblioteca de ontologia e ground truth em Python
pip install auto-ontology
```

### Regras Anti-Invenção de Números e Alucinação:
1. **Ground Truth Estrito:** O agente de IA **JAMAIS** deve inventar números, estatísticas, constantes matemáticas, portas de serviço, hashes, scores ou métricas inexistentes.
2. **Ancoragem em Dicionários e Esquemas Reais:** Em tarefas com bancos de dados, APIs ou JSONs, os campos devem ser rigorosamente validados contra a ontologia real do sistema (tabelas reais, tipos de dados canônicos, relacionamentos de chave estrangeira existentes).
3. **Declaração de Incerteza:** Se um dado numérico, estatística ou metadado não estiver explícito na documentação ou no código inspecionado, o agente deve **consultar o arquivo ou explicitar que o valor precisa ser fornecido pelo usuário/ambiente**, sem tentar adivinhar ou extrapolar valores aleatórios.

