# Guide: Troubleshooting & Conflict Isolation

1. **Module Conflict Resolution:**
   - Test in Safe Configuration (`game.settings.set("core", "safeConfiguration", true)`).
   - Use binary isolation (disable half of active modules to pinpoint culprit).
2. **Version Audit:** Verify manifest compatibility fields against current Foundry host version.
3. **Console Log Inspection:** Check F12 Developer Tools for uncaught Promise rejections or deprecated API warnings.
