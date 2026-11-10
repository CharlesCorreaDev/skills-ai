"ast" --- Árvores de sintaxe abstrata
*************************************

**Código-fonte:** Lib/ast.py

======================================================================

O módulo "ast" ajuda as aplicações Python a processar árvores da
gramática de sintaxe abstrata do Python. A sintaxe abstrata em si pode
mudar em cada lançamento do Python; este módulo ajuda a descobrir
programaticamente como é a gramática atual.

Uma árvore de sintaxe abstrata pode ser gerada passando
"ast.PyCF_ONLY_AST" como um sinalizador para a função embutida
"compile()", ou usando o auxiliar "parse()" fornecido neste módulo. O
resultado será uma árvore de objetos cujas classes herdam de
"ast.AST". Uma árvore de sintaxe abstrata pode ser compilada em um
objeto código Python usando a função embutida "compile()".


Gramática abstrata
==================

A gramática abstrata está atualmente definida da seguinte forma:

   -- ASDL's 4 builtin types are:
   -- identifier, int, string, constant

   module Python
   {
       mod = Module(stmt* body, type_ignore* type_ignores)
           | Interactive(stmt* body)
           | Expression(expr body)
           | FunctionType(expr* argtypes, expr returns)

       stmt = FunctionDef(identifier name, arguments args,
                          stmt* body, expr* decorator_list, expr? returns,
                          string? type_comment, type_param* type_params)
             | AsyncFunctionDef(identifier name, arguments args,
                                stmt* body, expr* decorator_list, expr? returns,
                                string? type_comment, type_param* type_params)

             | ClassDef(identifier name,
                expr* bases,
                keyword* keywords,
                stmt* body,
                expr* decorator_list,
                type_param* type_params)
             | Return(expr? value)

             | Delete(expr* targets)
             | Assign(expr* targets, expr value, string? type_comment)
             | TypeAlias(expr name, type_param* type_params, expr value)
             | AugAssign(expr target, operator op, expr value)
             -- 'simple' indicates that we annotate simple name without parens
             | AnnAssign(expr target, expr annotation, expr? value, int simple)

             -- use 'orelse' because else is a keyword in target languages
             | For(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
             | AsyncFor(expr target, expr iter, stmt* body, stmt* orelse, string? type_comment)
             | While(expr test, stmt* body, stmt* orelse)
             | If(expr test, stmt* body, stmt* orelse)
             | With(withitem* items, stmt* body, string? type_comment)
             | AsyncWith(withitem* items, stmt* body, string? type_comment)

             | Match(expr subject, match_case* cases)

             | Raise(expr? exc, expr? cause)
             | Try(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)
             | TryStar(stmt* body, excepthandler* handlers, stmt* orelse, stmt* finalbody)
             | Assert(expr test, expr? msg)

             | Import(alias* names, int? is_lazy)
             | ImportFrom(identifier? module, alias* names, int? level, int? is_lazy)

             | Global(identifier* names)
             | Nonlocal(identifier* names)
             | Expr(expr value)
             | Pass | Break | Continue

             -- col_offset is the byte offset in the utf8 string the parser uses
             attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

             -- BoolOp() can use left & right?
       expr = BoolOp(boolop op, expr* values)
            | NamedExpr(expr target, expr value)
            | BinOp(expr left, operator op, expr right)
            | UnaryOp(unaryop op, expr operand)
            | Lambda(arguments args, expr body)
            | IfExp(expr test, expr body, expr orelse)
            | Dict(expr?* keys, expr* values)
            | Set(expr* elts)
            | ListComp(expr elt, comprehension* generators)
            | SetComp(expr elt, comprehension* generators)
            | DictComp(expr key, expr? value, comprehension* generators)
            | GeneratorExp(expr elt, comprehension* generators)
            -- the grammar constrains where yield expressions can occur
            | Await(expr value)
            | Yield(expr? value)
            | YieldFrom(expr value)
            -- need sequences for compare to distinguish between
            -- x < 4 < 3 and (x < 4) < 3
            | Compare(expr left, cmpop* ops, expr* comparators)
            | Call(expr func, expr* args, keyword* keywords)
            | FormattedValue(expr value, int conversion, expr? format_spec)
            | Interpolation(expr value, constant str, int conversion, expr? format_spec)
            | JoinedStr(expr* values)
            | TemplateStr(expr* values)
            | Constant(constant value, string? kind)

            -- the following expression can appear in assignment context
            | Attribute(expr value, identifier attr, expr_context ctx)
            | Subscript(expr value, expr slice, expr_context ctx)
            | Starred(expr value, expr_context ctx)
            | Name(identifier id, expr_context ctx)
            | List(expr* elts, expr_context ctx)
            | Tuple(expr* elts, expr_context ctx)

            -- can appear only in Subscript
            | Slice(expr? lower, expr? upper, expr? step)

             -- col_offset is the byte offset in the utf8 string the parser uses
             attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

       expr_context = Load | Store | Del

       boolop = And | Or

       operator = Add | Sub | Mult | MatMult | Div | Mod | Pow | LShift
                    | RShift | BitOr | BitXor | BitAnd | FloorDiv

       unaryop = Invert | Not | UAdd | USub

       cmpop = Eq | NotEq | Lt | LtE | Gt | GtE | Is | IsNot | In | NotIn

       comprehension = (expr target, expr iter, expr* ifs, int is_async)

       excepthandler = ExceptHandler(expr? type, identifier? name, stmt* body)
                       attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

       arguments = (arg* posonlyargs, arg* args, arg? vararg, arg* kwonlyargs,
                    expr?* kw_defaults, arg? kwarg, expr* defaults)

       arg = (identifier arg, expr? annotation, string? type_comment)
              attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

       -- keyword arguments supplied to call (NULL identifier for **kwargs)
       keyword = (identifier? arg, expr value)
                  attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

       -- import name with optional 'as' alias.
       alias = (identifier name, identifier? asname)
                attributes (int lineno, int col_offset, int? end_lineno, int? end_col_offset)

       withitem = (expr context_expr, expr? optional_vars)

       match_case = (pattern pattern, expr? guard, stmt* body)

       pattern = MatchValue(expr value)
               | MatchSingleton(constant value)
               | MatchSequence(pattern* patterns)
               | MatchMapping(expr* keys, pattern* patterns, identifier? rest)
               | MatchClass(expr cls, pattern* patterns, identifier* kwd_attrs, pattern* kwd_patterns)

               | MatchStar(identifier? name)
               -- The optional "rest" MatchMapping parameter handles capturing extra mapping keys

               | MatchAs(pattern? pattern, identifier? name)
               | MatchOr(pattern* patterns)

                attributes (int lineno, int col_offset, int end_lineno, int end_col_offset)

       type_ignore = TypeIgnore(int lineno, string tag)

       type_param = TypeVar(identifier name, expr? bound, expr? default_value)
                  | ParamSpec(identifier name, expr? default_value)
                  | TypeVarTuple(identifier name, expr? default_value)
                  attributes (int lineno, int col_offset, int end_lineno, int end_col_offset)
   }


Classes de nós
==============

class ast.AST

   Esta é a base abstrata de todas as classes de nós de AST. As
   classes de nós reais são derivadas do arquivo "Parser/Python.asdl",
   que é reproduzido acima. Elas são definidas no módulo C "_ast" e
   reexportadas no "ast".

   Há uma classe definida para cada símbolo do lado esquerdo na
   gramática abstrata (por exemplo, "ast.stmt" ou "ast.expr"). Além
   disso, existe uma classe definida para cada construtor no lado
   direito; essas classes herdam das classes para as árvores do lado
   esquerdo. Por exemplo, "ast.BinOp" herda de "ast.expr". Para regras
   de produção com alternativas ("somas"), a classe do lado esquerdo é
   abstrata: apenas instâncias de nós construtores específicos são
   criadas.

   _fields

      Cada classe concreta possui um atributo "_fields" que fornece os
      nomes de todos os nós filhos.

      Cada instância de uma classe concreta tem um atributo para cada
      nó filho, do tipo definido na gramática. Por exemplo, as
      instâncias "ast.BinOp" possuem um atributo "left" do tipo
      "ast.expr".

      Se estes atributos estiverem marcados como opcionais na
      gramática (usando um ponto de interrogação), o valor pode ser
      "None". Se os atributos puderem ter valor zero ou mais (marcados
      com um asterisco), os valores serão representados como listas do
      Python. Todos os atributos possíveis devem estar presentes e ter
      valores válidos ao compilar uma AST com "compile()".

   _field_types

      O atributo "_field_types" em cada classe concreta é um
      dicionário que mapeia nomes de campos (como também listado em
      "_fields") para seus tipos.

         >>> ast.TypeVar._field_types
         {'name': <class 'str'>, 'bound': ast.expr | None, 'default_value': ast.expr | None}

      Adicionado na versão 3.13.

   lineno
   col_offset
   end_lineno
   end_col_offset

      As instâncias das subclasses "ast.expr" e "ast.stmt" possuem os
      atributos "lineno", "col_offset", "end_lineno" e
      "end_col_offset". O "lineno" e "end_lineno" são o primeiro e o
      último número de linha do intervalo do texto de origem (indexado
      em 1, para que a primeira linha seja a linha 1) e o "col_offset"
      e "end_col_offset" são os deslocamentos de byte UTF-8
      correspondentes do primeiro e do último tokens que geraram o nó.
      O deslocamento UTF-8 é registrado porque o analisador sintático
      usa UTF-8 internamente.

      Observe que as posições finais não são exigidas pelo compilador
      e, portanto, são opcionais. O deslocamento final está *após* o
      último símbolo, por exemplo, é possível obter o segmento de
      origem de um nó de expressão de uma linha usando
      "source_line[node.col_offset : node.end_col_offset]".

   O construtor de uma classe "ast.T" analisa seus argumentos da
   seguinte forma:

   * Se houver argumentos posicionais, deve haver tantos quanto houver
     itens em "T._fields"; eles serão atribuídos como atributos desses
     nomes.

   * Se houver argumentos nomeados, eles definirão os atributos dos
     mesmos nomes para os valores fornecidos.

   Por exemplo, para criar e popular um nó "ast.UnaryOp", você poderia
   usar

      node = ast.UnaryOp(ast.USub(), ast.Constant(5, lineno=0, col_offset=0),
                         lineno=0, col_offset=0)

   Se um campo que é opcional na gramática for omitido do construtor,
   o padrão é "None". Se um campo de lista for omitido, o padrão será
   a lista vazia. Se um campo do tipo "ast.expr_context" for omitido,
   o padrão é "Load()". Se qualquer outro campo for omitido, uma
   "DeprecationWarning" será levantada e o nó AST não terá este campo.
   No Python 3.15, esta condição levantará um erro.

Alterado na versão 3.8: A classe "ast.Constant" é agora usada para
todas as constantes.

Alterado na versão 3.9: Os índices simples são representados por seus
valores, as fatias estendidas são representadas como tuplas.

Alterado na versão 3.13: Os construtores de nós AST foram alterados
para fornecer valores padrão sensatos para campos omitidos: campos
opcionais agora têm "None" como padrão, campos do tipo lista têm uma
lista vazia como padrão e campos do tipo "ast.expr_context" têm
"Load()" como padrão. Anteriormente, atributos omitidos não existiam
nos nós construídos (tentar acessá-los levantava "AttributeError").

Alterado na versão 3.14: A saída "__repr__()" dos nós "AST" inclui os
valores dos campos dos nós.

Descontinuado desde a versão 3.8, removido na versão 3.14: Versões
anteriores do Python forneciam as classes AST "ast.Num", "ast.Str",
"ast.Bytes", "ast.NameConstant" e "ast.Ellipsis", que foram
descontinuadas no Python 3.8. Essas classes foram removidas no Python
3.14, e sua funcionalidade foi substituída por "ast.Constant".

Descontinuado desde a versão 3.9: Classes antigas "ast.Index" e
"ast.ExtSlice" ainda estão disponíveis, mas serão removidos em versões
futuras do Python. Enquanto isso, instanciá-las retornará uma
instância de uma classe diferente.

Descontinuado desde a versão 3.13, removido na versão 3.15: Versões
anteriores do Python permitiam a criação de nós AST sem campos
obrigatórios. Da mesma forma, os construtores do nó AST permitiam
argumentos nomeados arbitrários que eram definidos como atributos do
nó AST, mesmo que não correspondessem a nenhum dos campos do nó AST.
Estes casos agora levantam "TypeError".

Descontinuado desde a versão 3.15, será removido na versão 3.20: Na
gramática acima, as classes de nós da AST que correspondem a regras de
produção com variantes (também conhecidas como "somas") são classes
abstratas. Versões anteriores do Python permitiam a criação de
instâncias diretas dessas classes de nós abstratas. Esse comportamento
foi descontinuado e será removido no Python 3.20.

Nota:

  As descrições das classes de nós específicas exibidas aqui foram
  inicialmente adaptadas do fantástico projeto Green Tree Snakes e de
  todos os seus contribuidores.


Nós raízes
----------

class ast.Module(body, type_ignores)

   Um módulo Python, como entrada de arquivo. Tipo de nó gerado por
   "ast.parse()" com *mode* no padrão ""exec"".

   "body" é uma "list" das Instruções do módulo.

   "type_ignores" é uma "list" dos comentários de ignorar tipo do
   módulo; veja "ast.parse()" para mais detalhes.

      >>> print(ast.dump(ast.parse('x = 1'), indent=4))
      Module(
          body=[
              Assign(
                  targets=[
                      Name(id='x', ctx=Store())],
                  value=Constant(value=1))])

class ast.Expression(body)

   Uma única entrada de expressão Python. Tipo de nó gerado por
   "ast.parse()" quando *mode* é ""eval"".

   "body" é um nó único, um dos tipos de expressão.

      >>> print(ast.dump(ast.parse('123', mode='eval'), indent=4))
      Expression(
          body=Constant(value=123))

class ast.Interactive(body)

   Uma única entrada interativa, como em Modo interativo. Tipo de nó
   gerado por "ast.parse()" quando *mode* é ""single"".

   "body" é uma "list" de nós de instrução.

      >>> print(ast.dump(ast.parse('x = 1; y = 2', mode='single'), indent=4))
      Interactive(
          body=[
              Assign(
                  targets=[
                      Name(id='x', ctx=Store())],
                  value=Constant(value=1)),
              Assign(
                  targets=[
                      Name(id='y', ctx=Store())],
                  value=Constant(value=2))])

class ast.FunctionType(argtypes, returns)

   Uma representação de comentários de tipo antigo para funções, já
   que as versões do Python anteriores a 3.5 não davam suporte às
   anotações da **PEP 484**. Tipo de nó gerado por "ast.parse()"
   quando *mode* é ""func_type"".

   Esses comentários de tipo ficariam assim:

      def sum_two_number(a, b):
          # tipo: (int, int) -> int
          return a + b

   "argtypes" é uma "list" de nós de expressão.

   "returns" é um único nó de expressão.

      >>> print(ast.dump(ast.parse('(int, str) -> List[int]', mode='func_type'), indent=4))
      FunctionType(
          argtypes=[
              Name(id='int'),
              Name(id='str')],
          returns=Subscript(
              value=Name(id='List'),
              slice=Name(id='int')))

   Adicionado na versão 3.8.


Literais
--------

class ast.Constant(value, kind)

   Um valor constante. O atributo "value" do literal "Constant" contém
   o objeto Python que ele representa. Os valores representados podem
   ser instâncias de "str", "bytes", "int", "float", "complex" e
   "bool", e as constantes "None" e "Ellipsis".

   O atributo "kind" é uma string opcional. Para literais de string
   com o prefixo "u", "kind" é definido como "'u'". Para todas as
   outras constantes, "kind" é "None".

      >>> print(ast.dump(ast.parse('123', mode='eval'), indent=4))
      Expression(
          body=Constant(value=123))
      >>> print(ast.dump(ast.parse("u'hello'", mode='eval'), indent=4))
      Expression(
          body=Constant(value='hello', kind='u'))

class ast.FormattedValue(value, conversion, format_spec)

   Nó que representa um único campo de formatação em uma f-string. Se
   a string contiver um único campo de formatação e nada mais, o nó
   poderá ser isolado, caso contrário ele aparecerá em "JoinedStr".

   * "value" é qualquer nó de expressão (como um literal, uma variável
     ou uma chamada de função).

   * "conversion" é um inteiro:

     * -1: sem formatação

     * 97 ("ord('a')"): formatação e "ASCII" com "!a"

     * 114 ("ord('r')"): formatação em "repr()" com "!r"

     * 115 ("ord('s')"): formatação em "string" com "!s"

   * "format_spec" é um nó "JoinedStr" que representa a formatação do
     valor, ou "None" se nenhum formato foi especificado. Tanto
     "conversion" quanto "format_spec" podem ser configurados ao mesmo
     tempo.

class ast.JoinedStr(values)

   Uma f-string, compreendendo uma série de nós "FormattedValue" e
   "Constant".

      >>> print(ast.dump(ast.parse('f"sin({a}) is {sin(a):.3}"', mode='eval'), indent=4))
      Expression(
          body=JoinedStr(
              values=[
                  Constant(value='sin('),
                  FormattedValue(
                      value=Name(id='a'),
                      conversion=-1),
                  Constant(value=') is '),
                  FormattedValue(
                      value=Call(
                          func=Name(id='sin'),
                          args=[
                              Name(id='a')]),
                      conversion=-1,
                      format_spec=JoinedStr(
                          values=[
                              Constant(value='.3')]))]))

class ast.TemplateStr(values, /)

   Adicionado na versão 3.14.

   Nó que representa um literal de string template, compreendendo uma
   série de nós "Interpolation" e "Constant". Esses nós podem estar em
   qualquer ordem e não precisam ser intercalados.

      >>> expr = ast.parse('t"{name} finished {place:ordinal}"', mode='eval')
      >>> print(ast.dump(expr, indent=4))
      Expression(
          body=TemplateStr(
              values=[
                  Interpolation(
                      value=Name(id='name'),
                      str='name',
                      conversion=-1),
                  Constant(value=' finished '),
                  Interpolation(
                      value=Name(id='place'),
                      str='place',
                      conversion=-1,
                      format_spec=JoinedStr(
                          values=[
                              Constant(value='ordinal')]))]))

class ast.Interpolation(value, str, conversion, format_spec=None)

   Adicionado na versão 3.14.

   Nó que representa um único campo de interpolação em um literal de
   string template.

   * "value" é qualquer nó de expressão (como um literal, uma variável
     ou uma chamada de função). Tem o mesmo significado que
     "FormattedValue.value".

   * "str" é uma constante que contém o texto da expressão de
     interpolação.

     Se "str" for definido como "None", "value" será usado para gerar
     código ao chamar "ast.unparse()". Isso não garante mais que o
     código gerado seja idêntico ao original e se destina à geração de
     código.

   * "conversion" é um inteiro:

     * -1: sem formatação

     * 97 ("ord('a')"): conversão em "ASCII" com "!a"

     * 114 ("ord('r')"): conversão em "repr()" com "!r"

     * 115 ("ord('s')"): conversão em "string" com "!s"

     Isso tem o mesmo significado que "FormattedValue.conversion".

   * "format_spec" é um nó "JoinedStr" que representa a formatação do
     valor, ou "None" se nenhum formato foi especificado. Tanto
     "conversion" quanto "format_spec" podem ser definidos ao mesmo
     tempo. Isso tem o mesmo significado que
     "FormattedValue.format_spec".

class ast.List(elts, ctx)
class ast.Tuple(elts, ctx)

   Uma lista ou tupla. "elts" contém uma lista de nós que representam
   os elementos. "ctx" é "Store" se o contêiner for um alvo de
   atribuição (ou seja, "(x,y)=algumacoisa"), e "Load" caso contrário.

      >>> print(ast.dump(ast.parse('[1, 2, 3]', mode='eval'), indent=4))
      Expression(
          body=List(
              elts=[
                  Constant(value=1),
                  Constant(value=2),
                  Constant(value=3)]))
      >>> print(ast.dump(ast.parse('(1, 2, 3)', mode='eval'), indent=4))
      Expression(
          body=Tuple(
              elts=[
                  Constant(value=1),
                  Constant(value=2),
                  Constant(value=3)]))

class ast.Set(elts)

   Um conjunto. "elts" contém uma lista de nós que representam os
   elementos do conjunto.

      >>> print(ast.dump(ast.parse('{1, 2, 3}', mode='eval'), indent=4))
      Expression(
          body=Set(
              elts=[
                  Constant(value=1),
                  Constant(value=2),
                  Constant(value=3)]))

class ast.Dict(keys, values)

   Um dicionário. "keys" e "values" contêm listas de nós que
   representam as chaves e os valores respectivamente, em ordem
   correspondente (o que seria retornado ao chamar "dictionary.keys()"
   e "dictionary.values()").

   Ao desempacotar o dicionário usando literais de dicionário, a
   expressão a ser expandida vai para a lista "values", com um "None"
   na posição correspondente em "keys".

      >>> print(ast.dump(ast.parse('{"a":1, **d}', mode='eval'), indent=4))
      Expression(
          body=Dict(
              keys=[
                  Constant(value='a'),
                  None],
              values=[
                  Constant(value=1),
                  Name(id='d')]))


Variáveis
---------

class ast.Name(id, ctx)

   Um nome de variável. "id" contém o nome como uma string e "ctx" é
   um dos seguintes tipos.

class ast.Load
class ast.Store
class ast.Del

   As referências de variáveis podem ser usadas para carregar o valor
   de uma variável, para atribuir um novo valor a ela ou para
   excluí-la. As referências de variáveis recebem um contexto para
   distinguir esses casos.

      >>> print(ast.dump(ast.parse('a'), indent=4))
      Module(
          body=[
              Expr(
                  value=Name(id='a'))])

      >>> print(ast.dump(ast.parse('a = 1'), indent=4))
      Module(
          body=[
              Assign(
                  targets=[
                      Name(id='a', ctx=Store())],
                  value=Constant(value=1))])

      >>> print(ast.dump(ast.parse('del a'), indent=4))
      Module(
          body=[
              Delete(
                  targets=[
                      Name(id='a', ctx=Del())])])

class ast.Starred(value, ctx)

   Uma referência de variável "*var". "value" contém a variável,
   normalmente um nó "Name". Este tipo deve ser usado ao construir um
   nó "Call" com "*args".

      >>> print(ast.dump(ast.parse('a, *b = it'), indent=4))
      Module(
          body=[
              Assign(
                  targets=[
                      Tuple(
                          elts=[
                              Name(id='a', ctx=Store()),
                              Starred(
                                  value=Name(id='b', ctx=Store()),
                                  ctx=Store())],
                          ctx=Store())],
                  value=Name(id='it'))])


Expressões
----------

class ast.Expr(value)

   Quando uma expressão, como uma chamada de função, aparece como uma
   instrução por si só com seu valor de retorno não usado ou
   armazenado, ela é encapsulada neste contêiner. "value" contém um
   dos outros nós nesta seção, um nó "Constant", um "Name", um
   "Lambda", um "Yield" ou "YieldFrom".

      >>> print(ast.dump(ast.parse('-a'), indent=4))
      Module(
          body=[
              Expr(
                  value=UnaryOp(
                      op=USub(),
                      operand=Name(id='a')))])

class ast.UnaryOp(op, operand)

   Uma operação unária. "op" é o operador e "operand" qualquer nó de
   expressão.

class ast.UAdd
class ast.USub
class ast.Not
class ast.Invert

   Tokens de operador unário. "Not" é a palavra reservada "not",
   "Invert" é o operador "~".

      >>> print(ast.dump(ast.parse('not x', mode='eval'), indent=4))
      Expression(
          body=UnaryOp(
              op=Not(),
              operand=Name(id='x')))

class ast.BinOp(left, op, right)

   Uma operação binária (como adição ou divisão). "op" é o operador, e
   "left" e "right" são quaisquer nós de expressão.

      >>> print(ast.dump(ast.parse('x + y', mode='eval'), indent=4))
      Expression(
          body=BinOp(
              left=Name(id='x'),
              op=Add(),
              right=Name(id='y')))

class ast.Add
class ast.Sub
class ast.Mult
class ast.Div
class ast.FloorDiv
class ast.Mod
class ast.Pow
class ast.LShift
class ast.RShift
class ast.BitOr
class ast.BitXor
class ast.BitAnd
class ast.MatMult

   Tokens de operador binário.

class ast.BoolOp(op, values)

   Uma operação booleana, 'or' ou 'and'. "op" é "Or" ou "And".
   "values" são os valores envolvidos. Operações consecutivas com o
   mesmo operador, como "a or b or c", são recolhidas em um nó com
   vários valores.

   Isso não inclui "not", que é um "UnaryOp".

      >>> print(ast.dump(ast.parse('x or y', mode='eval'), indent=4))
      Expression(
          body=BoolOp(
              op=Or(),
              values=[
                  Name(id='x'),
                  Name(id='y')]))

class ast.And
class ast.Or

   Tokens de operador booleano.

class ast.Compare(left, ops, comparators)

   Uma comparação de dois ou mais valores. "left" é o primeiro valor
   na comparação, "ops" a lista de operadores e "comparators" a lista
   de valores após o primeiro elemento na comparação.

      >>> print(ast.dump(ast.parse('1 <= a < 10', mode='eval'), indent=4))
      Expression(
          body=Compare(
              left=Constant(value=1),
              ops=[
                  LtE(),
                  Lt()],
              comparators=[
                  Name(id='a'),
                  Constant(value=10)]))

class ast.Eq
class ast.NotEq
class ast.Lt
class ast.LtE
class ast.Gt
class ast.GtE
class ast.Is
class ast.IsNot
class ast.In
class ast.NotIn

   Tokens de operador de comparação.

class ast.Call(func, args, keywords)

   Uma chamada de função. "func" é a função, que geralmente será um
   objeto "Name" ou "Attribute". Dos argumentos:

   * "args" contém uma lista dos argumentos passados por posição.

   * "keywords" contém uma lista de objetos "keyword" representando
     argumentos passados como nomeados.

   Os argumentos "args" e "keywords" são opcionais e padrão para
   listas vazias.

      >>> print(ast.dump(ast.parse('func(a, b=c, *d, **e)', mode='eval'), indent=4))
      Expression(
          body=Call(
              func=Name(id='func'),
              args=[
                  Name(id='a'),
                  Starred(
                      value=Name(id='d'))],
              keywords=[
                  keyword(
                      arg='b',
                      value=Name(id='c')),
                  keyword(
                      value=Name(id='e'))]))

class ast.keyword(arg, value)

   Um argumento nomeado para uma chamada de função ou definição de
   classe. "arg" é uma string bruta do nome do parâmetro, "value" é um
   nó para passar.

class ast.IfExp(test, body, orelse)

   Uma expressão como "a if b else c". Cada campo contém um único nó,
   portanto, no exemplo a seguir, todos os três são nós "Name".

      >>> print(ast.dump(ast.parse('a if b else c', mode='eval'), indent=4))
      Expression(
          body=IfExp(
              test=Name(id='b'),
              body=Name(id='a'),
              orelse=Name(id='c')))

class ast.Attribute(value, attr, ctx)

   Acesso a atributo como, por exemplo, "d.keys". "value" é um nó,
   normalmente um "Name". "attr" é uma string simples fornecendo o
   nome do atributo, e "ctx" é "Load", "Store" ou "Del" de acordo com
   como o atributo é acionado sobre.

      >>> print(ast.dump(ast.parse('snake.colour', mode='eval'), indent=4))
      Expression(
          body=Attribute(
              value=Name(id='snake'),
              attr='colour'))

class ast.NamedExpr(target, value)

   Uma expressão nomeada. Este nó de AST é produzido pelo operador de
   expressões de atribuição (também conhecido como operador morsa). Ao
   contrário do nó "Assign" no qual o primeiro argumento pode ser
   múltiplos nós, neste caso ambos "target" e "value" devem ser nós
   únicos.

      >>> print(ast.dump(ast.parse('(x := 4)', mode='eval'), indent=4))
      Expression(
          body=NamedExpr(
              target=Name(id='x', ctx=Store()),
              value=Constant(value=4)))

   Adicionado na versão 3.8.


Subscrição
~~~~~~~~~~

class ast.Subscript(value, slice, ctx)

   Um subscrito, como "l[1]". "value" é o objeto subscrito (geralmente
   sequência ou mapeamento). "slice" é um índice, fatia ou chave. Pode
   ser uma "Tuple" e conter uma "Slice". "ctx" é "Load", "Store" ou
   "Del" de acordo com a ação realizada com o subscrito.

      >>> print(ast.dump(ast.parse('l[1:2, 3]', mode='eval'), indent=4))
      Expression(
          body=Subscript(
              value=Name(id='l'),
              slice=Tuple(
                  elts=[
                      Slice(
                          lower=Constant(value=1),
                          upper=Constant(value=2)),
                      Constant(value=3)])))

class ast.Slice(lower, upper, step)

   Fatiamento regular (no formato "lower:upper" ou
   "lower:upper:step"). Pode ocorrer apenas dentro do campo *slice* de
   "Subscript", diretamente ou como um elemento de "Tuple".

      >>> print(ast.dump(ast.parse('l[1:2]', mode='eval'), indent=4))
      Expression(
          body=Subscript(
              value=Name(id='l'),
              slice=Slice(
                  lower=Constant(value=1),
                  upper=Constant(value=2))))


Compreensões
~~~~~~~~~~~~

class ast.ListComp(elt, generators)
class ast.SetComp(elt, generators)
class ast.GeneratorExp(elt, generators)
class ast.DictComp(key, value, generators)

   Lista e define compreensões, expressões geradoras e compreensões de
   dicionário. "elt" (ou "key" e "value") é um único nó que representa
   a parte que será avaliada para cada item.

   Para compreensões de dicionário que utilizam desempacotamento, por
   exemplo "{**item for item in items}", a expressão a ser expandida
   fica na posição da "key" (chave), e o "value" (valor) é "None".

   "generators" é uma lista de nós de "comprehension".

      >>> print(ast.dump(
      ...     ast.parse('[x for x in numbers]', mode='eval'),
      ...     indent=4,
      ... ))
      Expression(
          body=ListComp(
              elt=Name(id='x'),
              generators=[
                  comprehension(
                      target=Name(id='x', ctx=Store()),
                      iter=Name(id='numbers'),
                      is_async=0)]))
      >>> print(ast.dump(
      ...     ast.parse('{x: x**2 for x in numbers}', mode='eval'),
      ...     indent=4,
      ... ))
      Expression(
          body=DictComp(
              key=Name(id='x'),
              value=BinOp(
                  left=Name(id='x'),
                  op=Pow(),
                  right=Constant(value=2)),
              generators=[
                  comprehension(
                      target=Name(id='x', ctx=Store()),
                      iter=Name(id='numbers'),
                      is_async=0)]))
      >>> print(ast.dump(
      ...     ast.parse('{x for x in numbers}', mode='eval'),
      ...     indent=4,
      ... ))
      Expression(
          body=SetComp(
              elt=Name(id='x'),
              generators=[
                  comprehension(
                      target=Name(id='x', ctx=Store()),
                      iter=Name(id='numbers'),
                      is_async=0)]))

class ast.comprehension(target, iter, ifs, is_async)

   Uma cláusula "for" em uma compreensão. "target" é a referência a
   ser usada para cada elemento - normalmente um nó "Name" ou "Tuple".
   "iter" é o objeto sobre o qual iterar. "ifs" é uma lista de
   expressões de teste: cada cláusula "for" pode ter múltiplos "ifs".

   "is_async" indica que uma compreensão é assíncrona (usando um
   "async for" em vez de "for"). O valor é um número inteiro (0 ou 1).

      >>> print(ast.dump(ast.parse('[ord(c) for line in file for c in line]', mode='eval'),
      ...                indent=4)) # Várias compreensões em uma.
      Expression(
          body=ListComp(
              elt=Call(
                  func=Name(id='ord'),
                  args=[
                      Name(id='c')]),
              generators=[
                  comprehension(
                      target=Name(id='line', ctx=Store()),
                      iter=Name(id='file'),
                      is_async=0),
                  comprehension(
                      target=Name(id='c', ctx=Store()),
                      iter=Name(id='line'),
                      is_async=0)]))

      >>> print(ast.dump(ast.parse('(n**2 for n in it if n>5 if n<10)', mode='eval'),
      ...                indent=4)) # compreensão do gerador
      Expression(
          body=GeneratorExp(
              elt=BinOp(
                  left=Name(id='n'),
                  op=Pow(),
                  right=Constant(value=2)),
              generators=[
                  comprehension(
                      target=Name(id='n', ctx=Store()),
                      iter=Name(id='it'),
                      ifs=[
                          Compare(
                              left=Name(id='n'),
                              ops=[
                                  Gt()],
                              comparators=[
                                  Constant(value=5)]),
                          Compare(
                              left=Name(id='n'),
                              ops=[
                                  Lt()],
                              comparators=[
                                  Constant(value=10)])],
                      is_async=0)]))

      >>> print(ast.dump(ast.parse('[i async for i in soc]', mode='eval'),
      ...                indent=4)) # compreensão de async
      Expression(
          body=ListComp(
              elt=Name(id='i'),
              generators=[
                  comprehension(
                      target=Name(id='i', ctx=Store()),
                      iter=Name(id='soc'),
                      is_async=1)]))


Instruções
----------

class ast.Assign(targets, value, type_comment)

   Uma atribuição. "targets" é uma lista de nós e "value" é um único
   nó.

   Vários nós em "targets" representam a atribuição do mesmo valor a
   cada um. O desempacotamento é representada colocando uma "Tuple" ou
   "List" dentro de "targets".

   type_comment

      "type_comment" é uma string opcional com a anotação de tipo como
      comentário.

      >>> print(ast.dump(ast.parse('a = b = 1'), indent=4)) # Multiple assignment
      Module(
          body=[
              Assign(
                  targets=[
                      Name(id='a', ctx=Store()),
                      Name(id='b', ctx=Store())],
                  value=Constant(value=1))])

      >>> print(ast.dump(ast.parse('a,b = c'), indent=4)) # Unpacking
      Module(
          body=[
              Assign(
                  targets=[
                      Tuple(
                          elts=[
                              Name(id='a', ctx=Store()),
                              Name(id='b', ctx=Store())],
                          ctx=Store())],
                  value=Name(id='c'))])

class ast.AnnAssign(target, annotation, value, simple)

   Uma atribuição com uma anotação de tipo. "target" é um nó único e
   pode ser uma classe "Name", "Attribute" ou "Subscript".
   "annotation" é a anotação, como um nó "Constant" ou "Name". "value"
   é um único nó opcional.

   "simple" é sempre 0 (indicando um alvo "complexo") ou 1 (indicando
   um alvo "simples"). Um alvo "simples" consiste apenas em um nó
   "Name" que não aparece entre parênteses; todos os outros alvos são
   considerados complexos. Apenas alvos simples aparecem no dicionário
   "__annotations__" de módulos e classes.

      >>> print(ast.dump(ast.parse('c: int'), indent=4))
      Module(
          body=[
              AnnAssign(
                  target=Name(id='c', ctx=Store()),
                  annotation=Name(id='int'),
                  simple=1)])

      >>> print(ast.dump(ast.parse('(a): int = 1'), indent=4)) # Annotation with parenthesis
      Module(
          body=[
              AnnAssign(
                  target=Name(id='a', ctx=Store()),
                  annotation=Name(id='int'),
                  value=Constant(value=1),
                  simple=0)])

      >>> print(ast.dump(ast.parse('a.b: int'), indent=4)) # Attribute annotation
      Module(
          body=[
              AnnAssign(
                  target=Attribute(
                      value=Name(id='a'),
                      attr='b',
                      ctx=Store()),
                  annotation=Name(id='int'),
                  simple=0)])

      >>> print(ast.dump(ast.parse('a[1]: int'), indent=4)) # Subscript annotation
      Module(
          body=[
              AnnAssign(
                  target=Subscript(
                      value=Name(id='a'),
                      slice=Constant(value=1),
                      ctx=Store()),
                  annotation=Name(id='int'),
                  simple=0)])

class ast.AugAssign(target, op, value)

   Atribuição aumentada, como "a += 1". No exemplo a seguir, "target"
   é um nó "Name" para "x" (com o contexto "Store"), "op" é "Add", e
   "value" é uma "Constant" com valor para 1.

   O atributo "target" não pode ser da classe "Tuple" ou "List",
   diferentemente dos alvos de "Assign".

      >>> print(ast.dump(ast.parse('x += 2'), indent=4))
      Module(
          body=[
              AugAssign(
                  target=Name(id='x', ctx=Store()),
                  op=Add(),
                  value=Constant(value=2))])

class ast.Raise(exc, cause)

   Uma instrução "raise". "exc" é o objeto de exceção a ser levantado,
   normalmente uma "Call" ou "Name", ou "None" para um "raise"
   independente. "cause" é a parte opcional para "y" em "raise x from
   y".

      >>> print(ast.dump(ast.parse('raise x from y'), indent=4))
      Module(
          body=[
              Raise(
                  exc=Name(id='x'),
                  cause=Name(id='y'))])

class ast.Assert(test, msg)

   Uma asserção. "test" contém a condição, como um nó "Compare". "msg"
   contém a mensagem de falha.

      >>> print(ast.dump(ast.parse('assert x,y'), indent=4))
      Module(
          body=[
              Assert(
                  test=Name(id='x'),
                  msg=Name(id='y'))])

class ast.Delete(targets)

   Representa uma instrução "del". "targets" é uma lista de nós, como
   nós "Name", "Attribute" ou "Subscript".

      >>> print(ast.dump(ast.parse('del x,y,z'), indent=4))
      Module(
          body=[
              Delete(
                  targets=[
                      Name(id='x', ctx=Del()),
                      Name(id='y', ctx=Del()),
                      Name(id='z', ctx=Del())])])

class ast.Pass

   Uma instrução "pass".

      >>> print(ast.dump(ast.parse('pass'), indent=4))
      Module(
          body=[
              Pass()])

class ast.TypeAlias(name, type_params, value)

   Um apelido de tipo criado através da instrução "type". "name" é o
   nome do apelido, "type_params" é uma lista de parâmetros de tipo, e
   "value" é o valor do apelido do tipo.

      >>> print(ast.dump(ast.parse('type Alias = int'), indent=4))
      Module(
          body=[
              TypeAlias(
                  name=Name(id='Alias', ctx=Store()),
                  value=Name(id='int'))])

   Adicionado na versão 3.12.

Outras instruções que são aplicáveis apenas dentro de funções ou laços
são descritas em outras seções.


Importações
~~~~~~~~~~~

class ast.Import(names)

   Uma instrução de importação. "names" é uma lista de nós de "alias".

      >>> print(ast.dump(ast.parse('import x,y,z'), indent=4))
      Module(
          body=[
              Import(
                  names=[
                      alias(name='x'),
                      alias(name='y'),
                      alias(name='z')],
                  is_lazy=0)])

class ast.ImportFrom(module, names, level)

   Representa "from x import y". "module" é uma string bruta do nome
   'from', sem quaisquer pontos iniciais, ou "None" para instruções
   como "from . import foo". "level" é um número inteiro que contém o
   nível da importação relativa (0 significa importação absoluta).

      >>> print(ast.dump(ast.parse('from y import x,y,z'), indent=4))
      Module(
          body=[
              ImportFrom(
                  module='y',
                  names=[
                      alias(name='x'),
                      alias(name='y'),
                      alias(name='z')],
                  level=0,
                  is_lazy=0)])

class ast.alias(name, asname)

   Ambos os parâmetros são strings brutas dos nomes. "asname" pode ser
   "None" se o nome normal for usado.

      >>> print(ast.dump(ast.parse('from ..foo.bar import a as b, c'), indent=4))
      Module(
          body=[
              ImportFrom(
                  module='foo.bar',
                  names=[
                      alias(name='a', asname='b'),
                      alias(name='c')],
                  level=2,
                  is_lazy=0)])


Fluxo de controle
-----------------

Nota:

  Cláusulas opcionais como "else" são armazenadas como uma lista vazia
  se não estiverem presentes.

class ast.If(test, body, orelse)

   Uma instrução "if". "test" contém um único nó, como um nó
   "Compare". "body" e "orelse" contêm, cada um, uma lista de nós.

   As cláusulas "elif" não têm uma representação especial no AST, mas
   aparecem como nós extras de "If" dentro da seção "orelse" da
   cláusula anterior.

      >>> print(ast.dump(ast.parse("""
      ... if x:
      ...    ...
      ... elif y:
      ...    ...
      ... else:
      ...    ...
      ... """), indent=4))
      Module(
          body=[
              If(
                  test=Name(id='x'),
                  body=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  orelse=[
                      If(
                          test=Name(id='y'),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))],
                          orelse=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

class ast.For(target, iter, body, orelse, type_comment)

   Um laço "for". "target" contém as variáveis às quais o laço
   atribui, como um único nó de "Name", "Tuple", "List", "Attribute"
   ou "Subscript". "iter" contém o item a ser repetido, novamente como
   um único nó. "body" e "orelse" contêm listas de nós para executar.
   Aqueles em "orelse" são executados se o laço terminar normalmente,
   ao invés de através de uma instrução "break".

   type_comment

      "type_comment" é uma string opcional com a anotação de tipo como
      comentário.

      >>> print(ast.dump(ast.parse("""
      ... for x in y:
      ...     ...
      ... else:
      ...     ...
      ... """), indent=4))
      Module(
          body=[
              For(
                  target=Name(id='x', ctx=Store()),
                  iter=Name(id='y'),
                  body=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  orelse=[
                      Expr(
                          value=Constant(value=Ellipsis))])])

class ast.While(test, body, orelse)

   Um laço "while". "test" contém a condição, como um nó de "Compare".

      >>> print(ast.dump(ast.parse("""
      ... while x:
      ...    ...
      ... else:
      ...    ...
      ... """), indent=4))
      Module(
          body=[
              While(
                  test=Name(id='x'),
                  body=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  orelse=[
                      Expr(
                          value=Constant(value=Ellipsis))])])

class ast.Break
class ast.Continue

   As instruções "break" e "continue".

      >>> print(ast.dump(ast.parse("""\
      ... for a in b:
      ...     if a > 5:
      ...         break
      ...     else:
      ...         continue
      ...
      ... """), indent=4))
      Module(
          body=[
              For(
                  target=Name(id='a', ctx=Store()),
                  iter=Name(id='b'),
                  body=[
                      If(
                          test=Compare(
                              left=Name(id='a'),
                              ops=[
                                  Gt()],
                              comparators=[
                                  Constant(value=5)]),
                          body=[
                              Break()],
                          orelse=[
                              Continue()])])])

class ast.Try(body, handlers, orelse, finalbody)

   Blocos "try". Todos os atributos são uma lista de nós a serem
   executados, exceto "handlers", que é uma lista de nós de
   "ExceptHandler".

      >>> print(ast.dump(ast.parse("""
      ... try:
      ...    ...
      ... except Exception:
      ...    ...
      ... except OtherException as e:
      ...    ...
      ... else:
      ...    ...
      ... finally:
      ...    ...
      ... """), indent=4))
      Module(
          body=[
              Try(
                  body=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  handlers=[
                      ExceptHandler(
                          type=Name(id='Exception'),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      ExceptHandler(
                          type=Name(id='OtherException'),
                          name='e',
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])],
                  orelse=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  finalbody=[
                      Expr(
                          value=Constant(value=Ellipsis))])])

class ast.TryStar(body, handlers, orelse, finalbody)

   Blocos "try" que são seguidos por cláusulas "except*". Os atributos
   são os mesmos de "Try", mas os nós "ExceptHandler" em "handlers"
   são interpretados como blocos "except*" em vez de "except".

      >>> print(ast.dump(ast.parse("""
      ... try:
      ...    ...
      ... except* Exception:
      ...    ...
      ... """), indent=4))
      Module(
          body=[
              TryStar(
                  body=[
                      Expr(
                          value=Constant(value=Ellipsis))],
                  handlers=[
                      ExceptHandler(
                          type=Name(id='Exception'),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Adicionado na versão 3.11.

class ast.ExceptHandler(type, name, body)

   Uma única cláusula "except". "type" é o tipo de exceção que irá
   corresponder, normalmente um nó de "Name" (ou "None" para uma
   cláusula abrangente "except:"). "name" é uma string bruta para o
   nome conter a exceção, ou "None" se a cláusula não tiver "as foo".
   "body" é uma lista de nós.

      >>> print(ast.dump(ast.parse("""\
      ... try:
      ...     a + 1
      ... except TypeError:
      ...     pass
      ... """), indent=4))
      Module(
          body=[
              Try(
                  body=[
                      Expr(
                          value=BinOp(
                              left=Name(id='a'),
                              op=Add(),
                              right=Constant(value=1)))],
                  handlers=[
                      ExceptHandler(
                          type=Name(id='TypeError'),
                          body=[
                              Pass()])])])

class ast.With(items, body, type_comment)

   Um bloco "with". "items" é uma lista de nós "withitem"
   representando os gerenciadores de contexto, e "body" é o bloco
   indentado dentro do contexto.

   type_comment

      "type_comment" é uma string opcional com a anotação de tipo como
      comentário.

class ast.withitem(context_expr, optional_vars)

   Um único gerenciador de contexto em um bloco "with". "context_expr"
   é o gerenciador de contexto, geralmente um nó de "Call".
   "optional_vars" é um "Name", "Tuple" ou "List" para a parte "as
   foo", ou "None" se não for usado.

      >>> print(ast.dump(ast.parse("""\
      ... with a as b, c as d:
      ...    something(b, d)
      ... """), indent=4))
      Module(
          body=[
              With(
                  items=[
                      withitem(
                          context_expr=Name(id='a'),
                          optional_vars=Name(id='b', ctx=Store())),
                      withitem(
                          context_expr=Name(id='c'),
                          optional_vars=Name(id='d', ctx=Store()))],
                  body=[
                      Expr(
                          value=Call(
                              func=Name(id='something'),
                              args=[
                                  Name(id='b'),
                                  Name(id='d')]))])])


Correspondência de padrões
--------------------------

class ast.Match(subject, cases)

   Uma instrução "match". "subject" contém o assunto da
   correspondência (o objeto que está sendo comparado com os casos) e
   "cases" contém um iterável de nós de "match_case" com os diferentes
   casos.

   Adicionado na versão 3.10.

class ast.match_case(pattern, guard, body)

   Um padrão de caso único em uma instrução "match". "pattern" contém
   o padrão de correspondência com o qual o assunto será comparado.
   Observe que os nós "AST" produzidos para padrões diferem daqueles
   produzidos para expressões, mesmo quando compartilham a mesma
   sintaxe.

   O atributo "guard" contém uma expressão que será avaliada se o
   padrão corresponder ao assunto.

   "body" contém uma lista de nós a serem executados se o padrão
   corresponder e o resultado da avaliação da expressão de guarda for
   verdadeiro.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case [x] if x>0:
      ...         ...
      ...     case tuple():
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x'),
                  cases=[
                      match_case(
                          pattern=MatchSequence(
                              patterns=[
                                  MatchAs(name='x')]),
                          guard=Compare(
                              left=Name(id='x'),
                              ops=[
                                  Gt()],
                              comparators=[
                                  Constant(value=0)]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      match_case(
                          pattern=MatchClass(
                              cls=Name(id='tuple')),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Adicionado na versão 3.10.

class ast.MatchValue(value)

   Um literal de correspondência ou padrão de valor que é comparado
   por igualdade. "value" é um nó de expressão. Os nós de valor
   permitido são restritos conforme descrito na documentação da
   instrução de correspondência. Este padrão será bem-sucedido se o
   assunto da correspondência for igual ao valor avaliado.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case "Relevant":
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x'),
                  cases=[
                      match_case(
                          pattern=MatchValue(
                              value=Constant(value='Relevant')),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Adicionado na versão 3.10.

class ast.MatchSingleton(value)

   Um padrão literal de correspondência que compara por identidade.
   "value" é o singleton a ser comparado com: "None", "True" ou
   "False". Este padrão será bem-sucedido se o assunto da
   correspondência for a constante fornecida.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case None:
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x'),
                  cases=[
                      match_case(
                          pattern=MatchSingleton(value=None),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Adicionado na versão 3.10.

class ast.MatchSequence(patterns)

   Um padrão de sequência de correspondência. "patterns" contém os
   padrões a serem comparados aos elementos do assunto se o assunto
   for uma sequência. Corresponde a uma sequência de comprimento
   variável se um dos subpadrões for um nó "MatchStar", caso contrário
   corresponde a uma sequência de comprimento fixo.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case [1, 2]:
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x'),
                  cases=[
                      match_case(
                          pattern=MatchSequence(
                              patterns=[
                                  MatchValue(
                                      value=Constant(value=1)),
                                  MatchValue(
                                      value=Constant(value=2))]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Adicionado na versão 3.10.

class ast.MatchStar(name)

   Corresponde ao restante da sequência em um padrão de sequência de
   correspondência de comprimento variável. Se "name" não for "None",
   uma lista contendo os elementos restantes da sequência será
   vinculada a esse nome se o padrão de sequência geral for bem-
   sucedido.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case [1, 2, *rest]:
      ...         ...
      ...     case [*_]:
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x'),
                  cases=[
                      match_case(
                          pattern=MatchSequence(
                              patterns=[
                                  MatchValue(
                                      value=Constant(value=1)),
                                  MatchValue(
                                      value=Constant(value=2)),
                                  MatchStar(name='rest')]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      match_case(
                          pattern=MatchSequence(
                              patterns=[
                                  MatchStar()]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Adicionado na versão 3.10.

class ast.MatchMapping(keys, patterns, rest)

   Um padrão de mapeamento de correspondência. "keys" é uma sequência
   de nós de expressão. "patterns" é uma sequência correspondente de
   nós padrão. "rest" é um nome opcional que pode ser especificado
   para capturar os elementos restantes do mapeamento. As expressões-
   chave permitidas são restritas conforme descrito na documentação da
   instrução match.

   Este padrão será bem-sucedido se o assunto for um mapeamento, todas
   as expressões-chave avaliadas estiverem presentes no mapeamento e o
   valor correspondente a cada chave corresponder ao subpadrão
   correspondente. Se "rest" não for "None", um dict contendo os
   elementos de mapeamento restantes será vinculado a esse nome se o
   padrão de mapeamento geral for bem-sucedido.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case {1: _, 2: _}:
      ...         ...
      ...     case {**rest}:
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x'),
                  cases=[
                      match_case(
                          pattern=MatchMapping(
                              keys=[
                                  Constant(value=1),
                                  Constant(value=2)],
                              patterns=[
                                  MatchAs(),
                                  MatchAs()]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      match_case(
                          pattern=MatchMapping(rest='rest'),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Adicionado na versão 3.10.

class ast.MatchClass(cls, patterns, kwd_attrs, kwd_patterns)

   Um padrão de classe de correspondência. "cls" é uma expressão que
   fornece a classe nominal a ser correspondida. "patterns" é uma
   sequência de nós padrão a serem comparados com a sequência definida
   pela classe de atributos de correspondência de padrões. "kwd_attrs"
   é uma sequência de atributos adicionais a serem correspondidos
   (especificados como argumentos nomeados no padrão de classe),
   "kwd_patterns" são os padrões correspondentes (especificados como
   valores de argumentos nomeados no padrão de classe).

   Esse padrão será bem-sucedido se o assunto for uma instância da
   classe indicada, todos os padrões posicionais corresponderem aos
   atributos correspondentes definidos pela classe e quaisquer
   atributos, passados como argumentos nomeados, especificados
   corresponderem ao seu padrão correspondente.

   Nota: as classes podem definir uma propriedade que retorna self
   para corresponder um nó padrão à instância que está sendo
   correspondida. Vários tipos internos também são combinados dessa
   forma, conforme descrito na documentação da instrução match.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case Point2D(0, 0):
      ...         ...
      ...     case Point3D(x=0, y=0, z=0):
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x'),
                  cases=[
                      match_case(
                          pattern=MatchClass(
                              cls=Name(id='Point2D'),
                              patterns=[
                                  MatchValue(
                                      value=Constant(value=0)),
                                  MatchValue(
                                      value=Constant(value=0))]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      match_case(
                          pattern=MatchClass(
                              cls=Name(id='Point3D'),
                              kwd_attrs=[
                                  'x',
                                  'y',
                                  'z'],
                              kwd_patterns=[
                                  MatchValue(
                                      value=Constant(value=0)),
                                  MatchValue(
                                      value=Constant(value=0)),
                                  MatchValue(
                                      value=Constant(value=0))]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Adicionado na versão 3.10.

class ast.MatchAs(pattern, name)

   Uma correspondência "como padrão", padrão de captura ou padrão
   curinga. "pattern" contém o padrão de correspondência com o qual o
   assunto será comparado. Se o padrão for "None", o nó representa um
   padrão de captura (ou seja, um nome simples) e sempre terá sucesso.

   O atributo "name" contém o nome que será vinculado se o padrão for
   bem-sucedido. Se "name" for "None", "pattern" também deverá ser
   "None" e o nó representa o padrão curinga.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case [x] as y:
      ...         ...
      ...     case _:
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x'),
                  cases=[
                      match_case(
                          pattern=MatchAs(
                              pattern=MatchSequence(
                                  patterns=[
                                      MatchAs(name='x')]),
                              name='y'),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))]),
                      match_case(
                          pattern=MatchAs(),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Adicionado na versão 3.10.

class ast.MatchOr(patterns)

   Uma correspondência de "padrão ou". Um "padrão ou" corresponde cada
   um de seus subpadrões com o assunto, até que um seja bem-sucedido.
   O "padrão ou" é então considerado bem-sucedido. Se nenhum dos
   subpadrões for bem-sucedido, o padrão or falhará. O atributo
   "patterns" contém uma lista de nós de padrões de correspondência
   que serão comparados com o assunto.

      >>> print(ast.dump(ast.parse("""
      ... match x:
      ...     case [x] | (y):
      ...         ...
      ... """), indent=4))
      Module(
          body=[
              Match(
                  subject=Name(id='x'),
                  cases=[
                      match_case(
                          pattern=MatchOr(
                              patterns=[
                                  MatchSequence(
                                      patterns=[
                                          MatchAs(name='x')]),
                                  MatchAs(name='y')]),
                          body=[
                              Expr(
                                  value=Constant(value=Ellipsis))])])])

   Adicionado na versão 3.10.


Anotações de tipos
------------------

class ast.TypeIgnore(lineno, tag)

   Um comentário "# type: ignore" localizado em *lineno*. *tag* é a
   tag opcional especificada pelo formato "# type: ignore <tag>".

      >>> print(ast.dump(ast.parse('x = 1 # type: ignore', type_comments=True), indent=4))
      Module(
          body=[
              Assign(
                  targets=[
                      Name(id='x', ctx=Store())],
                  value=Constant(value=1))],
          type_ignores=[
              TypeIgnore(lineno=1, tag='')])
      >>> print(ast.dump(ast.parse('x: bool = 1 # type: ignore[assignment]', type_comments=True), indent=4))
      Module(
          body=[
              AnnAssign(
                  target=Name(id='x', ctx=Store()),
                  annotation=Name(id='bool'),
                  value=Constant(value=1),
                  simple=1)],
          type_ignores=[
              TypeIgnore(lineno=1, tag='[assignment]')])

   Nota:

     Os nós "TypeIgnore" não são gerados quando o parâmetro
     *type_comments* está definido como "False" (padrão). Consulte
     "ast.parse()" para obter mais detalhes.

   Adicionado na versão 3.8.


Parâmetros de tipo
------------------

Parâmetros de tipo podem existir em classes, funções e apelidos de
tipo.

class ast.TypeVar(name, bound, default_value)

   Uma "typing.TypeVar". "name" é o nome da variável de tipo. "bound"
   é o limite ou as restrições, se houver. Se "bound" for uma "Tuple",
   ele representa restrições; caso contrário, representa o limite.
   "default_value" é o valor padrão; se "TypeVar" não tiver padrão,
   este atributo será definido como "None".

      >>> print(ast.dump(ast.parse("type Alias[T: int = bool] = list[T]"), indent=4))
      Module(
          body=[
              TypeAlias(
                  name=Name(id='Alias', ctx=Store()),
                  type_params=[
                      TypeVar(
                          name='T',
                          bound=Name(id='int'),
                          default_value=Name(id='bool'))],
                  value=Subscript(
                      value=Name(id='list'),
                      slice=Name(id='T')))])

   Adicionado na versão 3.12.

   Alterado na versão 3.13: Adicionado o parâmetro *default_value*.

class ast.ParamSpec(name, default_value)

   Uma "typing.ParamSpec". "name" é o nome da especificação do
   parâmetro. "default_value" é o valor padrão; se "ParamSpec" não
   tiver padrão, este atributo será definido como "None".

      >>> print(ast.dump(ast.parse("type Alias[**P = [int, str]] = Callable[P, int]"), indent=4))
      Module(
          body=[
              TypeAlias(
                  name=Name(id='Alias', ctx=Store()),
                  type_params=[
                      ParamSpec(
                          name='P',
                          default_value=List(
                              elts=[
                                  Name(id='int'),
                                  Name(id='str')]))],
                  value=Subscript(
                      value=Name(id='Callable'),
                      slice=Tuple(
                          elts=[
                              Name(id='P'),
                              Name(id='int')])))])

   Adicionado na versão 3.12.

   Alterado na versão 3.13: Adicionado o parâmetro *default_value*.

class ast.TypeVarTuple(name, default_value)

   Uma "typing.TypeVarTuple". "name" é o nome da tupla da variável de
   tipo. "default_value" é o valor padrão; se "TypeVarTuple" não tiver
   padrão, este atributo será definido como "None".

      >>> print(ast.dump(ast.parse("type Alias[*Ts = ()] = tuple[*Ts]"), indent=4))
      Module(
          body=[
              TypeAlias(
                  name=Name(id='Alias', ctx=Store()),
                  type_params=[
                      TypeVarTuple(name='Ts', default_value=Tuple())],
                  value=Subscript(
                      value=Name(id='tuple'),
                      slice=Tuple(
                          elts=[
                              Starred(
                                  value=Name(id='Ts'))])))])

   Adicionado na versão 3.12.

   Alterado na versão 3.13: Adicionado o parâmetro *default_value*.


Definições de função e classe
-----------------------------

class ast.FunctionDef(name, args, body, decorator_list, returns, type_comment, type_params)

   Uma definição de função

   * "name" é uma string bruta do nome da função.

   * "args" é um nó "arguments".

   * "body" é a lista de nós dentro da função.

   * "decorator_list" é a lista de decoradores a serem aplicados,
     armazenados primeiro na parte externa (ou seja, o primeiro da
     lista será aplicado por último).

   * "returns" é a anotação de retorno.

   * "type_params" é uma lista de parâmetros de tipo.

   type_comment

      "type_comment" é uma string opcional com a anotação de tipo como
      comentário.

   Alterado na versão 3.12: Adicionado "type_params".

class ast.Lambda(args, body)

   "lambda" é uma definição mínima de função que pode ser usada dentro
   de uma expressão. Ao contrário de "FunctionDef", "body" contém um
   único nó.

      >>> print(ast.dump(ast.parse('lambda x,y: ...'), indent=4))
      Module(
          body=[
              Expr(
                  value=Lambda(
                      args=arguments(
                          args=[
                              arg(arg='x'),
                              arg(arg='y')]),
                      body=Constant(value=Ellipsis)))])

class ast.arguments(posonlyargs, args, vararg, kwonlyargs, kw_defaults, kwarg, defaults)

   Os argumentos para uma função.

   * "posonlyargs", "args" e "kwonlyargs" são listas de nós "arg".

   * "vararg" e "kwarg" são nós "arg" únicos, referindo-se aos
     parâmetros "*args, **kwargs".

   * "kw_defaults" é uma lista de valores padrão para argumentos
     somente-nomeados. Se um for "None", o argumento correspondente é
     necessário.

   * "defaults" é uma lista de valores padrão para argumentos que
     podem ser passados posicionalmente. Se houver menos padrões, eles
     corresponderão aos últimos n argumentos.

class ast.arg(arg, annotation, type_comment)

   Um único argumento em uma lista. "arg" é uma string bruta do nome
   do argumento; "annotation" é sua anotação, como um nó "Name".

   type_comment

      "type_comment" é uma string opcional com a anotação de tipo como
      comentário

      >>> print(ast.dump(ast.parse("""\
      ... @decorator1
      ... @decorator2
      ... def f(a: 'annotation', b=1, c=2, *d, e, f=3, **g) -> 'return annotation':
      ...     pass
      ... """), indent=4))
      Module(
          body=[
              FunctionDef(
                  name='f',
                  args=arguments(
                      args=[
                          arg(
                              arg='a',
                              annotation=Constant(value='annotation')),
                          arg(arg='b'),
                          arg(arg='c')],
                      vararg=arg(arg='d'),
                      kwonlyargs=[
                          arg(arg='e'),
                          arg(arg='f')],
                      kw_defaults=[
                          None,
                          Constant(value=3)],
                      kwarg=arg(arg='g'),
                      defaults=[
                          Constant(value=1),
                          Constant(value=2)]),
                  body=[
                      Pass()],
                  decorator_list=[
                      Name(id='decorator1'),
                      Name(id='decorator2')],
                  returns=Constant(value='return annotation'))])

class ast.Return(value)

   Uma instrução "return".

      >>> print(ast.dump(ast.parse('return 4'), indent=4))
      Module(
          body=[
              Return(
                  value=Constant(value=4))])

class ast.Yield(value)
class ast.YieldFrom(value)

   Uma expressão "yield" ou "yield from". Por serem expressões, elas
   devem ser agrupadas em um nó "Expr" se o valor enviado de volta não
   for usado.

      >>> print(ast.dump(ast.parse('yield x'), indent=4))
      Module(
          body=[
              Expr(
                  value=Yield(
                      value=Name(id='x')))])

      >>> print(ast.dump(ast.parse('yield from x'), indent=4))
      Module(
          body=[
              Expr(
                  value=YieldFrom(
                      value=Name(id='x')))])

class ast.Global(names)
class ast.Nonlocal(names)

   Instruções "global" e "nonlocal". "names" é uma lista de strings
   brutas.

      >>> print(ast.dump(ast.parse('global x,y,z'), indent=4))
      Module(
          body=[
              Global(
                  names=[
                      'x',
                      'y',
                      'z'])])

      >>> print(ast.dump(ast.parse('nonlocal x,y,z'), indent=4))
      Module(
          body=[
              Nonlocal(
                  names=[
                      'x',
                      'y',
                      'z'])])

class ast.ClassDef(name, bases, keywords, body, decorator_list, type_params)

   Uma definição de classe

   * "name" é uma string bruta para o nome da classe

   * "bases" é uma lista de nós para classes base especificadas
     explicitamente.

   * "keywords" é uma lista de nós "keyword", principalmente para
     'metaclass'. Outras argumentos nomeados serão passadas para a
     metaclasse, conforme a **PEP 3115**.

   * "body" é uma lista de nós que representam o código dentro da
     definição de classe.

   * "decorator_list" é uma lista de nós, como em "FunctionDef".

   * "type_params" é uma lista de parâmetros de tipo.

      >>> print(ast.dump(ast.parse("""\
      ... @decorator1
      ... @decorator2
      ... class Foo(base1, base2, metaclass=meta):
      ...     pass
      ... """), indent=4))
      Module(
          body=[
              ClassDef(
                  name='Foo',
                  bases=[
                      Name(id='base1'),
                      Name(id='base2')],
                  keywords=[
                      keyword(
                          arg='metaclass',
                          value=Name(id='meta'))],
                  body=[
                      Pass()],
                  decorator_list=[
                      Name(id='decorator1'),
                      Name(id='decorator2')])])

   Alterado na versão 3.12: Adicionado "type_params".


Async e await
-------------

class ast.AsyncFunctionDef(name, args, body, decorator_list, returns, type_comment, type_params)

   Uma definição de função "async def". Possui os mesmos campos que
   "FunctionDef".

   Alterado na versão 3.12: Adicionado "type_params".

class ast.Await(value)

   Uma expressão "await". "value" é o que ela espera. Válido apenas no
   corpo de um "AsyncFunctionDef".

   >>> print(ast.dump(ast.parse("""\
   ... async def f():
   ...     await other_func()
   ... """), indent=4))
   Module(
       body=[
           AsyncFunctionDef(
               name='f',
               args=arguments(),
               body=[
                   Expr(
                       value=Await(
                           value=Call(
                               func=Name(id='other_func'))))])])

class ast.AsyncFor(target, iter, body, orelse, type_comment)
class ast.AsyncWith(items, body, type_comment)

   Laços "async for" e gerenciadores de contexto "async with". Eles
   têm os mesmos campos que "For" e "With", respectivamente. Válido
   apenas no corpo de "AsyncFunctionDef".

Nota:

  Quando uma string é analisada por "ast.parse()", os nós operadores
  (subclasses de "ast.operator", "ast.unaryop", "ast.cmpop",
  "ast.boolop" e "ast.expr_context") na árvore retornada serão
  singletons. As alterações em um serão refletidas em todas as outras
  ocorrências do mesmo valor (por exemplo, "ast.Add").


Auxiliares de "ast"
===================

Além das classes de nós, o módulo "ast" define essas funções e classes
utilitárias para percorrer árvores de sintaxe abstrata:

ast.parse(source, filename='<unknown>', mode='exec', *, type_comments=False, feature_version=None, optimize=-1, module=None)

   Analisa a fonte como um nó AST. Equivalente a "compile(source,
   filename, mode, flags=FLAGS_VALUE, optimize=optimize,
   module=module)", onde "FLAGS_VALUE" é "ast.PyCF_ONLY_AST" se
   "optimize <= 0" e "ast.PyCF_OPTIMIZED_AST" caso contrário.

   Se "type_comments=True" é fornecido, o analisador é modificado para
   verificar e retornar comentários do tipo, conforme especificado por
   **PEP 484** e **PEP 526**. Isso é equivalente a adicionar
   "ast.PyCF_TYPE_COMMENTS" aos sinalizadores passados para
   "compile()". Isso relatará erros de sintaxe para comentários do
   tipo extraviado. Sem esse sinalizador, os comentários do tipo serão
   ignorados e o campo "type_comment" nos nós AST selecionados sempre
   será "None". Além disso, os locais dos comentários "# type: ignore"
   serão retornados como o atributo "type_ignores" de "Module" (caso
   contrário, é sempre uma lista vazia).

   Além disso, se "mode" for "'func_type'", a sintaxe de entrada é
   modificada para corresponder a "comentários de tipo de assinatura"
   de **PEP 484**, por exemplo, "(str, int) -> List[str]".

   Definir "feature_version" como uma tupla "(major, minor)" resultará
   em uma tentativa de "melhor esforço" de análise usando a gramática
   daquela versão do Python. Por exemplo, definir "feature_version=(3,
   9)" tentará proibir a análise de instruções "match". Atualmente
   "major" deve ser igual a "3". A versão mais baixa suportada é "(3,
   7)" (e isso pode aumentar em versões futuras do Python); o mais
   alto é "sys.version_info[0:2]". A tentativa de "melhor esforço"
   significa que não há garantia de que a análise (ou sucesso da
   análise) seja a mesma que quando executada na versão Python
   correspondente a "feature_version".

   Se a fonte contém um caractere nulo ("\0"), "ValueError" é
   levantada.

   Aviso:

     Observe que a análise bem-sucedida do código-fonte em um objeto
     AST não garante que o código-fonte fornecido seja um código
     Python válido que pode ser executado, pois a etapa de compilação
     pode levantar mais exceções "SyntaxError". Por exemplo, a fonte
     "return 42" gera um nó AST válido para uma instrução return, mas
     não pode ser compilado sozinho (precisa estar dentro de um nó de
     função).Em particular, "ast.parse()" não fará nenhuma verificação
     de escopo, o que a etapa de compilação faz.

   Aviso:

     É possível travar o interpretador Python com uma string
     suficientemente grande/complexa devido às limitações de
     profundidade da pilha no compilador de AST do Python.

   Alterado na versão 3.8: Adicionado "type_comments",
   "mode='func_type'" e "feature_version".

   Alterado na versão 3.13: A versão mínima suportada para
   "feature_version" agora é "(3, 7)". O argumento "optimize" foi
   adicionado.

   Adicionado na versão 3.15: Adicionado o parâmetro *module*.

ast.unparse(ast_obj)

   Desfaz análise de um objeto "ast.AST" e gera uma string com código
   que produziria um objeto "ast.AST" equivalente se analisado
   novamente com "ast.parse()".

   Aviso:

     A string de código produzida não será necessariamente igual ao
     código original que gerou o objeto "ast.AST" (sem quaisquer
     otimizações do compilador, como tuplas/frozensets constantes).

   Aviso:

     Tentar desfazer análise de uma expressão altamente complexa
     resultaria em "RecursionError".

   Adicionado na versão 3.9.

ast.literal_eval(node_or_string)

   Avalia um nó de expressão ou uma string contendo apenas um literal
   Python ou uma exibição de contêiner. A string ou nó fornecido pode
   consistir apenas nas seguintes estruturas literais Python: strings,
   bytes, números, tuplas, listas, dicionários, conjuntos, booleanos,
   "None" e "Ellipsis".

   Isso pode ser usado para avaliar strings contendo valores Python
   sem a necessidade de analisar os valores por conta própria. Não é
   capaz de avaliar expressões arbitrariamente complexas, por exemplo,
   envolvendo operadores ou indexação.

   Esta função foi documentada como “segura” no passado sem definir o
   que isso significava. Isso foi enganoso. Isso foi projetado
   especificamente para não executar código Python, ao contrário do
   "eval()" mais geral. Não há espaço de nomes, pesquisas de nome ou
   capacidade de chamada. Mas não está livre de ataques: uma entrada
   relativamente pequena pode levar ao esgotamento da memória ou ao
   esgotamento da pilha C, travando o processo. Também existe a
   possibilidade de negação de serviço por consumo excessivo de CPU em
   algumas entradas. Portanto, não é recomendado chamá-la em dados não
   confiáveis.

   Aviso:

     É possível travar o interpretador Python devido às limitações de
     profundidade da pilha no compilador AST do Python.Pode levantar
     "ValueError", "TypeError", "SyntaxError", "MemoryError" e
     "RecursionError" dependendo da entrada malformada.

   Alterado na versão 3.2: Agora permite bytes e literais de
   conjuntos.

   Alterado na versão 3.9: Agora oferece suporte à criação de
   conjuntos vazios com "'set()'".

   Alterado na versão 3.10: Para entradas de string, os espaços
   iniciais e tabulações agora são removidos.

ast.get_docstring(node, clean=True)

   Retorna a docstring do *node* dado (que deve ser um nó
   "FunctionDef", "AsyncFunctionDef", "ClassDef" ou "Module") ou
   "None" se não tiver uma docstring. Se *clean* for verdadeiro, limpa
   o recuo da docstring com "inspect.cleandoc()".

   Alterado na versão 3.5: Não há suporte a "AsyncFunctionDef".

ast.get_source_segment(source, node, *, padded=False)

   Obtém o segmento de código-fonte do *source* que gerou o *node*. Se
   alguma informação de localização ("lineno", "end_lineno",
   "col_offset" ou "end_col_offset") está faltando, retorna "None".

   Se *padded* for "True", a primeira linha de uma instrução
   multilinha será preenchida com espaços para corresponder à sua
   posição original.

   Adicionado na versão 3.8.

ast.fix_missing_locations(node)

   Quando você compila uma árvore de nós com "compile()", o compilador
   espera atributos "lineno" e "col_offset" para cada nó que os
   suporta. Isso é tedioso para preencher nós gerados, portanto, esse
   auxiliar adiciona esses atributos recursivamente, onde ainda não
   estão definidos, definindo-os para os valores do nó pai. Ele
   funciona recursivamente a partir do *node*.

ast.increment_lineno(node, n=1)

   Incrementa o número da linhas e o número da linha final de cada nó
   na árvore começando em *node* em *n*. Isso é útil para "mover
   código" para um local diferente em um arquivo.

ast.copy_location(new_node, old_node)

   Copia o local de origem ("lineno", "col_offset", "end_lineno" e
   "end_col_offset") de *old_node* para *new_node* se possível e,
   então, retorna *new_node*.

ast.iter_fields(node)

   Produz uma tupla de "(fieldname, value)" para cada campo em
   "node._fields" que esteja presente em *node*.

ast.iter_child_nodes(node)

   Produz todos os nós filhos diretos de *node*, ou seja, todos os
   campos que são nós e todos os itens de campos que são listas de
   nós.

ast.walk(node)

   Produz recursivamente todos os nós descendentes na árvore começando
   em *node* (incluindo o próprio *node*), em nenhuma ordem
   especificada. Isso é útil se você quiser apenas modificar nós no
   lugar e não se importar com o contexto.

class ast.NodeVisitor

   Uma classe base de visitante de nó que percorre a árvore de sintaxe
   abstrata e chama uma função de visitante para cada nó encontrado.
   Esta função pode retornar um valor que é encaminhado pelo método
   "visit()".

   Esta classe deve ser uma subclasse, com a subclasse adicionando
   métodos visitantes.

   visit(node)

      Visita um nó. A implementação padrão chama o método chamado
      "self.visit_*nomedaclasse*" sendo *nomedaclasse* o nome da
      classe do nó, ou "generic_visit()" se aquele método não existir.

   generic_visit(node)

      Este visitante chama "visit()" em todos os filhos do nó.

      Observe que nós filhos de nós que possuem um método de visitante
      personalizado não serão visitados, a menos que o visitante chame
      "generic_visit()" ou os visite por conta própria.

   visit_Constant(node)

      Manipula todos os nós constantes.

   Não use o "NodeVisitor" se você quiser aplicar mudanças nos nós
   durante a travessia. Para isso existe um visitante especial
   ("NodeTransformer") que permite modificações.

   Descontinuado desde a versão 3.8, removido na versão 3.14: Os
   métodos "visit_Num()", "visit_Str()", "visit_Bytes()",
   "visit_NameConstant()" e "visit_Ellipsis()" não serão chamados nas
   versões 3.14 e mais novas do Python. Adicione um método
   "visit_Constant()" para lidar com nós de constantes.

class ast.NodeTransformer

   A subclasse "NodeVisitor" que percorre a árvore de sintaxe abstrata
   e permite a modificação de nós.

   O "NodeTransformer" percorrerá a AST e usará o valor de retorno dos
   métodos do visitante para substituir ou remover o nó antigo. Se o
   valor de retorno do método visitante for "None", o nó será removido
   de seu local, caso contrário, ele será substituído pelo valor de
   retorno. O valor de retorno pode ser o nó original, caso em que não
   há substituição.

   Aqui está um exemplo de transformador que rescreve todas as
   ocorrências de procuras por nome ("foo") para "data['foo']":

      class RewriteName(NodeTransformer):

          def visit_Name(self, node):
              return Subscript(
                  value=Name(id='data'),
                  slice=Constant(value=node.id),
                  ctx=node.ctx
              )

   Tenha em mente que, se o nó em que você está operando tiver nós
   filhos, você deve transformar os nós filhos por conta própria ou
   chamar o método "generic_visit()" para o nó primeiro.

   Para nós que faziam parte de uma coleção de instruções (que se
   aplica a todos os nós de instrução), o visitante também pode
   retornar uma lista de nós em vez de apenas um único nó.

   Se "NodeTransformer" introduz novos nós (que não faziam parte da
   árvore original) sem fornecer informações de localização (como
   "lineno"), "fix_missing_locations()" deve ser chamado com o novo
   subárvore para recalcular as informações de localização:

      tree = ast.parse('foo', mode='eval')
      new_tree = fix_missing_locations(RewriteName().visit(tree))

   Normalmente você usa o transformador assim:

      node = YourTransformer().visit(node)

ast.dump(node, annotate_fields=True, include_attributes=False, *, color=False, indent=None, show_empty=False)

   Retorne um despejo formatado da árvore em *node*. Isso é útil
   principalmente para fins de depuração. Se *annotate_fields* for
   verdadeiro (por padrão), a sequência retornada mostrará os nomes e
   os valores para os campos. Se *annotate_fields* for falso, a
   sequência de resultados será mais compacta ao omitir nomes de
   campos não ambíguos. Atributos como números de linha e
   deslocamentos de coluna não são despejados por padrão. Se isso for
   desejado, *include_attributes* pode ser definido como verdadeiro.

   Se *color* for "True", a string retornada terá destaque de sintaxe
   usando sequências de escape ANSI. Se for "False" (o padrão), a
   saída colorida estará sempre desativada.

   Se *indent* for um inteiro não negativo ou uma string, então a
   árvore terá uma saída formatada com este nível de indentação. Um
   nível de indentação 0, negativo ou """" apenas colocará novas
   linhas. "None" (o padrão) seleciona a representação de uma única
   linha. Usando um inteiro positivo a indentação terá alguns espaços
   por nível. Se *indent* for uma string (como ""\t""), essa string
   será usada para indentar cada nível.

   Se *show_empty* for falso (o padrão), listas vazias opcionais e
   valores opcionais de "Load()" serão omitidos da saída. Valores
   opcionais "None" são sempre omitidos.

      >>> tree = ast.parse('print(None)', '?', 'eval')
      >>> print(ast.dump(tree, indent=4))
      Expression(
          body=Call(
              func=Name(id='print'),
              args=[
                  Constant(value=None)]))
      >>> print(ast.dump(tree, indent=4, show_empty=True))
      Expression(
          body=Call(
              func=Name(id='print', ctx=Load()),
              args=[
                  Constant(value=None)],
              keywords=[]))

   Alterado na versão 3.9: Adicionada a opção *indent*.

   Alterado na versão 3.13: Adicionada a opção *show_empty*.

   Alterado na versão 3.15: Omite valores opcionais de "Load()" por
   padrão.

   Alterado na versão 3.15: Adicionado o parâmetro *color*.

ast.compare(a, b, /, *, compare_attributes=False)

   Compara recursivamente duas ASTs.

   *compare_attributes* afeta se os atributos da AST são considerados
   na comparação. Se *compare_attributes* for "False" (padrão), os
   atributos serão ignorados. Caso contrário, todos devem ser iguais.
   Esta opção é útil para verificar se os ASTs são estruturalmente
   iguais, mas diferem em espaços em branco ou em detalhes
   semelhantes. Os atributos incluem números de linha e deslocamentos
   de coluna.

   Adicionado na versão 3.14.


Sinalizadores do compilador
===========================

Os seguintes sinalizadores podem ser passados para "compile()" para
alterar os efeitos na compilação de um programa:

ast.PyCF_ALLOW_TOP_LEVEL_AWAIT

   Habilita suporte para "await", "async for", "async with" e
   compreensões assíncronas de nível superior.

   Adicionado na versão 3.8.

ast.PyCF_ONLY_AST

   Gera e retorna uma árvore de sintaxe abstrata em vez de retornar um
   objeto de código compilado.

ast.PyCF_OPTIMIZED_AST

   O AST retornado é otimizado de acordo com o argumento *optimize* em
   "compile()" ou "ast.parse()".

   Adicionado na versão 3.13.

ast.PyCF_TYPE_COMMENTS

   Habilita suporte para comentários do tipo **PEP 484** e **PEP 526**
   ("# type: <type>", "# type: ignore <stuff>").

   Adicionado na versão 3.8.


Uso na linha de comando
=======================

Adicionado na versão 3.9.

Alterado na versão 3.15: A saída agora possui realce de sintaxe por
padrão. Isso pode ser controlado usando variáveis de ambiente.

O módulo "ast" pode ser executado como um script na linha de comando.
É tão simples quanto:

   python -m ast [-m <mode>] [-a] [infile]

As seguintes opções são aceitas:

-h, --help

   Mostra a mensagem de ajuda e sai.

-m <mode>
--mode <mode>

   Especifica que tipo de código deve ser compilado, como o argumento
   *mode* em "parse()".

--no-type-comments

   Não analisa comentários de tipo.

-a, --include-attributes

   Inclui atributos como números de linha e deslocamentos de colunas.

-i <indent>
--indent <indent>

   indentação de nós em AST (número de espaços).

--feature-version <version>

   Versão do Python no formato 3.x (por exemplo, 3.10). O padrão é a
   versão atual do interpretador.

   Adicionado na versão 3.14.

-O <level>
--optimize <level>

   Nível de otimização do analisador. O padrão é sem otimização.

   Adicionado na versão 3.14.

--show-empty

   Exibe listas e campos vazios com o valor "None". O padrão é não
   exibir objetos vazios.

   Adicionado na versão 3.14.

Se "infile" for especificado, seu conteúdo será analisado no AST e
despejado no stdout. Caso contrário, o conteúdo será lido em stdin.

Ver também:

  Green Tree Snakes, um recurso de documentação externo, possui bons
  detalhes sobre trabalhar com ASTs do Python.

  ASTTokens anota ASTs do Python com as posições de tokens e texto no
  código-fonte que as gerou. Isso é útil para ferramentas que fazem
  transformações de código-fonte.

  leoAst.py unifica as visualizações baseadas em token e em árvore de
  análise de programas python, inserindo links duas vias entre tokens
  e nós de ast.

  LibCST analisa o código como uma árvore de sintaxe concreta que se
  parece com uma árvore ast e mantém todos os detalhes de formatação.
  É útil para construir linters e aplicações de refatoração
  automatizada (codemod).

  Parso é um analisador Python que oferece suporte a recuperação de
  erros e análise de ida e volta para diferentes versões do Python (em
  várias versões do Python). Parso também é capaz de listar vários
  erros de sintaxe em seu arquivo Python.
