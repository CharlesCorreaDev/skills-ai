---
name: docs-for-markdown
description: Universal multi-format document to clean Markdown converter supporting PDF, DOCX, XLSX, PPTX, ODT, ODS, HTML, EPUB, RTF, images (OCR), and audio. Resolves complex layout edge cases, multi-column reading orders, merged spreadsheet cells, broken hyphenation, and noisy headers/footers across Windows, Linux, and macOS. Use when the user wants to convert documents into clean Markdown via Antigravity, Claude Code, Copilot CLI, Hermes Agent, Orca, Gemini, Kilo, NVIDIA, or Ollama, or prepare text for RAG, knowledge bases, and LLM context windows.
---

# Docs for Markdown 📄➡️📝

---

## 🇺🇸 English

### 📌 Overview & Mental Model
**Docs for Markdown** is a cross-platform (Windows, Linux, macOS) document-to-markdown conversion suite for AI agents and LLM workflows. It transforms raw documents (PDF, Office, LibreOffice, HTML, RTF, images, audio) into clean, semantically sound, token-efficient Markdown (`.md`).

Its core mission is to solve edge cases that break downstream AI reasoning: multi-column PDF layouts, false tables, broken word hyphenation across line breaks, buried spreadsheet tabs, and repeated running headers/footers.

### 📚 Supported Format Matrix & Extraction Engines

| Format | Extensions | Primary Engine | Fallback Engine | Dependencies / Binaries |
|---|---|---|---|---|
| **PDF (Digital)** | `.pdf` | `markitdown` / `pdfminer.six` | `pdfplumber` (tables) | `pdfminer.six`, `pdfplumber`, `pypdf` |
| **PDF (Scanned/OCR)** | `.pdf` | `markitdown_ocr` | `tesseract` OCR | `tesseract-ocr`, `Pillow`, `pypdfium2` |
| **Microsoft Word** | `.docx` | `python-docx` / `markitdown` | `pandoc` / `mammoth` | `python-docx`, `mammoth` |
| **Legacy Word** | `.doc` | `pandoc` / `LibreOffice` CLI | `antiword` / `catdoc` | `pandoc`, `soffice` (LibreOffice) |
| **Microsoft Excel** | `.xlsx` | `openpyxl` / `markitdown` | `pandas` | `openpyxl`, `pandas` |
| **Legacy Excel** | `.xls` | `xlrd` / `pandas` | `soffice --convert-to xlsx` | `xlrd` |
| **Microsoft PowerPoint** | `.pptx` | `python-pptx` / `markitdown` | `pandoc` | `python-pptx` |
| **Legacy PowerPoint** | `.ppt` | `soffice` CLI | `pandoc` | `soffice` (LibreOffice) |
| **LibreOffice Writer** | `.odt` | `pandoc` | `odfpy` / `soffice` CLI | `pandoc`, `odfpy` |
| **LibreOffice Calc** | `.ods` | `pandas` (`odf` engine) | `soffice` CLI | `odfpy`, `pandas` |
| **LibreOffice Impress** | `.odp` | `pandoc` | `soffice` CLI | `pandoc` |
| **Rich Text** | `.rtf` | `pandoc` / `striprtf` | `soffice` CLI | `striprtf`, `pandoc` |
| **Web Pages** | `.html`, `.htm` | `markdownify` / `beautifulsoup4`| `html2text` | `markdownify`, `beautifulsoup4` |
| **E-books** | `.epub` | `markitdown` (`ebooklib`) | `pandoc` | `ebooklib`, `beautifulsoup4` |
| **E-mails** | `.msg`, `.eml` | `extract_msg` / `email` | `markitdown` | `extract-msg` |
| **Tabular Data** | `.csv`, `.tsv` | `csv` (Python built-in) / `pandas`| `markitdown` | `pandas` |
| **Images (OCR/EXIF)**| `.jpg`, `.png`, `.tiff`, `.webp` | `Pillow` + `tesseract` | LLM Vision | `Pillow`, `pytesseract` |
| **Audio** | `.mp3`, `.wav`, `.m4a` | `speech_recognition` | Whisper / FFMpeg | `SpeechRecognition`, `pydub`, `ffmpeg` |

### 🔍 Edge Case Resolution & Sanitization Rules

1. **Multi-column PDFs:** Bounding-box spatial sorting prevents horizontal sentence interleaving across columns.
2. **False Tables:** Prevents non-tabular paragraph layout from being corrupted into broken pipe (`|`) tables.
3. **Hyphenation Reassembly:** Reconnects words split by line-ending hyphens (`re.sub(r'(\b\w+)-\s*\n\s*(\w+\b)', r'\1\2', text)`).
4. **Header/Footer Stripping:** Removes repetitive page numbers and running chapter titles.
5. **Spreadsheets:** Iterates across all sheets and resolves merged cell references.

### 🛠️ CLI Usage
```bash
# Check environment
python scripts/check_env.py

# Convert document to file
python scripts/convert_to_md.py "path/to/document.pdf" "output.md"

# Output directly to stdout
python scripts/convert_to_md.py "document.docx"
```

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (pandoc, libreoffice, tesseract), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral & Modelo Mental
A skill **Docs for Markdown** é uma suíte multiplataforma (Windows, Linux, macOS) de conversão de documentos para Markdown limpo voltada a Agentes de IA e pipelines de LLM. Ela transforma documentos brutos (PDF, Office, LibreOffice, HTML, RTF, imagens, áudio) em Markdown (`.md`) semântico e econômico em tokens.

Sua missão central é eliminar problemas de layout que degradam o raciocínio das IAs: páginas PDF com múltiplas colunas, tabelas falsas, palavras hifenizadas quebradas no fim de linha, abas esquecidas em planilhas e cabeçalhos/rodapés repetitivos.

### 📚 Matriz de Formatos Suportados & Motores

| Formato | Extensões | Motor Principal | Mecanismo de Fallback | Pacotes Python / Ferramentas |
|---|---|---|---|---|
| **PDF (Digital)** | `.pdf` | `markitdown` / `pdfminer.six` | `pdfplumber` (tabelas) | `pdfminer.six`, `pdfplumber`, `pypdf` |
| **PDF (Escaneado/OCR)** | `.pdf` | `markitdown_ocr` | `tesseract` OCR | `tesseract-ocr`, `Pillow`, `pypdfium2` |
| **Microsoft Word** | `.docx` | `python-docx` / `markitdown` | `pandoc` / `mammoth` | `python-docx`, `mammoth` |
| **Word Legado** | `.doc` | `pandoc` / `LibreOffice` CLI | `antiword` / `catdoc` | `pandoc`, `soffice` (LibreOffice) |
| **Microsoft Excel** | `.xlsx` | `openpyxl` / `markitdown` | `pandas` | `openpyxl`, `pandas` |
| **Excel Legado** | `.xls` | `xlrd` / `pandas` | `soffice --convert-to xlsx` | `xlrd` |
| **Microsoft PowerPoint** | `.pptx` | `python-pptx` / `markitdown` | `pandoc` | `python-pptx` |
| **PowerPoint Legado** | `.ppt` | `soffice` CLI | `pandoc` | `soffice` (LibreOffice) |
| **LibreOffice Writer** | `.odt` | `pandoc` | `odfpy` / `soffice` CLI | `pandoc`, `odfpy` |
| **LibreOffice Calc** | `.ods` | `pandas` (`odf` engine) | `soffice` CLI | `odfpy`, `pandas` |
| **LibreOffice Impress** | `.odp` | `pandoc` | `soffice` CLI | `pandoc` |
| **Texto Rico** | `.rtf` | `pandoc` / `striprtf` | `soffice` CLI | `striprtf`, `pandoc` |
| **Páginas Web** | `.html`, `.htm` | `markdownify` / `beautifulsoup4`| `html2text` | `markdownify`, `beautifulsoup4` |
| **E-books** | `.epub` | `markitdown` (`ebooklib`) | `pandoc` | `ebooklib`, `beautifulsoup4` |
| **E-mails** | `.msg`, `.eml` | `extract_msg` / `email` | `markitdown` | `extract-msg` |
| **Tabelas Planas** | `.csv`, `.tsv` | `csv` (Python nativo) / `pandas`| `markitdown` | `pandas` |
| **Imagens (OCR / EXIF)**| `.jpg`, `.png`, `.tiff`, `.webp` | `Pillow` + `tesseract` | LLM Vision | `Pillow`, `pytesseract` |
| **Áudios** | `.mp3`, `.wav`, `.m4a` | `speech_recognition` | Whisper / FFMpeg | `SpeechRecognition`, `pydub`, `ffmpeg` |

### 🔍 Resolução de Casos de Borda e Sanitização

1. **PDFs em Múltiplas Colunas:** Ordenação espacial por coordenadas (bounding boxes) que impede a mistura de linhas entre colunas paralelas.
2. **Eliminação de Falsas Tabelas:** Impede que diagramações textuais virem blocos com barras (`|`).
3. **Reconstrução de Palavras Hifenizadas:** Reconecta palavras partidas no fim de linha.
4. **Remoção de Cabeçalhos e Rodapés:** Filtra números de página e títulos repetitivos folha a folha.
5. **Planilhas:** Itera por todas as abas e normaliza células mescladas.

### 🛠️ Uso via CLI
```bash
# Verificar ambiente
python scripts/check_env.py

# Converter documento para arquivo
python scripts/convert_to_md.py "caminho/do/documento.pdf" "saida.md"

# Exibir diretamente no console
python scripts/convert_to_md.py "documento.docx"
```

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro (dependências ausentes, permissões, ferramentas de SO, encoding de caracteres) e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente conforme seu propósito.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir a instalação de binários de sistema (pandoc, libreoffice, tesseract), pacotes globais ou configuração de chaves de API, o agente DEVE explicar o diagnóstico com clareza e solicitar a permissão explícita do desenvolvedor/operador antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar detalhadamente o que foi instalado e configurado para resolver o problema e executar imediatamente um teste de validação (ou solicitar ao operador os dados/arquivos necessários para testar a skill).
