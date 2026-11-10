# Python Security Shield & Critical CVE Mitigations 🛡️🐍
# Blindagem de Segurança e Mitigação de Vulnerabilidades Recentes do Python

> *Módulo Integrado para `python-dev-expert`*  
> **Status:** Atualizado para CPython e Ecossistema (2024–2026)  
> **Normas & Fontes:** Python Software Foundation (PSF), NIST NVD, CVE Program e OWASP Top 10.

---

## 🇺🇸 English

### 1. Overview of Recent Python Vulnerabilities (2024–2026)
Python core (CPython) and its primary package ecosystem have encountered critical security flaws that allow Remote Code Execution (RCE), Denial of Service (DoS/ReDoS), Server-Side Request Forgery (SSRF), and Supply Chain attacks.

This guide provides defensive programming methods, automated scanners, and concrete architectural mitigations to shield Python projects from these vulnerabilities.

---

### 2. Critical CPython Core CVEs & Defensive Fixes

#### A. TLS/SSL Use-After-Free in Server SNI (CVE-2026-19445 - CVSS 9.2) & wrap_bio (CVE-2026-19553)
- **Vulnerability:** Affects server-side `SSLContext` when an `sni_callback` dynamically switches contexts, leading to memory corruption or RCE. `wrap_bio` lacked validation of `server_hostname`.
- **Affected:** Python 3.10.x < 3.10.22, 3.11.x < 3.11.17, 3.12.x < 3.12.15, 3.13.x < 3.13.16.
- **Defensive Mitigation:**
  1. Patch CPython to patched maintenance versions.
  2. If running unpatched runtimes in containerized legacy services, avoid mutating `SSLContext` instances inside `sni_callback`:
  ```python
  import ssl

  # ✅ Defesa: pré-crie contextos imutáveis e evite reatribuição insegura
  def safe_sni_callback(ssl_socket, server_name, initial_context):
      # Em vez de criar e mutar novos contextos em tempo de execução:
      target_ctx = PRECONFIGURED_DOMAINS.get(server_name, initial_context)
      ssl_socket.context = target_ctx
  ```

#### B. Command Injection via `webbrowser.open()` (CVE-2026-4519 - CVSS 7.0)
- **Vulnerability:** `webbrowser.open()` accepted URLs starting with `--`, which underlying browser CLI binaries interpreted as flags (e.g. `--browser-test-mode`, `--load-extension`), executing arbitrary local commands.
- **Defensive Mitigation:** Always validate and sanitize URLs with scheme whitelisting before passing to `webbrowser.open()` or `subprocess`:
  ```python
  import re
  import urllib.parse
  import webbrowser

  def safe_open_url(target_url: str) -> bool:
      target_url = target_url.strip()
      # Rejeitar flags CLI iniciadas por traço (-)
      if target_url.startswith("-"):
          raise ValueError("Invalid URL: potential command line flag injection")
      
      parsed = urllib.parse.urlsplit(target_url)
      # Permitir estritamente esquemas HTTP/HTTPS seguros
      if parsed.scheme.lower() not in ("http", "https"):
          raise ValueError(f"Prohibited scheme: {parsed.scheme}")
      
      return webbrowser.open(target_url)
  ```

#### C. Path Traversal & Command Injection in `venv` (CVE-2024-9287)
- **Vulnerability:** Unquoted or malicious path names passed to `venv` creation allowed code injection when users sourced `activate` scripts (`source venv/bin/activate`).
- **Defensive Mitigation:**
  1. Always use sanitized paths free of quotes, backticks, or special shell characters when generating virtual environments.
  2. Execute the python binary directly (`./venv/bin/python script.py`) instead of sourcing activation scripts in automated CI/CD runners.

#### D. SSRF via Bracketed Host Parsing in `urllib.parse` (CVE-2024-11168)
- **Vulnerability:** `urlsplit()` and `urlparse()` accepted invalid bracketed hosts (`http://[invalid-host]/`), bypassing upstream firewall/SSRF filters and being parsed differently by downstream HTTP client libraries.
- **Defensive Mitigation:**
  ```python
  import ipaddress
  import urllib.parse

  def validate_safe_url(url: str) -> str:
      parsed = urllib.parse.urlsplit(url)
      hostname = parsed.hostname
      if not hostname:
          raise ValueError("Invalid URL: Hostname is missing")

      # Se o host vier entre colchetes, validar estritamente como IPv6
      if hostname.startswith("[") or "]" in hostname or ":" in hostname:
          raw_ip = hostname.strip("[]")
          try:
              ip_obj = ipaddress.ip_address(raw_ip)
              if ip_obj.is_private or ip_obj.is_loopback:
                  raise ValueError("Access to private/loopback IP is blocked (SSRF defense)")
          except ValueError:
              raise ValueError("Malformed bracketed IP host detected")
      return url
  ```

#### E. ReDoS & Tar Slip in `tarfile` (CVE-2024-6232)
- **Vulnerability:** ReDoS in PAX and sparse header parsing, and path traversal when extracting archives without `filter`.
- **Defensive Mitigation:**
  - Always use `filter='data'` (Python 3.12+) or safe extraction checks:
  ```python
  import tarfile

  def safe_extract_tar(tar_path: str, destination_dir: str):
      with tarfile.open(tar_path, "r:*") as tar:
          # Python 3.12+ Safe extraction filter
          if hasattr(tarfile, 'data_filter'):
              tar.extractall(path=destination_dir, filter='data')
          else:
              # Fallback seguro para versões anteriores: verificar cada membro
              for member in tar.getmembers():
                  target_path = os.path.realpath(os.path.join(destination_dir, member.name))
                  if not target_path.startswith(os.path.realpath(destination_dir)):
                      raise SecurityError("Attempted Path Traversal in Tar File")
              tar.extractall(path=destination_dir)
  ```

#### F. HTTP Cookies Quadratic Complexity DoS (CVE-2024-7592)
- **Vulnerability:** Deeply nested or backslash-laden cookie headers forced quadratic ($O(n^2)$) CPU parsing in `http.cookies`.
- **Defensive Mitigation:** Set header size limits at reverse proxy levels (Nginx `large_client_header_buffers 4 8k`) and truncate cookie strings before parsing untrusted headers.

---

### 3. Critical Ecosystem Vulnerabilities (Pillow & Image Processing)

#### Critical Memory Corruption & RCE in Pillow (CVE-2026-112900, CVE-2026-112393, CVE-2026-112403)
- **Impact:** CVSS 9.2 Critical. Processing untrusted EPS, TIFF, or JPEG files triggers heap overflow or arbitrary code execution via Ghostscript or corrupted `BytesIO` reallocations.
- **Defensive Rule:**
  1. Upgrade Pillow to **`Pillow >= 13.0.0`**.
  2. Disable unsafe Ghostscript formats in Pillow:
  ```python
  from PIL import Image

  # Desabilitar suporte a arquivos EPS potencialmente perigosos
  if hasattr(Image, 'register_mime'):
      Image.ID.remove('EPS') if 'EPS' in Image.ID else None
  ```

---

### 4. Automated Security Scanning Checklist for Python Projects
Every Python application developed by this skill must include proactive security checks:

```bash
# 1. Auditoria de CVEs conhecidas nas dependências instaladas:
pip install pip-audit
pip-audit -r requirements.txt

# 2. Análise Estática de Código (SAST) para padrões vulneráveis:
pip install bandit
bandit -r src/ -ll -ii

# 3. Verificação de supply chain e pacotes maliciosos:
pip install safety
safety check
```

---

## 🇧🇷 Português (Brasil)

### 1. Resumo das Vulnerabilidades Críticas Recentes
No período 2024–2026, tanto o núcleo do Python (CPython) quanto bibliotecas fundamentais (Pillow, venv, urllib) sofreram descobertas de alto impacto:
1. **CVE-2026-19445 & CVE-2026-19553 (SSL / TLS Use-After-Free):** Falha grave de corrupção de memória e RCE ao alternar contextos SSL em callbacks SNI de servidores.
2. **CVE-2026-4519 (Injeção de Comando em `webbrowser.open`):** URLs iniciadas por `--` eram interpretadas como parâmetros de linha de comando pelo navegador, permitindo execução de código.
3. **CVE-2024-9287 (RCE em scripts de ativação do `venv`):** Falha na criação de ambientes virtuais com caminhos contendo aspas e caracteres especiais.
4. **CVE-2024-11168 (SSRF em `urllib.parse`):** Aceitação incorreta de hosts com colchetes malformados, burlando firewalls e filtros de IP privado.
5. **CVE-2024-6232 (ReDoS e Tar Slip em `tarfile`):** Descompactação de arquivos maliciosos travando a CPU ou sobrescrevendo arquivos do sistema fora do diretório de destino.
6. **CVE-2026-112900 (Pillow RCE / Heap Overflow):** Processamento de imagens EPS/TIFF/JPEG especialmente forjadas disparando estouro de memória e execução remota de código.

### 2. Mandatos Obrigatórios para o Agente de IA (`python-dev-expert`):
1. **Descompactação Segura:** NUNCA usar `tar.extractall()` sem `filter='data'` (ou validação manual contra Path Traversal).
2. **Sanitização de URLs:** NUNCA repassar URLs externas diretamente para `webbrowser.open()` ou comandos de sistema sem validação de esquema (`http`/`https`) e rejeição de prefixos `-`.
3. **Prevenção de SSRF:** Sempre validar hosts resolvidos via `urllib.parse` contra faixas privadas (`is_private`, `is_loopback`) usando `ipaddress`.
4. **Pillow Atualizado:** Garantir `Pillow >= 13.0.0` e desativar suporte nativo a formatos perigosos (como EPS com Ghostscript).
5. **Auditoria Contínua:** Sugerir e configurar `pip-audit` e `bandit` no repositório do usuário.

