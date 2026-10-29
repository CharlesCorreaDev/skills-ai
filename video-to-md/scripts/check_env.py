#!/usr/bin/env python3
"""Verifica o ambiente da skill video-to-md / Environment check for video-to-md."""
import importlib.util
import shutil
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def has(pkg: str) -> bool:
    return importlib.util.find_spec(pkg) is not None


def main() -> int:
    ok = True
    missing = []

    print("📦 video-to-md — verificação de dependências\n")
    print(f"Python: {sys.version.split()[0]}\n")

    # --- Obrigatórias ---
    print("── Obrigatórias ──")
    for pkg, pip_name in (
        ("requests", "requests"),
        ("youtube_transcript_api", "youtube-transcript-api"),
    ):
        found = has(pkg)
        print(f"  {'✅' if found else '❌'} {pip_name}" + ("" if found else f"  →  pip install {pip_name}"))
        if not found:
            ok = False
            missing.append(pip_name)

    # yt-dlp (obrigatório para Vimeo/Twitch, recomendado para YouTube)
    ytdlp = shutil.which("yt-dlp") is not None
    print(f"  {'✅' if ytdlp else '❌'} yt-dlp" + ("" if ytdlp else "  →  pip install yt-dlp"))
    if not ytdlp:
        ok = False
        missing.append("yt-dlp")

    # --- Opcionais (fallback por áudio) ---
    print("\n── Opcionais (fallback por áudio) ──")

    whisperx = has("whisperx")
    whisper = has("whisper")
    whisper_ok = whisperx or whisper
    if whisperx:
        print("  ✅ whisperx")
    elif whisper:
        print("  ✅ openai-whisper")
    else:
        print("  ⚪ whisperx / openai-whisper  →  pip install whisperx  (necessário apenas com --fallback-audio)")

    ffmpeg = shutil.which("ffmpeg") is not None
    print(f"  {'✅' if ffmpeg else '⚪'} ffmpeg" + ("" if ffmpeg else "  →  instale via gerenciador do sistema (choco / apt / brew)"))

    # --- Resumo ---
    print("\n── Resumo ──")
    if ok:
        print("✅ Todas as dependências obrigatórias estão instaladas.")
        if whisper_ok and ffmpeg:
            print("✅ Fallback por áudio (Whisper) disponível.")
        else:
            print("⚪ Fallback por áudio indisponível (whisperx/whisper ou ffmpeg ausentes).")
        print("\n🎉 Tudo pronto para transcrição!")
    else:
        print(f"❌ Dependências ausentes: {', '.join(missing)}")
        print(f"\n   Para instalar: pip install {' '.join(missing)}")
        print("\n⚠️  Instale as dependências acima antes de usar a skill.")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
