# SOTA AI Agent Architecture & Companion Skills Standard 🧠⚡
# Padrões Canônicos de Arquitetura de Agentes, Memória e Engenharia de IA

> *Módulo Integrado para o Ecossistema de Skills (`bootstrap-ux-ui-plus`, `master-of-foundryvtt`, `php-dev-expert`, `python-dev-expert`)*  
> **Companheiros Oficiais & Ferramentas SOTA:**
> 1. **Superpowers** ([github.com/obra/superpowers](https://github.com/obra/superpowers)): Capacidades de extensão e ferramentas para agentes avançados.
> 2. **Karpathy Guidelines** ([github.com/multica-ai/andrej-karpathy-skills/.../SKILL.md](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md)): Disciplina de engenharia pragmática, código mínimo e validação sistemática.
> 3. **Claude Octopus** ([github.com/nyldn/claude-octopus](https://github.com/nyldn/claude-octopus)): Orquestração multi-modelo e consenso de validação antes de entregar código.
> 4. **AgentMemory** ([github.com/rohitg00/agentmemory](https://github.com/rohitg00/agentmemory)): Camada de memória persistente via busca híbrida (BM25 + vetorial) via MCP.
> 5. **Déjà Vu** ([github.com/vshulcz/deja-vu](https://github.com/vshulcz/deja-vu)): Memória local com indexação instantânea de transcrições de sessões anteriores sem dependências.
> 6. **Motion Design:** [Claude-Motion](https://github.com/whaleyxbt/claude-motion) para animações refinadas e autocorreção visual de interfaces.
> 7. **Dicionário de Conceitos de AI Coding (Matt Pocock):**
>    - [Handoff](https://github.com/mattpocock/dictionary-of-ai-coding/blob/main/dictionary/Handoff.md): Transferência de contexto limpo entre sessões e agentes sem vazamento de ruído.
>    - [Filesystem](https://github.com/mattpocock/dictionary-of-ai-coding/blob/main/dictionary/Filesystem.md): O sistema de arquivos como a única fonte de verdade duradoura para o agente.
>    - [Design Concept](https://github.com/mattpocock/dictionary-of-ai-coding/blob/main/dictionary/Design%20concept.md): O modelo mental formal antes de qualquer escrita de código.
>    - [Context](https://github.com/mattpocock/dictionary-of-ai-coding/blob/main/dictionary/Context.md) & [Contextual Knowledge](https://github.com/mattpocock/dictionary-of-ai-coding/blob/main/dictionary/Contextual%20knowledge.md): Conhecimento factual sob demanda vs tokens efêmeros.
>    - [Input Tokens](https://github.com/mattpocock/dictionary-of-ai-coding/blob/main/dictionary/Input%20tokens.md): Orçamento estrito de tokens para evitar alucinação e saturação.
>    - [MCP (Model Context Protocol)](https://github.com/mattpocock/dictionary-of-ai-coding/blob/main/dictionary/MCP.md): O protocolo aberto de interoperabilidade entre modelos e ferramentas locais.
>    - [Software Factory](https://github.com/mattpocock/dictionary-of-ai-coding/blob/main/dictionary/Software%20factory.md): A esteira automatizada e padronizada de produção de software por IA.

---

## 🇺🇸 Core Principles for Coding Agents
1. **Pragmatic Simplicity (Karpathy Rules):** Write readable, self-contained code. Do not add speculative abstractions. Test before claiming victory.
2. **Context Economics:** Keep prompt inputs focused. Store long-term knowledge on disk (`Filesystem as state`).
3. **Multi-Model Consensus (Octopus Pattern):** Verify critical logic, security patterns, and migrations against multiple perspectives.
4. **Persistent Memory Integration (AgentMemory / Déjà Vu):** Leverage past session decisions, learned preferences, and previous transcripts to avoid asking the user what was already solved.
5. **Polished Motion (Claude-Motion):** When generating animations, use tasteful, physics-based easing with full accessibility fallbacks.
