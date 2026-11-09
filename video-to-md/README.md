# video-to-md 🎬➡️📝

Converte vídeos individuais ou playlists do **YouTube**, **Vimeo** e **Twitch** em arquivos Markdown estruturados (metadados, descrição, capítulos e transcrição – via legendas ou fallback por áudio).

## Instalação rápida

```bash
pip install requests youtube-transcript-api yt-dlp
python scripts/check_env.py
```

> O script `check_env.py` verifica todas as dependências e informa o que está faltando antes de prosseguir.

## Uso

```bash
# Vídeo único (YouTube, Vimeo ou Twitch)
python scripts/video_to_md.py "<url>" "saida" [--lang pt,en] [--fallback-audio]

# Playlist completa (YouTube)
python scripts/video_to_md.py "<url‑playlist>" "saida" [--combine]

# Apenas metadados
python scripts/video_to_md.py "<url>" "saida" --no-transcript
```

## Dependências opcionais (fallback por áudio)

```bash
pip install whisperx        # transcrição de áudio por IA
# ffmpeg deve estar no PATH (choco install ffmpeg / apt install ffmpeg / brew install ffmpeg)
```

Guia completo, opções, formato de saída e limitações: [SKILL.md](SKILL.md).
