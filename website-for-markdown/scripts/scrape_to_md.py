#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Motor multiplataforma de captura de websites para Markdown.
Utiliza Firecrawl (se API_KEY disponível) ou Playwright + MarkItDown/Markdownify como fallback local.
"""
import sys
import os
import tempfile
from pathlib import Path
from urllib.parse import urlparse

# Força UTF-8 nas saídas de console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

def scrape_with_firecrawl(url, output_dir, mode="scrape"):
    try:
        from firecrawl import FirecrawlApp
    except ImportError:
        return False

    api_key = os.environ.get("FIRECRAWL_API_KEY")
    if not api_key:
        return False

    try:
        app = FirecrawlApp(api_key=api_key)
        out_path = Path(output_dir).resolve()
        out_path.mkdir(parents=True, exist_ok=True)
        
        print(f"🚀 [Firecrawl] Iniciando modo '{mode}' para: {url}")
        
        if mode == "scrape":
            result = app.scrape_url(url, params={'formats': ['markdown']})
            if 'markdown' in result:
                filename = urlparse(url).netloc.replace('.', '_') + ".md"
                (out_path / filename).write_text(result['markdown'], encoding='utf-8')
                print(f"✅ Salvo em: {out_path / filename}")
                return True
        elif mode == "crawl":
            crawl_status = app.crawl_url(url, params={'limit': 100, 'scrapeOptions': {'formats': ['markdown']}})
            if isinstance(crawl_status, dict) and 'data' in crawl_status:
                for i, page in enumerate(crawl_status['data']):
                    if 'markdown' in page and 'metadata' in page:
                        page_url = page['metadata'].get('sourceURL', f"page_{i}")
                        slug = urlparse(page_url).path.strip('/').replace('/', '_') or "index"
                        filename = f"{slug}.md"
                        (out_path / filename).write_text(page['markdown'], encoding='utf-8')
                print(f"✅ Crawling concluído. {len(crawl_status['data'])} páginas salvas em {out_path}")
                return True
    except Exception as e:
        print(f"⚠️ Erro ao executar Firecrawl: {e}")
        
    return False

def scrape_with_playwright(url, output_dir):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("❌ Playwright não instalado. Execute: pip install playwright && python -m playwright install chromium")
        return False

    out_path = Path(output_dir).resolve()
    out_path.mkdir(parents=True, exist_ok=True)
    
    print(f"🎭 [Playwright] Renderizando página (modo local): {url}")
    
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                args=['--disable-blink-features=AutomationControlled', '--no-sandbox']
            )
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
                viewport={'width': 1280, 'height': 800}
            )
            page = context.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=30000)
            # Aguarda renderização de SPAs
            page.wait_for_timeout(2000)
            
            html_content = page.content()
            page_title = page.title()
            browser.close()
            
        print("🔄 Convertendo HTML renderizado para Markdown...")
        
        # Converte HTML para Markdown via MarkItDown
        markdown_content = ""
        try:
            from markitdown import MarkItDown
            md = MarkItDown()
            with tempfile.NamedTemporaryFile('w', suffix='.html', encoding='utf-8', delete=False) as tmp:
                tmp.write(html_content)
                tmp_file = tmp.name
            
            try:
                res = md.convert(tmp_file)
                markdown_content = res.text_content if hasattr(res, 'text_content') else getattr(res, 'markdown', str(res))
            finally:
                if os.path.exists(tmp_file):
                    os.remove(tmp_file)
        except Exception:
            # Fallback para markdownify caso MarkItDown falhe
            import markdownify
            markdown_content = markdownify.markdownify(html_content, heading_style="ATX")

        parsed = urlparse(url)
        name_part = parsed.netloc.replace('.', '_')
        path_part = parsed.path.strip('/').replace('/', '_')
        filename = f"{name_part}_{path_part}.md" if path_part else f"{name_part}.md"
        
        output_file = out_path / filename
        output_file.write_text(f"# {page_title}\n\nFonte: {url}\n\n---\n\n" + markdown_content, encoding='utf-8')
        print(f"✅ Sucesso! Markdown salvo em: {output_file}")
        return True
        
    except Exception as e:
        print(f"❌ Erro durante captura com Playwright: {e}")
        return False

def main():
    if len(sys.argv) < 3:
        print("Uso: python scrape_to_md.py <url> <pasta_saida> [--crawl]")
        print("  <url>         : URL única ou domínio raiz.")
        print("  <pasta_saida> : Diretório onde os arquivos .md serão salvos.")
        print("  --crawl       : (Opcional) Tenta varrer o site inteiro (Requer Firecrawl API).")
        sys.exit(1)
        
    url = sys.argv[1]
    output_dir = sys.argv[2]
    mode = "crawl" if "--crawl" in sys.argv else "scrape"
    
    if not url.startswith("http"):
        url = "https://" + url

    # 1. Tenta Firecrawl se API KEY estiver presente
    if os.environ.get("FIRECRAWL_API_KEY"):
        if scrape_with_firecrawl(url, output_dir, mode):
            sys.exit(0)
    else:
        if mode == "crawl":
            print("ℹ️ FIRECRAWL_API_KEY não configurada. O modo --crawl em lote requer Firecrawl API.")
            print("👉 Executando captura da página alvo via Playwright local...")
        
    # 2. Executa Playwright (Local Headless Chromium)
    if scrape_with_playwright(url, output_dir):
        sys.exit(0)
        
    print("❌ Falha na captura. Verifique se o endereço está acessível ou bloqueado por firewall.")
    sys.exit(1)

if __name__ == "__main__":
    main()