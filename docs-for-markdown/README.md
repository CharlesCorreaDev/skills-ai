# Docs for Markdown 📄➡️📝

> **Universal Multi-Format Document to Clean Markdown Converter**  
> *Conversor Universal de Documentos Multiformato para Markdown Limpo*

---

## 🇺🇸 English

### 📌 Overview
**Docs for Markdown** is a robust, cross-platform Python toolchain designed to convert virtually any document format into clean, well-structured, and semantically sound **Markdown (`.md`)**. 

It serves as the foundational ingestion layer for AI agents, RAG (Retrieval-Augmented Generation) systems, and knowledge bases, resolving edge cases like multi-column PDFs, false tables, broken hyphenation, embedded Excel worksheets, speaker notes in PowerPoint, and LibreOffice ODF formats.

---

### 🌐 Supported Formats & Extraction Engines

| Format Category | Extensions | Primary Engine | Fallback / Alternative |
|---|---|---|---|
| **PDF (Digital)** | `.pdf` | `markitdown` / `pdfminer.six` | `pdfplumber` (tables) / `pypdf` |
| **PDF (Scanned/Images)** | `.pdf` | `markitdown_ocr` (Vision LLM) | `tesseract-ocr` |
| **Microsoft Word** | `.docx`, `.doc` | `python-docx` / `mammoth` | `pandoc` / `soffice` (LibreOffice) |
| **Microsoft Excel** | `.xlsx`, `.xls` | `openpyxl` / `markitdown` | `pandas` / `xlrd` |
| **Microsoft PowerPoint** | `.pptx`, `.ppt` | `python-pptx` / `markitdown` | `pandoc` / `soffice` |
| **LibreOffice / ODF** | `.odt`, `.ods`, `.odp` | `pandoc` / `odfpy` | `pandas` (`odf`) / `soffice` CLI |
| **Rich Text & Web** | `.rtf`, `.html`, `.htm` | `markdownify` / `striprtf` | `beautifulsoup4` / `pandoc` |
| **E-books & Email** | `.epub`, `.msg`, `.eml` | `ebooklib` / `extract-msg` | `pandoc` |
| **Images & Audio** | `.jpg`, `.png`, `.mp3` | `Pillow` + `tesseract` / `SpeechRecognition` | LLM Vision / Whisper |

---

### 🛠️ CLI Usage & Examples

#### 1. Environment Verification
Inspect installed packages and available system binaries on your OS:
```bash
# Windows
python scripts/check_env.py

# Linux / macOS
python3 scripts/check_env.py
```

#### 2. Convert Document to File
```bash
# Windows
python scripts/convert_to_md.py "C:\path\to\document.pdf" "C:\path\to\output.md"
python scripts/convert_to_md.py "spreadsheet.xlsx" "spreadsheet.md"
python scripts/convert_to_md.py "report.odt" "report.md"

# Linux / macOS
python3 scripts/convert_to_md.py "/path/to/document.pdf" "/path/to/output.md"
```

#### 3. Output Directly to Terminal Console
```bash
python scripts/convert_to_md.py "document.docx"
```

---

### 📦 Installation

```bash
# Core & Extended Python Packages
pip install markitdown pdfminer.six pdfplumber python-docx openpyxl Pillow python-pptx mammoth pandas odfpy xlrd striprtf extract-msg markdownify
```

**Optional System Binaries:**
- **Pandoc:** `winget install JohnMacFarlane.Pandoc` (Windows) | `brew install pandoc` (macOS) | `sudo apt install pandoc` (Linux)
- **Tesseract OCR:** `winget install UB-Mannheim.TesseractOCR` (Windows) | `brew install tesseract` (macOS) | `sudo apt install tesseract-ocr` (Linux)
- **LibreOffice:** `winget install TheDocumentFoundation.LibreOffice` (Windows) | `brew install libreoffice` (macOS) | `sudo apt install libreoffice` (Linux)

---
---

## 🇧🇷 Português (Brasil)

### 📌 Visão Geral
O **Docs for Markdown** é uma ferramenta Python multiplataforma de alta precisão projetada para converter praticamente qualquer formato de documento em **Markdown (`.md`) limpo, estruturado e padronizado**.

Ele atua como a camada essencial de ingestão para Agentes de IA, sistemas de RAG (Busca com Geração Aumentada) e bases de conhecimento, resolvendo desafios complexos como PDFs com múltiplas colunas, geração incorreta de tabelas falsas, palavras hifenizadas no final de linhas, múltiplas abas de planilhas Excel, anotações de slides PowerPoint e arquivos OpenDocument do LibreOffice.

---

### 🌐 Matriz de Formatos e Motores de Extração

| Categoria de Formato | Extensões | Motor Principal | Fallback / Alternativa |
|---|---|---|---|
| **PDF (Digital)** | `.pdf` | `markitdown` / `pdfminer.six` | `pdfplumber` (tabelas) / `pypdf` |
| **PDF (Digitalizado/Scans)** | `.pdf` | `markitdown_ocr` (Vision LLM) | `tesseract-ocr` |
| **Microsoft Word** | `.docx`, `.doc` | `python-docx` / `mammoth` | `pandoc` / `soffice` (LibreOffice) |
| **Microsoft Excel** | `.xlsx`, `.xls` | `openpyxl` / `markitdown` | `pandas` / `xlrd` |
| **Microsoft PowerPoint** | `.pptx`, `.ppt` | `python-pptx` / `markitdown` | `pandoc` / `soffice` |
| **LibreOffice / ODF** | `.odt`, `.ods`, `.odp` | `pandoc` / `odfpy` | `pandas` (`odf`) / `soffice` CLI |
| **Texto Rico & Web** | `.rtf`, `.html`, `.htm` | `markdownify` / `striprtf` | `beautifulsoup4` / `pandoc` |
| **E-books & E-mails** | `.epub`, `.msg`, `.eml` | `ebooklib` / `extract-msg` | `pandoc` |
| **Imagens & Áudio** | `.jpg`, `.png`, `.mp3` | `Pillow` + `tesseract` / `SpeechRecognition` | LLM Vision / Whisper |

---

### 🛠️ Modo de Uso via Terminal

#### 1. Verificação do Ambiente
Valida pacotes instalados e ferramentas de sistema disponíveis:
```bash
# Windows
python scripts/check_env.py

# Linux / macOS
python3 scripts/check_env.py
```

#### 2. Converter Documento e Salvar em Arquivo `.md`
```bash
# Windows
python scripts/convert_to_md.py "C:\caminho\documento.pdf" "C:\caminho\saida.md"
python scripts/convert_to_md.py "planilha.xlsx" "planilha.md"
python scripts/convert_to_md.py "relatorio.odt" "relatorio.md"

# Linux / macOS
python3 scripts/convert_to_md.py "/caminho/documento.pdf" "/caminho/saida.md"
```

#### 3. Exibir Saída Diretamente no Console
```bash
python scripts/convert_to_md.py "documento.docx"
```

---

### 📦 Instalação de Dependências

```bash
# Pacotes Python essenciais e estendidos
pip install markitdown pdfminer.six pdfplumber python-docx openpyxl Pillow python-pptx mammoth pandas odfpy xlrd striprtf extract-msg markdownify
```

**Ferramentas Opcionais de Sistema:**
- **Pandoc:** `winget install JohnMacFarlane.Pandoc` (Windows) | `brew install pandoc` (macOS) | `sudo apt install pandoc` (Linux)
- **Tesseract OCR:** `winget install UB-Mannheim.TesseractOCR` (Windows) | `brew install tesseract` (macOS) | `sudo apt install tesseract-ocr` (Linux)
- **LibreOffice:** `winget install TheDocumentFoundation.LibreOffice` (Windows) | `brew install libreoffice` (macOS) | `sudo apt install libreoffice` (Linux)

---

### 🛡️ Autonomous Error Recovery & Self-Healing Protocol (For AI Agents)

When an AI Agent encounters errors during skill installation, execution, or environment setup:
1. **Root Cause Diagnosis & Self-Correction:** The agent MUST analyze the underlying cause of failure (missing packages, permissions, OS binary gaps, charset issues) and iteratively attempt self-correction until the skill performs its intended purpose.
2. **Permission Gate for Extra / System Software:** If resolving an issue requires installing system binaries (pandoc, libreoffice, tesseract), elevated global packages, or configuring API keys, the agent MUST explicitly explain the situation to the developer/operator and request authorization before proceeding.
3. **Configuration Report & Verification:** Upon approval, the agent must clearly state what was installed and configured, then immediately execute an end-to-end test or ask the operator for sample inputs to validate that the skill is 100% operational.

---

### 🛡️ Protocolo de Auto-Correção e Recuperação de Erros (Para Agentes de IA)

Sempre que o Agente de IA encontrar falhas na instalação, execução ou configuração de ambiente da skill:
1. **Diagnóstico de Causa Raiz e Auto-Correção:** O agente DEVE analisar a causa exata do erro (dependências ausentes, permissões, ferramentas de SO, encoding de caracteres) e tentar se auto-corrigir iterativamente até que a skill esteja funcionando perfeitamente conforme seu propósito.
2. **Solicitação de Permissão para Instalações Extras:** Se a correção exigir a instalação de binários de sistema (pandoc, libreoffice, tesseract), pacotes globais ou configuração de chaves de API, o agente DEVE explicar o diagnóstico com clareza e solicitar a permissão explícita do desenvolvedor/operador antes de instalar.
3. **Relatório de Configuração e Validação:** Após a confirmação, o agente deve informar detalhadamente o que foi instalado e configurado para resolver o problema e executar imediatamente um teste de validação (ou solicitar ao operador os dados/arquivos necessários para testar a skill).

---

## 👨‍💻 Author / Autor

**Charles Corrêa**  
- 📧 **Email:** [charlescorreaweb@gmail.com](mailto:charlescorreaweb@gmail.com)  
- 📷 **Instagram:** [@mestrecharlescorrea](https://www.instagram.com/mestrecharlescorrea)  
- 🌐 **Websites:** [charlescorrea.com.br](https://charlescorrea.com.br) | [rpg.charlescorrea.com.br](https://rpg.charlescorrea.com.br)  
- 🐙 **GitHub:** [CharlesCorreaDev](https://github.com/CharlesCorreaDev)  
- ⚡ **Skills de IA By Charles Corrêa Repo:** [https://github.com/CharlesCorreaDev/skills-ai](https://github.com/CharlesCorreaDev/skills-ai)

