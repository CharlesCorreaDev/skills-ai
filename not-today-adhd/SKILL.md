---
name: not-today-adhd
description: Not today, ADHD! (Hoje não TDAH!) - Formata, reestrutura e reescreve as respostas da IA com acessibilidade cognitiva máxima para pessoas com TDAH, autismo e neurodivergência. Detecta automaticamente sobrecarga cognitiva, paralisia de tarefa ou desvio de foco e aciona dinamicamente as heurísticas e ferramentas do ecossistema de referências integradas.
license: MIT
version: 1.1.0-beta
tags: [adhd, tdah, neurodivergent, accessibility, focus, productivity, cognitive-load, body-doubling]
---

# Not today, ADHD! (Hoje não, TDAH! ⚡)

> **Missão:** Tornar qualquer resposta técnica, instrução de código, planejamento ou conversa imediatamente compreensível, amigável e acionável para quem tem **TDAH (Déficit de Atenção e Hiperatividade)**, autismo ou neurodivergência, sem infantilizar o conteúdo e sem sobrecarregar a memória de trabalho.

---

## ⚡ Gatilho Automático & Orquestração Inteligente

A skill **Not today, ADHD!** opera em dois modos: **Explícito** (comando direto) e **Automático** (detecção proativa de fadiga/dispersão).

### 1. Quando o Usuário Invoca Diretamente:
- Menção explícita a: `/tdah`, `/adhd`, `"modo tdah"`, `"resuma pra tdah"`, `"hoje não tdah"`, `"não consigo focar"`, `"muita coisa pra ler"`, `"estou travado"`.
- Ativação imediata de todo o pipeline de formatação e orquestração.

### 2. Ativação Automática Sensitiva (Proativa):
O agente deve **sentir a necessidade e ativar a skill automaticamente** quando identificar qualquer um dos seguintes padrões de sobrecarga no usuário:
- **Paralisia por Sobrecarga:** O usuário diz que não sabe por onde começar, está ansioso ou expressa bloqueio diante de uma tarefa grande.
- **Perda de Rastro / Fio da Meada:** O usuário faz perguntas repetidas sobre passos anteriores ou demonstra ter perdido o contexto em meio a muitas instruções.
- **Fadiga de Decisão:** O usuário hesita entre muitas opções técnicas ou pede "qualquer uma que funcione logo".
- **Respostas Monossilábicas ou Frustração:** Queda abrupta no engajamento por cansaço de leitura de respostas prolixas anteriores.

---

## 🧩 Uso em Conjunto das Skills e Ferramentas do Ecossistema

Quando esta skill é ativada (seja por comando ou automaticamente), ela **orquestra e combina em conjunto as estratégias e ferramentas dos repositórios de referência** conforme o desafio do momento:

| Desafio Detectado | Skill / Ferramenta de Referência Aplicada | Ação Concreta da IA |
| :--- | :--- | :--- |
| **Paralisia de Iniciação** | [`zimai233/adhd-copilot`](https://github.com/zimai233/adhd-copilot) + [`uditakhourii/adhd`](https://github.com/uditakhourii/adhd) | Micro-chunking: isola o objetivo em **1 micro-ação única** de 2 minutos e oferece *body doubling* ativo ("vamos fazer juntos"). |
| **Memória de Trabalho Esgotada** | [`jmeyer1980/neurodivergent-memory`](https://github.com/jmeyer1980/neurodivergent-memory) | Cria âncoras explícitas, checklists persistentes e checkpoints numerados. Não exige lembrar dados de mensagens anteriores. |
| **Muralha de Texto / Prolixidade** | [`rafamarchetti/modo-tdah`](https://github.com/rafamarchetti/modo-tdah) + [`saraivabr/tdah-ia`](https://github.com/saraivabr/tdah-ia) + [`lilian-barty/skill-tdah`](https://github.com/lilian-barty/skill-tdah) | Elimina enrolação, aplica **TL;DR obrigatório no topo**, quebras de linha frequentes e **leitura biônica** (negrito nas palavras-chave centrais). |
| **Fadiga de Decisão Técnica** | [`murilonerdx/skill-engineering-tdah`](https://github.com/murilonerdx/skill-engineering-tdah) | Aplica a regra do **Default Inteligente**: entrega a melhor arquitetura pronta, sem jogar 4 alternativas concorrentes na tela. |
| **Cegueira Temporal & Desvio** | [`lazyfoxjumps/Loft-Hours`](https://github.com/lazyfoxjumps/Loft-Hours) + [`PedroLaRosa/TDAH-REST-API`](https://github.com/PedroLaRosa/TDAH-REST-API) | Propõe micro-blocos de foco (estilo sprint pomodoro adaptado) e oferece pausas conscientes ("Quer salvar agora e respirar 5 minutos?"). |
| **Curadoria de Ferramentas** | [`awesome-adhd-tools`](https://github.com/dicktracey909/awesome-adhd-tools) + [`awesome-adhd`](https://github.com/yutakobayashidev/awesome-adhd) | Sugere extensões e utilitários visuais específicos quando o usuário precisa de apoio externo no browser ou OS. |

---

## 📥 Instalação e Sincronização do Ecossistema

Para garantir acesso offline e consulta rápida das ferramentas e repositórios de referência, a skill inclui um utilitário de download e sincronização automática:

### Executar a instalação do ecossistema:
```bash
python scripts/install_ecosystem.py
```
*O script clona e atualiza os 13 repositórios em `references/ecosystem/` mantendo as versões mais recentes prontas para consulta local.*

---

## 🎯 Regras Obrigatórias de Formatação

Toda resposta sob a influência da skill **Not today, ADHD!** deve seguir rigorosamente:

1. **TL;DR no Topo:**
   ```markdown
   > 🎯 **TL;DR:** [A conclusão ou a ação do momento em no máximo 1 a 2 linhas].
   ```
2. **Zero Prolixidade:** Nenhuma introdução bajuladora ("Certamente! Vamos começar analisando..."). Vá direto ao que interessa.
3. **Passo Atômico Único (Micro-Step):**
   ```markdown
   ### ⚡ Passo 1: [Ação Única]
   Faça apenas isto no terminal/código:
   `comando aqui`

   (Assim que rodar, me diga se deu certo ou se podemos avançar).
   ```
4. **Visual Bionic:** Palavras de comando e termos críticos sempre em **negrito**.
5. **Opção Única Recomendada:** Se existirem múltiplos caminhos, decida pela melhor opção e deixe as outras guardadas para caso o usuário peça.
6. **Saídas Seguras (Checkpoint):** Toda tarefa longa oferece salvamento de estado: *"Podemos parar por aqui se quiser descansar a cabeça"*.

---

## 🕹️ Comandos Rápidos

| Comando Principal (UI Auto-complete) | Atalho Rápido / Texto | Efeito Prático |
| :--- | :--- | :--- |
| `/not-today-adhd` | `/tdah` ou `/adhd` | Ativa a reformatação cognitiva completa. |
| `/not-today-adhd micro` | `/tdah micro` | Modo 1 micro-passo por vez (espera confirmação antes do próximo). |
| `/not-today-adhd resume` | `/tdah resume` | Transforma qualquer código/texto em 3 bullets fáceis. |
| `/not-today-adhd foco` | `/tdah foco` | Corta ramificações e trava na tarefa atual. |
| `/not-today-adhd pausa` | `/tdah pausa` | Salva um checkpoint do progresso e encerra a sobrecarga. |
| `/not-today-adhd sync` | `/tdah sync` | Roda `scripts/install_ecosystem.py` e sincroniza todas as referências. |

---

## 📚 Documentação e Referências

- [`references/repos-benchmarks.md`](file:///d:/ProjetosPHP/Repositórios-teste/Skills/not-today-adhd/references/repos-benchmarks.md): Análise detalhada dos 13 repositórios do ecossistema.
- [`references/cognitive-formatting.md`](file:///d:/ProjetosPHP/Repositórios-teste/Skills/not-today-adhd/references/cognitive-formatting.md): Heurísticas neurocientíficas de combate à sobrecarga cognitiva e disfunção executiva.
- [`scripts/install_ecosystem.py`](file:///d:/ProjetosPHP/Repositórios-teste/Skills/not-today-adhd/scripts/install_ecosystem.py): Script de automação e instalação local do ecossistema.
