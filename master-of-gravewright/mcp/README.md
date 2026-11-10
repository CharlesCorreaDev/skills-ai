# Servidor MCP Nativo: Master of Gravewright ⚔️🔌

Este documento descreve o funcionamento, configuração e ferramentas do servidor oficial **Model Context Protocol (MCP)** integrado à skill `master-of-gravewright`.

O **Gravewright MCP Server** permite que Agentes de IA e assistentes de código inspecionem diretamente projetos do Gravewright VTT, validem manifests, criem scaffolds de módulos e consultem a documentação técnica offline através do protocolo padrão JSON-RPC 2.0 (stdio).

---

## 🚀 Ferramentas Expostas pelo MCP Server

1. **`inspect_gravewright_environment`:**
   - Detecta automaticamente a raiz do projeto Gravewright, dependências do Astral `uv`, `manage.py`, subapps instaladas e diretórios de extensões.
2. **`list_installed_modules`:**
   - Escaneia a pasta de extensões (`extensions/` ou caminhos personalizados) e lista todos os módulos ativos, versões, tipos (browser vs django) e compatibilidade.
3. **`validate_module_manifest`:**
   - Valida esquemas de arquivos `manifest.json`, verificando campos obrigatórios (`id`, `title`, `version`), referências de scripts JS e folhas de estilo CSS existentes.
4. **`query_marketplace_packages`:**
   - Consulta o catálogo oficial do marketplace do Gravewright (como `gravewright.translator`, `gravewright.3d-dice`, pacotes de SRD 5e e Savage Worlds SWADE).
5. **`scaffold_extension`:**
   - Gera scaffolding instantâneo de novos módulos de navegador (Vanilla JS/CSS isolado) ou aplicativos Django completos (services, models, views).
6. **`search_offline_docs`:**
   - Pesquisa semântica direta nos 50 manuais técnicos offline em português e inglês sem consumir tokens na internet.

---

## ⚙️ Como Configurar no seu Cliente MCP (Antigravity, Claude Desktop, Cursor)

Adicione a seguinte configuração no seu arquivo de configuração MCP (`mcpServers`):

```json
{
  "mcpServers": {
    "master-of-gravewright-mcp": {
      "command": "python",
      "args": [
        "e:/Projetos_Docker/skills-ai/master-of-gravewright/mcp/gravewright_mcp_server.py"
      ],
      "env": {
        "PYTHONIOENCODING": "utf-8"
      }
    }
  }
}
```

