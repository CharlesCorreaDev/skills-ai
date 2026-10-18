#!/usr/bin/env node
/**
 * Foundry VTT Custom MCP Server & Bridge (Node.js Native)
 * ======================================================
 * Part of the Master of Foundry VTT Suite by GM Charles Corrêa.
 * 
 * An autonomous, zero-external-dependency Model Context Protocol (MCP) server
 * running over standard input/output (stdio JSON-RPC 2.0).
 * Compatible with Node.js v18+.
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');

const SERVER_NAME = "master-of-foundryvtt-mcp";
const SERVER_VERSION = "1.0.0";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
  terminal: false
});

function sendResponse(response) {
  process.stdout.write(JSON.stringify(response) + "\n");
}

function handleListTools() {
  return [
    {
      name: "inspect_foundry_environment",
      description: "Inspects local Foundry VTT installation directory, Data folder, installed systems and active modules.",
      inputSchema: {
        type: "object",
        properties: {
          data_path: {
            type: "string",
            description: "Optional path to the Foundry User Data folder (e.g. C:/Users/<User>/AppData/Local/FoundryVTT/Data)."
          }
        }
      }
    },
    {
      name: "query_official_systems",
      description: "Queries the official Foundry VTT systems directory with pagination support (https://foundryvtt.com/packages/systems?page=N).",
      inputSchema: {
        type: "object",
        properties: {
          page: {
            type: "integer",
            description: "The page number to fetch (starts at 1).",
            default: 1
          },
          search: {
            type: "string",
            description: "Optional keyword to filter systems by name or description."
          }
        }
      }
    },
    {
      name: "query_official_modules",
      description: "Queries the official Foundry VTT modules directory with pagination support (https://foundryvtt.com/packages/modules?page=N).",
      inputSchema: {
        type: "object",
        properties: {
          page: {
            type: "integer",
            description: "The page number to fetch (starts at 1).",
            default: 1
          },
          search: {
            type: "string",
            description: "Optional keyword to filter modules by name or category."
          }
        }
      }
    },
    {
      name: "query_foundry_store",
      description: "Queries the official Foundry VTT Store for commercial/premium rulebooks, adventures and packages (https://www.foundryvtt.store/search?q=...).",
      inputSchema: {
        type: "object",
        properties: {
          query: {
            type: "string",
            description: "The search term (e.g. 'Savage Worlds', 'dnd', 'pathfinder', 'alien')."
          }
        },
        required: ["query"]
      }
    },
    {
      name: "validate_manifest",
      description: "Performs static validation on a system.json or module.json manifest file for Foundry VTT v10-v14 compliance.",
      inputSchema: {
        type: "object",
        properties: {
          manifest_path: {
            type: "string",
            description: "Absolute path to system.json or module.json."
          }
        },
        required: ["manifest_path"]
      }
    },
    {
      name: "generate_foundry_boilerplate",
      description: "Generates production-ready boilerplate code for Foundry VTT (ApplicationV2, TypeDataModel, or socketlib wrapper).",
      inputSchema: {
        type: "object",
        properties: {
          type: {
            type: "string",
            enum: ["application_v2", "type_data_model", "socket_rpc"],
            description: "Type of boilerplate code to generate."
          },
          class_name: {
            type: "string",
            description: "Name of the class (e.g. CharacterDataModel, CustomDiceApp)."
          },
          module_id: {
            type: "string",
            description: "The identifier of the module or system."
          }
        },
        required: ["type", "class_name", "module_id"]
      }
    }
  ];
}

function toolInspectEnvironment(args) {
  let dataPath = args.data_path;
  if (!dataPath) {
    if (process.platform === 'win32') {
      const localAppData = process.env.LOCALAPPDATA || '';
      dataPath = path.join(localAppData, 'FoundryVTT', 'Data');
    } else {
      const home = process.env.HOME || '';
      dataPath = path.join(home, '.local', 'share', 'FoundryVTT', 'Data');
    }
  }

  if (!fs.existsSync(dataPath)) {
    return JSON.stringify({
      status: "warning",
      message: `Foundry Data directory not found at: ${dataPath}. Provide a custom 'data_path' argument if installed in a custom location.`
    }, null, 2);
  }

  const systemsPath = path.join(dataPath, 'systems');
  const modulesPath = path.join(dataPath, 'modules');
  const worldsPath = path.join(dataPath, 'worlds');

  const systems = fs.existsSync(systemsPath) ? fs.readdirSync(systemsPath) : [];
  const modules = fs.existsSync(modulesPath) ? fs.readdirSync(modulesPath) : [];
  const worlds = fs.existsSync(worldsPath) ? fs.readdirSync(worldsPath) : [];

  return JSON.stringify({
    status: "success",
    data_path: dataPath,
    counts: {
      systems: systems.length,
      modules: modules.length,
      worlds: worlds.length
    },
    systems: systems.slice(0, 30),
    worlds: worlds,
    modules_sample: modules.slice(0, 30)
  }, null, 2);
}

function toolQueryOfficialSystems(args) {
  const page = args.page || 1;
  const url = `https://foundryvtt.com/packages/systems?page=${page}`;
  return JSON.stringify({
    status: "success",
    target_url: url,
    page: page,
    instruction: `Fetch HTML from ${url} to inspect available systems on page ${page}.`
  }, null, 2);
}

function toolQueryOfficialModules(args) {
  const page = args.page || 1;
  const url = `https://foundryvtt.com/packages/modules?page=${page}`;
  return JSON.stringify({
    status: "success",
    target_url: url,
    page: page,
    instruction: `Fetch HTML from ${url} to inspect available community modules on page ${page}.`
  }, null, 2);
}

function toolQueryStore(args) {
  const query = args.query || "Savage Worlds";
  const url = `https://www.foundryvtt.store/search?q=${encodeURIComponent(query)}`;
  return JSON.stringify({
    status: "success",
    store_search_url: url,
    query: query,
    instruction: `Consult ${url} for commercial products, adventures, and licensed systems for '${query}'.`
  }, null, 2);
}

function toolValidateManifest(args) {
  const manifestPath = args.manifest_path;
  if (!manifestPath || !fs.existsSync(manifestPath)) {
    return `Manifest file not found: ${manifestPath}`;
  }

  let data;
  try {
    data = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
  } catch (err) {
    return `Invalid JSON syntax: ${err.message}`;
  }

  const errors = [];
  const warnings = [];

  if (!data.id) {
    errors.push("Missing mandatory 'id' field.");
  } else if (!/^[a-z0-9-_]+$/i.test(data.id)) {
    warnings.push(`Package ID '${data.id}' should use alphanumeric characters and hyphens only.`);
  }

  if (!data.compatibility) {
    errors.push("Missing 'compatibility' object (mandatory in v10+).");
  } else {
    if (!data.compatibility.minimum) warnings.push("Missing 'compatibility.minimum' field.");
    if (!data.compatibility.verified) warnings.push("Missing 'compatibility.verified' field.");
  }

  return JSON.stringify({
    valid: errors.length === 0,
    package_id: data.id,
    title: data.title || "",
    version: data.version || "",
    errors,
    warnings
  }, null, 2);
}

function toolGenerateBoilerplate(args) {
  const type = args.type;
  const className = args.class_name || "CustomFeature";
  const moduleId = args.module_id || "my-module";

  let code = "";
  if (type === "application_v2") {
    code = `// ApplicationV2 Boilerplate (Foundry VTT v12+ / v14+)
const { ApplicationV2, HandlebarsApplicationMixin } = foundry.applications.api;

export class ${className} extends HandlebarsApplicationMixin(ApplicationV2) {
  static DEFAULT_OPTIONS = {
    id: "${moduleId}-${className.toLowerCase()}",
    classes: ["${moduleId}", "${className.toLowerCase()}"],
    tag: "form",
    window: {
      title: "${className}",
      icon: "fas fa-dice-d20",
      resizable: true
    },
    position: {
      width: 540,
      height: "auto"
    },
    form: {
      handler: ${className}._onSubmitForm,
      closeOnSubmit: false
    }
  };

  static PARTS = {
    form: {
      template: "modules/${moduleId}/templates/${className.toLowerCase()}.hbs"
    }
  };

  async _prepareContext(options) {
    const context = await super._prepareContext(options);
    context.user = game.user;
    context.isGM = game.user.isGM;
    return context;
  }

  static async _onSubmitForm(event, form, formData) {
    const data = formData.object;
    ui.notifications.info(\`\${this.title} submitted successfully!\`);
  }
}`;
  } else if (type === "type_data_model") {
    code = `// TypeDataModel Boilerplate (Foundry VTT v11+ / v14+)
export class ${className} extends foundry.abstract.TypeDataModel {
  static defineSchema() {
    const fields = foundry.data.fields;
    return {
      hp: new fields.SchemaField({
        value: new fields.NumberField({ required: true, integer: true, min: 0, initial: 10 }),
        max: new fields.NumberField({ required: true, integer: true, min: 0, initial: 10 })
      }),
      biography: new fields.HTMLField({ required: false, initial: "" }),
      level: new fields.NumberField({ required: true, integer: true, min: 1, max: 20, initial: 1 })
    };
  }

  prepareDerivedData() {
    super.prepareDerivedData();
  }
}`;
  } else {
    code = `// Socket RPC Boilerplate (socketlib & native fallback)
export class ${className} {
  static socket = null;

  static initialize() {
    if (typeof socketlib !== "undefined") {
      this.socket = socketlib.registerModule("${moduleId}");
      this.socket.register("executeGmTask", this._handleGmTask);
    } else {
      game.socket.on("module.${moduleId}", this._handleNativeSocket.bind(this));
    }
  }

  static async requestGmAction(payload) {
    if (this.socket) {
      return await this.socket.executeAsGM("executeGmTask", payload);
    } else {
      game.socket.emit("module.${moduleId}", { action: "executeGmTask", payload });
    }
  }

  static async _handleGmTask(payload) {
    if (!game.user.isGM) return;
    console.log("[${moduleId}] GM Task executed:", payload);
    return { success: true };
  }

  static _handleNativeSocket(data) {
    if (game.user.isGM && data.action === "executeGmTask") {
      this._handleGmTask(data.payload);
    }
  }
}`;
  }

  return JSON.stringify({ status: "success", generated_code: code }, null, 2);
}

rl.on('line', (line) => {
  const trimmed = line.trim();
  if (!trimmed) return;

  let request;
  try {
    request = JSON.parse(trimmed);
  } catch (e) {
    return;
  }

  const { id, method, params } = request;

  if (method === "initialize") {
    sendResponse({
      jsonrpc: "2.0",
      id,
      result: {
        protocolVersion: "2024-11-05",
        capabilities: { tools: {} },
        serverInfo: {
          name: SERVER_NAME,
          version: SERVER_VERSION
        }
      }
    });
  } else if (method === "tools/list") {
    sendResponse({
      jsonrpc: "2.0",
      id,
      result: {
        tools: handleListTools()
      }
    });
  } else if (method === "tools/call") {
    const toolName = params.name;
    const toolArgs = params.arguments || {};

    try {
      let content = "";
      if (toolName === "inspect_foundry_environment") {
        content = toolInspectEnvironment(toolArgs);
      } else if (toolName === "query_official_systems") {
        content = toolQueryOfficialSystems(toolArgs);
      } else if (toolName === "query_official_modules") {
        content = toolQueryOfficialModules(toolArgs);
      } else if (toolName === "query_foundry_store") {
        content = toolQueryStore(toolArgs);
      } else if (toolName === "validate_manifest") {
        content = toolValidateManifest(toolArgs);
      } else if (toolName === "generate_foundry_boilerplate") {
        content = toolGenerateBoilerplate(toolArgs);
      } else {
        sendResponse({
          jsonrpc: "2.0",
          id,
          error: { code: -32601, message: `Tool '${toolName}' not found.` }
        });
        return;
      }

      sendResponse({
        jsonrpc: "2.0",
        id,
        result: {
          content: [{ type: "text", text: content }]
        }
      });
    } catch (err) {
      sendResponse({
        jsonrpc: "2.0",
        id,
        error: { code: -32000, message: err.message }
      });
    }
  } else if (method === "notifications/initialized") {
    // Handshake confirmation notification
  } else {
    sendResponse({
      jsonrpc: "2.0",
      id,
      error: { code: -32601, message: `Method '${method}' not found.` }
    });
  }
});
