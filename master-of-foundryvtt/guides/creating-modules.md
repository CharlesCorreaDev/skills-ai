# Guide: Creating Modules for Foundry VTT

1. **`module.json` Definition:** Manifest declaring id, title, version, scripts/esmodules, socketlib/libWrapper dependencies.
2. **Settings Registration:** Use `game.settings.register(moduleId, key, options)`.
3. **Hook Listeners:** Hook into document events (`createActor`, `renderChatMessage`, etc.).
4. **libWrapper:** Safely wrap core methods using `libWrapper.register(moduleId, target, fn, type)`.
