#!/usr/bin/env python3
"""
video_to_md.py - Converte vídeos e playlists do YouTube, Vimeo e Twitch em Markdown.
Converts videos and playlists from YouTube, Vimeo, and Twitch into Markdown.

Gera um .md com metadados, descrição, capítulos e transcrição
(legendas ou áudio via Whisper) com timestamps clicáveis.
Para playlists gera também _INDEX.md e manifest.json.
"""

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unicodedata
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import requests

USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)
HEADERS = {"User-Agent": USER_AGENT, "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8"}
COOKIES = {"CONSENT": "YES+1", "SOCS": "CAI"}
VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
CHAPTER_RE = re.compile(r"^\s*((?:\d{1,2}:)?\d{1,2}:\d{2})\s*[-–—:|]?\s*(.+?)\s*$")


# --------------------------------------------------------------------------- #
# Platform Detection & Target Parsing
# --------------------------------------------------------------------------- #
def detect_platform(url: str) -> str:
    url = url.strip()
    if VIDEO_ID_RE.match(url):
        return "youtube"
    parsed = urlparse(url)
    host = (parsed.hostname or "").lower().removeprefix("www.").removeprefix("m.")
    if host in ("youtube.com", "youtu.be", "music.youtube.com", "youtube-nocookie.com"):
        return "youtube"
    if "vimeo.com" in host:
        return "vimeo"
    if "twitch.tv" in host:
        return "twitch"
    return "unknown"


def parse_target(url: str, force_playlist: bool = False, force_video: bool = False):
    """Return (platform, kind, identifier, full_url)."""
    url = url.strip()
    platform = detect_platform(url)

    if platform == "youtube":
        if VIDEO_ID_RE.match(url):
            return "youtube", "video", url, f"https://www.youtube.com/watch?v={url}"

        parsed = urlparse(url)
        host = (parsed.hostname or "").lower().removeprefix("www.").removeprefix("m.")
        query = parse_qs(parsed.query)
        path_parts = [p for p in parsed.path.split("/") if p]

        video_id = None
        if host == "youtu.be" and path_parts:
            video_id = path_parts[0]
        elif host in ("youtube.com", "music.youtube.com", "youtube-nocookie.com"):
            if parsed.path == "/watch":
                video_id = (query.get("v") or [None])[0]
            elif path_parts and path_parts[0] in ("shorts", "embed", "live", "v") and len(path_parts) > 1:
                video_id = path_parts[1]

        playlist_id = (query.get("list") or [None])[0]
        is_playlist_page = parsed.path == "/playlist"

        if force_video and video_id:
            return "youtube", "video", video_id, f"https://www.youtube.com/watch?v={video_id}"
        if playlist_id and (is_playlist_page or force_playlist or not video_id):
            return "youtube", "playlist", playlist_id, f"https://www.youtube.com/playlist?list={playlist_id}"
        if video_id and VIDEO_ID_RE.match(video_id):
            return "youtube", "video", video_id, f"https://www.youtube.com/watch?v={video_id}"
        raise ValueError(
            "Não encontrei um vídeo ou playlist válido do YouTube na URL informada."
        )

    if platform == "vimeo":
        parsed = urlparse(url)
        path_parts = [p for p in parsed.path.split("/") if p]
        if not path_parts:
            raise ValueError(f"URL do Vimeo inválida: {url}")
        vimeo_id = path_parts[-1]
        return "vimeo", "video", vimeo_id, url

    if platform == "twitch":
        parsed = urlparse(url)
        path_parts = [p for p in parsed.path.split("/") if p]
        if not path_parts:
            raise ValueError(f"URL da Twitch inválida: {url}")
        video_id = path_parts[-1]
        return "twitch", "video", video_id, url

    raise ValueError(f"Plataforma não suportada ou URL desconhecida: {url}")


# --------------------------------------------------------------------------- #
# HTTP & Parsing Helpers
# --------------------------------------------------------------------------- #
def http_get(url: str, retries: int = 3, timeout: int = 20) -> str:
    last_err = None
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, cookies=COOKIES, timeout=timeout)
            if r.status_code in (429, 503):
                time.sleep(2.0 * (attempt + 1))
                continue
            r.raise_for_status()
            return r.text
        except requests.RequestException as e:
            last_err = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"Falha ao acessar {url}: {last_err}")


def extract_json_blob(page: str, marker: str):
    idx = page.find(marker)
    if idx == -1:
        return None
    start = page.find("{", idx)
    if start == -1:
        return None
    try:
        obj, _ = json.JSONDecoder().raw_decode(page[start:])
        return obj
    except json.JSONDecodeError:
        return None


def walk(node):
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for item in node:
            yield from walk(item)


def parse_timestamp(ts: str) -> int:
    parts = [int(p) for p in ts.split(":")]
    seconds = 0
    for p in parts:
        seconds = seconds * 60 + p
    return seconds


def fmt_ts(seconds: float) -> str:
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def parse_chapters(description: str):
    found = []
    for line in description.splitlines():
        m = CHAPTER_RE.match(line)
        if m:
            found.append({"start": parse_timestamp(m.group(1)), "title": m.group(2)})
    if len(found) >= 2 and found[0]["start"] == 0:
        return found
    return []


# --------------------------------------------------------------------------- #
# Metadata Fetchers
# --------------------------------------------------------------------------- #
def fetch_youtube_meta(video_id: str, fallback_title: str = ""):
    meta = {
        "id": video_id, "title": fallback_title or video_id, "channel": "", "channel_id": "",
        "duration": 0, "views": None, "published": "", "description": "",
        "keywords": [], "chapters": [], "platform": "youtube",
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "thumbnail": f"https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"
    }
    try:
        page = http_get(f"https://www.youtube.com/watch?v={video_id}")
    except RuntimeError as e:
        meta["error"] = str(e)
        return meta

    player = extract_json_blob(page, "ytInitialPlayerResponse = ")
    if not player:
        meta["error"] = "ytInitialPlayerResponse ausente (vídeo indisponível ou bloqueado)."
        return meta

    status = player.get("playabilityStatus", {})
    if status.get("status") not in (None, "OK") and not player.get("videoDetails"):
        meta["error"] = status.get("reason") or status.get("status")
        return meta

    vd = player.get("videoDetails", {})
    micro = player.get("microformat", {}).get("playerMicroformatRenderer", {})
    meta.update({
        "title": vd.get("title") or meta["title"],
        "channel": vd.get("author", ""),
        "channel_id": vd.get("channelId", ""),
        "duration": int(vd.get("lengthSeconds") or 0),
        "views": int(vd["viewCount"]) if str(vd.get("viewCount", "")).isdigit() else None,
        "published": micro.get("publishDate") or micro.get("uploadDate") or "",
        "description": vd.get("shortDescription", ""),
        "keywords": vd.get("keywords") or [],
    })
    meta["chapters"] = parse_chapters(meta["description"])
    return meta


def fetch_vimeo_meta(video_id: str, url: str):
    meta = {
        "id": video_id, "title": f"Vimeo Video {video_id}", "channel": "", "channel_id": "",
        "duration": 0, "views": None, "published": "", "description": "",
        "keywords": [], "chapters": [], "platform": "vimeo",
        "url": url, "thumbnail": ""
    }
    try:
        # Tenta API oEmbed pública do Vimeo
        oembed_url = f"https://vimeo.com/api/oembed.json?url={url}"
        r = requests.get(oembed_url, headers=HEADERS, timeout=15)
        if r.status_code == 200:
            data = r.json()
            meta["title"] = data.get("title", meta["title"])
            meta["channel"] = data.get("author_name", "")
            meta["duration"] = int(data.get("duration", 0))
            meta["description"] = data.get("description", "")
            meta["thumbnail"] = data.get("thumbnail_url", "")
    except Exception as e:
        meta["error"] = f"Erro no oEmbed Vimeo: {e}"

    # Complementa via v2 API se duration ainda for 0
    if not meta["duration"]:
        try:
            clean_id = re.sub(r"\D", "", video_id)
            if clean_id:
                v2_url = f"https://vimeo.com/api/v2/video/{clean_id}.json"
                r = requests.get(v2_url, headers=HEADERS, timeout=15)
                if r.status_code == 200:
                    d = r.json()[0]
                    meta["title"] = meta["title"] or d.get("title")
                    meta["channel"] = meta["channel"] or d.get("user_name")
                    meta["duration"] = int(d.get("duration", 0))
                    meta["description"] = meta["description"] or d.get("description", "")
                    meta["published"] = d.get("upload_date", "")
                    meta["views"] = d.get("stats_number_of_plays")
        except Exception:
            pass

    # Se yt-dlp estiver disponível, pode enriquecer ainda mais
    if shutil.which("yt-dlp"):
        try:
            res = subprocess.run(
                ["yt-dlp", "--dump-json", "--skip-download", url],
                capture_output=True, text=True, encoding="utf-8", timeout=30
            )
            if res.returncode == 0:
                yd = json.loads(res.stdout)
                meta["title"] = yd.get("title") or meta["title"]
                meta["channel"] = yd.get("uploader") or yd.get("channel") or meta["channel"]
                meta["duration"] = int(yd.get("duration") or meta["duration"])
                meta["description"] = yd.get("description") or meta["description"]
                meta["thumbnail"] = yd.get("thumbnail") or meta["thumbnail"]
                meta["views"] = yd.get("view_count") or meta["views"]
        except Exception:
            pass

    return meta


def fetch_twitch_meta(video_id: str, url: str):
    meta = {
        "id": video_id, "title": f"Twitch {video_id}", "channel": "", "channel_id": "",
        "duration": 0, "views": None, "published": "", "description": "",
        "keywords": [], "chapters": [], "platform": "twitch",
        "url": url, "thumbnail": ""
    }
    if shutil.which("yt-dlp"):
        try:
            res = subprocess.run(
                ["yt-dlp", "--dump-json", "--skip-download", url],
                capture_output=True, text=True, encoding="utf-8", timeout=30
            )
            if res.returncode == 0:
                yd = json.loads(res.stdout)
                meta["title"] = yd.get("title") or meta["title"]
                meta["channel"] = yd.get("uploader") or yd.get("channel") or meta["channel"]
                meta["duration"] = int(yd.get("duration") or 0)
                meta["description"] = yd.get("description") or ""
                meta["thumbnail"] = yd.get("thumbnail") or ""
                meta["views"] = yd.get("view_count")
                return meta
        except Exception as e:
            meta["error"] = f"yt-dlp erro Twitch: {e}"

    return meta


# --------------------------------------------------------------------------- #
# Subtitles / Transcripts
# --------------------------------------------------------------------------- #
def fetch_youtube_transcript(video_id: str, languages):
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        return {"error": "youtube-transcript-api não instalado (pip install youtube-transcript-api)"}

    api = YouTubeTranscriptApi()
    for attempt in range(2):
        try:
            transcripts = api.list(video_id)
            chosen = None
            try:
                chosen = transcripts.find_manually_created_transcript(languages)
            except Exception:
                try:
                    chosen = transcripts.find_generated_transcript(languages)
                except Exception:
                    for t in transcripts:
                        chosen = t
                        break
            if chosen is None:
                return {"error": "Nenhuma legenda disponível para este vídeo."}
            fetched = chosen.fetch()
            segments = [
                {"start": float(s.start), "duration": float(s.duration),
                 "text": html.unescape(s.text).replace("\n", " ").strip()}
                for s in fetched if s.text.strip()
            ]
            return {"segments": segments, "language": chosen.language_code,
                    "generated": bool(chosen.is_generated)}
        except Exception as e:
            name = type(e).__name__
            if name in ("RequestBlocked", "IpBlocked") and attempt == 0:
                time.sleep(10)
                continue
            if name in ("TranscriptsDisabled", "NoTranscriptFound"):
                return {"error": "Legendas desativadas ou inexistentes neste vídeo."}
            if name == "VideoUnavailable":
                return {"error": "Vídeo indisponível."}
            if name in ("RequestBlocked", "IpBlocked"):
                return {"error": "O YouTube bloqueou temporariamente as requisições. Tente depois ou use outra rede."}
            return {"error": f"{name}: {e}".splitlines()[0]}
    return {"error": "Falha desconhecida ao obter transcrição."}


def parse_vtt(vtt_text: str):
    segments = []
    blocks = re.split(r"\n\s*\n", vtt_text.strip())
    ts_pattern = re.compile(r"((?:\d{1,2}:)?\d{2}:\d{2}\.\d{3})\s*-->\s*((?:\d{1,2}:)?\d{2}:\d{2}\.\d{3})")

    for block in blocks:
        lines = block.strip().splitlines()
        for i, line in enumerate(lines):
            m = ts_pattern.search(line)
            if m:
                start_str, end_str = m.group(1), m.group(2)
                def to_sec(s):
                    parts = s.split(":")
                    if len(parts) == 2:
                        return int(parts[0]) * 60 + float(parts[1])
                    return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])

                start_sec = to_sec(start_str)
                end_sec = to_sec(end_str)
                text = " ".join(re.sub(r"<[^>]+>", "", l) for l in lines[i+1:]).strip()
                if text:
                    segments.append({
                        "start": start_sec,
                        "duration": max(0.5, end_sec - start_sec),
                        "text": html.unescape(text)
                    })
                break
    return segments


def fetch_ytdlp_subtitles(url: str, languages):
    ytdlp_exe = shutil.which("yt-dlp")
    if not ytdlp_exe:
        return {"error": "yt-dlp não instalado. Instale via pip install yt-dlp para capturar legendas desta plataforma."}

    with tempfile.TemporaryDirectory() as tmp_dir:
        lang_str = ",".join(languages)
        cmd = [
            ytdlp_exe,
            "--skip-download",
            "--write-subs",
            "--write-auto-subs",
            "--sub-langs", lang_str,
            "--sub-format", "vtt",
            "-o", str(Path(tmp_dir) / "%(id)s.%(ext)s"),
            url
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", timeout=60)
        vtt_files = list(Path(tmp_dir).glob("*.vtt"))
        if not vtt_files:
            return {"error": "Nenhuma legenda encontrada pelo yt-dlp."}

        vtt_file = vtt_files[0]
        lang = "auto"
        for part in vtt_file.stem.split("."):
            if len(part) in (2, 5) and ("-" in part or part.isalpha()):
                lang = part
        content = vtt_file.read_text(encoding="utf-8", errors="replace")
        segments = parse_vtt(content)
        if not segments:
            return {"error": "Legendas vazias ou formato não reconhecido."}
        return {"segments": segments, "language": lang, "generated": True}


# --------------------------------------------------------------------------- #
# Audio Fallback Transcription (Whisper)
# --------------------------------------------------------------------------- #
def fallback_audio_whisper(url: str, whisper_model: str = "base"):
    ytdlp_exe = shutil.which("yt-dlp")
    if not ytdlp_exe:
        return {"error": "yt-dlp é necessário para o download de áudio (pip install yt-dlp)."}

    # Verifica se whisper ou whisperx está disponível
    has_whisperx = False
    has_whisper = False
    try:
        import whisperx
        has_whisperx = True
    except ImportError:
        try:
            import whisper
            has_whisper = True
        except ImportError:
            pass

    if not (has_whisperx or has_whisper):
        return {"error": "Nem whisperx nem openai-whisper estão instalados (pip install openai-whisper ou whisperx)."}

    with tempfile.TemporaryDirectory() as tmp_dir:
        audio_file = Path(tmp_dir) / "audio.mp3"
        print("📥 Baixando áudio para transcrição via Whisper...")
        cmd_dl = [
            ytdlp_exe,
            "-x", "--audio-format", "mp3",
            "--audio-quality", "5",
            "-o", str(audio_file),
            url
        ]
        res_dl = subprocess.run(cmd_dl, capture_output=True, text=True, encoding="utf-8", timeout=300)
        if res_dl.returncode != 0 or not audio_file.exists():
            return {"error": f"Falha ao baixar áudio com yt-dlp: {res_dl.stderr.strip()[:200]}"}

        print(f"🎙️ Transcrevendo áudio com Whisper (modelo: {whisper_model})...")
        try:
            if has_whisperx:
                import whisperx
                device = "cuda" if getattr(whisperx, "torch", None) and whisperx.torch.cuda.is_available() else "cpu"
                compute_type = "float16" if device == "cuda" else "int8"
                model = whisperx.load_model(whisper_model, device, compute_type=compute_type)
                audio = whisperx.load_audio(str(audio_file))
                result = model.transcribe(audio, batch_size=16)
                segments = [
                    {"start": float(s["start"]), "duration": float(s["end"] - s["start"]),
                     "text": s["text"].strip()}
                    for s in result.get("segments", [])
                ]
                lang = result.get("language", "pt")
                return {"segments": segments, "language": lang, "generated": True, "source": "whisperx"}
            else:
                import whisper
                model = whisper.load_model(whisper_model)
                res = model.transcribe(str(audio_file))
                segments = [
                    {"start": float(s["start"]), "duration": float(s["end"] - s["start"]),
                     "text": s["text"].strip()}
                    for s in res.get("segments", [])
                ]
                lang = res.get("language", "pt")
                return {"segments": segments, "language": lang, "generated": True, "source": "whisper"}
        except Exception as e:
            return {"error": f"Erro durante a transcrição do Whisper: {e}"}


# --------------------------------------------------------------------------- #
# Output Formatters: Markdown & SRT
# --------------------------------------------------------------------------- #
def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text[:max_len].strip("-") or "video"


def yaml_str(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def build_paragraphs(segments, chapters, video_url: str, window: int = 60, timestamps: bool = True):
    def link(t):
        if "youtube.com" in video_url or "youtu.be" in video_url:
            return f"{video_url}?t={int(t)}" if "?" not in video_url else f"{video_url}&t={int(t)}"
        if "vimeo.com" in video_url:
            return f"{video_url}#t={int(t)}s"
        if "twitch.tv" in video_url:
            return f"{video_url}?t={fmt_ts(t).replace(':', 'h', 1).replace(':', 'm') + 's'}"
        return f"{video_url}#t={int(t)}"

    def stamp(t):
        return f"**[{fmt_ts(t)}]({link(t)})** " if timestamps else ""

    sections = []
    if chapters:
        bounds = [c["start"] for c in chapters] + [float("inf")]
        for i, ch in enumerate(chapters):
            chunk = [s for s in segments if bounds[i] <= s["start"] < bounds[i + 1]]
            sections.append((ch, chunk))
    else:
        sections.append((None, segments))

    out = []
    for chapter, chunk in sections:
        if chapter:
            if timestamps:
                out.append(f"### [{fmt_ts(chapter['start'])}]({link(chapter['start'])}) {chapter['title']}\n")
            else:
                out.append(f"### {chapter['title']}\n")
        buf, buf_start, last_start = [], None, None
        for seg in chunk:
            if buf_start is None:
                buf_start = seg["start"]
            buf.append(seg["text"])
            last_start = seg["start"]
            if last_start - buf_start >= window:
                out.append(f"{stamp(buf_start)}{' '.join(buf)}\n")
                buf, buf_start = [], None
        if buf:
            out.append(f"{stamp(buf_start)}{' '.join(buf)}\n")
        out.append("")
    return "\n".join(out).strip()


def srt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def render_srt(segments) -> str:
    blocks = []
    for i, seg in enumerate(segments, 1):
        end = seg["start"] + seg["duration"]
        if i < len(segments):
            end = min(end, segments[i]["start"])
        end = max(end, seg["start"] + 0.5)
        blocks.append(f"{i}\n{srt_time(seg['start'])} --> {srt_time(end)}\n{seg['text']}\n")
    return "\n".join(blocks)


def render_video_md(meta, transcript, include_transcript=True, position=None, playlist=None, timestamps=True):
    vid = meta["id"]
    url = meta.get("url") or f"https://www.youtube.com/watch?v={vid}"
    platform = meta.get("platform", "video")

    lines = ["---",
             f"title: {yaml_str(meta['title'])}",
             f"video_id: {vid}",
             f"platform: {platform}",
             f"url: {url}",
             f"channel: {yaml_str(meta['channel'])}"]
    if meta.get("published"):
        lines.append(f"published: {meta['published']}")
    if meta.get("duration"):
        lines.append(f"duration: {fmt_ts(meta['duration'])}")
    if meta.get("views") is not None:
        lines.append(f"views: {meta['views']}")
    if playlist and position:
        lines.append(f"playlist: {yaml_str(playlist)}")
        lines.append(f"playlist_position: {position}")
    if transcript and "segments" in transcript:
        lines.append(f"transcript_language: {transcript['language']}")
        lines.append(f"transcript_generated: {str(transcript['generated']).lower()}")
        if transcript.get("source"):
            lines.append(f"transcript_source: {transcript['source']}")
    lines += ["---", "", f"# {meta['title']}", ""]

    info = [f"- **Plataforma:** {platform.capitalize()}", f"- **Link:** {url}"]
    if meta.get("channel"):
        info.append(f"- **Canal / Autor:** {meta['channel']}")
    if meta.get("published"):
        info.append(f"- **Publicado em:** {meta['published']}")
    if meta.get("duration"):
        info.append(f"- **Duração:** {fmt_ts(meta['duration'])}")
    if meta.get("views") is not None:
        info.append(f"- **Visualizações:** {meta['views']:,}".replace(",", "."))
    if meta.get("keywords"):
        info.append(f"- **Tags:** {', '.join(meta['keywords'][:15])}")

    thumbnail = meta.get("thumbnail")
    lines += info
    if thumbnail:
        lines += ["", f"[![Miniatura]({thumbnail})]({url})", ""]
    else:
        lines.append("")

    if meta.get("error"):
        lines += [f"> ⚠️ Metadados incompletos: {meta['error']}", ""]

    if meta.get("description", "").strip():
        lines += ["## Descrição", "", meta["description"].strip(), ""]

    if meta.get("chapters"):
        lines += ["## Capítulos", ""]
        for ch in meta["chapters"]:
            lines.append(f"- {fmt_ts(ch['start'])} {ch['title']}")
        lines.append("")

    if include_transcript:
        lines += ["## Transcrição", ""]
        if transcript and "segments" in transcript:
            source_lbl = f" via {transcript['source']}" if transcript.get("source") else ""
            kind = "gerada automaticamente" if transcript["generated"] else "manual"
            lines += [f"> Idioma: `{transcript['language']}` ({kind}{source_lbl}). "
                      "Legendas automáticas/transcrição por áudio podem conter erros de reconhecimento.", ""]
            lines.append(build_paragraphs(transcript["segments"], meta.get("chapters", []), url, timestamps=timestamps))
        else:
            reason = (transcript or {}).get("error", "Transcrição não solicitada.")
            lines.append(f"> ⚠️ Transcrição indisponível: {reason}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def render_index(title, source_url, results):
    ok = sum(1 for r in results if r["transcript"] == "ok")
    lines = [f"# {title}", "",
             f"> **Fonte:** {source_url}", f"> **Vídeos:** {len(results)} | **Com transcrição:** {ok}", "",
             "| # | Vídeo | Duração | Transcrição | Arquivo |", "| :-: | :--- | :-: | :-: | :--- |"]
    for r in results:
        status = {"ok": f"✅ {r.get('language', '')}", "skipped": "—"}.get(r["transcript"], "❌")
        lines.append(
            f"| {r['position']} | [{r['title']}]({r['url']}) | {r['duration'] or '—'} | {status} | "
            f"[{r['file']}]({r['file']}) |"
        )
    failed = [r for r in results if r["transcript"] not in ("ok", "skipped")]
    if failed:
        lines += ["", "## Vídeos sem transcrição", ""]
        for r in failed:
            lines.append(f"- {r['title']} — {r.get('note', '')}")
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #
# Core Processing Workflow
# --------------------------------------------------------------------------- #
def process_video(platform: str, video_id: str, url: str, title_hint: str,
                  out_dir: Path, position, args, playlist_title=None):
    prefix = f"{position:02d}-" if position else ""
    existing = list(out_dir.glob(f"{prefix}*-{video_id}.md")) if position else list(out_dir.glob(f"*-{video_id}.md"))

    if existing and not args.no_resume:
        text = existing[0].read_text(encoding="utf-8", errors="replace")
        ok = "## Transcrição" in text and "Transcrição indisponível" not in text
        if ok or args.no_transcript:
            m_title = re.search(r'^title: (".*")$', text, flags=re.M)
            m_dur = re.search(r"^duration: (\S+)$", text, flags=re.M)
            m_lang = re.search(r"^transcript_language: (\S+)$", text, flags=re.M)
            cached_title = json.loads(m_title.group(1)) if m_title else (title_hint or video_id)
            print(f"⏭️  [CACHE] {existing[0].name}")
            return {"position": position or 1, "id": video_id, "title": cached_title,
                    "url": url, "duration": m_dur.group(1) if m_dur else "",
                    "file": existing[0].name, "transcript": "ok" if ok else "skipped",
                    "language": m_lang.group(1) if m_lang else "", "note": "em cache"}
        print(f"🔁 Sem transcrição no cache, tentando de novo: {existing[0].name}")

    # 1. Fetch Metadata
    if platform == "youtube":
        meta = fetch_youtube_meta(video_id, title_hint)
    elif platform == "vimeo":
        meta = fetch_vimeo_meta(video_id, url)
    elif platform == "twitch":
        meta = fetch_twitch_meta(video_id, url)
    else:
        meta = {"id": video_id, "title": title_hint or video_id, "url": url, "duration": 0, "platform": platform}

    # 2. Fetch Transcript / Captions
    transcript = None
    if not args.no_transcript:
        if platform == "youtube":
            transcript = fetch_youtube_transcript(video_id, args.lang)
        else:
            # Vimeo / Twitch nativo via yt-dlp
            transcript = fetch_ytdlp_subtitles(url, args.lang)

        # Fallback de áudio se falhou a legenda nativa e foi solicitado
        if (not transcript or "segments" not in transcript) and args.fallback_audio:
            print(f"⚠️  Legendas indisponíveis para {url}. Acionando fallback por áudio...")
            transcript = fallback_audio_whisper(url, whisper_model=args.whisper_model)

    # 3. Render Output
    filename = f"{prefix}{slugify(meta['title'])}-{video_id}.md"
    md = render_video_md(meta, transcript, include_transcript=not args.no_transcript,
                         position=position, playlist=playlist_title, timestamps=not args.no_timestamps)
    (out_dir / filename).write_text(md, encoding="utf-8")

    if args.srt and transcript and "segments" in transcript:
        (out_dir / (Path(filename).stem + ".srt")).write_text(render_srt(transcript["segments"]), encoding="utf-8")

    if args.no_transcript:
        status = "skipped"
    elif transcript and "segments" in transcript:
        status = "ok"
    else:
        status = "unavailable"

    note = (transcript or {}).get("error", "")
    print(f"{'✅' if status != 'unavailable' else '⚠️ '} {filename}" + (f" — {note}" if note else ""))
    return {"position": position or 1, "id": video_id, "title": meta["title"],
            "url": url, "duration": fmt_ts(meta.get("duration", 0)) if meta.get("duration") else "",
            "file": filename, "transcript": status,
            "language": (transcript or {}).get("language", ""), "note": note}


# --------------------------------------------------------------------------- #
# YouTube Playlist listing
# --------------------------------------------------------------------------- #
def list_playlist_with_ytdlp(playlist_id: str):
    exe = shutil.which("yt-dlp")
    if not exe:
        return None
    try:
        out = subprocess.run(
            [exe, "--flat-playlist", "-J", f"https://www.youtube.com/playlist?list={playlist_id}"],
            capture_output=True, text=True, encoding="utf-8", timeout=180,
        )
        if out.returncode != 0:
            return None
        data = json.loads(out.stdout)
        entries = [
            {"id": e["id"], "title": e.get("title") or e["id"]}
            for e in data.get("entries", []) if e and e.get("id")
        ]
        return {"title": data.get("title") or playlist_id, "entries": entries,
                "declared": len(entries), "channel": data.get("channel") or data.get("uploader")}
    except Exception:
        return None


def list_playlist_from_page(playlist_id: str):
    page = http_get(f"https://www.youtube.com/playlist?list={playlist_id}")
    data = extract_json_blob(page, "ytInitialData = ")
    if not data:
        raise RuntimeError("Não consegui ler os dados da playlist (ytInitialData ausente).")

    title, channel, declared = playlist_id, None, None
    meta = data.get("metadata", {}).get("playlistMetadataRenderer", {})
    title = meta.get("title") or title

    entries, seen = [], set()
    for node in walk(data):
        if "lockupViewModel" in node:
            lvm = node["lockupViewModel"]
            vid = lvm.get("contentId")
            vt = (lvm.get("metadata", {}).get("lockupMetadataViewModel", {})
                  .get("title", {}).get("content"))
            if vid and VIDEO_ID_RE.match(vid) and vid not in seen:
                seen.add(vid)
                entries.append({"id": vid, "title": vt or vid})
        elif "playlistVideoRenderer" in node:
            pvr = node["playlistVideoRenderer"]
            vid = pvr.get("videoId")
            runs = pvr.get("title", {}).get("runs") or [{}]
            if vid and vid not in seen:
                seen.add(vid)
                entries.append({"id": vid, "title": runs[0].get("text") or vid})

    header = data.get("header", {})
    for node in walk(header):
        txt = node.get("simpleText") if isinstance(node, dict) else None
        if txt and re.fullmatch(r"\d+\s+(v[ií]deos?|videos?)", txt.strip(), re.I):
            declared = int(txt.split()[0])
            break
    for node in walk(header):
        content = node.get("content") if isinstance(node, dict) else None
        if isinstance(content, str) and re.fullmatch(r"\d+\s+(v[ií]deos?|videos?)", content.strip(), re.I):
            declared = int(content.split()[0])
            break

    return {"title": title, "entries": entries, "declared": declared, "channel": channel}


def list_playlist(playlist_id: str):
    via_ytdlp = list_playlist_with_ytdlp(playlist_id)
    if via_ytdlp and via_ytdlp["entries"]:
        return via_ytdlp
    info = list_playlist_from_page(playlist_id)
    if info["declared"] and len(info["entries"]) < info["declared"]:
        print(
            f"⚠️  A página retornou {len(info['entries'])} de {info['declared']} vídeos. "
            "Playlists grandes são paginadas; instale o yt-dlp (`pip install yt-dlp`) "
            "para listar todos."
        )
    return info


# --------------------------------------------------------------------------- #
# CLI Main
# --------------------------------------------------------------------------- #
def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser(description="Converte vídeos/playlists do YouTube, Vimeo e Twitch em Markdown.")
    ap.add_argument("url", help="URL do vídeo (YouTube/Vimeo/Twitch), playlist ou ID de 11 caracteres")
    ap.add_argument("output_dir", help="Diretório de saída")
    ap.add_argument("--lang", default="pt,pt-BR,en",
                    help="Idiomas de legenda preferidos (padrão: pt,pt-BR,en)")
    ap.add_argument("--no-transcript", action="store_true", help="Somente metadados e descrição")
    ap.add_argument("--no-timestamps", action="store_true",
                    help="Transcrição sem marcações de tempo (texto limpo)")
    ap.add_argument("--srt", action="store_true", help="Grava também um arquivo .srt por vídeo")
    ap.add_argument("--max-videos", type=int, default=0, help="Limita a quantidade de vídeos de uma playlist (0 = todos)")
    ap.add_argument("--start", type=int, default=1, help="Posição inicial na playlist (padrão: 1)")
    ap.add_argument("--delay-ms", type=int, default=15000, help="Pausa entre vídeos em ms (padrão: 15000 / 15s)")
    ap.add_argument("--combine", action="store_true", help="Gera também _ALL.md consolidado")
    ap.add_argument("--playlist", action="store_true", help="Força modo playlist se aplicável")
    ap.add_argument("--video", action="store_true", help="Força modo vídeo se aplicável")
    ap.add_argument("--no-resume", action="store_true", help="Reprocessa mesmo se o arquivo já existir")
    ap.add_argument("--fallback-audio", action="store_true",
                    help="Quando não houver legendas, baixa áudio e usa Whisper para transcrever")
    ap.add_argument("--whisper-model", default="base",
                    help="Modelo do Whisper a usar no fallback (tiny, base, small, medium, large)")

    args = ap.parse_args()
    args.lang = [l.strip() for l in args.lang.split(",") if l.strip()]

    try:
        platform, kind, ident, full_url = parse_target(args.url, args.playlist, args.video)
    except ValueError as e:
        print(f"❌ {e}")
        return 2

    out_dir = Path(args.output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    if kind == "video":
        print(f"🎬 Vídeo [{platform.upper()}]: {ident}")
        res = process_video(platform, ident, full_url, "", out_dir, None, args)
        (out_dir / "manifest.json").write_text(
            json.dumps({"type": "video", "platform": platform, "videos": [res]}, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )
        print(f"\n🎉 Concluído em: {out_dir}")
        return 0 if res["transcript"] != "unavailable" or args.no_transcript else 1

    # Playlist (YouTube)
    print(f"📚 Playlist [{platform.upper()}]: {ident}")
    info = list_playlist(ident)
    entries = info["entries"][args.start - 1:]
    if args.max_videos:
        entries = entries[:args.max_videos]
    if not entries:
        print("❌ Nenhum vídeo encontrado na playlist (privada ou vazia?).")
        return 1

    print(f"   ├─ Título: {info['title']}")
    print(f"   └─ Vídeos a processar: {len(entries)}\n")

    results = []
    for idx, item in enumerate(entries, start=args.start):
        vid = item["id"]
        v_url = f"https://www.youtube.com/watch?v={vid}"
        r = process_video("youtube", vid, v_url, item.get("title", ""), out_dir, idx, args, playlist_title=info["title"])
        results.append(r)
        if idx - args.start + 1 < len(entries):
            time.sleep(args.delay_ms / 1000.0)

    # _INDEX.md & manifest.json
    index_md = render_index(info["title"], full_url, results)
    (out_dir / "_INDEX.md").write_text(index_md, encoding="utf-8")
    manifest = {
        "type": "playlist", "platform": "youtube", "title": info["title"],
        "playlist_id": ident, "url": full_url, "total_processed": len(results),
        "videos": results,
    }
    (out_dir / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

    # _ALL.md
    if args.combine:
        chunks = []
        for r in results:
            fpath = out_dir / r["file"]
            if fpath.exists():
                chunks.append(fpath.read_text(encoding="utf-8"))
        (out_dir / "_ALL.md").write_text("\n\n---\n\n".join(chunks) + "\n", encoding="utf-8")

    ok_count = sum(1 for r in results if r["transcript"] == "ok")
    print(f"\n🎉 Concluído: {len(results)} vídeo(s), {ok_count} com transcrição. Índice: {out_dir / '_INDEX.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
