"plistlib" --- Gera e analisa arquivos Apple ".plist"
*****************************************************

**Código-fonte:** Lib/plistlib.py

======================================================================

Este módulo fornece uma interface para ler e escrever os arquivos
"property listas (lista de propriedades) usados pela Apple,
principalmente no macOS e iOS. Este módulo tem suporte a arquivos
plist binários e XML.

O formato de arquivo de lista de propriedades (".plist") é uma
serialização simples que oferece suporte a tipos básicos de objetos,
como dicionários, listas, números e strings. Normalmente, o objeto de
nível superior é um dicionário ou um dicionário congelado.

Para escrever e analisar um arquivo plist, use as funções "dump()" e
"load()".

Para trabalhar com dados plist em objetos bytes ou string, use
"dumps()" e "loads()".

Os valores podem ser strings, inteiros, floats, booleanos, tuplas,
listas, dicionários (mas somente com chaves de string), objetos
"bytes", "bytearray" ou "datetime.datetime".

Alterado na versão 3.4: Nova API, API antiga descontinuada. Suporte
para plists de formato binário adicionado.

Alterado na versão 3.8: Adicionado suporte para leitura e escrita de
tokens "UID" em plists binários, conforme usado por NSKeyedArchiver e
NSKeyedUnarchiver.

Alterado na versão 3.9: API antiga removida.

Ver também:

  Pagina de manual de PList
     Documentação da Apple sobre o formato de arquivo.

Este módulo define as seguintes funções:

plistlib.load(fp, *, fmt=None, dict_type=dict, aware_datetime=False)

   Lê um arquivo plist. *fp* deve ser um objeto arquivo binário e
   legível. Retorna o objeto raiz desempacotado (que geralmente é um
   dicionário).

   *fmt* é o formato do arquivo e os seguintes valores são válidos:

   * "None": Detecta automaticamente o formato do arquivo

   * "FMT_XML": Formato de arquivo XML

   * "FMT_BINARY": Formato binário plist

   O *dict_type* é o tipo usado para dicionários que são lidos do
   arquivo plist.

   Quando *aware_datetime* for verdadeiro, campos com o tipo
   "datetime.datetime" serão criados como objeto conscientes, com
   "tzinfo" como "datetime.UTC".

   Dados XML para o formato "FMT_XML" são analisados usando o
   analisador sintático Expat de "xml.parsers.expat" -- veja sua
   documentação para possíveis exceções em XML malformado. Elementos
   desconhecidos serão simplesmente ignorados pelo analisador de
   plist.

   O analisador sintático levanta "InvalidFileException" quando o
   arquivo não pode ser analisado.

   Adicionado na versão 3.4.

   Alterado na versão 3.13: O parâmetro somente-nomeado
   *aware_datetime* foi adicionado.

plistlib.loads(data, *, fmt=None, dict_type=dict, aware_datetime=False)

   Carrega um plist de um objeto bytes ou string. Veja "load()" para
   uma explicação dos argumentos nomeados.

   Adicionado na versão 3.4.

   Alterado na versão 3.13: *data* pode ser uma string quando *fmt* é
   igual a "FMT_XML".

plistlib.dump(value, fp, *, fmt=FMT_XML, sort_keys=True, skipkeys=False, aware_datetime=False)

   Escreve *value* em um arquivo plist. *fp* deve ser um objeto
   arquivo binário gravável.

   O argumento *fmt* especifica o formato do arquivo plist e pode ser
   um dos seguintes valores:

   * "FMT_XML": Arquivo plist formatado em XML

   * "FMT_BINARY": Arquivo plist formatado em binário

   Quando *sort_keys* é verdadeiro (o padrão), as chaves dos
   dicionários serão escritas ordenadas no plist, caso contrário, elas
   serão escritas na ordem de iteração do dicionário.

   Quando *skipkeys* é falso (o padrão), a função levanta "TypeError"
   quando uma chave de um dicionário não é uma string, caso contrário,
   tais chaves são ignoradas.

   Quando *aware_datetime* é verdadeiro e qualquer campo com o tipo
   "datetime.datetime" é definido como um objeto consciente, ele será
   convertido para o fuso horário UTC antes de escrevê-lo.

   Uma "TypeError" será levantada se o objeto for de um tipo não
   suportado ou um contêiner que contém objetos de tipos não
   suportados.

   Uma "OverflowError" será levantada para valores inteiros que não
   podem ser representados em arquivos plist (binários).

   Adicionado na versão 3.4.

   Alterado na versão 3.13: O parâmetro somente-nomeado
   *aware_datetime* foi adicionado.

plistlib.dumps(value, *, fmt=FMT_XML, sort_keys=True, skipkeys=False, aware_datetime=False)

   Retorna *value* como um objeto bytes formatado em plist. Veja a
   documentação para "dump()" para uma explicação dos argumentos
   nomeados desta função.

   Adicionado na versão 3.4.

As seguintes classes estão disponíveis:

class plistlib.UID(data)

   Envolve um "int". Isso é usado ao ler ou escrever dados codificados
   NSKeyedArchiver, que contém UID (veja o manual de PList).

   data

      Valor inteiro do UID. Deve estar no intervalo "0 <= data <
      2**64".

   Adicionado na versão 3.8.

As seguintes constantes estão disponíveis:

plistlib.FMT_XML

   O formato XML para arquivos plist.

   Adicionado na versão 3.4.

plistlib.FMT_BINARY

   O formato binário para arquivos plist

   Adicionado na versão 3.4.

O módulo define as seguintes exceções:

exception plistlib.InvalidFileException

   Levantada quando um arquivo não puder ser analisado.

   Adicionado na versão 3.4.


Exemplos
========

Gerando um plist:

   import datetime as dt
   import plistlib

   pl = dict(
       aString = "Doodah",
       aList = ["A", "B", 12, 32.1, [1, 2, 3]],
       aFloat = 0.1,
       anInt = 728,
       aDict = dict(
           anotherString = "<hello & hi there!>",
           aThirdString = "M\xe4ssig, Ma\xdf",
           aTrueValue = True,
           aFalseValue = False,
       ),
       someData = b"<binary gunk>",
       someMoreData = b"<lots of binary gunk>" * 10,
       aDate = dt.datetime.now()
   )
   print(plistlib.dumps(pl).decode())

Analisando um plist:

   import plistlib

   plist = b"""<plist version="1.0">
   <dict>
       <key>foo</key>
       <string>bar</string>
   </dict>
   </plist>"""
   pl = plistlib.loads(plist)
   print(pl["foo"])
