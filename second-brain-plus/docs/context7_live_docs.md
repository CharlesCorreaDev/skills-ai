# Real-Time API Docs with Upstash Context7 📚⚡
# Documentação Atualizada em Tempo Real com Upstash Context7

> **Second Brain Plus Technical Specification / Especificação Técnica do Second Brain Plus**  
> *Bilingual Documentation: English (EN) and Portuguese (PT-BR) / Documentação Bilíngue: Inglês e Português*

---

## 🇺🇸 English

### 1. The Stale API Hallucination Bottleneck
One of the most persistent causes of agent hallucination is **stale training data**:
- LLMs routinely hallucinate deprecated syntax, non-existent methods, or obsolete configuration options when working with fast-moving frameworks (e.g., Next.js 15, Tailwind v4, Pydantic v2, Python 3.14).

### 2. Context7 Integration (`upstash/context7`)
Upstash Context7 delivers version-specific, real-time documentation directly into the agent's context through its **Model Context Protocol (MCP)** server and `ctx7` CLI.

### 3. Role in the Second Brain Plus Ecosystem
1. **Verification Before Coding (Karpathy Rule #1):**
   Before writing code that relies on third-party libraries, the agent checks Context7 to retrieve the canonical, modern syntax.
2. **Semantic Memory Persistence:**
   The retrieved documentation snippet is stored in `.second-brain/3-Resources/cheatsheets/` and cataloged in the **Notion Resources Database**, preventing future redundant lookups.
3. **Trigger Prompt:**
   Simply appending `use context7` or invoking the MCP server fetches verified reference documents.

```bash
# Add Context7 MCP server to Claude Code
claude mcp add context7 -- npx -y @upstash/context7-mcp

# Add to Cursor / Claude Desktop (mcpServers config)
{
  "mcpServers": {
    "context7": {
      "url": "https://mcp.context7.com/mcp"
    }
  }
}
```

---

## 🇧🇷 Português

### 1. O Gargalo da Alucinação por Bibliotecas Desatualizadas
Um dos maiores motivos de falhas e alucinações em agentes de codificação são os **dados de treinamento defasados**:
- Modelos fundacionais frequentemente inventam métodos que não existem mais ou usam padrões obsoletos em bibliotecas com atualizações frequentes (Next.js 15, Tailwind v4, Pydantic v2, Python 3.14).

### 2. Integração com Context7 (`upstash/context7`)
O Upstash Context7 fornece documentações oficiais, na versão exata do seu projeto, diretamente para os agentes via **Model Context Protocol (MCP)** ou pelo CLI `ctx7`.

### 3. Papel no Ecossistema Second Brain Plus
1. **Pense Antes de Codificar (Lei 1 de Karpathy):**
   Antes de implementar código com dependências externas, o agente consulta o Context7 para verificar a assinatura atualizada da API.
2. **Persistência na Memória Semântica:**
   Os snippets e guias resgatados são gravados em `.second-brain/3-Resources/cheatsheets/` e indexados no **Banco de Recursos do Notion**, evitando consumo desnecessário de tokens em turnos futuros.
3. **Gatilho Operacional:**
   Adicionar `use context7` no prompt ou consultar o servidor MCP garante respostas 100% ancoradas em código real e moderno.
