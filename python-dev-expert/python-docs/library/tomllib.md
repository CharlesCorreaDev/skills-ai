"tomllib" --- Analisa arquivos TOML
***********************************

**Código-fonte:** Lib/tomllib

======================================================================

Este módulo fornece uma interface para analisar TOML 1.1.0 (Tom's
Obvious Minimal Language, https://toml.io). Este módulo não oferece
suporte para escrever TOML.

Adicionado na versão 3.11: O módulo foi adicionado com suporte ao TOML
1.0.0.

Alterado na versão 3.15: Adicionado suporte ao TOML 1.1.0. Veja O que
há de novo para detalhes.

Aviso:

  Tenha cuidado quando estiver analisando dados de fontes não-
  confiáveis. Uma string TOML maliciosa pode fazer o decodificador
  consumir recursos consideráveis de CPU e memória. É recomendado
  limitar o tamanho do dado a ser analisado.

Ver também:

  O pacote Tomli-W é um editor de TOML que pode ser usado em conjunto
  com este módulo, fornecendo uma API de escrita familiar aos usuários
  da biblioteca padrão: módulos "marshal" e "pickle".

Ver também:

  O pacote TOML Kit é uma biblioteca TOML de preservação de estilo com
  capacidade de leitura e escrita. É uma substituição recomendada para
  este módulo para edição de arquivos TOML já existentes.

Este módulo define as seguintes funções:

tomllib.load(fp, /, *, parse_float=float)

   Lê um arquivo TOML. O primeiro argumento deve ser um objeto arquivo
   binário e legível. Retorna um "dict". Converte tipos TOML para
   Python usando esta tabela de conversão.

   *parse_float* será chamado com a string de cada ponto flutuante
   (float) do TOML a ser decodificado. Por padrão, isso é equivalente
   a "float(num_str)". Isso pode ser usado para usar outro tipo de
   dados ou analisador sintático para pontos flutuantes do TOML (por
   exemplo, "decimal.Decimal"). O chamável não deve retornar um "dict"
   ou um "list", senão uma exceção "ValueError" é levantada.

   Uma exceção "TOMLDecodeError" será levantada no caso de um
   documento TOML inválido.

tomllib.loads(s, /, *, parse_float=float)

   Carrega TOML de um objeto "str". Retorna um "dict". Converte tipos
   TOML para Python usando esta tabela de conversão. O argumento
   *parse_float* tem o mesmo significado que em "load()".

   Uma exceção "TOMLDecodeError" será levantada no caso de um
   documento TOML inválido.

As seguintes exceções estão disponíveis:

exception tomllib.TOMLDecodeError(msg, doc, pos)

   Subclasse de "ValueError" com os seguintes atributos adicionais:

   msg

      A mensagem de erro não formatada.

   doc

      O documento TOML sendo analisado.

   pos

      O índice de *doc* onde a análise falhou.

   lineno

      A linha correspondente a *pos*.

   colno

      A coluna correspondente a *pos*.

   Alterado na versão 3.14: Adicionados os parâmetros *msg*, *doc* e
   *pos*. Adicionados os atributos "msg", "doc", "pos", "lineno" e
   "colno".

   Descontinuado desde a versão 3.14: A passagem de argumentos
   posicionais de forma livre está descontinuada.


Exemplos
========

Analisando um arquivo TOML:

   import tomllib

   with open("pyproject.toml", "rb") as f:
       data = tomllib.load(f)

Analisando uma string TOML:

   import tomllib

   toml_str = """
   python-version = "3.11.0"
   python-implementation = "CPython"
   """

   data = tomllib.loads(toml_str)


Tabela de conversão
===================

+--------------------+----------------------------------------------------------------------------------------+
| TOML               | Python                                                                                 |
|====================|========================================================================================|
| documento TOML     | dict                                                                                   |
+--------------------+----------------------------------------------------------------------------------------+
| string             | str                                                                                    |
+--------------------+----------------------------------------------------------------------------------------+
| inteiro            | int                                                                                    |
+--------------------+----------------------------------------------------------------------------------------+
| ponto flutuante    | ponto flutuante (configurável com *parse_float*)                                       |
+--------------------+----------------------------------------------------------------------------------------+
| booleano           | bool                                                                                   |
+--------------------+----------------------------------------------------------------------------------------+
| deslocamento de    | datetime.datetime (atributo de "tzinfo" definido com uma instância de                  |
| data-hora          | "datetime.timezone")                                                                   |
+--------------------+----------------------------------------------------------------------------------------+
| data-hora local    | datetime.datetime (atributo de "tzinfo" definido com "None")                           |
+--------------------+----------------------------------------------------------------------------------------+
| data local         | datetime.date                                                                          |
+--------------------+----------------------------------------------------------------------------------------+
| hora local         | datetime.time                                                                          |
+--------------------+----------------------------------------------------------------------------------------+
| array              | lista                                                                                  |
+--------------------+----------------------------------------------------------------------------------------+
| tabela             | dict                                                                                   |
+--------------------+----------------------------------------------------------------------------------------+
| tabela inline      | dict                                                                                   |
+--------------------+----------------------------------------------------------------------------------------+
| array de tabelas   | lista de dicionários                                                                   |
+--------------------+----------------------------------------------------------------------------------------+


Considerações sobre limites e interoperabilidade
================================================

"tomllib" impõe alguns limites aos documentos que consegue processar e
preserva detalhes que outros analisadores de TOML têm permissão para
ignorar. Ao criar arquivos TOML portáteis, utilize apenas recursos
garantidos ou recomendados pelo padrão.

Os detalhes de implementação listados aqui podem mudar em versões
futuras do Python.

Tabelas/dicionários
   A especificação TOML não garante que os pares chave-valor em
   documentos e tabelas TOML estejam em qualquer ordem específica.

   O "tomllib" carrega as entradas de dicionário na ordem em que
   aparecem na fonte.

Inteiros
   O TOML recomenda oferecer suporte a números inteiros no intervalo
   "range(−2**63, 2**63)".

   O "tomllib" utiliza o limite do Python para a conversão de strings
   em inteiros (4300 dígitos por padrão).

Pontos flutuantes
   O TOML recomenda oferecer suporte a, pelo menos, valores IEEE 754
   binary64, o que significa que números com mais de 15 dígitos
   decimais significativos provavelmente serão arredondados.

   "tomllib" usa o "float" do Python por padrão; em muitas plataformas
   comuns, esse é o formato binary64 recomendado. Consulte
   "sys.float_info" para obter detalhes.

Limite aninhado
   O TOML 1.1.0 não recomenda um limite para a profundidade de
   aninhamento entre vetores e tabelas. (Um limite de 100 foi proposto
   para uma versão futura do TOML.)

   Na "tomllib", o nível de aninhamento é limitado principalmente pelo
   "limite de recursão" do Python. Observe que o código que chama
   "tomllib" pode contribuir para esse limite.
