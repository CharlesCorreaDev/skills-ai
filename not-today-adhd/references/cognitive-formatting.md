# Formatação Cognitiva Amigável (Cognitive Accessibility)

Pessoas com TDAH e neurodivergência enfrentam desafios primários em:
1. **Memória de Trabalho Reduzida (Working Memory):** Dificuldade de reter múltiplos fatos temporários ao mesmo tempo.
2. **Cegueira Temporal (Time Blindness):** Dificuldade de estimar tempo ou priorizar o que vem primeiro sem ancoragem clara.
3. **Paralisia de Iniciação (Task Paralysis / Executive Dysfunction):** Uma tarefa grande parece uma montanha intransponível.
4. **Sobrecarga de Informação ("Muralha de Texto"):** Blocos contínuos de texto provocam desistência ou perda total de foco.

---

## 1. Princípio da Pirâmide Invertida
- **Direto ao ponto no primeiro segundo:** Comece com a conclusão ou com o que deve ser feito.
- Nunca faça introduções vazias como "Certamente! Posso te ajudar com essa pergunta...".
- **TL;DR (Too Long; Didn't Read) / Resumo de 1 frase** sempre no topo.

---

## 2. Chunking Atômico (Decomposição em Micro-passos)
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

## 3. Leitura Guiada por Âncoras Visuais (Bionic Reading Pattern)
- Use **negrito nas palavras-chave estratégicas** para os olhos pularem rapidamente sem perder o sentido.
- Use listas com marcadores (`-`) ou passos numerados (`1.`, `2.`).
- Evite parágrafos com mais de 3 linhas. Dê espaçamento duplo entre parágrafos.
- Destaque termos críticos, caminhos de arquivo e comandos de forma inequívoca.

---

## 4. Redução de Tomada de Decisão (Decision Fatigue Shield)
- Pessoas neurodivergentes sofrem paralisia por excesso de opções.
- Se houver 4 alternativas:
  - Escolha a **Opção Recomendada (Caminho Feliz / Default Inteligente)** e a apresente pronta.
  - Deixe as outras 3 opções recolhidas ou em uma seção secundária curta ("Outras alternativas se precisar").

---

## 5. Body Doubling Conversacional e Tom Não Julgador
- Tom encorajador, calmo e resolutivo.
- Nunca repreender esquecimentos ou pausas.
- Sempre fornecer saídas rápidas ("Se cansou dessa etapa, podemos salvar onde paramos e voltar amanhã").

