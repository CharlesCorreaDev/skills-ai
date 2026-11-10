FAQ sobre Extensão/Incorporação
*******************************


Posso criar minhas próprias funções em C?
=========================================

Sim, você pode construir módulos embutidos contendo funções,
variáveis, exceções e até mesmo novos tipos em C. Isso é explicado no
documento Estendendo e incorporando o interpretador Python.

A maioria dos livros intermediários ou avançados em Python também
abordará esse tópico.


Posso criar minhas próprias funções em C++?
===========================================

Sim, usando recursos de compatibilidade encontrados em C++. Coloque
"extern "C" { ... }" em torno dos arquivos de inclusão do Python e
coloque "extern "C"" antes de cada função que será chamada pelo
interpretador do Python. Objetos globais ou estáticos em C++ com
construtores provavelmente não são uma boa ideia.


Escrever C é difícil; há alguma alternativa?
============================================

Há diversas alternativas para escrever suas próprias extensões C,
dependendo do que você está tentando fazer. Ferramentas recomendadas
de terceiros oferecem abordagens mais simples e mais sofisticadas para
criar extensões C e C++ para Python.


Como posso executar instruções arbitrárias de Python a partir de C?
===================================================================

A função mais alto-nível para isso é a "PyRun_SimpleString()", que
recebe como único argumento uma string a ser executada no contexto do
módulo "__main__" e retorna "0" para sucesso e "-1" quando uma exceção
ocorrer (incluindo "SyntaxError").  Se quiser mais controle, use
"PyRun_String()"; veja o código-fonte de "PyRun_SimpleString()" em
"Python/pythonrun.c".


Como posso executar e obter o resultado de uma expressão Python arbitrária a partir de C?
=========================================================================================

Chame a função "PyRun_String()" da pergunta anterior passando
"Py_eval_input" como o símbolo de início; ela faz a análise sintática
de uma expressão, a executa, e retorna o seu valor.


Como extraio valores em C a partir de um objeto Python?
=======================================================

Depende do tipo do objeto.  Se for uma tupla, a "PyTuple_Size()"
retorna o seu comprimento e a "PyTuple_GetItem()" retorna o item em um
determinado índice.  Listas têm funções similares, "PyList_Size()" e
"PyList_GetItem()".

Para bytes, a "PyBytes_Size()" retorna o comprimento e a
"PyBytes_AsStringAndSize()" fornece um ponteiro para o seu valor e o
seu comprimento. Note que objetos bytes em Python podem conter bytes
nulos, de forma que a "strlen()" do C não deve ser usada.

Para testar o tipo de um objeto, primeiramente se certifique de que
ele não é "NULL", e então use "PyBytes_Check()", "PyTuple_Check()",
"PyList_Check()", etc.

Também existe uma API alto-nível para objetos Python fornecida pela
chamada interface "abstrata" -- leia "Include/abstract.h" para mais
detalhes.  Ela permite interagir com qualquer tipo de sequência Python
usando chamadas como "PySequence_Length()", "PySequence_GetItem()",
etc, além de vários outros protocolos úteis tais como números
("PyNumber_Index()" e outros) e mapeamentos nas APIs PyMapping.


Como posso utilizar Py_BuildValue() para criar uma tupla de comprimento arbitrário?
===================================================================================

Não é possível. Use a função "PyTuple_Pack()" para isso.


Como eu chamo um método de um objeto a partir do C?
===================================================

A função "PyObject_CallMethod()" pode ser usada para chamar um método
arbitrário de um objeto.  Os parâmetros são o objeto, o nome do método
a ser chamado, uma string de formato como a usada em
"Py_BuildValue()", e os valores dos argumentos:

   PyObject *
   PyObject_CallMethod(PyObject *object, const char *method_name,
                       const char *arg_format, ...);

Isso funciona para qualquer objeto que tenha métodos -- sejam eles
embutidos ou definidos por usuário. Você fica então responsável por
chamar "Py_DECREF()" no valor de retorno.

Para chamar, por exemplo, o método "seek" de um objeto arquivo com
argumentos 10, 0 (presumindo que "f" é o ponteiro para o objeto
arquivo):

   res = PyObject_CallMethod(f, "seek", "(ii)", 10, 0);
   if (res == NULL) {
           ... ocorreu uma exceção ...
   }
   else {
           Py_DECREF(res);
   }

Note que a função "PyObject_CallObject()" *sempre* recebe os
argumentos da chamada como uma tupla, de forma que para chamar uma
função sem argumentos deve-se passar "()" como formato, e para chamar
uma função com 1 argumento, coloque-o entre parênteses, por exemplo
"(i)".


Como posso capturar a saída da função PyErr_Print() (ou qualquer outra coisa que escreva para stdout/stderr)?
=============================================================================================================

Com código Python, defina um objeto que suporte o método "write()".
Atribua esse objeto a "sys.stdout" e "sys.stderr". Chame print_error,
or simplesmente deixe o mecanismo padrão de traceback acontecer.
Assim, a saída irá para onde quer que o seu método "write()" a envie.

O jeito mais fácil de fazer isso é usar a classe "io.StringIO":

   >>> import io, sys
   >>> sys.stdout = io.StringIO()
   >>> print('foo')
   >>> print('hello world!')
   >>> sys.stderr.write(sys.stdout.getvalue())
   foo
   hello world!

Um objeto personalizado para fazer a mesma coisa seria esse:

   >>> import io, sys
   >>> class StdoutCatcher(io.TextIOBase):
   ...     def __init__(self):
   ...         self.data = []
   ...     def write(self, stuff):
   ...         self.data.append(stuff)
   ...
   >>> import sys
   >>> sys.stdout = StdoutCatcher()
   >>> print('foo')
   >>> print('hello world!')
   >>> sys.stderr.write(''.join(sys.stdout.data))
   foo
   hello world!


Como faço para acessar a partir do C um módulo escrito em Python?
=================================================================

Você pode obter um pointeiro para o objeto de módulo da seguinte
maneira:

   module = PyImport_ImportModule("<modulename>");

Se o módulo ainda não foi importado (isto é, ainda não aparece no
"sys.modules"), essa função vai inicializar o módulo; caso contrário,
ela vai simplesmente retornar o valor de
"sys.modules["<modulename>"]".  Note que ela não adiciona o módulo a
nenhum espaço de nomes -- ela simplesmente garante que ele foi
inicializado e colocado no "sys.modules".

Você pode então acessar os atributos do módulo (isto é, qualquer nome
definido no módulo) assim:

   attr = PyObject_GetAttrString(module, "<attrname>");

Chamar "PyObject_SetAttrString()" para definir variáveis no módulo
também funciona.


Como posso interagir com objetos C++ a partir do Python?
========================================================

Dependendo das suas necessidades, há diversas abordagens.  Para fazer
isso manualmente, comece lendo o documento "Estendendo e
Incorporando".  Note que, para o sistema Python em tempo de execução,
não há muita diferença entre C e C++ -- de forma que a estratégia de
construir um novo tipo Python ao redor de uma estrutura C (ou ponteiro
para uma) também funciona para objetos C++.

Para bibliotecas C++, veja Escrever C é difícil; há alguma
alternativa?.


Adicionei um módulo usando o arquivo de Setup e o make falha; por quê?
======================================================================

O Setup deve terminar com uma quebra de linha; se não houver uma
quebra de linha no final, o processo de compilação falha.  (Consertar
isso requer umas gambiarras feias em shell script, e esse bug é tão
pequeno que o esforço não parece valer a pena.)


Como eu depuro uma extensão?
============================

Ao usar o GDB com extensões carregadas dinamicamente, você não
consegue definir um ponto de interrupção antes da sua extensão ser
carregada.

No seu arquivo ".gdbinit" (ou então interativamente), adicione o
comando:

   br _PyImport_LoadDynamicModule

Então, ao executar o GDB:

   $ gdb /local/bin/python
   gdb) run myscript.py
   gdb) continue # repita até que a sua extensão seja carregada
   gdb) finish   # para que a sua extensão seja carregada
   gdb) br myfunction.c:50
   gdb) continue


Quero compilar um módulo Python no meu sistema Linux, mas alguns arquivos estão faltando. Por quê?
==================================================================================================

A maioria das versões empacotadas de Python omitem alguns arquivos
necessários para compilar extensões do Python.

Em sistemas Red Hat, instale o RPM python3-devel para obter os
arquivos necessários.

Para Debian, execute "apt-get install python3-dev".


Como posso distinguir "entrada incompleta" de "entrada inválida"?
=================================================================

Às vezes você quer emular o comportamento do interpretador interativo
do Python, que te dá um prompt de continuação quando a entrada está
incompleta (por exemplo, você digitou o início de uma instrução "if",
ou então não fechou os parênteses ou aspas triplas), mas que te dá um
mensagem de erro de sintaxe imediatamente se a entrada for inválida.

Em Python você pode usar o módulo "codeop", que aproxima
suficientemente o comportamento do analisador sintático.  Por exemplo,
o IDLE o usa.

Em C, a forma mais fácil de fazer isso é chamar
"PyRun_InteractiveLoop()" (talvez em uma thread separada) e deixar o
interpretador do Python tratar a entrada para você. Você também pode
apontar o "PyOS_ReadlineFunctionPointer()" para a sua função de
entrada personalizada. Consulte "Modules/readline.c" e
"Parser/myreadline.c" para mais dicas.


Como encontro os símbolos __builtin_new ou __pure_virtual não-definidos no g++?
===============================================================================

Para carregar dinamicamente módulos de extensão feitos com g++, você
precisa recompilar o Python, usando o g++ como ligador (mude a
constante LINKCC no Makefile dos módulos de extensão do Python), e use
o g++ também como ligador do seu módulo (por exemplo, "g++ -shared -o
mymodule.so mymodule.o").


Posso criar uma classe de objetos com alguns métodos implementados em C e outros em Python (por exemplo, via herança)?
======================================================================================================================

Sim, você pode herdar de classes embutidas como "int", "list", "dict"
etc.

A Boost Python Library (BPL,
https://www.boost.org/libs/python/doc/index.html) fornece uma forma de
fazer isso a partir do C++ (quer dizer, você consegue herdar de uma
classe de extensão escrita em C++ usando a BPL).
