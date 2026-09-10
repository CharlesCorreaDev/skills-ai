# Foundry VTT - Model Context Protocol (MCP) Integration Guide 🤖🔌
> *Part of the Master of Foundry VTT Suite by GM Charles Corrêa*

---

## 📌 Visão Geral & Por Que Instalar Servidores MCP para Foundry VTT?

O **Model Context Protocol (MCP)** é o padrão aberto que permite a agentes de IA (como Antigravity, Claude Code, Gemini, Copilot CLI, Hermes Agent e Ollama) conectarem-se diretamente ao ambiente de execução do Foundry Virtual Tabletop, ao sistema de arquivos de dados do usuário (`Data/`) e a instâncias ativas do servidor.

### 🚀 Capacidades Desbloqueadas pelo MCP:
1. **Inspeção de Dados em Tempo Real:** Leitura direta de atores, itens, cenas, tabelas roláveis, diários e compêndios sem necessidade de exportação manual.
2. **Execução Segura de Macros & Scripts:** Teste e validação de scripts de macros diretamente no contexto do mundo do Foundry ou em sandbox LevelDB/NeDB.
3. **Validação de DataModels & Schemas:** Verificação automática de esquemas de `system.json`, `module.json` e classes de dados (`foundry.abstract.DataModel`).
4. **Resolução Rápida de Erros & Conflitos:** Diagnóstico em tempo real inspecionando logs de console, ganchos (`Hooks`) registrados e árvores de dependência do `libWrapper`.
5. **Automação de Criação de Conteúdo:** Geração instantânea de itens de RPG, magias, NPCs e encontros estruturados diretamente nos bancos de dados do mundo ou compêndios `.db`/ClassicLevel.

---

## 🛠️ Servidores MCP Recomendados para Foundry VTT

| Repositório MCP | Autor | Foco Principal & Recursos | Tipo de Conexão |
| :--- | :--- | :--- | :--- |
| [**ninjos-foundry-mcp**](https://github.com/Niclasp1501/ninjos-foundry-mcp) | Niclasp1501 | Consulta e modificação de documentos do mundo, busca semântica em compêndios, execução de comandos e macros. | Conexão HTTP/WebSocket ao Foundry ativo |
| [**foundryvtt-mcp**](https://github.com/laurigates/foundryvtt-mcp) | laurigates | Integração profunda para desenvolvedores de módulos/sistemas, inspeção de pacotes e depuração. | Sistema de Arquivos / API REST |
| [**foundry-vtt-mcp**](https://github.com/adambdooley/foundry-vtt-mcp) | adambdooley | Leitura de pacotes LevelDB/ClassicLevel locais, validação estática de schemas e execução rápida. | Local CLI / Node.js stdio |

---

## 🚨 Protocolo de Intervenção e Solicitação de Credenciais

Quando o desenvolvedor solicitar a instalação, configuração ou conexão a um servidor MCP para o Foundry VTT, **o Agente de IA DEVE seguir este checklist de segurança e permissão**:

### 1. Solicitar Permissão Prévia
O agente deve explicar detalhadamente:
- Qual servidor MCP será instalado/configurado.
- Quais dependências serão necessárias (ex: Node.js, pacotes npm, módulo auxiliar no Foundry).
- Solicitar a aprovação expressa do desenvolvedor antes de executar comandos de instalação.

### 2. Coleta de Informações do Ambiente (Checklist Interativo)
O agente deve solicitar ao desenvolvedor as informações necessárias que não puderem ser auto-detectadas:

1. **Caminho da Pasta de Dados do Foundry (`User Data Path`):**
   - *Windows Padrão:* `%localappdata%\FoundryVTT\Data` (ex: `C:\Users\<Usuario>\AppData\Local\FoundryVTT\Data`)
   - *Linux Padrão:* `~/.local/share/FoundryVTT/Data`
   - *macOS Padrão:* `~/Library/Application Support/FoundryVTT/Data`
2. **URL e Porta da Instância do Foundry VTT:**
   - Local: `http://localhost:30000` (ou porta customizada).
   - Remoto/Servidor: URL completa (ex: `https://meufoundry.dominio.com`).
3. **Chave de Acesso / Senha de Administrador:**
   - Chave de administração do Foundry (`adminPassword`) para gerenciar mundos/pacotes se aplicável.
4. **Mundo Alvo e Usuário (Gamemaster/Assistente):**
   - Nome do Mundo (`worldId`) ativo.
   - Nome de usuário do GM e senha de acesso (se o mundo possuir autenticação por senha).
5. **Módulo Companion no Foundry (se exigido pelo MCP):**
   - Verificar se o módulo auxiliar de integração está instalado e ativo no mundo (`Active Modules`).

---

## ⚙️ Configurações Prontas para Clientes MCP

### 1. Configuração para Antigravity IDE / Claude Desktop (`mcp_config.json`)

```json
{
  "mcpServers": {
    "ninjos-foundry-mcp": {
      "command": "npx",
      "args": ["-y", "ninjos-foundry-mcp"],
      "env": {
        "FOUNDRY_URL": "http://localhost:30000",
        "FOUNDRY_API_KEY": "<INSERIR_API_KEY_SE_APLICAVEL>",
        "FOUNDRY_WORLD": "<NOME_DO_MUNDO>"
      }
    },
    "foundryvtt-mcp": {
      "command": "npx",
      "args": ["-y", "foundryvtt-mcp"],
      "env": {
        "FOUNDRY_DATA_PATH": "C:/Users/<SEU_USUARIO>/AppData/Local/FoundryVTT/Data"
      }
    },
    "adambdooley-foundry-mcp": {
      "command": "node",
      "args": ["C:/caminho/para/adambdooley-foundry-mcp/dist/index.js"],
      "env": {
        "FOUNDRY_DATA_DIR": "C:/Users/<SEU_USUARIO>/AppData/Local/FoundryVTT/Data"
      }
    }
  }
}
```

### 2. Configuração para Claude Code CLI

```bash
claude mcp add ninjos-foundry-mcp npx -y ninjos-foundry-mcp -- --url http://localhost:30000
claude mcp add foundryvtt-mcp npx -y foundryvtt-mcp -- --data-path "C:/Users/<SEU_USUARIO>/AppData/Local/FoundryVTT/Data"
```

---

## 🛡️ Boas Práticas de Segurança e Privacidade

1. **Nunca Versionar Senhas ou Chaves:** Arquivos `.env` ou `mcp_config.json` contendo senhas e chaves de API reais **nunca devem ser commitados no Git**. Adicionar sempre ao `.gitignore`.
2. **Ambiente Local Seguro:** Recomenda-se criar um usuário com privilégios de "Trusted Player" ou "Assistant GM" para testes automatizados, reservando o usuário principal "Gamemaster" para ações críticas.
3. **Backup dos Mundos:** Sempre orientar o desenvolvedor a realizar backup da pasta `worlds/<nome-do-mundo>` antes de executar operações em lote via MCP.

---

## 🔗 Links dos Repositórios Oficiais
- **Ninjos Foundry MCP:** [https://github.com/Niclasp1501/ninjos-foundry-mcp](https://github.com/Niclasp1501/ninjos-foundry-mcp)
- **FoundryVTT MCP (laurigates):** [https://github.com/laurigates/foundryvtt-mcp](https://github.com/laurigates/foundryvtt-mcp)
- **Foundry VTT MCP (adambdooley):** [https://github.com/adambdooley/foundry-vtt-mcp](https://github.com/adambdooley/foundry-vtt-mcp)
