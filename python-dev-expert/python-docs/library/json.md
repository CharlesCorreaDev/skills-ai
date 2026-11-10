"json" --- Codificador e decodificador JSON
*******************************************

**Código-fonte:** Lib/json/__init__.py

======================================================================

JSON (JavaScript Object Notation), especificado pelo **RFC 7159** (que
tornou o **RFC 4627** obsoleta) e pelo ECMA-404, é um formato leve de
troca de dados inspirado pela sintaxe de objeto JavaScript (embora não
seja um subconjunto estrito de JavaScript [1]).

Nota:

  O termo "objeto" no contexto do processamento JSON em Python pode
  ser ambíguo. Todos os valores em Python são objetos. Em JSON, um
  objeto se refere a qualquer dado entre chaves, semelhante a um
  dicionário Python.

Aviso:

  Tenha cuidado quando estiver analisando dados JSON de fontes não-
  confiáveis. Uma string JSON maliciosa pode fazer o decodificador
  consumir recursos consideráveis de CPU e memória. É recomendado
  limitar o tamanho do dado a ser analisado.

Este módulo expõe uma API familiar para pessoas usuárias dos módulos
"marshal" e "pickle" da biblioteca padrão.

Codificação de hierarquias básicas de objetos Python:

   >>> import json
   >>> json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
   '["foo", {"bar": ["baz", null, 1.0, 2]}]'
   >>> print(json.dumps("\"foo\bar"))
   "\"foo\bar"
   >>> print(json.dumps('\u1234'))
   "\u1234"
   >>> print(json.dumps('\\'))
   "\\"
   >>> print(json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True))
   {"a": 0, "b": 0, "c": 0}
   >>> from io import StringIO
   >>> io = StringIO()
   >>> json.dump(['streaming API'], io)
   >>> io.getvalue()
   '["streaming API"]'

Codificação compacta:

   >>> import json
   >>> json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
   '[1,2,3,{"4":5,"6":7}]'

Saída bonita:

   >>> import json
   >>> print(json.dumps({'6': 7, '4': 5}, sort_keys=True, indent=4))
   {
       "4": 5,
       "6": 7
   }

Personalizando em codificação de objeto JSON:

   >>> import json
   >>> def custom_json(obj):
   ...     if isinstance(obj, complex):
   ...         return {'__complex__': True, 'real': obj.real, 'imag': obj.imag}
   ...     raise TypeError(f'Cannot serialize object of {type(obj)}')
   ...
   >>> json.dumps(1 + 2j, default=custom_json)
   '{"__complex__": true, "real": 1.0, "imag": 2.0}'

Decodificando JSON:

   >>> import json
   >>> json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
   ['foo', {'bar': ['baz', None, 1.0, 2]}]
   >>> json.loads('"\\"foo\\bar"')
   '"foo\x08ar'
   >>> from io import StringIO
   >>> io = StringIO('["streaming API"]')
   >>> json.load(io)
   ['streaming API']

Personalizando em decodificação de objeto JSON:

   >>> import json
   >>> def as_complex(dct):
   ...     if '__complex__' in dct:
   ...         return complex(dct['real'], dct['imag'])
   ...     return dct
   ...
   >>> json.loads('{"__complex__": true, "real": 1, "imag": 2}',
   ...     object_hook=as_complex)
   (1+2j)
   >>> import decimal
   >>> json.loads('1.1', parse_float=decimal.Decimal)
   Decimal('1.1')
   >>> json.loads('{"name": "point", "coords": [[1, 2], [3, 4]]}',
   ...     array_hook=tuple)
   {'name': 'point', 'coords': ((1, 2), (3, 4))}
   >>> json.loads('{"name": "point", "coords": [1, 2]}',
   ...     object_pairs_hook=frozendict, array_hook=tuple)
   frozendict({'name': 'point', 'coords': (1, 2)})

Estendendo "JSONEncoder":

   >>> import json
   >>> class ComplexEncoder(json.JSONEncoder):
   ...     def default(self, obj):
   ...         if isinstance(obj, complex):
   ...             return [obj.real, obj.imag]
   ...         # Let the base class default method raise the TypeError
   ...         return super().default(obj)
   ...
   >>> json.dumps(2 + 1j, cls=ComplexEncoder)
   '[2.0, 1.0]'
   >>> ComplexEncoder().encode(2 + 1j)
   '[2.0, 1.0]'
   >>> list(ComplexEncoder().iterencode(2 + 1j))
   ['[2.0', ', 1.0', ']']

Usando "json" para validar a partir do console e exibir formatado:

   $ echo '{"json":"obj"}' | python -m json
   {
       "json": "obj"
   }
   $ echo '{1.2:3.4}' | python -m json
   Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

Veja Interface de linha de comando para a documentação detalhada.

Nota:

  JSON é um subconjunto do YAML 1.2. O JSON gerado pelas definições
  padrões desse módulo (particularmente, o valor padrão dos
  *separadores*) é também um subconjunto do YAML 1.0 e 1.1. Esse
  módulo pode, portanto, também ser usado como serializador YAML.

Nota:

  O codificador e o decodificador do módulo preservam a ordem de
  entrada e saída por padrão. A ordem só é perdida se os contêineres
  subjacentes estão desordenados.


Uso básico
==========

json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

   Serializa um *obj* como um stream JSON formatado para *fp* (um
   *objeto arquivo ou similar* com suporte a ".write()") usando essa
   tabela de conversão de Python para JSON.

   Nota:

     Diferente de "pickle" e "marshal", JSON não é um protocolo com
     datagrama, assim tentar serializar múltiplos objetos com chamadas
     repetidas para "dump()" usando o mesmo *fp* resultará em um
     arquivo JSON inválido.

   Parâmetros:
      * **obj** (*object*) -- O objeto Python a ser serializado.

      * **fp** (*file-like object*) -- O objeto arquivo ou similar
        *obj* para o qual será serializado. O módulo "json" sempre
        produz objetos "str", e não objetos "bytes". Dessa forma,
        "fp.write()" precisa ter suporte para entradas "str".

      * **skipkeys** (*bool*) -- Se "True", as chaves que não forem de
        um tipo básico ("str", "int", "float", "bool", "None") serão
        ignoradas ao invés de levantar uma exceção "TypeError". Padrão
        "False".

      * **ensure_ascii** (*bool*) -- Se definido como "True" (o
        padrão), a saída terá todos os caracteres não ASCII e não
        imprimíveis recebidos escapados. Se definido como "False",
        todos os caracteres serão exibidos como estão, exceto os
        caracteres que devem ser escapados: aspas, barra invertida e
        os caracteres de controle U+0000 a U+001F.

      * **check_circular** (*bool*) -- Se "False", a verificação de
        referência circular for de tipos contêineres é ignorada e uma
        referência circular resultará em uma exceção "RecursionError"
        (ou pior). Padrão "True".

      * **allow_nan** (*bool*) -- Se "False", serialização de valores
        "float" fora de intervalo ("nan", "inf", "-inf") vai resultar
        em um "ValueError" em estrita conformidade com a
        especificação. Se "True" (o padrão), seus equivalentes
        JavaScript ("NaN", "Infinity", "-Infinity") serão usados.

      * **cls** (a "JSONEncoder" subclass) -- Se definido, um
        codificador JSON personalizado com o método "default()"
        substituído, para serializar em tipos de dados personalizados.
        Se "None" (o padrão), "JSONEncoder" é usado.

      * **indent** (*int** | **str** | **None*) -- Se for um inteiro
        positivo ou string, os elementos de array JSON e membros de
        objeto serão formatados de forma legível com esse nível de
        indentação. Um inteiro positivo indenta essa quantidade de
        espaços por nível; uma string (como ""\t"") é usada para
        indentar cada nível. Se for zero, negativo ou """" (a string
        vazia), apenas quebras de linha são inseridas. Se for "None"
        (o padrão), nenhuma quebra de linha é inserida.

      * **separators** (*tuple** | **None*) -- Uma tupla dupla:
        "(item_separator, key_separator)". Se "None" (o padrão),
        *separators* assume como padrão "(', ', ': ')" se *indent* for
        "None", e "(',', ': ')" caso contrário. Para o JSON mais
        compacto, especifique "(',', ':')" para eliminar espaços em
        branco.

      * **default** (*callable* | None) -- Uma função que é chamada
        para objetos que não podem ser serializados de outra forma.
        Ela deve retornar uma versão JSON codificável do objeto ou
        gerar um "TypeError". Se "None" (o padrão), "TypeError" é
        levantada.

      * **sort_keys** (*bool*) -- Se "True", os dicionários serão
        emitidos classificados por chave. Padrão "False".

   Nota:

     Chaves nos pares chave/valor de JSON são sempre do tipo "str".
     Quando um dicionário é convertido para JSON, todas as chaves são
     convertidas para strings. Como resultado disso, se um dicionário
     é convertido para JSON e depois de volta para um dicionário, o
     dicionário pode não ser igual ao original. Isto é,
     "loads(dumps(x)) != x" se x tem chaves não strings. *sort_keys*
     ordena as chaves antes de elas serem convertidas em strings;
     portanto, chaves numéricas são ordenadas pelo valor, e não pela
     sua representação como string.

   Alterado na versão 3.2: Permite strings para *indent*, além de
   inteiros.

   Alterado na versão 3.4: Usa "(',', ': ')" como padrão se *indent*
   não for "None".

   Alterado na versão 3.6: Todos os parâmetros opcionais agora são
   somente-nomeados.

json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

   Serializa *obj* para uma "str" com formato JSON usando essa tabela
   de conversão. Os argumentos têm o mesmo significado que na função
   "dump()".

json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, array_hook=None, **kw)

   Desserializa *fp* para um objeto Python usando a tabela de
   conversão JSON para Python.

   Parâmetros:
      * **fp** (*file-like object*) -- Um *arquivo texto* ou *arquivo
        binário* com suporte a ".read()" contendo o documento JSON a
        ser desserializado.

      * **cls** (a "JSONDecoder" subclass) -- Se definido, um
        decodificador JSON personalizado. Argumentos nomeados
        adicionais para "load()" serão passados para o construtor de
        *cls*. Se "None" (o padrão), "JSONDecoder" é usado.

      * **object_hook** (*callable* | None) -- Se definido, uma função
        que é chamada com o resultado de qualquer literal de objeto
        JSON decodificado (um "dict"). O valor de retorno desta função
        será usado em vez do "dict". Este recurso pode ser usado para
        implementar decodificadores personalizados, por exemplo dica
        de classes JSON-RPC. O padrão é "None".

      * **object_pairs_hook** (*callable* | None) -- Se definido, uma
        função que é chamada com o resultado de qualquer literal de
        objeto JSON decodificado com uma lista ordenada de pares. O
        valor de retorno desta função será usado em vez de "dict".
        Este recurso pode ser usado para implementar decodificadores
        personalizados. Se *object_hook* também for definido,
        *object_pairs_hook* terá prioridade. O padrão é "None".

      * **array_hook** (*callable* | None) -- Se definido, uma função
        que é chamada com o resultado de qualquer literal de vetor
        JSON decodificado como uma lista Python. O valor de retorno
        desta função será usado em vez de "list". Este recurso pode
        ser usado para implementar decodificadores personalizados. O
        padrão é "None".

      * **parse_float** (*callable* | None) -- Se definido, uma função
        que é chamada com a string de cada ponto flutuante JSON a ser
        decodificada. Se "None" (o padrão), é equivalente a
        "float(num_str)". Isso pode ser usado para analisar pontos
        flutuantes JSON em tipos de dados personalizados, por exemplo
        "decimal.Decimal".

      * **parse_int** (*callable* | None) -- Se definido, uma função
        que é chamada com a string de cada int JSON a ser
        decodificado. Se "None" (o padrão), é equivalente a
        "int(num_str)". Isso pode ser usado para analisar inteiros
        JSON em tipos de dados personalizados, por exemplo "float".

      * **parse_constant** (*callable* | None) -- Se definido, uma
        função que é chamada com uma das seguintes strings:
        "'-Infinity'", "'Infinity'" ou "'NaN'". Isso pode ser usado
        para levantar uma exceção se números JSON inválidos forem
        encontrados. Padrão "None".

   Levanta:
      * **JSONDecodeError** -- Quando os dados a serem desserializados
        não forem um documento JSON válido.

      * **UnicodeDecodeError** -- Quando os dados que estão sendo
        desserializados não contêm dados codificados em UTF-8, UTF-16
        ou UTF-32.

   Alterado na versão 3.1:

   * Adicionado o parâmetro opcional *object_pairs_hook*.

   * *parse_constant* não é mais chamada para 'null', 'true', 'false'.

   Alterado na versão 3.6:

   * Todos os parâmetros opcionais agora são somente-nomeados.

   * *fp* agora pode ser um *arquivo binário*. A entrada deve estar
     codificada como UTF-8, UTF-16 ou UTF-32.

   Alterado na versão 3.11: O *parse_int* padrão para  "int()" agora
   limita o tamanho máximo da string de inteiro via limitação de
   comprimento de string na conversão para inteiro do interpretador
   para ajudar a evitar ataques por negação de serviço.

   Alterado na versão 3.15: Adicionado o parâmetro opcional
   *array_hook*.

json.loads(s, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, array_hook=None, **kw)

   Idêntico a "load()", mas em vez de um objeto arquivo ou similar,
   desserializa *s* (uma instância de "str", "bytes" ou "bytearray"
   contendo um documento JSON) para um objeto Python usando essa
   tabela de conversão.

   Alterado na versão 3.6: *s* agora pode ser um do tipo "bytes" ou
   "bytearray". A entrada deve estar codificado como UTF-8, UTF-16 ou
   UTF-32.

   Alterado na versão 3.9: O argumento nomeado *encoding* foi
   removido.


Codificadores e decodificadores
===============================

class json.JSONDecoder(*, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None, array_hook=None)

   Decodificador JSON simples.

   Executa as seguintes traduções na decodificação por padrão:

   +-----------------+---------------------+
   | JSON            | Python              |
   |=================|=====================|
   | objeto          | dict                |
   +-----------------+---------------------+
   | array           | lista               |
   +-----------------+---------------------+
   | string          | str                 |
   +-----------------+---------------------+
   | número          | int                 |
   | (inteiro)       |                     |
   +-----------------+---------------------+
   | número (real)   | ponto flutuante     |
   +-----------------+---------------------+
   | true            | True                |
   +-----------------+---------------------+
   | false           | False               |
   +-----------------+---------------------+
   | null            | None                |
   +-----------------+---------------------+

   Ele também entende "NaN", "Infinity" e "-Infinity" como seus
   valores "float" correspondentes, que estão fora da especificação
   JSON.

   *object_hook* é uma função opcional que será chamada com o
   resultado de cada objeto JSON decodificado e seu valor de retorno
   será usado no lugar do dado "dict". Isso pode ser usado para
   fornecer desserializações personalizadas (por exemplo, para
   oferecer suporte a dicas de classe JSON-RPC)

   *object_pairs_hook* é uma função opcional que será chamada com o
   resultado de todo objeto JSON decodificado com uma lista ordenada
   de pares. O valor de retorno de *object_pairs_hook* será usado no
   lugar do "dict". Este recurso pode ser usado para implementar
   decodificadores personalizados. Se *object_pairs_hook* também for
   definido, o *object_pairs_hook* terá prioridade.

   Alterado na versão 3.1: Adicionado suporte para
   *object_pairs_hook*.

   *array_hook* é uma função opcional que será chamada com o resultado
   de todo vetor JSON decodificado como uma lista. O valor de retorno
   de *array_hook* será usado em vez de "list". Este recurso pode ser
   usado para implementar decodificadores personalizados.

   Alterado na versão 3.15: Adicionado suporte a *array_hook*.

   *parse_float* é uma função opcional que será chamada com a string
   de cada ponto flutuante JSON para ser decodificado. Por padrão,
   equivale a "float(num_str)". Pode ser usado para qualquer outro
   tipo de dado ou analisador de pontos flutuante JSON (por exemplo,
   "decimal.Decimal").

   *parse_int* é uma função opcional que será chamada com a string de
   cada inteiro JSON para ser decodificado. Por padrão, equivale a
   "int(num_str)". Pode ser usado para qualquer outro tipo de dado ou
   analisador de inteiros JSON (por exemplo, "float").

   *parse_constant* é uma função opcional que será chamada para cada
   um das seguintes strings: "'-Infinity'", "'Infinity'", "'NaN'".
   Isso pode ser usado para levantar uma exceção se forem encontrados
   números JSON inválidos.

   Se *strict* for falso ("True" é o padrão), os caracteres de
   controle serão permitidos dentro das strings. Os caracteres de
   controle neste contexto são aqueles com códigos de caracteres no
   intervalo 0--31, incluindo "'\t'" (tab), "'\n'", "'\r'" e "'\0'".

   Se os dados a serem desserializados não forem um documento JSON
   válido, será levantada uma exceção "JSONDecodeError".

   Alterado na versão 3.6: Todos os parâmetros agora são somente-
   nomeado.

   decode(s)

      Retorna a representação Python de *s* (uma instância "str"
      contendo um documento JSON).

      Uma exceção "JSONDecodeError" será levantada se o documento JSON
      fornecido não for válido.

   raw_decode(s)

      Decodifica um documento JSON a partir de *s* (uma "str"
      iniciando com um documento JSON) e retornando uma tupla de 2
      elementos, a representação Python e o índice em *s* onde o
      documento finaliza.

      Isso pode ser usado para decodificar um documento JSON a partir
      de uma string que possa ter dados extras ao final.

class json.JSONEncoder(*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)

   Codificador JSON extensível para estruturas de dados Python.

   Por padrão, possui suporte para os seguintes objetos e tipos:

   +------------------------------------------+-----------------+
   | Python                                   | JSON            |
   |==========================================|=================|
   | dict, frozendict                         | objeto          |
   +------------------------------------------+-----------------+
   | list, tuple                              | array           |
   +------------------------------------------+-----------------+
   | str                                      | string          |
   +------------------------------------------+-----------------+
   | int, float e Enums derivados de int e    | número          |
   | float                                    |                 |
   +------------------------------------------+-----------------+
   | True                                     | true            |
   +------------------------------------------+-----------------+
   | False                                    | false           |
   +------------------------------------------+-----------------+
   | None                                     | null            |
   +------------------------------------------+-----------------+

   Alterado na versão 3.4: Adicionado suporte para classes Enum
   derivadas de int e float.

   Alterado na versão 3.15: Adicionado suporte para "frozendict".

   Para estender isso para reconhecer outros objetos, crie uma
   subclasse e implemente o método "default()" com outro método que
   retorne um objeto serializável para "o" se possível, caso contrário
   deveria chamar a implementação da superclasse (para levantar
   "TypeError").

   Se *skipkeys* é falso (o padrão), então sluma "TypeError" será
   levantada ao tentar codificar as chaves que não são "str", "int",
   "float", "bool" ou "None".  Se *skipkeys* é verdadeiro, esses itens
   são simplesmente pulados.

   Se *ensure_ascii* for verdadeiro (o padrão), a saída terá todos os
   caracteres não ASCII e não imprimíveis recebidos escapados. Se
   *ensure_ascii* for falso, todos os caracteres serão exibidos como
   estão, exceto os caracteres que devem ser escapados: aspas, barra
   invertida e os caracteres de controle U+0000 a U+001F.

   Se *check_circular* é verdadeiro (o padrão), então listas,
   dicionários e objetos codificados personalizados serão verificados
   por referências circulares durante a codificação para prevenir uma
   recursão infinita (que iria causar uma "RecursionError"). Caso
   contrário, nenhuma verificação será feita.

   Se *allow_nan* for verdadeiro (o padrão), então "NaN", "Infinity",
   e "-Infinity" serão codificados como tal. Esse comportamento não é
   compatível com a especificação do JSON, mas é consistente com a
   maioria dos codificadores e decodificadores baseados em JavaScript.
   Caso contrário, será levantada uma "ValueError" para tais pontos
   flutuantes.

   Se *sort_keys* for verdadeiro (padrão: "False"), então a saída dos
   dicionários serão ordenados pela chave; isto é útil para testes de
   regressão para certificar-se que as serializações de JSON possam
   ser comparadas com uma base no dia a dia.

   Se *indent* for um inteiro não negativo ou uma string, então
   elementos de um vetor JSON e membros de objetos terão uma saída
   formatada com este nível de indentação. Um nível de indentação 0,
   negativo ou """" apenas colocará novas linhas. "None" (o padrão)
   seleciona a representação mais compacta. Usando um inteiro positivo
   a indentação terá alguns espaços por nível. Se *indent* for uma
   string (como ""\t""), essa string será usada para indentar cada
   nível.

   Alterado na versão 3.2: Permite strings para *indent*, além de
   inteiros.

   Se especificado, *separators* deve ser uma tupla "(item_separator,
   key_separator)". O padrão é "(', ', ': ')" se *indent* for "None" e
   "(',', ': ')" caso contrário. Para pegar representação JSON mais
   compacta, você deve especificar "(',', ':')" para eliminar espaços
   em branco.

   Alterado na versão 3.4: Usa "(',', ': ')" como padrão se *indent*
   não for "None".

   Se especificado, *default* deve ser uma função para ser chamada
   para objetos que não podem ser serializados de outra forma. Deve
   retornar uma versão codificável JSON do objeto ou levantar uma
   exceção "TypeError". Se não for especificada, "TypeError" é
   levantada.

   Alterado na versão 3.6: Todos os parâmetros agora são somente-
   nomeado.

   default(o)

      Implemente este método em uma subclasse que retorna um objeto
      serializável para *o* ou que chame a implementação base (para
      levantar uma "TypeError").

      Por exemplo, para suporte a iteradores arbitrários, você poderia
      implementar "default()" dessa forma:

         def default(self, o):
            try:
                iterable = iter(o)
            except TypeError:
                pass
            else:
                return list(iterable)
            # Faz o método padrão de classe base levantar a TypeError
            return super().default(o)

   encode(o)

      Retorna uma string representando um JSON a partir da estrutura
      de dados Python, *o*. Por exemplo:

         >>> json.JSONEncoder().encode({"foo": ["bar", "baz"]})
         '{"foo": ["bar", "baz"]}'

   iterencode(o)

      Codifica o objeto dado, *o*, e produz cada representação em
      string assim que disponível.  Por exemplo:

         for chunk in json.JSONEncoder().iterencode(bigobject):
             mysocket.write(chunk)


Exceções
========

exception json.JSONDecodeError(msg, doc, pos)

   Subclasse de "ValueError" com os seguintes atributos adicionais:

   msg

      A mensagem de erro não formatada.

   doc

      O documento JSON sendo analisado.

   pos

      O índice inicial de *doc* em que a análise falhou.

   lineno

      A linha correspondente a *pos*.

   colno

      A coluna correspondente a *pos*.

   Adicionado na versão 3.5.


Conformidade e interoperabilidade entre padrões
===============================================

O formato JSON é especificado pela **RFC 7159** e por ECMA-404. Esta
seção detalha o nível de conformidade deste módulo com a RFC. Para
simplificar, as subclasses "JSONEncoder" e "JSONDecoder", e outros
parâmetros além daqueles explicitamente mencionados, não são
considerados.

Este módulo não está em conformidade com a RFC de forma estrita,
implementando algumas extensões que são JavaScript válidas, mas não
JSON válido. Em particular:

* Os valores de números infinitos e NaN são aceitos e produzidos;

* Nomes repetidos em um objeto são aceitos e apenas o valor do último
  par nome-valor é usado.

Uma vez que a RFC permite que os analisadores compatíveis com a RFC
aceitem textos de entrada que não sejam compatíveis com a RFC, o
desserializador deste módulo é tecnicamente compatível com a RFC nas
configurações padrão.


Codificações de caracteres
--------------------------

A RFC requer que JSON seja representado usando UTF-8, UTF-16 ou
UTF-32, com UTF-8 sendo o padrão recomendado para interoperabilidade
máxima.

Conforme permitido, embora não exigido, pela RFC, o serializador deste
módulo define *ensure_ascii=True* por padrão, escapando a saída para
que as strings resultantes contenham apenas caracteres ASCII
imprimíveis.

Além do parâmetro *ensure_ascii*, este módulo é definido estritamente
em termos de conversão entre objetos Python e "strings Unicode" e,
portanto, não aborda diretamente o problema de codificação de
caracteres.

A RFC proíbe adicionar uma marca de ordem de byte (do inglês *byte
order mark* - BOM) ao início de um texto JSON, e o serializador deste
módulo não adiciona um BOM à sua saída. A RFC permite, mas não exige,
que os desserializadores JSON ignorem um BOM inicial em sua entrada. O
desserializador deste módulo levanta uma "ValueError" quando um BOM
inicial está presente.

A RFC não proíbe explicitamente as strings JSON que contêm sequências
de bytes que não correspondem a caracteres Unicode válidos (por
exemplo, substitutos UTF-16 não emparelhados), mas observa que podem
causar problemas de interoperabilidade. Por padrão, este módulo aceita
e produz (quando presente no original "str") pontos de código para
tais sequências.


Valores numéricos infinitos e NaN
---------------------------------

A RFC não permite a representação de valores infinitos ou numéricos
NaN. Apesar disso, por padrão, este módulo aceita e produz "Infinity",
"-Infinity" e "NaN" como se fossem valores literais de número JSON
válidos:

   >>> # Nenhuma dessas chamadas levanta uma exceção, mas os resultados não são JSON válidos
   >>> json.dumps(float('-inf'))
   '-Infinity'
   >>> json.dumps(float('nan'))
   'NaN'
   >>> # Same when deserializing
   >>> json.loads('-Infinity')
   -inf
   >>> json.loads('NaN')
   nan

No serializador, o parâmetro *allow_nan* pode ser usado para alterar
esse comportamento. No desserializador, o parâmetro *parse_constant*
pode ser usado para alterar esse comportamento.


Nomes repetidos dentro de um objeto
-----------------------------------

A RFC especifica que os nomes em um objeto JSON devem ser exclusivos,
mas não determina como os nomes repetidos em objetos JSON devem ser
tratados. Por padrão, este módulo não levanta uma exceção; em vez
disso, ele ignora tudo, exceto o último par nome-valor para um
determinado nome:

   >>> weird_json = '{"x": 1, "x": 2, "x": 3}'
   >>> json.loads(weird_json)
   {'x': 3}

O parâmetro *object_pairs_hook* pode ser usado para alterar este
comportamento.


Valores não objeto e não vetor de nível superior
------------------------------------------------

A versão antiga de JSON especificada pela obsoleta **RFC 4627** exige
que o valor de nível superior do texto JSON deve ser do tipo object ou
array ("dict" ou "list" Python), e não poderia ser dos tipos null,
boolean, number ou string. **RFC 7159** removeu essa restrição, e esse
módulo não tem nenhuma implementação que faça essa restrição, seja em
seus serializadores, sejam nos desserializadores.

Independentemente, para máxima interoperabilidade, você pode querer
aderir voluntariamente à restrição.


Limitações de implementação
---------------------------

Algumas implementações de desserializadores JSON podem definir limites
em:

* o tamanho de textos JSON aceitos

* o nível máximo de aninhamento de objetos e vetores JSON

* o intervalo e a precisão de números JSON

* o conteúdo e o tamanho máximo de strings JSON

Esse módulo não impõe nenhum limite além daqueles já colocados pelas
estruturas de dados Python ou pelo interpretador Python em si.

Quando serializando para JSON, tenha cuidado com qualquer limitação
nas aplicações que irão consumir seu JSON. Em particular, é comum para
números JSON serem desserializados com números de precisão dupla
definida em IEEE 754 e, portanto, sujeito a limitações de precisão e
de intervalo da representação. Isso é especialmente relevante quando
serializando valores Python "int" de magnitude extremamente grande, ou
quando  serializando instâncias de tipos numéricos "exóticos" como
"decimal.Decimal".


Interface de linha de comando
=============================

**Código-fonte:** Lib/json/tool.py

======================================================================

O módulo "json" pode ser invocado como um script via "python -m json"
para validar e fazer uma impressão bem formatada de objetos JSON. O
submódulo "json.tool" implementa essa interface.

Se os argumentos opcionais "infile" e "outfile" não forem
especificados, "sys.stdin" e "sys.stdout" serão usados
respectivamente:

   $ echo '{"json": "obj"}' | python -m json
   {
       "json": "obj"
   }
   $ echo '{1.2:3.4}' | python -m json
   Expecting property name enclosed in double quotes: line 1 column 2 (char 1)

Alterado na versão 3.5: A saída agora está na mesma ordem da entrada.
Use a opção "--sort-keys" para ordenar a saída de dicionários
alfabeticamente pela chave.

Alterado na versão 3.14: O módulo "json" agora pode ser executado
diretamente como "python -m json". Para retrocompatibilidade, a
invocação da CLI como "python -m json.tool" continua sendo aceita.


Opções de linha de comando
--------------------------

infile

   O arquivo JSON para ser validado ou saída embelezada:

      $ python -m json mp_films.json
      [
          {
              "title": "And Now for Something Completely Different",
              "year": 1971
          },
          {
              "title": "Monty Python and the Holy Grail",
              "year": 1975
          }
      ]

   Se *infile* não é especificado, lê de "sys.stdin".

outfile

   Escreve a saída de *infile* para o *outfile* dado. Caso contrário,
   escreve em "sys.stdout".

--sort-keys

   Ordena a saída de dicionários alfabeticamente pela chave.

   Adicionado na versão 3.5.

--no-ensure-ascii

   Desabilita escape de caracteres não-ascii, veja "json.dumps()" para
   mais informações.

   Adicionado na versão 3.9.

--json-lines

   Analisa cada linha da entrada como um objeto JSON separado.

   Adicionado na versão 3.8.

--indent, --tab, --no-indent, --compact

   Opções mutualmente exclusivas para controle de espaços em branco.

   Adicionado na versão 3.9.

-h, --help

   Exibe a mensagem de ajuda.

-[ Notas de rodapé ]-

[1] Como apresentado na errata para RFC 7159, JSON permite os
    caracteres literais U+2028 (SEPARADOR DE LINHA) e U+2029
    (SEPARADOR DE PARÁGRAFO) em strings, enquanto que JavaScript
    (ECMAScript Edition 5.1) não.
