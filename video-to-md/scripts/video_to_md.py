#!/usr/bin/env python3
"""
youtube_to_md.py - Converte vídeos soltos e playlists do YouTube em Markdown.
Converts single YouTube videos and playlists into Markdown.

Para cada vídeo gera um .md com metadados, descrição, capítulos e transcrição
(legendas) com timestamps clicáveis. Para playlists gera também _INDEX.md e
manifest.json (e, opcionalmente, um _ALL.md consolidado).

Dependências / Dependencies:
  - requests                 (obrigatória)
  - youtube-transcript-api   (obrigatória para transcrições, >= 1.0)
  - yt-dlp                   (opcional: enumeração de playlists grandes)

Uso / Usage:
  python youtube_to_md.py "<url>" "<output_dir>" [--lang pt,pt-BR,en] [--combine]
"""

import argparse
import html
import json
import re
import shutil
import subprocess
import sys
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
# URL parsing
# --------------------------------------------------------------------------- #
def parse_target(url: str, force_playlist: bool = False, force_video: bool = False):
    """Return ('video', id) or ('playlist', id). Raise ValueError otherwise."""
    url = url.strip()
    if VIDEO_ID_RE.match(url):
        return "video", url

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
    else:
        raise ValueError(f"URL não reconhecida como YouTube: {url}")

    playlist_id = (query.get("list") or [None])[0]
    is_playlist_page = parsed.path == "/playlist"

    if force_video and video_id:
        return "video", video_id
    if playlist_id and (is_playlist_page or force_playlist or not video_id):
        return "playlist", playlist_id
    if video_id and VIDEO_ID_RE.match(video_id):
        return "video", video_id
    raise ValueError(
        "Não encontrei um vídeo ou playlist na URL. Canais não são suportados diretamente; "
        "passe a URL da playlist (ex.: /playlist?list=...) ou do vídeo."
    )


# --------------------------------------------------------------------------- #
# HTTP helpers
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
    """Extract the JSON object that follows `marker` (e.g. 'ytInitialData = ')."""
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
    """Yield every dict found inside a nested JSON structure."""
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk(v)
    elif isinstance(node, list):
        for item in node:
            yield from walk(item)


# --------------------------------------------------------------------------- #
# Playlist enumeration
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
# Video metadata
# --------------------------------------------------------------------------- #
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
    """Chapters follow YouTube's rule: >= 2 timestamped lines, the first at 0:00."""
    found = []
    for line in description.splitlines():
        m = CHAPTER_RE.match(line)
        if m:
            found.append({"start": parse_timestamp(m.group(1)), "title": m.group(2)})
    if len(found) >= 2 and found[0]["start"] == 0:
        return found
    return []


def fetch_video_meta(video_id: str, fallback_title: str = ""):
    meta = {
        "id": video_id, "title": fallback_title or video_id, "channel": "", "channel_id": "",
        "duration": 0, "views": None, "published": "", "description": "",
        "keywords": [], "chapters": [],
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


# --------------------------------------------------------------------------- #
# Transcript
# --------------------------------------------------------------------------- #
def fetch_transcript(video_id: str, languages):
    """Return dict(segments, language, generated) or dict(error=...)."""
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
                    for t in transcripts:  # any available language
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
        except Exception as e:  # noqa: BLE001 - library raises many specific errors
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
    return {"error": "Falha desconhecida ao obter a transcrição."}


def build_paragraphs(segments, chapters, video_id: str, window: int = 60, timestamps: bool = True):
    """Group segments into paragraphs, split by chapters when available."""
    def link(t):
        return f"https://youtu.be/{video_id}?t={int(t)}"

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
            end = min(end, segments[i]["start"])  # evita sobreposição de legendas
        end = max(end, seg["start"] + 0.5)
        blocks.append(f"{i}\n{srt_time(seg['start'])} --> {srt_time(end)}\n{seg['text']}\n")
    return "\n".join(blocks)


# --------------------------------------------------------------------------- #
# Markdown rendering
# --------------------------------------------------------------------------- #
def slugify(text: str, max_len: int = 60) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text[:max_len].strip("-") or "video"


def yaml_str(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_video_md(meta, transcript, include_transcript=True, position=None, playlist=None, timestamps=True):
    vid = meta["id"]
    url = f"https://www.youtube.com/watch?v={vid}"
    lines = ["---",
             f"title: {yaml_str(meta['title'])}",
             f"video_id: {vid}",
             f"url: {url}",
             f"channel: {yaml_str(meta['channel'])}"]
    if meta["published"]:
        lines.append(f"published: {meta['published']}")
    if meta["duration"]:
        lines.append(f"duration: {fmt_ts(meta['duration'])}")
    if meta["views"] is not None:
        lines.append(f"views: {meta['views']}")
    if playlist and position:
        lines.append(f"playlist: {yaml_str(playlist)}")
        lines.append(f"playlist_position: {position}")
    if transcript and "segments" in transcript:
        lines.append(f"transcript_language: {transcript['language']}")
        lines.append(f"transcript_generated: {str(transcript['generated']).lower()}")
    lines += ["---", "", f"# {meta['title']}", ""]

    info = [f"- **Link:** {url}"]
    if meta["channel"]:
        info.append(f"- **Canal:** {meta['channel']}")
    if meta["published"]:
        info.append(f"- **Publicado em:** {meta['published']}")
    if meta["duration"]:
        info.append(f"- **Duração:** {fmt_ts(meta['duration'])}")
    if meta["views"] is not None:
        info.append(f"- **Visualizações:** {meta['views']:,}".replace(",", "."))
    if meta["keywords"]:
        info.append(f"- **Tags:** {', '.join(meta['keywords'][:15])}")
    lines += info + ["", f"[![Miniatura](https://i.ytimg.com/vi/{vid}/hqdefault.jpg)]({url})", ""]

    if meta.get("error"):
        lines += [f"> ⚠️ Metadados incompletos: {meta['error']}", ""]

    if meta["description"].strip():
        lines += ["## Descrição", "", meta["description"].strip(), ""]

    if meta["chapters"]:
        lines += ["## Capítulos", ""]
        for ch in meta["chapters"]:
            lines.append(f"- [{fmt_ts(ch['start'])}](https://youtu.be/{vid}?t={ch['start']}) {ch['title']}")
        lines.append("")

    if include_transcript:
        lines += ["## Transcrição", ""]
        if transcript and "segments" in transcript:
            kind = "gerada automaticamente" if transcript["generated"] else "manual"
            lines += [f"> Idioma: `{transcript['language']}` ({kind}). "
                      "Legendas automáticas podem conter erros de reconhecimento.", ""]
            lines.append(build_paragraphs(transcript["segments"], meta["chapters"], vid, timestamps=timestamps))
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
# Main workflow
# --------------------------------------------------------------------------- #
def process_video(video_id, title_hint, out_dir: Path, position, args, playlist_title=None):
    prefix = f"{position:02d}-" if position else ""
    existing = list(out_dir.glob(f"{prefix}*-{video_id}.md")) if position else list(out_dir.glob(f"*-{video_id}.md"))
    if existing and not args.no_resume:
        text = existing[0].read_text(encoding="utf-8", errors="replace")
        ok = "## Transcrição" in text and "Transcrição indisponível" not in text
        # Arquivo sem transcrição só é reaproveitado se a transcrição não foi pedida;
        # caso contrário tenta de novo (ex.: bloqueio temporário do YouTube).
        if ok or args.no_transcript:
            m_title = re.search(r'^title: (".*")$', text, flags=re.M)
            m_dur = re.search(r"^duration: (\S+)$", text, flags=re.M)
            m_lang = re.search(r"^transcript_language: (\S+)$", text, flags=re.M)
            cached_title = json.loads(m_title.group(1)) if m_title else (title_hint or video_id)
            print(f"⏭️  [CACHE] {existing[0].name}")
            return {"position": position or 1, "id": video_id, "title": cached_title,
                    "url": f"https://www.youtube.com/watch?v={video_id}",
                    "duration": m_dur.group(1) if m_dur else "",
                    "file": existing[0].name, "transcript": "ok" if ok else "skipped",
                    "language": m_lang.group(1) if m_lang else "", "note": "em cache"}
        print(f"🔁 Sem transcrição no cache, tentando de novo: {existing[0].name}")

    meta = fetch_video_meta(video_id, title_hint)
    transcript = None
    if not args.no_transcript:
        transcript = fetch_transcript(video_id, args.lang)

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
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "duration": fmt_ts(meta["duration"]) if meta["duration"] else "",
            "file": filename, "transcript": status,
            "language": (transcript or {}).get("language", ""), "note": note}


def main():
    # Extend support to Vimeo and Twitch URLs
    # Detect platform based on netloc and route to appropriate handlers
    pass
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser(description="Converte vídeos/playlists do YouTube em Markdown.")
    ap.add_argument("url", help="URL de vídeo (watch, youtu.be, shorts), de playlist ou ID de 11 caracteres")
    ap.add_argument("output_dir", help="Diretório de saída")
    ap.add_argument("--lang", default="pt,pt-BR,en",
                    help="Idiomas de legenda preferidos, em ordem (padrão: pt,pt-BR,en)")
    ap.add_argument("--no-transcript", action="store_true", help="Somente metadados e descrição")
    ap.add_argument("--no-timestamps", action="store_true",
                    help="Transcrição sem marcações de tempo (texto mais limpo e menos tokens)")
    ap.add_argument("--srt", action="store_true", help="Grava também um arquivo .srt por vídeo")
    ap.add_argument("--max-videos", type=int, default=0, help="Limita a quantidade de vídeos (0 = todos)")
    ap.add_argument("--start", type=int, default=1, help="Posição inicial na playlist (padrão: 1)")
    ap.add_argument("--delay-ms", type=int, default=1500, help="Pausa entre vídeos (padrão: 1500)")
    ap.add_argument("--combine", action="store_true", help="Gera também _ALL.md com tudo em um arquivo")
    ap.add_argument("--playlist", action="store_true", help="Se a URL tiver vídeo e list=, força a playlist")
    ap.add_argument("--video", action="store_true", help="Se a URL tiver vídeo e list=, força só o vídeo")
    ap.add_argument("--no-resume", action="store_true", help="Reprocessa mesmo se o .md já existir")
    args = ap.parse_args()
    args.lang = [l.strip() for l in args.lang.split(",") if l.strip()]

    try:
        kind, ident = parse_target(args.url, args.playlist, args.video)
    except ValueError as e:
        print(f"❌ {e}")
        return 2

    out_dir = Path(args.output_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    if kind == "video":
        print(f"🎬 Vídeo: {ident}")
        res = process_video(ident, "", out_dir, None, args)
        (out_dir / "manifest.json").write_text(
            json.dumps({"type": "video", "videos": [res]}, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\n🎉 Concluído em: {out_dir}")
        return 0 if res["transcript"] != "unavailable" or args.no_transcript else 1

    print(f"📚 Playlist: {ident}")
    info = list_playlist(ident)
    entries = info["entries"][args.start - 1:]
    if args.max_videos:
        entries = entries[:args.max_videos]
    if not entries:
        print("❌ Nenhum vídeo encontrado na playlist (privada ou vazia?).")
        return 1
    print(f"   ├─ Título: {info['title']}\n   └─ Vídeos a processar: {len(entries)}\n")

    results = []
    for offset, entry in enumerate(entries):
        position = args.start + offset
        results.append(process_video(entry["id"], entry["title"], out_dir, position, args, info["title"]))
        if offset < len(entries) - 1:
            time.sleep(args.delay_ms / 1000)

    source = f"https://www.youtube.com/playlist?list={ident}"
    (out_dir / "_INDEX.md").write_text(render_index(info["title"], source, results), encoding="utf-8")
    (out_dir / "manifest.json").write_text(json.dumps(
        {"type": "playlist", "playlist_id": ident, "title": info["title"], "source": source,
         "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "videos": results},
        indent=2, ensure_ascii=False), encoding="utf-8")

    if args.combine:
        parts = [f"# {info['title']}\n\n> Fonte: {source}\n"]
        for r in results:
            body = (out_dir / r["file"]).read_text(encoding="utf-8", errors="replace")
            body = re.sub(r"\A---\n.*?\n---\n", "", body, flags=re.S).strip()
            body = re.sub(r"^(#{1,5}) ", lambda m: m.group(1) + "# ", body, flags=re.M)
            parts.append(f"\n\n---\n\n{body}\n")
        (out_dir / "_ALL.md").write_text("".join(parts), encoding="utf-8")
        print("📦 _ALL.md gerado.")

    ok = sum(1 for r in results if r["transcript"] == "ok")
    print(f"\n🎉 Concluído: {len(results)} vídeo(s), {ok} com transcrição. Índice: {out_dir / '_INDEX.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
