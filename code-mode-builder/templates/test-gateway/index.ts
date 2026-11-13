import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";
import vm from "node:vm";

// Catalog of upstream functions available to the script
const upstreamTools: Record<string, Function> = {
  "math.add": (a: number, b: number) => a + b,
  "math.multiply": (a: number, b: number) => a * b,
  "system.echo": (msg: string) => `Echo: ${msg}`,
};

const server = new Server(
  { name: "code-mode-gateway", version: "0.1.0" },
  { capabilities: { tools: {} } }
);

server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: "search",
        description: "Search available tools and methods in the upstream catalog. Returns TypeScript signatures.",
        inputSchema: {
          type: "object",
          properties: {
            query: { type: "string", description: "Keyword or domain to search (e.g. 'math', 'system')" }
          },
          required: ["query"]
        }
      },
      {
        name: "execute",
        description: "Executes JavaScript code in an isolated sandbox where upstream tools are global async functions. Returns only the final result.",
        inputSchema: {
          type: "object",
          properties: {
            code: { type: "string", description: "JavaScript code returning a value (e.g. 'const res = tools.math.add(2, 3); return res;')" }
          },
          required: ["code"]
        }
      }
    ]
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;

  if (name === "search") {
    const q = String(args?.query || "").toLowerCase();
    const matches = Object.keys(upstreamTools).filter(k => k.toLowerCase().includes(q));
    return {
      content: [{ type: "text", text: JSON.stringify({ matches }, null, 2) }]
    };
  }

  if (name === "execute") {
    const code = String(args?.code || "");
    const sandbox = {
      tools: {
        math: {
          add: upstreamTools["math.add"],
          multiply: upstreamTools["math.multiply"]
        },
        system: {
          echo: upstreamTools["system.echo"]
        }
      },
      console: { log: (...msgs: any[]) => {} }
    };

    try {
      const script = new vm.Script(`(async () => { ${code} })()`);
      const context = vm.createContext(sandbox);
      const result = await script.runInContext(context, { timeout: 15000 });
      return {
        content: [{ type: "text", text: JSON.stringify({ result }, null, 2) }]
      };
    } catch (err: any) {
      return {
        isError: true,
        content: [{ type: "text", text: JSON.stringify({ error: err.message }, null, 2) }]
      };
    }
  }

  throw new Error(`Tool ${name} not found`);
});

const transport = new StdioServerTransport();
await server.connect(transport);
