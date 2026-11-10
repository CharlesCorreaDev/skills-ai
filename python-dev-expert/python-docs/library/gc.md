"gc" --- Interface para o coletor de lixo
*****************************************

======================================================================

Este módulo fornece uma interface para o coletor de lixo opcional. Ele
permite desabilitar o coletor, ajustar a frequência de coleta e
configurar as opções de depuração. Ele também fornece acesso a objetos
inacessíveis que o coletor encontra, mas não pode "limpar". Como o
coletor complementa a contagem de referência já usada em Python, você
pode desabilitá-lo se tem certeza de que seu programa não cria ciclos
de referência. A coleta automática pode ser desativada pela chamada
"gc.disable()". Para depurar um programa vazando, chame
"gc.set_debug(gc.DEBUG_LEAK)". Perceba que isto inclui
"gc.DEBUG_SAVEALL", fazendo com que os objetos coletados pelo coletor
de lixo sejam salvos para inspeção em gc.garbage.

The "gc" module provides the following functions:

gc.enable()

   Habilita a coleta de lixo automática.

gc.disable()

   Desabilita a coleta de lixo automática.

gc.isenabled()

   Retorna "True" se a coleta automática estiver habilitada.

gc.collect(generation=2)

   Sem argumentos, execute uma coleta completa. O argumento opcional
   *generation* pode ser um inteiro especificando qual geração coletar
   (de 0 a 2). Uma exceção "ValueError" é levantada se o número de
   geração for inválido. A soma dos objetos coletados e dos objetos
   incoletáveis é retornada.

   As listas livres mantidas para vários tipos embutidos são limpas
   sempre que uma coleta completa ou a da geração mais alta (2) é
   executada. Nem todos os itens em algumas listas livres podem ser
   liberados devido à implementação particular, em particular "float".

   O efeito de chamar "gc.collect()" enquanto o interpretador já está
   realizando uma coleta é indefinido.

   Alterado na versão 3.14: "generation=1" executa um incremento de
   coleta.

   Alterado na versão 3.14.5: "generation=1" performs collection of
   the middle generation.

gc.set_debug(flags)

   Define os sinalizadores de depuração da coleta de lixo. As
   informações de depuração serão gravadas em "sys.stderr". Veja
   abaixo uma lista de sinalizadores de depuração que podem ser
   combinados usando operações de bit para controlar a depuração.

gc.get_debug()

   Retorna os sinalizadores de depuração atualmente definidos.

gc.get_objects(generation=None)

   Retorna uma lista de todos os objetos rastreados pelo coletor,
   excluindo a lista retornada. Se *generation* não for "None",
   retorna apenas os objetos rastreados pelo coletor que estão nessa
   geração.

   Aviso:

     Care must be taken when using objects returned by "get_objects()"
     because some of them could still be under construction and hence
     in a temporarily invalid state. Avoid using "get_objects()" for
     any purpose other than debugging.

   Alterado na versão 3.8: Novo parâmetro *generation*.

   Alterado na versão 3.14: A geração 1 foi removida

   Alterado na versão 3.14.5: Generation 1 is reintroduced to maintain
   GC behavior from 3.13.

   Levanta um evento de auditoria "gc.get_objects" com o argumento
   "generation".

gc.get_stats()

   Retorna uma lista de três dicionários por geração contendo
   estatísticas de coleta desde o início do interpretador. O número de
   chaves pode mudar no futuro, mas atualmente cada dicionário conterá
   os seguintes itens:

   * "collections" é o número de vezes que esta geração foi coletada;

   * "collected" é o número total de objetos coletados nesta geração;

   * "uncollectable" is the total number of objects which were found
     to be uncollectable (and were therefore moved to the "garbage"
     list) inside this generation;

   * "candidates" is the total number of objects in this generation
     which were considered for collection and traversed;

   * "duration" is the total time in seconds spent in collections for
     this generation.

   Adicionado na versão 3.4.

   Alterado na versão 3.15: Add "duration" and "candidates".

gc.set_threshold(threshold0[, threshold1[, threshold2]])

   Define os limites de coleta de lixo (a frequência de coleta).
   Definir *threshold0* como zero desativa a coleta.

   O GC classifica os objetos em três gerações, dependendo de quantas
   varreduras de coleta eles sobreviveram. Novos objetos são colocados
   na geração mais nova (geração "0"). Se um objeto sobreviver a uma
   coleção, ele será movido para a próxima geração mais antiga. Como a
   geração "2" é a geração mais antiga, os objetos dessa geração
   permanecem lá após uma coleta. Para decidir quando executar, o
   coletor acompanha o número de alocações e desalocações de objetos
   desde a última coleta. Quando o número de alocações menos o número
   de desalocações exceder *threshold0*, a coleta será iniciada.
   Inicialmente, apenas a geração "0" é examinada. Se a geração "0"
   foi examinada mais de *threshold1* vezes desde que a geração "1"
   foi examinada, então a geração "1" também é examinada. Com a
   terceira geração, as coisas são um pouco mais complicadas, veja
   Coletando a geração mais antiga para mais informações.

   See Garbage collector design for more information.

   Alterado na versão 3.14: *threshold2* é ignorado

   Alterado na versão 3.14.5: *threshold2* is restored to match Python
   3.13 behavior.

gc.get_count()

   Retorna as contagens da coleta atual como uma tupla de "(count0,
   count1, count2)".

gc.get_threshold()

   Retorna os limites da coleta atual como uma tupla de "(threshold0,
   threshold1, threshold2)".

gc.get_referrers(*objs)

   Retorna a lista de objetos que se referem diretamente a qualquer um
   dos objs. Esta função localizará apenas os contêineres que suportam
   coleta de lixo; tipos de extensão que se referem a outros objetos,
   mas não suportam coleta de lixo, não serão encontrados.

   Observe que os objetos que já foram desreferenciados, mas que vivem
   em ciclos e ainda não foram coletados pelo coletor de lixo podem
   ser listados entre os referenciadores resultantes. Para obter
   apenas os objetos atualmente ativos, chame "collect()" antes de
   chamar "get_referrers()".

   Aviso:

     Deve-se tomar cuidado ao usar objetos retornados por
     "get_referrers()" porque alguns deles ainda podem estar em
     construção e, portanto, em um estado temporariamente inválido.
     Evite usar "get_referrers()" para qualquer finalidade que não
     seja depuração.

   Levanta um evento de auditoria "gc.get_referrers" com o argumento
   "objs".

gc.get_referents(*objs)

   Retorna uma lista de objetos diretamente referenciados por qualquer
   um dos argumentos. Os referentes retornados são aqueles objetos
   visitados pelos métodos a nível do C "tp_traverse" dos argumentos
   (se houver), e podem não ser todos os objetos diretamente
   alcançáveis. Os métodos "tp_traverse" são suportados apenas por
   objetos que suportam coleta de lixo e são necessários apenas para
   visitar objetos que possam estar envolvidos em um ciclo. Assim, por
   exemplo, se um número inteiro pode ser acessado diretamente de um
   argumento, esse objeto inteiro pode ou não aparecer na lista de
   resultados.

   Levanta um evento de auditoria "gc.get_referents" com o argumento
   "objs".

gc.is_tracked(obj)

   Retorna "True" se o objeto está atualmente rastreado pelo coletor
   de lixo, "False" caso contrário. Como regra geral, as instâncias de
   tipos atômicos não são rastreadas e as instâncias de tipos não
   atômicos (contêineres, objetos definidos pelo usuário...) são. No
   entanto, algumas otimizações específicas do tipo podem estar
   presentes para suprimir a pegada do coletor de lixo de instâncias
   simples (por exemplo, dicts contendo apenas chaves e valores
   atômicos):

      >>> gc.is_tracked(0)
      False
      >>> gc.is_tracked("a")
      False
      >>> gc.is_tracked([])
      True
      >>> gc.is_tracked({})
      False
      >>> gc.is_tracked({"a": 1})
      True

   Adicionado na versão 3.1.

gc.is_finalized(obj)

   Retorna "True" se o objeto fornecido foi finalizado pelo coletor de
   lixo, "False" caso contrário.

      >>> x = None
      >>> class Lazarus:
      ...     def __del__(self):
      ...         global x
      ...         x = self
      ...
      >>> lazarus = Lazarus()
      >>> gc.is_finalized(lazarus)
      False
      >>> del lazarus
      >>> gc.is_finalized(x)
      True

   Adicionado na versão 3.9.

gc.freeze()

   Congela todos os objetos rastreados pelo coletor de lixo; move-os
   para uma geração permanente e ignora-os em todas as coleções
   futuras.

   Se um processo for "fork()" sem "exec()", evitar cópia em gravação
   (copy-on-write) desnecessário em processos filho maximizará o
   compartilhamento de memória e reduzirá o uso geral de memória. Isso
   requer evitar a criação de "buracos" liberados nas páginas de
   memória no processo pai e garantir que as coleções GC nos processos
   filho não toquem no contador "gc_refs" de objetos de vida longa
   originados no processo pai. Para realizar ambos, chame
   "gc.disable()" no início do processo pai, "gc.freeze()" logo antes
   de "fork()" e "gc.enable()" no início em processos filhos.

   Adicionado na versão 3.7.

gc.unfreeze()

   Descongela os objetos na geração permanente, coloca-os de volta na
   geração mais antiga.

   Adicionado na versão 3.7.

gc.get_freeze_count()

   Retorna o número de objetos na geração permanente.

   Adicionado na versão 3.7.

As seguintes variáveis são fornecidas para acesso somente leitura
(você pode alterar os valores, mas não deve revinculá-los):

gc.garbage

   Uma lista de objetos que o coletor considerou inacessíveis, mas não
   puderam ser liberados (objetos não coletáveis). A partir do Python
   3.4, esta lista deve estar vazia na maioria das vezes, exceto ao
   usar instâncias de tipos de extensão C com um slot "tp_del"
   não-"NULL".

   Se "DEBUG_SAVEALL" for definido, todos os objetos inacessíveis
   serão adicionados a esta lista ao invés de liberados.

   Alterado na versão 3.2: Se esta lista não estiver vazia no
   *desligamento do interpretador*, um "ResourceWarning" é emitido,
   que é silencioso por padrão. Se "DEBUG_UNCOLLECTABLE" for definido,
   além disso, todos os objetos não coletáveis serão impressos.

   Alterado na versão 3.4: Seguindo a **PEP 442**, objetos com um
   método "__del__()" não vão mais para "gc.garbage".

gc.callbacks

   Uma lista de retornos de chamada que serão invocados pelo coletor
   de lixo antes e depois da coleta. As funções de retorno serão
   chamadas com dois argumentos, *phase* e *info*.

   *phase* pode ser um dos dois valores:

      "start": A coleta de lixo está prestes a começar.

      "stop": A coleta de lixo terminou.

   *info* é um ditado que fornece mais informações para a função de
   retorno. As seguintes chaves estão atualmente definidas:

      "generation": A geração mais antiga sendo coletada.

      "collected": Quando *phase* é "stop", o número de objetos
      coletados com sucesso.

      "uncollectable": Quando *phase* é "stop", o número de objetos
      que não puderam ser coletados e foram colocados em "garbage".

      "candidates": When *phase* is "stop", the total number of
      objects in this generation which were considered for collection
      and traversed.

      "duration": When *phase* is "stop", the time in seconds spent in
      the collection.

   As aplicações podem adicionar suas próprias funções de retorno a
   essa lista. Os principais casos de uso são:

      Reunir estatísticas sobre coleta de lixo, como com que
      frequência várias gerações são coletadas e quanto tempo leva a
      coleta.

      Permitindo que os aplicativos identifiquem e limpem seus
      próprios tipos não colecionáveis quando eles aparecem em
      "garbage".

   Adicionado na versão 3.3.

   Alterado na versão 3.15: Add "duration" and "candidates".

As seguintes constantes são fornecidas para uso com "set_debug()":

gc.DEBUG_STATS

   Imprimir estatísticas durante a coleta. Esta informação pode ser
   útil ao sintonizar a frequência de coleta.

gc.DEBUG_COLLECTABLE

   Imprimir informações sobre objetos colecionáveis encontrados.

gc.DEBUG_UNCOLLECTABLE

   Imprime informações de objetos não colecionáveis encontrados
   (objetos que não são alcançáveis, mas não podem ser liberados pelo
   coletor). Esses objetos serão adicionados à lista "garbage".

   Alterado na versão 3.2: Imprime também o conteúdo da lista
   "garbage" em *desligamento do interpretador*, se não estiver vazia.

gc.DEBUG_SAVEALL

   Quando definido, todos os objetos inacessíveis encontrados serão
   anexados ao *lixo* em vez de serem liberados. Isso pode ser útil
   para depurar um programa com vazamento.

gc.DEBUG_LEAK

   Os sinalizadores de depuração necessários para o coletor imprimir
   informações sobre um programa com vazamento (igual a
   "DEBUG_COLLECTABLE | DEBUG_UNCOLLECTABLE | DEBUG_SAVEALL").
