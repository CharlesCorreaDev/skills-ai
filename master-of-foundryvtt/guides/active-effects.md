# Complete Guide: Active Effects & Status Conditions in Foundry VTT

> **Official Reference:** [https://foundryvtt.com/article/active-effects/](https://foundryvtt.com/article/active-effects/)

---

## 1. What are Active Effects?
Active Effects dynamically modify Actor and Item data properties during gameplay (e.g. Spells, Buffs, Debuffs, Poison, Wounds).

---

## 2. Change Modes Matrix
Each modification change has a target path, mode, and value:

| Mode | Identifier | Code | Description | Example |
|---|---|---|---|---|
| **CUSTOM** | `CONST.ACTIVE_EFFECT_MODES.CUSTOM` | `0` | Delegated to system-specific custom handler | Special script triggers |
| **MULTIPLY** | `CONST.ACTIVE_EFFECT_MODES.MULTIPLY` | `1` | Multiplies the base attribute by value | `* 2` (Haste double speed) |
| **ADD** | `CONST.ACTIVE_EFFECT_MODES.ADD` | `2` | Adds or subtracts numeric value | `+ 2` (Shield buff to AC) |
| **DOWNGRADE** | `CONST.ACTIVE_EFFECT_MODES.DOWNGRADE` | `3` | Caps attribute if lower than current | Max strength cap |
| **UPGRADE** | `CONST.ACTIVE_EFFECT_MODES.UPGRADE` | `4` | Sets attribute to value if greater than current | `Darkvision 60ft` |
| **OVERRIDE** | `CONST.ACTIVE_EFFECT_MODES.OVERRIDE` | `5` | Replaces the attribute completely | Hard set HP to 0 (Unconscious) |

---

## 3. Creating Active Effects Programmatically
```javascript
const effectData = {
  name: 'Blessing of Valor',
  icon: 'icons/svg/aura.svg',
  changes: [
    {
      key: 'system.attributes.hp.max',
      mode: CONST.ACTIVE_EFFECT_MODES.ADD,
      value: '10',
      priority: 20
    },
    {
      key: 'system.attributes.ac.value',
      mode: CONST.ACTIVE_EFFECT_MODES.ADD,
      value: '2',
      priority: 20
    }
  ],
  duration: {
    rounds: 10,
    seconds: 60
  }
};

await actor.createEmbeddedDocuments('ActiveEffect', [effectData]);
```
