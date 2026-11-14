# Anti-Slop, Expulso de Clichês e Humanização Textual

Modelos de Inteligência Artificial tendem a convergir para clichês estatísticos medianos — o chamado **AI Slop**. Textos sintéticos sem intervenção humana soam excessivamente pomposos, repetem metáforas gastas sobre sombras e turbilhões, e explicam as emoções em vez de fazê-las serem sentidas.

O **Escritor Pro** emprega uma barreira de contenção rigorosa para erradicar esses vícios, aliando-se aos princípios da skill `humanizer-plus`.

---

## 1. A Lista Negra dos Clichês Sintéticos de IA

Toda ocorrência das expressões abaixo deve ser detectada e sumariamente reescrita com imagens sensoriais específicas:

| Vício / Slop de IA | O que a IA tenta expressar | Como Reinscrever com Prosa Autêntica (*Show, Don't Tell*) |
| :--- | :--- | :--- |
| *"Um turbilhão de emoções"* | Confusão emocional interna | Descreva a taquicardia, a garganta seca, a incapacidade de manter os olhos parados em um ponto. |
| *"Uma dança perigosa de sombras"* | Luta ou escuridão tensa | O reflexo de lâminas em unhas sujas, o rangido de solas no cascalho, o cheiro de suor frio. |
| *"Um testamento da resiliência humana"* | Superação moral | Cicatrizes mal costuradas com linha de pesca, mãos calejadas colhendo o que sobrou do fogo. |
| *"Pouco sabia ele que o destino..."* | Foreshadowing forçado | Elimine o comentário do narrador. Mostre o detalhe factual que a personagem ignorou na cena. |
| *"Um farol de esperança"* | Inspiração moral | O som de um sino quebrando o silêncio do cerco; a fumaça de uma chaminé amiga ao longe. |
| *"Olhos faiscando de determinação"* | Fúria ou coragem | Mandíbulas travadas até estalar os dentes; a mão apertando o cabo da adaga até os nós dos dedos empalidecerem. |
| *"O tempo parecia ter congelado"* | Choque temporal | O ruído de uma gota de sangue caindo na pedra antes que o corpo tombasse. |
| *"O ar estava espesso com uma tensão palpável"* | Ambiente tenso | O silêncio subitamente pesado onde ninguém ousa tossir ou bater os talheres no prato. |
| *"Era um lembrete sombrio de que..."* | Lição moralizante | Deixe a imagem falar sozinha. Mostre a forca vazia balançando ao vento na entrada da vila. |
| *"Em suma..." / "Em última análise..."* | Conclusão acadêmica em ficção | Jamais use em prosa ficcional. Conclua com a ação final da cena. |

---

## 2. Princípios de Prosa Visceral

1. **A Especificidade Concreta**:
   - ❌ *Ele comeu uma fruta deliciosa.*
   - ✅ *Ele mordeu a polpa fibrosa do araçá, sentindo o sumo azedo travar-lhe a língua.*
2. **Substantivos Fortes e Verbos Ativos**:
   - Evite empilhar adjetivos fracos. Prefira um verbo que carregue a ação inteira:
   - ❌ *Ele caminhou de forma muito cansada e pesada pela lama fria.*
   - ✅ *Ele arrastou as botas no barro, os joelhos fraquejando a cada passo.*
3. **Erradicação da Redundância Psíquica**:
   - Evite o uso constante de verbos de percepção como *"ele viu"*, *"ela sentiu"*, *"ele ouviu"*:
   - ❌ *Ela ouviu os sinos tocarem e sentiu o chão tremer.*
   - ✅ *Os sinos dobraram no alto da torre. O chão estremeceu sob as lajes.*

---

## 3. Protocolo de Integração com `humanizer-plus`

Quando o texto passar pela etapa final de polimento:
1. **Varredura de Caracteres Invisíveis**: Purga de espaços de largura zero (*zero-width spaces*), pontuações homóglifas e marcadores de rastreamento de LLM.
2. **Descompactação de Parágrafos**: Quebra de blocos monotônicos de 4 linhas idênticas; intercalação de períodos de 3 palavras com períodos complexos de 20 palavras.
3. **Naturalização de Diálogos**: Inserção de quebras de pensamento, frases incompletas e reações orgânicas onde a etiqueta formal de máquina soa robótica.
