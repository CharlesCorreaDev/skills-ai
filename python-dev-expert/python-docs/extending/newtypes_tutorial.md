Definindo Tipos de Extensão: Tutorial
*************************************

O Python permite que o desenvolvedor de um módulo de extensão em C
defina novos tipos que podem ser manipulados a partir do código
Python, da mesma forma que os tipos embutidos "str" e "list". O código
para de todos tipos de extensão segue um padrão, mas há alguns
detalhes que você precisa entender antes de começar. Este documento é
uma introdução suave ao tópico.


O básico
========

O tempo de execução do *CPython* trata todos os objetos Python como
variáveis do tipo PyObject*, que funciona como um “tipo base” para
todos os objetos Python. A estrutura "PyObject" em si contém apenas a
*contagem de referências* do objeto e um ponteiro para o “objeto de
tipo” correspondente. É nesse objeto de tipo que tudo acontece: ele
determina quais funções em C o interpretador chama quando, por
exemplo, um atributo é acessado em um objeto, um método é chamado ou o
objeto é multiplicado por outro. Essas funções em C são chamadas de
“métodos de tipo”.

Então, se você quiser definir um novo tipo de extensão, você precisa
criar um novo objeto de tipo.

Esse tipo de coisa só pode ser explicado com exemplo, então aqui está
um módulo mínimo, mas completo, que define um novo tipo nomeado
"Custom" dentro de um módulo de extensão C "custom":

Nota:

  O que estamos mostrando aqui é a maneira tradicional de definir
  tipos de extensão *estáticos*. Deve ser adequada para a maioria dos
  usos. A API C também permite definir tipos de extensão alocados em
  heap usando a função "PyType_FromSpec()", que não é abordada neste
  tutorial.

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

   typedef struct {
       PyObject_HEAD
       /* Campos específico do tipo vão aqui. */
   } CustomObject;

   static PyTypeObject CustomType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom.Custom",
       .tp_doc = PyDoc_STR("Custom objects"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT,
       .tp_new = PyType_GenericNew,
   };

   static int
   custom_module_exec(PyObject *m)
   {
       if (PyType_Ready(&CustomType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot custom_module_slots[] = {
       {Py_mod_exec, custom_module_exec},
       // Só use isso quando estiver usando tipos estáticos
       {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
       {0, NULL}
   };

   static PyModuleDef custom_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "custom",
       .m_doc = "Example module that creates an extension type.",
       .m_size = 0,
       .m_slots = custom_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_custom(void)
   {
       return PyModuleDef_Init(&custom_module);
   }

Isso é bastante informação para assimilar de uma só vez, mas algumas
partes devem parecer familiares pelo que foi visto no capítulo
anterior. Este arquivo define três elementos:

1. O que um **objeto** "Custom" contém: esta é uma estrutura
   "CustomObject", alocada uma vez para cada instância de "Custom".

2. Como o **tipo** "Custom" se comporta: esta é a estrutura
   "CustomType", que define um conjunto de sinalizadores e ponteiros
   de função que o interpretador inspeciona quando operações
   específicas são solicitadas.

3. Como definir e executar o módulo "custom": esta é a função
   "PyInit_custom" e a estrutura associada "custom_module" para
   definir o módulo, e a função "custom_module_exec" para configurar
   um novo objeto de módulo.

O primeiro bit é

   typedef struct {
       PyObject_HEAD
   } CustomObject;

Isto é o que um objeto Custom conterá. "PyObject_HEAD" é obrigatório
no início de cada estrutura de objeto e define um campo chamado
"ob_base" do tipo "PyObject", contendo um ponteiro para um objeto de
tipo e uma contagem de referências (esses podem ser acessados usando
os macros "Py_TYPE" e "Py_REFCNT", respectivamente). O objetivo do
macro é abstrair o layout e permitir campos adicionais em construções
de depuração.

Nota:

  Não há ponto e vírgula acima após o macro "PyObject_HEAD". Tenha
  cuidado para não adicionar um por engano: alguns compiladores podem
  emitir erros.

Obviamente, objetos geralmente armazenam dados adicionais além do
padrão "PyObject_HEAD" boilerplate; por exemplo, aqui está a definição
do padrão Python floats:

   typedef struct {
       PyObject_HEAD
       double ob_fval;
   } PyFloatObject;

O segundo bit é a definição do objeto de tipo.

   estático PyTypeObject CustomType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom.Custom",
       .tp_doc = PyDoc_STR("Custom objeto"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT,
       .tp_new = PyType_GenericNew,
   };

Nota:

  Recomendamos usar inicializadores nomeados no estilo C99, como
  mostrado acima, para evitar listar todos os campos de "PyTypeObject"
  com os quais você não precisa se preocupar e também para não
  depender da ordem de declaração desses campos

A definição real de "PyTypeObject" no "object.h" possui muito mais
campos do que a definição acima. Os campos restantes serão preenchidos
com zeros pelo compilador C, e é prática comum não especificá-los
explicitamente, a menos que sejam necessários.

Vamos separá-lo, um campo de cada vez

   .ob_base = PyVarObject_HEAD_INIT(NULL, 0)

Essa linha é um boilerplate obrigatório para inicializar o campo
"ob_base" mencionado acima.

   .tp_name = "custom.Custom",

O nome do nosso tipo.  Ele aparecerá na representação textual padrão
do nosso objeto e em algumas mensagens erro, por exemplo:

   >>> "" + custom.Custom()
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: can only concatenate str (not "custom.Custom") to str

Observe que o nome é um nome pontilhado que inclui o nome módulo e o
nome do tipo dentro do módulo. O módulo, neste caso, é "custom" e o
tipo é "Custom", portanto, definimos o nome do tipo como
"custom.Custom". O uso do pontilhado real caminho de importação é
importante para tornar seu tipo compatível com o "pydoc" e os módulos
"pickle".

   .tp_basicsize = sizeof(CustomObject),
   .tp_itemsize = 0,

Isso serve para que o Python saiba quanta memória deve ser alocada ao
criar novas instâncias do "Custom". O "tp_itemsize" é usado somente
para objeto de tamanho variável e, caso contrário, deve ser zero.

Nota:

  Se você quiser que seu tipo possa ser subclassificado a partir do
  Python, e seu tipo tiver o mesmo "tp_basicsize" que seu tipo base,
  você poderá ter problemas com herança múltipla. Uma subclasse Python
  do seu tipo terá de listar o seu tipo primeiro em "__bases__", caso
  contrário ela não conseguirá chamar o método "__new__()" do seu tipo
  sem gerar um erro. Você pode evitar esse problema garantindo que seu
  tipo tenha um valor de "tp_basicsize" maior que o do tipo base. Na
  maior parte do tempo, isso já será verdadeiro, pois ou o tipo base
  será "object", ou você estará adicionando membros de dados ao seu
  tipo base e, portanto, aumentando seu tamanho.

Definimos os sinalizadores da classe como "Py_TPFLAGS_DEFAULT".

   .tp_flags = Py_TPFLAGS_DEFAULT,

Todos os tipos devem incluir essa constante em seus sinalizadores. Ela
habilita todos os membros definidos até pelo menos o Python 3.3. Se
você precisar de membros adicionais, será necessário fazer um OR com
os sinalizadores correspondentes.

Fornecemos uma docstring para o tipo em tp_doc "tp_doc".

   .tp_doc = PyDoc_STR("Custom objects"),

Para habilitar a criação de objetos, precisamos fornecer um
manipulador para "tp_new". Esse é o equivalente ao método Python
"__new__()", mas precisa ser especificado explicitamente. Neste caso,
podemos simplesmente usar a implementação padrão fornecida pela função
da API "PyType_GenericNew()".

   .tp_new = PyType_GenericNew,

Todo o restante do arquivo deve ser familiar, exceto por alguns
códigos em "custom_module_exec()":

   se (PyType_Ready(&CustomType) < 0) {
       retorno -1;
   }

Isso inicializa o tipo "Custom", preenchendo vários membros com os
valores padrão apropriados, incluindo "ob_type", que definimos
inicialmente como "NULL".

   if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
   return -1;
   }

Isso adiciona o tipo ao dicionário do módulo. Isso nos permite criar
instâncias de "Custom" chamando a classe "Custom":

   >>> import custom
   >>> mycustom = custom.Custom()

É isso! Só resta compilá-lo; coloque o código acima em um arquivo
chamado "custom.c",

   [build-system]
   requires = ["setuptools"]
   build-backend = "setuptools.build_meta"

   [project]
   name = "custom"
   version = "1"

Em um arquivo chamado "pyproject.toml", e

   from setuptools import Extension, setup
   setup(ext_modules=[Extension("custom", ["custom.c"])])

Em um arquivo chamado "setup.py"; e então digitando

   $ python -m pip install .

no console deverá gerar um arquivo "custom.so" em um subdiretório e
instalá-lo; agora abra o Python — você já deve conseguir "import
custom" e experimentar objetos "Custom".

Isso não foi tão difícil, foi?

Naturalmente, o tipo Custom atual é bastante desinteressante. Não tem
dados e não faz nada. Não pode nem ser subclassificado.


Adicionando dados e métodos ao exemplo básico
=============================================

Vamos estender o exemplo básico para adicionar alguns dados e métodos.
Também vamos tornar o tipo utilizável como uma classe base. Iremos
criar um novo módulo, "custom2", que adiciona esses recursos:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>
   #include <stddef.h> /* for offsetof() */

   typedef struct {
       PyObject_HEAD
       PyObject *first; /* first name */
       PyObject *last;  /* last name */
       int number;
   } CustomObject;

   static void
   Custom_dealloc(PyObject *op)
   {
       CustomObject *self = (CustomObject *) op;
       Py_XDECREF(self->first);
       Py_XDECREF(self->last);
       Py_TYPE(self)->tp_free(self);
   }

   static PyObject *
   Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
   {
       CustomObject *self;
       self = (CustomObject *) type->tp_alloc(type, 0);
       if (self != NULL) {
           self->first = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->first == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->last = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->last == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->number = 0;
       }
       return (PyObject *) self;
   }

   static int
   Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       CustomObject *self = (CustomObject *) op;
       static char *kwlist[] = {"first", "last", "number", NULL};
       PyObject *first = NULL, *last = NULL;

       if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist,
                                        &first, &last,
                                        &self->number))
           return -1;

       if (first) {
           Py_XSETREF(self->first, Py_NewRef(first));
       }
       if (last) {
           Py_XSETREF(self->last, Py_NewRef(last));
       }
       return 0;
   }

   static PyMemberDef Custom_members[] = {
       {"first", Py_T_OBJECT_EX, offsetof(CustomObject, first), 0,
        "first name"},
       {"last", Py_T_OBJECT_EX, offsetof(CustomObject, last), 0,
        "last name"},
       {"number", Py_T_INT, offsetof(CustomObject, number), 0,
        "custom number"},
       {NULL}  /* Sentinel */
   };

   static PyObject *
   Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
   {
       CustomObject *self = (CustomObject *) op;
       if (self->first == NULL) {
           PyErr_SetString(PyExc_AttributeError, "first");
           return NULL;
       }
       if (self->last == NULL) {
           PyErr_SetString(PyExc_AttributeError, "last");
           return NULL;
       }
       return PyUnicode_FromFormat("%S %S", self->first, self->last);
   }

   static PyMethodDef Custom_methods[] = {
       {"name", Custom_name, METH_NOARGS,
        "Return the name, combining the first and last name"
       },
       {NULL}  /* Sentinel */
   };

   static PyTypeObject CustomType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom2.Custom",
       .tp_doc = PyDoc_STR("Custom objects"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
       .tp_new = Custom_new,
       .tp_init = Custom_init,
       .tp_dealloc = Custom_dealloc,
       .tp_members = Custom_members,
       .tp_methods = Custom_methods,
   };

   static int
   custom_module_exec(PyObject *m)
   {
       if (PyType_Ready(&CustomType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot custom_module_slots[] = {
       {Py_mod_exec, custom_module_exec},
       {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
       {0, NULL}
   };

   static PyModuleDef custom_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "custom2",
       .m_doc = "Example module that creates an extension type.",
       .m_size = 0,
       .m_slots = custom_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_custom2(void)
   {
       return PyModuleDef_Init(&custom_module);
   }

Esta versão do módulo possui várias alterações.

O tipo "Custom" agora possui três atributos de dados em sua estrutura
C: first, last e number. As variáveis first e last são strings Python
contendo o primeiro e o último nome. O atributo number é um inteiro em
C.

A estrutura do objeto é atualizada de acordo

   typedef struct {
   PyObject_HEAD
   PyObject *first; /* first name */
   PyObject *last; /* last name */
   int number;
   } CustomObject;

Como agora temos dados para gerenciar, precisamos ter mais cuidado com
a alocação e a desalocação do objeto.  No mínimo, precisamos de método
de desalocação:

   static void
   Custom_dealloc(PyObject *op)
   {
   CustomObject *self = (CustomObject *) op;
   Py_XDECREF(self->first);
   Py_XDECREF(self->last);
   Py_TYPE(self)->tp_free(self);
   }

que é atribuído ao membro "tp_dealloc":

   tp_dealloc = Custom_dealloc,

Esse método primeiro limpa a contagem de referências dos dois
atributos Python. "Py_XDECREF()" lida corretamente com o caso em que
seu argumento é "NULL" (o que pode acontecer aqui se "tp_new" falhou
no meio do processo). Em seguida, ele chama o membro "tp_free" do tipo
do objeto (obtido por "Py_TYPE(self)") para liberar a memória do
objeto. Observe que o tipo do objeto pode não ser "CustomType", pois o
objeto pode ser uma instância de uma subclasse.

Nota:

  O cast explícito para "CustomObject *" acima é necessário porque
  definimos "Custom_dealloc" para receber um argumento do tipo
  "PyObject *", enquanto o ponteiro de função "tp_dealloc" espera
  receber um argumento "PyObject *". Ao atribuir nossa função ao slot
  "tp_dealloc" de um tipo, estamos declarando que ela só pode ser
  chamada com instâncias da classe "CustomObject"; portanto, o cast
  para "(CustomObject *)" é seguro. Isso é polimorfismo orientado a
  objetos, em C!Em códigos existentes, ou em versões anteriores deste
  tutorial, você pode consultar funções semelhantes receberem
  diretamente um ponteiro para estrutura de objeto do subtipo
  ("CustomObject*"), assim:

     Custom_dealloc(CustomObject *self)
     {
     Py_XDECREF(self->first);
     Py_XDECREF(self->last);
     Py_TYPE(self)->tp_free((PyObject *) self);
     }
     ...
     .tp_dealloc = (destructor) Custom_dealloc,

  Isso faz a mesma coisa em todas as arquiteturas que o CPython
  oferece suporte, mas, de acordo com o padrão da linguagem C, isso
  invoca um comportamento indefinido.

Queremos nos certificar de que o primeiro e o último nome sejam
inicializados como strings vazias, portanto, fornecemos uma
implementação:: "tp_new":

   static PyObject *
   Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
   {
   CustomObject *self;
   self = (CustomObject *) type->tp_alloc(type, 0);
   if (self != NULL) {
   self->first = PyUnicode_FromString("");
   if (self->first == NULL) {
   Py_DECREF(self);
   return NULL;
   }
   self->last = PyUnicode_FromString("");
   if (self->last == NULL) {
   Py_DECREF(self);
   return NULL;
   }
   self->number = 0;
   }
   return (PyObject *) self;
   }

e instale-o no membro:: "tp_new"

   .tp_new = Custom_new,

O manipulador "tp_new" é responsável por criar (em oposição a
inicializar) os objetos do tipo. Ele é exposto no Python como o método
"__new__()". Não é obrigatório definir um membro "tp_new" e, de fato,
muitos tipos de extensão simplesmente reutilizam
"PyType_GenericNew()", como na primeira versão do tipo "Custom" acima.
Neste caso, usamos o manipulador "tp_new" para inicializar os
atributos "first" e "last" com valores padrão que não sejam "NULL".

O "tp_new" recebe o tipo que está sendo instanciado (não
necessariamente "CustomType", caso uma subclasse esteja sendo
instanciada) e quaisquer argumentos passados quando o tipo foi
chamado, e deve retornar a instância criada. Manipuladores "tp_new"
sempre aceitam argumentos posicionais e argumentos nomeados, mas
frequentemente os ignoram, deixando o tratamento dos argumentos para
os métodos inicializadores (ou seja, "tp_init" em C ou "__init__" em
Python).

Nota:

  "tp_new" não deve chamar "tp_init" explicitamente, pois o
  interpretador fará isso por conta própria.

A implementação de "tp_new" chama o slot "tp_alloc" para alocar
memória:

   self = (CustomObject *) type->tp_alloc(type, 0);

Como a alocação de memória pode falhar, precisamos verificar se o
resultado de "tp_alloc" é "NULL" antes de prosseguir.

Nota:

  Nós não preenchemos o slot "tp_alloc" por conta própria. Em vez
  disso, "PyType_Ready()" o preenche herdando-o da nossa classe base,
  que por padrão é "object". A maioria dos tipos usa a estratégia de
  alocação padrão.

Nota:

  Se você estiver criando um "tp_new" cooperativo (um que chama o
  "tp_new" ou "__new__()" de um tipo base), você *não* deve tentar
  determinar qual método chamar usando a ordem de resolução de métodos
  em tempo de execução. Sempre determine estaticamente qual tipo você
  vai chamar e chame seu "tp_new" diretamente ou via
  "type->tp_base->tp_new". Se você não fizer isso, as subclasses
  Python do seu tipo que também herdam de outras classes definidas em
  Python podem não funcionar corretamente. (Especificamente, você pode
  não conseguir criar instâncias dessas subclasses sem receber um
  "TypeError".)

Também definimos uma função de inicialização que aceita argumentos
para fornecer valores iniciais para nosso instância:

   static intCustom_init(PyObject *op, PyObject *args, PyObject *kwds){ CustomObject *self = (CustomObject *) op; static char *kwlist[] = {"first", "last", "number", NULL}; PyObject *first = NULL, *last = NULL, *tmp; if (!PyArg_ParseTupleAndKeywords(args, kwds, "|OOi", kwlist, &first, &last, &self->number)) return -1; if (first) { tmp = self->first; Py_INCREF(first); self->first = first; Py_XDECREF(tmp); } if (last) { tmp = self->last; Py_INCREF(last); self->last = last; Py_XDECREF(tmp); } return 0;}

preenchendo o slot :: "tp_init".

   .tp_init = Custom_init,

O slot "tp_init" é exposto em Python como o método "__init__()". Ele é
usado para inicializar um objeto depois que ele é criado.
Inicializadores sempre aceitam argumentos posicionais e argumentos
nomeados, e devem retornar "0" em caso de sucesso ou "-1" em caso de
erro.

Ao contrário do manipulador "tp_new", não há garantia de que  seja
chamado (por exemplo, o módulo "pickle" por padrão não chama
"__init__()" em instâncias desserializadas). Além disso, "tp_init"
pode ser chamado várias vezes. Qualquer um pode chamar o método
"__init__()" em nossos objetos. Por esse motivo, precisamos ter
cuidado redobrado ao atribuir os novos valores de atributos.
Poderíamos ficar tentados, por exemplo, a atribuir o membro "first"
assim:

   if (first) { Py_XDECREF(self->first); Py_INCREF(first); self->first = first;}

Mas isso seria arriscado. Nosso tipo não restringe o tipo do membro
"first", então ele poderia ser qualquer tipo de objeto. Ele poderia
ter um destrutor que executasse código que tentasse acessar o membro
"first"; ou esse destrutor poderia desanexar o *estado de thread* e
permitir que código arbitrário fosse executado em outras threads,
acessando e modificando nosso objeto.

Para sermos extremamente cautelosos e nos proteger dessa
possibilidade, quase sempre atribuímos novamente os membros antes de
decrementar a contagem de referências. Quando não precisamos fazer
isso?

* quando sabemos absolutamente que a contagem de referência é maior
  que 1;

* quando sabemos que a desalocação do objeto [1] não desvinculará o
  *estado de thread* nem causará quaisquer chamadas de volta no código
  do nosso tipo;

* quando estamos decrementando uma contagem de referências em um
  manipulador "tp_dealloc" de um tipo que não oferece suporte à coleta
  de lixo cíclica [2].

Queremos expor nossas variáveis de instância como atributos. Há várias
maneiras de fazer isso. A forma mais simples é estabelecer definições
de membros:

   static PyMemberDef Custom_members[] = { {"first", Py_T_OBJECT_EX, offsetof(CustomObject, first), 0, "first name"}, {"last", Py_T_OBJECT_EX, offsetof(CustomObject, last), 0, "last name"}, {"number", Py_T_INT, offsetof(CustomObject, number), 0, "custom number"}, {NULL} /* Sentinel */};

e colocar as definições no slot "tp_members":

   .tp_members = Custom_members,

Cada definição de membro possui um nome de membro, um tipo, um
deslocamento, sinalizadores de acesso e uma string de documentação.
Consulte a seção Generic Attribute Management abaixo para mais
detalhes.

Uma desvantagem dessa abordagem é que ela não fornece uma forma de
restringir os tipos de objetos que podem ser atribuídos aos atributos
em Python. Esperamos que os nomes first e last sejam strings, mas
qualquer objeto Python pode ser atribuído. Além disso, os atributos
podem ser excluídos, fazendo com que os ponteiros em C sejam definidos
como "NULL". Mesmo que possamos garantir que os membros sejam
inicializados com valores não "NULL", eles ainda podem acabar sendo
definidos como "NULL" caso os atributos sejam apagados.

Definimos um único método,:meth:*!Custom.name*, que exibe o nome do
objeto como a concatenação do primeiro nome com o último nome

   static PyObject *Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy)){ CustomObject *self = (CustomObject *) op; if (self->first == NULL) { PyErr_SetString(PyExc_AttributeError, "first"); return NULL; } if (self->last == NULL) { PyErr_SetString(PyExc_AttributeError, "last"); return NULL; } return PyUnicode_FromFormat("%S %S", self->first, self->last);}

O método é implementado como uma função em C que recebe uma instância
de "Custom" (ou de uma subclasse de "Custom") como primeiro argumento.
Métodos sempre recebem a instância como primeiro argumento. Eles
também costumam aceitar argumentos posicionais e nomeados, mas, neste
caso, não recebemos nenhum e não precisamos aceitar uma tupla de
argumentos posicionais nem um dicionário de argumentos nomeados. Este
método equivale ao método Python:

   def name(self): return "%s %s" % (self.first, self.last)

Observe que precisamos verificar a possibilidade de que nossos
atributos "first" e "last" estejam com valor "NULL". Isso ocorre
porque eles podem ser excluídos e, nesse caso, ficam definidos como
"NULL". Seria melhor impedir a exclusão desses atributos e restringir
seus valores para que sejam sempre strings. Veremos como fazer isso na
próxima seção.

Agora que definimos o método, precisamos criar uma array de definições
de métodos:

   static PyMethodDef Custom_methods[] = {
   {"name", Custom_name, METH_NOARGS,
   "Return the name, combining the first and last name"
   },
   {NULL} /* Sentinel */
   };

note que usamos o sinalizador "METH_NOARGS" para indicar que o método
não espera argumentos além de *self*)

e atribuí-lo para o slot:: "tp_methods"

   .tp_methods = Custom_methods,

Por fim, tornaremos nosso tipo utilizável como classe base para
herança. Escrevemos nossos métodos com cuidado até agora, garantindo
que eles não façam suposições sobre o tipo do objeto que está sendo
criado ou utilizado; portanto, tudo o que precisamos fazer é adicionar
a "Py_TPFLAGS_BASETYPE" à definição dos sinalizadores da nossa classe:

   .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,

Renomeamos "PyInit_custom()" para "PyInit_custom2()", atualizamos o
nome do módulo na estrutura "PyModuleDef", e atualizamos o nome
completo da classe na estrutura "PyTypeObject".

Finalmente, atualizamos nosso arquivo "setup.py" para incluir o novo
módulo,

   from setuptools import Extension, setupsetup(ext_modules=[ Extension("custom", ["custom.c"]), Extension("custom2", ["custom2.c"]),])

então podemos instalar novamente para realizarmos o "import custom2"

   $ python -m pip install .


Fornecendo controle mais preciso sobre atributos de dados
=========================================================

Nesta seção, forneceremos um controle mais preciso sobre como os
atributos "first" e "last" são definidos no exemplo "Custom". Na
versão anterior do nosso módulo, as variáveis de instância "first" e
"last" podiam receber valores que não fossem strings ou até mesmo ser
excluídas. Queremos garantir que esses atributos sempre contenham
strings.

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>
   #include <stddef.h> /* for offsetof() */

   typedef struct {
       PyObject_HEAD
       PyObject *first; /* first name */
       PyObject *last;  /* last name */
       int number;
   } CustomObject;

   static void
   Custom_dealloc(PyObject *op)
   {
       CustomObject *self = (CustomObject *) op;
       Py_XDECREF(self->first);
       Py_XDECREF(self->last);
       Py_TYPE(self)->tp_free(self);
   }

   static PyObject *
   Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
   {
       CustomObject *self;
       self = (CustomObject *) type->tp_alloc(type, 0);
       if (self != NULL) {
           self->first = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->first == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->last = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->last == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->number = 0;
       }
       return (PyObject *) self;
   }

   static int
   Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       CustomObject *self = (CustomObject *) op;
       static char *kwlist[] = {"first", "last", "number", NULL};
       PyObject *first = NULL, *last = NULL;

       if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                        &first, &last,
                                        &self->number))
           return -1;

       if (first) {
           Py_SETREF(self->first, Py_NewRef(first));
       }
       if (last) {
           Py_SETREF(self->last, Py_NewRef(last));
       }
       return 0;
   }

   static PyMemberDef Custom_members[] = {
       {"number", Py_T_INT, offsetof(CustomObject, number), 0,
        "custom number"},
       {NULL}  /* Sentinel */
   };

   static PyObject *
   Custom_getfirst(PyObject *op, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       return Py_NewRef(self->first);
   }

   static int
   Custom_setfirst(PyObject *op, PyObject *value, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       if (value == NULL) {
           PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
           return -1;
       }
       if (!PyUnicode_Check(value)) {
           PyErr_SetString(PyExc_TypeError,
                           "The first attribute value must be a string");
           return -1;
       }
       Py_SETREF(self->first, Py_NewRef(value));
       return 0;
   }

   static PyObject *
   Custom_getlast(PyObject *op, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       return Py_NewRef(self->last);
   }

   static int
   Custom_setlast(PyObject *op, PyObject *value, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       if (value == NULL) {
           PyErr_SetString(PyExc_TypeError, "Cannot delete the last attribute");
           return -1;
       }
       if (!PyUnicode_Check(value)) {
           PyErr_SetString(PyExc_TypeError,
                           "The last attribute value must be a string");
           return -1;
       }
       Py_SETREF(self->last, Py_NewRef(value));
       return 0;
   }

   static PyGetSetDef Custom_getsetters[] = {
       {"first", Custom_getfirst, Custom_setfirst,
        "first name", NULL},
       {"last", Custom_getlast, Custom_setlast,
        "last name", NULL},
       {NULL}  /* Sentinel */
   };

   static PyObject *
   Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
   {
       CustomObject *self = (CustomObject *) op;
       return PyUnicode_FromFormat("%S %S", self->first, self->last);
   }

   static PyMethodDef Custom_methods[] = {
       {"name", Custom_name, METH_NOARGS,
        "Return the name, combining the first and last name"
       },
       {NULL}  /* Sentinel */
   };

   static PyTypeObject CustomType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom3.Custom",
       .tp_doc = PyDoc_STR("Custom objects"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
       .tp_new = Custom_new,
       .tp_init = Custom_init,
       .tp_dealloc = Custom_dealloc,
       .tp_members = Custom_members,
       .tp_methods = Custom_methods,
       .tp_getset = Custom_getsetters,
   };

   static int
   custom_module_exec(PyObject *m)
   {
       if (PyType_Ready(&CustomType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot custom_module_slots[] = {
       {Py_mod_exec, custom_module_exec},
       {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
       {0, NULL}
   };

   static PyModuleDef custom_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "custom3",
       .m_doc = "Example module that creates an extension type.",
       .m_size = 0,
       .m_slots = custom_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_custom3(void)
   {
       return PyModuleDef_Init(&custom_module);
   }

Para oferecer um controle maior sobre os atributos "first" e "last",
usaremos funções personalizadas de acesso (getters) e modificação
(setters). A seguir estão as funções para obter e definir o atributo
"first":

   static PyObject *
   Custom_getfirst(PyObject *op, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       Py_INCREF(self->first);
       return self->first;
   }

   static int
   Custom_setfirst(PyObject *op, PyObject *value, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       PyObject *tmp;
       if (value == NULL) {
           PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
           return -1;
       }
       if (!PyUnicode_Check(value)) {
           PyErr_SetString(PyExc_TypeError,
                           "The first attribute value must be a string");
           return -1;
       }
       tmp = self->first;
       Py_INCREF(value);
       self->first = value;
       Py_DECREF(tmp);
       return 0;
   }

A função getter recebe um objeto "Custom" e um closure, que é um
ponteiro para void. Neste caso, o closure é ignorado. (O closure
oferece suporte a um modo de usar mais avançado, no qual dados de
definição são passados ao getter e ao setter. Isso pode, por exemplo,
permitir que um único conjunto de funções getter e setter decida qual
atributo obter ou definir com base nos dados presentes no closure.)

A função setter recebe o objeto "Custom", o novo valor e o closure. O
novo valor pode ser "NULL", caso em que o atributo está sendo
excluído. No nosso setter, levantamos um erro se o atributo for
excluído ou se o novo valor não for uma string.

Nós criamos um vetor de estruturas "PyGetSetDef":

   static PyGetSetDef Custom_getsetters[] = {
       {"first", Custom_getfirst, Custom_setfirst,
        "first name", NULL},
       {"last", Custom_getlast, Custom_setlast,
        "last name", NULL},
       {NULL}  /* Sentinel */
   };

e registra isso num slot "tp_getset":

   .tp_getset = Custom_getsetters,

A última entrada em uma estrutura "PyGetSetDef" é o “closure”
mencionado acima. Neste caso, não estamos usando um closure, então
simplesmente passamos "NULL".

Também removemos as definições de membros para esses atributos:

   static PyMemberDef Custom_members[] = {
       {"number", Py_T_INT, offsetof(CustomObject, number), 0,
        "custom number"},
       {NULL}  /* Sentinel */
   };

Também precisamos atualizar o manipulador "tp_init" para permitir
apenas strings [3] como valores passados:

   static int
   Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       CustomObject *self = (CustomObject *) op;
       static char *kwlist[] = {"first", "last", "number", NULL};
       PyObject *first = NULL, *last = NULL, *tmp;

       if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                        &first, &last,
                                        &self->number))
           return -1;

       if (first) {
           tmp = self->first;
           Py_INCREF(first);
           self->first = first;
           Py_DECREF(tmp);
       }
       if (last) {
           tmp = self->last;
           Py_INCREF(last);
           self->last = last;
           Py_DECREF(tmp);
       }
       return 0;
   }

Com essas alterações, podemos garantir que os membros "first" e "last"
nunca sejam "NULL", de modo que podemos remover quase todas as
verificações de valores "NULL". Isso significa que a maioria das
chamadas para "Py_XDECREF()" pode ser substituída por chamadas para
"Py_DECREF()". O único lugar em que não podemos substituir essas
chamadas é na implementação de "tp_dealloc", onde existe a
possibilidade de que a inicialização desses membros tenha falhado em
"tp_new".

Também renomeamos a função de inicialização do módulo e o nome do
módulo dentro da função de inicialização, como fizemos anteriormente,
e adicionamos uma definição extra ao arquivo "setup.py".


Apoiando a coleta de lixo cíclica
=================================

O Python possui um *coletor de lixo (GC) cíclico* que pode identificar
objetos que não são mais necessários mesmo quando suas contagens de
referências não são zero. Isso pode acontecer quando os objetos
participam de ciclos. Por exemplo, considere:

   >>> l = []
   >>> l.append(l)
   >>> del l

Neste exemplo, criamos uma lista que contém a si mesma. Quando a
apagamos, ela ainda possui uma referência apontando para si própria.
Sua contagem de referências não cai para zero. Felizmente, o coletor
de lixo cíclico do Python acabará percebendo que a lista é lixo e irá
liberá-la.

No segunda versão do exemplo de "Custom", permitimos que qualquer tipo
de objeto fosse armazenado nos atributos "first" ou "last" [4]. Além
disso, na segunda e na terceira versões, permitimos estender "Custom",
e subclasses podem adicionar atributos arbitrários. Por qualquer um
desses dois motivos, instâncias de "Custom" podem participar de
ciclos:

   >>> import custom3
   >>> class Derived(custom3.Custom): pass
   ...
   >>> n = Derived()
   >>> n.some_attribute = n

Para permitir que uma instância de "Custom" que participa de um ciclo
de referência seja corretamente detectada e coletada pelo coletor de
lixo cíclico, nosso tipo "Custom" precisa preencher dois slots
adicionais e ativar um sinalizador que habilita esses slots:

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>
   #include <stddef.h> /* for offsetof() */

   typedef struct {
       PyObject_HEAD
       PyObject *first; /* first name */
       PyObject *last;  /* last name */
       int number;
   } CustomObject;

   static int
   Custom_traverse(PyObject *op, visitproc visit, void *arg)
   {
       CustomObject *self = (CustomObject *) op;
       Py_VISIT(self->first);
       Py_VISIT(self->last);
       return 0;
   }

   static int
   Custom_clear(PyObject *op)
   {
       CustomObject *self = (CustomObject *) op;
       Py_CLEAR(self->first);
       Py_CLEAR(self->last);
       return 0;
   }

   static void
   Custom_dealloc(PyObject *op)
   {
       PyObject_GC_UnTrack(op);
       (void)Custom_clear(op);
       Py_TYPE(op)->tp_free(op);
   }

   static PyObject *
   Custom_new(PyTypeObject *type, PyObject *args, PyObject *kwds)
   {
       CustomObject *self;
       self = (CustomObject *) type->tp_alloc(type, 0);
       if (self != NULL) {
           self->first = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->first == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->last = Py_GetConstant(Py_CONSTANT_EMPTY_STR);
           if (self->last == NULL) {
               Py_DECREF(self);
               return NULL;
           }
           self->number = 0;
       }
       return (PyObject *) self;
   }

   static int
   Custom_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       CustomObject *self = (CustomObject *) op;
       static char *kwlist[] = {"first", "last", "number", NULL};
       PyObject *first = NULL, *last = NULL;

       if (!PyArg_ParseTupleAndKeywords(args, kwds, "|UUi", kwlist,
                                        &first, &last,
                                        &self->number))
           return -1;

       if (first) {
           Py_SETREF(self->first, Py_NewRef(first));
       }
       if (last) {
           Py_SETREF(self->last, Py_NewRef(last));
       }
       return 0;
   }

   static PyMemberDef Custom_members[] = {
       {"number", Py_T_INT, offsetof(CustomObject, number), 0,
        "custom number"},
       {NULL}  /* Sentinel */
   };

   static PyObject *
   Custom_getfirst(PyObject *op, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       return Py_NewRef(self->first);
   }

   static int
   Custom_setfirst(PyObject *op, PyObject *value, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       if (value == NULL) {
           PyErr_SetString(PyExc_TypeError, "Cannot delete the first attribute");
           return -1;
       }
       if (!PyUnicode_Check(value)) {
           PyErr_SetString(PyExc_TypeError,
                           "The first attribute value must be a string");
           return -1;
       }
       Py_XSETREF(self->first, Py_NewRef(value));
       return 0;
   }

   static PyObject *
   Custom_getlast(PyObject *op, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       return Py_NewRef(self->last);
   }

   static int
   Custom_setlast(PyObject *op, PyObject *value, void *closure)
   {
       CustomObject *self = (CustomObject *) op;
       if (value == NULL) {
           PyErr_SetString(PyExc_TypeError, "Cannot delete the last attribute");
           return -1;
       }
       if (!PyUnicode_Check(value)) {
           PyErr_SetString(PyExc_TypeError,
                           "The last attribute value must be a string");
           return -1;
       }
       Py_XSETREF(self->last, Py_NewRef(value));
       return 0;
   }

   static PyGetSetDef Custom_getsetters[] = {
       {"first", Custom_getfirst, Custom_setfirst,
        "first name", NULL},
       {"last", Custom_getlast, Custom_setlast,
        "last name", NULL},
       {NULL}  /* Sentinel */
   };

   static PyObject *
   Custom_name(PyObject *op, PyObject *Py_UNUSED(dummy))
   {
       CustomObject *self = (CustomObject *) op;
       return PyUnicode_FromFormat("%S %S", self->first, self->last);
   }

   static PyMethodDef Custom_methods[] = {
       {"name", Custom_name, METH_NOARGS,
        "Return the name, combining the first and last name"
       },
       {NULL}  /* Sentinel */
   };

   static PyTypeObject CustomType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "custom4.Custom",
       .tp_doc = PyDoc_STR("Custom objects"),
       .tp_basicsize = sizeof(CustomObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,
       .tp_new = Custom_new,
       .tp_init = Custom_init,
       .tp_dealloc = Custom_dealloc,
       .tp_traverse = Custom_traverse,
       .tp_clear = Custom_clear,
       .tp_members = Custom_members,
       .tp_methods = Custom_methods,
       .tp_getset = Custom_getsetters,
   };

   static int
   custom_module_exec(PyObject *m)
   {
       if (PyType_Ready(&CustomType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "Custom", (PyObject *) &CustomType) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot custom_module_slots[] = {
       {Py_mod_exec, custom_module_exec},
       {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
       {0, NULL}
   };

   static PyModuleDef custom_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "custom4",
       .m_doc = "Example module that creates an extension type.",
       .m_size = 0,
       .m_slots = custom_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_custom4(void)
   {
       return PyModuleDef_Init(&custom_module);
   }

Primeiro, o método de travessia informa ao coletor de lixo cíclico
quais subobjetos podem participar de ciclos:

   static int
   Custom_traverse(PyObject *op, visitproc visit, void *arg)
   {
       CustomObject *self = (CustomObject *) op;
       int vret;
       if (self->first) {
           vret = visit(self->first, arg);
           if (vret != 0)
               return vret;
       }
       if (self->last) {
           vret = visit(self->last, arg);
           if (vret != 0)
               return vret;
       }
       return 0;
   }

Para cada subobjeto que pode participar de ciclos, precisamos chamar a
função "visit()", que é passada para o método de travessia. A função
"visit()" recebe como argumentos o subobjeto e o argumento extra *arg*
fornecido ao método de travessia. Ela retorna um valor inteiro que
deve ser retornado se for diferente de zero.

O Python fornece o macro "Py_VISIT()", que automatiza as chamadas às
funções visit. Com "Py_VISIT()", podemos minimizar a quantidade de
boilerplate em "Custom_traverse":

   static int
   Custom_traverse(PyObject *op, visitproc visit, void *arg)
   {
       CustomObject *self = (CustomObject *) op;
       Py_VISIT(self->first);
       Py_VISIT(self->last);
       return 0;
   }

Nota:

  A implementação de "tp_traverse" deve nomear seus argumentos
  exatamente como *visit* e *arg* para que seja possível usar
  "Py_VISIT()".

Segundo, precisamos fornecer um método para limpar quaisquer
subobjetos que possam participar de ciclos:

   static int
   Custom_clear(PyObject *op)
   {
       CustomObject *self = (CustomObject *) op;
       Py_CLEAR(self->first);
       Py_CLEAR(self->last);
       return 0;
   }

Observe o uso do macro "Py_CLEAR()". Ele é a forma recomendada e
segura de limpar atributos de dados de tipos arbitrários enquanto
decrementa suas contagens de referências. Se você chamasse
"Py_XDECREF()" no atributo antes de defini-lo como "NULL", haveria a
possibilidade de que o destrutor do atributo chamasse novamente algum
código que lesse o atributo (especialmente se houver um ciclo de
referência).

Nota:

  Você poderia emular "Py_CLEAR()" ao escrever:

     PyObject *tmp;
     tmp = self->first;
     self->first = NULL;
     Py_XDECREF(tmp);

  Apesar disso, é muito mais fácil e menos propenso a erros, usar
  sempre "Py_CLEAR()" ao excluir um atributo. Não tente micro‐otimizar
  às custas da robustez!

O desalocador "Custom_dealloc" pode executar código arbitrário ao
limpar atributos. Isso significa que o GC pode ser acionado dentro da
função. Como o GC presume que a contagem de referências não é zero,
precisamos remover o objeto do rastreamento do GC chamando
"PyObject_GC_UnTrack()" antes de limpar os membros. A seguir está
nossa versão reimplementada do desalocador usando
"PyObject_GC_UnTrack()" e "Custom_clear":

   static void
   Custom_dealloc(PyObject *op)
   {
       PyObject_GC_UnTrack(op);
       (void)Custom_clear(op);
       Py_TYPE(op)->tp_free(op);
   }

Por fim, adicionamos o macro "Py_TPFLAGS_HAVE_GC" aos sinalizadores da
classe:

   .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE | Py_TPFLAGS_HAVE_GC,

Isso é praticamente tudo. Se tivéssemos escrito manipuladores
personalizados para "tp_alloc" ou "tp_free", precisaríamos adaptá-los
para a coleta de lixo cíclica. A maior parte das extensões usará as
versões fornecidas automaticamente.


Criando subclasses de outros tipos
==================================

É possível criar novos tipos de extensão derivados de tipos já
existentes. É mais fácil herdar dos tipos embutidos, já que uma
extensão pode usar diretamente o "PyTypeObject" de que precisa. Pode
ser difícil compartilhar essas estruturas "PyTypeObject" entre módulos
de extensão distintos.

Neste exemplo, criaremos um tipo "SubList" que herda do tipo embutido
"list". O novo tipo será totalmente compatível com listas comuns, mas
terá um método adicional, "increment()", que incrementa um contador
interno:

   >>> import sublist
   >>> s = sublist.SubList(range(3))
   >>> s.extend(s)
   >>> print(len(s))
   6
   >>> print(s.increment())
   1
   >>> print(s.increment())
   2

   #define PY_SSIZE_T_CLEAN
   #include <Python.h>

   typedef struct {
       PyListObject list;
       int state;
   } SubListObject;

   static PyObject *
   SubList_increment(PyObject *op, PyObject *Py_UNUSED(dummy))
   {
       SubListObject *self = (SubListObject *) op;
       self->state++;
       return PyLong_FromLong(self->state);
   }

   static PyMethodDef SubList_methods[] = {
       {"increment", SubList_increment, METH_NOARGS,
        PyDoc_STR("increment state counter")},
       {NULL},
   };

   static int
   SubList_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       SubListObject *self = (SubListObject *) op;
       if (PyList_Type.tp_init(op, args, kwds) < 0)
           return -1;
       self->state = 0;
       return 0;
   }

   static PyTypeObject SubListType = {
       .ob_base = PyVarObject_HEAD_INIT(NULL, 0)
       .tp_name = "sublist.SubList",
       .tp_doc = PyDoc_STR("SubList objects"),
       .tp_basicsize = sizeof(SubListObject),
       .tp_itemsize = 0,
       .tp_flags = Py_TPFLAGS_DEFAULT | Py_TPFLAGS_BASETYPE,
       .tp_init = SubList_init,
       .tp_methods = SubList_methods,
   };

   static int
   sublist_module_exec(PyObject *m)
   {
       SubListType.tp_base = &PyList_Type;
       if (PyType_Ready(&SubListType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "SubList", (PyObject *) &SubListType) < 0) {
           return -1;
       }

       return 0;
   }

   static PyModuleDef_Slot sublist_module_slots[] = {
       {Py_mod_exec, sublist_module_exec},
       {Py_mod_multiple_interpreters, Py_MOD_MULTIPLE_INTERPRETERS_NOT_SUPPORTED},
       {0, NULL}
   };

   static PyModuleDef sublist_module = {
       .m_base = PyModuleDef_HEAD_INIT,
       .m_name = "sublist",
       .m_doc = "Example module that creates an extension type.",
       .m_size = 0,
       .m_slots = sublist_module_slots,
   };

   PyMODINIT_FUNC
   PyInit_sublist(void)
   {
       return PyModuleDef_Init(&sublist_module);
   }

Como você pode consultar, o código-fonte se assemelha bastante aos
exemplos de "Custom" das seções anteriores. Vamos detalhar as
principais diferenças entre eles.

   typedef struct {
       PyListObject list;
       int state;
   } SubListObject;

A diferença principal para objetos de tipos derivados é que a
estrutura de objeto do tipo base deve ser o primeiro valor. O tipo
base já inclui o "PyObject_HEAD()" no início de sua própria estrutura.

Quando um objeto Python é uma instância de "SubList", seu ponteiro
"PyObject *" pode ser convertido com segurança tanto para
"PyListObject *" quanto para "SubListObject *":

   static int
   SubList_init(PyObject *op, PyObject *args, PyObject *kwds)
   {
       SubListObject *self = (SubListObject *) op;
       if (PyList_Type.tp_init(op, args, kwds) < 0)
           return -1;
       self->state = 0;
       return 0;
   }

Vemos acima como chamar o método "__init__()" do tipo base.

Esse padrão é importante ao escrever um tipo que possui membros
personalizados em "tp_new" e "tp_dealloc". O manipulador "tp_new" não
deve realmente criar a memória do objeto usando o seu próprio
"tp_alloc"; em vez disso, deve permitir que a classe base faça isso,
chamando o seu próprio "tp_new".

A estrutura "PyTypeObject" provê o campo "tp_base", que especifica a
classe base concreta do tipo. Devido a problemas de compilação
multiplataforma, não se deve preencher esse campo diretamente com uma
referência para "PyList_Type"; isso deve ser feito dentro da função
"Py_mod_exec":

   static int
   sublist_module_exec(PyObject *m)
   {
       SubListType.tp_base = &PyList_Type;
       if (PyType_Ready(&SubListType) < 0) {
           return -1;
       }

       if (PyModule_AddObjectRef(m, "SubList", (PyObject *) &SubListType) < 0) {
           return -1;
       }

       return 0;
   }

Before calling "PyType_Ready()", the type structure must have the
"tp_base" slot filled in.  When we are deriving an existing type, it
is not necessary to fill out the "tp_alloc" slot with
"PyType_GenericAlloc()" -- the allocation function from the base type
will be inherited.

Depois disso, chamar "PyType_Ready()" e adicionar o objeto de tipo ao
módulo é o mesmo processo usado nos exemplos básicos com "Custom".

-[ Notas de rodapé ]-

[1] Isso é verdade quando sabemos que o objeto é um tipo básico, como
    uma string ou um float.

[2] Confiamos nisso no manipulador "tp_dealloc" neste exemplo, porque
    o nosso tipo não oferece suporte à coleta de lixo.

[3] Agora sabemos que o primeiro e último membros são strings, então
    talvez pudéssemos ter menos cuidado com a diminuição de suas
    contagens de referência, no entanto, aceitamos instâncias de
    subclasses de string. Mesmo que a desalocação de strings normais
    não retorne aos nossos objetos, não podemos garantir que a
    desalocação de uma instância de uma subclasse de cadeias de
    caracteres não retornará aos nossos objetos.

[4] Além disso, mesmo com nossos atributos restritos a instâncias de
    strings, o usuário poderia passar arbitrariamente subclasses "str"
    e, portanto, ainda criar ciclos de referência.
