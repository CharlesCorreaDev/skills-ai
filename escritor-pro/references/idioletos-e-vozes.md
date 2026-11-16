# Idioletos, Vozes e Matriz de Caracterização de Personagens
## Parte Integrante da Skill Escritor Pro

Um dos maiores problemas em romances, contos e campanhas de RPG escritos com assistência de IA é a **homogeneização de voz**: todos os personagens soam como o próprio narrador polido, usando períodos compostos simétricos, vocabulário idêntico e mesmo nível de formalidade.

O **Idioleto** é a impressão digital linguística de um indivíduo. Quando bem construído, o leitor consegue identificar quem está falando **mesmo se todos os travessões e tags dicendi forem apagados** (*O Teste do Diálogo Cego*).

---

## 1. Os 6 Pilares do Idioleto Canônico

Para cada personagem principal ou NPC relevante, defina sua matriz:

```
┌────────────────────────────────────────────────────────┐
│               MATRIZ DE IDIOLETO CANÔNICO              │
├────────────────────────────────────────────────────────┤
│ 1. Vocabulário Ativo & Jargão (Profissão, Origem, Idade) │
│ 2. Sintaxe & Extensão de Frase (Monossilábico vs Prolixo)│
│ 3. Pronomes de Tratamento & Formalidade (Tu, Você, Vós) │
│ 4. Muletas de Linguagem, Tiques & Bordões             │
│ 5. Padrão de Respiração & Ritmo (Frenético, Pausado)  │
│ 6. Subtexto Típico (O que esconde sob o que fala)      │
└────────────────────────────────────────────────────────┘
```

### 1. Vocabulário Ativo e Metáforas Prediletas
As metáforas de um indivíduo nascem de seu cotidiano e ofício:
* **Um ferreiro ou militar**: Pensa e fala em termos de têmpera, peso, lâmina, desgaste, flanco e impacto (*"Aquela conversa não tem fio nenhum"*, *"Ele amoleceu na forja"*).
* **Um marinheiro ou ribeirinho**: Fala em correntezas, marés, nós, calados e tempestades (*"Não adianta remar contra o refluxo"*, *"Água mansa afoga desavisado"*).
* **Um nobre ou acadêmico**: Termos latinizados, abstrações, precedentes jurídicos e linhagem (*"Tal conduta carece de prudência ancestral"*, *"Não há substância no pleito"*).
* **Um larápio dos becos**: Calão de rua, termos cortados, gírias locais e eufemismos para roubo e morte (*"Passar a navalha"*, *"Dormir no cascalho"*, *"Fritar a língua"*).

### 2. Sintaxe e Extensão de Frase
* **Períodos Curtos & Cortantes**: Personagens práticos, traumatizados, operários ou predadores. Poucas conjunções subordinativas. Uso frequente de imperativos e elipses.
  * *Exemplo*: `— Fogo no celeiro. Tirem os cavalos. Agora.`
* **Períodos Longos, Subordinados & Perifrásticos**: Personagens manipuladores, diplomatas, filósofos ou prolixos. Uso de concessivas (*ainda que, conquanto, nada obstante*).
  * *Exemplo*: `— Conquanto me pareça razoável vossa urgência, meu caro capitão, convém recordar que precipitações custam mais caros tributos do que a paciência nos conselhos régios.`

### 3. Nível de Formalidade e Pronomes de Tratamento (PT-BR)
A coesão dos pronomes no Brasil histórico e fantástico precisa de consistência rígida:
* **Tu / Vós**: Adequado para alta nobreza arcaica, clero devoto ou regionalismo estrito (sulista/nordestino arcaico). Conjugação precisa ser rigorosa (`tu disseste`, `vós sabeis`).
* **Você / O Senhor / A Senhora**: Padrão culto brasileiro contemporâneo ou cortesias pragmáticas.
* **Sem Pronome Explícito (Elipse)**: Ocultar o sujeito para acelerar a fala ou soar rude (`— Fez o combinado? — Não deu tempo.`).

### 4. Muletas de Linguagem, Tiques e Cacoetes
Pequenos vícios que marcam o personagem sem sobrecarregar o texto:
* **Interjeições recorrentes**: *"Pois é"*, *"Ora bolas"*, *"Vejam só"*, *"Pela carcaça dos deuses"*.
* **Perguntas retóricas de validação**: Terminar frases com *"Entende?"*, *"Não é?"*, *"Viu?"*, *"Confere?"*.
* **Pausas reflexivas marcadas**: Limpar a garganta antes de concordar, estalar a língua antes de negar.

---

## 2. O Teste do Diálogo Cego (*The Blind Dialogue Test*)

Antes de aprovar uma cena com 2 ou mais debatedores, aplique o teste:

### Exemplo Ruim (Vozes Idênticas / IA Slop):
> — Precisamos nos apressar ou os guardas nos encontrarão aqui — disse o ladrão.
> — De fato, nossa margem de segurança é praticamente nula — respondeu o nobre.
> — O risco é grande, mas a recompensa vale a pena — retrucou o mercenário.

*Diagnóstico*: Se remover os nomes, qualquer um poderia ter dito qualquer uma das três frases. Não há textura, corte ou diferença de classe social.

### Exemplo Excelente (Idioletos Vivos e Distintos):
> — Pé na tábua. Se a ronda dobrar aquela esquina, a gente vira adubo de calabouço.
> — Sugiro prudência, senhor Rato. Seus modos barulhentos atrairão a patrulha muito antes da vigília mudar.
> — Me paguem o ouro adiantado. Se tiver que cortar garganta imperial esta noite, a tarifa dobra.

*Diagnóstico*: Claramente distinguem-se o batedor de sarjeta, o nobre/estudioso pedante e o soldado mercenário interesseiro, **sem necessidade de nenhuma tag declarativa**.

---

## 3. Template de Ficha de Idioleto para a Bíblia Canônica

Adicione ao arquivo `mundo/personagens.md` de cada figura central:

```markdown
### [Nome do Personagem] — Matriz Vocal
- **Camada Social / Origem:** [Ex: Ex-gladiador que ascendeu a guarda-costas da elite]
- **Ritmo de Fala:** [Ex: Pausado, rouco, frases monossilábicas de no máximo 7 palavras]
- **Tratamento:** [Ex: Trata todos por "patrão" ou "chefe", nunca usa "senhor"]
- **Jargão / Metáforas:** [Ex: Usa metáforas de arena, carniçaria e apostas]
- **Expressão Típica (Bordão):** [Ex: "Sangue que seca na areia não volta pra veia."]
- **Tabu Linguístico:** [Ex: Nunca pede "por favor" nem usa diminutivos carinhosos]
```

