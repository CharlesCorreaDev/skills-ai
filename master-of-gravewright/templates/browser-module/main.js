// main.js - Gravewright VTT Browser Module Lifecycle
// Lifecycle: start(moduleContext), register(registrationContext), stop()
// Ciclo de vida oficial do módulo de navegador no Gravewright

export default {
  start({ styles }) {
    // EN: Attach isolated styles
    // PT-BR: Registra e ativa a folha de estilos isolada
    styles.use("styles.css");
  },

  register({ register }) {
    // EN: Synchronous registration of UI surfaces (actor.directory, actor.sheet, token.sheet, etc.)
    // PT-BR: Registro síncrono de superfícies (actor.directory, actor.sheet, token.sheet, etc.)
    register("actor.directory", async ({ root, api, signal }) => {
      const container = root.ownerDocument.createElement("div");
      container.className = "example-actor-counter-root";
      
      const label = root.ownerDocument.createElement("span");
      label.className = "example-actor-counter-label";
      container.append(label);
      root.append(container);

      const render = (actors) => {
        if (!signal.aborted) {
          label.textContent = `Atores Visíveis: ${actors.length} / Visible: ${actors.length}`;
        }
      };

      // Initial list & reactive event subscription
      render(await api.actors.list());
      api.events.on("actors.changed", (snapshot) => render(snapshot.actors));
    });
  },

  stop() {
    // EN: The host automatically cleans up roots, aborts signal and disposes styles
    // PT-BR: O runtime do Gravewright descarta estilos, raízes e assinaturas automaticamente
  }
};
