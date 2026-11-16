---
name: video-to-md
description: Converte vídeos do YouTube, Vimeo e Twitch (ou playlists) em Markdown estruturado com metadados, descrição, capítulos e transcrição de áudio/legendas. Use when transcribing online videos, converting YouTube playlists to markdown documentation, extracting speech transcripts, or indexing video lectures into a knowledge base.
---

# Video to Markdown 🎬➡️📝

## Visão geral
`video-to-md` (`v0.2.0‑beta`) captura **vídeos individuais** e **playlists** dos serviços **YouTube**, **Vimeo** e **Twitch** e gera arquivos Markdown prontos para leitura humana ou posterior processamento por agentes. Cada arquivo contém:
- Metadados (título, canal/autor, data, duração, visualizações, etc.)
- Descrição do vídeo
- Capítulos detectados a partir da descrição
- Transcrição completa **com timestamps clicáveis**
  - Primeiro tenta usar legendas nativas (captions) disponíveis.
  - Quando não houver legendas, pode‑se habilitar o **fallback por áudio** (Whisper/WhisperX) que baixa o áudio e gera a transcrição.

---

## Dependências

### Obrigatórias (sempre necessárias)
| Pacote | Finalidade |
|---|---|
| `requests` | Requisições HTTP para obter metadados dos vídeos. |
| `youtube-transcript-api` | Captura legendas do YouTube (manual e automática). |
| `yt-dlp` | Extração de metadados e legendas de **YouTube**, **Vimeo** e **Twitch**; download de áudio para fallback. |

### Opcionais (apenas se usar `--fallback-audio`)
| Pacote | Finalidade |
|---|---|
| `whisperx` (ou `openai-whisper`) | Transcrição de áudio por IA (speech‑to‑text) quando não houver legendas disponíveis. |
| `ffmpeg` | Conversão e manipulação de áudio (exigido pelo Whisper). Deve estar no PATH do sistema. |

### Fluxo do agente para verificação e instalação
> **O agente DEVE seguir estes passos antes de executar qualquer transcrição:**

1. **Verificar dependências** — executar `python scripts/check_env.py` e analisar a saída.
2. **Informar o usuário** — apresentar a lista de dependências encontradas (✅) e ausentes (❌) de forma clara:
   ```
   📦 Verificação de dependências — video‑to‑md

   ✅ requests
   ✅ youtube-transcript-api
   ❌ yt-dlp                  ← necessário para Vimeo/Twitch e playlists grandes
   ❌ whisperx                ← necessário apenas com --fallback-audio
   ❌ ffmpeg                  ← necessário apenas com --fallback-audio
   ```
3. **Pedir aprovação** — perguntar ao usuário:
   > "Posso instalar as dependências ausentes? (yt‑dlp, whisperx, etc.)"
4. **Instalar** — após aprovação, executar os comandos de instalação:
   ```bash
   pip install requests youtube-transcript-api yt-dlp
   # Se o usuário deseja fallback por áudio:
   pip install whisperx    # ou: pip install openai-whisper
   # ffmpeg deve ser instalado pelo sistema (ex.: choco install ffmpeg, apt install ffmpeg, brew install ffmpeg)
   ```
5. **Confirmar** — executar `check_env.py` novamente e informar:
   > "✅ Todas as dependências estão instaladas. Tudo pronto para transcrição!"
6. **Só então** prosseguir com a transcrição.

> ⚠️ **Nunca instalar dependências sem aprovação explícita do usuário.**

---

## Uso rápido
```bash
# Verificar ambiente (primeira execução)
python scripts/check_env.py

# Vídeo único (YouTube, Vimeo ou Twitch)
python scripts/video_to_md.py "<url‑de‑vídeo>" "saida" [--lang pt,en] [--fallback-audio]

# Playlist completa (YouTube)
python scripts/video_to_md.py "<url‑da‑playlist>" "saida" [--start 1] [--max-videos 0]

# Gerar um arquivo consolidado com todas as transcrições
python scripts/video_to_md.py "<url‑da‑playlist>" "saida" --combine

# Apenas metadados (sem transcrição)
python scripts/video_to_md.py "<url>" "saida" --no-transcript
```

## Opções da linha de comando
| Opção | Padrão | Descrição |
|---|---:|---|
| `--lang` | `pt,pt-BR,en` | Idiomas de legenda a serem procurados (primeiro o manual, depois automático). |
| `--no-transcript` | `false` | Gera somente metadados e descrição, sem transcrição. |
| `--max-videos` | `0` (todos) | Limita a quantidade de vídeos a processar em uma playlist. |
| `--start` | `1` | Posição inicial na playlist. |
| `--delay-ms` | `15000` | Pausa entre a requisição de cada vídeo (15 s) – ajuda a evitar bloqueios por taxa. |
| `--combine` | `false` | Gera um `_ALL.md` contendo a concatenação de todas as transcrições da playlist. |
| `--fallback-audio` | `false` | Quando não houver legendas, baixa o áudio e usa Whisper/WhisperX para gerar a transcrição. |
| `--whisper-model` | `base` | Modelo Whisper a ser usado no fallback (ex.: `tiny`, `small`, `medium`, `large`). |
| `--no-resume` | `false` | Reprocessa arquivos que já existam, ignorando o cache. |

---

## Fluxo de trabalho completo do agente

```
┌──────────────────────────────────────────────────────────┐
│  1. VERIFICAR DEPENDÊNCIAS                               │
│     Executar check_env.py                                │
│     Listar ✅ instaladas e ❌ ausentes                    │
│     Perguntar ao usuário se pode instalar as ausentes    │
├──────────────────────────────────────────────────────────┤
│  2. INSTALAR (após aprovação)                            │
│     pip install <pacotes ausentes>                       │
│     Re‑executar check_env.py                             │
│     Confirmar: "Tudo pronto para transcrição!"           │
├──────────────────────────────────────────────────────────┤
│  3. EXECUTAR TRANSCRIÇÃO                                 │
│     Rodar video_to_md.py com a URL e flags do usuário    │
├──────────────────────────────────────────────────────────┤
│  4. VERIFICAR RESULTADO                                  │
│     Ler _INDEX.md e conferir quais vídeos têm transcrição│
│     Avisar sobre vídeos sem legenda                      │
├──────────────────────────────────────────────────────────┤
│  5. CONSOLIDAÇÃO (perguntar ao usuário)                  │
│     Deseja gerar um documento único (manual/blog/livro)  │
│     a partir das transcrições, sem citar as fontes?      │
│     → Se sim: gerar CONSOLIDADO.md                       │
│     → Se não: pular                                      │
├──────────────────────────────────────────────────────────┤
│  6. LIMPEZA (perguntar ao usuário)                       │
│     Manter ou excluir as transcrições individuais?       │
│     → Se excluir: remover *.md (manter _INDEX e manifest)│
│     → Se manter: deixar como está                        │
├──────────────────────────────────────────────────────────┤
│  7. FEEDBACK FINAL                                       │
│     Informar status: consolidado criado, transcrições    │
│     mantidas ou removidas, total de vídeos processados.  │
├──────────────────────────────────────────────────────────┤
│  8. TRATAMENTO DE ERROS (se houver falhas)               │
│     a) Comunicar o usuário com detalhes do erro.         │
│     b) Perguntar se deseja abrir uma issue no repo.      │
│     c) Se sim: criar issue bilíngue (pt-BR + EN)         │
│        com diagnóstico, sugestões e logs relevantes.     │
└──────────────────────────────────────────────────────────┘
```

---

## Tratamento de Erros & Abertura de Issues
Consulte as diretrizes de diagnóstico, formato de issues bilíngue e labels em [references/error-handling-and-issues.md](references/error-handling-and-issues.md).

## Limitações conhecidas
- **Legendas são a primeira opção**; nem todos os vídeos de Vimeo/Twitch possuem legendas embutidas. O fallback por áudio pode ser custoso em termos de tempo e recursos.
- **Bloqueio por taxa** – YouTube pode bloquear temporariamente o IP se houver muitas requisições rápidas. O parâmetro `--delay‑ms` (padrão 15 s) ajuda a mitigar; aumente o valor ou troque de rede se necessário.
- **Playlists grandes** – sem `yt-dlp` a extração de playlists pode ser incompleta; recomenda‑se manter `yt-dlp` instalado.
- **Vídeos privados, removidos ou com restrição de idade/região** – podem gerar apenas metadados parciais.
- **Canais** – não são aceitos diretamente; use URLs de vídeos ou playlists.
- **Dependência de Whisper** – requer `ffmpeg` e, para melhor desempenho, hardware compatível (GPU). Em CPUs, o tempo de transcrição pode ser elevado.

---

## Arquivos principais
- [`scripts/video_to_md.py`](scripts/video_to_md.py) — motor principal de transcrição.
- [`scripts/check_env.py`](scripts/check_env.py) — verificação de dependências.
- [`README.md`](README.md) — guia rápido de uso.
- [`CHANGELOG.md`](CHANGELOG.md) — histórico de versões.
- [`VERSION`](VERSION) — número da versão.


---

## Arquivos Principais
- [scripts/video_to_md.py](scripts/video_to_md.py) — motor principal de transcrição.
- [scripts/check_env.py](scripts/check_env.py) — verificação de dependências.
- [
eferences/error-handling-and-issues.md](references/error-handling-and-issues.md) — protocolo de issues.
