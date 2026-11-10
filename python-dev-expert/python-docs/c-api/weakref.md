Objetos referência fraca
************************

Python oferece suporte a *referências fracas* como objetos de primeira
classe. Existem dois tipos de objetos específicos que implementam
diretamente referências fracas. O primeiro é um objeto de referência
simples, e o segundo atua como um intermediário entre o objeto
original e o primeiro, tanto quanto possível.

int PyWeakref_Check(PyObject *ob)

   Retorna não zero se *ob* for um objeto referência ou um objeto
   intermediário. Esta função sempre tem sucesso.

int PyWeakref_CheckRef(PyObject *ob)

   Retorna não zero se *ob* for um objeto referência ou uma subclasse
   do tipo de referência. Esta função sempre tem sucesso.

int PyWeakref_CheckRefExact(PyObject *ob)

   Retorna não zero se *ob* for um objeto referência, mas não uma
   subclasse do tipo de referência. Esta função sempre tem sucesso.

int PyWeakref_CheckProxy(PyObject *ob)

   Retorna não zero se *ob* for um objeto intermediário. Esta função
   sempre tem sucesso.

PyObject *PyWeakref_NewRef(PyObject *ob, PyObject *callback)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um objeto de referência fraca para o objeto *ob*. Isso
   sempre retornará uma nova referência, mas não é garantido que um
   novo objeto seja criado; um objeto de referência existente pode ser
   retornado. O segundo parâmetro, *callback*, pode ser um objeto
   chamável que recebe uma notificação quando *ob* for coletado como
   lixo; ele deve aceitar um único parâmetro, que será o objeto de
   referência fraca propriamente dito. *callback* também pode ser
   "None" ou "NULL". Se *ob* não for um objeto fracamente
   referenciável, isso retornará "NULL" e levantará "TypeError".

   Ver também:

     "PyType_SUPPORTS_WEAKREFS()" para verificar se *ob* é fracamente
     referenciável.

PyObject *PyWeakref_NewProxy(PyObject *ob, PyObject *callback)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Retorna um objeto proxy de referência fraca para o objeto *ob*.
   Isso sempre retornará uma nova referência, mas não é garantido que
   um novo objeto seja criado; um objeto proxy de referência existente
   pode ser retornado. O segundo parâmetro, *callback*, pode ser um
   objeto chamável que recebe uma notificação quando *ob* for coletado
   como lixo; ele deve aceitar um único parâmetro, que será o objeto
   de referência fraca propriamente dito. *callback* também pode ser
   "None" ou "NULL". Se *ob* for um objeto fracamente referenciável,
   isso retornará "NULL" e levantará "TypeError".

   Ver também:

     "PyType_SUPPORTS_WEAKREFS()" para verificar se *ob* é fracamente
     referenciável.

int PyWeakref_GetRef(PyObject *ref, PyObject **pobj)
    * Parte da ABI Estável desde a versão 3.13.*

   Obtém uma *referência forte* para o objeto referenciado a partir de
   uma referência fraca, *ref*, em **pobj*.

   * Em caso de sucesso, define **pobj* como uma nova *referência
     forte* para o objeto referenciado e retorna 1.

   * Se a referência estiver quebrada, define **pobj* como "NULL" e
     retorna 0.

   * Em caso de erro, levanta uma exceção e retorna -1.

   Adicionado na versão 3.13.

int PyWeakref_IsDead(PyObject *ref)

   Testa se a referência fraca *ref* está inativa. Retorna 1 se a
   referência estiver inativa, 0 se estiver ativa e -1 com um erro
   definido se *ref* não for um objeto referência fraca.

   Adicionado na versão 3.14.

void PyObject_ClearWeakRefs(PyObject *object)
    * Parte da ABI Estável.*

   Esta função é chamada pelo tratador "tp_dealloc" para limpar
   referências fracas.

   Isso itera pelas referências fracas para *object* e chama as
   funções de retorno para as referências que possuem um. Ele retorna
   quando todas as funções de retorno tiverem sido executadas.

PyObject **PyObject_GET_WEAKREFS_LISTPTR(PyObject *object)

   Retorna um ponteiro para uma lista encadeada interna de referências
   fracas para *object*. *object* deve oferecer suporte a referências
   fracas e não deve ser "NULL".

   Esta função destina-se apenas a uso interno. Não acesse nem
   modifique a lista de referências fracas por meio do ponteiro
   retornado.

   Suavemente descontinuado desde a versão 3.15.2.

void PyUnstable_Object_ClearWeakRefsNoCallbacks(PyObject *object)

   *Esta é uma API Instável. Isso pode se alterado sem aviso em
   lançamentos menores.*

   Limpa as referências fracas para *object* sem chamar as funções de
   retorno.

   Esta função é chamada pelo manipulador "tp_dealloc" para tipos com
   finalizadores (por exemplo, "__del__()"). O manipulador para esses
   objetos primeiro chama "PyObject_ClearWeakRefs()" para limpar
   referências fracas e chamar suas funções de retorno, depois o
   finalizador e, finalmente, esta função para limpar quaisquer
   referências fracas que possam ter sido criadas pelo finalizador.

   Na maioria das circunstâncias, é mais apropriado usar
   "PyObject_ClearWeakRefs()" para limpar referências fracas em vez
   desta função.

   Adicionado na versão 3.13.
