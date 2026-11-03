#!/usr/bin/env python3
"""Verifica o ambiente da skill video-to-md / Environment check for video-to-md."""
import importlib.util
import shutil
import subprocess
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def has(pkg: str) -> bool:
    return importlib.util.find_spec(pkg) is not None


def check_github_cli():
    print("\n── Ferramenta Obrigatória: GitHub CLI (`gh`) ──")
    gh_bin = shutil.which("gh")
    if not gh_bin:
        print("  ❌ GitHub CLI (`gh`) NÃO encontrado no PATH.")
        print("     Instalação: winget install GitHub.cli (Windows) | brew install gh (macOS) | sudo apt install gh (Linux)")
        return False

    print("  ✅ GitHub CLI (`gh`) encontrado.")
    try:
        res = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True, encoding="utf-8")
        if res.returncode == 0:
            print("  ✅ Conta do GitHub conectada e autenticada via `gh`.")
            return True
        else:
            print("  ⚠️ GitHub CLI instalado, porém NÃO autenticado.")
            print("     👉 Execute agora: gh auth login (para conectar sua conta)")
            return False
    except Exception as e:
        print(f"  ⚠️ Erro ao verificar autenticação do gh: {e}")
        return False


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

    # GitHub CLI obrigatório para todas as skills
    gh_ok = check_github_cli()
    if not gh_ok:
        ok = False

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
        print("✅ Todas as dependências obrigatórias estão instaladas e GitHub CLI conectado.")
        if whisper_ok and ffmpeg:
            print("✅ Fallback por áudio (Whisper) disponível.")
        else:
            print("⚪ Fallback por áudio indisponível (whisperx/whisper ou ffmpeg ausentes).")
        print("\n🎉 Tudo pronto para transcrição!")
    else:
        if missing:
            print(f"❌ Dependências Python ausentes: {', '.join(missing)}")
            print(f"   Para instalar: pip install {' '.join(missing)}")
        if not gh_ok:
            print("⚠️ GitHub CLI ausente ou não autenticado. Execute `gh auth login` para conectar sua conta.")
        print("\n⚠️ Resolva as pendências acima antes de usar a skill.")

    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
