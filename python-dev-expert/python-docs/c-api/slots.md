Slots de definição
******************

Para definir objetos de módulo e classes usando a API C, você pode
usar um vetor de *slots* -- essencialmente, pares de chave-valor que
descrevem características do objeto a ser criado. Isso desacopla os
dados das estruturas usadas em tempo de execução, permitindo que o
CPython -- e outras implementações da API C do Python -- atualizem as
estruturas sem quebrar a retrocompatibilidade.

Esta seção documenta os slots em geral. Para comportamento específico
de objetos e valores de slots, consulte a documentação das funções que
aplicam slots:

* "PyType_FromSlots()" para tipos;

* "PyModule_FromSlotsAndSpec()" e Extension export hook para módulos.

Quando os slots são passados para uma função que os aplica, a função
não modificará o vetor de slots, nem quaisquer dados para os quais ela
aponte (recursivamente). Depois que a função terminar, o chamador tem
permissão para modificar ou desalocar o vetor e quaisquer dados para
os quais ela aponte (recursivamente), exceto dados marcados
explicitamente com "PySlot_STATIC".

Exceto quando documentado de outra forma, vários slots com o mesmo ID
("sl_id") não podem ocorrer em um único vetor de slots.

Adicionado na versão 3.15: As matrizes de slots generalizam uma forma
anterior de definir objetos: usando "PyType_Spec" com "PyType_Slot"
para tipos, e "PyModuleDef" com "PyModuleDef_Slot" para módulos. A API
anterior está *suavemente descontinuada*; não há planos para
removê-la.

As entradas do vetor de slots utilizam a seguinte estrutura:

type PySlot
    * Parte da ABI Estável (incluindo todos os membros) desde a versão
   3.15.*

   Uma entrada em um vetor de slots. Definida como:

      typedef struct {
          uint16_t sl_id;
          uint16_t sl_flags;
          union {
              uint32_t sl_reserved;  // deve ser 0
          };
          union {
              void *sl_ptr;
              void (*sl_func)(void);
              Py_ssize_t sl_size;
              int64_t sl_int64;
              uint64_t sl_uint64;
          };
      } PySlot;

   uint16_t sl_id

      Um ID de slot, escolhido entre:

      * Valores "Py_slot_*" documentados em IDs de slot comuns abaixo;

      * Valores "Py_mod_*" para módulos, conforme documentado em
        Module definition;

      * Valores para tipos, conforme documentado em Type slot IDs.

      Um "sl_id" igual a zero ("Py_slot_end") marca o fim de um vetor
      de slots.

   void *sl_ptr
   void (*sl_func)(void)
   Py_ssize_t sl_size
   int64_t sl_int64
   uint64_t sl_uint64

      Os dados para o slot. Esses membros fazem parte de uma união
      anônima; o membro a ser usado depende de qual tipo de dado é
      exigido pelo ID do slot: ponteiro de dados, ponteiro de função,
      tamanho, inteiro com sinal ou sem sinal, respectivamente.

      Exceto quando documentado de outra forma para um ID de slot
      específico, ponteiros (ou seja, "sl_ptr" e "sl_func") não podem
      ser NULL.

   uint16_t sl_flags

      Zero ou mais dos seguintes sinalizadores, combinados com OU bit
      a bit (OR):

      PySlot_STATIC
          * Parte da ABI Estável desde a versão 3.15.*

         Todos os dados para os quais o slot aponta são alocados
         estaticamente e constantes. Portanto, o interpretador não
         precisa copiar a informação.

         Este sinalizador é implícito para ponteiros de função.

         O sinalizador se aplica mesmo aos dados para os quais o slot
         aponta "indiretamente", exceto para slots aninhados via
         "Py_slot_subslots" que podem ter seus próprios sinalizadores
         "PySlot_STATIC". Por exemplo, se aplicado a um slot
         "Py_tp_members" que aponta para um vetor de estruturas
         "PyMemberDef", então toda o vetor, bem como o nome e as
         strings de documentação (doc strings) em seus elementos,
         devem ser estáticos e constantes.

      PySlot_INTPTR
          * Parte da ABI Estável desde a versão 3.15.*

         Os dados são armazenados em "sl_ptr"; o CPython fará o *cast*
         (conversão explícita) para o tipo apropriado.

         Este sinalizador pode simplificar a portabilidade a partir
         das estruturas mais antigas "PyType_Slot" e
         "PyModuleDef_Slot".

      PySlot_OPTIONAL
          * Parte da ABI Estável desde a versão 3.15.*

         Se o ID do slot for desconhecido, o interpretador deve
         ignorar o slot, em vez de falhar.

         Por exemplo, se o Python 3.16 adicionar um novo recurso com
         um novo ID de slot, o slot correspondente poderá ser marcado
         como "PySlot_OPTIONAL" para que o Python 3.15 o ignore.

         Observe que a "opcionalidade" aplica-se apenas a IDs de slot
         desconhecidos. Este sinalizador não faz com que o Python
         ignore valores inválidos de slots conhecidos.

   Adicionado na versão 3.15.


Macros de conveniência
======================

PySlot_DATA(name, value)
PySlot_FUNC(name, value)
PySlot_SIZE(name, value)
PySlot_INT64(name, value)
PySlot_UINT64(name, value)
PySlot_STATIC_DATA(name, value)
    * This macro is available when compiling for the ABI Estável desde
   a versão 3.15.*

   Macros de conveniência para definir estruturas "PySlot" com "sl_id"
   e um membro de união específico definido.

   "PySlot_STATIC_DATA" define o sinalizador "PySlot_STATIC"; as
   demais não definem nenhum sinalizador.

   Observe que essas macros usam *inicializadores designados*
   (*designated initializers*), um recurso da linguagem C que o C++
   adicionou na versão de 2020 do padrão. Se o seu código precisar ser
   compatível com C++11 ou anterior, use "PySlot_PTR" em vez disso.

   Definido como:

      #define PySlot_DATA(NAME, VALUE) \
         {.sl_id=NAME, .sl_ptr=(void*)(VALUE)}

      #define PySlot_FUNC(NAME, VALUE) \
         {.sl_id=NAME, .sl_func=(VALUE)}

      #define PySlot_SIZE(NAME, VALUE) \
         {.sl_id=NAME, .sl_size=(VALUE)}

      #define PySlot_INT64(NAME, VALUE) \
         {.sl_id=NAME, .sl_int64=(VALUE)}

      #define PySlot_UINT64(NAME, VALUE) \
         {.sl_id=NAME, .sl_uint64=(VALUE)}

      #define PySlot_STATIC_DATA(NAME, VALUE) \
         {.sl_id=NAME, .sl_flags=PySlot_STATIC, .sl_ptr=(VALUE)}

   Adicionado na versão 3.15.

PySlot_END
    * This macro is available when compiling for the ABI Estável desde
   a versão 3.15.*

   Macro de conveniência para marcar o fim de um vetor "PySlot".

   Definido como:

      #define PySlot_END {0}

   Adicionado na versão 3.15.

PySlot_PTR(name, value)
PySlot_PTR_STATIC(name, value)
    * This macro is available when compiling for the ABI Estável desde
   a versão 3.15.*

   Macros de conveniência para uso em código compatível com C++11.
   Esta versão do C++ não permite definir membros de união arbitrários
   em literais; em vez disso, estas macros definem o sinalizador
   "PySlot_INTPTR" e fazem o *cast* do valor para "(void*)".

   Definido como:

      #define PySlot_PTR(NAME, VALUE) \
         {NAME, PySlot_INTPTR, {0}, {(void*)(VALUE)}}

      #define PySlot_PTR_STATIC(NAME, VALUE) \
         {NAME, PySlot_INTPTR|Py_SLOT_STATIC, {0}, {(void*)(VALUE)}}

   Adicionado na versão 3.15.


IDs de slot comuns
==================

Os seguintes IDs de slot podem ser usados tanto em definições de tipo
quanto de módulo.

Py_slot_end
    * Parte da ABI Estável desde a versão 3.15.*

   Marca o fim de um vetor de slots. Definido como zero.

   Adicionado na versão 3.15.

Py_slot_subslots
    * Parte da ABI Estável desde a versão 3.15.*

   Vetor de slots aninhados.

   O valor ("sl_ptr") deve apontar para um vetor de estruturas
   "PySlot". Os slots no vetor (até o terminador de ID zero,
   exclusivo) serão tratados como se tivessem sido inseridos no vetor
   de slots atual, no ponto em que "Py_slot_subslots" aparecer.

   A profundidade de aninhamento de slots é limitada a 5 níveis. Esta
   restrição poderá ser removida no futuro.

   Adicionado na versão 3.15.

Py_slot_invalid
    * Parte da ABI Estável desde a versão 3.15.*

   Reservado; será sempre tratado como um ID de slot desconhecido.
   Definido como "UINT16_MAX" ("0xFFFF").

   Quando usado com o sinalizador "PySlot_OPTIONAL", define um slot
   sem nenhum efeito. Sem o sinalizador, o processamento de um slot
   com este ID falhará.

   Adicionado na versão 3.15.
