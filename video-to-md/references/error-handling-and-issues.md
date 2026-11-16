## Tratamento de erros e abertura de issues

Quando ocorrer **qualquer erro** durante a transcrição (legendas indisponíveis, bloqueio do YouTube, falha no Whisper, dependência faltando, etc.), o agente **DEVE**:

### 1. Comunicar o usuário
Informar claramente:
- **O que aconteceu** – qual vídeo falhou, qual etapa (legendas? áudio? Whisper?).
- **Possível causa** – rate‑limit, vídeo privado, dependência ausente, etc.
- **Sugestão de solução** – aumentar `--delay-ms`, instalar dependência X, tentar outra rede, usar `--fallback-audio`, etc.

### 2. Perguntar se deseja abrir uma issue
> "Ocorreu um erro na transcrição. Deseja que eu abra uma issue no repositório da skill com os detalhes do problema?"

### 3. Criar a issue (após aprovação)
Usar a ferramenta do GitHub (MCP `github > create_issue`) para abrir a issue no repositório da skill. A issue deve ser **bilíngue (pt‑BR + English)** com a seguinte estrutura:

```markdown
# 🐛 [pt-BR] Erro na transcrição: <descrição curta>

## Contexto
- **Plataforma:** YouTube / Vimeo / Twitch
- **URL do vídeo:** `<url>`
- **Flags usadas:** `--lang pt --fallback-audio` (exemplo)
- **Sistema operacional:** Windows / Linux / macOS
- **Python:** <versão>
- **Dependências instaladas:** requests ✅, yt-dlp ✅, whisperx ❌, etc.

## Erro encontrado
<descrição detalhada do erro, incluindo mensagem de erro e stack trace se houver>

## Diagnóstico
<análise do agente sobre a causa raiz>

## Sugestão de melhoria
- [ ] Usar outra dependência (ex.: `whisperx` em vez de `openai-whisper`)
- [ ] Implementar retry com backoff exponencial
- [ ] Adicionar suporte a <funcionalidade>
- [ ] Melhorar tratamento de <caso específico>

---

# 🐛 [EN] Transcription error: <short description>

## Context
- **Platform:** YouTube / Vimeo / Twitch
- **Video URL:** `<url>`
- **Flags used:** `--lang pt --fallback-audio` (example)
- **OS:** Windows / Linux / macOS
- **Python:** <version>
- **Installed deps:** requests ✅, yt-dlp ✅, whisperx ❌, etc.

## Error
<detailed error description, including error message and stack trace if available>

## Diagnosis
<agent's analysis of root cause>

## Suggested improvement
- [ ] Use alternative dependency (e.g., `whisperx` instead of `openai-whisper`)
- [ ] Implement retry with exponential backoff
- [ ] Add support for <feature>
- [ ] Improve handling of <specific case>
```

### Labels recomendadas
- `bug` — quando o erro é um defeito no script.
- `enhancement` — quando a sugestão é uma melhoria ou nova funcionalidade.
- `dependencies` — quando o problema envolve pacotes externos.
- `help wanted` — quando o agente não consegue resolver sozinho.

> ⚠️ **Nunca abrir issue sem aprovação do usuário.**
> ⚠️ **Nunca incluir dados sensíveis** (tokens, senhas, caminhos pessoais) na issue.

---

