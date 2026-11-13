import { defineWorker } from "@notionhq/workers";

/**
 * Second Brain Plus - Serverless Notion Worker
 * Worker serverless para automação de memória, compilação de ADRs e gatilhos de agentes.
 */
export default defineWorker({
  name: "second-brain-sync-worker",

  // Triggered when a new page is created in any database
  async onPageCreated({ page, notion }) {
    console.log(`[Second Brain Worker] Nova página detectada: ${page.id}`);

    // If title has [ADR], auto-tag status
    const titleObj = page.properties["Title"] || page.properties["Name"];
    const titleText = titleObj?.title?.[0]?.plain_text || "";

    if (titleText.startsWith("[ADR]")) {
      console.log(`[Second Brain Worker] Auto-classificando ADR: ${titleText}`);
      await notion.pages.update({
        page_id: page.id,
        properties: {
          "Status": { select: { name: "Proposed" } }
        }
      });
    }
  },

  // Triggered when properties change (e.g. project marked completed)
  async onPropertyChanged({ page, property, previousValue, currentValue, notion }) {
    if (property === "Status" && currentValue?.select?.name === "Completed") {
      console.log(`[Second Brain Worker] Projeto concluído: ${page.id}. Disparando arquivamento.`);
    }
  }
});
