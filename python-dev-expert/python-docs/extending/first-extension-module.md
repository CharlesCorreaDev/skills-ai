Seu primeiro módulo de extensão da API C
****************************************

Este tutorial guiará você pela criação de um módulo de extensão
simples para Python, escrito em C ou C++.

Utilizaremos diretamente a API C do Python de baixo nível. Para formas
mais simples de criar módulos de extensão, consulte as ferramentas de
terceiros recomendadas.

O tutorial pressupõe conhecimentos básicos de Python: você deve ser
capaz de definir funções em código Python antes de começar a
escrevê-las em C. Consulte O tutorial do Python para uma introdução ao
próprio Python.

O tutorial deve ser acessível a qualquer pessoa capaz de escrever uma
biblioteca básica em C. Embora mencionemos vários conceitos que não se
espera que um iniciante em C conheça — como funções *static* ou
declarações de vinculação (*linkage*) —, compreendê-los não é
necessário para obter êxito.

Nosso foco será proporcionar a você uma noção de como é a API C do
Python. Isso não ensinará conceitos importantes, como tratamento de
erros e contagem de referências, que são abordados em capítulos
posteriores.

Vamos supor que você utilize um sistema do tipo Unix (incluindo macOS
e Linux) ou Windows. Em outros sistemas, talvez seja necessário
ajustar alguns detalhes — por exemplo, o nome de um comando do
sistema.

Você precisa ter um compilador C adequado e os cabeçalhos de
desenvolvimento do Python instalados. No Linux, esses cabeçalhos
geralmente estão em um pacote como "python3-dev" ou "python3-devel".

Você precisa ser capaz de instalar pacotes Python. Este tutorial
utiliza o *pip <https://pip.pypa.io/>`__* ("pip install"), mas você
pode substituí-lo por qualquer ferramenta capaz de realizar a
construção e a instalação de projetos baseados em "pyproject.toml",
como uv ("uv setup.py install"). De preferência, mantenha um ambiente
virtual ativado.

Nota:

  Este tutorial utiliza APIs que foram adicionadas no CPython 3.15.
  Para criar uma extensão compatível com versões anteriores do
  CPython, consulte uma versão anterior desta documentação.Este
  tutorial utiliza sintaxe de C introduzida no C11 e no C++20. Se a
  sua extensão precisar ser compatível com padrões anteriores,
  consulte os tutoriais na documentação para o Python 3.14 ou versões
  anteriores.


O que faremos
=============

Vamos criar um módulo de extensão chamado "spam" [1], que incluirá uma
interface Python para a função "system()" da biblioteca padrão C. Essa
função é definida em "stdlib.h". Ela recebe uma string C como
argumento, executa o argumento como um comando do sistema e retorna um
valor de resultado como um inteiro. Uma página de manual para
"system()" poderia resumi-la da seguinte forma:

   #include <stdlib.h>
   int system(const char *command);

Observe que, assim como muitas funções da biblioteca padrão da
linguagem C, esta função já está disponível no Python. Em ambientes de
produção, utilize "os.system()" ou "subprocess.run()" em vez do módulo
que você escreverá aqui.

Queremos que esta função seja chamável a partir do Python da seguinte
forma:

   >>> import spam
   >>> status = spam.system("whoami")
   Nome do usuário
   >>> status
   0

Nota:

  O comando de sistema *whoami* exibe o seu nome de usuário. Ele é
  útil em tutoriais como este porque possui o mesmo nome tanto no Unix
  quanto no Windows.


Comece com os cabeçalhos
========================

Comece criando um diretório para este tutorial e acessando-o na linha
de comando. Em seguida, crie um arquivo chamado "spammodule.c" no seu
diretório. [2]

Neste arquivo, incluiremos dois cabeçalhos: "Python.h", para importar
todas as declarações da API C do Python, e "stdlib.h", para a função
"system()". [3]

Adicione as seguintes linhas a "spammodule.c":

   #include <Python.h>
   #include <stdlib.h>     // para system()

Certifique-se de colocar "stdlib.h" — e quaisquer outras inclusões à
biblioteca padrão — *após* "Python.h". Em alguns sistemas, o Python
pode definir diretivas de pré-processador que afetam os cabeçalhos
padrão.


Executando sua ferramenta de construção
=======================================

Com apenas as diretivas de inclusões (includes) implementadas, sua
extensão não fará nada. Ainda assim, é um bom momento para compilá-la
e tentar importá-la. Isso garantirá que sua ferramenta de construção
esteja funcionando, permitindo que você faça e teste alterações
incrementais à medida que acompanha o restante do texto.

O próprio CPython não inclui uma ferramenta para construir módulos de
extensão; recomenda-se utilizar um projeto de terceiros para essa
finalidade. Neste tutorial, utilizaremos o meson-python. (Caso queira
utilizar outra ferramenta, consulte Appendix: Other build tools.)

O "meson-python" requer a definição de um "projeto" utilizando dois
arquivos extras.

Primeiro, adicione um arquivo "pyproject.toml" com o seguinte
conteúdo:

   [build-system]
   build-backend = 'mesonpy'
   requires = ['meson-python']

   [project]
   # Placeholders de informações de projeto
   # (altere isso antes de distribuir o módulo)
   name = 'projetoexemplo'
   version = '0'

Então, cria "meson.build" contendo o seguinte:

   project('projetoexemplo', 'c')

   py = import('python').find_installation(pure: false)

   py.extension_module(
      'spam',          # nome do módulo Python importável
      'spammodule.c',  # o arquivo-fonte C
      install: true,
   )

Nota:

  Consulte a documentação do meson-python para detalhes sobre a
  configuração.

Agora, construa e instale o *projeto no diretório atual* (".") via
"pip":

   python -m pip -v install .

A opção "-v" ("--verbose") faz com que o "pip" mostre a saída do
compilador, o que é frequentemente útil durante o desenvolvimento.

Dica:

  Se você não tiver o "pip" instalado, execute "python -m ensurepip",
  de preferência em um ambiente virtual. (Ou, se preferir outra
  ferramenta capaz de construir e instalar projetos baseados em
  "pyproject.toml", utilize-a.)

Observe que precisará de executar este comando novamente sempre que
alterar a sua extensão. Ao contrário do Python, o C tem um passo de
compilação explícito.

Quando a sua extensão estiver compilada e instalada, inicie o Python e
tente importá-la. Isto deverá falhar com a seguinte exceção:

   >>> import spam
   Traceback (most recent call last):
      ...
   ImportError: dynamic module does not define module export function (PyModExport_spam or PyInit_spam)


Gancho de exportação de módulo
==============================

A exceção que você recebeu ao tentar importar o módulo indicava que o
Python está procurando uma "função de exportação de módulo", também
conhecida como gancho de exportação de módulo. Vamos definir uma.

Primeiro, adicione um protótipo embaixo das linhas "#include":


   PyMODEXPORT_FUNC PyModExport_spam(void);


Dica:

  O protótipo não é estritamente necessário, mas alguns compiladores
  modernos emitem avisos se ele não estiver presente. Geralmente, é
  melhor adicionar o protótipo do que desativar o aviso.

A macro "PyMODEXPORT_FUNC" declara o tipo de retorno da função e
adiciona quaisquer declarações de vinculação especiais necessárias
para tornar a função visível e utilizável quando o CPython a carrega.

Após o protótipo, adicione a função em si. Por enquanto, faça com que
ela retorne "NULL":

   PyMODEXPORT_FUNC
   PyModExport_spam(void)
   {
      return NULL;
   }

Compile e carregue o módulo novamente. Você deverá receber um erro
diferente desta vez.

   >>> import spam
   Traceback (most recent call last):
      ...
   SystemError: module export hook for module 'spam' failed without setting an exception

Simplesmente retornar "NULL" *não* é o comportamento correto para um
gancho de exportação, e o CPython reclama disso. Isso é bom —
significa que o CPython encontrou a função! Agora, vamos fazer com que
ela realize alguma tarefa útil.


A tabela de slots
=================

Em vez de "NULL", o gancho de exportação deve retornar as informações
necessárias para criar um módulo. Vamos começar pelo básico: o nome e
a docstring.

As informações devem ser definidas em um vetor de entradas "PySlot",
que são essencialmente pares chave-valor. Defina esse array logo antes
do seu gancho de exportação:

   PyABIInfo_VAR(abi_info);

   static PySlot spam_slots[] = {
      PySlot_STATIC_DATA(Py_mod_abi, &abi_info),
      PySlot_STATIC_DATA(Py_mod_name, "spam"),
      PySlot_STATIC_DATA(Py_mod_doc, "Um módulo maravilhoso com um exemplo de função"),
      PySlot_END
   };

A macro "PySlot_STATIC_DATA" é usada quando o valor do slot (aqui:
"&abi_info", ""spam"" e a docstring) é um ponteiro para dados
constantes alocados estaticamente.

A macro "PyABIInfo_VAR(abi_info);" e o slot "Py_mod_abi" constituem um
código padrão que ajuda a evitar que extensões compiladas para uma
versão diferente do Python causem a falha do interpretador.

Para ambos "Py_mod_name" e "Py_mod_doc", os valores são strings C —
isto é, vetores de bytes terminados em NUL e codificados em UTF-8.

Observe a entrada sentinela "PySlot_END" ao final. Ela marca o fim do
vetor. Se você esquecê-la, provocará um comportamento indefinido.

The array is defined as "static" -- that is, not visible outside this
".c" file. This will be a common theme. CPython only needs to access
the export hook; all global variables and all other functions should
generally be "static", so that they don't clash with other extensions.

Return this array from your export hook instead of "NULL":

   PyMODEXPORT_FUNC
   PyModExport_spam(void)
   {
      return spam_slots;
   }

Now, recompile and try it out:

   >>> import spam
   >>> print(spam)
   <module 'spam' from '/home/encukou/dev/cpython/spam.so'>

You have an extension module! Try "help(spam)" to see the docstring.

The next step will be adding a function.


Exposing a function
===================

To expose the "system()" C function directly to Python, we'll need to
write a layer of glue code to convert arguments from Python objects to
C values, and the C return value back to Python.

One of the simplest ways to write glue code is a ""METH_O"" function,
which takes two Python objects and returns one. All Python objects --
regardless of the Python type -- are represented in C as pointers to
the "PyObject" structure.

Add such a function above the slots array:

   static PyObject *
   spam_system(PyObject *self, PyObject *arg)
   {
      Py_RETURN_NONE;
   }

For now, we ignore the arguments, and use the "Py_RETURN_NONE" macro,
which expands to a "return" statement that properly returns a Python
"None" object.

Recompile your extension to make sure you don't have syntax errors. We
haven't yet added "spam_system" to the module, so you might get a
warning that "spam_system" is unused.


Method definitions
------------------

To expose the C function to Python, you will need to provide several
pieces of information in a structure called "PyMethodDef" [4]:

* "ml_name": the name of the Python function;

* "ml_doc": a docstring;

* "ml_meth": the C function to be called; and

* "ml_flags": a set of flags describing details like how Python
  arguments are passed to the C function. We'll use "METH_O" here --
  the flag that matches our "spam_system" function's signature.

Because modules typically create several functions, these definitions
need to be collected in an array, with a zero-filled sentinel at the
end. Add this array just below the "spam_system" function:


   static PyMethodDef spam_methods[] = {
       {
           .ml_name="system",
           .ml_meth=spam_system,
           .ml_flags=METH_O,
           .ml_doc="Execute a shell command.",
       },
       {NULL, NULL, 0, NULL}        /* Sentinel */
   };


As with module slots, a zero-filled sentinel marks the end of the
array.

Next, we'll add the method to the module. Add a "Py_mod_methods" slot
to your "PySlot" array:


   PyABIInfo_VAR(abi_info);

   static PySlot spam_slots[] = {
       PySlot_STATIC_DATA(Py_mod_abi, &abi_info),
       PySlot_STATIC_DATA(Py_mod_name, "spam"),
       PySlot_STATIC_DATA(Py_mod_doc, "A wonderful module with an example function"),
       PySlot_STATIC_DATA(Py_mod_methods, spam_methods),
       PySlot_END
   };


Recompile your extension again, and test it. Be sure to restart the
Python interpreter, so that "import spam" picks up the new version of
the module.

You should now be able to call the function:

   >>> import spam
   >>> print(spam.system)
   <built-in function system>
   >>> print(spam.system('whoami'))
   None

Note that our "spam.system" does not yet run the "whoami" command; it
only returns "None".

Check that the function accepts exactly one argument, as specified by
the "METH_O" flag:

   >>> print(spam.system('too', 'many', 'arguments'))
   Traceback (most recent call last):
      ...
   TypeError: spam.system() takes exactly one argument (3 given)


Returning an integer
====================

Now, let's take a look at the return value. Instead of "None", we'll
want "spam.system" to return a number -- that is, a Python "int"
object. Eventually this will be the exit code of a system command, but
let's start with a fixed value, say, "3".

The Python C API provides a function to create a Python "int" object
from a C "int" value: "PyLong_FromLong()". [5]

To call it, replace the "Py_RETURN_NONE" with the following 3 lines:

   static PyObject *
   spam_system(PyObject *self, PyObject *arg)
   {
      int status = 3;
      PyObject *result = PyLong_FromLong(status);
      return result;
   }

Recompile, restart the Python interpreter again, and check that the
function now returns 3:

   >>> import spam
   >>> spam.system('whoami')
   3


Accepting a string
==================

Finally, let's handle the function argument.

Our C function, "spam_system()", takes two arguments. The first one,
"PyObject *self", will be set to the "spam" module object. This isn't
useful in our case, so we'll ignore it.

The other one, "PyObject *arg", will be set to the object that the
user passed from Python. We expect that it should be a Python string.
In order to use the information in it, we will need to convert it to a
C value -- in this case, a C string ("const char *").

There's a slight type mismatch here: Python's "str" objects store
Unicode text, but C strings are arrays of bytes. So, we'll need to
*encode* the data, and we'll use the UTF-8 encoding for it. (UTF-8
might not always be correct for system commands, but it's what
"str.encode()" uses by default, and the C API has special support for
it.)

The function to encode a Python string into a UTF-8 buffer is named
"PyUnicode_AsUTF8AndSize()" [6]. Call it like this:

   static PyObject *
   spam_system(PyObject *self, PyObject *arg)
   {
      const char *command = PyUnicode_AsUTF8AndSize(arg, NULL);
      int status = 3;
      PyObject *result = PyLong_FromLong(status);
      return result;
   }

If "PyUnicode_AsUTF8AndSize()" is successful, *command* will point to
the resulting C string -- a zero-terminated array of bytes [7]. This
buffer is managed by the *arg* object, which means we don't need to
free it, but we must follow some rules:

* We should only use the buffer inside the "spam_system" function.
  After "spam_system" returns, *arg* and the buffer it manages might
  be garbage-collected.

* We must not modify it. This is why we use "const".

If "PyUnicode_AsUTF8AndSize()" was *not* successful, it returns a
"NULL" pointer. When calling *any* Python C API, we always need to
handle such error cases. The way to do this in general is left for
later chapters of this documentation. For now, be assured that we are
already handling errors from "PyLong_FromLong()" correctly.

For the "PyUnicode_AsUTF8AndSize()" call, the correct way to handle
errors is returning "NULL" from "spam_system". Add an "if" block for
this:

   static PyObject *
   spam_system(PyObject *self, PyObject *arg)
   {
      const char *command = PyUnicode_AsUTF8AndSize(arg, NULL);
      if (command == NULL) {
         return NULL;
      }
      int status = 3;
      PyObject *result = PyLong_FromLong(status);
      return result;
   }

To test that error handling works, compile again, restart Python so
that "import spam" picks up the new version of your module, and try
passing a non-string value to your function:

   >>> import spam
   >>> spam.system(3)
   Traceback (most recent call last):
      ...
   TypeError: bad argument type for built-in operation

Now, all that is left is calling the C library function "system()"
with the "char *" buffer, and using its result instead of the "3":

   static PyObject *
   spam_system(PyObject *self, PyObject *arg)
   {
      const char *command = PyUnicode_AsUTF8AndSize(arg, NULL);
      if (command == NULL) {
         return NULL;
      }
      int status = system(command);
      PyObject *result = PyLong_FromLong(status);
      return result;
   }

Compile your module, restart Python, and test. This time, you should
see your username -- the output of the "whoami" system command:

   >>> import spam
   >>> result = spam.system('whoami')
   User Name
   >>> result
   0

You can also test with other commands, like "ls", "dir", or one that
doesn't exist:

   >>> import spam
   >>> result = spam.system('nonexistent-command')
   sh: line 1: nonexistent-command: command not found
   >>> result
   32512


The result
==========

Congratulations! You have written a complete Python C API extension
module, and completed this tutorial!

Here is the entire source file, for your convenience:

   /// Includes

   #include <Python.h>
   #include <stdlib.h>     // for system()

   /// Implementation of spam.system

   static PyObject *
   spam_system(PyObject *self, PyObject *arg)
   {
      const char *command = PyUnicode_AsUTF8AndSize(arg, NULL);
      if (command == NULL) {
         return NULL;
      }
      int status = system(command);
      PyObject *result = PyLong_FromLong(status);
      return result;
   }

   /// Module method table

   static PyMethodDef spam_methods[] = {
       {
           .ml_name="system",
           .ml_meth=spam_system,
           .ml_flags=METH_O,
           .ml_doc="Execute a shell command.",
       },
       {NULL, NULL, 0, NULL}        /* Sentinel */
   };

   /// Module slot table

   PyABIInfo_VAR(abi_info);

   static PySlot spam_slots[] = {
       PySlot_STATIC_DATA(Py_mod_abi, &abi_info),
       PySlot_STATIC_DATA(Py_mod_name, "spam"),
       PySlot_STATIC_DATA(Py_mod_doc, "A wonderful module with an example function"),
       PySlot_STATIC_DATA(Py_mod_methods, spam_methods),
       PySlot_END
   };

   /// Export hook prototype

   PyMODEXPORT_FUNC PyModExport_spam(void);

   /// Module export hook

   PyMODEXPORT_FUNC
   PyModExport_spam(void)
   {
      return spam_slots;
   }


Appendix: Other build tools
===========================

You should be able to follow this tutorial -- except the *Running your
build tool* section itself -- with a build tool other than "meson-
python".

The Python Packaging User Guide has a list of recommended tools; be
sure to choose one for the C language.


Workaround for missing PyInit function
--------------------------------------

If your build tool output complains about missing "PyInit_spam", add
the following function to your module for now:

   // A workaround
   void *PyInit_spam(void) { return NULL; }

This is a shim for an old-style initialization function, which was
required in extension modules for CPython 3.14 and below. Current
CPython does not need it, but some build tools may still assume that
all extension modules need to define it.

If you use this workaround, you will get the exception "SystemError:
initialization of spam failed without raising an exception" instead of
"ImportError: dynamic module does not define module export function".


Compiling directly
------------------

Using a third-party build tool is heavily recommended, as it will take
care of various details of your platform and Python installation, of
naming the resulting extension, and, later, of distributing your work.

If you are building an extension for as *specific* system, or for
yourself only, you might instead want to run your compiler directly.
The way to do this is system-specific; be prepared for issues you will
need to solve yourself.


Linux
~~~~~

On Linux, the Python development package may include a
"python3-config" command that prints out the required compiler flags.
If you use it, check that it corresponds to the CPython interpreter
you'll use to load the module. Then, start with the following command:

   gcc --shared $(python3-config --cflags --ldflags) spammodule.c -o spam.so

This should generate a "spam.so" file that you need to put in a
directory on "sys.path".

-[ Notas de rodapé ]-

[1] "spam" is the favorite food of Monty Python fans...

[2] The source file name is entirely up to you, though some tools can
    be picky about the ".c" extension. This tutorial uses the
    traditional "*module.c" suffix. Some people would just use
    "spam.c" to implement a module named "spam", projects where Python
    isn't the primary language might use "py_spam.c", and so on.

[3] Including "stdlib.h" is technically not necessary, since
    "Python.h" includes it and several other standard headers for its
    own use or for backwards compatibility. However, it is good
    practice to explicitly include what you need.

[4] The "PyMethodDef" structure is also used to create methods of
    classes, so there's no separate ""PyFunctionDef"".

[5] The name "PyLong_FromLong()" might not seem obvious. "PyLong"
    refers to a the Python "int", which was originally called "long";
    the "FromLong" refers to the C "long" (or "long int") type.

[6] Here, "PyUnicode" refers to the original name of the Python "str"
    class: "unicode".

    The "AndSize" part of the name refers to the fact that this
    function can also retrieve the size of the buffer, using an output
    argument. We don't need this, so we set the second argument to
    NULL.

[7] We're ignoring the fact that Python strings can also contain NUL
    bytes, which terminate a C string. In other words, our function
    will treat "spam.system("foo\0bar")" as "spam.system("foo")". This
    possibility can lead to security issues, so the real "os.system"
    function size checks for this case and raises an error.
