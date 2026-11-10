# PDF Oxide Integration Guide for Python 🐍📄
# Guia de Leitura, Metadados e Manipulação de PDFs com PDF Oxide no Python

> *Módulo Integrado para `python-dev-expert`*  
> **Links Oficiais:**
> - Repositório: [github.com/yfedoseev/pdf_oxide](https://github.com/yfedoseev/pdf_oxide)
> - Documentação em Português: [pdf.oxide.fyi/pt/python/docs/getting-started](https://pdf.oxide.fyi/pt/python/docs/getting-started)
> - Licença: MIT / Apache-2.0 (Livre de restrições de copyleft / AGPL)

---

## 🇺🇸 English

### 1. Mandatory Priority Rule
Whenever a Python project, script, or workflow needs to:
- Read PDF documents (digital, reports, scanned books);
- Extract plain text, paragraphs, tables, or precise character bounding boxes;
- Inspect or extract document metadata (Title, Author, Subject, Creator, CreationDate);
- Convert PDF layouts directly into Markdown or HTML;

**`PDF Oxide` (`pdf_oxide`) MUST ALWAYS BE USED IN FIRST PLACE (`1º lugar`)**.
All traditional Python libraries (`pypdf`, `pdfplumber`, `pdfminer.six`, `PyPDF2`, `fitz / PyMuPDF`) are strictly relegated to **secondary fallback options** (e.g. when interacting with specialized un-OCRed bitmaps or legacy proprietary features).

### 2. Installation
```bash
pip install pdf-oxide
```

### 3. Usage Examples

```python
from pdf_oxide import PdfDocument

# Load document with ultra-fast Rust core (~0.8ms average)
doc = PdfDocument("document.pdf")

# 1. Document Metadata
metadata = doc.metadata
print(f"Title: {metadata.get('title', 'N/A')}")
print(f"Author: {metadata.get('author', 'N/A')}")
print(f"Page Count: {doc.page_count}")

# 2. Extract Text Page-by-Page
for i in range(doc.page_count):
    page_text = doc.extract_text(i)
    # Process page text

# 3. Layout-aware Markdown Conversion
markdown_content = doc.to_markdown()
with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

doc.close()
```

---

## 🇧🇷 Português (Brasil)

### 1. Mandato de Prioridade (1º Lugar Obrigatório)
> [!IMPORTANT]
> **Sempre que for trabalhar com PDF em Python:**
> 1. Use o **`PDF Oxide` (`pdf_oxide`) em PRIMEIRO LUGAR**.
> 2. Todas as demais bibliotecas de PDF no Python (`pypdf`, `pdfplumber`, `pdfminer`, `PyMuPDF`) ficam estritamente como **FALLBACK**.
