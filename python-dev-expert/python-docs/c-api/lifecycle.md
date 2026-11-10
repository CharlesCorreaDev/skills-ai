Ciclo de vida do objeto
***********************

Esta seção explica como os slots de um tipo se relacionam entre si ao
longo da vida de um objeto. Não se destina a ser uma referência
canônica completa para os slots; em vez disso, consulte a documentação
específica do slot em Estruturas de objetos tipo para obter detalhes
sobre um slot específico.


Eventos de vida
===============

A figura abaixo ilustra a ordem dos eventos que podem ocorrer ao longo
da vida de um objeto. Uma seta de *A* para *B* indica que o evento *B*
pode ocorrer após a ocorrência do evento *A*, com o rótulo da seta
indicando a condição que deve ser verdadeira para que *B* ocorra após
*A*.

[imagem: Diagrama mostrando eventos na vida de um objeto. Explicado em
detalhes abaixo.][imagem]

Explicação:

* Quando um novo objeto é construído chamando seu tipo:

  1. "tp_new" é chamado para criar um novo objeto.

  2. "tp_alloc" é chamado diretamente por "tp_new" para alocar a
     memória para o novo objeto.

  3. "tp_init" inicializa o objeto recém-criado. "tp_init" pode ser
     chamado novamente para reinicializar um objeto, se desejado. A
     chamada DE "tp_init" também pode ser completamente ignorada, por
     exemplo, com código Python chamando "__new__()".

* Após a conclusão de "tp_init", o objeto estará pronto para uso.

* Algum tempo após a última referência a um objeto ser removida:

  1. Se um objeto não estiver marcado como *finalizado*, ele poderá
     ser finalizado marcando-o como *finalizado* e chamando sua função
     "tp_finalize". O Python *não* finaliza um objeto quando a última
     referência a ele é excluída; use
     "PyObject_CallFinalizerFromDealloc()" para garantir que
     "tp_finalize" seja sempre chamado.

  2. Se o objeto estiver marcado como finalizado, "tp_clear" poderá
     ser chamado pelo coletor de lixo para limpar as referências
     mantidas pelo objeto. Ele *não* é chamado quando a contagem de
     referências do objeto chega a zero.

  3. "tp_dealloc" é chamado para destruir o objeto. Para evitar
     duplicação de código, "tp_dealloc" normalmente chama "tp_clear"
     para liberar as referências do objeto.

  4. Quando "tp_dealloc" termina a destruição do objeto, ele chama
     diretamente "tp_free" (geralmente definido como "PyObject_Free()"
     ou "PyObject_GC_Del()" automaticamente, conforme apropriado para
     o tipo) para desalocar a memória.

* A função "tp_finalize" tem permissão para adicionar uma referência
  ao objeto, se desejado. Se isso acontecer, o objeto será
  *ressuscitado*, impedindo sua destruição pendente. (Somente
  "tp_finalize" tem permissão para ressuscitar um objeto; "tp_clear" e
  "tp_dealloc" não podem sem chamar "tp_finalize".) Ressuscitar um
  objeto pode ou não causar a remoção da marca *finalizado* do objeto.
  Atualmente, o Python não remove a marca *finalizado* de um objeto
  ressuscitado se ele suportar coleta de lixo (ou seja, o sinalizador
  "Py_TPFLAGS_HAVE_GC" estiver definido), mas remove a marca se o
  objeto não suportar coleta de lixo; qualquer um ou ambos os
  comportamentos podem mudar no futuro.

* "tp_dealloc" pode opcionalmente chamar "tp_finalize" via
  "PyObject_CallFinalizerFromDealloc()" se desejar reutilizar esse
  código para auxiliar na destruição de objetos. Isso é recomendado
  porque garante que "tp_finalize" seja sempre chamado antes da
  destruição. Consulte a documentação de "tp_dealloc" para obter um
  exemplo de código.

* Se o objeto for membro de um *isolado cíclico* e "tp_clear" não
  conseguir interromper o ciclo de referência ou o isolado cíclico não
  for detectado (talvez "gc.disable()" tenha sido chamado ou o
  sinalizador "Py_TPFLAGS_HAVE_GC" tenha sido omitido erroneamente em
  um dos tipos envolvidos), os objetos permanecerão indefinidamente
  não coletáveis (eles "vazam"). Veja "gc.garbage".

Se o objeto for marcado como compatível com coleta de lixo (o
sinalizador "Py_TPFLAGS_HAVE_GC" estiver definido em "tp_flags"), os
seguintes eventos também serão possíveis:

* O coletor de lixo ocasionalmente chama "tp_traverse" para
  identificar *isolados cíclicos*.

* Quando o coletor de lixo descobre um *isolado cíclico*, ele finaliza
  um dos objetos do grupo marcando-o como *finalizado* e chamando sua
  função "tp_finalize", se houver. Isso se repete até que o isolado
  cíclico não exista mais ou todos os objetos tenham sido finalizados.

* "tp_finalize" tem permissão para ressuscitar o objeto adicionando
  uma referência externa ao *isolado cíclico*. A nova referência faz
  com que o grupo de objetos não forme mais um isolado cíclico (o
  ciclo de referência ainda pode existir, mas se existir, os objetos
  não estarão mais isolados).

* Quando o coletor de lixo descobre um *isolado cíclico* e todos os
  objetos do grupo já foram marcados como *finalizados*, o coletor de
  lixo limpa um ou mais objetos não limpos no grupo (possivelmente
  simultaneamente) chamando a função "tp_clear" de cada um. Isso se
  repete enquanto o isolado cíclico ainda existir e nem todos os
  objetos tiverem sido limpos.


Destruição de isolado cíclico
=============================

Abaixo estão listados os estágios de vida de um *isolado cíclico*
hipotético que continua a existir após cada objeto membro ser
finalizado ou limpo. É um vazamento de memória se um isolado cíclico
passar por todos esses estágios; ele deve desaparecer assim que todos
os objetos forem limpos, ou até mesmo antes. Um isolado cíclico pode
desaparecer porque o ciclo de referência foi quebrado ou porque os
objetos não estão mais isolados devido à ressurreição do finalizador
(veja "tp_finalize").

* **Alcançável** (ainda não é um isolado cíclico): todos os objetos
  estão em seu estado normal e acessível. Um ciclo de referência pode
  existir, mas uma referência externa significa que os objetos ainda
  não estão isolados.

* **Inalcançável, mas consistente:** a referência final de fora do
  grupo cíclico de objetos foi removida, causando o isolado dos
  objetos (criando assim um isolado cíclico). Nenhum dos objetos do
  grupo foi finalizado ou limpo ainda. O isolado cíclico permanece
  neste estágio até alguma execução futura do coletor de lixo (não
  necessariamente a próxima execução, pois a próxima execução pode não
  varrer todos os objetos).

* **Mistura de finalizados e não finalizados:** objetos em um isolado
  cíclico são finalizados um de cada vez, o que significa que há um
  período em que o isolado cíclico é composto por uma mistura de
  objetos finalizados e não finalizados. A ordem de finalização não é
  especificada, portanto, pode parecer aleatória. Um objeto finalizado
  deve se comportar de maneira sensata quando objetos não finalizados
  interagem com ele, e um objeto não finalizado deve ser capaz de
  tolerar a finalização de um subconjunto arbitrário de seus
  referentes.

* **Todos finalizados:** todos os objetos em um isolado cíclico são
  finalizados antes que qualquer um deles seja limpo.

* **Combinação de finalizado e limpo:** os objetos podem ser limpos em
  série ou simultaneamente (mas com a *GIL* mantida); de qualquer
  forma, alguns serão concluídos antes de outros. Um objeto finalizado
  deve ser capaz de tolerar a limpeza de um subconjunto de seus
  referentes. **PEP 442** chama essa etapa de "lixo cíclico".

* **Vazamento:** se um isolado cíclico ainda existir após todos os
  objetos do grupo terem sido finalizados e limpos, os objetos
  permanecerão indefinidamente não coletáveis (consulte "gc.garbage").
  É um bug se um isolado cíclico atingir esse estágio --- significa
  que os métodos "tp_clear" dos objetos participantes falharam em
  interromper o ciclo de referência conforme necessário.

Se "tp_clear" não existisse, o Python não teria como interromper com
segurança um ciclo de referência. A simples destruição de um objeto em
um isolado cíclico resultaria em um ponteiro pendente, desencadeando
um comportamento indefinido quando um objeto que referencia o objeto
destruído é destruído. A etapa de limpeza torna a destruição de
objetos um processo de duas fases: primeiro, "tp_clear" é chamado para
destruir parcialmente os objetos o suficiente para desvinculá-los uns
dos outros; em seguida, "tp_dealloc" é chamado para completar a
destruição.

Ao contrário da limpeza, a finalização não é uma fase da destruição.
Um objeto finalizado ainda deve se comportar corretamente, continuando
a cumprir seus contratos de design. O finalizador de um objeto pode
executar código Python arbitrário e até mesmo impedir a destruição
iminente adicionando uma referência. O finalizador está relacionado à
destruição apenas pela ordem de chamada — se for executado, será
executado antes da destruição, que começa com "tp_clear" (se chamado)
e termina com "tp_dealloc".

A etapa de finalização não é necessária para recuperar com segurança
os objetos em um isolado cíclico, mas sua existência facilita o design
de tipos que se comportam de maneira sensata quando os objetos são
limpos. Limpar um objeto pode necessariamente deixá-lo em um estado
quebrado, parcialmente destruído — pode ser inseguro chamar qualquer
um dos métodos do objeto limpo ou acessar qualquer um de seus
atributos. Com a finalização, apenas objetos finalizados podem
interagir com objetos limpos; objetos não finalizados têm a garantia
de interagir apenas com objetos não limpos (mas potencialmente
finalizados).

Para resumir as interações possíveis:

* Um objeto não finalizado pode ter referências a ou de objetos não
  finalizados e finalizados, mas não a ou de objetos limpos.

* Um objeto finalizado pode ter referências a ou de objetos não
  finalizados, finalizados e limpos.

* Um objeto limpo pode ter referências a ou de objetos finalizados e
  limpos, mas não a ou de objetos não finalizados.

Sem ciclos de referência, um objeto pode ser simplesmente destruído
após a exclusão de sua última referência; as etapas de finalização e
limpeza não são necessárias para recuperar objetos não utilizados com
segurança. No entanto, pode ser útil chamar automaticamente
"tp_finalize" e "tp_clear" antes da destruição, pois o design de tipos
é simplificado quando todos os objetos sempre experimentam a mesma
série de eventos, independentemente de terem participado ou não de um
isolado cíclico. Atualmente, o Python chama "tp_finalize" e "tp_clear"
apenas conforme necessário para destruir um isolado cíclico; isso pode
mudar em uma versão futura.


Funções
=======

Para alocar e liberar memória, consulte Alocando objetos na heap.

void PyObject_CallFinalizer(PyObject *op)

   Finaliza o objeto conforme descrito em "tp_finalize". Chame esta
   função (ou "PyObject_CallFinalizerFromDealloc()") em vez de chamar
   "tp_finalize" diretamente, pois esta função pode desduplicar várias
   chamadas para "tp_finalize". Atualmente, as chamadas são
   desduplicadas somente se o tipo oferecer suporte a coleta de lixo
   (ou seja, se o sinalizador "Py_TPFLAGS_HAVE_GC" estiver definido);
   isso pode mudar no futuro.

   Adicionado na versão 3.4.

int PyObject_CallFinalizerFromDealloc(PyObject *op)
    * Parte da ABI Estável desde a versão 3.15.*

   O mesmo que "PyObject_CallFinalizer()", mas deve ser chamado no
   início do destrutor do objeto ("tp_dealloc"). Não deve haver
   nenhuma referência ao objeto. Se o finalizador do objeto
   ressuscitar o objeto, esta função retornará -1; nenhuma outra
   destruição deverá ocorrer. Caso contrário, esta função retornará 0
   e a destruição pode continuar normalmente.

   Adicionado na versão 3.4.

   Ver também: "tp_dealloc" para código de exemplo.
