# Guide: Creating Game Systems for Foundry VTT

1. **`system.json` Definition:** Manifest declaring id, title, version, compatibility (minimum/verified), esmodules, and styles.
2. **DataModels:** Define `TypeDataModel` schemas for Actor and Item types under `src/module/data/`.
3. **Actor & Item Sheets:** Extend `ActorSheet` (or `ActorSheetV2` in v12+) to render Handlebars templates.
4. **Registration:** Register sheets and models in `Hooks.once('init')`.
