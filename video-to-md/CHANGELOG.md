# Changelog - Video to Markdown 🎬

Todas as alterações notáveis desta skill serão documentadas aqui.  
Formato baseado em [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) e [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.2.0-beta] - 2026-11-03

### Added / Adicionado
- **Multiplataforma**: suporte nativo a vídeos do **Vimeo** (via oEmbed e API v2) e **Twitch** (via `yt-dlp`).
- **Fallback por Áudio (Whisper / WhisperX)**: `--fallback-audio` com opção `--whisper-model` para transcrever áudio diretamente via IA quando legendas não estiverem disponíveis.
- **Pausa padrão ajustada**: `--delay-ms` atualizado para padrão de 15.000 ms (15s) evitando bloqueios por taxa.
- Renomeação da skill e scripts de `youtube-to-md` para `video-to-md`.
- `check_env.py` expandido para validar dependências obrigatórias (`requests`, `youtube-transcript-api`, `yt-dlp`) e opcionais (`whisperx`, `openai-whisper`, `ffmpeg`).

---

## [0.1.0-beta] - 2026-10-28

### Added / Adicionado
- `scripts/video_to_md.py`: conversão de vídeos soltos (`watch`, `youtu.be`, `shorts`, ID) e playlists do YouTube em Markdown.
- Metadados (título, canal, data, duração, visualizações, tags), descrição, capítulos extraídos da descrição e transcrição com timestamps clicáveis.
- Escolha de idioma de legenda (`--lang`), preferindo legenda manual sobre automática, com fallback para qualquer idioma disponível.
- Playlists: arquivo por vídeo numerado, `_INDEX.md`, `manifest.json` e `_ALL.md` opcional (`--combine`).
- Retomada (pula arquivos existentes), pausa entre vídeos (`--delay-ms`), `--start`, `--max-videos`, `--no-transcript`.
- Uso opcional do `yt-dlp` para listar playlists grandes.
- `scripts/check_env.py`.
