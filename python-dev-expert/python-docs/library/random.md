"random" --- Gera números pseudoaleatórios
******************************************

**Código-fonte:** Lib/random.py

======================================================================

Este módulo implementa geradores de números pseudoaleatórios para
várias distribuições.

Para números inteiros, há uma seleção uniforme de um intervalo. Para
sequências, há uma seleção uniforme de um elemento aleatório, uma
função para gerar uma permutação aleatória de uma lista localmente e
uma função para amostragem aleatória sem substituição.

Na linha real, existem funções para calcular distribuições uniforme,
normal (gaussiana), log-normal, exponencial negativa, gama e beta.
Para gerar distribuições de ângulos, a distribuição de von Mises está
disponível.

Quase todas as funções do módulo dependem da função básica "random()",
que gera um ponto flutuante aleatório uniformemente no intervalo
semiaberto "0.0 <= X < 1.0". Python usa o Mersenne Twister como
gerador de núcleo. Produz pontos flutuantes de precisão de 53 bits e
possui um período de 2**19937-1. A implementação subjacente em C é
rápida e segura para threads. O Mersenne Twister é um dos geradores de
números aleatórios mais amplamente testados existentes. No entanto,
sendo completamente determinístico, não é adequado para todos os fins
e é totalmente inadequado para fins criptográficos.

As funções fornecidas por este módulo são, na verdade, métodos
vinculados de uma instância oculta da classe "random.Random". Você
pode instanciar suas próprias instâncias de "Random" para obter
geradores que não compartilham estado.

A classe "Random" também pode ser subclassificada se você quiser usar
um gerador básico diferente de sua própria criação: veja a
documentação dessa classe para mais detalhes.

O módulo "random" também fornece a classe "SystemRandom" que usa a
função do sistema "os.urandom()" para gerar números aleatórios a
partir de fontes fornecidas pelo sistema operacional.

Aviso:

  Os geradores pseudoaleatórios deste módulo não devem ser usados para
  fins de segurança. Para segurança ou uso criptográfico, veja o
  módulo "secrets".

Ver também:

  M. Matsumoto and T. Nishimura, "Mersenne Twister: A
  623-dimensionally equidistributed uniform pseudorandom number
  generator", ACM Transactions on Modeling and Computer Simulation
  Vol. 8, No. 1, January pp.3--30 1998.

  Receita de Complementary-Multiply-with-Carry para um gerador de
  números aleatórios alternativo compatível com um longo período e
  operações de atualização comparativamente simples.

Nota:

  O gerador global de números aleatórios e as instâncias de "Random"
  são seguros para thread. No entanto, na construção com threads
  livres, chamadas simultâneas ao gerador global ou à mesma instância
  de "Random" podem encontrar contenção e baixo desempenho. Considere
  usar instâncias separadas de "Random" por thread.


Funções de contabilidade
========================

random.seed(a=None, version=2)

   Inicializa o gerador de números aleatórios.

   Se *a* for omitido ou "None", a hora atual do sistema será usada.
   Se fontes de aleatoriedade são fornecidas pelo sistema operacional,
   elas são usadas no lugar da hora do sistema (consulte a função
   "os.urandom()" para detalhes sobre disponibilidade).

   Se *a* é um int, seu valor absoluto é usado diretamente.

   Com a versão 2 (o padrão), o objeto a "str", "bytes" ou "bytearray"
   é convertido em um objeto "int" e todos os seus bits são usados.

   Com a versão 1 (fornecida para reproduzir sequências aleatórias de
   versões mais antigas do Python), o algoritmo para "str" e "bytes"
   gera um intervalo mais restrito de sementes.

   Alterado na versão 3.2: Movido para o esquema da versão 2, que usa
   todos os bits em uma semente de strings.

   Alterado na versão 3.11: *seed* deve ser um dos seguintes tipos:
   "None", "int", "float", "str", "bytes" ou "bytearray".

random.getstate()

   Retorna um objeto capturando o estado interno atual do gerador.
   Este objeto pode ser passado para "setstate()" para restaurar o
   estado.

random.setstate(state)

   *state* deveria ter sido obtido de uma chamada anterior para
   "getstate()", e "setstate()" restaura o estado interno do gerador
   para o que era no momento que "getstate()" foi chamado.


Funções para bytes
==================

random.randbytes(n)

   Gera *n* bytes aleatórios.

   Este método não deve ser usado para gerar tokens de segurança. Use
   "secrets.token_bytes()".

   Adicionado na versão 3.9.


Funções para inteiros
=====================

random.randrange(stop)
random.randrange(start, stop[, step])

   Retorna um elemento selecionado aleatoriamente de "range(start,
   stop, step)".

   Isso é aproximadamente equivalente a "choice(range(start, stop,
   step))" mas provê suporte a intervalos arbitrariamente grandes e é
   otimizado para casos comuns.

   O padrão de argumento posicional corresponde à função "range()".

   Argumentos nomeados não devem ser usados porque podem ser
   interpretados de maneiras inesperadas. Por exemplo
   "randrange(start=100)" é interpretado como "randrange(0, 100, 1)".

   Alterado na versão 3.2: "randrange()" é mais sofisticado em
   produzir valores igualmente distribuídos. Anteriormente, usava um
   estilo como "int(random()*n)", que poderia produzir distribuições
   ligeiramente desiguais.

   Alterado na versão 3.12: A conversão automática de tipos não
   inteiros não é mais suportada. Chamadas como "randrange(10.0)" e
   "randrange(Fraction(10, 1))" agora levantam uma "TypeError".

random.randint(a, b)

   Retorna um inteiro aleatório *N* de forma que "a <= N <= b".
   Apelido para "randrange(a, b+1)".

random.getrandbits(k)

   Retorna um número inteiro Python não-negativo com bits aleatórios
   *k*. Este método é fornecido com o gerador Mersenne Twister e
   alguns outros geradores também podem fornecê-lo como uma parte
   opcional da API. Quando disponível, "getrandbits()" permite que
   "randrange()" manipule intervalos arbitrariamente grandes.

   Alterado na versão 3.9: Este método agora aceita zero em *k*.


Funções para sequências
=======================

random.choice(seq)

   Retorna um elemento aleatório da sequência não vazia *seq*. Se
   *seq* estiver vazio, levanta "IndexError".

random.choices(population, weights=None, *, cum_weights=None, k=1)

   Retorna uma lista do tamanho de *k* de elementos escolhidos da
   *population* com substituição. Se a *population* estiver vazio,
   levanta "IndexError".

   Se uma sequência *weights* for especificada, as seleções serão
   feitas de acordo com os pesos relativos. Alternativamente, se uma
   sequência *cum_weights* for fornecida, as seleções serão feitas de
   acordo com os pesos cumulativos (talvez calculados usando
   "itertools.accumulate()"). Por exemplo, os pesos relativos "[10, 5,
   30, 5]" são equivalentes aos pesos cumulativos "[10, 15, 45, 50]".
   Internamente, os pesos relativos são convertidos em pesos
   acumulados antes de fazer seleções, portanto, fornecer pesos
   cumulativos economiza trabalho.

   Se nem *weights* nem *cum_weights* forem especificados, as seleções
   serão feitas com igual probabilidade. Se uma sequência de pesos for
   fornecida, ela deverá ter o mesmo comprimento que a sequência
   *population*. É um "TypeError" para especificar ambos os *weights*
   e *cum_weights*.

   The *weights* or *cum_weights* can use any numeric type that
   interoperates with the "float" values returned by "random()" (that
   includes integers, floats, and fractions but excludes decimals).
   Weights are assumed to be non-negative and finite.  A "ValueError"
   is raised if all weights are zero.

   Para uma dada semente, a função "choices()" com igual peso
   normalmente produz uma sequência diferente das chamadas repetidas
   para "choice()". O algoritmo usado por "choices()" usa aritmética
   de ponto flutuante para consistência e velocidade internas. O
   algoritmo usado por "choice()" assume como padrão aritmética
   inteira com seleções repetidas para evitar pequenos vieses de erro
   de arredondamento.

   Adicionado na versão 3.6.

   Alterado na versão 3.9: Levanta uma "ValueError" se todos os pesos
   forem zero.

random.shuffle(x)

   Embaralha a sequência *x* internamente.

   Para embaralhar uma sequência imutável e retornar uma nova lista
   embaralhada, use "sample(x, k=len(x))".

   Observe que, mesmo para pequenos "len(x)", o número total de
   permutações de *x* pode crescer rapidamente maior que o período da
   maioria dos geradores de números aleatórios. Isso implica que a
   maioria das permutações de uma longa sequência nunca pode ser
   gerada. Por exemplo, uma sequência de comprimento 2080 é a maior
   que pode caber no período do gerador de números aleatórios Mersenne
   Twister.

   Alterado na versão 3.11: Removido o parâmetro opcional *random*.

random.sample(population, k, *, counts=None)

   Retorna uma lista de comprimento *k* de elementos únicos escolhidos
   na sequência populacional. Usado para amostragem aleatória sem
   reposição.

   Retorna uma nova lista contendo elementos da população, mantendo a
   população original inalterada. A lista resultante está na ordem de
   seleção, para que todas as subfatias também sejam amostras
   aleatórias válidas. Isso permite que os vencedores do sorteio (a
   amostra) sejam divididos em grandes prêmios e vencedores de segundo
   lugar (as subfatias).

   Os membros da população não precisam ser *hasheáveis* ou únicos. Se
   a população contiver repetições, cada ocorrência é uma seleção
   possível na amostra.

   Elementos repetidos podem ser especificados um de cada vez ou com o
   parâmetro somente-nomeado opcional *count*. Por exemplo,
   "sample(['red', 'blue'], counts=[4, 2], k=5)" é equivalente a
   "sample(['red', 'red', 'red', 'red', 'blue', 'blue'], k=5)".

   Para escolher uma amostra de um intervalo de números inteiros, use
   um objeto "range()" como argumento. Isso é especialmente rápido e
   com eficiência de espaço para amostragem de uma grande população:
   "sample(range(10000000), k=60)".

   Se o tamanho da amostra for maior que o tamanho da população, uma
   "ValueError" é levantada.

   Alterado na versão 3.9: Adicionado o parâmetro *counts*.

   Alterado na versão 3.11: *population* deve ser uma sequência. A
   conversão automática de conjuntos em listas não é mais suportada.


Distribuições discretas
=======================

A função a seguir gera uma distribuição discreta.

random.binomialvariate(n=1, p=0.5)

   Distribuição binomial. Retorna o número de sucessos para *n*
   tentativas independentes com a probabilidade de sucesso em cada
   tentativa sendo *p*:

   Matematicamente equivalente a:

      sum(random() < p for i in range(n))

   O número de tentativas *n* deve ser um número inteiro não negativo.
   A probabilidade de sucesso *p* deve estar entre "0.0 <= p <= 1.0".
   O resultado é um número inteiro no intervalo "0 <= X <= n".

   Adicionado na versão 3.12.


Distribuições com valor real
============================

As funções a seguir geram distribuições específicas com valor real. Os
parâmetros de função são nomeados após as variáveis correspondentes na
equação da distribuição, conforme usadas na prática matemática comum;
a maioria dessas equações pode ser encontrada em qualquer texto
estatístico.

random.random()

   Retorna o próximo número aleatório de ponto flutuante no intervalo
   "0.0 <= X < 1.0".

random.uniform(a, b)

   Retorna um número de ponto flutuante aleatório *N* de forma que "a
   <= N <= b" para "a <= b" e "b <= N <= a" para "b < a".

   O valor final "b" pode ou não ser incluído no intervalo dependendo
   do arredondamento de ponto flutuante na expressão "a + (b-a) *
   random()".

random.triangular(low, high, mode)

   Retorna um número de ponto flutuante aleatório *N* de forma que
   "low <= N <= high" e com o *mode* especificado entre esses limites.
   Os limites *low* e *high* são padronizados como zero e um. O
   argumento *mode* assume como padrão o ponto médio entre os limites,
   fornecendo uma distribuição simétrica.

random.betavariate(alpha, beta)

   Distribuição beta. As condições nos parâmetros são "alpha > 0" e
   "beta > 0". Os valores retornados variam entre 0 e 1.

random.expovariate(lambd=1.0)

   Distribuição exponencial. *lambd* é 1.0 dividido pela média
   desejada. Deve ser diferente de zero. (O parâmetro seria chamado
   "lambda", mas é uma palavra reservada em Python.) Os valores
   retornados variam de 0 a infinito positivo se *lambd* for positivo
   e de infinito negativo a 0 se *lambd* for negativo.

   Alterado na versão 3.12: Adicionado o valor padrão para "lambd".

random.gammavariate(alpha, beta)

   Distribuição gama. (*Não* a função gama!) Os parâmetros de forma e
   escala, *alfa* e *beta*, devem ter valores positivos. (As
   convenções de chamada variam e algumas fontes definem 'beta' como o
   inverso da escala).

   A função de distribuição de probabilidade é:

                x ** (alpha - 1) * math.exp(-x / beta)
      pdf(x) =  --------------------------------------
                  math.gamma(alpha) * beta ** alpha

random.gauss(mu=0.0, sigma=1.0)

   Distribuição normal, também chamada de distribuição gaussiana. *mu*
   é a média e *sigma* é o desvio padrão. Isto é um pouco mais rápido
   que a função "normalvariate()" definida abaixo.

   Nota sobre multithreading: quando duas threads chamam esta função
   simultaneamente, é possível que recebam o mesmo valor de retorno.
   Isso pode ser evitado de três maneiras. 1) Fazer com que cada
   thread use uma instância diferente do gerador de números
   aleatórios. 2) Colocar travas em todas as chamadas. 3) Usar a
   função mais lenta, mas segura para thread "normalvariate()".

   Alterado na versão 3.11: *mu* e *sigma* agora têm argumentos
   padrão.

random.lognormvariate(mu, sigma)

   Distribuição log normal. Se você usar o logaritmo natural dessa
   distribuição, obterá uma distribuição normal com média *mu* e
   desvio padrão *sigma*. *mu* pode ter qualquer valor e *sigma* deve
   ser maior que zero.

random.normalvariate(mu=0.0, sigma=1.0)

   Distribuição normal. *mu* é a média e *sigma* é o desvio padrão.

   Alterado na versão 3.11: *mu* e *sigma* agora têm argumentos
   padrão.

random.vonmisesvariate(mu, kappa)

   *mu* é o ângulo médio, expresso em radianos entre 0 e 2**pi*, e
   *kappa* é o parâmetro de concentração, que deve ser maior ou igual
   a zero. Se *kappa* for igual a zero, essa distribuição será
   reduzida para um ângulo aleatório uniforme no intervalo de 0 a
   2**pi*.

random.paretovariate(alpha)

   Distribuição de Pareto. *alpha* é o parâmetro de forma.

random.weibullvariate(alpha, beta)

   Distribuição Weibull. *alpha* é o parâmetro de escala e *beta* é o
   parâmetro de forma.


Gerador alternativo
===================

class random.Random([seed])

   Classe que implementa o gerador de números pseudoaleatórios padrão
   usado pelo módulo "random".

   Alterado na versão 3.11: Anteriormente, o *seed* poderia ser
   qualquer objeto hasheável. Agora está limitado a: "None", "int",
   "float", "str", "bytes" ou "bytearray".

   Subclasses de "Random" devem substituir os seguintes métodos se
   desejarem fazer uso de um gerador básico diferente:

   seed(a=None, version=2)

      Substitua este método nas subclasses para personalizar o
      comportamento de "seed()" das instâncias de "Random".

   getstate()

      Substitua este método nas subclasses para personalizar o
      comportamento de "getstate()" das instâncias de "Random".

   setstate(state)

      Substitua este método nas subclasses para personalizar o
      comportamento de "setstate()" das instâncias de "Random".

   random()

      Substitua este método nas subclasses para personalizar o
      comportamento de "random()" das instâncias de "Random".

   Opcionalmente, uma subclasse geradora personalizada também pode
   fornecer o seguinte método:

   getrandbits(k)

      Substitua este método nas subclasses para personalizar o
      comportamento de "getrandbits()" das instâncias de "Random".

   randbytes(n)

      Substitua este método nas subclasses para personalizar o
      comportamento de "randbytes()" das instâncias de "Random".

class random.SystemRandom([seed])

   Classe que usa a função "os.urandom()" para gerar números
   aleatórios a partir de fontes fornecidas pelo sistema operacional.
   Não disponível em todos os sistemas. Não depende do estado do
   software e as sequências não são reproduzíveis. Assim, o método
   "seed()" não tem efeito e é ignorado. Os métodos "getstate()" e
   "setstate()" levantam "NotImplementedError" se chamados.


Notas sobre reprodutibilidade
=============================

Às vezes, é útil poder reproduzir as sequências fornecidas por um
gerador de números pseudoaleatórios. Reutilizando um valor inicial, a
mesma sequência deve ser reproduzível de execução para execução, desde
que mais de uma thread não estejam em execução.

A maioria dos algoritmos e funções de propagação do módulo aleatório
está sujeita a alterações nas versões de Python, mas dois aspectos são
garantidos para não serem alterados:

* Se um novo método de semeadura for adicionado, será oferecida um
  semeador compatível com versões anteriores.

* O método "random()" do gerador continuará produzindo a mesma
  sequência quando o semeador compatível receber a mesma semente.


Exemplos
========

Exemplos básicos:

   >>> random()                          # Ponto flutuante aleatório:  0.0 <= x < 1.0
   0.37444887175646646

   >>> uniform(2.5, 10.0)                # Ponto flutuante aleatório:  2.5 <= x <= 10.0
   3.1800146073117523

   >>> expovariate(1 / 5)                # Intervalo entre chegadas com médias de 5 segundos
   5.148957571865031

   >>> randrange(10)                     # Inteiro de 0 até 9 inclusivo
   7

   >>> randrange(0, 101, 2)              # Inteiro par entre 0 até 100 inclusivo
   26

   >>> choice(['win', 'lose', 'draw'])   # Um único elemento aleatório de uma sequência
   'draw'

   >>> deck = 'ace two three four'.split()
   >>> shuffle(deck)                     # Embaralha uma lista
   >>> deck
   ['four', 'two', 'ace', 'three']

   >>> sample([10, 20, 30, 40, 50], k=4) # Quatro amostras sem substitutos
   [40, 10, 50, 30]

Simulações:

   >>> # Seis giros da roleta (amostragem ponderada com substituição)
   >>> choices(['red', 'black', 'green'], [18, 18, 2], k=6)
   ['red', 'green', 'black', 'black', 'red', 'black']

   >>> # Distribui 20 cartas sem reposição de um baralho de
   >>> # 52 cartas e determine a proporção de cartas com
   >>> # valor dez: dez, valete, rainha ou rei.
   >>> deal = sample(['tens', 'low cards'], counts=[16, 36], k=20)
   >>> deal.count('tens') / 20
   0.15

   >>> # Estima a probabilidade de obter 5 ou mais caras em 7 giros
   >>> # de uma moeda viciada que cai em cara 60% das vezes.
   >>> sum(binomialvariate(n=7, p=0.6) >= 5 for i in range(10_000)) / 10_000
   0.4169

   >>> # Probabilidade da mediana de 5 amostras estar nos dois quartis do meio
   >>> def trial():
   ...     return 2_500 <= sorted(choices(range(10_000), k=5))[2] < 7_500
   ...
   >>> sum(trial() for i in range(10_000)) / 10_000
   0.7958

Exemplo de bootstrapping estatístico usando reamostragem com
substituição para estimar um intervalo de confiança para a média de
uma amostra:

   # https://www.thoughtco.com/example-of-bootstrapping-3126155
   from statistics import fmean as mean
   from random import choices

   data = [41, 50, 29, 37, 81, 30, 73, 63, 20, 35, 68, 22, 60, 31, 95]
   means = sorted(mean(choices(data, k=len(data))) for i in range(100))
   print(f'The sample mean of {mean(data):.1f} has a 90% confidence '
         f'interval from {means[5]:.1f} to {means[94]:.1f}')

Exemplo de um teste de permutação de reamostragem para determinar a
significância estatística ou valor-p de uma diferença observada entre
os efeitos de uma droga em comparação com um placebo:

   # Exemplo de "Statistics is Easy" de Dennis Shasha e Manda Wilson
   from statistics import fmean as mean
   from random import shuffle

   drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
   placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
   observed_diff = mean(drug) - mean(placebo)

   n = 10_000
   count = 0
   combined = drug + placebo
   for i in range(n):
       shuffle(combined)
       new_diff = mean(combined[:len(drug)]) - mean(combined[len(drug):])
       count += (new_diff >= observed_diff)

   print(f'{n} label reshufflings produced only {count} instances with a difference')
   print(f'at least as extreme as the observed difference of {observed_diff:.1f}.')
   print(f'The one-sided p-value of {count / n:.4f} leads us to reject the null')
   print(f'hypothesis that there is no difference between the drug and the placebo.')

Simulação de tempos de chegada e entregas de serviços para uma fila
multisservidor:

   from heapq import heapify, heapreplace
   from random import expovariate, gauss
   from statistics import mean, quantiles

   average_arrival_interval = 5.6
   average_service_time = 15.0
   stdev_service_time = 3.5
   num_servers = 3

   waits = []
   arrival_time = 0.0
   servers = [0.0] * num_servers  # hora em que cada servidor fica disponível
   heapify(servers)
   for i in range(1_000_000):
       arrival_time += expovariate(1.0 / average_arrival_interval)
       next_server_available = servers[0]
       wait = max(0.0, next_server_available - arrival_time)
       waits.append(wait)
       service_duration = max(0.0, gauss(average_service_time, stdev_service_time))
       service_completed = arrival_time + wait + service_duration
       heapreplace(servers, service_completed)

   print(f'Mean wait: {mean(waits):.1f}   Max wait: {max(waits):.1f}')
   print('Quartiles:', [round(q, 1) for q in quantiles(waits)])

Ver também:

  Statistics for Hackers um tutorial em vídeo por Jake Vanderplas
  sobre análise estatística usando apenas alguns conceitos
  fundamentais, incluindo simulação, amostragem, embaralhamento e
  validação cruzada.

  Economics Simulation uma simulação de um mercado por Peter Norvig
  que mostra o uso eficaz de muitas das ferramentas e distribuições
  fornecidas por este módulo (gauss, uniform, sample, betavariate,
  choice, triangular e randrange).

  A Concrete Introduction to Probability (using Python) um tutorial de
  Peter Norvig cobrindo os fundamentos da teoria das probabilidades,
  como escrever simulações e como realizar análises de dados usando
  Python.


Receitas
========

Estas receitas mostram como fazer seleções aleatórias de forma
eficiente a partir dos iteradores combinatórios no módulo "itertools"
ou no projeto more-itertools:

   import random

   def random_product(*iterables, repeat=1):
       "Random selection from itertools.product(*iterables, repeat=repeat)"
       pools = tuple(map(tuple, iterables)) * repeat
       return tuple(map(random.choice, pools))

   def random_permutation(iterable, r=None):
       "Random selection from itertools.permutations(iterable, r)"
       pool = tuple(iterable)
       r = len(pool) if r is None else r
       return tuple(random.sample(pool, r))

   def random_combination(iterable, r):
       "Random selection from itertools.combinations(iterable, r)"
       pool = tuple(iterable)
       n = len(pool)
       indices = sorted(random.sample(range(n), r))
       return tuple(pool[i] for i in indices)

   def random_combination_with_replacement(iterable, r):
       "Choose r elements with replacement.  Order the result to match the iterable."
       # Result will be in set(itertools.combinations_with_replacement(iterable, r)).
       pool = tuple(iterable)
       n = len(pool)
       indices = sorted(random.choices(range(n), k=r))
       return tuple(pool[i] for i in indices)

   def random_derangement(iterable):
       "Choose a permutation where no element stays in its original position."
       seq = tuple(iterable)
       if len(seq) < 2:
           if not seq:
               return ()
           raise IndexError('No derangments to choose from')
       perm = list(range(len(seq)))
       start = tuple(perm)
       while True:
           random.shuffle(perm)
           if all(p != q for p, q in zip(start, perm)):
               return tuple([seq[i] for i in perm])

O padrão de "random()" é retornar múltiplos de 2⁻⁵³ no intervalo *0.0
≤ x < 1.0*. Todos esses números são espaçados uniformemente e são
representáveis exatamente como pontos flutuantes Python. No entanto,
muitos outros pontos flutuantes representados nesse intervalo não são
seleções possíveis. Por exemplo, "0.05954861408025609" não é um
múltiplo inteiro de 2⁻⁵³.

A receita a seguir tem uma abordagem diferente. Todos os pontos
flutuantes no intervalo são seleções possíveis. A mantissa vem de uma
distribuição uniforme de inteiros no intervalo *2⁵² ≤ mantissa < 2⁵³*.
O expoente vem de uma distribuição geométrica onde expoentes menores
que *-53* ocorrem com metade da frequência do próximo expoente maior.

   from random import Random
   from math import ldexp

   class FullRandom(Random):

       def random(self):
           mantissa = 0x10_0000_0000_0000 | self.getrandbits(52)
           exponent = -53
           x = 0
           while not x:
               x = self.getrandbits(32)
               exponent += x.bit_length() - 32
           return ldexp(mantissa, exponent)

Todas as distribuições reais valoradas na classe usarão o novo método:

   >>> fr = FullRandom()
   >>> fr.random()
   0.05954861408025609
   >>> fr.expovariate(0.25)
   8.87925541791544

A receita é conceitualmente equivalente a um algoritmo que escolhe
entre todos os múltiplos de 2⁻¹⁰⁷⁴ no intervalo *0.0 ≤ x < 1.0*. Todos
esses números são espaçados uniformemente, mas a maioria deve ser
arredondada para o ponto flutuante Python representável mais próximo.
(O valor 2⁻¹⁰⁷⁴ é o menor ponto flutuante positivo não normalizado e é
igual a "math.ulp(0.0)".)

Ver também:

  Generating Pseudo-random Floating-Point Values um artigo de Allen B.
  Downey descrevendo formas de gerar pontos flutuantes mais refinados
  do que normalmente gerados por "random()".


Uso na linha de comando
=======================

Adicionado na versão 3.13.

O módulo "random" pode ser invocado como um script na linha de
comando:

   python -m random [-h] [-c ESCOLHA [ESCOLHA ...] | -i N | -f N] [entrada ...]

As seguintes opções são aceitas:

-h, --help

   Mostra a mensagem de ajuda e sai.

-c CHOICE [CHOICE ...]
--choice CHOICE [CHOICE ...]

   Imprime uma escolha aleatória, usando "choice()".

-i <N>
--integer <N>

   Imprime um inteiro aleatório entre 1 e N inclusive, usando
   "randint()".

-f <N>
--float <N>

   Imprime um número de ponto flutuante aleatório entre 0 e N
   inclusive, usando "uniform()".

Se nenhuma opção for fornecida, a saída dependerá da entrada:

* String ou vários: mesmo que "--choice".

* Inteiro mesmo que "--integer".

* Ponto flutuante: mesmo que "--float".


Exemplos na linha de comando
============================

Aqui estão alguns exemplos da interface de linha de comando "random":

   $ # Escolhe um aleatório
   $ python -m random egg bacon sausage spam "Lobster Thermidor aux crevettes with a Mornay sauce"
   Lobster Thermidor aux crevettes with a Mornay sauce

   $ # Inteiro aleatório
   $ python -m random 6
   6

   $ # Número de ponto flutuante aleatório
   $ python -m random 1.8
   1.7080016272295635

   $ # Com argumentos explícitos
   $ python  -m random --choice egg bacon sausage spam "Lobster Thermidor aux crevettes with a Mornay sauce"
   egg

   $ python -m random --integer 6
   3

   $ python -m random --float 1.8
   1.5666339105010318

   $ python -m random --integer 6
   5

   $ python -m random --float 6
   3.1942323316565915
