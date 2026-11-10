"annotationlib" --- Funcionalidade para introspecção de anotações
*****************************************************************

Adicionado na versão 3.14.

**Código-fonte:** Lib/annotationlib.py

======================================================================

O módulo "annotationlib" fornece ferramentas para introspecção de
*anotações* em módulos, classes e funções.

As anotações são avaliadas preguiçosamente e frequentemente contêm
referências futuras a objetos que ainda não foram definidos quando a
anotação é criada. Este módulo fornece um conjunto de ferramentas de
baixo nível que podem ser usadas para recuperar anotações de forma
confiável, mesmo na presença de referências futuras e em outros casos
extremos.

Este módulo oferece suporte à recuperação de anotações em três
formatos principais (veja "Format"), cada um dos quais funciona melhor
para diferentes casos de uso:

* "VALUE" avalia as anotações e retorna seus valores. Isso é mais
  simples de usar, mas pode levantar erros, por exemplo, se as
  anotações contiverem referências a nomes indefinidos.

* "FORWARDREF" retorna objetos "ForwardRef" para anotações que não
  podem ser resolvidas, permitindo que você inspecione as anotações
  sem avaliá-las. Isso é útil quando você precisa trabalhar com
  anotações que podem conter referências de encaminhamento não
  resolvidas.

* "STRING" retorna as anotações como uma string, semelhante a como
  apareceriam no arquivo-fonte. Isso é útil para geradores de
  documentação que desejam exibir anotações de forma legível.

A função "get_annotations()" é o principal ponto de entrada para
recuperar anotações. Dada uma função, classe ou módulo, ela retorna um
dicionário de anotações no formato solicitado. Este módulo também
fornece funcionalidade para trabalhar diretamente com a *função de
anotação*, usada para avaliar anotações, como
"get_annotate_from_class_namespace()" e "call_annotate_function()",
bem como a função "call_evaluate_function()" para trabalhar com
*funções de avaliação*.

Cuidado:

  A maioria das funcionalidades deste módulo pode executar código
  arbitrário; veja a seção de segurança para mais informações.

Ver também:

  **PEP 649** propôs o modelo atual de como as anotações funcionam em
  Python.

  **PEP 749** expandiu vários aspectos de **PEP 649** e introduziu o
  módulo "annotationlib".

  Boas práticas para anotações fornece práticas recomendadas para
  trabalhar com anotações.

  typing-extensions fornece uma função "get_annotations()", com
  compatibilidade retroativa, que funciona em versões anteriores do
  Python.


Semânticas de anotação
======================

A forma como as anotações são avaliadas mudou ao longo da história do
Python 3 e atualmente ainda depende de uma importação futura. Houve
modelos de execução para anotações:

* *Semântica de estoque* (padrão no Python 3.0 a 3.13; veja **PEP
  3107** e **PEP 526**): As anotações são avaliadas avidamente, à
  medida que são encontradas no código-fonte.

* *Anotações em string* (usadas com "from __future__ import
  annotations" no Python 3.7 e versões mais recentes; veja **PEP
  563**): As anotações são armazenadas apenas como strings.

* *Avaliação adiada* (padrão no Python 3.14 e versões mais recentes;
  veja **PEP 649** e **PEP 749**): As anotações são avaliadas
  preguiçosamente, somente quando são acessadas.

Como exemplo, considere o seguinte programa:

   def func(a: Cls) -> None:
       print(a)

   class Cls: pass

   print(func.__annotations__)

Isso se comportará da seguinte maneira:

* De acordo com a semântica de estoque (Python 3.13 e versões
  anteriores), ele levantará uma "NameError" na linha onde "func" está
  definido, porque "Cls" é um nome indefinido naquele ponto.

* Em anotações stringificadas (se "from __future__ import annotations"
  for usado), exibirá "{'a': 'Cls', 'return': 'None'}".

* Em avaliação adiada (Python 3.14 e posterior), exibirá "{'a': <class
  'Cls'>, 'return': None}".

A semântica de estoque foi usada quando as anotações de função foram
introduzidas pela primeira vez no Python 3.0 (por **PEP 3107**) porque
esta era a maneira mais simples e óbvia de implementar anotações. O
mesmo modelo de execução foi usado quando as anotações de variáveis
foram introduzidas no Python 3.6 (por **PEP 526**). No entanto, a
semântica de estoque causou problemas ao usar anotações como dicas de
tipo, como a necessidade de se referir a nomes que ainda não estavam
definidos quando a anotação era encontrada. Além disso, havia
problemas de desempenho com a execução de anotações no momento da
importação do módulo. Portanto, no Python 3.7, **PEP 563** introduziu
a capacidade de armazenar anotações como strings usando a sintaxe
"from __future__ import annotations". O plano na época era
eventualmente tornar esse comportamento o padrão, mas um problema
surgiu: anotações em string são mais difíceis de processar para
aqueles que inspecionam anotações em tempo de execução. Uma proposta
alternativa, **PEP 649**, introduziu o terceiro modelo de execução,
avaliação adiada, e foi implementada no Python 3.14. Anotações em
string ainda são usadas se "from __future__ import annotations"
estiver presente, mas esse comportamento será eventualmente removido.


Classes
=======

class annotationlib.Format

   Uma "IntEnum" que descreve os formatos nos quais as anotações podem
   ser retornadas. Membros da enumeração, ou seus valores inteiros
   equivalentes, podem ser passados para "get_annotations()" e outras
   funções neste módulo, bem como para funções "__annotate__".

   VALUE = 1

      Os valores são o resultado da avaliação das expressões de
      anotação.

   VALUE_WITH_FAKE_GLOBALS = 2

      Valor especial usado para sinalizar que uma função de anotação
      está sendo avaliada em um ambiente especial com variáveis
      globais falsas. Ao receber este valor, as funções de anotação
      devem retornar o mesmo valor do formato "Format.VALUE" ou
      levantar "NotImplementedError" para sinalizar que não suportam
      execução neste ambiente. Este formato é usado apenas
      internamente e não deve ser passado para as funções deste
      módulo.

   FORWARDREF = 3

      Valores são valores de anotação reais (conforme o formato
      "Format.VALUE") para valores definidos e proxies "ForwardRef"
      para valores indefinidos. Objetos reais podem conter referências
      a objetos proxy "ForwardRef".

   STRING = 4

      Valores são a string de texto da anotação como ela aparece no
      código-fonte, até modificações, incluindo, mas não se limitando
      a, normalizações de espaços em branco e otimizações de valores
      constantes.

      Os valores exatos dessas strings podem mudar em versões futuras
      do Python.

   Adicionado na versão 3.14.

class annotationlib.ForwardRef

   Um objeto proxy para referências futuras em anotações.

   Instâncias desta classe são retornadas quando o formato
   "FORWARDREF" é usado e as anotações contêm um nome que não pode ser
   resolvido. Isso pode acontecer quando uma referência de avanço é
   usada em uma anotação, como quando uma classe é referenciada antes
   de ser definida.

   __forward_arg__

      Uma string contendo o código que foi avaliado para produzir
      "ForwardRef". A string pode não ser exatamente equivalente à
      fonte original.

   evaluate(*, owner=None, globals=None, locals=None, type_params=None, format=Format.VALUE)

      Avalia a referência futura, retornando seu valor.

      Se o argumento *format* for "VALUE" (o padrão), este método
      poderá levantar uma exceção, como "NameError", caso a referência
      futura se refira a um nome que não pode ser resolvido. Os
      argumentos deste método podem ser usados para fornecer ligações
      para nomes que, de outra forma, seriam indefinidos. Se o
      argumento *format* for "FORWARDREF", o método nunca levantará
      uma exceção, mas poderá retornar uma instância de "ForwardRef".
      Por exemplo, se o objeto de referência futura contiver o código
      "list[undefined]", onde "undefined" é um nome que não está
      definido, avaliá-lo com o formato "FORWARDREF" retornará
      "list[ForwardRef('undefined')]". Se o argumento *format* for
      "STRING", o método retornará "__forward_arg__".

      O parâmetro *owner* fornece o mecanismo preferencial para passar
      informações de escopo para este método. O proprietário de uma
      "ForwardRef" é o objeto que contém a anotação da qual a
      "ForwardRef" deriva, como um objeto módulo, objeto tipo ou
      objeto função.

      Os parâmetros *globals*, *locals* e *type_params* fornecem um
      mecanismo mais preciso para influenciar os nomes disponíveis
      quando "ForwardRef" é avaliado. *globals* e *locals* são
      passados para "eval()", representando os espaços de nomes global
      e local nos quais o nome é avaliado. O parâmetro *type_params* é
      relevante para objetos criados usando a sintaxe nativa para
      classes genéricas e funções. É uma tupla de parâmetros de tipo
      que estão no escopo enquanto a referência futura está sendo
      avaliada. Por exemplo, ao avaliar um "ForwardRef" recuperado de
      uma anotação encontrada no espaço de nomes de classe de uma
      classe genérica "C", *type_params* deve ser definido como
      "C.__type_params__".

      Instâncias de "ForwardRef" retornadas por "get_annotations()"
      retêm referências a informações sobre o escopo de onde se
      originaram, portanto, chamar esse método sem argumentos
      adicionais pode ser suficiente para avaliar tais objetos.
      Instâncias de "ForwardRef" criadas por outros meios podem não
      ter nenhuma informação sobre seu escopo, portanto, passar
      argumentos para esse método pode ser necessário para avaliá-las
      com sucesso.

      Se nenhum entre *owner*, *globals*, *locals* ou *type_params*
      for fornecido e "ForwardRef" não contiver informações sobre sua
      origem, dicionários globals e locals vazios serão usados.

   Adicionado na versão 3.14.


Funções
=======

annotationlib.annotations_to_string(annotations)

   Converte um dicionário de anotações contendo valores de tempo de
   execução em um dicionário contendo apenas strings. Se os valores
   ainda não forem strings, eles serão convertidos usando
   "type_repr()". Isso serve como um auxiliar para funções de anotação
   fornecidas pelo usuário que oferecem suporte ao formato "STRING",
   mas não têm acesso ao código que cria as anotações.

   For example, this is used to implement the "STRING" format for
   "typing.TypedDict" classes created through the functional syntax:

      >>> from typing import TypedDict
      >>> Movie = TypedDict("movie", {"name": str, "year": int})
      >>> get_annotations(Movie, format=Format.STRING)
      {'name': 'str', 'year': 'int'}

   Adicionado na versão 3.14.

annotationlib.call_annotate_function(annotate, format, *, owner=None)

   Chama a *função de anotação* *annotate* com o *format* fornecido,
   um membro da enumeração "Format" e retorne o dicionário de
   anotações produzido pela função.

   Esta função auxiliar é necessária porque as funções de anotação
   geradas pelo compilador para funções, classes e módulos oferecem
   suporte a apenas o formato "VALUE" quando chamadas diretamente.
   Para oferecer suporte a outros formatos, esta função chama a função
   de anotação em um ambiente especial que permite a produção de
   anotações nos outros formatos. Este é um bloco de construção útil
   ao implementar funcionalidades que precisam avaliar anotações
   parcialmente enquanto uma classe está sendo construída.

   *owner* é o objeto que possui a função de anotação, geralmente uma
   função, classe ou módulo. Se fornecido, é usado no formato
   "FORWARDREF" para produzir um objeto "ForwardRef" que contém mais
   informações.

   Ver também:

     **PEP 649** contém uma explicação da técnica de implementação
     usada por esta função.

   Adicionado na versão 3.14.

annotationlib.call_evaluate_function(evaluate, format, *, owner=None)

   Chama a *função de avaliação* *evaluate* com o *format* fornecido,
   um membro da enumeração "Format" e retorna o valor produzido pela
   função. Isso é semelhante a "call_annotate_function()", mas esta
   última sempre retorna um dicionário que mapeia strings para
   anotações, enquanto esta função retorna um único valor.

   Isso se destina ao uso com as funções de avaliação geradas para
   elementos avaliados preguiçosamente relacionados a apelidos de tipo
   e parâmetros de tipo:

   * "typing.TypeAliasType.evaluate_value()", o valor dos apelidos de
     tipo

   * "typing.TypeVar.evaluate_bound()", a delimitação das variáveis de
     tipo

   * "typing.TypeVar.evaluate_constraints()", as restrições de tipos
     variáveis

   * "typing.TypeVar.evaluate_default()", o valor padrão de tipos
     variáveis

   * "typing.ParamSpec.evaluate_default()", o valor padrão de
     especificações de parâmetros

   * "typing.TypeVarTuple.evaluate_default()", o valor padrão de
     tuplas de tipos variáveis

   *owner* é o objeto que possui a função de avaliação, como o apelido
   de tipo ou o objeto de tipo variável.

   *format* pode ser usado para controlar o formato no qual o valor é
   retornado:

      >>> type Alias = undefined
      >>> call_evaluate_function(Alias.evaluate_value, Format.VALUE)
      Traceback (most recent call last):
      ...
      NameError: name 'undefined' is not defined
      >>> call_evaluate_function(Alias.evaluate_value, Format.FORWARDREF)
      ForwardRef('undefined')
      >>> call_evaluate_function(Alias.evaluate_value, Format.STRING)
      'undefined'

   Adicionado na versão 3.14.

annotationlib.get_annotate_from_class_namespace(namespace)

   Recupera a *função de anotação* de um dicionário de espaço de nomes
   de classe *namespace*. Retorna "None" se o espaço de nomes não
   contiver uma função de anotação. Isso é útil principalmente antes
   da classe ser totalmente criada (por exemplo, em uma metaclasse);
   após a classe existir, a função de anotação pode ser recuperada com
   "cls.__annotate__". Veja abaixo para um exemplo usando esta função
   em uma metaclasse.

   Adicionado na versão 3.14.

annotationlib.get_annotations(obj, *, globals=None, locals=None, eval_str=False, format=Format.VALUE)

   Calcula o dicionário de anotações para um objeto.

   *obj* pode ser um objeto chamável, classe, módulo ou outro objeto
   com os atributos "__annotate__" ou "__annotations__". Passar
   qualquer outro objeto levanta "TypeError".

   O parâmetro *format* controla o formato em que as anotações são
   retornadas e deve ser um membro da enumeração "Format" ou seu
   equivalente inteiro. Os diferentes formatos funcionam da seguinte
   forma:

   * VALUE: "object.__annotations__" é tentado primeiro; se não
     existir, a função "object.__annotate__" é chamada, se existir.

   * FORWARDREF: Se "object.__annotations__" existir e puder ser
     avaliado com sucesso, ele será usado; caso contrário, a função
     "object.__annotate__" será chamada. Se também não existir,
     "object.__annotations__" será tentado novamente e qualquer erro
     ao acessá-lo será levantado novamente.

     * Ao chamar "object.__annotate__", ele é chamado primeiro com
       "FORWARDREF". Se isso não for implementado, ele verificará se
       "VALUE_WITH_FAKE_GLOBALS" é suportado e o utilizará no ambiente
       de globais falsos. Se nenhum desses formatos for suportado, ele
       retornará para "VALUE". Se "VALUE" falhar, o erro desta chamada
       será gerado.

   * STRING: Se "object.__annotate__" existir, ele será chamado
     primeiro; caso contrário, "object.__annotations__" será usado e
     transformado em string usando "annotations_to_string()".

     * Ao chamar "object.__annotate__", ele é chamado primeiro com
       "STRING". Se isso não for implementado, ele verificará se
       "VALUE_WITH_FAKE_GLOBALS" é suportado e o utilizará no ambiente
       de globais falsos. Se nenhum desses formatos for suportado, ele
       recorrerá a "VALUE" com o resultado convertido usando
       "annotations_to_string()". Se "VALUE" falhar, o erro desta
       chamada será levantado.

   Retorna um dict. "get_annotations()" retorna um novo dict toda vez
   que é chamado; chamá-lo duas vezes no mesmo objeto retornará dois
   dicts diferentes, mas equivalentes.

   Esta função cuida de vários detalhes para você:

   * Se *eval_str* for verdadeiro, valores do tipo "str" serão
     descodificados usando "eval()". Isso se destina ao uso com
     anotações transformadas em string ("from __future__ import
     annotations"). É um erro definir *eval_str* como true com
     formatos diferentes de "Format.VALUE".

   * Se *obj* não tiver um dicionário de anotações, retorna um
     dicionário vazio. (Funções e métodos sempre têm um dicionário de
     anotações; classes, módulos e outros tipos de chamáveis podem não
     ter.)

   * Ignora anotações herdadas em classes, bem como anotações em
     metaclasses. Se uma classe não tiver seu próprio dicionário de
     anotações, retorna um dicionário vazio.

   * Todos os acessos aos membros do objeto e valores do dicionário
     são feitos usando "getattr()" e "dict.get()" por segurança.

   *eval_str* controla se valores do tipo "str" são substituídos ou
   não pelo resultado da chamada de "eval()" nesses valores:

   * Se eval_str for verdadeiro, "eval()" será chamado em valores do
     tipo "str". (Observe que "get_annotations()" não captura
     exceções; se "eval()" levanta uma exceção, ele desenrolará a
     pilha após a chamada de "get_annotations()".)

   * Se *eval_str* for falso (o padrão), os valores do tipo "str" não
     serão alterados.

   *globals* e *locals* são passados para "eval()"; consulte a
   documentação de "eval()" para mais informações. Se *globals* ou
   *locals* for "None", esta função pode substituir esse valor por um
   padrão específico do contexto, dependendo de "type(obj)":

   * Se *obj* for um módulo, *globals* assume como padrão
     "obj.__dict__".

   * Se *obj* for uma classe, *globals* assume como padrão
     "sys.modules[obj.__module__].__dict__" e *locals* assume como
     padrão o espaço de nomes da classe *obj*.

   * Se *obj* for um chamável, *globals* assume como padrão
     "obj.__globals__", embora se *obj* for uma função encapsulada
     (usando "functools.update_wrapper()") ou um objeto
     "functools.partial", ela será desencapsulada até que uma função
     não encapsulada seja encontrada.

   Chamar "get_annotations()" é uma boa prática para acessar o
   dicionário de anotações de qualquer objeto. Consulte Boas práticas
   para anotações para obter mais informações sobre as práticas
   recomendadas para anotações.

      >>> def f(a: int, b: str) -> float:
      ...     pass
      >>> get_annotations(f)
      {'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'float'>}

   Adicionado na versão 3.14.

annotationlib.type_repr(value)

   Converte um valor Python arbitrário para um formato adequado para
   uso pelo formato "STRING". Isso chama "repr()" para a maioria dos
   objetos, mas tem um tratamento especial para alguns objetos, como
   objetos tipo.

   Isto serve como um auxiliar para funções de anotação fornecidas
   pelo usuário que oferecem suporte ao formato "STRING", mas não têm
   acesso ao código que cria as anotações. Também pode ser usado para
   fornecer uma representação de string amigável para outros objetos
   que contêm valores comumente encontrados em anotações.

   Adicionado na versão 3.14.


Receitas
========


Usando anotações em uma metaclasse
----------------------------------

Uma metaclasse pode querer inspecionar ou até mesmo modificar as
anotações no corpo de uma classe durante a criação da classe. Isso
requer a recuperação das anotações do dicionário de espaços de nomes
da classe. Para classes criadas com "from __future__ import
annotations", as anotações estarão na chave "__annotations__" do
dicionário. Para outras classes com anotações,
"get_annotate_from_class_namespace()" pode ser usado para obter a
função annotate, e "call_annotate_function()" pode ser usado para
chamá-la e recuperar as anotações. Usar o formato "FORWARDREF"
geralmente é a melhor opção, pois permite que as anotações se refiram
a nomes que ainda não podem ser resolvidos quando a classe é criada.

Para modificar as anotações, é melhor criar uma função de anotação que
chame a função de anotação original, faça os ajustes necessários e
retorne o resultado.

Abaixo está um exemplo de uma metaclasse que filtra todas as anotações
"typing.ClassVar" da classe e as coloca em um atributo separado:

   import annotationlib
   import typing

   class ClassVarSeparator(type):
      def __new__(mcls, name, bases, ns):
         if "__annotations__" in ns:  # from __future__ import annotations
            annotations = ns["__annotations__"]
            classvar_keys = {
               key for key, value in annotations.items()
               # Use comparação de strings para simplificar; uma solução
               # mais robusta poderia usar annotationlib.ForwardRef.evaluate
               if value.startswith("ClassVar")
            }
            classvars = {key: annotations[key] for key in classvar_keys}
            ns["__annotations__"] = {
               key: value for key, value in annotations.items()
               if key not in classvar_keys
            }
            wrapped_annotate = None
         elif annotate := annotationlib.get_annotate_from_class_namespace(ns):
            annotations = annotationlib.call_annotate_function(
               annotate, format=annotationlib.Format.FORWARDREF
            )
            classvar_keys = {
               key for key, value in annotations.items()
               if typing.get_origin(value) is typing.ClassVar
            }
            classvars = {key: annotations[key] for key in classvar_keys}

            def wrapped_annotate(format):
               annos = annotationlib.call_annotate_function(annotate, format, owner=typ)
               return {key: value for key, value in annos.items() if key not in classvar_keys}

         else:  # nenhuma anotação
            classvars = {}
            wrapped_annotate = None
         typ = super().__new__(mcls, name, bases, ns)

         if wrapped_annotate is not None:
            # Encapsula o __annotate__ original com um invólucro que remove ClassVars
            typ.__annotate__ = wrapped_annotate
         typ.classvars = classvars  # Armazena as ClassVars em um atributo separado
         return typ


Creating a custom callable annotate function
--------------------------------------------

*Funções de anotação* personalizadas podem ser funções literais como
aquelas geradas automaticamente para funções, classes e módulos. Ou,
elas podem querer utilizar o encapsulamento fornecido por classes,
caso em que qualquer *chamável* pode ser usado como uma *função de
anotação*.

To provide the "VALUE", "STRING", or "FORWARDREF" formats directly, an
*annotate function* must provide the following attribute:

* A callable "__call__" with signature "__call__(format, /) -> dict",
  that does not raise a "NotImplementedError" when called with a
  supported format.

To provide the "VALUE_WITH_FAKE_GLOBALS" format, which is used to
automatically generate "STRING" or "FORWARDREF" if they are not
supported directly, *annotate functions* must provide the following
attributes:

* A callable "__call__" with signature "__call__(format, /) -> dict",
  that does not raise a "NotImplementedError" when called with
  "VALUE_WITH_FAKE_GLOBALS".

* A code object "__code__" containing the compiled code for the
  annotate function.

* Optional: A tuple of the function's positional defaults
  "__defaults__", if the function represented by "__code__" uses any
  positional defaults.

* Optional: A dict of the function's keyword defaults
  "__kwdefaults__", if the function represented by "__code__" uses any
  keyword defaults.

* Optional: All other function attributes.

   class Annotate:
       called_formats = []

       def __call__(self, format=None, /, *, _self=None):
           # When called with fake globals, `_self` will be the
           # actual self value, and `self` will be the format.
           if _self is not None:
               self, format = _self, self

           self.called_formats.append(format)
           if format <= 2:  # VALUE or VALUE_WITH_FAKE_GLOBALS
               return {"x": MyType}
           raise NotImplementedError

       __code__ = __call__.__code__
       __defaults__ = (None,)
       __kwdefaults__ = property(lambda self: dict(_self=self))

       __globals__ = {}
       __builtins__ = {}
       __closure__ = None

This can then be called with:

   >>> from annotationlib import call_annotate_function, Format
   >>> call_annotate_function(Annotate(), format=Format.STRING)
   {'x': 'MyType'}

Or used as the annotate function for an object:

   >>> from annotationlib import get_annotations, Format
   >>> class C:
   ...   pass
   >>> C.__annotate__ = Annotate()
   >>> get_annotations(Annotate(), format=Format.STRING)
   {'x': 'MyType'}


Limitações do formato "STRING"
==============================

O formato "STRING" tem como objetivo aproximar o código-fonte da
anotação, mas a estratégia de implementação usada significa que nem
sempre é possível recuperar o código-fonte exato.

Primeiro, a transformação em string, é claro, não pode recuperar
nenhuma informação que não esteja presente no código compilado,
incluindo comentários, espaços em branco, parênteses e operações que
são simplificadas pelo compilador.

Em segundo lugar, a transformação em string pode interceptar quase
todas as operações que envolvem nomes pesquisados em algum escopo, mas
não pode interceptar operações que operem totalmente em constantes.
Como corolário, isso também significa que não é seguro solicitar o
formato "STRING" em código não confiável: Python é poderoso o
suficiente para permitir a execução arbitrária de código mesmo sem
acesso a nenhuma variável global ou embutida. Por exemplo:

   >>> def f(x: (1).__class__.__base__.__subclasses__()[-1].__init__.__builtins__["print"]("Hello world")): pass
   ...
   >>> annotationlib.get_annotations(f, format=annotationlib.Format.STRING)
   Hello world
   {'x': 'None'}

Nota:

  Este exemplo específico funciona no momento em que este artigo foi
  escrito, mas depende de detalhes de implementação e não há garantia
  de que funcionará no futuro.

Entre os diferentes tipos de expressões que existem em Python,
conforme representado pelo módulo "ast", algumas expressões são
suportadas, o que significa que o formato "STRING" geralmente pode
recuperar o código-fonte original; outras não são suportadas, o que
significa que podem resultar em saída incorreta ou erro.

Os seguintes são aceitos (às vezes com ressalvas):

* "ast.BinOp"

* "ast.UnaryOp"

  * "ast.Invert" ("~"), "ast.UAdd" ("+") e "ast.USub" ("-") são
    suportadas

  * "ast.Not" ("not") não é suportada

* "ast.Dict" (exceto ao usar desempacotamento "**")

* "ast.Set"

* "ast.Compare"

  * "ast.Eq" e "ast.NotEq" são suportadas

  * "ast.Lt", "ast.LtE", "ast.Gt" e "ast.GtE" são suportadas, mas o
    operando pode ser invertido

  * "ast.Is", "ast.IsNot", "ast.In" e "ast.NotIn" não são suportadas

* "ast.Call" (exceto ao usar desempacotamento "**")

* "ast.Constant" (embora não seja a representação exata da constante;
  por exemplo, sequências de escape em strings são perdidas; números
  hexadecimais são convertidos em decimais)

* "ast.Attribute" (presumindo que o valor não é uma constante)

* "ast.Subscript" (presumindo que o valor não é uma constante)

* "ast.Starred" (desempacotamento "*")

* "ast.Name"

* "ast.List"

* "ast.Tuple"

* "ast.Slice"

Os seguintes não são suportados, mas geram um erro informativo quando
encontrados pela transformação em string:

* "ast.FormattedValue" (f-strings; o erro não é detectado se
  especificadores de conversões como "!r" forem usados)

* "ast.JoinedStr" (f-strings)

Os seguintes itens não são suportados e resultam em saída incorreta:

* "ast.BoolOp" ("and" e "or")

* "ast.IfExp"

* "ast.Lambda"

* "ast.ListComp"

* "ast.SetComp"

* "ast.DictComp"

* "ast.GeneratorExp"

Os seguintes itens não são permitidos em escopos de anotação e,
portanto, não são relevantes:

* "ast.NamedExpr" (":=")

* "ast.Await"

* "ast.Yield"

* "ast.YieldFrom"


Limitações do formato "FORWARDREF"
==================================

O formato "FORWARDREF" visa produzir valores reais o máximo possível,
com tudo o que não puder ser resolvido sendo substituído por objetos
"ForwardRef". Ele é afetado, em linhas gerais, pelas mesmas limitações
do formato "STRING": anotações que realizam operações em literais ou
que usam tipos de expressão não suportados podem levantar exceções
quando avaliadas usando o formato "FORWARDREF".

Abaixo estão alguns exemplos do comportamento com expressões não
suportadas:

   >>> from annotationlib import get_annotations, Format
   >>> def zerodiv(x: 1 / 0): ...
   >>> get_annotations(zerodiv, format=Format.STRING)
   Traceback (most recent call last):
     ...
   ZeroDivisionError: division by zero
   >>> get_annotations(zerodiv, format=Format.FORWARDREF)
   Traceback (most recent call last):
     ...
   ZeroDivisionError: division by zero
   >>> def ifexp(x: 1 if y else 0): ...
   >>> get_annotations(ifexp, format=Format.STRING)
   {'x': '1'}


Implicações de segurança de anotações de introspecção
=====================================================

Grande parte da funcionalidade deste módulo envolve a execução de
código relacionado a anotações, que podem então realizar ações
arbitrárias. Por exemplo, "get_annotations()" pode chamar uma *função
de anotação* arbitrária, e "ForwardRef.evaluate()" pode chamar
"eval()" em uma string arbitrária. O código contido em uma anotação
pode realizar chamadas de sistema arbitrárias, entrar em um laço
infinito ou executar qualquer outra operação. Isso também se aplica a
qualquer acesso ao atributo "__annotations__" e a várias funções no
módulo "typing" que trabalham com anotações, como
"typing.get_type_hints()".

Qualquer problema de segurança decorrente disso também se aplica
imediatamente após a importação de código que possa conter anotações
não confiáveis: a importação de código sempre pode causar a execução
de operações arbitrárias. No entanto, não é seguro aceitar strings ou
outras entradas de uma fonte não confiável e passá-las para qualquer
uma das APIs para introspecção de anotações, por exemplo, editando um
dicionário "__annotations__" ou criando diretamente um objeto
"ForwardRef".
