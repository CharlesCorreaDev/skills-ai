# Servidor MCP Nativo: Master of Gravewright ⚔️🔌

Este documento descreve o funcionamento, configuração e ferramentas do servidor oficial **Model Context Protocol (MCP)** integrado à skill `master-of-gravewright`.

O **Gravewright MCP Server** permite que Agentes de IA e assistentes de código inspecionem diretamente projetos do Gravewright VTT, validem manifests contra o JSON Schema Draft 2020-12 oficial, criem scaffolds de módulos e consultem a documentação técnica offline através do protocolo padrão JSON-RPC 2.0 (stdio).

---

## 🚀 Ferramentas Expostas pelo MCP Server

1. **`inspect_gravewright_environment`:**
   - Detecta automaticamente a raiz do projeto Gravewright, dependências do Astral `uv`, `manage.py`, subapps instaladas e banco de dados SQLite (`data/gravewright.sqlite3`).
2. **`list_installed_modules`:**
   - Escaneia a pasta de módulos oficiais (`data/media/modules/packages/`, `GRAVEWRIGHT_MODULES_ROOT` ou caminhos personalizados) e lista módulos instalados, identificando tipos (`browser`, `django`, `system`, `translation`).
3. **`validate_module_manifest`:**
   - Valida esquemas de arquivos `manifest.json` contra o JSON Schema Draft 2020-12 oficial do Gravewright, checando campos obrigatórios (`id`, `name`, `version`, `sdk`, `entry`), regex de identificador e impedindo propriedades desconhecidas.
4. **`query_marketplace_packages`:**
   - Consulta o catálogo oficial de pacotes com IDs canônicos (como `gravewright.translator`, `gravewright-3d-dice`, `gravewright.5e-srd` e `gravewright.savage-worlds`).
5. **`scaffold_extension`:**
   - Gera scaffolding instantâneo de novos módulos de navegador (ES Module com ciclo `start/register/stop`) ou aplicativos Django completos (`AppConfig`, `models.py`, `services.py` e `migrations/`).
6. **`search_offline_docs`:**
   - Pesquisa semântica direta nos 50 manuais técnicos offline em português e inglês sem consumir tokens na internet.

---

## ⚙️ Como Configurar no seu Cliente MCP (Antigravity, Claude Desktop, Cursor)

Adicione a seguinte configuração no seu arquivo de configuração MCP (`mcpServers`), ajustando o caminho do script conforme seu ambiente:

```json
{
  "mcpServers": {
    "master-of-gravewright-mcp": {
      "command": "python",
      "args": [
        "${workspaceFolder}/master-of-gravewright/mcp/gravewright_mcp_server.py"
      ],
      "env": {
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```
*(Nota: substitua `${workspaceFolder}` pelo caminho absoluto da raiz do repositório onde a skill está localizada caso seu cliente MCP não suporte variáveis de workspace)*
