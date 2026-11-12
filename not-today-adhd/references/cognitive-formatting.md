# Formatação Cognitiva Amigável & Acessibilidade Sensorial (TEA / TDAH) 🧠⚡

> **Fundamentação Científica & Padrões Clínicos:**
> - Dissertação de Mestrado PPGDesign/UFPE (2025): *Acessibilidade em UX/UI e Matriz dos 7 Vetores para Autismo* — Lucas Silva.
> - Relatos de UX Designers Autistas (*Brasil UX Design*, *Ladies That UX BR*, *r/UXDesign*).
> - Estudos de Sobrecarga Sensorial e Acústica (*Interference Journal*).
> - Neurociência e Ergonomia Cognitiva para TDAH (*Revista Projética/UEL*, *DIO.me*, *Fast Company*, *Homem Máquina*).

---

## 🧭 Desafios Centrais da Neurodivergência (TDAH & TEA)

Pessoas com TDAH, autismo e condições correlatas enfrentam barreiras cognitivas específicas diante de interfaces e assistentes de IA:

1. **Memória de Trabalho Reduzida (Working Memory):** Dificuldade de reter múltiplos fatos temporários ao mesmo tempo.
2. **Cegueira Temporal (Time Blindness):** Dificuldade de estimar tempo ou priorizar o que vem primeiro sem ancoragem clara.
3. **Paralisia de Iniciação (Task Paralysis / Executive Dysfunction):** Uma tarefa grande parece uma montanha intransponível.
4. **Sobrecarga Sensorial (Sensory Overload):** Sons imprevisíveis, animações não solicitadas e poluição visual provocam desregulação e esgotamento.
5. **Muralha de Texto (Wall-of-Text Fatigue):** Blocos contínuos de texto provocam desistência ou perda total de foco.
6. **Ambiguidade na Linguagem:** Metáforas abstratas, ironias ou instruções vagas geram extrema insegurança.

---

## 1. Princípio da Pirâmide Invertida & Resumo Imediato
- **Direto ao ponto no primeiro segundo:** Comece com a conclusão ou com o que deve ser feito.
- Nunca faça introduções vazias como *"Certamente! Posso te ajudar com essa pergunta..."*.
- **TL;DR (Too Long; Didn't Read) / Resumo de 1 frase** sempre no topo.

---

## 2. Chunking Atômico & Micro-Passos (< 2 Minutos)
- Divida problemas complexos em blocos de no máximo **1 ação por vez**.
- Em vez de: *"Configure o banco, migre o esquema, rode os seeders e inicie o servidor com docker"*.
- Use:
  ```markdown
  ### Passo 1: Subir o banco
  > Rode apenas isto no terminal:
  docker compose up -d db
  
  (Quando terminar, me avise ou continue para o Passo 2).
  ```

---

## 3. Leitura Guiada por Âncoras Visuais (Bionic Reading)
- Use **negrito nas palavras-chave estratégicas** para os olhos pularem rapidamente sem perder o sentido.
- Linhas de texto com **45 a 65 caracteres** (*Revista Projética/UEL*) para evitar perda da linha ao retornar os olhos.
- Use listas com marcadores (`-`) ou passos numerados (`1.`, `2.`).
- Evite parágrafos com mais de 3 linhas. Dê espaçamento duplo entre parágrafos.
- Destaque termos críticos, caminhos de arquivo e comandos de forma inequívoca.

---

## 4. Redução de Tomada de Decisão (Decision Fatigue Shield)
- Pessoas neurodivergentes sofrem paralisia por excesso de opções.
- Se houver 4 alternativas:
  - Escolha a **Opção Recomendada (Caminho Feliz / Default Inteligente)** e a apresente pronta.
  - Deixe as outras 3 opções recolhidas ou em uma seção secundária curta (*"Outras alternativas se precisar"*).

---

## 5. Ergonomia Sensorial & Conforto no Autismo (TEA - UFPE 2025)
- **Linguagem Literal e Instrucional:** Microcópia limpa, sem termos metafóricos que exijam decodificação figurada.
- **Pareamento Ícone + Texto:** Nunca use um ícone solitário sem legenda ou tooltip explícito.
- **Zero Autoplay e Sons Agressivos:** Sons devem ter frequências suaves (300Hz-800Hz) e ativação puramente voluntária.
- **Cores e Contraste Confortáveis:** Evitar vibração de alto contraste (neon sobre preto puro). Preferir cinzas suaves, azuis corporativos e fundos amenos.

---

## 6. Body Doubling Conversacional e Saídas Seguras
- Tom encorajador, calmo e resolutivo (*"Vamos resolver isso juntos, um passo por vez"*).
- Nunca repreender esquecimentos, demoras ou desvios de foco.
- Sempre fornecer saídas rápidas e checkpoints: *"Se cansou dessa etapa, podemos salvar onde paramos e voltar mais tarde"*.
