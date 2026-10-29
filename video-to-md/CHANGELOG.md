# Changelog - YouTube to Markdown 🎬

Todas as alterações notáveis desta skill serão documentadas aqui.  
Formato baseado em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) e [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0-beta] - 2026-10-28

### Added / Adicionado
- `scripts/youtube_to_md.py`: conversão de vídeos soltos (`watch`, `youtu.be`, `shorts`, ID) e playlists em Markdown.
- Metadados (título, canal, data, duração, visualizações, tags), descrição, capítulos extraídos da descrição e transcrição com timestamps clicáveis.
- Escolha de idioma de legenda (`--lang`), preferindo legenda manual sobre automática, com fallback para qualquer idioma disponível.
- Playlists: arquivo por vídeo numerado, `_INDEX.md`, `manifest.json` e `_ALL.md` opcional (`--combine`).
- Retomada (pula arquivos existentes), pausa entre vídeos (`--delay-ms`), `--start`, `--max-videos`, `--no-transcript`.
- Uso opcional do `yt-dlp` para listar playlists grandes.
- `scripts/check_env.py`.

### Testado
- Um vídeo solto e os 3 primeiros vídeos de uma playlist pública, com legendas automáticas em `pt`.

### Não testado
- Playlists com mais de ~100 vídeos, vídeos sem legenda, privados ou com restrição de idade, e o caminho com `yt-dlp` instalado.
