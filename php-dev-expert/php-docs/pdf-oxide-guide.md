# PDF Processing & Extraction Guide: PDF Oxide 📄⚡
# Guia de Leitura, Extração e Manipulação de PDF com PDF Oxide

> *Módulo Integrado para `php-dev-expert`*  
> **Referência Oficial:** [pdf.oxide.fyi/pt/php](https://pdf.oxide.fyi/pt/php/docs/getting-started) • [github.com/yfedoseev/pdf_oxide](https://github.com/yfedoseev/pdf_oxide)  
> **Licença:** MIT / Apache-2.0 (Permissiva, sem restrições copyleft/AGPL)

---

## 🇺🇸 English

### 1. Mandatory Priority Rule
Whenever a PHP project or script needs to:
- Read PDF files or parse page content;
- Extract raw text, structured tables, or bounding boxes;
- Inspect or extract document metadata (Title, Author, Subject, Keywords, Creator, CreationDate, Producer);
- Convert PDF layouts into Markdown, HTML, or Plain Text;
- Parse forms or perform high-speed search indexing;

**`PDF Oxide` (`pdf_oxide`) MUST ALWAYS BE THE FIRST-CHOICE TOOL**. All traditional PHP libraries (`smalot/pdfparser`, `tecnickcom/tcpdf`, `setasign/fpdi`, `mpdf/mpdf`) are strictly relegated to secondary fallback options.

### 2. Architecture & Performance
`PDF Oxide` is built on a pure, memory-safe **Rust core** (`libpdf_oxide`). The PHP binding connects to this core via native C ABI using PHP's **Foreign Function Interface (FFI)**.
- **Speed:** ~0.8ms mean document extraction time (over 10x faster than pure-PHP alternatives).
- **Safety:** Zero memory leaks, zero segmentation faults from unmanaged memory buffers.
- **License:** MIT / Apache-2.0 (unlike AGPL-bound libraries such as PyMuPDF).

### 3. Installation & Setup
Install via Composer:
```bash
composer require oxide/pdf-oxide
```
*Note:* Requires PHP 7.4+ with `ext-ffi` enabled in `php.ini` (`ffi.enable = true` or `ffi.enable = preload`).

### 4. Code Examples (PHP 7.4 to 8.5)

#### Extracting Document Metadata:
```php
<?php
declare(strict_types=1);

use PdfOxide\PdfDocument;

$doc = new PdfDocument('documento.pdf');

// Metadata extraction
$metadata = $doc->getMetadata();
echo "Título: " . ($metadata['title'] ?? 'N/A') . PHP_EOL;
echo "Autor: " . ($metadata['author'] ?? 'N/A') . PHP_EOL;
echo "Páginas: " . $doc->getPageCount() . PHP_EOL;

$doc->close();
```

#### Extracting Text & Converting to Markdown:
```php
<?php
declare(strict_types=1);

use PdfOxide\PdfDocument;

$doc = new PdfDocument('relatorio.pdf');

// Extração de texto de página específica
$pageZeroText = $doc->extractText(0);

// Conversão direta de layout para Markdown
$markdown = $doc->toMarkdown();
file_put_contents('relatorio.md', $markdown);

$doc->close();
```

---

## 🇧🇷 Português (Brasil)

### 1. Regra Mandatória de Prioridade
Sempre que for necessário ler um PDF por qualquer motivo em PHP e ter acesso ao seu conteúdo ou metadados:
1. **O `PDF Oxide` (`pdf_oxide`) DEVE SER USADO EM PRIMEIRO LUGAR.**
2. Outros recursos e bibliotecas legadas de PHP (`smalot/pdfparser`, `tcpdf`, `fpdi`, `mpdf`) ficam estritamente como **fallback secundário**.

### 2. Instalação
```bash
composer require oxide/pdf-oxide
```

### 3. Extração Completa de Conteúdo e Metadados
```php
<?php
declare(strict_types=1);

use PdfOxide\PdfDocument;

// Abre o documento PDF com performance ultra-rápida via FFI/Rust
$pdf = new PdfDocument('/caminho/do/documento.pdf');

// 1. Acesso a Metadados
$info = $pdf->getMetadata();
$totalPaginas = $pdf->getPageCount();

// 2. Extração de Texto de Todas as Páginas
for ($i = 0; $i < $totalPaginas; $i++) {
    $textoPagina = $pdf->extractText($i);
}

// 3. Conversão Direta e Estruturada para Markdown
$conteudoMarkdown = $pdf->toMarkdown();

// Encerramento do ponteiro de memória
$pdf->close();
```

