---
name: website-for-skill
description: End-to-end orchestration pipeline that crawls live websites, API documentation, and technical portals (including multi-thousand-page manuals) and compiles them into structured, token-efficient AI skills (SKILL.md, chapters/_INDEX.md, cheatsheet, glossary, patterns) with preserved internal links.
---

# Website for Skill 🌐➡️🧠

---

## 🇺🇸 English

### 📌 Objective & Orchestration Model
**Website for Skill** (`v0.3.0-beta`) is the high-level orchestration pipeline that integrates `docs-for-markdown` and `website-for-markdown` to automatically convert live websites, developer documentation, and web portals into **fully structured, production-ready AI Skills**.

### 🏗️ Generated Skill Structure
- **Hardware-Aware Eco Compilation:** Automatically inspects the host CPU and available free RAM, sets process priority to `BELOW_NORMAL_PRIORITY_CLASS` (`nice(10)`), reads only the first 512 bytes per file when indexing titles, streams `_INDEX.md` directly to disk, and forces garbage collection (`gc.collect()`) with micro-pauses so RAM and CPU usage stay minimal even on 12,000-page skills.
- `SKILL.md`: Master bilingual index and domain mental model (automatically groups large sites > 40 pages by category so the context window never overflows).
- `chapters/_INDEX.md`: Complete searchable map of all captured pages and categories (named `_INDEX.md` to avoid case-insensitive collision with `index.md` on Windows/macOS).
- `chapters/*.md`: Individual documentation chapters with preserved filenames and rewritten internal `.md` links.
- `cheatsheet.md`, `glossary.md`, `patterns.md`, `VERSION`.

### 🛠️ CLI Usage
```bash
# Check environment
python Scripts/check_env.py

# Build skill from single documentation URL
python Scripts/build_skill.py "https://foundryvtt.com/api/v12/" "foundryvtt-api-v12" [output_dir]

# Build skill with recursive local crawling (no API key required!)
python Scripts/build_skill.py "https://www.php.net/manual/pt_BR/" "php-manual-pt-br" [output_dir] --crawl --fast --max-pages 200

# Build skill filtering specific sections or from an existing folder of .md files
python Scripts/build_skill.py "https://www.php.net/manual/pt_BR/" "php-manual-pt-br" [output_dir] --crawl --fast --include "security|language" --max-pages 0
python Scripts/build_skill.py "https://www.php.net/manual/pt_BR/" "php-manual-pt-br" [output_dir] --from-dir "./pasta_mds_ja_baixados"
```

---

## 🇧🇷 Português (Brasil)

### 📌 Objetivo & Modelo de Orquestração
O **Website for Skill** (`v0.3.0-beta`) é o orquestrador de alto nível que integra `docs-for-markdown` e `website-for-markdown` para converter automaticamente websites ao vivo, documentações de desenvolvedores e portais técnicos em **Skills Modulares Prontas para Agentes de IA**.

### 🏗️ Estrutura da Skill Gerada
- `SKILL.md`: Índice mestre bilíngue e modelo mental do domínio (agrupa automaticamente sites grandes > 40 páginas por categoria para jamais estourar a janela de contexto).
- `chapters/_INDEX.md`: Mapa completo pesquisável de todas as páginas e categorias capturadas (nomeado `_INDEX.md` para não colidir com `index.md` da página raiz no Windows/macOS).
- `chapters/*.md`: Capítulos preservando os nomes originais e links internos `.md` funcionais entre si.
- `cheatsheet.md`, `glossary.md`, `patterns.md`, `VERSION`.

### 🛠️ Uso via CLI
```bash
# Verificar ambiente
python Scripts/check_env.py

# Gerar skill a partir de uma URL única
python Scripts/build_skill.py "https://foundryvtt.com/api/v12/" "foundryvtt-api-v12" [diretorio_saida]

# Gerar skill varrendo site inteiro localmente (sem precisar de chave Firecrawl!)
python Scripts/build_skill.py "https://www.php.net/manual/pt_BR/" "php-manual-pt-br" [diretorio_saida] --crawl --fast --max-pages 200

# Gerar skill filtrando seções via Regex ou a partir de uma pasta de .md já baixada
python Scripts/build_skill.py "https://www.php.net/manual/pt_BR/" "php-manual-pt-br" [diretorio_saida] --crawl --fast --include "security|language" --max-pages 0
python Scripts/build_skill.py "https://www.php.net/manual/pt_BR/" "php-manual-pt-br" [diretorio_saida] --from-dir "./pasta_mds_ja_baixados"
```
